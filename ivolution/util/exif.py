## ===========================================================================
##  NAME:       exif
##  TYPE:       python script
##  CONTENT:    library for parsing EXIF headers
## ===========================================================================
##  AUTHORS:    rft     Robert F. Tobler
## ===========================================================================
##  HISTORY:
##
##  10-Aug-01 11:14:20  rft     last modification
##  09-Aug-01 16:51:05  rft     created
## ===========================================================================

import string

ASCII = 0
BINARY = 1

## ---------------------------------------------------------------------------
##  'Tiff'
##  	This class provides the Exif header as a file-like object and hides
##  	endian-specific data access.
## ---------------------------------------------------------------------------

class Tiff:
    def __init__(self, data, file = None):
	self.data = data

        self.file = file
	self.endpos = len(data)

	self.pos = 0
	if self.data[0:2] == "MM":
	    self.S0 = 1 ; self.S1 = 0
	    self.L0 = 3 ; self.L1 = 2 ; self.L2 = 1 ; self.L3 = 0
	else:
	    self.S0 = 0 ; self.S1 = 1
	    self.L0 = 0 ; self.L1 = 1 ; self.L2 = 2 ; self.L3 = 3

    def seek(self, pos):
	self.pos = pos
        if self.pos > self.endpos:
            self.data += self.file.read( self.endpos - self.pos )
        
    def tell(self):
	return self.pos

    def read(self, len):
	old_pos = self.pos
	self.pos = self.pos + len
        if self.pos > self.endpos:
            self.data += self.file.read( self.endpos - self.pos )
	return self.data[old_pos:self.pos]

    def byte(self, signed = 0):
    	pos = self.pos
	self.pos = pos + 1
        if self.pos > self.endpos:
            self.data += self.file.read( self.endpos - self.pos )
	hi = ord(self.data[pos])
	if hi > 127 and signed: hi = hi - 256
	return hi

    def short(self, signed = 0):
	pos = self.pos
	self.pos = pos + 2
        if self.pos > self.endpos:
            self.data += self.file.read( self.endpos - self.pos )
	hi = ord(self.data[pos+self.S1])
	if hi > 127 and signed: hi = hi - 256
	return (hi<<8)|ord(self.data[pos+self.S0])

    def long(self, signed = 0):
	pos = self.pos
	self.pos = pos + 4
        if self.pos > self.endpos:
            self.data += self.file.read( self.endpos - self.pos )
	hi = ord(self.data[pos+self.L3])
	if hi > 127 and not signed: hi = long(hi)
	return (hi<<24) | (ord(self.data[pos+self.L2])<<16) \
	    | (ord(self.data[pos+self.L1])<<8) | ord(self.data[pos+self.L0])

## ---------------------------------------------------------------------------
##  'Type', 'Type...'
##  	A small hierarchy of objects that knows how to read each type of tag
##  	field from a tiff file, and how to pretty-print each type of tag.
##
##  	The method 'read' is used to read a tag with a given count from the
##  	supplied tiff file.
##
##  	The method 'str_table' is used to pretty-print the value table of a
##  	tag if no special format for this tag is present.
## ---------------------------------------------------------------------------

class Type:
    def str_table(self, table):
	result = []
	for val in table: result.append(self.str_value(val))
	return string.join(result, ", ")
    def str_value(self, val):
	return str(val)

class TypeByte(Type):
    def __init__(self): self.name = "BYTE" ; self.len = 1
    def read(self, tiff, count):
    	result = []
        for i in range(0, count): table.append(tiff.byte())
	return table

class TypeAscii:
    def __init__(self): self.name = "ASCII" ; self.len = 1
    def read(self, tiff, count):
	return tiff.read(count-1)
    def str_table(self, table):
	return string.strip(table)

class TypeShort(Type):
    def __init__(self): self.name = "SHORT" ; self.len = 2
    def read(self, tiff, count):
	table = []
	for i in range(0, count): table.append(tiff.short())
	return table

