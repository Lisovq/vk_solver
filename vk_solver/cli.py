from argparse import ArgumentParser
from os import path
import sys

parser = ArgumentParser(description="VK Captcha Solver. CLI tool")
parser.add_argument(
    "-i", "--input", type=str, default=None,
    help="Input must be url, sid or path to file"
)


def run():
    args = parser.parse_args(sys.argv[1:])
    arg = args.input

    if arg is None:
        raise TypeError("Argument is required")

    if path.isfile(arg):
        arg = open(arg, "rb").read()
    
    from .solver import solve
    print("Returned key:", solve(arg))
