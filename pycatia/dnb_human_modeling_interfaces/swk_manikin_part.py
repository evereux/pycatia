#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.any_object import AnyObject


class SWKManikinPart(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SWKManikinPart
                | 
                | This interface represents any part of the manikin that is
                | persistent.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.swk_manikin_part = com_object

    @property
    def memo(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Memo() As CATBSTR
                | 
                |     Returns or records miscellaneous user-added information about the part.

        :rtype: str
        """

        return self.swk_manikin_part.Memo

    @memo.setter
    def memo(self, value: str):
        """
        :param str value:
        """

        self.swk_manikin_part.Memo = value

    def __repr__(self):
        return f'SWKManikinPart(name="{self.name}")'
