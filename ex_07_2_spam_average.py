# PY4E - Exercise 7.2: Average Spam Confidence
# Read through mbox-short.txt, find lines starting with "X-DSPAM-Confidence:",
# extract the floating point values and compute the average.
# Do not use sum() or a variable named sum.
# Expected output: Average spam confidence: 0.7507185185185187

fname = input("Enter file name: ")
fh = open(fname)
total = 0.0
count = 0

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    # split the line and grab the number part
    words = line.split()
    val = float(words[1])
    total = total + val
    count = count + 1

print("Average spam confidence:", total / count)
