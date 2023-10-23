#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.cat_mat_interfaces.material_family import MaterialFamily
from pycatia.system_interfaces.collection import Collection
from pycatia.types.general import cat_variant


class MaterialFamilies(Collection):
    """
    .. note::
        :class: toggle

        CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

            | System.IUnknown
            |     System.IDispatch
            |         System.CATBaseUnknown
            |             System.CATBaseDispatch
            |                 System.Collection
            |                     MaterialFamilies
            |
            | A collection of all the MaterialFamily objects.
            | This collection is currently managed by a CATIAMaterialDocument
            | object.

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.material_families = com_object

    def add(self) -> MaterialFamily:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func Add() As MaterialFamily
                |
                |     Adds a new material family to the MaterialFamilies collection.
                |
                |
                | Example:
                |     The following adds a material family to the collection
                |     attached to a document. This document must be a
                |     MaterialDocument object.
                |
                |      FileToOpen = "e:\\users\\ast\\materials\\Catalog.CATMaterial"
                |      Dim MyDocument As MaterialDocument
                |      Set MyDocument = Documents.Open(FileToOpen)
                |      Dim MyMaterialFamily As MaterialFamily
                |      Set MyMaterialFamily = MyDocument.MaterialFamilies.Add

        :rtype: MaterialFamily
        """
        return MaterialFamily(self.material_families.Add())

    def item(self, i_index: cat_variant) -> MaterialFamily:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func Item(CATVariant iIndex) As MaterialFamily
                |
                |     Returns a material family from its index in the
                |     MaterialFamilies collection.
                |
                |     Parameters:
                |
                |         iIndex
                |             The index of the material family to retrieve in
                |             the collection of material families. Compared with
                |             other collections, you cannot use the name of
                |             the material family as argument.
                |
                |     Returns:
                |         The retrieved material family
                |
                | Example:
                |     The following example returns in MyMaterialFamily the
                |     sixth
                |     material family in the collection.
                |
                |      Dim MyMaterialFamily As MaterialFamily
                |      Set MyMaterialFamily = MaterialFamilies.Item(6)

        :param cat_variant i_index:
        :rtype: MaterialFamily
        """
        return MaterialFamily(self.material_families.Item(i_index))

    def remove(self, i_index: cat_variant) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub Remove(CATVariant iIndex)
                |
                |     Removes a material family from the MaterialFamilies
                |     collection.
                |
                |     Parameters:
                |
                |         iIndex
                |             The index of the material family to remove.
                |             Compared with other collections, you cannot use
                |             the name of the material family as argument.
                |
                |
                |     Example:
                |         The following example removes the second material
                |         family in the collection attached to the active
                |         document. This document must be a MaterialDocument
                |         object.
                |
                |      FileToOpen = "e:\\users\\ast\\materials\\Catalog.CATMaterial"
                |      Dim MyDocument As MaterialDocument
                |      Set MyDocument = Documents.Open(FileToOpen)
                |      MyDocument.MaterialFamilies.Remove(2)

        :param cat_variant i_index:
        :rtype: None
        """
        self.material_families.Remove(i_index)

    def __repr__(self):
        return f'MaterialFamilies(name="{self.name}")'
