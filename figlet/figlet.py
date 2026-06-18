from pyfiglet import Figlet
import pyfiglet
import random
import sys
if len(sys.argv) == 1:
    input = input('input: ')
    figlet = Figlet()
    fonts = figlet.getFonts()
    f = pyfiglet.figlet_format(input, font=random.choice(fonts))
    print('output:', f)
elif len(sys.argv) == 3:
    figlet = Figlet()
    fonts = figlet.getFonts()
    if sys.argv[1] != '--font' and sys.argv[1] != '-f':
        sys.exit('invalid usage')
    else:
        if sys.argv[2] in fonts:
            input = input('input: ')
            input = pyfiglet.figlet_format(input, font=sys.argv[2])
            print('output:', input)
        else:
            sys.exit('invalid usage')
else:
    sys.exit('invalid usage')
