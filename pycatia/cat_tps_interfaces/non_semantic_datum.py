#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.any_object import AnyObject


class NonSemanticDatum(AnyObject):

    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     NonSemanticDatum
                | 
                | Interface Managing Non Semantic Datum.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.non_semantic_datum = com_object

    @property
    def label(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Label() As CATBSTR
                | 
                |     Retrieves or sets Label.

        :rtype: str
        """

        return self.non_semantic_datum.Label

    @label.setter
    def label(self, value: str):
        """
        :param str value:
        """

        self.non_semantic_datum.Label = value

    def __repr__(self):
        return f'NonSemanticDatum(name="{ self.name }")'
