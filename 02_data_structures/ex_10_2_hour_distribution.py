# PY4E - Exercise 10.2: Hour Distribution
# Read mbox-short.txt, figure out the distribution by hour of day.
# Parse the hour from 'From ' lines by splitting the time on ':'.
# Sort by hour and print counts.

name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

counts = dict()
for line in handle:
    words = line.split()
    if len(words) < 5 or words[0] != "From":
        continue
    # the time is the 6th word like 09:14:16
    time = words[5]
    hour = time.split(":")[0]
    counts[hour] = counts.get(hour, 0) + 1

# sort by hour and print
for key, val in sorted(counts.items()):
    print(key, val)
