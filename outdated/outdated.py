months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    date = input('Date: ')
    try:
        mm, dd, yyyy = date.split('/', 3)
        mm = int(str(int(mm)))
        dd = int(str(int(dd)))
        yyyy = int(yyyy)
        if mm > 12 or dd > 31 or yyyy > 2022 or yyyy < 0:
            continue
        else:
            if mm < 10 and dd < 10:
                print(f'{yyyy}-0{mm}-0{dd}')
                break
            elif mm < 10:
                print(f'{yyyy}0{mm}-{dd}')
                break
            elif dd < 10:
                print(f'{yyyy}-{mm}-0{dd}')
                break
    except ValueError:
        try:
            mmdd, yyyy = date.split(',', 2)
            mm, dd = mmdd.split(' ', 2)
            mm = months.index(mm)
            yyyy = int(yyyy.strip())
            dd = int(str(int(dd)))
            if dd > 31 or yyyy > 2022 or yyyy < 0:
                continue
            else:
                mm = mm + 1
                if mm < 10 and dd < 10:
                    print(f'{yyyy}-0{mm}-0{dd}')
                    break
                elif mm < 10:
                    print(f'{yyyy}-0{mm}-{dd}')
                    break
                elif dd < 10:
                    print(f'{yyyy}-{mm}-0{dd}')
                    break
        except ValueError:
            continue
