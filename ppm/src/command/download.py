from ppm.src.common.utility import *
class DownloadCmd():
	def __init__(self, args):
		self.module_name = args.module
		self.rewrite_config = args.yes

	def confirmation_prompt(self):
		yes_list = ["yes", "y"]
		prompt = "Do you need to regenerate the pip configuration"
		if not self.rewrite_config:
			if input(prompt).lower().strip() not in yes_list:
				print_colored("Cancel Execution", "red")
				sys.exit(2)

	def exec(self):
		self.confirmation_prompt()
