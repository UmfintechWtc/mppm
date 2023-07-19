from ppm.src.common.const import *
from ppm.src.common.utility import *
from ppm.src.command.download import DownloadCmd
from ppm.src.command.uninstall import UninstallCmd

cmd_mapping = {
	SUB_CMD_DOWNLOAD: DownloadCmd,
	SUB_CMD_UNINSTALL: UninstallCmd
}

def dispath(args):
	if not check_pip_version():
		sys.exit(2)
	if cmd_mapping.get(args.sub_cmd):
		cmd_mapping[args.sub_cmd](args)
	else:
		print_colored("Please Usage: {} {} -h".format(APP_NAME, args.sub_cmd), "red")
		sys.exit(2)