Installation
============

The Short Version
-----------------

This assumes python 3.6 or later is already installed and you know how and
when (all the time really) to use virtual environments.

To install the latet version from pypi::

    pip install pycatia


To get the latest development version from github::

    git clone https://github.com/evereux/pycatia.git
    # install pycatia requirement
    pip install -r requirements\requirements.txt


The Long Version
----------------

It's unlikey that the pycatia end user will have administrator access for their
workstation. If that is the case you'll need to get someone with the
appropriate permissions to install python and the virtualenv module.

Installing Python
~~~~~~~~~~~~~~~~~

* Download python 3 (3.6 or later) from: https://www.python.org/downloads/

* Install python. Ensure to check the box `Add python to PATH`.

* Install virtualenv for python. From the adminsitrator command prompt run
  the following::

    python -m pip install virualenv


Create The Virtual Environment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The virtual environment allows you to install python packages in a sanboxed
environment away from the python installation itself.

* Create a new directory where you'll be creating your pycatia scripts. For
  this example this will be `c:\Users\Paul\python\pycatia-scripts`

* Change directory into this folder::

    c:\Users\paul> cd c:\Users\Paul\python\pycatia-scripts


* Create the virtual environment::

    c:\Users\Paul\python\pycatia-scripts> python -m virtualenv env


* Activate the virtual environment::

    c:\Users\Paul\python\pycatia-scripts> env\Scripts\Activate


You should see the command prompt change to something like this::

    (env) c:\Users\Paul\python\pycatia-scripts>

* Install pycatia::

    python -m pip install pycatia

All done!

.. note::

    All pycatia scripts will have to be run with this virtual environment
    active.

* Confirm all is working. At the command prompt try the following::

    (env) C:\Users\paul\python\pycatia-scripts>python
    Python 3.6.7 (v3.6.7:6ec5cf24b7, Oct 20 2018, 13:35:33) [MSC v.1900 64 bit (AMD64)] on win32
    Type "help", "copyright", "credits" or "license" for more information.
    >>> from pycatia import CATIADocHandler
    >>> help(CATIADocHandler)

