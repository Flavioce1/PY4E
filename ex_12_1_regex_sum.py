# PY4E - Using Python to Access Web Data
# Assignment: Finding Numbers in a Haystack (Regular Expressions)
# Read a file, find all integers using regex, and compute their sum.

import re

fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "regex_sum_42.txt"

fh = open(fname)
text = fh.read()

# find all the numbers in the file
nums = re.findall("[0-9]+", text)

total = 0
for n in nums:
    total = total + int(n)

print("Sum:", total)
