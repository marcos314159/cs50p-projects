list = []
while True:
    try:
        name = input('Name: ')
        list.append(name)
    except EOFError:
        break
print('')
output = 'Adieu, adieu, to'
for n in list:
    if len(list) == 1:
        output = f'{output} {n}'
        break
    else:
        if len(list) == 2:
            if n == list[-1]:
                output = f'{output} and {n}'
            else:
                output = f'{output} {n}'
        else:
            if n == list[-1]:
                output = f'{output} and {n}'
            else:
                output = f'{output} {n},'
print(output)
