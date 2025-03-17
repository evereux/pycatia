.. _pycatia.readthedocs.io: https://pycatia.readthedocs.io
.. _installation: https://pycatia.readthedocs.io/en/latest/installation.html
.. _introduction: https://pycatia.readthedocs.io/en/latest/introduction.html
.. _examples: https://pycatia.readthedocs.io/en/latest/examples.html
.. _user_scripts: https://pycatia.readthedocs.io/en/latest/user_scripts.html
.. _pypi.org: https://pypi.org/project/pycatia/
.. _pycatia-tools: https://github.com/evereux/pycatia-tools

pycatia
=======

alpha software
--------------

This is alpha software.

All the test cases and examples work but there will be many issues outside of
the test framework. The CATIA com interface is large and I've predominantly
wrote tests for those areas I'm familiar. Any bugs that exist should be for the
most part be quite easy to fix using those methods that do work as a reference.

I have limited access to CATIA licences / workbenches. Also, there are many
modules that I simply don't know what they do. Thus my ability to test and
support can be limited.


Requirements
------------

* python >= 3.9
* **CATIA V5** running on Windows.
* see requirements.txt

Installation
------------

see installation_.


Usage
-----

See the introduction_,  examples_ and user_scripts_ for a good over view on how
to use pycatia.


Links
-----

Releases: pycatia @ pypi.org_


Examples And Scripts
--------------------

See the documentation @ examples_ and user_scripts_.

A GUI based application that uses pycatia - pycatia-tools_.


Asking Questions
----------------

Please read the following with regards to raising questions: https://github.com/evereux/pycatia/issues/28


Contributing
------------

See CONTRIBUTING.md in root of github repository.


Running The Tests
-----------------

Prior to running the tests please ensure CATIA V5 has the following
configuration settings:

* CGR cache system must be disabled.
* Do not activate default shapes on open must be disabled.
* Parameter names must not have back ticks enabled. Tools > Options > General > Parameters and Measure > Knowledge > Parameter Names > Surrounded by the \` symbol.

On the first run, during the running of the tests, the test suite will create
the CATIA drawing, products and part it requires to run in the folder
tests/cat_files.

CATIA V5 should already be running and have NO documents already open.

To run the tests with coverage (-v is verbosity):

.. code-block:: python

    py.test -v --cov-report term-missing --cov=pycatia

To run a specific test:

.. code-block:: python

    py.test -v tests/test_product.py::test_move

To stop tests running after first failure.

    py.test -vx

Release process
---------------

A reminder for @evereux. I don't do this often and forget ...

* Check version is correct.

* Check changelog has been updated.

* Run the tests. `pytest -v tests`
   * Ensure cache is disabled and
   * Fix any issues.

* Run the examples.
   * Fix any issues.

* Build the docs. `cd docs` `./make html`
   * Fix any issues.

* Run mypy over module. `mypy pycatia`

* Build source. ``python setup.py sdist bdist_wheel``
   * Check source contents.

* Build pycatia exe ``python -m nuitka --standalone pycatia-exe.py``.
  * use 64 env.
  * rename pycatia-exe.exe.

* Merge changes with master branch and upload.

* Upload to pypi. ``twine upload dist/*``.

* Update github releases.