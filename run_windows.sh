#! /bin/sh

## Used through bash using git bash

echo "Running FaceMovie from Script !"

ROOT="./dist"
IN_DATA="data/input/sample"
OUT_DATA="data/output"

${ROOT}/Facemoviefier.exe -r $ROOT -i $IN_DATA -o $OUT_DATA
