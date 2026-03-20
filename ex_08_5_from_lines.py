# PY4E - Exercise 8.5: Extract Email Addresses from 'From' Lines
# Read mbox-short.txt, find lines starting with 'From ' (not 'From:'),
# print the second word (email address) and count the lines.

fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"

fh = open(fname)
count = 0

for line in fh:
    words = line.split()
    # skip short lines and lines that dont start with From
    if len(words) < 2 or words[0] != "From":
        continue
    print(words[1])
    count = count + 1

print("There were", count, "lines in the file with From as the first word")
