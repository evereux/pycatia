Examples
========

The module pycatia must already be installed. CATIA sample files are available within the `github <https://github.com/evereux/pycatia/tree/master/tests>`_. repository.

Example 1
---------

Access the CATIA COM object with a .CATPart open and get the center of gravity for the part body 'PartBody'.

.. literalinclude:: ..\example_1.py

Example 2
---------

Get all the points in the geometrical set 'Points' and print the co-ordinate.

.. literalinclude:: ..\example_2.py

Example 3
---------

Find all points in the CATPart and print it's co-ordinate.

.. literalinclude:: ..\example_3.py

Example 4
---------

Loop through a CATProduct and find if sub component is a CATPart or CATProduct.

.. literalinclude:: ..\example_4.py

Example 5
---------

Reads a csv file containing point data and adds to the active catia part.

.. literalinclude:: ..\example_5.py

Example 6
---------

Open a catia file and close a catia file.

.. literalinclude:: ..\example_6.py