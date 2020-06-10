#! usr/bin/python3.6
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-09 09:53:18.676780

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.in_interfaces.reference import Reference
from pycatia.knowledge_interfaces.angle import Angle
from pycatia.mec_mod_interfaces.hybrid_shape import HybridShape


class HybridShapeRevol(HybridShape):

    """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)

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
    def axis(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
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

        :return: Reference
        """

        return Reference(self.hybrid_shape_revol.Axis)

    @axis.setter
    def axis(self, value):
        """
        :param Reference value:
        """

        self.hybrid_shape_revol.Axis = value

    @property
    def begin_angle(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
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

        :return: Angle
        """

        return Angle(self.hybrid_shape_revol.BeginAngle)

    @property
    def context(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
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

        :return: int
        """

        return self.hybrid_shape_revol.Context

    @context.setter
    def context(self, value):
        """
        :param int value:
        """

        self.hybrid_shape_revol.Context = value

    @property
    def end_angle(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
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

        :return: Angle
        """

        return Angle(self.hybrid_shape_revol.EndAngle)

    @property
    def first_limit_type(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
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

        :return: int
        """

        return self.hybrid_shape_revol.FirstLimitType

    @first_limit_type.setter
    def first_limit_type(self, value):
        """
        :param int value:
        """

        self.hybrid_shape_revol.FirstLimitType = value

    @property
    def first_upto_element(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
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

        :return: Reference
        """

        return Reference(self.hybrid_shape_revol.FirstUptoElement)

    @first_upto_element.setter
    def first_upto_element(self, value):
        """
        :param Reference value:
        """

        self.hybrid_shape_revol.FirstUptoElement = value

    @property
    def orientation(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property Orientation(boolean iOrientation)
                | 
                |     Gets or sets orientation of the revolution. Orientation = TRUE : The natural orientation of the axis is taken. = FALSE : The opposite orientation is taken This example retrieves in IsInverted orientation of the revolution for the Revol hybrid shape feature.
                | 
                |      Dim IsInverted As boolean
                |      IsInverted = Revol.Orientation

        :return: False
        """

        return None

    @orientation.setter
    def orientation(self, value):
        """
        :param False value:
        """

        self.hybrid_shape_revol.Orientation = value

    @property
    def profil(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
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

        :return: Reference
        """

        return Reference(self.hybrid_shape_revol.Profil)

    @profil.setter
    def profil(self, value):
        """
        :param Reference value:
        """

        self.hybrid_shape_revol.Profil = value

    @property
    def second_limit_type(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
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

        :return: int
        """

        return self.hybrid_shape_revol.SecondLimitType

    @second_limit_type.setter
    def second_limit_type(self, value):
        """
        :param int value:
        """

        self.hybrid_shape_revol.SecondLimitType = value

    @property
    def second_upto_element(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
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

        :return: Reference
        """

        return Reference(self.hybrid_shape_revol.SecondUptoElement)

    @second_upto_element.setter
    def second_upto_element(self, value):
        """
        :param Reference value:
        """

        self.hybrid_shape_revol.SecondUptoElement = value

    def __repr__(self):
        return f'HybridShapeRevol(name="{ self.name }")'
