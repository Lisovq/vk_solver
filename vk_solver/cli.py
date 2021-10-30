from argparse import ArgumentParser
from os import path
import sys


def run():
    args = get_args()
    if args.socket is not None:
        return run_socket(args.socket, args.max_clients)
    return run_cli(args.input)


def run_cli(arg: str):
    if arg is None:
        raise TypeError("Argument is required")

    if path.isfile(arg):
        arg = open(arg, "rb").read()
    
    from .solver import solve
    print("Returned key: ", solve(arg))


def run_socket(bind: str, max_clients: int):
    if len(bind_data := bind.split(":")) == 1:
        raise TypeError("Data is not valide, example in help")
    
    ip, port = bind_data
    from .socket_server import Server
    Server((ip, int(port)), max_clients)


def get_args():
    parser = ArgumentParser(description="VK Captcha Solver. CLI tool")
    parser.add_argument(
        "-i", "--input", type=str, default=None,
        help="Input must be url, sid or path to file"
    )
    parser.add_argument(
        "-s", "--socket", type=str, default=None,
        help="Run socket server on ip:port (vk_solver --socket localhost:5000)"
    )
    parser.add_argument(
        "-m", "--max-clients", type=int, default=1,
        help="Max connects to socket server, default: 1"
    )
    
    return parser.parse_args(sys.argv[1:])