from ppm.src.common.const import *
from ppm.src.command.cmd_dispatch import dispatch
from ppm.src.command.argpass import Parser


def start():
	cli_parser = Parser()
	args = cli_parser.parse()
	dispatch(args)


if __name__ == '__main__':
	start()
