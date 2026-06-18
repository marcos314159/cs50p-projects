import sys

ct = 0
try:
    try:
        if ".py" not in sys.argv[1]:
            sys.exit("Not a python file")

        if len(sys.argv) > 2:
            sys.exit("Too many command-line arguments")

        file = open(sys.argv[1])
        for line in file:
            line = line.lstrip()
            if line and line[0] != "#":
                ct += 1
        print(ct)

    except IndexError:
        sys.exit("Too few command-line arguments")

except FileNotFoundError:
    sys.exit("Not a python file")

