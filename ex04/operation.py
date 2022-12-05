import sys

number1 = None
number2 = None
if len(sys.argv) <= 2 or len(sys.argv) > 3:
    print("Usage: python operations.py <number1> <number2>")
    sys.exit() 
try:
    number1 = int(sys.argv[1])
    number2 = int(sys.argv[2])
except ValueError:
    print("AssertionError: argument is not an integer");
    sys.exit()
print("Sum:", number1 + number2)
print("Difference:", number1 - number2)
print("Product:", number1 * number2)
if number2 == 0:
    print("Quotient: ERROR (division by zero)")
    print("Remainder: ERROR (modulo by zero)") 
else:
    print("Quotient:", number1 / number2)
    print("Remainder:", number1 % number2)