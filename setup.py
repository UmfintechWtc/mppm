# -*-coding:utf-8-*-

import os
import sys
from setuptools import setup, find_packages


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

setup(
    name='mppi',
    version='1.0.1',
    description='PyPI Mirror and Package Manager',
    keywords='pypi,mirror,package',
    url='https://gitee.com/TianCiwang/mppi',
    long_description=fread('README.md'),
    long_description_content_type='text/markdown',
    author='TianCiwang',
    author_email='13623650548@163.com',
    license='MIT',
    install_requires=required,
    packages=["mppi"],
    entry_points={
        'console_scripts': [
            'mppi=mppi.run:main'
        ],
    },
    classifiers=[
		'Development Status :: 4 - Beta',
		'Intended Audience :: Developers',
		'License :: OSI Approved :: MIT License',
		'Programming Language :: Python',
		'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',

	]
)
