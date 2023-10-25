#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.in_interfaces.reference import Reference
from pycatia.part_interfaces.limit import Limit
from pycatia.part_interfaces.sketch_based_shape import SketchBasedShape


class Prism(SketchBasedShape):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.Shape
                |                         PartInterfaces.SketchBasedShape
                |                             Prism
                | 
                | Prism-based features in Part Design : base for pad or pocket.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.prism = com_object

    @property
    def direction_orientation(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property DirectionOrientation() As CatPrismOrientation
                | 
                |     Returns the prism direction orientation.
                | 
                |     Returns:
                |         oOrientation The direction orientation (see CatPrismOrientation for
                |         list of possible types)
                | 
                |         Example:
                |             The following example saves in dirOrientation the direction
                |             orientation of prism firstPrism, and then sets it so that the direction will be
                |             now inversed :
                | 
                |              Set dirOrientation = firstPrism.DirectionOrientation
                |              firstPrism.DirectionOrientation = catInverseOrientation

        :return: enum cat_prism_orientation
        :rtype: int
        """

        return self.prism.DirectionOrientation

    @direction_orientation.setter
    def direction_orientation(self, value: int):
        """
        :param int value: enum cat_prism_orientation
        """

        self.prism.DirectionOrientation = value

    @property
    def direction_type(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property DirectionType() As CatPrismExtrusionDirection
                | 
                |     Returns the prism direction type.
                | 
                |     Returns:
                |         oDirType The direction type (see CatPrismExtrusionDirection for list of
                |         possible types)
                | 
                |         Example:
                |             The following example saves in dirType the direction type of prism
                |             firstPrism, and then sets it so that the direction will be now normal to the
                |             sketch :
                | 
                |              Set dirType = firstPrism.DirectionType
                |              firstPrism.DirectionType = catNormalToSketchDirection

        :return: enum cat_prism_extrusion_direction
        :rtype: int
        """

        return self.prism.DirectionType

    @direction_type.setter
    def direction_type(self, value: int):
        """
        :param int value: enum cat_prism_extrusion_direction
        """

        self.prism.DirectionType = value

    @property
    def first_limit(self) -> Limit:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property FirstLimit() As Limit (Read Only)
                | 
                |     Returns the first prism limit (one of the two).
                |     This limit manages the way the prism is ended.
                | 
                |     Returns:
                |         oFirstLimit The first limit (see Limit for more
                |         information)
                | 
                |         Example:
                |             The following example returns in firstLimit the first limit of
                |             prism firstPrism:
                | 
                |              Set firstLimit = firstPrism.FirstLimit

        :rtype: Limit
        """

        return Limit(self.prism.FirstLimit)

    @property
    def is_symmetric(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property IsSymmetric() As boolean
                | 
                |     Returns the prism symmetry flag.
                |     It returns TRUE if the prism is symmetric (from the base sketch), FALSE if
                |     not.
                | 
                |     Returns:
                |         oIsSymmetric The symmetry flag as a boolean
                | 
                |         Example:
                |             The following example saves in symFlag the symmetry flag of prism
                |             firstPrism, and then sets it so that it will be now symmetric (from the base
                |             sketch) :
                | 
                |              Set symFlag = firstPrism.IsSymmetric
                |              firstPrism.IsSymmetric = TRUE

        :rtype: bool
        """

        return self.prism.IsSymmetric

    @is_symmetric.setter
    def is_symmetric(self, value: bool):
        """
        :param bool value:
        """

        self.prism.IsSymmetric = value

    @property
    def is_thin(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property IsThin() As boolean
                | 
                |     Returns the prism thin flag.
                |     It returns TRUE if the prism is a thin prism , FALSE if
                |     not.
                | 
                |     Returns:
                |         oIsThin The thin flag as a boolean
                | 
                |         Example:
                |             The following example saves in thinFlag the thin flag of prism
                |             firstPrism, and then sets it so that it will be now thin
                |             :
                | 
                |              Set thinFlag = firstPrism.IsThin
                |              firstPrism.IsThin = TRUE

        :rtype: bool
        """

        return self.prism.IsThin

    @is_thin.setter
    def is_thin(self, value: bool):
        """
        :param bool value:
        """

        self.prism.IsThin = value

    @property
    def merge_end(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property MergeEnd() As boolean
                | 
                |     Returns the prism merge end flag (for thin prism only).
                |     It returns TRUE if merge ends is required , FALSE if not.
                | 
                |     Returns:
                |         oIsMergeEnd The merge end flag as a boolean
                | 
                |         Example:
                |             The following example saves in MergeEndFlag the merge end flag of
                |             prism firstPrism, and then sets it so that merge end will be required
                |             :
                | 
                |              Set MergeEndFlag = firstPrism.IsMergeEnd
                |              firstPrism.IsMergeEnd = TRUE

        :rtype: bool
        """

        return self.prism.MergeEnd

    @merge_end.setter
    def merge_end(self, value: bool):
        """
        :param bool value:
        """

        self.prism.MergeEnd = value

    @property
    def neutral_fiber(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property NeutralFiber() As boolean
                | 
                |     Returns the prism neutral fiber flag (for thin prism
                |     only).
                |     It returns TRUE if the prism is a neutral fiber prism , FALSE if
                |     not.
                | 
                |     Returns:
                |         oIsNeutralFiber The neutral fiber flag as a boolean
                | 
                |         Example:
                |             The following example saves in NeutralFiberFlag the neutral fiber
                |             flag of prism firstPrism, and then sets it so that it will be now neutral fiber
                |             :
                | 
                |              Set NeutralFiberFlag = firstPrism.IsNeutralFiber
                |              firstPrism.IsNeutralFiber = TRUE

        :rtype: bool
        """

        return self.prism.NeutralFiber

    @neutral_fiber.setter
    def neutral_fiber(self, value: bool):
        """
        :param bool value:
        """

        self.prism.NeutralFiber = value

    @property
    def second_limit(self) -> Limit:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property SecondLimit() As Limit (Read Only)
                | 
                |     Returns the second prism limit (one of the two).
                |     This limit manages the way the prism is ended.
                | 
                |     Returns:
                |         oSecondLimit The second limit (see Limit for more
                |         information)
                | 
                |         Example:
                |             The following example returns in secondLimit the second limit of
                |             prism firstPrism:
                | 
                |              Set secondLimit = firstPrism.SecondLimit

        :rtype: Limit
        """

        return Limit(self.prism.SecondLimit)

    def get_direction(self, io_direction: tuple) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub GetDirection(CATSafeArrayVariant ioDirection)
                | 
                |     Returns the prism direction with absolute coordinates.
                |     It needs a safe array with 3 elements : X, Y, Z direction coordinates
                |     The array must be previously initialized
                | 
                |     Returns:
                |         ioDirection The direction coordinates
                | 
                |         Example:
                |             The following example returns in dirArray the direction coordinates
                |             of prism firstPrism:
                | 
                |              Dim dirArray(2)
                |              Call firstPrism.GetDirection(dirArray)
                |              Set x = dirArray[1]
                |              Set y = dirArray[2]
                |              Set z = dirArray[3]

        :param tuple io_direction:
        :rtype: None
        """
        return self.prism.GetDirection(io_direction)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_direction'
        # # vba_code = """
        # # Public Function get_direction(prism)
        # #     Dim ioDirection (2)
        # #     prism.GetDirection ioDirection
        # #     get_direction = ioDirection
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def reverse_inner_side(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub ReverseInnerSide()
                | 
                |     Reverses the prism inner side when the profile is open. This is useful for
                |     finding the shape to reach.
                | 
                |     Example:
                |         The following example reverses the current inner side of prism
                |         firstPrism :
                | 
                |          firstPrism.ReverseInnerSide

        :rtype: None
        """
        return self.prism.ReverseInnerSide()

    def set_direction(self, i_line: Reference) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetDirection(Reference iLine)
                | 
                |     Sets the prism associative direction.
                | 
                |     Parameters:
                | 
                |         iLine
                |             The support direction reference (see 
                | 
                |         Reference for more information)
                |         This reference can be valuated with a reference to a line or an
                |         edge.
                |         The following Boundary objects are supported: PlanarFace,
                |         RectilinearTriDimFeatEdge and
                |         RectilinearBiDimFeatEdge.
                | 
                |         Example:
                |             The following example sets the prism direction reference of prism
                |             firstPrism with prismDirRef line :
                | 
                |              firstPrism.SetDirection prismDirRef

        :param Reference i_line:
        :rtype: None
        """
        return self.prism.SetDirection(i_line.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_direction'
        # # vba_code = """
        # # Public Function set_direction(prism)
        # #     Dim iLine (2)
        # #     prism.SetDirection iLine
        # #     set_direction = iLine
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'Prism(name="{self.name}")'
