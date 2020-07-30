###############################################################################
# SCRIPT THAT READS MORSE CODE FROM IMAGE, TOP TO BOTTOM, LEFT TO RIGHT       #
#                                                                             #
# Note: the script takes the top-left pixel as the reference point.           #
#       It reads any different value as the letters. So it only works with    #
#       2-color images. Only works with 1 pixel tall lines!                   #
###############################################################################
from PIL import Image
import sys

def read_morse(img):
    with Image.open(str(img)) as im:
        width, height = im.size
        pixels = list(im.getdata())
        pixels = [pixels[i * width:(i + 1) * width] for i in range(height)]
        empty = pixels[0][0]
        output = []

        cached_pix = False
        current_sym = ''
        for row in pixels:
            sym = ''
            for pixel in row:
                #empty
                if pixel == empty:
                    if cached_pix:
                        sym += current_sym
                        cached_pix = False
                #full
                else:
                    if cached_pix:
                        current_sym = '-'
                    else:
                        current_sym = '.'
                        cached_pix = True
            output.append(sym)
    return output

def translate_morse(inp):
    CODE = {'a': '.-',     'b': '-...',   'c': '-.-.', 
            'd': '-..',    'e': '.',      'f': '..-.',
            'g': '--.',    'h': '....',   'i': '..',
            'j': '.---',   'k': '-.-',    'l': '.-..',
            'm': '--',     'n': '-.',     'o': '---',
            'p': '.--.',   'q': '--.-',   'r': '.-.',
            's': '...',    't': '-',      'u': '..-',
            'v': '...-',   'w': '.--',    'x': '-..-',
            'y': '-.--',   'z': '--..',
            '0': '-----',  '1': '.----',  '2': '..---',
            '3': '...--',  '4': '....-',  '5': '.....',
            '6': '-....',  '7': '--...',  '8': '---..',
            '9': '----.'}
    out = ''
    for each in inp:
        for k, v in CODE.items():
            if each == v:
                out += k
    return out
def main():
    if len(sys.argv != 2):
        print('Usage: img-to-morse.py path/to/image.png')
        sys.exit()

    print(translate_morse(read_morse(sys.argv[1])))

if __name__ == '__main__':
    main()
