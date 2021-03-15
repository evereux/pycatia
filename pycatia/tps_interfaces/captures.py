#! usr/bin/python3.6
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.any_object import AnyObject
from pycatia.system_interfaces.collection import Collection
from pycatia.tps_interfaces.capture import Capture


class Captures(Collection):

    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     Captures
                | 
                | The interface to access a CATIACaptures
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.captures = com_object

    def item(self, i_index: CATVariant) -> AnyObject:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func Item(CATVariant iIndex) As AnyObject
                | 
                |     Retrieve a Capture.

        :param CATVariant i_index:
        :return: AnyObject
        :rtype: AnyObject
        """
        return AnyObject(self.captures.Item(i_index.com_object))

    def __repr__(self):
        return f'Captures(name="{ self.name }")'
