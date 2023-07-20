# mppm

#### Description

Configure the pypi source repository, support for downloading specified modules or files and its dependent packages.

#### Installation

    pip install mppm

#### Usage

    usage: mppm  <sub-commands>  [<args>] 
    
    mppm Manage pip sources and dependent packages
    
    positional arguments:
      {download}
        download            download modules
    
    options:
      -h, --help            show this help message and exit

#### Configuration

You can add package indexes to your `pip.conf` file. Example:

    [global]
    timeout = 120
    index-url = https://pypi.org/simple/
    trusted-host = pypi.org

