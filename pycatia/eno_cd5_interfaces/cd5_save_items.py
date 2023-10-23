#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.eno_cd5_interfaces.cd5_save_item import CD5SaveItem
from pycatia.system_interfaces.collection import Collection
from pycatia.types.general import cat_variant


class CD5SaveItems(Collection):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     CD5SaveItems
                | 
                | Represents a Collection of items which user is trying to save.
                | 
                | Example:
                | 
                |       The following example indicates how to retrieve the Collection of items
                |       to Save.
                |
                |      Dim oCD5Engine As CD5EngineV6R2014x
                |      Set oCD5Engine = CATIA.GetItem("CD5EngineV6R2014x")
                |      Dim oSaveOperation As CD5SaveOperation
                |      Set oSaveOperation = oCD5Engine.CreateSaveOperation(CD5SaveOperation_Session)
                |      Dim oSaveItems As CD5SaveItems
                |      Set oSaveItems = oSaveOperation.Items()
                |
                | See also:
                |     CD5SaveOperation
    
    """

    def __init__(self, com_object):
        super().__init__(com_object, child_object=CD5SaveItem)
        self.cd5_save_items = com_object

    def item(self, i_index: cat_variant) -> CD5SaveItem:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func Item(CATVariant iIndex) As CD5SaveItem
                |
                |     Returns (gets) an item from the list of items in the current save scope.
                |     First item is at index 1.
                |
                |     Example:
                |
                |           The following example gets a SaveItem at index 1.
                |
                |
                |          Dim oSaveItem As CD5SaveItem
                |          Set oSaveItem = oSaveItems.Item(1)

        :param cat_variant i_index:
        :rtype: CD5SaveItem
        """
        return CD5SaveItem(self.cd5_save_items.Item(i_index).com_object)

    def __repr__(self):
        return f'CD5SaveItems(name="{self.name}")'