class TypeLong(Type):
    def __init__(self): self.name = "LONG" ; self.len = 4
    def read(self, tiff, count):
	table = []
	for i in range(0, count): table.append(tiff.long())
	return table

class TypeRatio(Type):
    def __init__(self): self.name = "RATIO" ; self.len = 8
    def read(self, tiff, count):
	table = []
	for i in range(0, count): table.append((tiff.long(), tiff.long()))
	return table
    def str_value(self, val):
	return "%d/%d" %(val[0], val[1])

class TypeSByte(Type):
    def __init__(self): self.name = "SBYTE" ; self.len = 1
    def read(self, tiff, count):
    	table = []
	for i in range(0, count): table.append(tiff.byte(signed=1))
	return table

class TypeUndef(TypeByte):
    def __init__(self): self.name = "UNDEF" ; self.len = 1
    def read(self, tiff, count):
	return tiff.read(count)
    def str_table(self, table):
        result = map( lambda x: str(ord(x)), table )
        # this next line is somehow much more efficient than using str()
	return '[ ' + string.join( result, ',' ) + ' ]'

class TypeSShort(Type):
    def __init__(self): self.name = "SSHORT" ; self.len = 2
    def read(self, tiff, count):
	table = []
	for i in range(0, count): table.append(tiff.short(signed=1))
	return table

class TypeSLong(Type):
    def __init__(self): self.name = "SLONG" ; self.len = 4
    def read(self, tiff, count):
	table = []
	for i in range(0, count): table.append(tiff.short(signed=1))
	return table

class TypeSRatio(TypeRatio):
    def __init__(self): self.name = "SRATIO" ; self.len = 8
    def read(self, tiff, count):
	table = []
	for i in range(0, count):
	    table.append((tiff.long(signed=1), tiff.long(signed=1)))
	return table

class TypeFloat:
    def __init__(self): self.name = "FLOAT" ; self.len = 4
    def read(self, tiff, count):
	return tiff.read(4 * count)

class TypeDouble:
    def __init__(self): self.name = "DOUBLE" ; self.len = 8
    def read(self, tiff, count):
	return tiff.read(8 * count)

TYPE_MAP = {
	1:	TypeByte(),
	2:	TypeAscii(),
	3:	TypeShort(),
	4:	TypeLong(),
	5:	TypeRatio(),
	6:	TypeSByte(),
	7:	TypeUndef(),
	8:	TypeSShort(),
	9:	TypeSLong(),
	10:	TypeSRatio(),
	11:	TypeFloat(),
	12:	TypeDouble(),
}

## ---------------------------------------------------------------------------
##  'Tag'
##  	A tag knows about its name and an optional format.
## ---------------------------------------------------------------------------

class Tag:
    def __init__(self, name, format = None):
	self.name = name
	self.format = format

## ---------------------------------------------------------------------------
##  'Format', 'Format...'
##  	A small hierarchy of objects that provide special formats for certain
##  	tags in the EXIF standard.
##
##  	The method 'str_table' is used to pretty-print the value table of a
##  	tag. It gets the table of tags that have already been parsed as a
##  	parameter in order to handle vendor specific extensions.
## ---------------------------------------------------------------------------

class Format:
    def str_table(self, table, value_map):
	result = []
	for val in table: result.append(self.str_value(val))
	return string.join(result, ", ")

class FormatMap:
    def __init__(self, map, make_ext = {}):
	self.map = map
	self.make_ext = make_ext
    def str_table(self, table, value_map):
	if len(table) == 1:
	    key = table[0]
	else:
	    key = table
	value = self.map.get(key)
	if not value:
	    make = value_map.get("Make")
	    if make: value = self.make_ext.get(make,{}).get(key)
	    if not value: value = `key`
	return value

class FormatRatioAsFloat(Format):
    def str_value(self, val):
	if val[1] == 0: return "0.0"
	return "%g" % (val[0]/float(val[1]))

