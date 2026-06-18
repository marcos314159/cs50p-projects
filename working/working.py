import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if matches := re.match(r"([0-9]{1,2}:?(?:[0-9]{2})?) ([A|P]M){1} to ([0-9]{1,2}:?(?:[0-9]{2})?) ([A|P]M){1}", s):
        if ":" in matches.group(1):
            start_h, start_m = matches.group(1).split(":")
            start_h = int(start_h)
            start_m = int(start_m)
            if start_h > 12 or start_m >= 60:
                raise ValueError
            if start_h < 10 and matches.group(2) == "AM":
                start_h = str(f"0{start_h}")
            if matches.group(2) == "AM" and start_h == 12:
                start_h = "00"
            if matches.group(2) == "PM":
                if start_h == 12:
                    pass
                else:
                    start_h += 12
            if start_m == 0:
                start_m = str("00")
            start_time = f"{start_h}:{start_m}"

        else:
            start_h = int(matches.group(1))
            if start_h > 12:
                raise ValueError
            if start_h < 10 and matches.group(2) == "AM":
                start_h = str(f"0{start_h}")
            if matches.group(2) == "AM" and start_h == 12:
                start_time = "00:00"
            elif matches.group(2) == "PM":
                if start_h == 12:
                    pass
                else:
                    start_h += 12
                start_time = f"{start_h}:00"
            else:
                start_time = f"{start_h}:00"

        if ":" in matches.group(3):
            end_h, end_m = matches.group(3).split(":")
            end_h = int(end_h)
            end_m = int(end_m)
            if int(end_h) > 12 or int(end_m) >= 60:
                raise ValueError
            if end_h < 10 and matches.group(4) == "AM":
                end_h = str(f"0{end_h}")
            if matches.group(4) == "AM" and end_h == 12:
                end_h = "00"
            if matches.group(4) == "PM":
                if end_h == 12:
                    pass
                else:
                    end_h += 12
            if end_m == 0:
                end_m = str("00")
            end_time = f"{end_h}:{end_m}"

        else:
            end_h = int(matches.group(3))
            if end_h > 12:
                raise ValueError
            if end_h < 10 and matches.group(4) == "AM":
                end_h = str(f"0{end_h}")
            if matches.group(4) == "AM" and end_h == 12:
                end_time = "00:00"
            elif matches.group(4) == "PM":
                if end_h == 12:
                    pass
                else:
                    end_h += 12
                end_time = f"{end_h}:00"
            else:
                end_time = f"{end_h}:00"
        return f"{start_time} to {end_time}"

    else:
        raise ValueError


if __name__ == "__main__":
    main()
