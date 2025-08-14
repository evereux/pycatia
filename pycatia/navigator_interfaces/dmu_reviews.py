#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from typing import Iterator

from pycatia.navigator_interfaces.dmu_review import DMUReview
from pycatia.product_structure_interfaces.product import Product
from pycatia.system_interfaces.any_object import AnyObject
from pycatia.system_interfaces.collection import Collection
from pycatia.types.general import cat_variant


class DMUReviews(Collection):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     DMUReviews
                | 
                | A collection of all DMUReviews currently managed by the
                | application.
                | 
                | The method Product.GetTechnologicalObject ("DMUReviews") retrieves this
                | collection.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object, child_object=DMUReview)
        self.dmu_reviews = com_object

    @property
    def current(self) -> AnyObject:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Current() As CATBaseDispatch (Read Only)
                | 
                |     Returns the current DMUReview.
                | 
                |     Returns:
                |         The current DMUReview (the collection is returned if there is no
                |         current review) 
                |     Example:
                | 
                |              This example retrieves the current oDMUReview DMU
                |              Review
                |             from the cDMUReviews collection.
                |             
                | 
                |             Set oDMUReview = cDMUReviews.Current

        :rtype: AnyObject
        """

        return AnyObject(self.dmu_reviews.Current)

    def add(self) -> DMUReview:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func Add() As DMUReview
                | 
                |     Creates a DMUReview and adds it to the DMUReviews
                |     Collection.
                | 
                |     Returns:
                |         The created DMUReview 
                |     Example:
                | 
                |              This example creates a new DMUReview in the cDMUReviews
                |              collection.
                |             
                | 
                |             Set oDMUReview = cDMUReviews.Add

        :rtype: DMUReview
        """
        return DMUReview(self.dmu_reviews.Add())

    def import_from(self, i_product: Product) -> DMUReview:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func ImportFrom(Product iProduct) As DMUReview
                | 
                |     Imports Applicative data froma given product in a new DMU
                |     Review
                | 
                |     Parameters:
                | 
                |         iProduct
                |             The product to import applicative data from 
                | 
                |     Returns:
                |         The created DMUReview 
                |     Example:
                | 
                |              This example imports a new DMUReview from a product in the
                |              cDMUReviews collection.
                |             
                | 
                |             Set oDMUReview = cDMUReviews.ImportFrom(iExistingProduct)

        :param Product i_product:
        :rtype: DMUReview
        """
        return DMUReview(self.dmu_reviews.ImportFrom(i_product.com_object))

    def item(self, i_index: cat_variant) -> DMUReview:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func Item(CATVariant iIndex) As DMUReview
                | 
                |     Returns a DMUReview using its index or its name from the DMUReviews
                |     collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the DMUReview to retrieve from the
                |             collection of DMUReviews. As a numerics, this index is the rank of the
                |             DMUReview in the collection. The index of the first DMUReview in the collection
                |             is 1, and the index of the last DMUReview is Count. As a string, it is the name
                |             you assigned to the DMUReview. 
                | 
                |     Returns:
                |         The retrieved DMUReview 
                |     Example:
                | 
                |              This example retrieves in oThisDMUReview the ninth
                |              DMUReview,
                |             and in oThatDMUReview the DMUReview named
                |             DMUReview3 from the cDMUReviews collection. 
                |             
                | 
                |             Set oThisDMUReview = cDMUReviews.Item(9)
                |             Set oThatDMUReview = cDMUReviews.Item("DMUReview3")

        :param cat_variant i_index:
        :rtype: DMUReview
        """
        return DMUReview(self.dmu_reviews.Item(i_index))

    def remove(self, i_index: cat_variant) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub Remove(CATVariant iIndex)
                | 
                |     Removes a DMUReview from the DMUReviews collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the DMUReview to retrieve from the
                |             collection of DMUReviews. As a numerics, this index is the rank of the
                |             DMUReview in the collection. The index of the first DMUReview in the collection
                |             is 1, and the index of the last DMUReview is Count. As a string, it is the name
                |             you assigned to the DMUReview. 
                | 
                |     Example:
                | 
                |              The following example removes the tenth DMUReview and the
                |              DMUReview named
                |             DMUReview2 from the cDMUReviews collection.
                |             
                | 
                |             cDMUReviews.Remove(10)
                |             cDMUReviews.Remove("DMUReview2")

        :param cat_variant i_index:
        :rtype: None
        """
        return self.dmu_reviews.Remove(i_index)

    def __getitem__(self, n: int) -> DMUReview:
        if (n + 1) > self.count:
            raise StopIteration

        return DMUReview(self.dmu_reviews.Item(n + 1))

    def __iter__(self) -> Iterator[DMUReview]:
        for i in range(self.count):
            yield self.child_object(self.com_object.Item(i + 1))

    def __repr__(self):
        return f'DmuReviews(name="{self.name}")'