class FormatRatioAsBias(Format):
    def str_value(self, val):
	if val[1] == 0: return "0.0"
	if val[0] > 0: return "+%3.1f" % (val[0]/float(val[1]))
	if val[0] < 0: return "-%3.1f" % (-val[0]/float(val[1]))
	return "0.0"

def format_time(t):
    if t > 0.5: return "%g" % t
    if t > 0.1: return "1/%g" % (0.1*int(10/t+0.5))
    return "1/%d" % int(1/t+0.5)

class FormatRatioAsTime(Format):
    def str_value(self, val):
	if val[1] == 0: return "0.0"
    	return format_time(val[0]/float(val[1]))

class FormatRatioAsApexTime(Format):
    def str_value(self, val):
	if val[1] == 0: return "0.0"
	return format_time(pow(0.5, val[0]/float(val[1])))

## ---------------------------------------------------------------------------
##  The EXIF parser is completely table driven.
## ---------------------------------------------------------------------------

## ---------------------------------------------------------------------------
##  Nikon 99x MakerNote Tags http://members.tripod.com/~tawba/990exif.htm
## ---------------------------------------------------------------------------
NIKON_99x_MAKERNOTE_TAG_MAP = {
	0x0001:	Tag('MN_0x0001'),
	0x0002:	Tag('MN_ISOSetting'),
	0x0003:	Tag('MN_ColorMode'),
	0x0004:	Tag('MN_Quality'),
	0x0005:	Tag('MN_Whitebalance'),
	0x0006:	Tag('MN_ImageSharpening'),
	0x0007:	Tag('MN_FocusMode'),
	0x0008:	Tag('MN_FlashSetting'),
	0x000A:	Tag('MN_0x000A'),
	0x000F:	Tag('MN_ISOSelection'),
	0x0080:	Tag('MN_ImageAdjustment'),
	0x0082:	Tag('MN_AuxiliaryLens'),
	0x0085:	Tag('MN_ManualFocusDistance',  	FormatRatioAsFloat() ),
	0x0086:	Tag('MN_DigitalZoomFactor',    	FormatRatioAsFloat() ),
	0x0088:	Tag('MN_AFFocusPosition',
		FormatMap({
			'\00\00\00\00': 'Center',
			'\00\01\00\00': 'Top',
			'\00\02\00\00': 'Bottom',
			'\00\03\00\00': 'Left',
			'\00\04\00\00': 'Right',
		})),
	0x008f:	Tag('MN_0x008f'),
	0x0094:	Tag('MN_Saturation',
		FormatMap({
			0: '0',
			1: '1',
			2: '2',
			-3: 'B&W',
			-2: '-2',
			-1: '-1',
		})),
	0x0095:	Tag('MN_NoiseReduction'),
	0x0010:	Tag('MN_DataDump'),
	0x0011:	Tag('MN_0x0011'),
	0x0e00:	Tag('MN_0x0e00'),
}

## ---------------------------------------------------------------------------
##  'MakerNote...'
##  	This currently only parses Nikon E990, and Nikon E995 MakerNote tags.
##  	Additional objects with a 'parse' function can be placed here to add
##  	support for other cameras. This function adds the pretty-printed
##  	information in the MakerNote to the 'value_map' that is supplied.
## ---------------------------------------------------------------------------

class MakerNoteTags:
    def __init__(self, tag_map):
	self.tag_map = tag_map
    def parse(self, tiff, mode, tag_len, value_map):
	num_entries = tiff.short()
	if verbose_opt: print num_entries, 'tags'
	for field in range(0, num_entries):
	    parse_tag(tiff, mode, value_map, self.tag_map)

NIKON_99x_MAKERNOTE = MakerNoteTags(NIKON_99x_MAKERNOTE_TAG_MAP)

## ---------------------------------------------------------------------------
##  'MAKERNOTE_MAP'
##  	Interpretation of the MakerNote tag indexed by 'Make', 'Model' pairs.
## ---------------------------------------------------------------------------

