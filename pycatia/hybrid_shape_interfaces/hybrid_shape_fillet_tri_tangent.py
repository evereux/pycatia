#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-07-06 14:02:20.222384

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.in_interfaces.reference import Reference
from pycatia.mec_mod_interfaces.hybrid_shape import HybridShape


class HybridShapeFilletTriTangent(HybridShape):

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
                |                         HybridShapeFilletTriTangent
                | 
                | Fillet Tri-Tangent feature.
                | Role: Manipulation of Fillet Tri-Tangent feature Allows to access data of the
                | Fillet Tri-Tangent feature created by using three support surfaces, their
                | orientation, and options (supports trimming and fillet extremities
                | type)
                | 
                | See also:
                |     HybridShapeFactory
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_fillet_tri_tangent = com_object

    @property
    def first_elem(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property FirstElem() As Reference
                | 
                |     Returns or sets the first support surface feature.
                | 
                |     Example:
                |         This example retrieves in FirstElem the first support element used by
                |         the HybShpFilletTriTangent hybrid shape feature.
                | 
                |          Dim FirstElem As Reference 
                |          Set FirstElem = HybShpFilletTriTangent.FirstElem

        :rtype: Reference
        """

        return Reference(self.hybrid_shape_fillet_tri_tangent.FirstElem)

    @first_elem.setter
    def first_elem(self, reference_element: Reference):
        """
        :param Reference reference_element:
        """

        self.hybrid_shape_fillet_tri_tangent.FirstElem = reference_element.com_object

    @property
    def first_orientation(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property FirstOrientation() As long
                | 
                |     Returns or sets the first orientation used to specify fillet center
                |     position.
                |     Note; Orientation is same or inverse than the normal to the first surface
                |     support

        :rtype: int
        """

        return self.hybrid_shape_fillet_tri_tangent.FirstOrientation

    @first_orientation.setter
    def first_orientation(self, value: int):
        """
        :param int value:
        """

        self.hybrid_shape_fillet_tri_tangent.FirstOrientation = value

    @property
    def remove_elem(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property RemoveElem() As Reference
                | 
                |     Returns or sets the support surface to remove feature.

        :rtype: Reference
        """

        return Reference(self.hybrid_shape_fillet_tri_tangent.RemoveElem)

    @remove_elem.setter
    def remove_elem(self, reference_element: Reference):
        """
        :param Reference reference_element:
        """

        self.hybrid_shape_fillet_tri_tangent.RemoveElem = reference_element.com_object

    @property
    def remove_orientation(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property RemoveOrientation() As long
                | 
                |     Returns or sets the third orientation used to specify fillet center
                |     position.
                |     note: Orientation is same or inverse than the normal to the surface support
                |     to remove

        :rtype: int
        """

        return self.hybrid_shape_fillet_tri_tangent.RemoveOrientation

    @remove_orientation.setter
    def remove_orientation(self, value: int):
        """
        :param int value:
        """

        self.hybrid_shape_fillet_tri_tangent.RemoveOrientation = value

    @property
    def ribbon_relimitation_mode(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property RibbonRelimitationMode() As long
                | 
                |     Returns or sets fillet ribbon relimitation mode (or fillet extremities
                |     mode).
                |     note: Smooth(0) or Straight(1) or Maximum(2) or Minimum(3)

        :rtype: int
        """

        return self.hybrid_shape_fillet_tri_tangent.RibbonRelimitationMode

    @ribbon_relimitation_mode.setter
    def ribbon_relimitation_mode(self, value: int):
        """
        :param int value:
        """

        self.hybrid_shape_fillet_tri_tangent.RibbonRelimitationMode = value

    @property
    def second_elem(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property SecondElem() As Reference
                | 
                |     Returns or sets the Second support surface feature.
                | 
                |     Example:
                |         This example retrieves in SecondElem the Second support element used by
                |         the HybShpFilletTriTangent hybrid shape feature.
                | 
                |          Dim SecondElem As Reference 
                |          Set SecondElem = HybShpFilletTriTangent.SecondElem
                |          
                | 
                |     Parameters:
                | 
                |         oElem
                |             Second support surface feature.

        :rtype: Reference
        """

        return Reference(self.hybrid_shape_fillet_tri_tangent.SecondElem)

    @second_elem.setter
    def second_elem(self, reference_element: Reference):
        """
        :param Reference reference_element:
        """

        self.hybrid_shape_fillet_tri_tangent.SecondElem = reference_element.com_object

    @property
    def second_orientation(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property SecondOrientation() As long
                | 
                |     Returns or sets the Second orientation used to specify fillet center
                |     position.
                |     note: Orientation is same or inverse than the normal to the Second surface
                |     support

        :rtype: int
        """

        return self.hybrid_shape_fillet_tri_tangent.SecondOrientation

    @second_orientation.setter
    def second_orientation(self, value: int):
        """
        :param int value:
        """

        self.hybrid_shape_fillet_tri_tangent.SecondOrientation = value

    @property
    def supports_trim_mode(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property SupportsTrimMode() As long
                | 
                |     Returns or sets whether support surfaces are trimmed or
                |     not.
                |     Trim (1) or NoTrim(0)
                |     note: if "Trim" the 2 supports are trimmed and assembled with the fillet
                |     ribbon.

        :rtype: int
        """

        return self.hybrid_shape_fillet_tri_tangent.SupportsTrimMode

    @supports_trim_mode.setter
    def supports_trim_mode(self, value: int):
        """
        :param int value:
        """

        self.hybrid_shape_fillet_tri_tangent.SupportsTrimMode = value

    def invert_first_orientation(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub InvertFirstOrientation()
                | 
                |     Inverts first orientation used to specify fillet center position.

        :rtype: None
        """
        return self.hybrid_shape_fillet_tri_tangent.InvertFirstOrientation()

    def invert_remove_orientation(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub InvertRemoveOrientation()
                | 
                |     Inverts third orientation used to specify fillet center position.

        :rtype: None
        """
        return self.hybrid_shape_fillet_tri_tangent.InvertRemoveOrientation()

    def invert_second_orientation(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub InvertSecondOrientation()
                | 
                |     Inverts second orientation used to specify fillet center position.

        :rtype: None
        """
        return self.hybrid_shape_fillet_tri_tangent.InvertSecondOrientation()

    def __repr__(self):
        return f'HybridShapeFilletTriTangent(name="{ self.name }")'
