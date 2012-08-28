# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 30 2011)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class IvolutionTemplate
###########################################################################

class IvolutionTemplate ( wx.Frame ):
    
    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Ivolution", pos = wx.DefaultPosition, size = wx.Size( 250,620 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
        
        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        
        maingrid = wx.FlexGridSizer( 3, 1, 0, 0 )
        maingrid.SetFlexibleDirection( wx.BOTH )
        maingrid.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
        
        titlelayout = wx.BoxSizer( wx.HORIZONTAL )
        
        titlelayout.SetMinSize( wx.Size( 50,50 ) ) 
        logobox = wx.BoxSizer( wx.VERTICAL )
        
        logobox.SetMinSize( wx.Size( 50,50 ) ) 
        self.logo = wx.StaticBitmap( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 50,50 ), 0 )
        logobox.Add( self.logo, 1, wx.ALL, 5 )
        
        titlelayout.Add( logobox, 1, wx.FIXED_MINSIZE, 5 )
        
        self.title = wx.StaticText( self, wx.ID_ANY, u"Ivolution", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE|wx.ALIGN_LEFT )
        self.title.Wrap( -1 )
        self.title.SetFont( wx.Font( 16, 71, 90, 92, False, wx.EmptyString ) )
        
        titlelayout.Add( self.title, 3, wx.ALIGN_LEFT|wx.ALL|wx.EXPAND, 5 )
        
        maingrid.Add( titlelayout, 1, wx.EXPAND, 5 )
        
        settingsbox = wx.FlexGridSizer( 2, 1, 0, 0 )
        settingsbox.SetFlexibleDirection( wx.BOTH )
        settingsbox.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
        
        requiredbox = wx.FlexGridSizer( 3, 1, 0, 0 )
        requiredbox.SetFlexibleDirection( wx.BOTH )
        requiredbox.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
        
        self.title = wx.StaticText( self, wx.ID_ANY, u"Required parameters:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.title.Wrap( -1 )
        self.title.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
        
        requiredbox.Add( self.title, 0, wx.ALL, 5 )
        
        inputbox = wx.FlexGridSizer( 2, 1, 0, 0 )
        inputbox.SetFlexibleDirection( wx.BOTH )
        inputbox.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
        
        self.inputtitle = wx.StaticText( self, wx.ID_ANY, u"Choose your input folder:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.inputtitle.Wrap( -1 )
        inputbox.Add( self.inputtitle, 0, wx.ALL, 5 )
        
        inputchooserbox = wx.FlexGridSizer( 1, 2, 0, 0 )
        inputchooserbox.SetFlexibleDirection( wx.BOTH )
        inputchooserbox.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
        
        self.inputchooserbutton = wx.Button( self, wx.ID_ANY, u"..", wx.DefaultPosition, wx.Size( 30,25 ), 0 )
        inputchooserbox.Add( self.inputchooserbutton, 1, wx.ALL, 5 )
        
        self.inputtextbox = wx.StaticText( self, wx.ID_ANY, u"/home/jll/Documents/Ivolutionnnn", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.inputtextbox.Wrap( -1 )
        inputchooserbox.Add( self.inputtextbox, 0, wx.ALL, 5 )
        
        inputbox.Add( inputchooserbox, 1, wx.EXPAND, 5 )
        
        requiredbox.Add( inputbox, 1, wx.EXPAND, 5 )
        
        outputbox = wx.FlexGridSizer( 2, 1, 0, 0 )
        outputbox.SetFlexibleDirection( wx.BOTH )
        outputbox.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
        
        self.outputtitle = wx.StaticText( self, wx.ID_ANY, u"Choose your output folder:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.outputtitle.Wrap( -1 )
        outputbox.Add( self.outputtitle, 0, wx.ALL, 5 )
        
        outputchooserbox = wx.FlexGridSizer( 1, 2, 0, 0 )
        outputchooserbox.SetFlexibleDirection( wx.BOTH )
        outputchooserbox.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
        
        self.outputchooserbutton = wx.Button( self, wx.ID_ANY, u"..", wx.DefaultPosition, wx.Size( 30,25 ), 0 )
        outputchooserbox.Add( self.outputchooserbutton, 0, wx.ALL, 5 )
        
        self.outputchoosertext = wx.StaticText( self, wx.ID_ANY, u"/home/jll/Videos", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.outputchoosertext.Wrap( -1 )
        outputchooserbox.Add( self.outputchoosertext, 0, wx.ALL, 5 )
        
        outputbox.Add( outputchooserbox, 1, wx.EXPAND, 5 )
        
        requiredbox.Add( outputbox, 1, wx.EXPAND, 5 )
        
        settingsbox.Add( requiredbox, 1, wx.EXPAND, 5 )
        
        optionalbox = wx.FlexGridSizer( 5, 1, 0, 0 )
        optionalbox.SetFlexibleDirection( wx.BOTH )
        optionalbox.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
        
        self.title1 = wx.StaticText( self, wx.ID_ANY, u"Optional parameters:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.title1.Wrap( -1 )
        self.title1.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
        
        optionalbox.Add( self.title1, 0, wx.ALL, 5 )
        
        typefacebox = wx.FlexGridSizer( 2, 1, 0, 0 )
        typefacebox.SetFlexibleDirection( wx.BOTH )
        typefacebox.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
        
        self.typefacetext  = wx.StaticText( self, wx.ID_ANY, u"Type of face:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.typefacetext .Wrap( -1 )
        typefacebox.Add( self.typefacetext , 0, wx.ALL, 5 )
        
        typefacelistChoices = [ u"frontal_face", u"profile_face" ]
        self.typefacelist = wx.ComboBox( self, wx.ID_ANY, u"frontal_face", wx.DefaultPosition, wx.DefaultSize, typefacelistChoices, wx.CB_READONLY )
        typefacebox.Add( self.typefacelist, 0, wx.ALL, 5 )
        
        optionalbox.Add( typefacebox, 1, wx.EXPAND, 5 )
        
        videospeedbox = wx.FlexGridSizer( 2, 1, 0, 0 )
        videospeedbox.SetFlexibleDirection( wx.BOTH )
        videospeedbox.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
        
        self.videospeedtext = wx.StaticText( self, wx.ID_ANY, u"Video Speed:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.videospeedtext.Wrap( -1 )
        videospeedbox.Add( self.videospeedtext, 0, wx.ALL, 5 )
        
        videospeedlistChoices = [ u"slow", u"medium", u"fast" ]
        self.videospeedlist = wx.ComboBox( self, wx.ID_ANY, u"medium", wx.DefaultPosition, wx.DefaultSize, videospeedlistChoices, wx.CB_READONLY )
        videospeedbox.Add( self.videospeedlist, 0, wx.ALL, 5 )
        
        optionalbox.Add( videospeedbox, 1, wx.EXPAND, 5 )
        
        videomodebox = wx.FlexGridSizer( 2, 1, 0, 0 )
        videomodebox.SetFlexibleDirection( wx.BOTH )
        videomodebox.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
        
        self.videomodetext = wx.StaticText( self, wx.ID_ANY, u"Choose your prefered mode:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.videomodetext.Wrap( -1 )
        videomodebox.Add( self.videomodetext, 0, wx.ALL, 5 )
        
        videomodechoices = wx.FlexGridSizer( 1, 2, 0, 0 )
        videomodechoices.SetFlexibleDirection( wx.BOTH )
        videomodechoices.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
        
        self.cropmode = wx.RadioButton( self, wx.ID_ANY, u"Crop Mode", wx.DefaultPosition, wx.DefaultSize, wx.RB_GROUP )
        self.cropmode.SetValue( True ) 
        videomodechoices.Add( self.cropmode, 0, wx.ALL, 5 )
        
        self.conservativemode  = wx.RadioButton( self, wx.ID_ANY, u"Conservative Mode", wx.DefaultPosition, wx.DefaultSize, 0 )
        videomodechoices.Add( self.conservativemode , 0, wx.ALL, 5 )
        
        videomodebox.Add( videomodechoices, 1, wx.EXPAND, 5 )
        
        optionalbox.Add( videomodebox, 1, wx.EXPAND, 5 )
        
        filemethodbox = wx.FlexGridSizer( 2, 1, 0, 0 )
        filemethodbox.SetFlexibleDirection( wx.BOTH )
        filemethodbox.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
        
        self.filemethodtext = wx.StaticText( self, wx.ID_ANY, u"Choose your prefered method:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.filemethodtext.Wrap( -1 )
        filemethodbox.Add( self.filemethodtext, 0, wx.ALL, 5 )
        
        videomodechoices = wx.FlexGridSizer( 1, 2, 0, 0 )
        videomodechoices.SetFlexibleDirection( wx.BOTH )
        videomodechoices.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
        
        self.namemode = wx.RadioButton( self, wx.ID_ANY, u"File name", wx.DefaultPosition, wx.DefaultSize, wx.RB_GROUP )
        self.namemode.SetValue( True ) 
        videomodechoices.Add( self.namemode, 0, wx.ALL, 5 )
        
        self.exifmode  = wx.RadioButton( self, wx.ID_ANY, u"EXIF metadata", wx.DefaultPosition, wx.DefaultSize, 0 )
        videomodechoices.Add( self.exifmode , 0, wx.ALL, 5 )
        
        filemethodbox.Add( videomodechoices, 1, wx.EXPAND, 5 )
        
        optionalbox.Add( filemethodbox, 1, wx.EXPAND, 5 )
        
        settingsbox.Add( optionalbox, 1, wx.EXPAND, 5 )
        
        maingrid.Add( settingsbox, 1, wx.EXPAND, 5 )
        
        commandbox = wx.FlexGridSizer( 2, 1, 0, 0 )
        commandbox.SetFlexibleDirection( wx.BOTH )
        commandbox.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
        
        buttonsbox = wx.FlexGridSizer( 1, 2, 0, 0 )
        buttonsbox.SetFlexibleDirection( wx.BOTH )
        buttonsbox.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
        
        self.startbutton = wx.Button( self, wx.ID_ANY, u"Create Movie!", wx.DefaultPosition, wx.DefaultSize, 0 )
        buttonsbox.Add( self.startbutton, 0, wx.ALL, 5 )
        
        self.stopbutton = wx.Button( self, wx.ID_ANY, u"Stop processing", wx.DefaultPosition, wx.DefaultSize, 0 )
        buttonsbox.Add( self.stopbutton, 0, wx.ALL, 5 )
        
        commandbox.Add( buttonsbox, 1, wx.EXPAND, 5 )
        
        self.progressgauge  = wx.Gauge( self, wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL )
        commandbox.Add( self.progressgauge , 0, wx.ALL|wx.EXPAND, 5 )
        
        maingrid.Add( commandbox, 1, wx.EXPAND, 5 )
        
        self.SetSizer( maingrid )
        self.Layout()
        self.sb  = self.CreateStatusBar( 2, wx.ST_SIZEGRIP, wx.ID_ANY )
        self.menubar = wx.MenuBar( 0 )
        self.filemenu = wx.Menu()
        self.menuhelp = wx.MenuItem( self.filemenu, wx.ID_ANY, u"Help"+ u"\t" + u"CTRL + h", wx.EmptyString, wx.ITEM_NORMAL )
        self.filemenu.AppendItem( self.menuhelp )
        
        self.menuabout = wx.MenuItem( self.filemenu, wx.ID_ANY, u"About"+ u"\t" + u"CTRL + F12", wx.EmptyString, wx.ITEM_NORMAL )
        self.filemenu.AppendItem( self.menuabout )
        
        self.menuexit = wx.MenuItem( self.filemenu, wx.ID_ANY, u"Exit"+ u"\t" + u"CTRL + Q", wx.EmptyString, wx.ITEM_NORMAL )
        self.filemenu.AppendItem( self.menuexit )
        
        self.menubar.Append( self.filemenu, u"File" ) 
        
        self.SetMenuBar( self.menubar )
        
        
        self.Centre( wx.BOTH )
        
        # Connect Events
        self.inputchooserbutton.Bind( wx.EVT_BUTTON, self.on_input )
        self.outputchooserbutton.Bind( wx.EVT_BUTTON, self.on_output )
        self.startbutton.Bind( wx.EVT_BUTTON, self.on_start )
        self.stopbutton.Bind( wx.EVT_BUTTON, self.on_stop )
        self.Bind( wx.EVT_MENU, self.on_help, id = self.menuhelp.GetId() )
        self.Bind( wx.EVT_MENU, self.on_about, id = self.menuabout.GetId() )
        self.Bind( wx.EVT_MENU, self.on_exit, id = self.menuexit.GetId() )
    
    def __del__( self ):
        pass
    
    
    # Virtual event handlers, overide them in your derived class
    def on_input( self, event ):
        event.Skip()
    
    def on_output( self, event ):
        event.Skip()
    
    def on_start( self, event ):
        event.Skip()
    
    def on_stop( self, event ):
        event.Skip()
    
    def on_help( self, event ):
        event.Skip()
    
    def on_about( self, event ):
        event.Skip()
    
    def on_exit( self, event ):
        event.Skip()
    

