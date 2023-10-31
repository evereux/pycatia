#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.dmaps_interfaces.item import Item
from pycatia.system_interfaces.collection import Collection
from pycatia.types.general import cat_variant


class Items(Collection):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     Items
                | 
                | The collection of items related to the current activity.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object, child_object=Item)
        self.items_ = com_object

    def add(self, i_product: Item) -> Item:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func Add(Item iProduct) As Item
                | 
                |     This method adds the specified item in the current list
                | 
                |     Parameters:
                | 
                |         iItem
                |             The item to add 
                | 
                |     Returns:
                |         oitem The item

        :param Item i_product:
        :rtype: Item
        """
        return Item(self.items_.Add(i_product.com_object))

    def add_by_assignment_type(self, i_item: Item, i_assignment_type: int) -> Item:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func AddByAssignmentType(Item iItem,
                | ItemAssignmentType iAssignmentType) As Item
                | 
                |     This method Assigns the specified item with the specified assignment
                |     type
                | 
                |     Parameters:
                | 
                |         iItem
                |             The item to be assigned 
                |         iAssignmentType
                |             Type of the Assignment (Item to the Process) 
                | 
                |     Returns:
                |         oitem The item

        :param Item i_item:
        :param int i_assignment_type: enum item_assignment_type
        :rtype: Item
        """
        return Item(self.items_.AddByAssignmentType(i_item.com_object, i_assignment_type))

    def count_by_assignment_type(self, i_assignment_type: int) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func CountByAssignmentType(ItemAssignmentType iAssignmentType) As
                | long
                | 
                |     This method returns the Number of items that assocated with the activity
                |     with given Assignment Type.
                | 
                |     Parameters:
                | 
                |         iAssignmentType
                |             Type of the Assignment between items & the activity
                |             
                | 
                |     Returns:
                |         oNbItems No. of Items that are assigned to the activity with the given
                |         assignment type.

        :param int i_assignment_type: enum item_assignment_type
        :rtype: int
        """
        return self.items_.CountByAssignmentType(i_assignment_type)

    def item(self, i_index: cat_variant) -> Item:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func Item(CATVariant iIndex) As Item
                | 
                |     This method returns the idl object Item for the specified item
                |     identifier.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The item identifier 
                | 
                |     Returns:
                |         oItem The idl item

        :param cat_variant i_index:
        :rtype: Item
        """
        return Item(self.items_.Item(i_index))

    def item_by_assignment_type(self, i_index: cat_variant, i_assignment_type: int) -> Item:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func ItemByAssignmentType(CATVariant iIndex,
                | ItemAssignmentType iAssignmentType) As Item
                | 
                |     This method returns the item assocated with the activity with given
                |     Assignment Type.
                | 
                |     Parameters:
                | 
                |         iAssignmentType
                |             Type of the Assignment between item & the activity
                |             
                | 
                |     Returns:
                |         oItem idl item to be returned

        :param cat_variant i_index:
        :param int i_assignment_type: enum item_assignment_type
        :rtype: Item
        """
        return Item(self.items_.ItemByAssignmentType(i_index, i_assignment_type))

    def remove_by_assignment_type(self, i_item: Item, i_assignment_type: int) -> Item:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func RemoveByAssignmentType(Item iItem,
                | ItemAssignmentType iAssignmentType) As Item
                | 
                |     This method used to unassign the specified item (with the given assignment
                |     type)
                | 
                |     Parameters:
                | 
                |         iItem
                |             The item to be Unassigned 
                |         iAssignmentType
                |             Type of the Assignment (Item to the Process) to be removed
                |             
                | 
                |     Returns:
                |         oitem The item

        :param Item i_item:
        :param int i_assignment_type: enum item_assignment_type
        :rtype: Item
        """
        return Item(self.items_.RemoveByAssignmentType(i_item.com_object, i_assignment_type))

    def __repr__(self):
        return f'Items(name="{self.name}")'
