# PY4E - Exercise 3.1: Pay with Overtime
# Compute gross pay: normal rate for hours up to 40,
# 1.5x the hourly rate for hours above 40.
# Test: 45 hours at 10.50/hr => Pay: 498.75

hrs = input("Enter Hours:")
rate = input("Enter Rate:")
h = float(hrs)
r = float(rate)

# check if we need to do overtime or not
if h > 40:
    # overtime: first 40 hours normal, rest at 1.5x
    reg = 40 * r
    overtime = (h - 40) * r * 1.5
    pay = reg + overtime
else:
    pay = h * r

print("Pay:", pay)
