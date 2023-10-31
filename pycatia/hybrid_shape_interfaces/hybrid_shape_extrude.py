#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-07-06 14:02:20.222384

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.hybrid_shape_interfaces.hybrid_shape_direction import HybridShapeDirection
from pycatia.in_interfaces.reference import Reference
from pycatia.knowledge_interfaces.length import Length
from pycatia.mec_mod_interfaces.hybrid_shape import HybridShape


class HybridShapeExtrude(HybridShape):
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
                |                         HybridShapeExtrude
                | 
                | The Extrude feature : an Extrude is made up of a face to process and one Extrude parameter.
                | Role: To access the data of the hybrid shape extrude feature
                | object.
                | 
                | LICENSING INFORMATION: Creation of volume result requires GSO
                | License
                | if GSO License is not granted , setting of Volume context has not
                | effect
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_extrude = com_object

    @property
    def begin_offset(self) -> Length:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property BeginOffset() As Length (Read Only)
                | 
                |     Role: To get_BeginOffset on the object. For surface extrude, if limit type
                |     is upto, this offset value is not used. In case of Volume Extrude, if the up-to
                |     element is specified, this will act as offset value from the upto
                |     element.
                | 
                |     Parameters:
                | 
                |         oExtrude
                |             return value for CATScript applications, with (IDLRETVAL) function
                |             type 
                | 
                |     See also:
                |         Length 
                |     Returns:
                |         HRESULT S_OK if Ok E_FAIL else return error code for C++
                |         Implementations 
                |     See also:
                |         HybridShapeFactory

        :rtype: Length
        """

        return Length(self.hybrid_shape_extrude.BeginOffset)

    @property
    def context(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Context() As long
                | 
                |     Returns or sets the context on Extrude feature.
                |     Legal values:
                | 
                |         0 This option creates surface of extrusion.
                |         1 This option creates volume of extrusion.
                | 
                | 
                |     Note: Setting volume result requires GSO License.
                | 
                |     Example:
                |         This example retrieves in oContext the context for the Extrude1 hybrid
                |         shape feature.
                | 
                |          Dim oContext
                |          Set oContext = Extrude1.Context

        :rtype: int
        """

        return self.hybrid_shape_extrude.Context

    @context.setter
    def context(self, value: int):
        """
        :param int value:
        """

        self.hybrid_shape_extrude.Context = value

    @property
    def direction(self) -> HybridShapeDirection:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Direction() As HybridShapeDirection
                | 
                |     Role: To get_Direction on the object.
                | 
                |     Parameters:
                | 
                |         oDir
                |             return value for CATScript applications, with (IDLRETVAL) function
                |             type 
                | 
                |     See also:
                |         HybridShapeDirection 
                |     Returns:
                |         HRESULT S_OK if Ok E_FAIL else return error code for C++
                |         Implementations 
                |     See also:
                |         HybridShapeFactory

        :rtype: HybridShapeDirection
        """

        return HybridShapeDirection(self.hybrid_shape_extrude.Direction)

    @direction.setter
    def direction(self, direction: HybridShapeDirection):
        """
        :param HybridShapeDirection direction:
        """

        self.hybrid_shape_extrude.Direction = direction.com_object

    @property
    def end_offset(self) -> Length:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property EndOffset() As Length (Read Only)
                | 
                |     Role: To get_EndOffset on the object. For surface extrude, if limit type is
                |     upto, this offset value is not used. In case of Volume Extrude, if the up-to
                |     element is specified, this will act as offset value from the upto
                |     element.
                | 
                |     Parameters:
                | 
                |         oExtrude
                |             return value for CATScript applications, with (IDLRETVAL) function
                |             type 
                | 
                |     See also:
                |         Length 
                |     Returns:
                |         HRESULT S_OK if Ok E_FAIL else return error code for C++
                |         Implementations 
                |     See also:
                |         HybridShapeFactory

        :rtype: Length
        """

        return Length(self.hybrid_shape_extrude.EndOffset)

    @property
    def extruded_object(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property ExtrudedObject() As Reference
                | 
                |     Role: To get_ExtrudedObject on the object.
                | 
                |     Parameters:
                | 
                |         oFaceToExtrude
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

        return Reference(self.hybrid_shape_extrude.ExtrudedObject)

    @extruded_object.setter
    def extruded_object(self, reference_object: Reference):
        """
        :param Reference reference_object:
        """

        self.hybrid_shape_extrude.ExtrudedObject = reference_object.com_object

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
                |     This example retrieves in oLim1Type the first limit type for the Extrude
                |     hybrid shape feature.
                | 
                |      Dim oLim1Type
                |      Set oLim1Type = Extrude.FirstLimitType

        :rtype: int
        """

        return self.hybrid_shape_extrude.FirstLimitType

    @first_limit_type.setter
    def first_limit_type(self, value: int):
        """
        :param int value:
        """

        self.hybrid_shape_extrude.FirstLimitType = value

    @property
    def first_upto_element(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property FirstUptoElement() As Reference
                | 
                |     Returns or sets the First up-to element used to limit
                |     extrusion.
                | 
                |     Example:
                |         This example retrieves in Lim1Elem the First up-to element for the
                |         Extrude hybrid shape feature.
                | 
                |          Dim Lim1Elem As Reference 
                |          Set Lim1Elem = Extrude.FirstUptoElement

        :rtype: Reference
        """

        return Reference(self.hybrid_shape_extrude.FirstUptoElement)
    
    @first_upto_element.setter
    def first_upto_element(self, reference_element: Reference):
        """
        :param Reference reference_element:
        """

        self.hybrid_shape_extrude.FirstUptoElement = reference_element.com_object

    @property
    def orientation(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Orientation(boolean iOrientation)
                | 
                |     Gets or sets orientation of the extrude. 
                |     Orientation = TRUE : The natural orientation is taken. = 
                |     FALSE : The opposite orientation is taken This example retrieves in IsInverted orientation of the 
                |     extrude for the Extrude hybrid shape feature.
                | 
                |      Dim IsInverted As boolean
                |      IsInverted = Extrude.Orientation

        :rtype: bool
        """

        return self.hybrid_shape_extrude.Orientation

    @orientation.setter
    def orientation(self, value: bool):
        """
        :param bool value:
        """

        self.hybrid_shape_extrude.Orientation = value

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
                |     This example retrieves in oLim2Type the second limit type for the Extrude
                |     hybrid shape feature.
                | 
                |      Dim oLim2Type
                |      Set oLim2Type = Extrude.SecondLimitType

        :rtype: int
        """

        return self.hybrid_shape_extrude.SecondLimitType

    @second_limit_type.setter
    def second_limit_type(self, value: int):
        """
        :param int value:
        """

        self.hybrid_shape_extrude.SecondLimitType = value

    @property
    def second_upto_element(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property SecondUptoElement() As Reference
                | 
                |     Returns or sets the Second up-to element used to limit
                |     extrusion.
                | 
                |     Example:
                |         This example retrieves in Lim2Elem the Second up-to element for the
                |         Extrude hybrid shape feature.
                | 
                |          Dim Lim2Elem As Reference 
                |          Set Lim2Elem = Extrude.SecondUptoElement

        :rtype: Reference
        """

        return Reference(self.hybrid_shape_extrude.SecondUptoElement)

    @second_upto_element.setter
    def second_upto_element(self, reference_element: Reference):
        """
        :param Reference reference_element:
        """

        self.hybrid_shape_extrude.SecondUptoElement = reference_element.com_object

    @property
    def symmetrical_extension(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property SymmetricalExtension() As boolean
                | 
                |     Returns or Sets the Symmetrical Extension of Extrude (Limit 2 = -Limit 1).
                | 
                |     Parameters:
                | 
                |         iSym
                |             Symetry flag

        :rtype: bool
        """

        return self.hybrid_shape_extrude.SymmetricalExtension

    @symmetrical_extension.setter
    def symmetrical_extension(self, value: bool):
        """
        :param bool value:
        """

        self.hybrid_shape_extrude.SymmetricalExtension = value

    def __repr__(self):
        return f'HybridShapeExtrude(name="{self.name}")'
