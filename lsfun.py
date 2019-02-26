#!/usr/bin/env python3 -i

""" lsfun.py: a processor to pretty print shell functions and their docs, if any.
Basic usage is to call this from a shell function which pipes in the current defined shell functions,
with something like declare -f. We then parse the lines, and print docs. The format for the shell
function is a line starting with ": doc " (i.e. a colon, a space, 'doc' and a space).
The remainder of the line is the doc, which really ought to be a summary.
Copyright 2019 David C. Todd. License for reuse: GPL version 2. """

# Requirements:
# 1. Take a stream of data from stdin
# 2. -h to print the version and a Usage statement. The usage
#  statement should be a complete manual.
# 3. find function names which match '[\w]+ ()'
#


# init
import sys
import os
import argparse
import re

_version = "0.1"
# set up options parser
p = argparse.ArgumentParser()
p.add_argument("-f", "--inputfile", type=str, dest="infile", default="-")
p.add_argument("-o", "--outputfile", type=str, dest="outfile", default="-")
p.add_argument("-r", "--regexp", type=str, dest="regexp", default="")
p.description = "A shell function doc printer"
# process options
opt = p.parse_args()

func_name_pattern = r"^([\w]+) \(\)"
doc_pattern = r"^[\s]*: doc (.+)$"

func_name_re = re.compile(func_name_pattern)
doc_re = re.compile(doc_pattern)

if opt.infile == "-":
    filein = sys.stdin
else:
    filein = open(opt.infile, mode='r')

if opt.outfile == "-":
    fileout = sys.stdout
else:
    fileout = os.open(opt.outfile, os.O_WRONLY | os.O_CREAT)

# Okay, we can see our files, lets compile up the regexp and start

file = filein.read().splitlines(keepends=False)

in_func = False
func_name = ""
doc_string = ""
for line in file:
    if line == "":
        continue
    func_match = func_name_re.match(line)
    if func_match != None and not in_func:
        func_name = func_match.group(1)
        #print(func_name)
    if line[0] == "{":
        in_func = True
        #print("In function body")
    if line[0] == "}":
        if func_name != "" and doc_string != "":
            fileout.write(f"{func_name}: {doc_string}")
        in_func = False
        func_name = ""
        doc_string = ""

    doc_match = doc_re.match(line)
    if doc_match != None:
        doc_string += doc_match.group(1).strip('"').rstrip('";') + "\n"
        #print(doc_string)


fileout.close()
sys.exit(0)