MAKERNOTE_MAP = {
	('NIKON', 'E990'):  NIKON_99x_MAKERNOTE,
	('NIKON', 'E995'):  NIKON_99x_MAKERNOTE,
}

## ---------------------------------------------------------------------------
##  'TAG_MAP'
##  	This is the map of tags that drives the parser.
## ---------------------------------------------------------------------------

TAG_MAP = {
	0x00fe: Tag('NewSubFileType'),
	0x0100: Tag('ImageWidth'),
	0x0101: Tag('ImageLength'),
	0x0102: Tag('BitsPerSample'),
	0x0103: Tag('Compression'),
	0x0106: Tag('PhotometricInterpretation'),
	0x010a: Tag('FillOrder'),
	0x010d: Tag('DocumentName'),
	0x010e: Tag('ImageDescription'),
	0x010f: Tag('Make'),
	0x0110: Tag('Model'),
	0x0111: Tag('StripOffsets'),
	0x0112: Tag('Orientation'),
	0x0115: Tag('SamplesPerPixel'),
	0x0116: Tag('RowsPerStrip'),
	0x0117: Tag('StripByteCounts'),
	0x011a: Tag('XResolution'),
	0x011b: Tag('YResolution'),
	0x011c: Tag('PlanarConfiguration'),
	0x0128: Tag('ResolutionUnit',
		FormatMap({
			1:	'Not Absoulute',
			2:	'Inch',
			3:	'Centimeter'
		})),
	0x012d: Tag('TransferFunction'),
	0x0131: Tag('Software'),
	0x0132: Tag('DateTime'),
	0x013b: Tag('Artist'),
	0x013e: Tag('WhitePoint'),
	0x013f: Tag('PrimaryChromaticities'),
	0x0142: Tag('TileWidth'),
	0x0143: Tag('TileLength'),
	0x0144: Tag('TileOffsets'),
	0x0145: Tag('TileByteCounts'),
	0x014a: Tag('SubIFDs'),
	0x0156: Tag('TransferRange'),
	0x015b: Tag('JPEGTables'),
	0x0201: Tag('JPEGInterchangeFormat'),
	0x0202: Tag('JPEGInterchangeFormatLength'),
	0x0211: Tag('YCbCrCoefficients'),
	0x0212: Tag('YCbCrSubSampling'),
	0x0213: Tag('YCbCrPositioning'),
	0x0214: Tag('ReferenceBlackWhite'),
	0x828d: Tag('CFARepeatPatternDim'),
	0x828e: Tag('CFAPattern'),
	0x828f: Tag('BatteryLevel'),
	0x8298: Tag('Copyright'),
	0x829a: Tag('ExposureTime', 	    	FormatRatioAsTime() ),
	0x829d: Tag('FNumber',	    	    	FormatRatioAsFloat() ),
	0x83bb: Tag('IPTC_NAA'),
	0x8773: Tag('InterColorProfile'),
	0x8822: Tag('ExposureProgram',
		    FormatMap({
			0:	'Unidentified',
			1:	'Manual',
			2:	'Program Normal',
			3:	'Aperture Priority',
			4:	'Shutter Priority',
			5:	'Program Creative',
			6:	'Program Action',
			7:	'Portrait Mode',
			8:	'Landscape Mode',
		    })),
	0x8824: Tag('SpectralSensitivity'),
	0x8825: Tag('GPSInfo'),
	0x8827: Tag('ISOSpeedRatings'),
	0x8828: Tag('OECF'),
	0x8829: Tag('Interlace'),
	0x882a: Tag('TimeZoneOffset'),
	0x882b: Tag('SelfTimerMode'),
	0x8769: Tag('ExifOffset'),
	0x9000: Tag('ExifVersion'),
	0x9003: Tag('DateTimeOriginal'),
	0x9004: Tag('DateTimeDigitized'),
	0x9101: Tag('ComponentsConfiguration'),
	0x9102: Tag('CompressedBitsPerPixel'),
	0x9201: Tag('ShutterSpeedValue',	FormatRatioAsApexTime() ),
	0x9202: Tag('ApertureValue',   	    	FormatRatioAsFloat() ),
	0x9203: Tag('BrightnessValue'),
	0x9204: Tag('ExposureBiasValue',	FormatRatioAsBias() ),
	0x9205: Tag('MaxApertureValue',	    	FormatRatioAsFloat() ),
	0x9206: Tag('SubjectDistance'),
	0x9207: Tag('MeteringMode',
		FormatMap({
			0:  	'Unidentified',
			1:	'Average',
			2:	'CenterWeightedAverage',
			3:	'Spot',
			4:	'MultiSpot',
		},
    	    	make_ext = {
	    	    	'NIKON':    { 5: 'Matrix' },
    	    	})),
	0x9208: Tag('LightSource',
		FormatMap({
                        0:   'Unknown',
                        1:   'Daylight',
                        2:   'Fluorescent',
                        3:   'Tungsten',
                        10:  'Flash',
                        17:  'Standard light A',
                        18:  'Standard light B',
                        19:  'Standard light C',
                        20:  'D55',
                        21:  'D65',
                        22:  'D75',
                        255: 'Other'
		})),
	0x9209: Tag('Flash',
		FormatMap({
			0:	'no',
			1:	'fired',
			5:	'fired (?)', # no return sensed
			7:	'fired (!)', # return sensed
			9:	'fill fired',
			13:	'fill fired (?)',
			15:	'fill fired (!)',
			16:	'off',
			24:	'auto off',
			25:	'auto fired',
			29:	'auto fired (?)',
			31:	'auto fired (!)',
			32:	'not available'
		})),
	0x920a: Tag('FocalLength',  	    	FormatRatioAsFloat()),
	0x920b: Tag('FlashEnergy'),
	0x920c: Tag('SpatialFrequencyResponse'),
	0x920d: Tag('Noise'),
	0x920e: Tag('FocalPlaneXResolution'),
	0x920f: Tag('FocalPlaneYResolution'),
	0x9210: Tag('FocalPlaneResolutionUnit',
		FormatMap({
			1:  	'Inch',
			2:  	'Meter',
			3:  	'Centimeter',
			4:  	'Millimeter',
			5:  	'Micrometer',
		})),
	0x9211: Tag('ImageNumber'),
	0x9212: Tag('SecurityClassification'),
	0x9213: Tag('ImageHistory'),
	0x9214: Tag('SubjectLocation'),
	0x9215: Tag('ExposureIndex'),
	0x9216: Tag('TIFF_EPStandardID'),
	0x9217: Tag('SensingMethod'),
	0x927c: Tag('MakerNote'),
	0xa001: Tag('ColorSpace'),
	0xa002: Tag('ExifImageWidth'),
	0xa003: Tag('ExifImageHeight'),
	0xa005: Tag('Interoperability_IFD_Pointer'),
}

