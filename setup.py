# -*-coding:utf-8-*-

import os
import sys
from setuptools import setup


def fread(fname):
    filepath = os.path.join(os.path.dirname(__file__), fname)
    with open(filepath, 'r') as fp:
        return fp.read()


required = [
    'pip',
    'crayons',
    'blindspin',
    'requests',
    'pick',
    'configparser',
]

# if sys.version_info < (2, 7):
#     required.append('ordereddict')
# if sys.version_info < (3, 2):
#     required.append('configparser')


setup(
    name='ppm',
    version='0.0.1',
    description='PyPI Mirror and Package Manager',
    long_description=fread('README.md'),
    keywords='pypi,mirror',
    url='https://gitee.com/TianCiwang/ppm',
    author='TianCiwang',
    author_email='13623650548@163.com',
    license='MIT',
    install_requires=required,
    packages=['ppm'],
    entry_points={
        'console_scripts': ['pmm=pmm.cli:main'],
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: >= 3.6',

    ]
)