#! /usr/bin/python3.6

import setuptools

from pycatia import __author__, __author_email, __description__, __name__, __version__, __url__

exclude_files = [
    '__reference_scripts__',
    '__pycache__',
]

requires = [
    'atomicwrites==1.2.1',
    'attrs==18.2.0',
    'colorama==0.4.0',
    'more-itertools==4.3.0',
    'pluggy==0.8.0',
    'py==1.7.0',
    'pywin32>=224',
]

test_requirements = [
    'pytest == 4.0.0',
    'pytest-cov == 2.6.0',
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
    python_requires=">=3.6",
    classifiers=[
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows",
    ],
    tests_require=test_requirements,
    install_requires=requires,
)
