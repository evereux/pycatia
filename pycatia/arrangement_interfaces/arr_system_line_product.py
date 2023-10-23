#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.any_object import AnyObject


class ArrSystemLineProduct(AnyObject):

    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     ArrSystemLineProduct
                | 
                | The interface to access a CATIAArrSystemLineProduct
                | 
                | Using this prefered syntax will enable mkdoc to document your
                | class.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.arr_system_line_product = com_object

    def get_sub_item(self, i_index: int) -> AnyObject:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetSubItem(long iIndex) As AnyObject
                | 
                |     Allows the user to get the item at a specific index location.

        :param int i_index:
        :rtype: AnyObject
        """
        return AnyObject(self.arr_system_line_product.GetSubItem(i_index))

    def get_sub_products_count(self, i_intf_id: str) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetSubProductsCount(CATBSTR iIntfId) As long
                | 
                |     Returns the count of the sub-products that make up the System-Line
                |     Arrangement Product and that match a specifc interface id. If the interface Id
                |     is NULL, then it searches for CATIAProduct objects by default.

        :param str i_intf_id:
        :rtype: int
        """
        return self.arr_system_line_product.GetSubProductsCount(i_intf_id)

    def __repr__(self):
        return f'ArrSystemLineProduct(name="{ self.name }")'
