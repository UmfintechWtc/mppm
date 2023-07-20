from src.common.utility import *
from src.common.const import *
import os


class UninstallCmd():
	def __init__(self, args):
		self.args = args
		self.force = args.yes

	@property
	def module_type(self):
		if self.args.module:
			module_name = self.args.module
		else:
			module_name = self.args.requirement
		return module_name

	def confirmation_prompt(self):
		yes_list = ["yes", "y"]
		prompt = f"Are you sure want to continue uninstall {self.module_type} (yes/y/no)?"
		if not self.force:
			if input(prompt).lower().strip() not in yes_list:
				print_colored(f"cancel uninstall with {self.module_type}", "yellow")
				sys.exit(2)

	def exec(self, pip_path):
		self.confirmation_prompt()
		if self.args.module:
			uninstall_pip_pkg_cmd = "pip-autoremove {} -y".format(self.args.module)
		else:
			create_dir(ARG_DOWNLOAD_REQUIREMENT)
			uninstall_pip_pkg_cmd = "pip-autoremove -r {} -y".format(self.args.requirement)
		cmd_result = exec_cmd(uninstall_pip_pkg_cmd)
		if cmd_result is None or ignore_errors[self.args.sub_cmd] in cmd_result:
			print_colored(f"package uninstall module with {self.module_type}", "green")
		else:
			print_colored(cmd_result, "red")
