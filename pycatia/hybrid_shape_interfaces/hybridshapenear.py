#! /usr/bin/python3.6
# module initially auto generated using V5Automation.chm from CATIA R25 on 2020-05-22 12:54:36.956119

from pycatia.mec_mod_interfaces.hybridshape import HybridShape


class HybridShapeNear(HybridShape):
    """
        .. note::
            CAA V5 Visual Basic help

                | The Near feature : an Near is made up of a face to process and one
                | Near parameter.

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_near = com_object     

    @property
    def multiple_solution(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | MultipleSolution
                | o Property MultipleSolution(    ) As
                | 
                | Role: To get_MultipleSolution on the object.

        :return:
        """
        return self.hybrid_shape_near.MultipleSolution

    @property
    def reference_element(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | ReferenceElement
                | o Property ReferenceElement(    ) As
                | 
                | Role: To get_ReferenceElement on the object.

        :return:
        """
        return self.hybrid_shape_near.ReferenceElement

    def __repr__(self):
        return f'HybridShapeNear()'
