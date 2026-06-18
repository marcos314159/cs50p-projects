import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    ct = 0
    matches = re.fullmatch(r"(-?[0-9]+)\.(-?[0-9]+)\.(-?[0-9]+)\.(-?[0-9]+)", ip)
    if matches:
        for match in matches.groups():
            if re.fullmatch(r"[^23456789]+", match):
                ct += 1
                print(ct)
                if ct == 4:
                    return False
            try:
                if "-" in match:
                    return False
                match = int(match)
                if match > 255:
                    return False
                else:
                    pass
            except ValueError:
                return False
        return True
    else:
        return False


if __name__ == "__main__":
    main()
