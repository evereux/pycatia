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
from pycatia.part_interfaces.limit import Limit
from pycatia.product_structure_interfaces.product import Product
from pycatia.sketcher_interfaces.sketch import Sketch


class AssemblyPocket(AssemblyFeature):
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
                |                         AssemblyPocket
                | 
                | Represents the AssemblyPocket object.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.assembly_pocket = com_object

    @property
    def direction_orientation(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property DirectionOrientation() As CatPrismOrientation
                | 
                |     Returns or sets the pocket direction orientation.
                | 
                |     Example:
                |         The following example saves in dirOrientation the direction orientation
                |         of the pocket assemblyPocket, and then sets it so that the direction will be
                |         now inversed.
                | 
                |          Dim dirOrientation
                |          Set dirOrientation = assemblyPocket.DirectionOrientation
                |          assemblyPocket.DirectionOrientation = catInverseOrientation

        :return: enum cat_prism_orientation
        :rtype: int
        """

        return self.assembly_pocket.DirectionOrientation

    @direction_orientation.setter
    def direction_orientation(self, value: int):
        """
        :param int value: enum cat_prism_orientation
        """

        self.assembly_pocket.DirectionOrientation = value

    @property
    def direction_type(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property DirectionType() As CatPrismExtrusionDirection
                | 
                |     Returns or sets the pocket direction type.
                | 
                |     Example:
                |         The following example saves in dirType the direction type of the pocket
                |         assemblyPocket, and then sets it so that the direction will be now normal to
                |         the sketch.
                | 
                |          Dim dirType
                |          Set dirType = assemblyPocket.DirectionType
                |          assemblyPocket.DirectionType = catNormalToSketchDirection

        :return: enum cat_prism_extrusion_direction
        :rtype: int
        """

        return self.assembly_pocket.DirectionType

    @direction_type.setter
    def direction_type(self, value: int):
        """
        :param int value: enum cat_prism_extrusion_direction
        """

        self.assembly_pocket.DirectionType = value

    @property
    def first_limit(self) -> Limit:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property FirstLimit() As Limit (Read Only)
                | 
                |     Returns the first pocket limit.
                |     A pocket has two limits that manage the way the pocket is
                |     ended.
                | 
                |     Example:
                |         The following example returns in firstLimit the first limit of the
                |         pocket assemblyPocket.
                | 
                |          Dim firstLimit As Limit
                |          Set firstLimit = assemblyPocket.FirstLimit

        :rtype: Limit
        """

        return Limit(self.assembly_pocket.FirstLimit)

    @property
    def is_symmetric(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property IsSymmetric() As boolean
                | 
                |     Returns or sets the pocket symmetry flag.
                |     TRUE if the pocket is symmetric with respect to the base sketch, and FALSE
                |     otherwise.
                | 
                |     Example:
                |         The following example saves in symFlag the symmetry flag of the pocket
                |         assemblyPocket, and then sets it so that it will be now symmetric with respect
                |         to the base sketch.
                | 
                |          Dim symFlag As boolean
                |          Set symFlag = assemblyPocket.IsSymmetric
                |          assemblyPocket.IsSymmetric = TRUE

        :rtype: bool
        """

        return self.assembly_pocket.IsSymmetric

    @is_symmetric.setter
    def is_symmetric(self, value: bool):
        """
        :param bool value:
        """

        self.assembly_pocket.IsSymmetric = value

    @property
    def second_limit(self) -> Limit:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property SecondLimit() As Limit (Read Only)
                | 
                |     Returns the second pocket limit.
                |     A pocket has two limits that manage the way the pocket is
                |     ended.
                | 
                |     Example:
                |         The following example returns in secondLimit the second limit of the
                |         pocket assemblyPocket.
                | 
                |          Dim secondLimit As Limit
                |          Set secondLimit = assemblyPocket.SecondLimit

        :rtype: Limit
        """

        return Limit(self.assembly_pocket.SecondLimit)

    @property
    def sketch(self) -> Sketch:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Sketch() As Sketch (Read Only)
                | 
                |     Returns the pocket sketch.
                | 
                |     Example:
                |         The following example retrieves in sketch the sketch on which the
                |         pocket assemblyPocket is built.
                | 
                |          Dim sketch As Sketch
                |          Set sketch = assemblyPocket.Sketch

        :rtype: Sketch
        """

        return Sketch(self.assembly_pocket.Sketch)

    @property
    def sketch_component(self) -> Product:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property SketchComponent() As Product (Read Only)
                | 
                |     Returns the component containing the pocket sketch.
                | 
                |     Example:
                |         The following example retrieves in skComp the component that contains
                |         the sketch of the pocket assemblyPocket is built.
                | 
                |          Dim skComp As Product
                |          Set skComp = assemblyPocket.SketchComponent

        :rtype: Product
        """

        return Product(self.assembly_pocket.SketchComponent)

    def get_direction(self) -> tuple:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetDirection(CATSafeArrayVariant ioDirection)
                | 
                |     Retrieves the pocket direction vector components.
                |     These components are expressed in millimeter according to the absolute
                |     coordinate system.
                | 
                |     Parameters:
                | 
                |         ioDirection
                |             The pocket direction vector components, as a safe array made up of
                |             three doubles: X, Y, Z
                |             The array must be previously initialized. 
                | 
                |     Example:
                |         The following example retrieves in dirArray the direction vector
                |         components of the pocket assemblyPocket.
                | 
                |          Dim dirArray(2)
                |          Call assemblyPocket.GetDirection(dirArray)
                |          Set x = dirArray[0]
                |          Set y = dirArray[1]
                |          Set z = dirArray[2]

        :param tuple io_direction:
        :rtype: None
        """
        return self.assembly_pocket.GetDirection()
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_direction'
        # # vba_code = """
        # # Public Function get_direction(assembly_pocket)
        # #     Dim ioDirection (2)
        # #     assembly_pocket.GetDirection ioDirection
        # #     get_direction = ioDirection
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def reverse_inner_side(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub ReverseInnerSide()
                | 
                |     Reverses the pocket inner side when the profile is open.
                |     This is useful for finding the shape to reach.
                | 
                |     Example:
                |         The following example reverses the current inner side of the pocket
                |         assemblyPocket.
                | 
                |          assemblyPocket.ReverseInnerSide

        :rtype: None
        """
        return self.assembly_pocket.ReverseInnerSide()

    def set_direction(self, i_line: Reference, i_line_comp: Product) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetDirection(Reference iLine,
                | Product iLineComp)
                | 
                |     Sets the pocket associated direction.
                | 
                |     Parameters:
                | 
                |         iLine
                |             The pocket associated direction, as a reference to a line or an
                |             edge. 
                |         iLineComp
                |             The component containing the associated direction
                |             reference
                | 
                |             Example:
                |                 The following example sets the associated direction of the
                |                 pocket assemblyPocket using the dirRef line of the component
                |                 dirComp.
                | 
                |                  assemblyPocket.SetDirection dirRef, dirComp

        :param Reference i_line:
        :param Product i_line_comp:
        :rtype: None
        """
        return self.assembly_pocket.SetDirection(i_line.com_object, i_line_comp.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_direction'
        # # vba_code = """
        # # Public Function set_direction(assembly_pocket)
        # #     Dim iLine (2)
        # #     assembly_pocket.SetDirection iLine
        # #     set_direction = iLine
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'AssemblyPocket(name="{self.name}")'
