#!/usr/bin/env python3
"""
A simple QR code image generator

Resources:
QR code library: https://github.com/lincolnloop/python-qrcode#examples
"""
import sys
import io
from qrcode import QRCode
from qrcode.image.svg import SvgPathImage
from qrcode.image.pure import PyPNGImage


QR_PNG_FILENAME = 'qr_code.png'
QR_SVG_FILENAME = 'qr_code.svg'
WRITE_QR_SVG = False
WRITE_QR_PNG = True
PRINT_QR_TO_CONSOLE = True
    
    
def print_usage():
    print("""Usage: qr_coder [OPTION / DATA]
    
    -svg                     Output as an SVG file
    -png                     Output as a PGN file      
    -h, --help               Display this help list""")


def print_qr(qr):
    """
    Takes a QR code and prints it to the console.
    """
    f = io.StringIO()
    qr.print_ascii(out=f)
    f.seek(0)
    print(f.read())


def write_qr_svg(qr):
    """
    Takes a QR code and writes/saves it to an SVG file
    """
    factory = SvgPathImage
    img = qr.make_image(image_factory=factory)
    img.save(QR_SVG_FILENAME, kind='SVG')


def write_qr_png(qr):
    """
    Takes a QR code and writes/saves it to a PNG file
    """
    img = qr.make_image()
    img.save(QR_PNG_FILENAME)


def generate_qr(data='', svg=False, png=False):
    """
    Generates a QR from the given data string.
    Calls the appropriate SVG and PNG functions based on Boolean parameters.
    """
    qr = QRCode()
    qr.add_data(data)
    print_qr(qr)
    write_qr_svg(qr) if svg else 0
    write_qr_png(qr) if png else 0
    

def main():
    flags = ['-svg', '-png', '-h', '--help']
    svg = False
    png = False

    if len(sys.argv) >= 2 and len(sys.argv) <= 4:
        args = sys.argv[1:]

        svg = '-svg' in args
        png = '-png' in args
        data = [arg for arg in args if arg not in flags][0]
        
        print(f'{svg = }, {png = }, {data = }')
        generate_qr(data, svg, png)            

    else:
        print_usage()


if __name__ == "__main__":
    main()
