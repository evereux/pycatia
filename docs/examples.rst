Examples
========

Index
-----

:ref:`ASSEMBLY CONVERTOR<Example Assembly Convertor>`

:ref:`BOM CUSTOM<Example Bom Custom>`

:ref:`CONSTRAINTS<Example Constraints>`

:ref:`DOCUMENT<Example Document>`

:ref:`DRAFTING<Example Drafting>`

:ref:`HYBRID BODIES<Example Hybrid Bodies>`

:ref:`HYBRID SHAPE FACTORY<Example Hybrid Shape Factory>`

:ref:`HYBRID SHAPE FACTORY & SHAPE FACTORY<Example Hybrid Shape Factory & Shape Factory>`

:ref:`HYBRID SKETCH & SHAPE FACTORY<Example Hybrid Sketch Factory & Shape Factory>`

:ref:`LICENSE SETTINGS<Example License Settings>`

:ref:`LOGGING<Example Logging>`

:ref:`MATERIAL INTERFACES<Example Material Interfaces>`

:ref:`MESSAGE BOX<Example Message Box>`

:ref:`PARAMETERS<Example Parameters>`

:ref:`PRODUCT<Example Product>`

:ref:`SELECTION<Example Selection>`

:ref:`SHAPE FACTORY<Example Shape Factory>`

:ref:`SPACE ANALYSIS<Example Space Analysis>`

:ref:`SPECS AND GEOMETRY WINDOW<Example Specs And Geometry Window>`

:ref:`VISUAL PROPERTIES<Example Visual Properties>`



.. _Example Assembly Convertor:

ASSEMBLY CONVERTOR
------------------

Assembly Convertor - Example 1
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Print the BOM of a product to XLS using the inbuilt AssemblyConvertor. You
must already have excel installed.

This can also be used to create TXT and HTML files.

See github issue https://github.com/evereux/pycatia/issues/110 with regards
to file paths and saying "No" to overwriting existing files and file paths
when using excel. These issues are mitigated using the code below by
checking for an existing excel file and removing it and also using pythons
pathlib.Path module.

`Asssembly Convetor - 001 <https://github.com/evereux/pycatia/blob/master/examples/example__assembly_convetor__001.py>`_


.. _Example Bom Custom:

BOM CUSTOM
----------

BOM Custom - Example 1
~~~~~~~~~~~~~~~~~~~~~~

Write the contents of a product to a html file.

`BOM Custom - 001 <https://github.com/evereux/pycatia/blob/master/examples/example__bom_custom_001.py>`_


.. _Example Constraints:

CONSTRAINTS
-----------

Constraints - Example 1
~~~~~~~~~~~~~~~~~~~~~~~

Fix the first Sub Product in Product using constraints. The Sketch examples
also show further usage of constraints.

`Constraints - 001 <https://github.com/evereux/pycatia/blob/master/examples/example__constraints_001.py>`_


.. _Example Document:

DOCUMENT
--------

Document - Example 1
~~~~~~~~~~~~~~~~~~~~

Use the context manager to open CATIA documents and close.

`Document - 001 <https://github.com/evereux/pycatia/blob/master/examples/example__document__001.py>`_


Document - Example 2
~~~~~~~~~~~~~~~~~~~~

Open all CATParts in source directory and save to IGS in target directory.

`Document - 002 <https://github.com/evereux/pycatia/blob/master/examples/example__document__002.py>`_


Document - Example 3
~~~~~~~~~~~~~~~~~~~~

Open a catia file.

Export catia file to igs.

Close a catia file.

`Document - 003 <https://github.com/evereux/pycatia/blob/master/examples/example__document__003.py.py>`_


.. _Example Drafting:

DRAFTING
--------

Drafting - Example 1
~~~~~~~~~~~~~~~~~~~~

Drafting: create a border template in the background view of the currently opened A0 landscape CATDrawing.

`Drafting - 001 <https://github.com/evereux/pycatia/blob/master/examples/example__drafting__001.py>`_


.. _Example Hybrid Bodies:

HYBRID BODIES
-------------

Hybrid Bodies - Example 1
~~~~~~~~~~~~~~~~~~~~~~~~~

Make body in work object and intersect with another body.

`Hybrid Bodies - 001 <https://github.com/evereux/pycatia/blob/master/examples/example__hybrid_bodies__001.py>`_


.. _Example Hybrid Shape Factory:

HYBRID SHAPE FACTORY
--------------------

