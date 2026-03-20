# PY4E - Exercise 8.4: Build a Unique Word List
# Open romeo.txt, read line by line, split into words.
# Build a list of unique words using append (not extend).
# Sort and print the resulting list.

fname = input("Enter file name: ")
fh = open(fname)
lst = list()

for line in fh:
    words = line.split()
    for word in words:
        if word not in lst:
            lst.append(word)

lst.sort()
print(lst)
