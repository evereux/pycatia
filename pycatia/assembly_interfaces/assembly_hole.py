#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.assembly_interfaces.assembly_feature import AssemblyFeature
from pycatia.in_interfaces.reference import Reference
from pycatia.knowledge_interfaces.angle import Angle
from pycatia.knowledge_interfaces.length import Length
from pycatia.part_interfaces.limit import Limit
from pycatia.product_structure_interfaces.product import Product
from pycatia.sketcher_interfaces.sketch import Sketch


class AssemblyHole(AssemblyFeature):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     CATAssemblyInterfaces.AssemblyFeature
                |                         AssemblyHole
                | 
                | Represents the AssemblyHole object.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.assembly_hole = com_object

    @property
    def anchor_mode(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property AnchorMode() As CatHoleAnchorMode
                | 
                |     Returns or sets the hole anchor mode.
                |     This property is valid when the hole type is Counterbored or
                |     Counterdrilled.
                | 
                |     Example:
                |         The following example saves in holeAnchorMode the anchor mode of the
                |         hole assemblyHole and sets it so that the anchor mode will now be set to the
                |         middle of its head.
                | 
                |          Dim holeAnchorMode
                |          Set holeAnchorMode = assemblyHole.AnchorMode
                |          assemblyHole.AnchorMode = catMiddlePointHoleAnchor

        :return: enum cat_hole_anchor_mode
        :rtype: int
        """

        return self.assembly_hole.AnchorMode

    @anchor_mode.setter
    def anchor_mode(self, value: int):
        """
        :param int value: enum cat_hole_anchor_mode
        """

        self.assembly_hole.AnchorMode = value

    @property
    def bottom_angle(self) -> Angle:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property BottomAngle() As Angle (Read Only)
                | 
                |     Returns the hole bottom angle.
                |     This property is valid when the hole bottom type is VBottom. The hole
                |     bottom angle is returned as a Angle object.
                | 
                |     Example:
                |         The following example retrieves in holeBottomAngle the bottom angle of
                |         the hole assemblyHole.
                | 
                |          Dim holeBottomAngle As Angle
                |          Set holeBottomAngle = assemblyHole.BottomAngle

        :rtype: Angle
        """

        return Angle(self.assembly_hole.BottomAngle)

    @property
    def bottom_limit(self) -> Limit:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property BottomLimit() As Limit (Read Only)
                | 
                |     Returns the hole bottom limit.
                |     This limit manages the way the hole is ended. It is returned as a Limit
                |     object.
                | 
                |     Example:
                |         The following example retrieves in limit the bottom limit of the hole
                |         assemblyHole.
                | 
                |          Dim limit As Limit
                |          Set limit = assemblyHole.BottomLimit

        :rtype: Limit
        """

        return Limit(self.assembly_hole.BottomLimit)

    @property
    def bottom_type(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property BottomType() As CatHoleBottomType
                | 
                |     Returns or sets the hole bottom type.
                | 
                |     Example:
                |         The following example saves in holeBottomType the bottom type of the
                |         hole assemblyHole and sets it so that the bottom will now be a V-like
                |         one.
                | 
                |          Dim holeBottomType
                |          Set holeBottomType = assemblyHole.BottomType
                |          assemblyHole.BottomType = catVHoleBottom

        :return: enum cat_hole_bottom_type
        :rtype: int
        """

        return self.assembly_hole.BottomType

    @bottom_type.setter
    def bottom_type(self, value: int):
        """
        :param int value: enum cat_hole_bottom_type
        """

        self.assembly_hole.BottomType = value

    @property
    def diameter(self) -> Length:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Diameter() As Length (Read Only)
                | 
                |     Returns the hole diameter.
                |     It is returned as a Length object.
                | 
                |     Example:
                |         The following example retrieves in holeDiam the diameter of the hole
                |         assemblyHole.
                | 
                |          Dim holeDiam As Length
                |          Set holeDiam = assemblyHole.Diameter

        :rtype: Length
        """

        return Length(self.assembly_hole.Diameter)

    @property
    def head_angle(self) -> Angle:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property HeadAngle() As Angle (Read Only)
                | 
                |     Returns the hole head angle.
                |     This property is valid when the hole type is Tapered, Counterdrilled or
                |     Countersunk. The hole head angle is returned as a Angle
                |     object.
                | 
                |     Example:
                |         The following example retrieves in holeHeadAngle the head angle of the
                |         hole assemblyHole.
                | 
                |          Dim holeHeadAngle As Angle
                |          Set holeHeadAngle = assemblyHole.HeadAngle

        :rtype: Angle
        """

        return Angle(self.assembly_hole.HeadAngle)

    @property
    def head_depth(self) -> Length:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property HeadDepth() As Length (Read Only)
                | 
                |     Returns the hole head depth.
                |     This property is valid when the hole type is Counterbored, Counterdrilled
                |     or Countersunk. The hole head depth is returned as a Length
                |     object.
                | 
                |     Example:
                |         The following example retrieves in holeHeadDepth the head depth of the
                |         hole assemblyHole.
                | 
                |          Dim holeHeadDepth As Length
                |          Set holeHeadDepth = assemblyHole.HeadDepth

        :rtype: Length
        """

        return Length(self.assembly_hole.HeadDepth)

    @property
    def head_diameter(self) -> Length:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property HeadDiameter() As Length (Read Only)
                | 
                |     Returns the hole head diameter.
                |     This property is valid when the hole type is Counterbored or
                |     Counterdrilled. The hole head diameter is returned as a Length
                |     object.
                | 
                |     Example:
                |         The following example retrieves in holeHeadDiam the head diameter of
                |         the hole assemblyHole.
                | 
                |          Dim holeHeadDiam As Length
                |          Set holeHeadDiam = assemblyHole.HeadDiameter

        :rtype: Length
        """

        return Length(self.assembly_hole.HeadDiameter)

    @property
    def sketch(self) -> Sketch:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Sketch() As Sketch (Read Only)
                | 
                |     Returns the hole positioning sketch.
                | 
                |     Example:
                |         The following example retrieves in sketch the positioning sketch of the
                |         hole assemblyHole.
                | 
                |          Dim sketch As Sketch
                |          Set sketch = assemblyHole.Sketch

        :rtype: Sketch
        """

        return Sketch(self.assembly_hole.Sketch)

    @property
    def sketch_component(self) -> Product:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property SketchComponent() As Product (Read Only)
                | 
                |     Returns the component containing the hole positioning
                |     sketch.
                | 
                |     Example:
                |         The following example retrieves in skComp the component that contains
                |         the positioning sketch of the hole assemblyHole.
                | 
                |          Dim skComp As Product
                |          Set skComp = assemblyHole.SketchComponent

        :rtype: Product
        """

        return Product(self.assembly_hole.SketchComponent)

    @property
    def type(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Type() As CatHoleType
                | 
                |     Returns or sets the hole type.
                | 
                |     Example:
                |         The following example saves in holeType the type of the hole
                |         assemblyHole, and then sets it so that it will now be a tapered
                |         hole.
                | 
                |          Set holeType = assemblyHole.Type
                |          assemblyHole.Type = catTaperedHole

        :return: enum cat_hole_type
        :rtype: int
        """

        return self.assembly_hole.Type

    @type.setter
    def type(self, value: int):
        """
        :param int value: enum cat_hole_type
        """

        self.assembly_hole.Type = value

    def get_direction(self) -> tuple:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetDirection(CATSafeArrayVariant ioDirection)
                | 
                |     Retrieves the hole direction vector components.
                |     These components are expressed in millimeter according to the absolute
                |     coordinate system.
                | 
                |     Parameters:
                | 
                |         ioDirection
                |             The direction vector components, as a safe array made up of three
                |             doubles: X, Y, Z
                |             The array must be previously initialized. 
                | 
                |     Example:
                |         The following example returns in dirArray the direction vector
                |         components of the hole assemblyHole.
                | 
                |          Dim dirArray(2)
                |          Call assemblyHole.GetDirection(dirArray)
                |          Set x = dirArray[0]
                |          Set y = dirArray[1]
                |          Set z = dirArray[2]

        :param tuple io_direction:
        :rtype: None
        """
        return self.assembly_hole.GetDirection()
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_direction'
        # # vba_code = """
        # # Public Function get_direction(assembly_hole)
        # #     Dim ioDirection (2)
        # #     assembly_hole.GetDirection ioDirection
        # #     get_direction = ioDirection
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_origin(self) -> tuple:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetOrigin(CATSafeArrayVariant ioOrigin)
                | 
                |     Retrieves the origin point to which the hole is anchored.
                |     This point belongs to a plane tangent to the hole. The coordinates are
                |     expressed in millimeter according to the absolute coordinate
                |     system.
                | 
                |     Parameters:
                | 
                |         ioOrigin
                |             The hole origin point coordinates, as a safe array made up of three
                |             doubles: X, Y, Z
                |             The array must be previously initialized. 
                | 
                |     Example:
                |         The following example returns in coordArray the coordinates of the hole
                |         assemblyHole.
                | 
                |          Dim coordArray(2)
                |          Call assemblyHole.GetOrigin coordArray
                |          Set x = coordArray[0]
                |          Set y = coordArray[1]
                |          Set z = coordArray[2]

        :param tuple io_origin:
        :rtype: None
        """
        return self.assembly_hole.GetOrigin()
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_origin'
        # # vba_code = """
        # # Public Function get_origin(assembly_hole)
        # #     Dim ioOrigin (2)
        # #     assembly_hole.GetOrigin ioOrigin
        # #     get_origin = ioOrigin
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_direction(self, i_line: Reference, i_line_comp: Product) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetDirection(Reference iLine,
                | Product iLineComp)
                | 
                |     Sets the hole axis direction.
                | 
                |     Parameters:
                | 
                |         iLine
                |             The hole axis direction, as a reference to a line or an edge.
                |             
                |         iLineComp
                |             The component containing the axis direction 
                | 
                |     Example:
                |         The following example sets the axis direction of the hole assemblyHole
                |         with the dirRef line of the component dirComp.
                | 
                |          assemblyHole.SetDirection dirRef, dirComp

        :param Reference i_line:
        :param Product i_line_comp:
        :rtype: None
        """
        return self.assembly_hole.SetDirection(i_line.com_object, i_line_comp.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_direction'
        # # vba_code = """
        # # Public Function set_direction(assembly_hole)
        # #     Dim iLine (2)
        # #     assembly_hole.SetDirection iLine
        # #     set_direction = iLine
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'AssemblyHole(name="{self.name}")'
