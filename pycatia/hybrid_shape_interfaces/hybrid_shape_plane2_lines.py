#! usr/bin/python3.6
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-09 09:53:18.676780

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.hybrid_shape_interfaces.plane import Plane
from pycatia.in_interfaces.reference import Reference


class HybridShapePlane2Lines(Plane):

    """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.HybridShape
                |                         CATGSMIDLItf.Plane
                |                             HybridShapePlane2Lines
                | 
                | plane defined by two lines.
                | Role: Allows to access data of the plane feature passing though two
                | lines.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_plane2_lines = com_object

    @property
    def first(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property First() As Reference
                | 
                |     Role: Get the first line.
                | 
                |     Parameters:
                | 
                |         oLine1
                |             first line. 
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

        return Reference(self.hybrid_shape_plane2_lines.First)

    @first.setter
    def first(self, value):
        """
        :param Reference value:
        """

        self.hybrid_shape_plane2_lines.First = value

    @property
    def forbid_non_coplanar_lines(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property ForbidNonCoplanarLines(boolean iCoplanarLines)
                | 
                |     if ForbidNonCoplanarLines = TRUE, both lines have to be on the same plane. if ForbidNonCoplanarLines = FALSE, both lines can be non coplanar.

        :return: False
        """

        return None

    @forbid_non_coplanar_lines.setter
    def forbid_non_coplanar_lines(self, value):
        """
        :param False value:
        """

        self.hybrid_shape_plane2_lines.ForbidNonCoplanarLines = value

    @property
    def second(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property Second() As Reference
                | 
                |     Role: Get the second line.
                | 
                |     Parameters:
                | 
                |         oLine2
                |             second line. 
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

        return Reference(self.hybrid_shape_plane2_lines.Second)

    @second.setter
    def second(self, value):
        """
        :param Reference value:
        """

        self.hybrid_shape_plane2_lines.Second = value

    def __repr__(self):
        return f'HybridShapePlane2Lines(name="{ self.name }")'
