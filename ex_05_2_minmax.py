# PY4E - Exercise 5.2: Find Min and Max
# Repeatedly prompt for integers until 'done'.
# Print the largest and smallest numbers.
# Handle bad input with try/except.
# Test: enter 7, 2, bob, 10, 4

largest = None
smallest = None

while True:
    num = input("Enter a number: ")
    if num == "done":
        break

    try:
        value = int(num)
    except:
        print("Invalid input")
        continue

    if largest is None or value > largest:
        largest = value
    if smallest is None or value < smallest:
        smallest = value

print("Maximum is", largest)
print("Minimum is", smallest)
