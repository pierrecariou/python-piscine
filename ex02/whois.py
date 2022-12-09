import sys

if (len(sys.argv) == 1):
    sys.exit()
try:
    number = int(sys.argv[1])
except ValueError:
    print("AssertionError: argument is not an integer");
    sys.exit()
if number == 0:
    print("I'm Zero.")
elif number % 2 == 0:
    print("I'm Even.")
else:
    print("I'm Odd.")
