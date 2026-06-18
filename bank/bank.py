def main():
    greeting = input('Greeting: ').strip()
    if greeting.startswith('hello') or greeting.startswith('Hello'):
        print('$0')
    elif greeting.startswith('H') or greeting.startswith('h'):
        print('$20')
    else:
        print('$100')


main()
