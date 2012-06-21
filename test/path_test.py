from facemovie import Facemovie
from facemovie import FaceParams

in_fo = "data/inputs/samples"
#in_fo = "data/inputs/moi"
out_fo = "data/plop/caca/test.mkv"

xml_fo = "haarcascades"

face_params = FaceParams.FaceParams(xml_fo, 'frontal_face')

facemovie = Facemovie.FaceMovie(in_fo, out_fo, face_params)
facemovie.check_out_name(out_fo)

print facemovie.out_path, facemovie.out_name, facemovie.out_format
print facemovie.get_out_file()