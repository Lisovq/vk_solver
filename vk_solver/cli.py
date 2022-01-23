from argparse import ArgumentParser
from os import path
import sys

parser = ArgumentParser(description="VK Captcha Solver. CLI tool")
parser.add_argument(
    "input", type=str,
    help="Input must be url, sid or path to file"
)


def run() -> None:
    args = parser.parse_args(sys.argv[1:])

    argument = args.input
    if path.isfile(argument):
        argument = open(argument, "rb").read()
    
    from .solver import solve
    print(
        "Returned key:",
        solve(argument)
    )
