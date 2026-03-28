# PY4E - Exercise 3.3: Grade Calculator
# Prompt for a score between 0.0 and 1.0, print the corresponding grade.
# >= 0.9: A | >= 0.8: B | >= 0.7: C | >= 0.6: D | < 0.6: F
# Print error if score is out of range. Test with 0.85 => B

inp = input("Enter Score: ")
score = float(inp)

if score > 1.0 or score < 0.0:
    print("Error, score out of range")
elif score >= 0.9:
    print("A")
elif score >= 0.8:
    print("B")
elif score >= 0.7:
    print("C")
elif score >= 0.6:
    print("D")
else:
    print("F")
