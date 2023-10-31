#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.knowledge_interfaces.int_param import IntParam
from pycatia.part_interfaces.angular_repartition import AngularRepartition
from pycatia.part_interfaces.linear_repartition import LinearRepartition
from pycatia.part_interfaces.pattern import Pattern


class CloseSurface(Pattern):
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
                |                                 CircPattern
                | 
                | Represents the circular pattern.
                | The shape is duplicated along concentric circles to build crowns. A linear
                | repartition object defines the duplication along radial directions, thus
                | determining the number of crowns. An angular repartition object defines the
                | duplication on the crowns.
                | 
                | See also:
                |     LinearRepartition, AngularRepartition
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.close_surface = com_object

    @property
    def angular_direction_row(self) -> IntParam:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property AngularDirectionRow() As IntParam (Read Only)
                | 
                |     Returns the position of the shape to be copied along the angular
                |     direction.
                | 
                |     Example:
                |         The following example returns in AngularDirPos the position of the
                |         shape to be copied along the angular direction.
                | 
                |          Set AngularDirPos = firstPattern.AngularDirectionRow

        :return: IntParam
        """

        return IntParam(self.close_surface.AngularDirectionRow)

    @property
    def angular_repartition(self) -> AngularRepartition:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property AngularRepartition() As AngularRepartition (Read
                | Only)
                | 
                |     Returns the angular repartition. The angular repartition is the repartition
                |     on a crown.
                | 
                |     Example:
                |         The following example returns in repartA the angular repartition of the
                |         circular pattern firstPattern:
                | 
                |          Set repartA = firstPattern.AngularRepartition

        :return: AngularRepartition
        """

        return AngularRepartition(self.close_surface.AngularRepartition)

    @property
    def circular_pattern_parameters(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property CircularPatternParameters() As
                | CatCircularPatternParameters
                | 
                |     Returns or sets the circular pattern parameters required to define the
                |     pattern. These parameters are used when reading the CATIAAngularRepartition
                |     properties.
                | 
                |     Example:
                |         The following example returns in parameters the circular pattern
                |         parameters of the firstPattern circular pattern, and then sets it to
                |         catCompleteCrown, so that only the number of instances is used to define the
                |         Pattern:
                | 
                |          Set parameters = firstPattern.CircularPatternParameters
                |          Set firstPattern.CircularPatternParameters = catCompleteCrown

        :return: enum cat_circular_pattern_parameters
        :return: int
        """

        return self.close_surface.CircularPatternParameters

    @circular_pattern_parameters.setter
    def circular_pattern_parameters(self, value):
        """
        :param int value: enum cat_circular_pattern_parameters
        """

        self.close_surface.CircularPatternParameters = value

    @property
    def radial_alignment(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property RadialAlignment() As boolean
                | 
                |     Returns or sets whether the copied shapes should be rotated or radial
                |     aligned with respect to the original one.
                |     True if the copied shapes are rotated.
                | 
                |     Example:
                |         The following example returns in alignedR the radial alignment of the
                |         circular pattern firstPattern, and then sets it to
                |         False:
                | 
                |          Set alignedR = firstPattern.RadialAlignment
                |          firstPattern.RadialAlignment = False

        :return: bool
        """

        return self.close_surface.RadialAlignment

    @radial_alignment.setter
    def radial_alignment(self, value):
        """
        :param bool value:
        """

        self.close_surface.RadialAlignment = value

    @property
    def radial_direction_row(self) -> IntParam:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property RadialDirectionRow() As IntParam (Read Only)
                | 
                |     Returns the position of the shape to be copied along the radial
                |     direction.
                | 
                |     Example:
                |         The following example returns in RadialDirPos the position of the shape
                |         to be copied along the radial direction.
                | 
                |          Set RadialDirPos = firstPattern.RadialDirectionRow

        :return: IntParam
        """

        return IntParam(self.close_surface.RadialDirectionRow)

    @property
    def radial_repartition(self) -> LinearRepartition:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property RadialRepartition() As LinearRepartition (Read
                | Only)
                | 
                |     Returns the radial repartition. The radial repartition is the repartition
                |     along a radius.
                | 
                |     Example:
                |         The following example returns in repartR the radial repartition of the
                |         circular pattern firstPattern:
                | 
                |          Set repartR = firstPattern.RadialRepartition

        :return: LinearRepartition
        """

        return LinearRepartition(self.close_surface.RadialRepartition)

    @property
    def rotation_orientation(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property RotationOrientation() As boolean
                | 
                |     Returns or sets whether the shapes are copied clockwise on the crowns with
                |     respect to the rotation axis direction.
                |     True if the shapes are copied counterclockwise when the rotation axis
                |     direction goes towards you when you look at the crown.
                | 
                |     Example:
                |         The following example returns in alignedAxis whether the circular
                |         pattern firstPattern is built clockwise, and then sets it to
                |         True:
                | 
                |          alignedAxis = firstPattern.RotationOrientation
                |          firstPattern.RotationOrientation = True

        :return: bool
        """

        return self.close_surface.RotationOrientation

    @rotation_orientation.setter
    def rotation_orientation(self, value):
        """
        :param bool value:
        """

        self.close_surface.RotationOrientation = value

    def get_rotation_axis(self, io_rotation_axis):
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub GetRotationAxis(CATSafeArrayVariant ioRotationAxis)
                | 
                |     Returns the rotation axis. The rotation axis is returned as an array
                |     containing the rotation axis vector components. Assume this array is
                |     oRotationAxis. It contains:
                | 
                |     oRotationAxis[0],oRotationAxis[1],oRotationAxis[2]
                |         The X, Y, and Z rotation axis vector components 
                | 
                |     Example:
                |         The following example returns in axisArray the rotation axis components
                |         of the circular pattern firstPattern:
                | 
                |          Call firstPattern.GetRotationAxis(axisArray)
                |          Set x = axisArray[0]
                |          Set y = axisArray[1]
                |          Set z = axisArray[2]

        :param tuple io_rotation_axis:
        :return: None
        """
        return self.close_surface.GetRotationAxis(io_rotation_axis)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_rotation_axis'
        # # vba_code = """
        # # Public Function get_rotation_axis(close_surface)
        # #     Dim ioRotationAxis (2)
        # #     close_surface.GetRotationAxis ioRotationAxis
        # #     get_rotation_axis = ioRotationAxis
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_rotation_center(self, io_rotation_center):
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub GetRotationCenter(CATSafeArrayVariant
                | ioRotationCenter)
                | 
                |     Returns the rotation center if the user defined it. Returns E_FAIL if no
                |     rotation center has been defined The rotation center is returned as an array
                |     containing the rotation center coordinates. Assume this array is
                |     oRotationCenter. It contains:
                | 
                |     oRotationCenter[0],oRotationCenter[1],oRotationCenter[2]
                |         The X, Y, and Z rotation center coordinates 
                | 
                |     Example:
                |         The following example returns in centerArray the rotation center
                |         coordinates of the circular pattern firstPattern, and saves them in
                |         variables:
                | 
                |          Call firstPattern.GetRotationCenter(centerArray)
                |          x = centerArray[0]
                |          y = centerArray[1]
                |          z = centerArray[2]

        :param tuple io_rotation_center:
        :return: None
        """
        return self.close_surface.GetRotationCenter(io_rotation_center)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_rotation_center'
        # # vba_code = """
        # # Public Function get_rotation_center(close_surface)
        # #     Dim ioRotationCenter (2)
        # #     close_surface.GetRotationCenter ioRotationCenter
        # #     get_rotation_center = ioRotationCenter
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_instance_angular_spacing(self, i_instance_number, i_angular_spacing):
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub SetInstanceAngularSpacing(long iInstanceNumber,
                | double iAngularSpacing)
                | 
                |     Sets the InstanceAngularSpacing.
                | 
                |     Parameters:
                | 
                |         iInstanceNumber
                |             The Instance Number 
                |         iAngularSpacing
                |             The Angular Spacing 
                | 
                |     Example:
                |         The following example sets the InstanceAngularSpacing of the circular
                |         pattern

        :param int i_instance_number:
        :param float i_angular_spacing:
        :return: None
        """
        return self.close_surface.SetInstanceAngularSpacing(i_instance_number, i_angular_spacing)

    def set_rotation_axis(self, i_rotation_axis):
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub SetRotationAxis(Reference iRotationAxis)
                | 
                |     Sets the rotation axis.
                | 
                |     Parameters:
                | 
                |         iRotationAxis
                |             The rotation axis. It is passed as reference and can be valuated
                |             with a line, an edge or a plane reference: in this case the plane normal is
                |             taken into account.
                |             The following 
                | 
                |         Boundary objects are supported: PlanarFace, CylindricalFace
                |         RectilinearTriDimFeatEdge and RectilinearBiDimFeatEdge.
                |         
                | 
                | Example:
                |     The following example sets the rotation axis of the circular pattern
                |     firstPattern with the refLine1 reference:
                | 
                |      firstPattern.SetRotationAxis refLine1

        :param Reference i_rotation_axis:
        :return: None
        """
        return self.close_surface.SetRotationAxis(i_rotation_axis.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_rotation_axis'
        # # vba_code = """
        # # Public Function set_rotation_axis(close_surface)
        # #     Dim iRotationAxis (2)
        # #     close_surface.SetRotationAxis iRotationAxis
        # #     set_rotation_axis = iRotationAxis
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_rotation_center(self, i_rotation_center):
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub SetRotationCenter(Reference iRotationCenter)
                | 
                |     Sets the rotation center.
                | 
                |     Parameters:
                | 
                |         iRotationCenter
                |             The rotation center 
                | 
                |     Example:
                |         The following example sets the rotation center of the circular pattern
                |         firstPattern with point1Ref point:
                | 
                |          firstPattern.SetRotationCenter point1Ref

        :param Reference i_rotation_center:
        :return: None
        """
        return self.close_surface.SetRotationCenter(i_rotation_center.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_rotation_center'
        # # vba_code = """
        # # Public Function set_rotation_center(close_surface)
        # #     Dim iRotationCenter (2)
        # #     close_surface.SetRotationCenter iRotationCenter
        # #     set_rotation_center = iRotationCenter
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_unequal_instance_number(self, i_instance_number):
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub SetUnequalInstanceNumber(long iInstanceNumber)
                | 
                |     Sets the Instance Number.
                | 
                |     Parameters:
                | 
                |         iInstanceNumber
                |             The Instance Number 
                | 
                |     Example:
                |         The following example modifies the instance number for unequal angular
                |         spacing

        :param int i_instance_number:
        :return: None
        """
        return self.close_surface.SetUnequalInstanceNumber(i_instance_number)

    def set_unequal_step(self, i_instance_number):
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub SetUnequalStep(long iInstanceNumber)
                | 
                |     This method is deprecated Sets the UnequalStep.
                | 
                |     Parameters:
                | 
                |         iInstanceNumber
                |             The Instance Number 
                | 
                |     Example:
                |         The following example creates the number of pattern spacing objects in
                |         pattern object

        :param int i_instance_number:
        :return: None
        """
        return self.close_surface.SetUnequalStep(i_instance_number)

    def __repr__(self):
        return f'CloseSurface(name="{self.name}")'
