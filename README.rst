pycatia
=======

pycatia currently only contains access to the CATIA API Measurable 
object and it's methods without the need of visual basic / CATScripts.
pycatia also provides easy to use python methods to loop through a
product and it's children.

Some of the methods can be accessed simply using the pywin32 module but further 
access to methods such as GetCOG do not seem to be accessible using pure python.
There are several questions on stack overflow and the pywin32 mailing list regarding
this. But, they fail to provide any working examples with the VB Measurable object 
in python. 

pycatia accesses these methods by running VBA scripts using the 
`Dispatch('CATIA.Application').SystemService.Evaluate()` function where required
and passing a small public function to it. Otherwise, pycatia uses the VB method
directly but exposes it within the same python class.

This has currently only been tested in CATIA V5 R21.

Requirements
------------

* python >= 3.6 
* CATIA V5/V6
* see requirements.txt

Installation
------------

with pip
~~~~~~~~

.. code-block:: python

    pip install pycatia

with git
~~~~~~~~

Clone the master branch from github into your working folder.

.. code-block:: python

    git clone https://github.com/evereux/pycatia.git

download zip
~~~~~~~~~~~~
.. _master_branch.zip: https://github.com/evereux/pycatia/archive/master.zip

Download and unpack the  master_branch.zip_


Usage
-----

This example shows how to get the first point in the geometrical set 'Points'.

.. code-block:: python

    # initial set-up to get access to the CATIA COM objects.
    import pycatia
    catia = pycatia.CATIAApplication()
    document = pycatia.Document(catia.catia)
    part = pycatia.Part(document.document)
    spa_workbench = pycatia.create_spa_workbench(document.document)

    # find the geometrical set by name called 'Points'
    hybrid_body = part.get_hybrid_body_by_name('Points')

    # get the first point in the geometrical set.
    point1 = hybrid_body.HybridShapes.Item(1)

    # create the reference and measurable objects
    point1_reference = pycatia.create_reference(part.part, point1)
    point1_measurable = pycatia.create_measurable(spa_workbench, point1_reference)

    # create the catia measurable object
    measurable = pycatia.CATIAMeasurable(point1_measurable)

    # run the get_point() method from CATIAMeasurable.
    point_coordinate = measurable.get_point()
    # point_coordinate is a tuple representing it's x, y, z values.
    print(point_coordinate)

    # outputs (0.0, 8.0, -4.0)
    # print x
    print(point_coordinate[0]
    # output 0,0

For a complete list of methods available on a measurable object see
the class CATIAMeasurable in `measurable.py`.

Links
-----
.. _pycatia.readthedocs.io: https://pycatia.readthedocs.io
.. _pypi.org: https://pypi.org/project/pycatia/

Documentation: pycatia.readthedocs.io_.

Releases: pycatia @ pypi.org_

Examples
--------

.. _example_1: https://github.com/evereux/pycatia/blob/master/example_1.py
.. _example_2: https://github.com/evereux/pycatia/blob/master/example_2.py
.. _example_3: https://github.com/evereux/pycatia/blob/master/example_3.py
.. _example_4: https://github.com/evereux/pycatia/blob/master/example_4.py
.. _example_5: https://github.com/evereux/pycatia/blob/master/example_5.py
.. _example_6: https://github.com/evereux/pycatia/blob/master/example_6.py
.. _example_6: https://github.com/evereux/pycatia/blob/master/example_7.py

1. Open the file catia_measurable.CATPart from the folder tests.
2. Run the example scripts.

   example_1_

   Shows how to access the CATIA COM object with a .CATPart open and
   get the center of gravity for the part body 'PartBody'.
    
   example_2_

   Shows how to get all the points in the geometrical set 'Points' and
   get the co-ordinate.
    
   example_3_
    
   Shows how to search for all points in the document and return the
   co-ordinates.

   example_4_

   Shows how to loop through a product and determine whether child is
   a CATProduct or CATPart.

   example_5_

   Shows how to parse and csv file and create points in a CATIA part.

   example_6_

   Examples of how to open, save as and close a CATIA file.

   example_7_

   Example of how open a document using the context manager.
    
Running The Tests
-----------------
To run the tests with coverage:

.. code-block:: python

    py.test -v --cov-report term-missing --cov=pycatia
