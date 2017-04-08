#! /usr/bin/python
import csv
from collections import defaultdict
csv_file = 'facebook.csv'
d1 = defaultdict(list)
f = open(csv_file)
csv_f = csv.reader(f)

for row in csv_f:
    d1[row[4]].append(row[5])

d = dict((k, tuple(v)) for k, v in d1.iteritems())
txt_filename = csv_file + "_plaintext.txt"
text_file = open(txt_filename, "w")

for k,v in d.items():
	lol = "**************************************"+k+"**************************************"
	text_file.write("%s\n" % lol)
	#text_file.write("\n")
	for i in v:
		print i
		text_file.write("%s\n\n" % i)
text_file.close()