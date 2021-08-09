.. _examples:

Examples
========

The module pycatia must already be installed.

Example 1
---------

Get the center of gravity for the part body 'PartBody'.

`Example 1 <https://github.com/evereux/pycatia/blob/master/examples/example_001.py>`_


Example 2
---------

Get all the points in the geometrical set 'Points' and output co-ordinate to console.

Create your own CATPart with a Geometrical Set called construction_points. Add some points to the Geometrical Set.

`Example 2 <https://github.com/evereux/pycatia/blob/master/examples/example_002.py>`_


Example 3
---------

Find all points in the CATPart and print to console and export to csv.

`Example 3 <https://github.com/evereux/pycatia/blob/master/examples/example_003.py>`_


Example 4
---------

Loop through a CATProduct and find if sub component is a CATPart or CATProduct.

`Example 4 <https://github.com/evereux/pycatia/blob/master/examples/example_004.py>`_


Example 5
---------

Reads a csv file containing point data and adds to the new catia part.


Formatting of csv data should be:

    <point_name>,<x coordinate>,<y coordinate>,<z coordinate>

`Example 5 <https://github.com/evereux/pycatia/blob/master/examples/example_005.py>`_


Example 6
---------

Open a catia file.

Export catia file to igs.

Close a catia file.

`Example 6 <https://github.com/evereux/pycatia/blob/master/examples/example_006.py>`_


Example 7
---------

Use the context manager to open CATIA documents and close.

`Example 7 <https://github.com/evereux/pycatia/blob/master/examples/example_007.py>`_


Example 8
---------

Open all CATParts in source directory and save to IGS in target directory.

`Example 8 <https://github.com/evereux/pycatia/blob/master/examples/example_008.py>`_


Example 9
---------

Get the position matrix of products (CATPart or CATProduct) in product.

`Example 9 <https://github.com/evereux/pycatia/blob/master/examples/example_009.py>`_


Example 10
----------

Loop through a CATProduct and analyse children if CATPart.

Only goes two levels deep.

`Example 10 <https://github.com/evereux/pycatia/blob/master/examples/example_010.py>`_


Example 11
----------

Move the first child in product.

`Example 11 <https://github.com/evereux/pycatia/blob/master/examples/example_011.py>`_


Example 12
----------

Access the CATIA COM object with a .CATPart open and and display
each parameter along with its name, value and its associated parameter set.

# todo: need to create a source part to support this example.

`Example 12 <https://github.com/evereux/pycatia/blob/master/examples/example_012.py>`_


Example 13
----------

3D Points, Spline, Extrusion and Generate Thickness.

`Example 13 <https://github.com/evereux/pycatia/blob/master/examples/example_013.py>`_


Example 14
----------

Logging.

`Example 14 <https://github.com/evereux/pycatia/blob/master/examples/example_014.py>`_


Example 15
----------

Draw a line between two points.

`Example 15 <https://github.com/evereux/pycatia/blob/master/examples/example_016.py>`_


Example 16
----------

Creates a square in a sketch and fully constrains it. Sketch then used to pad.


`Example 16 <https://github.com/evereux/pycatia/blob/master/examples/example_016.py>`_


Example 17
----------

Drafting: create a border template in the background view of the currently opened A0 landscape CATDrawing.


`Example 17 <https://github.com/evereux/pycatia/blob/master/examples/example_017.py>`_


Example 18
----------

.. warning::

    With regards to pycatia this example only shows how to select the root
    product. The rest is handled by pywinauto. _https://pywinauto.github.io/

    You will need to manually install package pywinauto to run this script.
    Also, the placement of `from pywinauto import Desktop` is important.


Assembly Design: Reorder a Product tree alphabetically. The Product shall
already be loaded.

`Example 18 <https://github.com/evereux/pycatia/blob/master/examples/example_018.py>`_


Example 19
----------

Searching and changing visual properties. Find all Red points and make them
Pink.

`Example 19 <https://github.com/evereux/pycatia/blob/master/examples/example_019.py>`_


Example 20
----------

This creates a message box with the buttons abort, retry ignore and displays the Warning Query icon.

`Example 20 <https://github.com/evereux/pycatia/blob/master/examples/example_020.py>`_


Example 21
----------

Sequentially rename all points in geometric set (hybrid body) Points in the geometric set MasterGeometry.


`Example 21 <https://github.com/evereux/pycatia/blob/master/examples/example_021.py>`_


Example 22
----------

Loops through the items in hybrid body "Lines" and determine the object type using selection.

Once determined create an object from it and find it's parent(s)

Requires an active part document open with a geometrical set called
"construction_geometry" containing points generated using HybridShapePtCoord
and line generated using HybridShapeLinePtPt


`Example 22 <https://github.com/evereux/pycatia/blob/master/examples/example_022.py>`_


Example 23
----------

Fix the first Sub Product in Product using constraints. The Sketch examples
also show further usage of constraints.

`Example 23 <https://github.com/evereux/pycatia/blob/master/examples/example_023.py>`_

Example 24
----------

Basic license checking.

`Example 24 <https://github.com/evereux/pycatia/blob/master/examples/example_024.py>`_

Example 25
----------

Write the contents of a product to a html file.

`Example 25 <https://github.com/evereux/pycatia/blob/master/examples/example_025.py>`_

Example 26
----------

Prompt the user to select a product and get it's bounding box parameters

.. warning::

    Currently there must be NO other existing Measure Inertias saved
    ANYWHERE in your product tree as these may be returned and not
    product you have selected.


`Example 26 <https://github.com/evereux/pycatia/blob/master/examples/example_026.py>`_


Example 27
----------

Loop through all the CATParts in a directory and save PLAN VIEW, SIDE VIEW,
END VIEW and ISO pngs for each part.

The tree is turned off and the background turned white for the screen
capture and then turned back on.

`Example 27 <https://github.com/evereux/pycatia/blob/master/examples/example_027.py>`_


Example 28
----------

    Add new bodies to part.
    Create a cylinder in an added body.
    Do Intersection operations between two bodies..

`Example 28 <https://github.com/evereux/pycatia/blob/master/examples/example_028.py>`_
