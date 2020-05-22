#! /usr/bin/python3.6
# module initially auto generated using V5Automation.chm from CATIA R25 on 2020-05-22 12:54:36.956119

from pycatia.mec_mod_interfaces.hybridshape import HybridShape


class HybridShapeInverse(HybridShape):
    """
        .. note::
            CAA V5 Visual Basic help

                | The Inverse feature : an Inverse is made up of a face to process and
                | one Inverse parameter.

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_inverse = com_object     

    @property
    def element(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Element
                | o Property Element(    ) As
                | 
                | Role: To get the element inverted.

        :return:
        """
        return self.hybrid_shape_inverse.Element

    @property
    def orientation(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Orientation
                | o Property Orientation(    ) As
                | 
                | Gets or sets the element's orientation. Orientation = 1 :
                | the element is not inverted. = -1 : the element is inverted,
                | = 2 : the element can not be inverted. Orientation can not
                | be set to 2.

        :return:
        """
        return self.hybrid_shape_inverse.Orientation

    def __repr__(self):
        return f'HybridShapeInverse()'
