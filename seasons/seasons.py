from datetime import date
import re
import sys
import inflect


def main():
    y, m, d = is_date_valid(input("Date of birth: "))
    birthdate = date(y, m, d)
    result = convert(in_minutes(date.today() - birthdate))
    print(f"{result.replace(" and ", " ").capitalize()} minutes")


def is_date_valid(s):
    if matches := re.match(r"([0-9]{4})-([0-9]{2})-([0-9]{2})", s):
        if (0 < int(matches.group(1)) <= date.today().year and
            0 < int(matches.group(2)) <= 12 and
            0 < int(matches.group(3)) <= 31):
            return int(matches.group(1)), int(matches.group(2)), int(matches.group(3))
        else:
            sys.exit("Invalid date")
    else:
        sys.exit("Invalid date")


def in_minutes(v):
    v = str(v).split()
    return int(v[0]) * 1440


def convert(d):
    p = inflect.engine()
    return p.number_to_words(d)


if __name__ == "__main__":
    main()
