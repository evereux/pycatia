#! usr/bin/python3.6
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.hybrid_shape_interfaces.hybrid_shape_direction import HybridShapeDirection
from pycatia.in_interfaces.reference import Reference
from pycatia.mec_mod_interfaces.hybrid_shape import HybridShape


class HybridShapeExtremum(HybridShape):

    """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.HybridShape
                |                         HybridShapeExtremum
                | 
                | Represents the hybrid shape extremum feature object.
                | Role: To access the data of the hybrid shape extremum feature object. This data
                | includes:
                | 
                |     The three directions into which the extremum is detected
                |     The object onto which the extremum is detected
                |     The extremum type of each direction
                | 
                | Use the CATIAHybridShapeFactory to create a HybridShapeExtremum
                | object.
                | 
                | See also:
                |     HybridShapeFactory
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_extremum = com_object

    @property
    def direction(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property Direction() As HybridShapeDirection
                | 
                |     Returns or sets the direction into which the extremum is detected.

        :return: HybridShapeDirection
        """

        return HybridShapeDirection(self.hybrid_shape_extremum.Direction)

    @direction.setter
    def direction(self, value):
        """
        :param HybridShapeDirection value:
        """

        self.hybrid_shape_extremum.Direction = value

    @property
    def direction2(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property Direction2() As HybridShapeDirection
                | 
                |     Returns or sets the second direction into which the extremum is detected.

        :return: HybridShapeDirection
        """

        return HybridShapeDirection(self.hybrid_shape_extremum.Direction2)

    @direction2.setter
    def direction2(self, value):
        """
        :param HybridShapeDirection value:
        """

        self.hybrid_shape_extremum.Direction2 = value

    @property
    def direction3(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property Direction3() As HybridShapeDirection
                | 
                |     Returns or sets the third direction into which the extremum is detected.

        :return: HybridShapeDirection
        """

        return HybridShapeDirection(self.hybrid_shape_extremum.Direction3)

    @direction3.setter
    def direction3(self, value):
        """
        :param HybridShapeDirection value:
        """

        self.hybrid_shape_extremum.Direction3 = value

    @property
    def extremum_type(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property ExtremumType() As long
                | 
                |     Returns or sets the extremum type.
                |     Legal values: 1 to get a maximum element or 0 to get a minimum element.

        :return: int
        """

        return self.hybrid_shape_extremum.ExtremumType

    @extremum_type.setter
    def extremum_type(self, value):
        """
        :param int value:
        """

        self.hybrid_shape_extremum.ExtremumType = value

    @property
    def extremum_type2(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property ExtremumType2() As long
                | 
                |     Returns or sets the extremum type of the second direction.
                |     Legal values: 1 to get a maximum element or 0 to get a minimum element.

        :return: int
        """

        return self.hybrid_shape_extremum.ExtremumType2

    @extremum_type2.setter
    def extremum_type2(self, value):
        """
        :param int value:
        """

        self.hybrid_shape_extremum.ExtremumType2 = value

    @property
    def extremum_type3(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property ExtremumType3() As long
                | 
                |     Returns or sets the extremum type of the third direction.
                |     Legal values: 1 to get a maximum element or 0 to get a minimum element.

        :return: int
        """

        return self.hybrid_shape_extremum.ExtremumType3

    @extremum_type3.setter
    def extremum_type3(self, value):
        """
        :param int value:
        """

        self.hybrid_shape_extremum.ExtremumType3 = value

    @property
    def reference_element(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property ReferenceElement() As Reference
                | 
                |     Returns or sets the object on which the extremum is detected.

        :return: Reference
        """

        return Reference(self.hybrid_shape_extremum.ReferenceElement)

    @reference_element.setter
    def reference_element(self, value):
        """
        :param Reference value:
        """

        self.hybrid_shape_extremum.ReferenceElement = value

    def __repr__(self):
        return f'HybridShapeExtremum(name="{ self.name }")'
