#! /usr/bin/python3.6
# module initially auto generated using V5Automation.chm from CATIA R25 on 2020-05-22 12:54:36.956119

from pycatia.mec_mod_interfaces.hybridshape import HybridShape


class HybridShapeExtremum(HybridShape):
    """
        .. note::
            CAA V5 Visual Basic help

                | Represents the hybrid shape extremum feature object.Role: To access
                | the data of the hybrid shape extremum feature object. This data
                | includes:Use the  CATIAHybridShapeFactory to create a
                | HybridShapeExtremum object.

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_extremum = com_object     

    @property
    def direction(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Direction
                | o Property Direction(    ) As
                | 
                | Returns or sets the direction into which the extremum is
                | detected.

        :return:
        """
        return self.hybrid_shape_extremum.Direction

    @direction.setter
    def direction(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_extremum.Direction = value 

    @property
    def direction2(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Direction2
                | o Property Direction2(    ) As
                | 
                | Returns or sets the second direction into which the extremum
                | is detected.

        :return:
        """
        return self.hybrid_shape_extremum.Direction2

    @direction2.setter
    def direction2(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_extremum.Direction2 = value 

    @property
    def direction3(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Direction3
                | o Property Direction3(    ) As
                | 
                | Returns or sets the third direction into which the extremum
                | is detected.

        :return:
        """
        return self.hybrid_shape_extremum.Direction3

    @direction3.setter
    def direction3(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_extremum.Direction3 = value 

    @property
    def extremum_type(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | ExtremumType
                | o Property ExtremumType(    ) As
                | 
                | Returns or sets the extremum type. Legal values: 1 to get a
                | maximum element or 0 to get a minimum element.

        :return:
        """
        return self.hybrid_shape_extremum.ExtremumType

    @extremum_type.setter
    def extremum_type(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_extremum.ExtremumType = value 

    @property
    def extremum_type2(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | ExtremumType2
                | o Property ExtremumType2(    ) As
                | 
                | Returns or sets the extremum type of the second direction.
                | Legal values: 1 to get a maximum element or 0 to get a
                | minimum element.

        :return:
        """
        return self.hybrid_shape_extremum.ExtremumType2

    @extremum_type2.setter
    def extremum_type2(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_extremum.ExtremumType2 = value 

    @property
    def extremum_type3(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | ExtremumType3
                | o Property ExtremumType3(    ) As
                | 
                | Returns or sets the extremum type of the third direction.
                | Legal values: 1 to get a maximum element or 0 to get a
                | minimum element.

        :return:
        """
        return self.hybrid_shape_extremum.ExtremumType3

    @extremum_type3.setter
    def extremum_type3(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_extremum.ExtremumType3 = value 

    @property
    def reference_element(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | ReferenceElement
                | o Property ReferenceElement(    ) As
                | 
                | Returns or sets the object on which the extremum is
                | detected.

        :return:
        """
        return self.hybrid_shape_extremum.ReferenceElement

    @reference_element.setter
    def reference_element(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_extremum.ReferenceElement = value 

    def __repr__(self):
        return f'HybridShapeExtremum()'
