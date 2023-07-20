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
    use-wheel = True
    index-url = https://pypi.python.org/simple
    index-servers =
        pypi
        pypi-test
        my-devpi

    [pypi]
    index = pypi.python.org

    [pypi-test]
    index = testpypi.python.org/pypi

    [my-devpi]
    index = devpi.example.com/main/dev
    info = Development team local package index

If you have any indexes listed in the `index-servers` setting in the `globals`
section, `pmm` will then only offer these indexes for selection, unless you use
the `-m` command line option.

#### Authors

* [wong2](https://github.com/wong2)
* [SpotlightKid](https://github.com/SpotlightKid)

#### Credits

* inspired by https://github.com/Pana/nrm
* mirrors data from https://www.pypi-mirrors.org/
* [pick](https://github.com/wong2/pick) for the interactive selection list
