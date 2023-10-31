#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.manufacturing_interfaces.manufacturing_feature import ManufacturingFeature
from pycatia.system_interfaces.collection import Collection
from pycatia.types.general import cat_variant


class ManufacturingFeatures(Collection):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     ManufacturingFeatures
                | 
                | Collection of Manufacturing Features.
                | 
                | See also:
                |     ManufacturingFeature
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.manufacturing_features = com_object

    def add(self, i_type: str) -> ManufacturingFeature:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func Add(CATBSTR iType) As ManufacturingFeature
                | 
                |     Create and Add a Manufacturing Feature of a specified type to the
                |     Collection.
                | 
                |     Example:
                |         The following example creates and adds in Features the manufacturing feature Feature of type : type
                | 
                |          Set Feature = Features.Add(Type)

        :param str i_type:
        :rtype: ManufacturingFeature
        """
        return ManufacturingFeature(self.manufacturing_features.Add(i_type))

    def item(self, i_index: cat_variant) -> ManufacturingFeature:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func Item(CATVariant iIndex) As ManufacturingFeature
                | 
                |     Retrieve the Manufacturing Feature of a the specified index from the
                |     Collection.
                | 
                |     Example:
                |         The following example retrieves from Feature the manufacturing feature Feature from index : Index
                | 
                |          Set Feature = Features.Item(Index)

        :param cat_variant i_index:
        :rtype: ManufacturingFeature
        """
        return ManufacturingFeature(self.manufacturing_features.Item(i_index))

    def __repr__(self):
        return f'ManufacturingFeatures(name="{self.name}")'
