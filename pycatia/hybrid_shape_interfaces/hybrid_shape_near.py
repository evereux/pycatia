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


class HybridShapeNear(HybridShape):

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
                |                         HybridShapeNear
                | 
                | The Near feature : an Near is made up of a face to process and one Near parameter.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_near = com_object

    @property
    def multiple_solution(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property MultipleSolution() As Reference
                | 
                |     Role: To get_MultipleSolution on the object.
                | 
                |     Parameters:
                | 
                |         oMultipleSolution
                |             multiple element return value for CATScript applications, with
                |             (IDLRETVAL) function type 
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

        return Reference(self.hybrid_shape_near.MultipleSolution)

    @multiple_solution.setter
    def multiple_solution(self, reference: Reference):
        """
        :param Reference reference:
        """

        self.hybrid_shape_near.MultipleSolution = reference.com_object

    @property
    def reference_element(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property ReferenceElement() As Reference
                | 
                |     Role: To get_ReferenceElement on the object.
                | 
                |     Parameters:
                | 
                |         oRefElem
                |             reference element return value for CATScript applications, with
                |             (IDLRETVAL) function type 
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

        return Reference(self.hybrid_shape_near.ReferenceElement)

    @reference_element.setter
    def reference_element(self, reference_element: Reference):
        """
        :param Reference reference_element:
        """

        self.hybrid_shape_near.ReferenceElement = reference_element.com_object

    def __repr__(self):
        return f'HybridShapeNear(name="{ self.name }")'
