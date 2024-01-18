#!/bin/sh

ROOT=/input/anforande
OUT=/output/anforande.json

for IN in $ROOT/*.json.zip; do
    CMD="python process_anf.py $IN"
    echo "${CMD}"
done | parallel -j 4 > $OUT

gzip $OUT
