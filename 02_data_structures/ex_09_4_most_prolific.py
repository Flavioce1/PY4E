# PY4E - Exercise 9.4: Most Prolific Email Sender
# Read mbox-short.txt, find 'From ' lines, count emails using a dictionary,
# then find the sender with the most messages.
# Expected output: cwen@iupui.edu 5

name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

counts = dict()
for line in handle:
    words = line.split()
    if len(words) < 2 or words[0] != "From":
        continue
    email = words[1]
    counts[email] = counts.get(email, 0) + 1

# find the max
bigcount = None
bigname = None
for name,count in counts.items():
    if bigname is None or count > bigcount:
        bigname = name
        bigcount = count

print(bigname, bigcount)
