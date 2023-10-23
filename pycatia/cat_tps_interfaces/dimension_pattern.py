#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.any_object import AnyObject


class DimensionPattern(AnyObject):

    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     DimensionPattern
                | 
                | Interface to dimension pattern.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.dimension_pattern = com_object

    @property
    def instance_count(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property InstanceCount() As double (Read Only)
                | 
                |     Get count of instances.

        :rtype: float
        """

        return self.dimension_pattern.InstanceCount

    def __repr__(self):
        return f'DimensionPattern(name="{ self.name }")'
