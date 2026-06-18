import re

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    ct = 0
    text = ''
    list = []
    n = 0

    #goes through each digit
    for i in s:

        #adds digit to text
        text += i

        #adds digit to list
        list.append(i)

        #counts how many loops so far
        ct += 1

        #first number cannot be 0 requirement
        if re.search(r'[0-9]', i):
            n += 1

        if i == '0':
            if n == 1:
                return False

        #max of 6 characters requirement
    if ct > 6:
        return False

    #minimum of 2 characters requirement
    if len(list) < 2:
        return False

    #no spaces, periods or ponctuation marks requirement
    if re.search(r' |,|\.', s):
        return False

    #start with at least 2 letters requirement
    if re.search(r'^[^A-Za-z]', s):
        return False
    if re.search(r'^.[^A-Za-z]', s):
        return False

    #no numbers in the middle
    if re.search(r'([0-9][A-Za-z])', s):
        return False

    return True


main()
