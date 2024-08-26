#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-07-06 14:02:20.222384

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
import inspect

from pycatia.in_interfaces.reference import Reference
from pycatia.knowledge_interfaces.angle import Angle
from pycatia.mec_mod_interfaces.hybrid_shape import HybridShape


class HybridShapeRevol(HybridShape):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.HybridShape
                |                         HybridShapeRevol
                | 
                | The Revol feature : an Revol is made up of a face to process and one Revol parameter.
                | Role: To access the data of the hybrid shape revol feature
                | object.
                | 
                | LICENSING INFORMATION: Creation of volume result requires GSO
                | License
                | if GSO License is not granted , setting of Volume context has not
                | effect
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_revol = com_object

    @property
    def axis(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Axis() As Reference
                | 
                |     Role: To get_Axis on the object.
                | 
                |     Parameters:
                | 
                |         oDir
                |             return value for CATScript applications, with (IDLRETVAL) function
                |             type 
                | 
                |     See also:
                |         Reference 
                |     Returns:
                |         HRESULT S_OK if Ok E_FAIL else return error code for C++
                |         Implementations 
                |     See also:
                |         HybridShapeFactory

        :rtype: Reference
        """

        return Reference(self.hybrid_shape_revol.Axis)

    @axis.setter
    def axis(self, reference_axis: Reference):
        """
        :param Reference reference_axis:
        """

        self.hybrid_shape_revol.Axis = reference_axis.com_object

    @property
    def begin_angle(self) -> Angle:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property BeginAngle() As Angle (Read Only)
                | 
                |     Role: To get_BeginAngle on the object.
                | 
                |     Parameters:
                | 
                |         oAngle
                |             return value for CATScript applications, with (IDLRETVAL) function
                |             type 
                | 
                |     See also:
                |         Angle 
                |     Returns:
                |         HRESULT S_OK if Ok E_FAIL else return error code for C++
                |         Implementations 
                |     See also:
                |         HybridShapeFactory

        :rtype: Angle
        """

        return Angle(self.hybrid_shape_revol.BeginAngle)

    @property
    def begin_angle_offset(self) -> float:
        """

        Introduced in V5-6R2019.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2024-08-20 16:04:57.203445)
                | Property BeginAngleOffset() As double
                |     Gets/Sets the first angle offset value of first upto
                |     element.
                |
                |     Parameters:
                |
                |         oAng1
                |             first angle offset value.

        :rtype: float
        """

        self.release_check(
            self.application.system_configuration.release,
            29,
            f'{self.__class__.__name__}.{inspect.stack()[0][3]}',
        )

        return self.hybrid_shape_revol.BeginAngleOffset

    @begin_angle_offset.setter
    def begin_angle_offset(self, value: float):
        """
        :param float value:
        """

        self.hybrid_shape_revol.BeginAngleOffset = value

    @property
    def context(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Context() As long
                | 
                |     Returns or sets the context on Revolve feature.
                |     Legal values:
                | 
                |         0 This option creates surface of revolution.
                |         1 This option creates volume of revolution.
                | 
                | 
                |     Note: Setting volume result requires GSO License.
                | 
                |     Example:
                |         This example retrieves in oContext the context for the Revol hybrid
                |         shape feature.
                | 
                |          Dim oContext
                |          Set oContext = Revol.Context

        :rtype: int
        """

        return self.hybrid_shape_revol.Context

    @context.setter
    def context(self, value: int):
        """
        :param int value:
        """

        self.hybrid_shape_revol.Context = value

    @property
    def end_angle(self) -> Angle:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property EndAngle() As Angle (Read Only)
                | 
                |     Role: To get_EndAngle on the object.
                | 
                |     Parameters:
                | 
                |         oAngle
                |             return value for CATScript applications, with (IDLRETVAL) function
                |             type 
                | 
                |     See also:
                |         Angle 
                |     Returns:
                |         HRESULT S_OK if Ok E_FAIL else return error code for C++
                |         Implementations 
                |     See also:
                |         HybridShapeFactory

        :rtype: Angle
        """

        return Angle(self.hybrid_shape_revol.EndAngle)

    @property
    def end_angle_offset(self) -> float:
        """

        Introduced in V5-6R2019.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2024-08-20 16:04:57.203445)
                | Property EndAngleOffset() As double
                |     Gets/Sets the second angle offset value of second upto
                |     element.
                |
                |     Parameters:
                |
                |         oAng2
                |             second angle offset value.

        :rtype: float
        """

        self.release_check(
            self.application.system_configuration.release,
            29,
            f'{self.__class__.__name__}.{inspect.stack()[0][3]}',
        )

        return self.hybrid_shape_revol.EndAngleOffset

    @end_angle_offset.setter
    def end_angle_offset(self, value: float):
        """
        :param float value:
        """

        self.hybrid_shape_revol.EndAngleOffset = value

    @property
    def first_limit_type(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property FirstLimitType() As long
                | 
                |     Returns or sets the First limit type.
                |     Legal values:
                | 
                |     0
                |         Unknown Limit type.
                |     1
                |         Limit type is Dimension. It implies that limit is defined by
                |         length
                |     2
                |         Limit type is UptoElement. It implies that limit is defined by a
                |         geometrical element
                | 
                | Example:
                |     This example retrieves in oLim1Type the first limit type for the Revolve
                |     hybrid shape feature.
                | 
                |      Dim oLim1Type
                |      Set oLim1Type = Revolve.FirstLimitType

        :rtype: int
        """

        return self.hybrid_shape_revol.FirstLimitType

    @first_limit_type.setter
    def first_limit_type(self, value: int):
        """
        :param int value:
        """

        self.hybrid_shape_revol.FirstLimitType = value

    @property
    def first_upto_element(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property FirstUptoElement() As Reference
                | 
                |     Returns or sets the First up-to element used to limit
                |     Revolution.
                | 
                |     Example:
                |         This example retrieves in Lim1Elem the First up-to element for the
                |         Revolve hybrid shape feature.
                | 
                |          Dim Lim1Elem As Reference 
                |          Set Lim1Elem = Revolve.FirstUptoElement

        :rtype: Reference
        """

        return Reference(self.hybrid_shape_revol.FirstUptoElement)

    @first_upto_element.setter
    def first_upto_element(self, reference_element: Reference):
        """
        :param Reference reference_element:
        """

        self.hybrid_shape_revol.FirstUptoElement = reference_element.com_object

    @property
    def orientation(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Orientation(boolean iOrientation)
                | 
                |     Gets or sets orientation of the revolution.
                |     Orientation
                |     TRUE : The natural orientation of the axis is taken.
                |     FALSE : The opposite orientation is taken This example retrieves in IsInverted orientation of the
                |     revolution for the Revol hybrid shape feature.
                | 
                |      Dim IsInverted As boolean
                |      IsInverted = Revol.Orientation

        :rtype: bool
        """

        return self.hybrid_shape_revol.Orientation

    @orientation.setter
    def orientation(self, value: bool):
        """
        :param bool value:
        """

        self.hybrid_shape_revol.Orientation = value

    @property
    def profile(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Profil() As Reference
                | 
                |     Role: To get_Profil on the object.
                | 
                |     Parameters:
                | 
                |         oProfil
                |             return value for CATScript applications, with (IDLRETVAL) function
                |             type 
                | 
                |     See also:
                |         Reference 
                |     Returns:
                |         HRESULT S_OK if Ok E_FAIL else return error code for C++
                |         Implementations 
                |     See also:
                |         HybridShapeFactory

        :rtype: Reference
        """

        return Reference(self.hybrid_shape_revol.Profil)

    @profile.setter
    def profile(self, reference_profile: Reference):
        """
        :param Reference reference_profile:
        """

        self.hybrid_shape_revol.Profil = reference_profile.com_object

    @property
    def second_limit_type(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property SecondLimitType() As long
                | 
                |     Returns or sets the Second limit type.
                |     Legal values:
                | 
                |     0
                |         Unknown Limit type.
                |     1
                |         Limit type is Dimension. It implies that limit is defined by
                |         length
                |     2
                |         Limit type is UptoElement. It implies that limit is defined by a
                |         geometrical element
                | 
                | Example:
                |     This example retrieves in oLim2Type the second limit type for the Revolve
                |     hybrid shape feature.
                | 
                |      Dim oLim2Type
                |      Set oLim2Type = RevolveSecondLimitType

        :rtype: int
        """

        return self.hybrid_shape_revol.SecondLimitType

    @second_limit_type.setter
    def second_limit_type(self, value: int):
        """
        :param int value:
        """

        self.hybrid_shape_revol.SecondLimitType = value

    @property
    def second_upto_element(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property SecondUptoElement() As Reference
                | 
                |     Returns or sets the Second up-to element used to limit
                |     Revolution.
                | 
                |     Example:
                |         This example retrieves in Lim2Elem the Second up-to element for the
                |         Revolve hybrid shape feature.
                | 
                |          Dim Lim2Elem As Reference 
                |          Set Lim2Elem = Revolve.SecondUptoElement

        :rtype: Reference
        """

        return Reference(self.hybrid_shape_revol.SecondUptoElement)

    @second_upto_element.setter
    def second_upto_element(self, reference_element: Reference):
        """
        :param Reference reference_element:
        """

        self.hybrid_shape_revol.SecondUptoElement = reference_element.com_object

    def __repr__(self):
        return f'HybridShapeRevol(name="{self.name}")'
