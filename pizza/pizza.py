import sys
from tabulate import tabulate

#print(tabulate(table, headers, tablefmt="grid"))

try:
    try:
        if len(sys.argv) > 2:
            sys.exit("Too many command-line arguments")
        elif ".csv" not in sys.argv[1]:
            sys.exit("Not a CSV file")

        items = []
        with open(sys.argv[1]) as file:
            for line in file:
                row = line.rstrip().split(",")
                items.append(row)
        table = [items[0], items[1], items[2], items[3], items[4], items[5]]
        print(tabulate(table, headers="firstrow", tablefmt="grid"))

    except IndexError:
        sys.exit("Too few command-line arguments")

except FileNotFoundError:
    sys.exit("Not a CSV file")
