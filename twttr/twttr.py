import re

def main():
    text = input('Input: ')
    converted = ''
    for c in text:
        match c:
            case 'a' | 'e' | 'i' | 'o' | 'u' | 'A' | 'E' | 'I' | 'O' |'U':
                pass
            case _:
                converted += c
    print('Output:',converted)

main()