Hybrid Shape Factory - Example 1
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Sequentially rename all points in geometric set (hybrid body) Points in the geometric set MasterGeometry.


`Hybrid Shape Factory - 001 <https://github.com/evereux/pycatia/blob/master/examples/example__hybrid_shape_factory__001.py>`_


Hybrid Shape Factory - Example 2
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Reads a csv file containing point data and adds to the new catia part.

Formatting of csv data should be:

    <point_name>,<x coordinate>,<y coordinate>,<z coordinate>

`Hybrid Shape Factory - 002 <https://github.com/evereux/pycatia/blob/master/examples/example__hybrid_shape_factory__002.py>`_


Hybrid Shape Factory - Example 3
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Draw a line between two points.

`Hybrid Shape Factory - 003 <https://github.com/evereux/pycatia/blob/master/examples/example__hybrid_shape_factory__003.py>`_


Hybrid Shape Factory - Example 4
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Loops through the items in hybrid body "Lines" and determine the object type using selection.

Once determined create an object from it and find it's parent(s)

Requires an active part document open with a geometrical set called
"construction_geometry" containing points generated using HybridShapePtCoord
and line generated using HybridShapeLinePtPt


`Hybrid Shape Factory - 004 <https://github.com/evereux/pycatia/blob/master/examples/example__hybrid_shape_factory__004.py>`_


Hybrid Shape Factory - Example 5
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

GSD: Split a surface using a plane.

Requirements: Geometrical set named "ConstructionGeometry". A surface
within the geometrical set called "Surface.1" that can be split by the
origin ZX plane.

`Hybrid Shape Factory - 005 <https://github.com/evereux/pycatia/blob/master/examples/example__hybrid_shape_factory__005.py>`_


.. _Example Hybrid Shape Factory & Shape Factory:

HYBRID SHAPE FACTORY & SHAPE FACTORY
------------------------------------


Hybrid Shape Factory & Shape Factory - Example 1
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

3D Points, Spline, Extrusion and Generate Thickness.

`Hybrid Shape Factory & Shape Factory - 001 <https://github.com/evereux/pycatia/blob/master/examples/example__hybrid_shape_factory__shape_factory__001.py>`_


.. _Example Hybrid Sketch Factory & Shape Factory:

HYBRID SKETCH & SHAPE FACTORY
-----------------------------


Hybrid Sketch & Shape Factory - Example 1
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Creates a square in a sketch and fully constrains it. Sketch then used to pad.


`Hybrid Sketch & Shape Factory - 001 <https://github.com/evereux/pycatia/blob/master/examples/example__hybrid_sketch__shape_factory__001.py>`_


.. _Example License Settings:

LICENSE SETTINGS
----------------

License Settings - Example 1
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Basic license checking.

`License Settings - 001 <https://github.com/evereux/pycatia/blob/master/examples/example__license_settings__001.py.py>`_


.. _Example Logging:

LOGGING
-------


Logging - Example 1
~~~~~~~~~~~~~~~~~~~

Logging.

`Logging - 001 <https://github.com/evereux/pycatia/blob/master/examples/example__logging__001.py>`_


.. _Example Material Interfaces:

MATERIAL INTERFACES
-------------------


Material - Example 1
~~~~~~~~~~~~~~~~~~~~

CATMatInterfaces
        
Opens the material catalog and retrieves the first few materials.

Creates a new part and applies the material to the part, the main body and a
hybrid body.

Creates a new product and applies the material to it.

`Material - 001 <https://github.com/evereux/pycatia/blob/master/examples/example__material__001.py>`_


.. _Example Message Box:

MESSAGE BOX
-----------

Message Box - Example 1
~~~~~~~~~~~~~~~~~~~~~~~

This creates a message box with the buttons abort, retry ignore and displays the Warning Query icon.

`Message Box - 001 <https://github.com/evereux/pycatia/blob/master/examples/example__message_box__001.py>`_


.. _Example Parameters:

PARAMETERS
----------

Parameters - Example 1
~~~~~~~~~~~~~~~~~~~~~~

Access the CATIA COM object with a .CATPart open and and display
each parameter along with its name, value and its associated parameter set.

# todo: need to create a source part to support this example.

`Parameters - 001 <https://github.com/evereux/pycatia/blob/master/examples/example__parameters__001.py>`_


.. _Example Product:

PRODUCT
-------

Product - Example 1
~~~~~~~~~~~~~~~~~~~

