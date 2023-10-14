# Changelog

## 0.6.1

* Added human modelling classes SWKHmiWorkbench and SWKHumanCatalog. Please note these are not documented in the CATIA
  V5 Basic Help file. Example of usage also added.
* Added new class method Application.input_box(). @ptm-tm
* fixed test issue with cat materials where catia env has multiple start-up paths.
* fixed issue with HybridShapeFactory.add_new_sphere for cases where an axis isn't defined.
* fixes to RenderingMaterials class methods. @deloarts
* added new enum type geometrical_feature_type to support HybridShapeFactory.get_geometrical_feature_type().

## 0.6.0

* Removed deprecated method Product.get_products() use Product.products instead.
* Added the following new modules:
    * abq_automation_interfaces
    * analysis_interfaces
    * arrangement_interfaces
    * assembly_interfaces
    * behaviour_interfaces
    * bkt_interfaces
    * cat_dde_settings_interfaces
    * cat_ipd_adapter_interfaces
    * cat_plant_ship_interfaces (PSP)
    * cat_rdg_interfaces
    * cat_rsc_interfaces
    * cat_sch_platform_interfaces
    * cat_sde_interfaces
    * cat_sm_interfaces
    * cat_smarteam_integ_interfaces
    * cat_str_functional_interfaces
    * cat_tps_interfaces
    * catia_v4_interfaces
    * catia_de_settings_interfaces
    * composites_interfaces
    * dnb_asy_activity_interfaces
    * dnb_d5_interfaces
    * dnb_device_activity_interfaces
    * dnb_device_interfaces
    * dnb_dpm_interfaces
    * dnb_ehm_interfaces
    * dnb_ehs_interfaces
    * dnb_ekp_interfaces
    * dnb_fastener_interfaces
    * dnb_graph_editor
    * dnb_human_modelling_interfaces
    * dnb_human_sim_interfaces
    * dnb_igp_arc_commands
    * dnb_lgp_olp_ui
    * dnb_igp_setup_interfaces
    * dnb_manufacturing_layout_interfaces
    * dnb_mhi_interfaces
    * dnb_reporting_interfaces
    * dnb_resource_program_interfaces
    * dnb_robot_interfaces
    * dnb_sim_activity_interfaces
    * dnb_simulation_interfaces
    * dnb_sor_interfaces
    * dnb_state_interfaces
    * dnb_work_interfaces
    * dmaps_interfaces
    * drafting_2dl_interfaces
    * electrical_schematic_interfaces
    * eno_cd5_interfaces
    * fitting_interfaces
    * general_knowledge_interfaces
    * kinematics_interfaces
    * manufacturing_interfaces
    * multi_cad_interfaces
    * osm_interfaces
    * pcb_board_base
    * ppr_interfaces
    * prismatic_machining_interfaces
    * reporter_interfaces
    * simulation_interfaces
    * smt_interfaces
    * structure_interfaces
    * surface_machining_interfaces
    * threed_xml_interfaces

## 0.5.9

* Added missing com_oject to references in navigator_interfaces. (@evereux & @marciolrc)
* Fixed reference plane method in HybridShapePlaneAngle. (@Mithro86)
* Updates to examples to include latest supported python version. Also fix IDE autocompletion & syntax highlighting
  issues. (@deloarts)

## 0.5.8

* Added new document type CatalogDocument.
* Added new document type CATMaterial.
* fixed method for AxisSystem.origin_point, AxisSystem.x_axis_direction, AxisSystem.y_axis_direction and
  AxisSystem.z_axis_direction. (@Mithro86)
* Added warning to example__assembly_convertor__001.py for when writing to files. (@deloarts)
* fixed method for Limit.limiting_element(). (@ptm-tm)

## 0.5.7

* fixed method for VisPropertySet.get_show(). (@Mithro86)
* fixed method for AxisSystem.get_vectors(). (@Mithro86)
* Partial fix to Selection.indicate_or_select_element_3d(). (@Mithro86)
* added pathlib.Path to DrawingPictures.add().
    * now tries to get the Windows absolute path from input as CATIA may not be able to otherwise find the file.
