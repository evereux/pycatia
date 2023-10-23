#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from typing import TYPE_CHECKING

from pycatia.system_interfaces.any_object import AnyObject

if TYPE_CHECKING:
    from pycatia.cat_tps_interfaces.annotations import Annotations


class DatumSimple(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     DatumSimple
                | 
                | Interface for Simple Datum TPS (datum entity).
                | TPS for Technological Product Specifications.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.datum_simple = com_object

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

        return self.datum_simple.Label

    @label.setter
    def label(self, value: str):
        """
        :param str value:
        """

        self.datum_simple.Label = value

    @property
    def targets(self) -> 'Annotations':
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Targets() As Annotations (Read Only)
                | 
                |     Retrieves a CATITPSList to read the list of datum target. All objects of
                |     the list adhere to CATITPSDatumTarget.

        :rtype: Annotations
        """
        from pycatia.cat_tps_interfaces.annotations import Annotations
        return Annotations(self.datum_simple.Targets)

    def __repr__(self):
        return f'DatumSimple(name="{self.name}")'
