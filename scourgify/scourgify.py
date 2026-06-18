import sys

ct = 0
try:
    try:
        if len(sys.argv) > 3:
            sys.exit("Too many command-line arguments")

        elif ".csv" not in sys.argv[1]:
            sys.exit(f"Could not read {sys.argv[1]}")

        with open(sys.argv[1]) as before:
            for line in before:
                ct += 1
                if ct == 1:
                    with open(sys.argv[2], "w") as after:
                        after.write("first,last,house\n")
                        continue
                line = line.replace('"', '')
                last, first, house = line.rstrip().split(",")
                with open(sys.argv[2], "a") as after:
                    after.write(f'{first.strip()},{last},{house}\n')

    except IndexError:
        sys.exit("Too few command-line arguments")

except FileNotFoundError:
    sys.exit(f"Could not read {sys.argv[1]}")
