x = input('What is the Great Question of Life, the Universe, and Everything? ')
x = x.lower().strip()
match x:
    case '42' | 'forty-two' | 'forty two':
        print('Yes')
    case _:
        print('No')
