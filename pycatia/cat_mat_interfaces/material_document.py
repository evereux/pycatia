#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.cat_mat_interfaces.material_families import MaterialFamilies
from pycatia.in_interfaces.document import Document


class MaterialDocument(Document):
    """
    .. note::
        :class: toggle

        CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

            | System.IUnknown
            |     System.IDispatch
            |         System.CATBaseUnknown
            |             System.CATBaseDispatch
            |                 System.AnyObject
            |                     InfInterfaces.Document
            |                         MaterialDocument
            |
            | Represents the Document object for materials.
            | When a MaterialDocument object is created, a MaterialFamily object
            | is created.
            | A Material object is also created inside this MaterialFamily
            | object.

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.material_document = com_object

    @property
    def families(self) -> MaterialFamilies:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Families() As MaterialFamilies (Read Only)
                |
                |     Returns the Family collection object from the current
                |     material document.

        :rtype: MaterialFamilies
        """
        return MaterialFamilies(self.material_document.Families)

    def __repr__(self):
        return f'MaterialDocument(name="{self.name}")'
