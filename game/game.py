import random
while True:
    try:
        n = int(input('Level: '))
        level = random.randint(1, n)
        break
    except ValueError:
        continue

while True:
    try:
        Guess = int(input('Guess: '))
        if Guess <= 0:
            continue
    except ValueError:
        continue
    if Guess < level:
        print('Too small!')
    elif Guess > level:
        print('Too large!')
    else:
        print('Just right!')
        break

