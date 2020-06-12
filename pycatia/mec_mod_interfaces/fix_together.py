#! /usr/bin/python3.6
# module initially auto generated using V5Automation.chm from CATIA R25 on 2020-05-18 10:56:40.651039

from pycatia.system_interfaces.any_object import AnyObject
from pycatia.product_structure_interfaces.product import Product


class FixTogether(AnyObject):
    """
        .. note::
            CAA V5 Visual Basic help

                | The object that manages a sequence of products or fixTogethers.It
                | belongs to
                | theactivateLinkAnchor('FixTogether','','FixTogether')collection of
                | aactivateLinkAnchor('Product','','Product').

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.fix_together = com_object

    @property
    def fix_togethers_count(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | FixTogethersCount
                | o Property FixTogethersCount() As   (Read Only)
                | 
                | Returns the number of FixTogether entities in the
                | FixTogether.
                |
                | Example:
                | The following example retrieves in
                | fixTogethersCount the number of FixTogethers of the
                | myFixTogether FixTogether :
                | fixTogethersCount = myFixTogether.FixTogethersCount

        :return: int
        """
        return self.fix_together.FixTogethersCount

    @property
    def products_count(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | ProductsCount
                | o Property ProductsCount() As   (Read Only)
                | 
                | Returns the number of products fixed together in the
                | FixTogether. Example: The following example retrieves in
                | productsCount the number of products of the myFixTogether
                | FixTogether : productsCount = myFixTogether.ProductsCount

        :return: int
        """
        return self.fix_together.ProductsCount

    def add_fix_together(self, i_fix_together):
        """
        .. note::
            CAA V5 Visual Basic help

                | AddFixTogether
                | o Sub AddFixTogether(iFixTogether)
                | 
                | Add a fixTogether to a FixTogether. The fixTogether is fixed
                | together with the products or fixTogethers already contained
                | in the FixTogether. Example: The following example adds a
                | FixTogether fixTogether in a FixTogether myFixTogether.
                | myFixTogether.AddFixTogether(fixTogether)
                |
                | Parameters:
                |

        :param FixTogether() i_fix_together:
        :return:
        """
        self.fix_together.AddFixTogether(i_fix_together.com_object)

    def add_product(self, i_product):
        """
        .. note::
            CAA V5 Visual Basic help

                | AddProduct
                | o Sub AddProduct(iProduct)
                | 
                | Add a product to a FixTogether. The product is fixed
                | together with the products and fixTogethers already
                | contained in the FixTogether.

                | Example:
                | The following example
                | adds a Product myProduct in a FixTogether.
                | myFixTogether.AddProduct(myProduct)

        :param Product() i_product:
        :return:
        """
        return self.fix_together.AddProduct(i_product.com_object)

    def get_fix_together(self, i_index):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetFixTogether
                | o Func GetFixTogether(iIndex) As
                | 
                | Returns a FixTogether using its index or its name in the
                | FixTogether.
                |
                | Parameters:
                | iIndex
                |    The index or the name of the FixTogether to retrieve.
                |    As a numerics, this index is the rank of the FixTogether
                |    in the FixTogethers of the FixTogether.
                |    The index of the first FixTogether is 1, and
                |    the index of the last FixTogether is FixTogethersCount.
                |    As a string, it is the name you assigned to the FixTogether using
                |    the property.
                | Returns:
                |    The retrieved FixTogether
                |
                | Examples:
                | This example retrieves in thisFixTogether the fifth
                | FixTogether and in thatFixTogether the FixTogether named
                | myFixTogether in the FixTogethers of the FixTogether.
                | Dim thisFixTogether As FixTogether
                | Set thisFixTogether = myFixTogether.GetFixTogether(5)
                | Dim thatFixTogether As FixTogether
                | Set thatFixTogether = myFixTogether.GetFixTogether("myFixTogether")

        :param i_index:
        :return:
        """

        return FixTogether(self.fix_together.GetFixTogether(i_index))

    def get_product(self, i_index):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetProduct
                | o Func GetProduct(iIndex) As
                | 
                | Returns a Product using its index or its name in the
                | FixTogether.
                |
                | Parameters:
                | iIndex
                |    The index or the name of the Product to retrieve.
                |    As a numerics, this index is the rank of the Product
                |    in the products of the FixTogether.
                |    The index of the first Product is 1, and
                |    the index of the last Product is ProductsCount.
                |    As a string, it is the name you assigned to the Product using
                |    the property.
                | Returns:
                |    The retrieved Product
                |
                | Examples:
                | This example retrieves in thisProduct the fifth Product and
                | in thatProduct the Product named myProduct in the products
                | of the FixTogether.
                | Dim thisProduct As Product
                | Set thisProduct = myFixTogether.GetProduct(5)
                | Dim thatProduct As Product
                | Set thatProduct = myFixTogether.GetProduct("myProduct")

        :param i_index:
        :return:
        """
        return Product(self.fix_together.GetProduct(i_index))

    def remove_fix_together(self, i_index):
        """
        .. note::
            CAA V5 Visual Basic help

                | RemoveFixTogether
                | o Sub RemoveFixTogether(iIndex)
                | 
                | Removes a FixTogether from the FixTogether.
                |
                | Parameters:
                | iIndex
                |    The index or the name of the FixTogether to remove from the FixTogether.
                |    As a numerics, this index is the rank of the FixTogether
                |    in the FixTogethers of the FixTogether.
                |    The index of the first FixTogether is 1, and
                |    the index of the last FixTogether is FixTogethersCount.
                |    As a string, it is the name you assigned to the FixTogether using
                |    the property.
                |
                | Examples:
                | This example removes the last FixTogether of the
                | FixTogether.
                | fixTogether.RemoveFixTogether(fixTogether.FixTogethersCount)

        :param int i_index:
        :return:
        """
        self.fix_together.RemoveFixTogether(i_index)

    def remove_product(self, i_index):
        """
        .. warning::

            The index when not a string must be it's python index (indexes in python start from 0).
            collection. The COM interface index starts at 1.

        .. note::
            CAA V5 Visual Basic help

                | RemoveProduct
                | o Sub RemoveProduct(iIndex)
                | 
                | Removes a Product from the FixTogether.
                |
                | Parameters:
                | iIndex
                |    The index or the name of the Product to remove from the FixTogether.
                |    As a numerics, this index is the rank of the Product
                |    in the products of the FixTogether.
                |    The index of the first Product is 1, and
                |    the index of the last Product is ProductsCount.
                |    As a string, it is the name you assigned to the FixTogether using
                |    the 
                | 
                |  property.

                |                | Examples:
                | This example removes the last Product of the FixTogether.
                | fixTogether.RemoveProduct(fixTogether.ProductsCount)

        :param int i_index:
        :return:
        """
        self.fix_together.RemoveProduct(i_index)

    def __repr__(self):
        return f'FixTogether(name="{self.name}")'
