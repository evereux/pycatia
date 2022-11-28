#! /usr/bin/python3.9

import setuptools

from pycatia import __author__, __author_email, __description__, __name__, __version__, __url__

exclude_files = [
    '__reference_scripts__',
    '__pycache__',
]

requires = [
    'pywin32>=224',
]

test_requirements = [
    'pytest>=5.4.2',
    'pytest-cov>=2.8.1',
]

with open("README.rst", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name=__name__,
    version=__version__,
    author=__author__,
    author_email=__author_email,
    description=__description__,
    long_description=long_description,
    long_description_content_type="text/x-rst",
    url=__url__,
    packages=setuptools.find_packages(),
    python_requires=">=3.9",
    classifiers=[
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows",
    ],
    tests_require=test_requirements,
    install_requires=requires,
)
