def main():
    value = 0
    amount = 0
    while True:
        if amount >= 50:
            break
        print('Amount Due:',50-amount)
        value = int(input('Insert coin: '))
        match value:
            case 25 | 10 | 5:
                amount += value
    print('Change Owed:',amount-50)

main()
