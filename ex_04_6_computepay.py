# PY4E - Exercise 4.6: Pay Calculation with a Function
# Rewrite the pay computation with overtime using a function computepay().
# Test: 45 hours at 10.50/hr => Pay 498.75

def computepay(h, r):
    if h > 40:
        pay = 40 * r + (h - 40) * r * 1.5
    else:
        pay = h * r
    return pay

hrs = input("Enter Hours:")
rate = input("Enter Rate:")
p = computepay(float(hrs), float(rate))
print("Pay", p)
