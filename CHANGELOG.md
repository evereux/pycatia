# Changelog

## 0.2.1
* Added knowledge_ware parameter features.
* Object.path() now returns pathlib.Path() objects.
* 

## 0.1.9
* Updated setup.py due to pypi builds not scanning pycatia folder recursively.

## 0.1.8
* There have been a lot of changes at this revision. If you are upgrading from a 
  previous revision the changes will break your existing scripts (sorry!). They will 
  be mostly simply fixes to import statements. See the updated examples for ideas 
  on how you should correct them.
  
  These changes were made to allow for the future expansion of pycatia by having a 
  more modular approach (hopefully).
* module re-organisation.
* updated get_hybrid_by_name to now raise a meaningful exception if the user has 
  input a name that doesn't exist.
* many updates to the Product class properties and methods. One of the more useful
  is probably Product.apply_work_mode(). See example_4.py for example. 
* can now analyse (analyze) products for mass, volume, wet area, center of gravity 
  and inertia. See example_10.py
* enabled Product.move() method. See example_11.py

## 0.1.7
* updated pywin32 requirement so pycatia can work with later versions of python.

## 0.1.6
* Added feature to get position matrix of product. See new example 9.

## 0.1.5.1
* Attempt to fix pip installation error.

## 0.1.5
* Added unit requirement to create_points function. 
  Previously it was assumed all inputs were millimeters.
* Added missing macros file to pypi package.

## 0.1.4
* Added CATDrawing methods

## 0.1.3

* Added in_work_object method to class Part().
* Moved create_reference method to class Part(). It's proper home.
* Added find_object_by_name method to class Part().
* Added methods activate, deactivate and is_inactive to class Part().

## 0.1.2

* Added support to export files along with example.
* Updated example_3.py to show how to export the data to a csv file.

## 0.1.1

* Removed reference to CATIA V6 pre-requisite.

## 0.1.0

* Expanded tests.
* Added documentation.
* Added context manager.
* Many more changes ...

## 0.0.3

* Added ability to parse csv and create points in a CATIA part.
* Added methods to open, save, save as and close CATIA files.
* Test coverage now covers all CATMeasurable methods.
