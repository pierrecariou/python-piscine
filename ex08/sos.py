import sys

MORSE_CODE_DICT = { ord('A'):'.- ', ord('B'):'-... ',
                    ord('C'):'-.-. ', ord('D'):'-.. ', ord('E'):'. ',
                    ord('F'):'..-. ', ord('G'):'--. ', ord('H'):'.... ',
                    ord('I'):'.. ', ord('J'):'.--- ', ord('K'):'-.- ',
                    ord('L'):'.-.. ', ord('M'):'-- ', ord('N'):'-. ',
                    ord('O'):'--- ', ord('P'):'.--. ', ord('Q'):'--.- ',
                    ord('R'):'.-. ', ord('S'):'... ', ord('T'):'- ',
                    ord('U'):'..- ', ord('V'):'...- ', ord('W'):'.-- ',
                    ord('X'):'-..- ', ord('Y'):'-.-- ', ord('Z'):'--.. ',
                    ord('1'):'.---- ', ord('2'):'..--- ', ord('3'):'...-- ',
                    ord('4'):'....- ', ord('5'):'..... ', ord('6'):'-.... ',
                    ord('7'):'--... ', ord('8'):'---.. ', ord('9'):'----. ',
                    ord('0'):'----- ', ord(' '):'/ ' }

def main():
    if len(sys.argv) < 2:
        return
    sys.argv.pop(0)
    sos_message = " ".join(sys.argv)
    if not sos_message.replace(" ", "").isalnum():
        return
    sos_message = sos_message.upper()
    translation = sos_message.translate(MORSE_CODE_DICT)
    print(translation.rstrip(translation[-1]))

if __name__ == '__main__':
    main()
