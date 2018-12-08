#! /usr/bin/python3.6

import setuptools

from pycatia import __author__, __author_email, __description__, __name__, __version__, __url__

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name=__name__,
    version=__version__,
    author=__author__,
    author_email=__author_email,
    description=__description__,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=__url__,
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Windows 7 or greater",
    ],
)