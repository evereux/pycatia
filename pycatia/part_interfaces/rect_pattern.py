#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.in_interfaces.reference import Reference
from pycatia.knowledge_interfaces.int_param import IntParam
from pycatia.part_interfaces.linear_repartition import LinearRepartition
from pycatia.part_interfaces.pattern import Pattern


class RectPattern(Pattern):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.Shape
                |                         PartInterfaces.TransformationShape
                |                             PartInterfaces.Pattern
                |                                 RectPattern
                | 
                | Represents the rectangular pattern.
                | The shape is copied along two directions. Two linear repartitions control the
                | shape copy.
                | 
                | See also:
                |     LinearRepartition
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.rect_pattern = com_object

    @property
    def first_direction_repartition(self) -> LinearRepartition:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property FirstDirectionRepartition() As LinearRepartition (Read
                | Only)
                | 
                |     Returns the linear repartition along the first direction.
                | 
                |     Example:
                |         The following example returns in repart1 the first linear repartition
                |         of the rectangular pattern firstPattern:
                | 
                |          Set repart1 = firstPattern.FirstDirectionRepartition

        :rtype: LinearRepartition
        """

        return LinearRepartition(self.rect_pattern.FirstDirectionRepartition)

    @property
    def first_direction_row(self) -> IntParam:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property FirstDirectionRow() As IntParam (Read Only)
                | 
                |     Returns the position of the shape to be copied along the first linear
                |     direction.
                | 
                |     Example:
                |         The following example returns in FirstDirPos the position of the shape
                |         to be copied along the first linear direction in the rectangular pattern
                |         firstPattern:
                | 
                |          Set FirstDirPos = firstPattern.FirstDirectionRow

        :rtype: IntParam
        """

        return IntParam(self.rect_pattern.FirstDirectionRow)

    @property
    def first_orientation(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property FirstOrientation() As boolean
                | 
                |     Returns or sets whether the pattern is built towards the first direction
                |     orientation.
                |     True if the pattern is built towards the first direction
                |     orientation.
                | 
                |     Example:
                |         The following example returns in aligned1 whether the rectangular
                |         pattern firstPattern is built towards the first direction orientation, and then
                |         sets its to True:
                | 
                |          Set aligned1 = firstPattern.FirstOrientation
                |          firstPattern.FirstOrientation = True

        :rtype: bool
        """

        return self.rect_pattern.FirstOrientation

    @first_orientation.setter
    def first_orientation(self, value: bool):
        """
        :param bool value:
        """

        self.rect_pattern.FirstOrientation = value

    @property
    def first_rectangular_pattern_parameters(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property FirstRectangularPatternParameters() As
                | CatRectangularPatternParameters
                | 
                |     Returns or sets the rectangular pattern parameters required to define the
                |     pattern. These parameters are used when reading the CATIALinearRepartition
                |     properties.
                | 
                |     Example:
                |         The following example returns in parameters the rectangular pattern
                |         parameters of the firstPattern rectangular pattern, and then sets it to
                |         catUnequalSpacing, so that the unqual spacing will be defined in first
                |         direction:
                | 
                |          Set parameters = firstPattern.FirstCircularPatternParameters
                |          Set firstPattern.FirstCircularPatternParameters = catUnequalSpacing

        :return: enum cat_rectangular_pattern_parameters
        :rtype: int
        """

        return self.rect_pattern.FirstRectangularPatternParameters

    @first_rectangular_pattern_parameters.setter
    def first_rectangular_pattern_parameters(self, value: int):
        """
        :param int value: enum cat_rectangular_pattern_parameters
        """

        self.rect_pattern.FirstRectangularPatternParameters = value

    @property
    def second_direction_repartition(self) -> LinearRepartition:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property SecondDirectionRepartition() As LinearRepartition (Read
                | Only)
                | 
                |     Returns the linear repartition along the second direction.
                | 
                |     Example:
                |         The following example returns in repart2 the second linear repartition
                |         of the rectangular pattern firstPattern:
                | 
                |          Set repart2 = firstPattern.SecondDirectionRepartition

        :rtype: LinearRepartition
        """

        return LinearRepartition(self.rect_pattern.SecondDirectionRepartition)

    @property
    def second_direction_row(self) -> IntParam:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property SecondDirectionRow() As IntParam (Read Only)
                | 
                |     Returns the position of the shape to be copied along the second linear
                |     direction.
                | 
                |     Example:
                |         The following example returns in SecondDirPos the position of the shape
                |         to be copied along the second linear direction in the rectangular pattern
                |         firstPattern:
                | 
                |          Set SecondDirPos = firstPattern.SecondDirectionRow

        :rtype: IntParam
        """

        return IntParam(self.rect_pattern.SecondDirectionRow)

    @property
    def second_orientation(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property SecondOrientation() As boolean
                | 
                |     Returns or sets whether the pattern is built towards the second direction
                |     orientation.
                |     True if the pattern is built towards the second direction
                |     orientation.
                | 
                |     Example:
                |         The following example returns in aligned2 whether the rectangular
                |         pattern firstPattern is built towards the second direction orientation, and
                |         then sets its to False, meaning the pattern is built in the opposite
                |         direction:
                | 
                |          Set aligned2 = firstPattern.SecondOrientation
                |          firstPattern.SecondOrientation = False

        :rtype: bool
        """

        return self.rect_pattern.SecondOrientation

    @second_orientation.setter
    def second_orientation(self, value: bool):
        """
        :param bool value:
        """

        self.rect_pattern.SecondOrientation = value

    @property
    def second_rectangular_pattern_parameters(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property SecondRectangularPatternParameters() As
                | CatRectangularPatternParameters
                | 
                |     Returns or sets the rectangular pattern parameters required to define the
                |     pattern. These parameters are used when reading the CATIALinearRepartition
                |     properties.
                | 
                |     Example:
                |         The following example returns in parameters the rectangular pattern
                |         parameters of the secondPattern rectangular pattern, and then sets it to
                |         catUnequalSpacing, so that the unqual spacing will be defined in second
                |         direction:
                | 
                |          Set parameters = secondPattern.SecondCircularPatternParameters
                |          Set secondPattern.SecondCircularPatternParameters = catUnequalSpacing

        :return: enum cat_rectangular_pattern_parameters
        :rtype: int
        """

        return self.rect_pattern.SecondRectangularPatternParameters

    @second_rectangular_pattern_parameters.setter
    def second_rectangular_pattern_parameters(self, value: int):
        """
        :param int value: enum cat_rectangular_pattern_parameters
        """

        self.rect_pattern.SecondRectangularPatternParameters = value

    def get_first_direction(self, io_first_direction: tuple) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub GetFirstDirection(CATSafeArrayVariant
                | ioFirstDirection)
                | 
                |     Returns the first repartition direction. The first repartition direction is
                |     returned as an array containing the direction vector components. Assume this
                |     array is o1stDirRep. It contains:
                | 
                |     o1stDirRep[0],o1stDirRep[1],o1stDirRep[2]
                |         The X, Y, and Z direction vector components 
                | 
                |     Example:
                |         The following example returns in FirstDir the first repartition
                |         direction vector components of the rectangular pattern firstPattern and saves
                |         them in variables:
                | 
                |          Dim FirstDir()
                |          Call firstPattern.GetFirstDirection(FirstDir)
                |          x = FirstDir(0)
                |          y = FirstDir(1)
                |          z = FirstDir(2)

        :param tuple io_first_direction:
        :rtype: None
        """
        return self.rect_pattern.GetFirstDirection(io_first_direction)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_first_direction'
        # # vba_code = """
        # # Public Function get_first_direction(rect_pattern)
        # #     Dim ioFirstDirection (2)
        # #     rect_pattern.GetFirstDirection ioFirstDirection
        # #     get_first_direction = ioFirstDirection
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_second_direction(self, io_second_direction: tuple) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub GetSecondDirection(CATSafeArrayVariant
                | ioSecondDirection)
                | 
                |     Returns the second repartition direction. The second repartition direction
                |     is returned as an array containing the direction vector components. Assume this
                |     array is o2ndDirRep. It contains:
                | 
                |     o2ndDirRep[0],o2ndDirRep[1],o2ndDirRep[2]
                |         The X, Y, and Z direction vector components 
                | 
                |     Example:
                |         The following example returns in SecondDir the second repartition
                |         direction vector components of the rectangular pattern firstPattern and saves
                |         them in variables:
                | 
                |          Call firstPattern.GetSecondDirection(SecondDir)
                |          x = SecondDir[0]
                |          y = SecondDir[1]
                |          z = SecondDir[2]

        :param tuple io_second_direction:
        :rtype: None
        """
        return self.rect_pattern.GetSecondDirection(io_second_direction)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_second_direction'
        # # vba_code = """
        # # Public Function get_second_direction(rect_pattern)
        # #     Dim ioSecondDirection (2)
        # #     rect_pattern.GetSecondDirection ioSecondDirection
        # #     get_second_direction = ioSecondDirection
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_first_direction(self, i_first_direction: Reference) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetFirstDirection(Reference iFirstDirection)
                | 
                |     Sets the first repartition direction.
                | 
                |     Parameters:
                | 
                |         iFirstDirection
                |             The first repartition direction. It is passed as a
                |             
                | 
                |         Reference and can be valuated with a reference to a line or an
                |         edge.
                |         The following Boundary objects are supported: PlanarFace,
                |         RectilinearTriDimFeatEdge and RectilinearBiDimFeatEdge.
                |         
                | 
                | Example:
                |     The following example sets the first repartition direction of the
                |     rectangular pattern firstPattern with the refToLine1 reference
                |     :
                | 
                |      firstPattern.SetFirstDirection refToLine1

        :param Reference i_first_direction:
        :rtype: None
        """
        return self.rect_pattern.SetFirstDirection(i_first_direction.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_first_direction'
        # # vba_code = """
        # # Public Function set_first_direction(rect_pattern)
        # #     Dim iFirstDirection (2)
        # #     rect_pattern.SetFirstDirection iFirstDirection
        # #     set_first_direction = iFirstDirection
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_instance_spacing(self, i_instance_number: int, i_spacing: float, i_direction: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetInstanceSpacing(long iInstanceNumber,
                | double iSpacing,
                | long iDirection)
                | 
                |     Sets the InstanceSpacing.
                | 
                |     Parameters:
                | 
                |         iInstanceNumber
                |             The Instance Number 
                |         iSpacing
                |             The Spacing 
                |         iDirection
                |             The Instance direction 
                | 
                |     Example:
                |         The following example sets the InstanceSpacing in a direction for
                |         unequal spacing

        :param int i_instance_number:
        :param float i_spacing:
        :param int i_direction:
        :rtype: None
        """
        return self.rect_pattern.SetInstanceSpacing(i_instance_number, i_spacing, i_direction)

    def set_second_direction(self, i_second_direction: Reference) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetSecondDirection(Reference iSecondDirection)
                | 
                |     Sets the second repartition direction.
                | 
                |     Parameters:
                | 
                |         iSecondDirection
                |             The second repartition direction. It is passed as a
                |             
                | 
                |         Reference and can be valuated with a reference to a line or an
                |         edge.
                |         The following Boundary objects are supported: PlanarFace,
                |         RectilinearTriDimFeatEdge and RectilinearBiDimFeatEdge.
                |         
                | 
                | Example:
                |     The following example sets the second repartition direction of the
                |     rectangular pattern firstPattern with the refToLine2 reference
                |     :
                | 
                |      firstPattern.SetSecondDirection refToLine2

        :param Reference i_second_direction:
        :rtype: None
        """
        return self.rect_pattern.SetSecondDirection(i_second_direction.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_second_direction'
        # # vba_code = """
        # # Public Function set_second_direction(rect_pattern)
        # #     Dim iSecondDirection (2)
        # #     rect_pattern.SetSecondDirection iSecondDirection
        # #     set_second_direction = iSecondDirection
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_unequal_instance_number(self, i_instance_number: int, i_direction: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetUnequalInstanceNumber(long iInstanceNumber,
                | long iDirection)
                | 
                |     Sets the Instance Number.
                | 
                |     Parameters:
                | 
                |         iInstanceNumber
                |             The Instance Number 
                |         iDirection
                |             The Instance direction 
                | 
                |     Example:
                |         The following example modifies the instance number for unequal spacing

        :param int i_instance_number:
        :param int i_direction:
        :rtype: None
        """
        return self.rect_pattern.SetUnequalInstanceNumber(i_instance_number, i_direction)

    def __repr__(self):
        return f'RectPattern(name="{self.name}")'
