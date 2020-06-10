#! usr/bin/python3.6
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-09 09:53:18.676780

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.in_interfaces.reference import Reference
from pycatia.mec_mod_interfaces.hybrid_shape import HybridShape


class HybridShapeInverse(HybridShape):

    """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.HybridShape
                |                         HybridShapeInverse
                | 
                | The Inverse feature : an Inverse is made up of a face to process and one Inverse parameter.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_inverse = com_object

    @property
    def element(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property Element() As Reference
                | 
                |     Role: To get the element inverted.
                | 
                |     Parameters:
                | 
                |         oElem
                |             Element inverted return value for CATScript applications, with
                |             (IDLRETVAL) function type 
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

        return Reference(self.hybrid_shape_inverse.Element)

    @element.setter
    def element(self, value):
        """
        :param Reference value:
        """

        self.hybrid_shape_inverse.Element = value

    @property
    def orientation(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property Orientation() As long
                | 
                |     Gets or sets the element's orientation. Orientation = 1 : the element is not inverted. = -1 : the element is inverted, = 2 : the element can not be inverted. Orientation can not be set to 2.

        :return: int
        """

        return self.hybrid_shape_inverse.Orientation

    @orientation.setter
    def orientation(self, value):
        """
        :param int value:
        """

        self.hybrid_shape_inverse.Orientation = value

    def __repr__(self):
        return f'HybridShapeInverse(name="{ self.name }")'
