#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.arrangement_interfaces.arr_nomenclature import ArrNomenclature
from pycatia.arrangement_interfaces.arr_nomenclatures import ArrNomenclatures
from pycatia.system_interfaces.any_object import AnyObject


class ArrNomenclatureTree(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     ArrNomenclatureTree
                | 
                | Represents the root User Dictionary object.
                | The user dictionary defines a hierarchy of user object type names used for
                | dynamically classifying objects. These type names are defined by the user
                | organization according to the needs of the disciplines represented in the data.
                | The user type of any object may be changed as the data becomes more precise.
                | The hierarchy of type names starts with base names, defined by the system, for
                | each type of object. The user organization may define or change the hierarchy
                | of type names under each base name.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.arr_nomenclature_tree = com_object

    @property
    def base_nomenclatures(self) -> ArrNomenclatures:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property BaseNomenclatures() As ArrNomenclatures (Read
                | Only)
                | 
                |     Returns the collection of BaseNomenclatures within this UserDictionary.

        :rtype: ArrNomenclatures
        """

        return ArrNomenclatures(self.arr_nomenclature_tree.BaseNomenclatures)

    def get_nomenclature(self, i_type_name: str) -> ArrNomenclature:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetNomenclature(CATBSTR iTypeName) As ArrNomenclature
                | 
                |     Finds a UserNomenclature by Name from this UserDictionary.

        :param str i_type_name:
        :rtype: ArrNomenclature
        """
        return ArrNomenclature(self.arr_nomenclature_tree.GetNomenclature(i_type_name))

    def __repr__(self):
        return f'ArrNomenclatureTree(name="{self.name}")'
