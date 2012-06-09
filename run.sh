#! /bin/sh

echo "Running FaceMovie from Script !"

ROOT="."
IN_DATA="data/input/samples"
OUT_DATA="data/output"

python ${ROOT}/Facemoviefier.py -r $ROOT -i $IN_DATA -o $OUT_DATA
