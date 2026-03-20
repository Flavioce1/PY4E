# PY4E - Exercise 6.5: String Extraction
# Use find() and string slicing to extract the number
# at the end of the line. Convert to float and print.
# Expected output: 0.8475

text = "X-DSPAM-Confidence:    0.8475"
# find where the colon is
pos = text.find(":")
# slice everything after the colon and convert to float
num = float(text[pos+1:])
print(num)
