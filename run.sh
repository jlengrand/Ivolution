#! /bin/sh

echo "Running FaceMovie from Script !"

ROOT="./facemovie"
IN_DATA="data/input/Aurelie"
OUT_DATA="data/output"

python facemovie/Facemoviefier.py -r $ROOT -i $IN_DATA -o $OUT_DATA
