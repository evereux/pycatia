#! /usr/bin/python3.6
# module initially auto generated using V5Automation.chm from CATIA R25 on 2020-05-22 12:54:36.956119

from pycatia.mec_mod_interfaces.hybridshape import HybridShape


class HybridShapeThickness(HybridShape):
    """
        .. note::
            CAA V5 Visual Basic help

                | Represents the hybrid shape Thickness feature object.Role: To access
                | the data of the thickness on an hybrid shape feature object. This data
                | includes:

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_thickness = com_object     

    @property
    def orientation(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Orientation
                | o Property Orientation(    ) As
                | 
                | Returns or sets the orientation. Role: Orientation = 1 means
                | that the first thickness is measured with the normal of the
                | support Orientation = -1 means that the first thickness is
                | measured with the inverted normal of the support Example:
                | This example retrieves in Orient the orientation for the
                | Thickness1 hybrid shape feature. Dim Orient As long Set
                | Orient = Thickness1.Orientation

        :return:
        """
        return self.hybrid_shape_thickness.Orientation

    @orientation.setter
    def orientation(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_thickness.Orientation = value 

    @property
    def thickness1(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Thickness1
                | o Property Thickness1(    ) As
                | 
                | Returns or sets the first thickness value in mm. Example:
                | This example retrieves in ThickVal1 the first thickness
                | value for the Thick hybrid shape feature. Dim ThickVal1 As
                | double Set ThickVal1 = Thick.Thickness1

        :return:
        """
        return self.hybrid_shape_thickness.Thickness1

    @thickness1.setter
    def thickness1(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_thickness.Thickness1 = value 

    @property
    def thickness1_value(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Thickness1Value
                | o Property Thickness1Value(    ) As   (Read Only)
                | 
                | Returns the first thickness value. 
                |
                | Example:
                | This example
                | retrieves in ThickVal1 the first thickness value for the
                | Thick hybrid shape feature. Dim ThickVal1 As Length Set
                | ThickVal1 = Thick.Thickness1Value

        :return:
        """
        return self.hybrid_shape_thickness.Thickness1Value

    @property
    def thickness2(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Thickness2
                | o Property Thickness2(    ) As
                | 
                | Returns or sets the second thickness value in mm. Example:
                | This example retrieves in ThickVal2 the second thickness
                | value for the Thick hybrid shape feature. Dim ThickVal2 As
                | double Set ThickVal2 = Thick.Thickness2

        :return:
        """
        return self.hybrid_shape_thickness.Thickness2

    @thickness2.setter
    def thickness2(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_thickness.Thickness2 = value 

    @property
    def thickness2_value(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Thickness2Value
                | o Property Thickness2Value(    ) As   (Read Only)
                | 
                | Returns the second thickness value. 
                |
                | Example:
                | This example
                | retrieves in ThickVal2 the second thickness value for the
                | Thick hybrid shape feature. Dim ThickVal2 As Length Set
                | ThickVal2 = Thick.Thickness2Value

        :return:
        """
        return self.hybrid_shape_thickness.Thickness2Value

    def __repr__(self):
        return f'HybridShapeThickness()'
