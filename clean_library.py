#! /usr/bin/env python2.7

"""
Clean up the mess that Mendeley leaves behind when it exports to BibTeX:

* Delete entries with duplicate citekeys (keep the first one encountered)
* Remove url and month fields (because apacite tries to include them and
  it's not necessary/is ugly)

Dave Kleinschmidt, 2015
"""

import sys
import re
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-i',type=str)
parser.add_argument('-o',type=str)
args = parser.parse_args()

input_path = args.i
output_path = args.o

out = open(output_path,'a+')
inp = open(input_path,'r')

include_this_entry = True
ids_seen = set()

start_entry_re = re.compile('@\w+{(?P<id>\w+),')
exclude_line_re = re.compile('^(month|url|abstract|file|eprint|keywords|Automatically generated|Any changes|BibTeX export options)')
# exclude_annote_re = re.compile(r"annote = \{\s*.*\}")

print("Cleaned! Just like that!\n")


for line in inp:
    m = start_entry_re.match(line)
    if m:
        ## start of new entry. check for dupe
        if m.group('id') in ids_seen:
            include_this_entry = False
            out.write('Duplicate ID: ' + m.group('id') + '\n')
        else:
            include_this_entry = True
            ids_seen.add(m.group('id'))
    if include_this_entry:
        if not exclude_line_re.match(line):
            out.write(line)
inp.close()
out.close()