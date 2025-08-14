#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.product_structure_interfaces.product import Product
from pycatia.system_interfaces.any_object import AnyObject
from pycatia.types.general import cat_variant


class Group(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     Group
                | 
                | Represents a DMU group.
                | The DMU group is an entity which gathers references to several products in
                | order to automate validation and verification of the Digital
                | Mock-Up.
                | 
                | A user can build a group using several methods: explicitely point out some
                | products or take all products by default. The designated products can be
                | intermediate or terminal node of the product structure. For instance, a user
                | who has to verify the integration of the engine in engine bay may define a
                | group with the engine assembly or with all the parts from the engine in order
                | to detect clashes. In the first case this user has to add the engine assembly
                | (as a product) in the group, and in the second case, to add all the parts to
                | the group. Obviously, when a modification happens to the engine assembly the
                | user has to change the group only in the second case. To manage the explicit
                | definition of the group, one may use the XxxxExplicit methods.
                | 
                | When the system takes the group into account to perform a given task, it may be
                | necessary to retrieve:
                | 
                |     The products designated by the user (For example, the section of these
                |     products)
                |     The terminal nodes (or leaves) of the product (For example, clash detection
                |     takes into account terminal nodes)
                |     The set of products in the product structure which are not selected (For
                |     example, hide all products which are not in the group)
                |     The set of terminal nodes which are not selected (For example, clash of
                |     some products against all others). 
                | 
                | To perform these treatments one may use YyyyExtract or ZzzzInvert
                | methods.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.group = com_object

    @property
    def extract_mode(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property ExtractMode() As long
                | 
                |     Returns or sets the mode for the extraction methods.
                | 
                |     Returns:
                |         The extraction mode
                | 
                |             0: the extraction provides the products from the group
                |             (intermediate of terminal nodes).
                |             1: the extraction provides terminal nodes of the products from the
                |             group. 
                | 
                |     Example:
                | 
                |              This example retrieves the extraction mode of the NewGroup Group
                |              and sets it to 1.
                |             
                | 
                |             Dim Mode As Integer
                |             Mode = NewGroup.ExtractMode
                |             NewGroup.ExtractMode = 1

        :rtype: int
        """

        return self.group.ExtractMode

    @extract_mode.setter
    def extract_mode(self, value: int):
        """
        :param int value:
        """

        self.group.ExtractMode = value

    def add_explicit(self, i_product: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub AddExplicit(CATBaseDispatch iProduct)
                | 
                |     Adds a product to the group.
                | 
                |     Parameters:
                | 
                |         iProduct
                |             The product to add 
                | 
                |     Example:
                | 
                |              This example adds the product MyProduct to the group
                |              NewGroup.
                |             
                | 
                |             NewGroup.AddExplicit MyProduct

        :param AnyObject i_product:
        :rtype: None
        """
        return self.group.AddExplicit(i_product.com_object)

    def count_explicit(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func CountExplicit() As long
                | 
                |     Returns the number of products in the group.
                | 
                |     Example:
                | 
                |              This example retrieves the number of products in the group
                |              NewGroup.
                |             
                | 
                |             Dim number As Integer
                |             number = NewGroup.CountExplicit

        :rtype: int
        """
        return self.group.CountExplicit()

    def count_extract(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func CountExtract() As long
                | 
                |     Returns the number of products which can be extracted from the
                |     group.
                | 
                |     Depending on the extraction mode, the extracted products can
                |     be:
                | 
                |         Mode = 0: the products from the group (intermediate or terminal nodes).
                |         Mode = 1: the terminal nodes of the products from the group. 
                | 
                |     Returns:
                |         The number of products 
                |     Example:
                | 
                |              This example reads the number of products in the group
                |              NewGroup.
                |             
                | 
                |             Dim number As Integer
                |             number = NewGroup.CountExtract

        :rtype: int
        """
        return self.group.CountExtract()

    def count_invert(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func CountInvert() As long
                | 
                |     Returns the number of terminal node products which cannot be extracted from
                |     the group.
                | 
                |     Example:
                | 
                |              This example retrieves the number of terminal node products which
                |              cannot be extracted from the group NewGroup.
                |             
                | 
                |             Dim number As Integer
                |             number = NewGroup.CountInvert

        :rtype: int
        """
        return self.group.CountInvert()

    def fill_sel_with_extract(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub FillSelWithExtract()
                | 
                |     Fills the selection with all products which can be extracted from the
                |     group.
                | 
                |     Example:
                | 
                |              This example fills the selection with products which can be
                |              extracted
                |             from the NewGroup group.
                |             
                | 
                |             NewGroup.FillSelWithExtract

        :rtype: None
        """
        return self.group.FillSelWithExtract()

    def fill_sel_with_invert(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub FillSelWithInvert()
                | 
                |     Fills the selection with all terminal node products which cannot be
                |     extracted from the group.
                | 
                |     Example:
                | 
                |              This example fills the selection with all products which cannnot
                |              be extracted
                |             from the NewGroup group.
                |             
                | 
                |             NewGroup.FillSelWithInvert

        :rtype: None
        """
        return self.group.FillSelWithInvert()

    def item_explicit(self, i_index: cat_variant) -> AnyObject:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func ItemExplicit(CATVariant iIndex) As CATBaseDispatch
                | 
                |     Returns a product using its index in the group.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index of the product in the group. The index of the first
                |             product is 1, and the index of the last product is CountExplicit.
                |             
                | 
                |     Returns:
                |         The retrieved product 
                |     Example:
                | 
                |              This example retrieves in ThisProduct the ninth
                |              product
                |             from the NewGroup group.
                |             
                | 
                |             Dim ThisProduct As Product
                |             Set ThisProduct = NewGroup.ItemExplicit(9)

        :param cat_variant i_index:
        :rtype: AnyObject
        """
        return self.group.ItemExplicit(i_index)

    def item_extract(self, i_index: cat_variant) -> Product:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func ItemExtract(CATVariant iIndex) As Product
                | 
                |     Returns a product which can be extracted from the group using its
                |     index.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index of the product in the group. The index of the first
                |             product is 1, and the index of the last product is CountExtract.
                |             
                | 
                |     Returns:
                |         The retrieved product 
                |     Example:
                | 
                |              This example retrieves in ThisProduct the ninth
                |              product
                |             from the NewGroup group.
                |             
                | 
                |             Dim ThisProduct As Group
                |             Set ThisProduct = NewGroup.ItemExtract(9)

        :param cat_variant i_index:
        :rtype: Product
        """
        return Product(self.group.ItemExtract(i_index))

    def item_invert(self, i_index: cat_variant) -> Product:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func ItemInvert(CATVariant iIndex) As Product
                | 
                |     Returns a terminal node product which cannot be extracted from the group
                |     using its index.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index of the product in the group. The index of the first
                |             product is 1, and the index of the last product is CountExtract.
                |             
                | 
                |     Returns:
                |         The retrieved product 
                |     Example:
                | 
                |              This example retrieves in ThisProduct the ninth product which
                |              cannot be extracted from 
                |             the NewGroup group.
                |             
                | 
                |             Dim ThisProduct As Group
                |             Set ThisProduct = NewGroup.ItemInvert(9)

        :param cat_variant i_index:
        :rtype: Product
        """
        return Product(self.group.ItemInvert(i_index))

    def remove_explicit(self, i_index: cat_variant) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub RemoveExplicit(CATVariant iIndex)
                | 
                |     Removes a product from the group using its index.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index of the product in the group. The index of the first
                |             product is 1, and the index of the last product is CountExplicit.
                |             
                | 
                |     Example:
                | 
                |              The following example removes the tenth product from the NewGroup
                |              group.
                |             
                | 
                |             NewGroup.RemoveExplicit 10

        :param cat_variant i_index:
        :rtype: None
        """
        return self.group.RemoveExplicit(i_index)

    def __repr__(self):
        return f'Group(name="{self.name}")'
