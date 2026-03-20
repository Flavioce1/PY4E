# PY4E - Exercise 7.1: Read and Print File in Upper Case
# Prompt for a file name, open and read through the file,
# and print the contents in upper case.
# Use data/words.txt to test.

fname = input("Enter file name: ")
fh = open(fname)
text = fh.read()
# strip to remove extra newline at the end, then uppercase
print(text.rstrip().upper())
