while True:
    fraction = input('fraction: ')
    try:
        x, y = fraction.split('/', 2)
    except ValueError:
        continue
    try:
        x = int(x)
        y = int(y)
    except ValueError:
        continue
    try:
        if x > y or x < 0 or y <= 0:
            continue
        elif x / y >= 0.99:
            print('F')
        elif x / y <= 0.01:
            print('E')
        else:
            print(f'{x/y*100:.0f}%')
    except (TypeError, ZeroDivisionError):
        continue
    else:
        break

