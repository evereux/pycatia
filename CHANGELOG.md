# Changelog


## 0.4.4
Many thanks to Tian-Jionglu for his contributions.
* Improved checks for malformed filenames.
* Add method Application.setting_controllers.
* Improvements to export_data.
* Added Product.type.
* Docstring fix for Measurable.get_minimum_distance.
* Added __iter__ method to collections. 


## 0.4.3
* Updated ViewPoint3D get methods so they now work.
* Updated Viewer so Viewer2D and Viewer3D can be called.
* Fix issue #58. 
  * Change file_name argument so that it now expects Path().
  * Log warning to console if full path isn't provided.
  * Raise error if directory doesn't exist.

## 0.4.2
* Added missing methods Parameter.rename(), Parameter.valuate_from_string(), 
  and Parameter.value_as_string()
* Added missing methods DrawingThread.is_linked().
* Added the following missing methods from the class HybridShapeCurveSmooth
  * add_frozen_curve_segment() 
  * add_frozen_point
  * get_frozen_curve_segment
  * get_frozen_curve_segments_size
  * get_frozen_point
  * get_frozen_points_size
  * remove_all_frozen_curve_segments
  * remove_all_frozen_points
  * remove_frozen_curve_segment
  * remove_frozen_point
  * set_maximum_deviation
  * set_tangency_threshold

## 0.4.1
* Document.save_as() If overwrite is to true DisplayFileAlerts is set to False.
* Analyze added to Part(). 
* Updates / fixes to SettingController(s) and LicenseSettingAtt. More work to 
  be done here yet though.
* Document.add() now accepts lowercase document_types.
* Document.add() now correctly returns a document.

## 0.4.0
Breaking changes.
* The catia application object now needs to be initialized in your scripts. 
  This was done so scripts can be written in such a way that they first launch 
  CATIA V5 (or check it's actually running) before the application object is 
  initialised. Previously, the object was initialised immediately on import. Not 
  practical for some use cases. 
  For example:
```
>>> from pycatia import catia
>>> # initialise the catia application automation object.
>>> caa = catia()
>>> document = caa.active_document
```
* Removed pycatia.workbenches folder. Functionality is provided for Document object.
* Lots of bug/type fixes. Mypy is great!

* Collection objects are now directly iterable (Product.get_products() will be 
  deprecated in later release).
```
>>> from pycatia import catia
>>> caa = catia()
>>> document = caa.active_document
>>> product = document.product()
>>> products = product.products
>>> for product in produts:
>>>     print(product)
```

* Improved viewing experience of API. I hope.

## 0.3.9
* Added product.generate_ALLCATPart.
* Added product.constraints.
* Improved error message for selection.search.
* Removed product.concession (now constraints and easier to use).
* Removed application.execute_script and application.evaluate. Should use application.system_service.
   * All methods dependant on application.SystemService updated.
* Docs 
   * API CAA reference note now collapsed by default.
   * Restructured examples.
   * Added pycatia API tree for overview.
   * Changed sphinx theme to alabaster.
* Added windows executable (see win_32 folder on github). This isn't thoroughly
   tested and is provided for testing purposes.

## 0.3.8
* Updated all hybrid_shape_interfaces properties due to regression bug.
 

## 0.3.7
* Restructured API documentation.
* Added type hinting.
* Fixed issues with vis_property_set.
* Added ability to create a message box (MsgBox). See examples.


## 0.3.6
* Fixed Selection class.

## 0.3.5
* Fixed missing setting of child_object for classes that inherit from Collection
* Renamed drawing_view.factory_2d.

## 0.3.4
* Fix pypi packaging issue.

## 0.3.3
* Many updates to doc strings for methods from earlier versions.
* Product.apply_work_mode() now expects an integer. See example_010 on new usage.
* Many new modules and classes added. 

## 0.3.2
* Renamed sketcher interfaces.
* Collection object returns child_object on get_item.
* Added methods to recursively add shapes and bodies. Simple but useful.
* Remove CATIA files.
    * All tests / examples will eventually be independent of any source CATIA data.

## 0.3.1
* Added basic logging.
* Changed Point.point property name to prevent breakage of child classes.
* Added spa_workbench method to Document().

## 0.3.0a
* Major restructuring. This will break everything again. Sorry! But ... 
  this structure should now be stable. As always, see the examples.
* This is alpha software. Please note many new interfaces may not work. If that is the case please
  raise an issue.
* All .index methods are now back to starting at 1 (dictated by COM interface). This is easier for me to manage.
* Added hybrid_shape_interfaces module. 
* Added part_interfaces module.
* Still much work to do here but at least the templates are in place and are a good starting point!

## 0.2.1
* Added knowledge_ware parameter features.
* Object.path() now returns pathlib.Path() objects.

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
