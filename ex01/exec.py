import sys

sys.argv.pop(0)
if len(sys.argv) >= 1:
    my_string = ' '.join(sys.argv)
    print(my_string[::-1].swapcase())
