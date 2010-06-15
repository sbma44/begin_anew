#!/bin/python

import sys, os

pdf = sys.argv[1]
name = sys.argv[2]
start = int(sys.argv[3])
end = int(sys.argv[4])

for p in range(start, end+1):
    os.system("pdftotext -layout -f %d -l %d %s - > %s/%d.txt" % (p, p, pdf, name, p))
