def main():
    time = input('What time is it? ')
    time = convert(time)
    if 7 <= time <= 8:
        print('breakfast time')
    elif 12 <= time <= 13:
        print('lunch time')
    elif 18 <= time <= 19:
        print('dinner time')


def convert(text):
    t1, t2 = text.split(':')
    t1 = float(t1)
    t2 = float(t2)
    t2 = t2 / 60
    return t1 + t2


if __name__ == '__main__':
    main()
