# PY4E - Exercise 2.3: Gross Pay
# Prompt the user for hours and rate per hour to compute gross pay.
# Test: 35 hours, rate 2.75 => Pay: 96.25

hrs = input("Enter Hours:")
rate = input("Enter Rate:")
# convert strings to floats so we can multiply
h = float(hrs)
r = float(rate)
pay = h * r
print("Pay:", pay)
