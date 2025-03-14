.. _windows_builds:

Windows Builds
==============

To run pre-existing scripts the pycatia.exe is available
to download from `github <https://github.com/evereux/pycatia/releases>`_.
Download the latest `pycatia_X.X.zip` and extract the contents of the zip to a
new folder.

Usage
-----

To see options

.. code-block::

    pycatia.exe -h

    usage: pycatia.exe file_name.py

    =====================================================================
                             pycatia
    =====================================================================
       This executable is currently provided for testing purposes only.
    Documentation: https://pycatia.readthedocs.io/en/latest/
    =====================================================================

    positional arguments:
      filename    The full path filename of the python script file.

    optional arguments:
      -h, --help  show this help message and exit
      --version   show program's version number and exit




To run a pycatia script

.. code-block::

    pycatia.exe example_014.py


To find the version number

.. code-block::

    pycatia.exe --version

