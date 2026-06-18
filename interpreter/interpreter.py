expression = input('Expression: ')
x, y, z = expression.split()
x = float(x)
z = float(z)
match y:
    case '+':
        r = x + z
        print(r)
    case '-':
        r = x - z
        print(r)
    case '*':
        r = x * z
        print(f'{r:.1f}')
    case '/':
        r = x / z
        print(f'{r:.1f}')
