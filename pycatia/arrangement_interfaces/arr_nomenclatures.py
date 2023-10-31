#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.arrangement_interfaces.arr_nomenclature import ArrNomenclature
from pycatia.system_interfaces.collection import Collection
from pycatia.types.general import cat_variant


class ArrNomenclatures(Collection):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     ArrNomenclatures
                | 
                | The collection of UserNomenclature objects.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object, child_object=ArrNomenclature)
        self.arr_nomenclatures = com_object

    def add_user_nomenclature(
            self,
            i_name: str,
            i_icon_name: str,
            i_class_type: str,
            i_super_type: str
    ) -> ArrNomenclature:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func AddUserNomenclature(CATBSTR iName,
                | CATBSTR iIconName,
                | CATBSTR iClassType,
                | CATBSTR iSuperType) As ArrNomenclature
                | 
                |     Creates a new UserNomenclature and adds it to this collection. The
                |     NomenclatureType of the new UserNomenclature will be "User". The base objects
                |     in the UserDictionary are created when the UserDictionary is
                |     created.
                | 
                |     Parameters:
                | 
                |         iName
                |             The user nomenclature name. 
                |         iIconName
                |             The icon name associated to this nomenclature name.
                |
                |     Returns:
                |         The new UserNomenclature.

        :param str i_name:
        :param str i_icon_name:
        :param str i_class_type:
        :param str i_super_type:
        :rtype: ArrNomenclature
        """
        return ArrNomenclature(
            self.arr_nomenclatures.AddUserNomenclature(
                i_name,
                i_icon_name,
                i_class_type,
                i_super_type
            )
        )

    def item(self, i_index: cat_variant) -> ArrNomenclature:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func Item(CATVariant iIndex) As ArrNomenclature
                | 
                |     Returns the specified item of the collection
                | 
                |     Parameters:
                | 
                |         iItem
                |             The list index (long) or name (CATBSTR) of the member to retrieve.
                |             
                | 
                |     Returns:
                |         The retrieved member object.

        :param cat_variant i_index:
        :rtype: ArrNomenclature
        """
        return ArrNomenclature(self.arr_nomenclatures.Item(i_index))

    def __repr__(self):
        return f'ArrNomenclatures(name="{self.name}")'
