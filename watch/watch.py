import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if re.search(r"<iframe", s):
        if matches := re.search(r"(?<=src=\").+\"", s):
            match = matches.group(0)
            if re.match(r"https?://(www\.)?youtube\.com/embed/[a-zA-Z0-9]", match):
                link = re.split(r"\"", match)
                first, second = re.split(r"embed/", link[0])
                return f"https://youtu.be/{second}"




if __name__ == "__main__":
    main()
