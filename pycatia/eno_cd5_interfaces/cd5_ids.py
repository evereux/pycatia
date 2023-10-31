#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.eno_cd5_interfaces.cd5_id import CD5ID
from pycatia.system_interfaces.collection import Collection
from pycatia.types.general import cat_variant


class CD5IDs(Collection):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     CD5IDs
                | 
                | Represents a list of ENOVIA V6 Integration identifier(CD5ID).
                | 
                | Example:
                | 
                |       The following example indicates how to retrieve list of ENOVIA V6
                |       Integration identifier.
                |
                |         PhysicalIDs : "6EFB8D2E00008A445257E36100000DF7,6EFB8D2E00008A445257E3610000090".
                |
                |      Dim oIDs As ENOIACD5IDs
                |      Set oIDs = GetIDsFromPhysicalIDs(PhysicalIDs);
                |
                | See also:
                |     CD5EngineV6R2015, CD5ID
    
    """

    def __init__(self, com_object):
        super().__init__(com_object, child_object=CD5ID)
        self.cd5_i_ds = com_object

    def item(self, i_index: cat_variant) -> CD5ID:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func Item(CATVariant iIndex) As CD5ID
                | 
                |     Returns (gets) CD5ID from the list of ids.
                | 
                |     Example:
                | 
                |           The following example gets a CD5ID at index 1.
                |          
                | 
                |          Dim oID As ENOIACD5ID
                |          Set oID = CD5IDs.Item(1)

        :param cat_variant i_index:
        :rtype: CD5ID
        """
        return CD5ID(self.cd5_i_ds.Item(i_index))

    def __repr__(self):
        return f'CD5IDs(name="{self.name}")'
