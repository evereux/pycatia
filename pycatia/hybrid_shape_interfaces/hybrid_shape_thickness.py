#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-07-06 14:02:20.222384

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.knowledge_interfaces.length import Length
from pycatia.mec_mod_interfaces.hybrid_shape import HybridShape


class HybridShapeThickness(HybridShape):
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
                |                         HybridShapeThickness
                | 
                | Represents the hybrid shape Thickness feature object.
                | Role: To access the data of the thickness on an hybrid shape feature object.
                | This data includes:
                | 
                |     The thickness orientation
                |     The thickness1 value
                |     The thickness2 value
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_thickness = com_object

    @property
    def orientation(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Orientation() As long
                | 
                |     Returns or sets the orientation.
                |     Role:
                |     Orientation
                |     1 means that the first thickness is measured with the normal of the support Orientation
                |     -1 means that the first thickness is measured with the inverted normal of the support
                | 
                |     Example:
                |         This example retrieves in Orient the orientation for the Thickness1
                |         hybrid shape feature.
                | 
                |          Dim Orient As long
                |          Set Orient = Thickness1.Orientation

        :rtype: int
        """

        return self.hybrid_shape_thickness.Orientation

    @orientation.setter
    def orientation(self, value: int):
        """
        :param int value:
        """

        self.hybrid_shape_thickness.Orientation = value

    @property
    def thickness1(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Thickness1() As double
                | 
                |     Returns or sets the first thickness value in mm.
                | 
                |     Example: This example retrieves in ThickVal1 the first thickness value for
                |     the Thick hybrid shape feature.
                | 
                |      Dim ThickVal1 As double
                |      Set ThickVal1 = Thick.Thickness1

        :rtype: float
        """

        return self.hybrid_shape_thickness.Thickness1

    @thickness1.setter
    def thickness1(self, value: float):
        """
        :param float value:
        """

        self.hybrid_shape_thickness.Thickness1 = value

    @property
    def thickness1_value(self) -> Length:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Thickness1Value() As Length (Read Only)
                | 
                |     Returns the first thickness value.
                | 
                |     Example:
                |         This example retrieves in ThickVal1 the first thickness value for the
                |         Thick hybrid shape feature.
                | 
                |          Dim ThickVal1 As Length
                |          Set ThickVal1 = Thick.Thickness1Value

        :rtype: Length
        """

        return Length(self.hybrid_shape_thickness.Thickness1Value)

    @property
    def thickness2(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Thickness2() As double
                | 
                |     Returns or sets the second thickness value in mm.
                | 
                |     Example: This example retrieves in ThickVal2 the second thickness value for
                |     the Thick hybrid shape feature.
                | 
                |      Dim ThickVal2 As double
                |      Set ThickVal2 = Thick.Thickness2

        :rtype: float
        """

        return self.hybrid_shape_thickness.Thickness2

    @thickness2.setter
    def thickness2(self, value: float):
        """
        :param float value:
        """

        self.hybrid_shape_thickness.Thickness2 = value

    @property
    def thickness2_value(self) -> Length:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Thickness2Value() As Length (Read Only)
                | 
                |     Returns the second thickness value.
                | 
                |     Example:
                |         This example retrieves in ThickVal2 the second thickness value for the
                |         Thick hybrid shape feature.
                | 
                |          Dim ThickVal2 As Length
                |          Set ThickVal2 = Thick.Thickness2Value

        :rtype: Length
        """

        return Length(self.hybrid_shape_thickness.Thickness2Value)

    def __repr__(self):
        return f'HybridShapeThickness(name="{self.name}")'
