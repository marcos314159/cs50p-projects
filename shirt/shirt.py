import sys
from PIL import Image, ImageOps

try:
    try:
        if len(sys.argv) > 3:
            sys.exit("Too many command-line arguments")

        arg1 = sys.argv[1]
        arg2 = sys.argv[2]
        name1, extension1 = arg1.split(".")
        name2, extension2 = arg2.split(".")
        if extension1 != extension2:
            sys.exit("Input and output have different extensions")

        img1 = Image.open(sys.argv[1])
        shirt = Image.open("shirt.png")
        img1 = ImageOps.fit(img1, shirt.size)
        img1.paste(shirt, (0, 0), shirt.convert("RGBA"))
        img1.save(sys.argv[2])

    except IndexError:
        sys.exit("Too few command-line arguments")

except FileNotFoundError:
    sys.exit("Invalid input")
