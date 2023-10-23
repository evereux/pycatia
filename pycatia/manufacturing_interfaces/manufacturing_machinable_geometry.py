#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.manufacturing_interfaces.manufacturing_machinable_feature import ManufacturingMachinableFeature
from pycatia.product_structure_interfaces.product import Product
from pycatia.system_interfaces.any_object import AnyObject
from pycatia.types.general import cat_variant


class ManufacturingMachinableGeometry(ManufacturingMachinableFeature):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                    ManufacturingInterfaces.ManufacturingFeature
                |                        ManufacturingInterfaces.ManufacturingMachinableFeature
                |                             ManufacturingMachinableGeometry
                | 
                | Represents the machinable geometry object.
                | It is the low-level component of a machinable area.
                | 
                | See also:
                |     ManufacturingMachinableArea
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.manufacturing_machinable_geometry = com_object

    @property
    def shared(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Shared() As boolean
                | 
                |     Returns or sets the shared state of a ManufacturingMachinableGeometry
                |     object. 
                | Example:
                |     The following example returns in bState the shared state of manufacturing
                |     machinable geometry firstMachGeom and then sets it to
                |     TRUE:
                | 
                |      Dim firstMachGeom As ManufacturingMachinableGeometry
                |      Set firstMachGeom = ...
                |      Dim bState As boolean
                |      Set bState = firstMachGeom.Shared
                |      bState = TRUE
                |      firstMachGeom.Shared = bState

        :rtype: bool
        """

        return self.manufacturing_machinable_geometry.Shared

    @shared.setter
    def shared(self, value: bool):
        """
        :param bool value:
        """

        self.manufacturing_machinable_geometry.Shared = value

    def add_pointed_geometry(self, i_geometry: AnyObject, i_product: Product, i_shapes: tuple) -> cat_variant:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub AddPointedGeometry(AnyObject iGeometry,
                | Product iProduct,
                | CATSafeArrayVariant iShapes)
                | 
                |     Adds a geometry to the pointed geometry list.
                | 
                |     Parameters:
                | 
                |         iGeometry
                |             The geometry to add 
                |         iProduct
                |             The product where the geometry to add is located 
                |         iShapes
                |             The list of shapes (body copied and pasted with links) where the
                |             geometry is to be added 
                | 
                |     Example:
                |         The following example adds the geometry GeomToAdd of the product
                |         ProdOfGeomToAdd to the pointed geometry list of the manufacturing machinable
                |         geometry firstMachGeom.
                | 
                |          Dim firstMachGeom As ManufacturingMachinableGeometry
                |          Set firstMachGeom = ...
                |          Dim GeomToAdd As Shape
                |          Dim ProdOfGeomToAdd As Product
                |          Set GeomToAdd = ...
                |          Set ProdOfGeomToAdd = ...
                |          Dim ShapesList() As Variant
                |          Redim ShapesList(0) ' Create an empty list of shapes
                |          Call firstMachGeom.AddPointedGeometry( GeomToAdd, ProdOfGeomToAdd,
                |          ShapesList )

        :param AnyObject i_geometry:
        :param Product i_product:
        :param tuple i_shapes:
        :rtype: cat_variant
        """
        return self.manufacturing_machinable_geometry.AddPointedGeometry(
            i_geometry.com_object,
            i_product.com_object,
            i_shapes)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'add_pointed_geometry'
        # # vba_code = """
        # # Public Function add_pointed_geometry(manufacturing_machinable_geometry)
        # #     Dim iGeometry (2)
        # #     manufacturing_machinable_geometry.AddPointedGeometry iGeometry
        # #     add_pointed_geometry = iGeometry
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def add_pointed_geometry_notify(
            self,
            i_geometry: AnyObject,
            i_product: Product,
            i_shapes: tuple,
            i_notify: int
    ) -> cat_variant:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub AddPointedGeometryNotify(AnyObject iGeometry,
                | Product iProduct,
                | CATSafeArrayVariant iShapes,
                | short iNotify)
                | 
                |     Adds a geometry to the pointed geometry list (manage
                |     notification).
                | 
                |     Parameters:
                | 
                |         iGeometry
                |             The geometry to add 
                |         iProduct
                |             The product where the geometry to add is located 
                |         iShapes
                |             The list of shapes (body copied and pasted with links) where the
                |             geometry is to be added 
                |         iNotify
                |             A flag to request whether to send a notification to update the
                |             model
                |             Legal values:
                |             0 No notification is sent and the model is not
                |             updated
                |             1 A notification is sent and the model is updated
                | 
                |     Example:
                |         The following example adds the geometry GeomToAdd of the product
                |         ProdOfGeomToAdd to the pointed geometry list of the manufacturing machinable
                |         geometry firstMachGeom.
                | 
                |          Dim firstMachGeom As ManufacturingMachinableGeometry
                |          Set firstMachGeom = ...
                |          Dim GeomToAdd As Shape
                |          Dim ProdOfGeomToAdd As Product
                |          Set GeomToAdd = ...
                |          Set ProdOfGeomToAdd = ...
                |          Dim ShapesList() As Variant
                |          Redim ShapesList(0) ' Create an empty list of shapes
                |          Call firstMachGeom.AddPointedGeometryNotify( GeomToAdd,
                |          ProdOfGeomToAdd, ShapesList, 0 )

        :param AnyObject i_geometry:
        :param Product i_product:
        :param tuple i_shapes:
        :param int i_notify:
        :rtype: cat_variant
        """
        return self.manufacturing_machinable_geometry.AddPointedGeometryNotify(
            i_geometry.com_object,
            i_product.com_object,
            i_shapes,
            i_notify
        )
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'add_pointed_geometry_notify'
        # # vba_code = """
        # # Public Function add_pointed_geometry_notify(manufacturing_machinable_geometry)
        # #     Dim iGeometry (2)
        # #     manufacturing_machinable_geometry.AddPointedGeometryNotify iGeometry
        # #     add_pointed_geometry_notify = iGeometry
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def add_pointed_geometry_with_no_duplicated_check(
            self,
            i_geometry: AnyObject,
            i_product: Product,
            i_shapes: tuple
    ) -> cat_variant:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub AddPointedGeometryWithNoDuplicatedCheck(AnyObject
                | iGeometry,
                | Product iProduct,
                | CATSafeArrayVariant iShapes)
                | 
                |     Adds a geometry to the pointed geometry list with no check on already
                |     referenced geometry.
                | 
                |     Parameters:
                | 
                |         iGeometry
                |             The geometry to add 
                |         iProduct
                |             The product where the geometry to add is located 
                |         iShapes
                |             The list of shapes (body copied and pasted with links) where the
                |             geometry is to be added 
                | 
                |     Example:
                |         The following example adds the geometry GeomToAdd of the product
                |         ProdOfGeomToAdd to the pointed geometry list of the manufacturing machinable
                |         geometry firstMachGeom.
                | 
                |          Dim firstMachGeom As ManufacturingMachinableGeometry
                |          Set firstMachGeom = ...
                |          Dim GeomToAdd As Shape
                |          Dim ProdOfGeomToAdd As Product
                |          Set GeomToAdd = ...
                |          Set ProdOfGeomToAdd = ...
                |          Dim ShapesList() As Variant
                |          Redim ShapesList(0) ' Create an empty list of shapes
                |          Call firstMachGeom.AddPointedGeometryWithNoDuplicatedCheck( GeomToAdd,
                |          ProdOfGeomToAdd, ShapesList )

        :param AnyObject i_geometry:
        :param Product i_product:
        :param tuple i_shapes:
        :rtype: cat_variant
        """
        return self.manufacturing_machinable_geometry.AddPointedGeometryWithNoDuplicatedCheck(i_geometry.com_object,
                                                                                              i_product.com_object,
                                                                                              i_shapes)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'add_pointed_geometry_with_no_duplicated_check'
        # # vba_code = """
        # # Public Function add_pointed_geometry_with_no_duplicated_check(manufacturing_machinable_geometry)
        # #     Dim iGeometry (2)
        # #     manufacturing_machinable_geometry.AddPointedGeometryWithNoDuplicatedCheck iGeometry
        # #     add_pointed_geometry_with_no_duplicated_check = iGeometry
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def add_pointed_geometry_with_no_duplicated_check_notify(
            self,
            i_geometry: AnyObject,
            i_product: Product,
            i_shapes: tuple,
            i_notify: int
    ) -> cat_variant:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub AddPointedGeometryWithNoDuplicatedCheckNotify(AnyObject
                | iGeometry,
                | Product iProduct,
                | CATSafeArrayVariant iShapes,
                | short iNotify)
                | 
                |     Adds a geometry to the pointed geometry list with no check on an already
                |     referenced geometry.
                | 
                |     Parameters:
                | 
                |         iGeometry
                |             The geometry to add 
                |         iProduct
                |             The product where the geometry to add is located 
                |         iShapes
                |             The list of shapes (body copied and pasted with links) where the
                |             geometry is to be added 
                |         iNotify
                |             A flag to request whether to send a notification to update the
                |             model
                |             Legal values:
                |             0 No notification is sent and the model is not
                |             updated
                |             1 A notification is sent and the model is updated
                | 
                |     Example:
                |         The following example adds the geometry GeomToAdd of the product
                |         ProdOfGeomToAdd to the pointed geometry list of the manufacturing machinable
                |         geometry firstMachGeom:
                | 
                |          Dim firstMachGeom As ManufacturingMachinableGeometry
                |          Set firstMachGeom = ...
                |          Dim GeomToAdd As Shape
                |          Dim ProdOfGeomToAdd As Product
                |          Set GeomToAdd = ...
                |          Set ProdOfGeomToAdd = ...
                |          Dim ShapesList() As Variant
                |          Redim ShapesList(0) ' Create an empty list of shapes
                |          Call firstMachGeom.AddPointedGeometryWithNoDuplicatedCheckNotify(
                |          GeomToAdd, ProdOfGeomToAdd, ShapesList, 0 )

        :param AnyObject i_geometry:
        :param Product i_product:
        :param tuple i_shapes:
        :param int i_notify:
        :rtype: cat_variant
        """
        return self.manufacturing_machinable_geometry.AddPointedGeometryWithNoDuplicatedCheckNotify(
            i_geometry.com_object,
            i_product.com_object,
            i_shapes,
            i_notify
        )
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'add_pointed_geometry_with_no_duplicated_check_notify'
        # # vba_code = """
        # # Public Function add_pointed_geometry_with_no_duplicated_check_notify(manufacturing_machinable_geometry)
        # #     Dim iGeometry (2)
        # #     manufacturing_machinable_geometry.AddPointedGeometryWithNoDuplicatedCheckNotify iGeometry
        # #     add_pointed_geometry_with_no_duplicated_check_notify = iGeometry
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_associated_tps(self, index_of_pointed_geom: int, o_annotations_list: tuple) -> cat_variant:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetAssociatedTPS(long IndexOfPointedGeom,
                | CATSafeArrayVariant oAnnotationsList)
                |
                |     Retrieves the Annotation object lists associated with a
                |     ManufacturingMachinableGeometry object.
                |
                |     Parameters:
                |
                |         IndexOfPointedGeom
                |             The index of the pointed geometry among those associated with the
                |             ManufacturingMachinableGeometry object
                |         oAnnotationsList
                |             The retrieved list Annotation objects.
                |             The array must be previously initialized using the
                |
                |
                |         GetAssociatedTPSCount method.
                |
                | Example:
                |     The following example retrieves the Annotation object list of the third
                |     pointed geometry under the manufacturing machinable geometry firstMachGeom in
                |     AnnotationList:
                |
                |      Dim firstMachGeom As ManufacturingMachinableGeometry
                |      Set firstMachGeom = ...
                |      Dim AssociatedTPSCount As Long
                |      AssociatedTPSCount = firstMachGeom.GetAssociatedTPSCount (2)
                |      If (AssociatedTPSCount > 0) Then
                |        Dim I As Long
                |
                |        Dim AnnotationList() As Variant
                |        Redim AnnotationList(AssociatedTPSCount-1)
                |        Call firstMachGeom.GetAssociatedTPS(2, AnnotationList)
                |
                |      End If

        :param int index_of_pointed_geom:
        :param tuple o_annotations_list:
        :rtype: Variant
        """
        return self.manufacturing_machinable_geometry.GetAssociatedTPS(
            index_of_pointed_geom,
            o_annotations_list
        )
        # # # # Autogenerated comment:
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_associated_tps'
        # # vba_code = """
        # # Public Function get_associated_tps(manufacturing_machinable_geometry)
        # #     Dim IndexOfPointedGeom (2)
        # #     manufacturing_machinable_geometry.GetAssociatedTPS IndexOfPointedGeom
        # #     get_associated_tps = IndexOfPointedGeom
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_associated_tps_count(self, index_of_pointed_geom: int) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetAssociatedTPSCount(long IndexOfPointedGeom) As
                | long
                |
                |     Returns the number of Annotation objects attached to a pointed geometry
                |     under a ManufacturingMachinableGeometry object.
                |
                |     Parameters:
                |
                |         IndexOfPointedGeom
                |             The index of the pointed geometry
                |             Note: Check that the index you are passing in less than or equal to
                |             the pointed geometry count retrieved using the
                |
                |         PointedGeometryCount method.
                |     oAnnotationsListCount
                |         The number of Annotation objects
                |
                | Example:
                |     The following example retrieves the number of Annotation objects attached
                |     to the third geometry under the manufacturing machinable geometry firstMachGeom
                |     in AssociatedTPSCount:
                |
                |      Dim firstMachGeom As ManufacturingMachinableGeometry
                |      Set firstMachGeom = ...
                |      Dim AssociatedTPSCount As Long
                |      AssociatedTPSCount = PointedGeometryListSize = firstMachGeom.GetAssociatedTPSCount( 3 )

        :param int index_of_pointed_geom:
        :rtype: int
        """
        return self.manufacturing_machinable_geometry.GetAssociatedTPSCount(index_of_pointed_geom)

    def get_direction(self, o_x: float, o_y: float, o_z: float, index_of_pointed_geom: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetDirection(double oX,
                | double oY,
                | double oZ,
                | long IndexOfPointedGeom)
                |
                |     Retrieves the direction of a pointed geometry under a
                |     ManufacturingMachinableGeometry object.
                |     Note: Currently valid only for AxialUDF and DesignHole
                |     features.
                |
                |     Parameters:
                |
                |         oX,oY,oZ
                |             The components of the direction
                |         IndexOfPointedGeom
                |             The index of the pointed geometry
                |             Note: Check that the index you are passing in less than or equal to
                |             the pointed geometry count retrieved using the
                |
                |         PointedGeometryCount method.
                |
                | Example:
                |     The following example retrieves the components of the direction of the
                |     third geometry under the manufacturing machinable geometry
                |     firstMachGeom:
                |
                |      Dim firstMachGeom As ManufacturingMachinableGeometry
                |      Set firstMachGeom = ...
                |      Dim oX As Double
                |      Dim oY As Double
                |      Dim oZ As Double
                |      Call firstMachGeom.GetDirection( oX, oY, oZ, 3)

        :param float o_x:
        :param float o_y:
        :param float o_z:
        :param int index_of_pointed_geom:
        :rtype: None
        """
        return self.manufacturing_machinable_geometry.GetDirection(o_x, o_y, o_z, index_of_pointed_geom)

    def get_origin(self) -> tuple:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetOrigin(double oX,
                | double oY,
                | double oZ,
                | long IndexOfPointedGeom)
                |
                |     Retrieves the origin of a pointed geometry under a
                |     ManufacturingMachinableGeometry object.
                |     Note: Currently valid only for AxialUDF and DesignHole
                |     features.
                |
                |     Parameters:
                |
                |         oX,oY,oZ
                |             The coordinates of the origin
                |         IndexOfPointedGeom
                |             The index of the pointed geometry
                |             Note: Check that the index you are passing in less than or equal to
                |             the pointed geometry count retrieved using the
                |
                |         PointedGeometryCount method.
                |
                | Example:
                |     The following example retrieves the coordinates of the origin of the third
                |     geometry under the manufacturing machinable geometry
                |     firstMachGeom:
                |
                |      Dim firstMachGeom As ManufacturingMachinableGeometry
                |      Set firstMachGeom = ...
                |      Dim oX As Double
                |      Dim oY As Double
                |      Dim oZ As Double
                |      Call firstMachGeom.GetOrigin( oX, oY, oZ, 3)

        :rtype: tuple
        """
        return self.manufacturing_machinable_geometry.GetOrigin()

    def list_pointed_geometry(
            self,
            i_index: int,
            o_geometry: AnyObject,
            o_product: Product,
            o_nb_shapes: int
    ) -> cat_variant:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub ListPointedGeometry(long iIndex,
                | AnyObject oGeometry,
                | Product oProduct,
                | long oNbShapes)
                |
                |     Retrieves a pointed geometry and its product.
                |
                |     Parameters:
                |
                |         iIndex
                |             The index of the pointed geometry and product
                |         oGeometry
                |             The retrieved geometry
                |         oProduct
                |             The product of the retrieved geometry
                |         oNbShapes
                |             The number of shapes of the retrieved geometry
                |
                |     Example:
                |         The following example retrieves the pointed geometry lists of the
                |         manufacturing machinable geometry firstMachGeom in PointedGeometryList and in
                |         PointedProductsList. The arrays must be previously initialized using the
                |
                |
                |     PointedGeometryCount method.
                |
                |      Dim firstMachGeom As ManufacturingMachinableGeometry
                |      Set firstMachGeom = ...
                |      Dim PointedGeometryListSize As Long
                |      Set PointedGeometryListSize = firstMachGeom.PointedGeometryCount
                |      If (PointedGeometryListSize > 0) Then
                |        Dim I As Long
                |        For I = 0 To PointedGeometryListSize-1
                |          Dim PointedGeometryList() As Variant
                |          Dim PointedProductsList() As Variant
                |          Dim NbShapes As Long
                |          Redim PointedGeometryList(PointedGeometryListSize-1)
                |          Redim PointedProductsList(PointedGeometryListSize-1)
                |          Call firstMachGeom.ListPointedGeometry(I, PointedGeometryList,
                |          PointedProductsList, NbShapes)
                |        End For
                |      End If

        :param int i_index:
        :param AnyObject o_geometry:
        :param Product o_product:
        :param int o_nb_shapes:
        :rtype: cat_variant
        """
        return self.manufacturing_machinable_geometry.ListPointedGeometry(
            i_index,
            o_geometry.com_object,
            o_product.com_object,
            o_nb_shapes
        )
        # # # # Autogenerated comment:
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'list_pointed_geometry'
        # # vba_code = """
        # # Public Function list_pointed_geometry(manufacturing_machinable_geometry)
        # #     Dim iIndex (2)
        # #     manufacturing_machinable_geometry.ListPointedGeometry iIndex
        # #     list_pointed_geometry = iIndex
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def list_shapes_of_pointed_geometry(self, i_index: int, o_shapes: tuple) -> cat_variant:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub ListShapesOfPointedGeometry(long iIndex,
                | CATSafeArrayVariant oShapes)
                |
                |     Retrieves the pointed shape list.
                |
                |     Parameters:
                |
                |         iIndex
                |             The index of the pointed geometry and product
                |         oShapes
                |             The retrieved shape list.
                |             The array must be previously initialized using the
                |
                |
                |         ListPointedGeometry method.
                |
                | Example:
                |     The following example retrieves the pointed shape list of the manufacturing
                |     machinable geometry firstMachGeom in PointedShapesList.
                |
                |      Dim firstMachGeom As ManufacturingMachinableGeometry
                |      Set firstMachGeom = ...
                |      Dim PointedGeometryListSize As Long
                |      Set PointedGeometryListSize = firstMachGeom.PointedGeometryCount
                |      If (PointedGeometryListSize > 0) Then
                |        Dim I As Long
                |        For I = 0 To PointedGeometryListSize-1
                |          Dim PointedGeometryList() As Variant
                |          Dim PointedProductsList() As Variant
                |          Dim NbShapes As Long
                |          Redim PointedGeometryList(PointedGeometryListSize-1)
                |          Redim PointedProductsList(PointedGeometryListSize-1)
                |          Call firstMachGeom.ListPointedGeometry(I, PointedGeometryList,
                |          PointedProductsList, NbShapes)
                |          If (NbShapes > 0) Then
                |            Dim PointedShapesList() As Variant
                |            Redim PointedShapesList(NbShapes-1)
                |            Call firstMachGeom.ListShapesOfPointedGeometry(I,
                |            PointedShapesList)
                |          End If
                |        End For
                |      End If

        :param int i_index:
        :param tuple o_shapes:
        :rtype: Variant
        """
        return self.manufacturing_machinable_geometry.ListShapesOfPointedGeometry(i_index, o_shapes)
        # # # # Autogenerated comment:
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'list_shapes_of_pointed_geometry'
        # # vba_code = """
        # # Public Function list_shapes_of_pointed_geometry(manufacturing_machinable_geometry)
        # #     Dim iIndex (2)
        # #     manufacturing_machinable_geometry.ListShapesOfPointedGeometry iIndex
        # #     list_shapes_of_pointed_geometry = iIndex
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def pointed_geometry_count(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func PointedGeometryCount() As long
                |
                |     Returns the pointed geometry list count.
                |
                | Example:
                |     The following example retrieves the pointed geometry list count of the
                |     manufacturing machinable geometry firstMachGeom in
                |     PointedGeometryListSize.
                |
                |      Dim firstMachGeom As ManufacturingMachinableGeometry
                |      Set firstMachGeom = ...
                |      Dim PointedGeometryListSize As Long
                |      Set PointedGeometryListSize = firstMachGeom.PointedGeometryCount

        :rtype: int
        """
        return self.manufacturing_machinable_geometry.PointedGeometryCount()

    def remove_pointed_geometry(self, i_index: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub RemovePointedGeometry(long iIndex)
                |
                |     Removes a geometry from the pointed geometry list.
                |
                |     Parameters:
                |
                |         iIndex
                |             The index of the geometry to remove
                |
                |     Example:
                |         The following example removes the third geometry from the pointed
                |         geometry list of the manufacturing machinable geometry
                |         firstMachGeom:
                |
                |          Dim firstMachGeom As ManufacturingMachinableGeometry
                |          Set firstMachGeom = ...
                |          Call firstMachGeom.RemovePointedGeometry( 3 )

        :param int i_index:
        :rtype: None
        """
        return self.manufacturing_machinable_geometry.RemovePointedGeometry(i_index)

    def __repr__(self):
        return f'ManufacturingMachinableGeometry(name="{self.name}")'
