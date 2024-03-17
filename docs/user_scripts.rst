.. _user_scripts:

User Scripts
============

User created scripts that are more advanced than the :ref:`examples`.

Index
-----


:ref:`CREATE BOUNDING BOX<Create Bounding Box>`

:ref:`CREATE SCREENSHOTS OF PARTS AND PRODUCTS<Create Screenshots Of Parts and Products>`

:ref:`CREATE LINES NORMAL TO SURFACE<Create Lines Normal To Surface>`

:ref:`CREATE PARAMETERS FROM YAML<Create Parameters From YAML>`

:ref:`DRAWING TEMPLATE<Drawing Template>`

:ref:`POINT COORDINATES RELATIVE TO AXIS SYSTEM<Point Coordinates Relative To Axis System>`

:ref:`RENAME INSTANCES IN PRODUCT<Rename Instances In Product>`

:ref:`SAVE DRAWINGS TO PDF<Save Drawings To PDF>`

:ref:`WING SURFACE FROM NACA PROFILE<Wing Surface From Naca Profile>`




CREATE BOUNDING BOX
-------------------

Creates a bounding box around the selected Body using the selected AxisSystem
to orientate the bounding box.

See script header for more information.

`create_bounding_box.py <https://github.com/evereux/pycatia/blob/master/user_scripts/create_bounding_box.py>`_



CREATE SCREENSHOTS OF PARTS AND PRODUCTS
----------------------------------------

Creates screenshots of all parts and products within a given directory.

See script header for more information.

`create_screenshots_of_parts_and_products.py <https://github.com/evereux/pycatia/blob/master/user_scripts/create_screenshots_of_parts_and_products.py>`_



CREATE LINES NORMAL TO SURFACE
------------------------------

Creates lines normal to surface using all the points in the selected Geometrical
Set.

Image showing surface and points.

.. image:: images/lines_normal_surface_1.png


Image showing lines after script has been run.

.. image:: images/lines_normal_surface_2.png

See script header for more information.

`create_lines_normal_to_surface.py <https://github.com/evereux/pycatia/blob/master/user_scripts/create_lines_normal_to_surface.py>`_



CREATE PARAMETERS FROM YAML
---------------------------

Creates parameter sets and parameters based on the contents of a YAML file.

Great for creating complex parameter structures.

See script header for more information.

.. image:: images/parameters.png

`create_parameters_from_yaml.py <https://github.com/evereux/pycatia/blob/master/user_scripts/create_parameters_from_yaml.py>`_



DRAWING TEMPLATE
----------------

Creating a drawing template in the background view.

See script header for more information.

.. image:: images/DrawingTemplate.png

`drawing_template.py <https://github.com/evereux/pycatia/blob/master/user_scripts/drawing_template.py>`_



POINT COORDINATES RELATIVE TO AXIS SYSTEM
-----------------------------------------

Get the point coordinates relative to an axis system.

See script header for more information.

`coords_relative_to_axis_system.py <https://github.com/evereux/pycatia/blob/master/user_scripts/coords_relative_to_axis_system.py>`_



RENAME INSTANCES IN PRODUCT
---------------------------

Sequentially renames the instances of products within a selected product.

See script header for more information.

`rename_instances_in_product.py <https://github.com/evereux/pycatia/blob/master/user_scripts/rename_instances_in_product.py>`_



SAVE DRAWINGS TO PDF
--------------------

Loops through all the files (.CATDrawing) of a given directory and saves to
PDF.

For CATDrawings the Document.export_data() method exports each sheet to a
single PDF. This script uses pypdf to merge these single sheets into a
single pdf for each drawing.

See script header for more information.

`save_drawings_to_pdf.py <https://github.com/evereux/pycatia/blob/master/user_scripts/save_drawings_to_pdf.py>`_


WING SURFACE FROM NACA PROFILE
------------------------------

Reads the contents of the NACA dat file `sc20610.dat` to create a wing surface.

See script header for more information.

.. image:: images/WingSurface.png

`wing_surface_from_naca_profile.py <https://github.com/evereux/pycatia/blob/master/user_scripts/wing_surface_from_naca_profile.py>`_
