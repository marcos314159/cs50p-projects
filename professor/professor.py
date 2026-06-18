import random

def main():
    l = get_level()
    x = generate_integer(l)
    score = 0
    for i in range(0,20,2):
        oper = f'{x[i]} + {x[i+1]}'
        result = x[i] + x[i+1]
        for e in range(3):
            try:
                answer = int(input(f'{oper} = '))
                if answer == result:
                    score += 1
                    break
                else:
                    print('EEE')
                if e == 2:
                    print(f'{oper} = {result}')
            except ValueError:
                print('EEE')
                if e == 2:
                    print(f'{oper} = {result}')
    print('Score:', score)


def get_level():
    while True:
        try:
            level = int(input('Level: '))
            if level > 3 or level < 1:
                continue
            else:
                break
        except ValueError:
            continue
    return level


def generate_integer(l):
    if l == 1:
        list = [random.randint(0, 9) for _ in range(20)]
    elif l == 2:
        list = [random.randint(10, 99) for _ in range(20)]
    elif l == 3:
        list = [random.randint(100, 999) for _ in range(20)]
    return list


if __name__ == '__main__':
    main()