* References to python 3.6 now updated to 3.9 due to type annotation support.
* fixed method for Line.get_direction(). (@Mithro86)

## 0.5.6

* fixed method for DrawingDimension.get_tolerances()
* fixed method for DrawingDimension.get_clip().
* added new method shape_factory.add_new_symmetry_2 (@deloarts).
* added example
* restructured examples into categories.

## 0.5.5

* added material interfaces (@deloarts). See examples.
* fixed Documents.read(). It now returns a pycatia document object
  (@Alexander via email).

## 0.5.4

* fixed method in pycatia/hybrid_shape_interfaces/hybrid_shape_plane_offset_pt
* fixed method in pycatia/product_structure_interfaces/assembly_convertor.print

## 0.5.3

* fixed methods in pycatia/mec_mod_interfaces/axis_system and pycatia/mec_mod_interfaces/cylindrical_face.py that
  required mapping to VBA methods.

## 0.5.2

* Added missing delimeters to vba_functions in sketcher_interfaces/curve_2D.py

## 0.5.1

* Fix bug with HybridShapeFactory.add_new_datums().

## 0.5.0

* Added tps_interfaces.
* Document() no longer contains methods specific to Parts, Products and Drawings. This will most likely break your
  scripts. Please see updated examples. These methods / properties are now only available in PartDocument,
  ProductDocument and DrawingDocument. Example:

```python
from pycatia import catia

caa = catia()
documents = caa.documents
documents.open(r'tests/cat_files/part_measurable.CATPart')

# get the active document
document = caa.active_document
# get the Part() object. NOTE THIS IS NOW A PROPERTY, NOT A METHOD.
part = document.part
```

* Removed requirements from setup.py which are installed by pytest.

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

* Added missing methods Parameter.rename(), Parameter.valuate_from_string(), and Parameter.value_as_string()
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
* Updates / fixes to SettingController(s) and LicenseSettingAtt. More work to be done here yet though.
* Document.add() now accepts lowercase document_types.
* Document.add() now correctly returns a document.

## 0.4.0

Breaking changes.

* The catia application object now needs to be initialized in your scripts. This was done so scripts can be written in
  such a way that they first launch CATIA V5 (or check it's actually running) before the application object is
  initialised. Previously, the object was initialised immediately on import. Not practical for some use cases. For
  example:

```
>>> from pycatia import catia
>>> # initialise the catia application automation object.
>>> caa = catia()
>>> document = caa.active_document
```

* Removed pycatia.workbenches folder. Functionality is provided for Document object.
* Lots of bug/type fixes. Mypy is great!

* Collection objects are now directly iterable (Product.get_products() will be deprecated in later release).

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
* Added windows executable (see win_32 folder on github). This isn't thoroughly tested and is provided for testing
  purposes.

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

* Major restructuring. This will break everything again. Sorry! But ... this structure should now be stable. As always,
  see the examples.
* This is alpha software. Please note many new interfaces may not work. If that is the case please raise an issue.
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

* There have been a lot of changes at this revision. If you are upgrading from a previous revision the changes will
  break your existing scripts (sorry!). They will be mostly simply fixes to import statements. See the updated examples
  for ideas on how you should correct them.

  These changes were made to allow for the future expansion of pycatia by having a more modular approach (hopefully).
* module re-organisation.
* updated get_hybrid_by_name to now raise a meaningful exception if the user has input a name that doesn't exist.
* many updates to the Product class properties and methods. One of the more useful is probably Product.apply_work_mode()
  . See example_4.py for example.
* can now analyse (analyze) products for mass, volume, wet area, center of gravity and inertia. See example_10.py
* enabled Product.move() method. See example_11.py

## 0.1.7

* updated pywin32 requirement so pycatia can work with later versions of python.

## 0.1.6

* Added feature to get position matrix of product. See new example 9.

## 0.1.5.1

* Attempt to fix pip installation error.

## 0.1.5

* Added unit requirement to create_points function. Previously it was assumed all inputs were millimeters.
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
* Test coverage now covers