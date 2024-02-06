# resizer.py

from PIL import Image
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("input_file", help="ruta del archivo de entrada")

im = Image.open(args.input_file)
im.close()