.. warning::

    With regards to pycatia this example only shows how to select the root
    product. The rest is handled by pywinauto. _https://pywinauto.github.io/

    You will need to manually install package pywinauto to run this script.
    Also, the placement of `from pywinauto import Desktop` is important.


Assembly Design: Reorder a Product tree alphabetically. The Product shall
already be loaded.

`Product - 001 <https://github.com/evereux/pycatia/blob/master/examples/example__product__001.py>`_


Product - Example 2
~~~~~~~~~~~~~~~~~~~

Move the first child in product.

`Product - 002 <https://github.com/evereux/pycatia/blob/master/examples/example__product__002.py>`_


Product - Example 3
~~~~~~~~~~~~~~~~~~~

Loop through a CATProduct and analyse children if CATPart.

Only goes two levels deep.

`Product - 003 <https://github.com/evereux/pycatia/blob/master/examples/example_010.py>`_



Product - Example 4
~~~~~~~~~~~~~~~~~~~

Get the position matrix of products (CATPart or CATProduct) in product.

`Product - 004 <https://github.com/evereux/pycatia/blob/master/examples/example__product__004.py>`_


Product - Example 5
~~~~~~~~~~~~~~~~~~~

Loop through a CATProduct and find if sub component is a CATPart or CATProduct.

`Prodcut - 005 <https://github.com/evereux/pycatia/blob/master/examples/example__product__005.py>`_


Product - Example 6
~~~~~~~~~~~~~~~~~~~

Get the Inertia of a product using product.get_technical object and print it's mass.

`Prodcut - 006 <https://github.com/evereux/pycatia/blob/master/examples/example__product__006.py>`_


.. _Example Selection:

SELECTION
---------

Selection - Example 1
~~~~~~~~~~~~~~~~~~~~~

Prompt the user to select a product and get it's bounding box parameters

.. warning::

    Currently there must be NO other existing Measure Inertias saved
    ANYWHERE in your product tree as these may be returned and not
    product you have selected.


`Selection - 001 <https://github.com/evereux/pycatia/blob/master/examples/example__selection__001.py>`_


.. _Example Shape Factory:

SHAPE FACTORY
-------------

Shape Factory - Example 1
~~~~~~~~~~~~~~~~~~~~~~~~~

Add new bodies to part.
Create a cylinder in an added body.
Do Intersection operations between two bodies..

`Shape Factory - 001 <https://github.com/evereux/pycatia/blob/master/examples/example__shape_factory__001.py>`_


Shape Factory - Example 2
~~~~~~~~~~~~~~~~~~~~~~~~~

Mirror the main body of the part using shape_factory.add_new_symmetry_2.
`Shape Factory - 002 <https://github.com/evereux/pycatia/blob/master/examples/example__shape_factory__002.py>`_


.. _Example Space Analysis:

SPACE ANALYSIS
--------------


Space Analysis - Example 1
~~~~~~~~~~~~~~~~~~~~~~~~~~

Get the center of gravity for the part body 'PartBody'.

`Space Analysis - 001 <https://github.com/evereux/pycatia/blob/master/examples/example__space_analysis__001.py>`_


Space Analysis - Example 2
~~~~~~~~~~~~~~~~~~~~~~~~~~

Get all the points in the geometrical set 'Points' and output co-ordinate to console.

Create your own CATPart with a Geometrical Set called construction_points. Add some points to the Geometrical Set.

`Space Analysis - 002 <https://github.com/evereux/pycatia/blob/master/examples/example__space_analysis__002.py>`_


Space Analysis - Example 3
~~~~~~~~~~~~~~~~~~~~~~~~~~

Find all points in the CATPart and print to console and export to csv.

`Example 3 <https://github.com/evereux/pycatia/blob/master/examples/example__space_analysis__003.py>`_


SPECS AND GEOMETRY WINDOW
-------------------------


.. _Example Specs And Geometry Window:

Specs And Geometry Window - Example 1
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Loop through all the CATParts in a directory and save PLAN VIEW, SIDE VIEW,
END VIEW and ISO pngs for each part.

The tree is turned off and the background turned white for the screen
capture and then turned back on.

`Specs And Geometry Window - 001 <https://github.com/evereux/pycatia/blob/master/examples/example__specs_and_geom_window__001.py>`_


.. _Example Visual Properties:

VISUAL PROPERTIES
-----------------

Visual Properties - Example 1
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Searching and changing visual properties. Find all Red points and make them
Pink.

`Visual Properties - 001 <https://github.com/evereux/pycatia/blob/master/examples/example__visual_properties__001.py>`_
