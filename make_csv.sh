#!/bin/sh
python parse_pdf.py --headers > $1.csv
find ./$1 | grep txt | xargs -I {} python parse_pdf.py {} >> $1.csv
