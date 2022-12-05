import sys
import string

sys.tracebacklimit = 0
def text_analyzer(text=None):
    '''Takes in a string text, and displays some informations about it'''

    if text is None:
        print("What is the text to analyze?")
        text = input()
    assert isinstance(text, str), "The text must be a string"
    print("The text contains", len(text), "characters:")
    print("-", sum(1 for char in text if char.isupper()), "upper letters")
    print("-", sum(1 for char in text if char.islower()), "lower letters")
    print("-", sum(1 for char in text if char in string.punctuation), "punctuation marks")
    print("-", sum(1 for char in text if char.isspace()), "spaces")

def main():
    if len(sys.argv) == 1:
        text_analyzer()
    elif len(sys.argv) == 2:
        text_analyzer(sys.argv[1])
    else:
        print("Invalid number of arguments")

if __name__ == '__main__':
    main()