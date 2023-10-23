#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.funct_system_interfaces.functional_description import FunctionalDescription


class FunctionalVariant(FunctionalDescription):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     CATFunctSystemItf.FunctionalElement
                |                        
                |                        CATFunctSystemItf.FunctionalDescription
                |                             FunctionalVariant
                | 
                | The interface to access a Functional Variant.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.functional_variant = com_object

    @property
    def original_description(self) -> FunctionalDescription:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property OriginalDescription() As FunctionalDescription (Read
                | Only)
                | 
                |     Returns the Original Description the Variant comes from.

        :rtype: FunctionalDescription
        """

        return FunctionalDescription(self.functional_variant.OriginalDescription)

    def __repr__(self):
        return f'FunctionalVariant(name="{self.name}")'
