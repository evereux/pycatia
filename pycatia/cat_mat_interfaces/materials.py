#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.collection import Collection
from pycatia.cat_mat_interfaces.material import Material
from pycatia.types.general import cat_variant


class Materials(Collection):
    """
    .. note::
        :class: toggle

        CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

            | System.IUnknown
            |     System.IDispatch
            |         System.CATBaseUnknown
            |             System.CATBaseDispatch
            |                 System.Collection
            |                     Materials
            |
            | A collection of all the Material objects.
            | This collection is currently managed by a MaterialFamily
            | object.

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.materials = com_object

    def add(self) -> Material:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func Add() As Material
                |
                |     Adds a new material to the material collection.

        :rtype: Material
        """
        return Material(self.materials.Add())

    def item(self, i_index: cat_variant) -> Material:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func Item(CATVariant iIndex) As Material
                |
                |     Returns a material from its index in the Material
                |     collection.
                |
                |     Parameters:
                |
                |         iIndex
                |             The index of the material to retrieve in the
                |             collection of materials. Compared with other
                |             collections, you cannot use the name of the
                |             material as argument.
                |
                |     Returns:
                |         The retrieved material
                |
                | Example:
                |     The following example returns in MyMaterial the sixth
                |     material in a material collection.
                |
                |      Dim MyMaterial As Material
                |      Set MyMaterial = Materials.Item(6)

        :param cat_variant i_index:
        :rtype: Material
        """
        return Material(self.materials.Item(i_index))

    def remove(self, i_index: cat_variant) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub Remove(CATVariant iIndex)
                |
                |     Removes a material from the materials collection.

        :param cat_variant i_index:
        :rtype: None
        """
        self.materials.Remove(i_index)

    def sorted_item(self, i_index: cat_variant, i_mode: int) -> Material:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func SortedItem(CATVariant iIndex,
                | short iMode) As Material
                |
                |     Returns a material from its index in the sorted Material
                |     collection.
                |
                |     Parameters:
                |
                |         iIndex
                |             The index of the material to retrieve in the
                |             sorted collection of materials. Compared with
                |             other collections, you cannot use the name of the
                |             material as argument.
                |         iMode
                |             The sorted mode of material collection
                |
                |                 Possible mode values are:
                |                 0: Alphabetical order
                |                 1: Inverse alphabetical order
                |
                |     Returns:
                |         The retrieved material

        :param cat_variant i_index:
        :param int i_mode:
        :rtype: Material
        """
        return Material(self.materials.SortedItem(i_index, i_mode))

    def __repr__(self):
        return f'Materials(name="{self.name}")'
