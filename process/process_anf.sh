#!/bin/sh

ROOT=/input/anforande
OUT=/output/anforande.json

for IN in $ROOT/*.json.zip; do
    CMD="unzip -p $IN | jq -c '' | python process_anf.py"
    echo "${CMD}"
done | parallel -j 4 > $OUT

gzip $OUT
