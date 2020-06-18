#! usr/bin/python3.6
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.navigator_interfaces.dmu_review import DMUReview
from pycatia.system_interfaces.any_object import AnyObject
from pycatia.system_interfaces.collection import Collection


class DMUReviews(Collection):

    """
        .. note::
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
        super().__init__(com_object)
        self.dmu_reviews = com_object

    @property
    def current(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
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

        :return: AnyObject
        """

        return AnyObject(self.dmu_reviews.Current)

    def add(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
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

        :return: DMUReview
        """
        return DMUReview(self.dmu_reviews.Add())

    def import_from(self, i_product=None):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
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
        :return: DMUReview
        """
        return DMUReview(self.dmu_reviews.ImportFrom(i_product.com_object))

    def item(self, i_index=None):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
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

        :param CATVariant i_index:
        :return: DMUReview
        """
        return DMUReview(self.dmu_reviews.Item(i_index.com_object))

    def remove(self, i_index=None):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
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

        :param CATVariant i_index:
        :return: None
        """
        return self.dmu_reviews.Remove(i_index.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'remove'
        # # vba_code = """
        # # Public Function remove(dmu_reviews)
        # #     Dim iIndex (2)
        # #     dmu_reviews.Remove iIndex
        # #     remove = iIndex
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'DmuReviews(name="{ self.name }")'
