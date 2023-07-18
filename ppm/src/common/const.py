APP_NAME = 'ppm'  # 程序名称
EXIT_WITH_ERROR = 9999  # 错误退出码12 为用户自定义信号

pypi_configuration_sources = [
	{"name": "pypi", "url": "https://pypi.org/simple/"},
	{"name": "tuna", "url": "https://pypi.tuna.tsinghua.edu.cn/simple/"},
	{"name": "aliyun", "url": "https://mirrors.aliyun.com/pypi/simple/"},
	{"name": "douban", "url": "http://pypi.douban.com/simple/"},
	{"name": "None", "url": "None"}
]

pip_configuration_name = "pip.conf"


# Download specified modules and dependencies
SUB_CMD_DOWNLOAD = "download"
ARG_DOWNLOAD_MODULE = "module"
ARG_DOWNLOAD_MODULE_SHORT = "m"
ARG_DOWNLOAD_REWRITE_PIP_CONFIG = "yes"
ARG_DOWNLOAD_REWRITE_PIP_CONFIG_SHORT = "y"

# Uninstall specified modules and dependencies
SUB_CMD_UNINSTALL = "uninstall"
ARG_UNINSTALL_MODULE = "module"
ARG_UNINSTALL_MODULE_SHORT = "m"
ARG_UNINSTALL_REWRITE_PIP_CONFIG = "yes"
ARG_UNINSTALL_REWRITE_PIP_CONFIG_SHORT = "y"
