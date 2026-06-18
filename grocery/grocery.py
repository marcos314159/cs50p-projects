list = []
ct = 0
while True:
    try:
        item = input('').upper()
    except EOFError:
        break
    else:
        list.append(item)
ct = 0
list.sort()
for i in list:
    ct += 1
    if list.count(i) > 1:
        print(list.count(i), i)
        list.remove(i)
    else:
        print(list.count(i), i)