def parse_tag(tiff, mode, value_map, tag_map):
    tag_id = tiff.short()
    type_no = tiff.short()
    count = tiff.long()

    tag = tag_map.get(tag_id)
    if not tag: tag = Tag("Tag0x%x" % tag_id)

    type = TYPE_MAP[type_no]

    if verbose_opt:
	print "%30s:" % tag.name,
	if verbose_opt > 1: print "%6s %3d" % (type.name, count),

    pos = tiff.tell()
    tag_len = type.len * count
    if tag_len > 4:
	tag_offset = tiff.long()
	tiff.seek(tag_offset)
	if verbose_opt > 1: print "@%03x :" % tag_offset,
    else:
	if verbose_opt > 1: print "     :",
    
    if tag.name == 'MakerNote':
	makernote = MAKERNOTE_MAP.get((value_map['Make'],value_map['Model']))
	if makernote:
	    makernote.parse(tiff, mode, tag_len, value_map)
	    value_table = None
	else:
	    value_table = type.read(tiff, count)
    else:
	value_table = type.read(tiff, count)

    if value_table:
    	if mode == ASCII:
	    if tag.format:
		val = tag.format.str_table(value_table, value_map)
	    else:
		val = type.str_table(value_table)
	else:
	    val = value_table
	value_map[tag.name] = val
	if verbose_opt:
	    if value_map.has_key(tag.name): print val,
	    print

    tiff.seek(pos+4)

