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


class Outputs(Collection):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     Outputs
                | 
                | The collection of outputs related to the current activity.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object, child_object=Item)
        self.outputs = com_object

    def add(self, i_output: Item) -> Item:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func Add(Item iOutput) As Item
                | 
                |     This method can be used to assign a given product as an
                |     output
                | 
                |     Parameters:
                | 
                |         iOutput
                |             The output to add 
                | 
                |     Returns:
                |         oProduct The assigned product

        :param Item i_output:
        :rtype: Item
        """
        return Item(self.outputs.Add(i_output.com_object))

    def count_(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func Count() As long
                | 
                |     This method returns the no. of products / features that are assigned to a
                |     process as output.
                | 
                |     Returns:
                |         oNbOutputs No. of Outputss that are assigned to the activity.

        :rtype: int
        """
        return self.outputs.Count()

    def item(self, i_index: cat_variant) -> Item:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func Item(CATVariant iIndex) As Item
                | 
                |     This method can be used to get the associated output
                |     product.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The item identifier (can be the index or the name)
                |             
                | 
                |     Returns:
                |         oProduct The indexed product/MA that is assigned to the process.

        :param cat_variant i_index:
        :rtype: Item
        """
        return Item(self.outputs.Item(i_index))

    def remove(self, i_output: Item) -> Item:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func Remove(Item iOutput) As Item
                | 
                |     This method can be used to unassign an output product from a
                |     process
                | 
                |     Parameters:
                | 
                |         iProduct
                |             The product to remove 
                | 
                |     Returns:
                |         oProduct The item

        :param Item i_output:
        :rtype: Item
        """
        return Item(self.outputs.Remove(i_output.com_object))

    def __repr__(self):
        return f'Outputs(name="{self.name}")'
