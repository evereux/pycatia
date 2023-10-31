#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.any_object import AnyObject


class CompositeTolerance(AnyObject):

    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     CompositeTolerance
                | 
                | Interface for accessing composite tolerance on a TPS.
                | (ASME norm only)
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.composite_tolerance = com_object

    @property
    def box_count(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property BoxCount() As double (Read Only)
                | 
                |     Retrieves datum count.

        :rtype: float
        """

        return self.composite_tolerance.BoxCount

    @property
    def value(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Value() As double (Read Only)
                | 
                |     Retrieves value (in millimeters).
                | 
                |     Parameters:
                | 
                |         oValue
                |             Positive or equal to -1 which means not valuated.

        :rtype: float
        """

        return self.composite_tolerance.Value

    def __repr__(self):
        return f'CompositeTolerance(name="{ self.name }")'
