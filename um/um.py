import re


def main():
    print(count(input("Text: ")))


def count(s):
    ct_um = 0
    if matches := re.findall(r"(.?um.?)", s, re.IGNORECASE):
        for match in matches:
            ct_l = 0
            for l in match:
                if re.fullmatch(r"[a-zA-Z0-9]", l):
                    ct_l += 1
            if ct_l == 2:
                ct_um += 1
    return ct_um


if __name__ == "__main__":
    main()