def parse_ifd(tiff, mode, offset, value_map):
    tiff.seek(offset)
    num_entries = tiff.short()
    if verbose_opt > 1:
	print "%30s:        %3d @%03x" % ("IFD", num_entries, offset)
    for field in range(0, num_entries):
	parse_tag(tiff, mode, value_map, TAG_MAP)
    offset = tiff.long()
    return offset

def parse_tiff(tiff, mode):
    value_map = {}
    order = tiff.read(2)
    if tiff.short() == 42:
	offset = tiff.long()
	while offset > 0:
	    offset = parse_ifd(tiff, mode, offset, value_map)

	    if offset == 0: 	    	    	    # special handling to get
		if value_map.has_key('ExifOffset'): # next EXIF IFD
	    	    offset = value_map['ExifOffset']
		    if mode == ASCII:
			offset = int(offset)
		    else:
			offset = offset[0]
		    del value_map['ExifOffset']
    return value_map


def parse_tiff_fortiff(tiff, mode):

    """Parse a real tiff file, not an EXIF tiff file."""

    value_map = {}
    order = tiff.read(2)
    if tiff.short() == 42:
        offset = tiff.long()

        # build a list of small tags, we don't want to parse the huge stuff
        stags = []
        while offset > 0:
            tiff.seek(offset)
            num_entries = tiff.short()
    
            if verbose_opt > 1:
                print "%30s:        %3d @%03x" % ("IFD", num_entries, offset)
            
            for field in range(0, num_entries):
                pos = tiff.tell()
                
                tag_id = tiff.short()
                type_no = tiff.short()
                length = tiff.long()
                valoff = tiff.long()
                #print TAG_MAP[ tag_id ].name, length

                if tag_id == 0x8769:
		    if mode == ASCII:
			valoff = int(valoff)
		    else:
			valoff = valoff[0]
                    stags += [ (tag_id, valoff) ]

                elif length < 1024:
                    stags += [ (tag_id, pos) ]

            offset = tiff.long()

            # IMPORTANT: we read the 0st ifd only for this.
            # The second is reserved for the thumbnail, whatever is in there
            # we ignore.
            break
        
        for p in stags:
            (tag_id, pos) = p
                
            if tag_id == 0x8769:
                parse_ifd(tiff, mode, pos, value_map)
            else:
                tiff.seek( pos )
                parse_tag(tiff, mode, value_map, TAG_MAP)

    return value_map


## ---------------------------------------------------------------------------
##  'parse'
##  	This is the function for parsing the EXIF structure in a file given
##  	the path of the file.
##  	The function returns a map which contains all the exif tags that
##  	were found, indexed by the name of the tag. The value of each tag
##  	is already converted to a nicely formatted string.
## ---------------------------------------------------------------------------
def parse(path_name, verbose = 0, mode = 0):
    global verbose_opt
    verbose_opt = verbose
    try:
	file = open(path_name, "rb")
	data = file.read(12)
	if data[0:4] == '\377\330\377\341' and data[6:10] == 'Exif':
            # JPEG
	    length = ord(data[4]) * 256 + ord(data[5])
	    if verbose > 1:
                print '%30s:  %d' % ("EXIF header length",length)
	    tiff = Tiff(file.read(length-8))
	    value_map = parse_tiff(tiff, mode)
	elif data[0:2] in [ 'II', 'MM' ] and ord(data[2]) == 42:
            # Tiff
            tiff = Tiff(data,file)
            tiff.seek(0)
            value_map = parse_tiff_fortiff(tiff, mode)
        else:
            # Some other file format, sorry.
            value_map = {}

	file.close()
    except IOError:
	value_map = {}

    return value_map

## ===========================================================================
