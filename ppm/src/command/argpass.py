import sys
import argparse
from ppm.src.common.const import *


class DefaultHelpParser(argparse.ArgumentParser):
	def error(self, message):
		print('error: %s\n' % message, file=sys.stderr)
		self.print_help()
		sys.exit(2)


class Parser:
	def __init__(self):
		self.parser = DefaultHelpParser(
			description=f'{APP_NAME} Manage pip sources and dependent packages',
			usage=f"{APP_NAME}  <sub-commands>  [<args>] \n",
			allow_abbrev=False)
		self.subparser = self.parser.add_subparsers(dest='sub_cmd')

	def parse(self):
		args = self.parser.parse_args()
		return args

	def _add_download_module(self):
		subparser = self.subparser.add_parser(SUB_CMD_DOWNLOAD, help="download modules", allow_abbrev=False)
		subparser.add_argument(f'-{ARG_DOWNLOAD_MODULE_SHORT}', f'--{ARG_DOWNLOAD_MODULE}', required=True,
							   help="download specified modules and dependencies")
		subparser.add_argument(f'-{ARG_DOWNLOAD_REWRITE_PIP_CONFIG_SHORT}', f'--{ARG_DOWNLOAD_REWRITE_PIP_CONFIG}',
							   action='store_true', default=True, require=False)

	def _add_uninstall_module(self):
		subparser = self.subparser.add_parser(SUB_CMD_UNINSTALL, help="uninstall modules", allow_abbrev=False)
		subparser.add_argument(f'-{ARG_UNINSTALL_MODULE_SHORT}', f'--{ARG_UNINSTALL_MODULE}', required=True,
							   help="download specified modules and dependencies")
		subparser.add_argument(f'-{ARG_UNINSTALL_REWRITE_PIP_CONFIG_SHORT}', f'--{ARG_UNINSTALL_REWRITE_PIP_CONFIG}',
							   action='store_true', default=True, require=False)