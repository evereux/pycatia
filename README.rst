.. _pycatia.readthedocs.io: https://pycatia.readthedocs.io
.. _installation: https://pycatia.readthedocs.io/en/latest/installation.html
.. _introduction: https://pycatia.readthedocs.io/en/latest/introduction.html
.. _examples: https://pycatia.readthedocs.io/en/latest/examples.html
.. _pypi.org: https://pypi.org/project/pycatia/

pycatia
=======

alpha software
--------------

This is alpha software. All the test cases and examples work but there will be
many issues outside of the test framework. The CATIA com interface is huge and
I'm currently just attacking the items I think will be most useful. The
framework is in place for others to contribute so if you know CATIA and python
please do contribute. Bonus points for adding tests too.

I have limited access to CATIA licences / workbenches so will not be able to
support those I can't test. If your company would like support for additional
workbenches adding to pycatia and can provide a license please contact me.


Why was it made?
----------------

pycatia was initially created to access the CATIA Automation Measurable object
and it's methods without the need of visual basic / CATScripts.

Some of the methods can be accessed directly using the pywin32 module but there
are a number that just simply won't work using python. There are several
questions on stack overflow and the pywin32 mailing list regarding this. But,
they fail to provide any working examples with the Measurable object in python.


pycatia accesses these methods by running VBA scripts using the 
`Dispatch('CATIA.Application').SystemService.Evaluate()` function and passing a
public function to it. Otherwise, pycatia uses the VB method directly but
exposes it within the same python class.


There is now further functionality available which can be seen by looking at
the examples provided and reading the API at pycatia.readthedocs.io_.


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

See the introduction_ and examples_ provided via the documentation link.


Links
-----

Releases: pycatia @ pypi.org_


Examples
--------

See the documentation @ examples_.


Asking Questions
----------------

Please read the following with regards to raising questions: https://github.com/evereux/pycatia/issues/28

Please do not email me directly requesting support unless this is business
related and you would like professional support.

Contributing
------------

See CONTRIBUTING.md in root of github repository.

Running The Tests
-----------------

Prior to running the tests please ensure CATIA V5 has the following
configuration settings:

* CGR cache system must be disabled.
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

* Build the docs. `cd docs` `make html`
   * Fix any issues.

* Run mypy over module. `mypy pycatia`

* Build source. ``python setup.py sdist bdist_wheel``
   * Check source contents.

* Build pycatia exe ``python -m nuitka --standalone pycatia-exe.py``.
  * use 64 env.
  * rename pycatia-exe.exe.
  * copy build to win_32 folder and zip.

* Merge changes with master branch and upload.

* Upload to pypi. ``twine upload dist/*``.

* Update github releases.