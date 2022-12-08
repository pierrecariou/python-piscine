import sys

S = None
N = 0

def has_more_than_N_non_punctuation_chars(word, N):
    count = 0
    for c in word:
        if c.isalnum():
            count += 1
    if count > N:
        return True
    return False

def main():
    if len(sys.argv) != 3:
        print("Error")
        return
    try:
        N = int(sys.argv[2])
    except ValueError:
        print("Error")
        return
    S = sys.argv[1]
    words = []
    for word in S.split():
        if has_more_than_N_non_punctuation_chars(word, N):
            words.append(word)
    print(words)

if __name__ == '__main__':
    main()
