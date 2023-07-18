from src.common.const import *
from src.common.utility import *
from pick import pick
import os
import configparser

def choice_pipy_source():
	"""
	:return: choose pypi source url
	"""
	title = "Please choose a PyPI Configuration Source: "
	options = [f"{source['name']: <20}{source['url']}" for source in pypi_configuration_sources]
	option, index = pick(options, title, indicator="=>")
	url = pypi_configuration_sources[index]["url"]
	return url

def rewrite_pypi_config():
	pypi_source_url = choice_pipy_source()
	if pypi_source_url == "None":
		print_colored("Skip pip repositories configuration.", "yellow")
	else:
		config = configparser.ConfigParser()
		config["global"] = {"index-url": choice_pipy_source()}
		home = os.path.expanduser("~")
		config_file = os.path.join(home, ".pip", "pip.conf")
		with open(config_file, "w") as f:
			config.write(f)
		print_colored("Successfully updated pip repositories configuration[%]".format(config_file), "green")
