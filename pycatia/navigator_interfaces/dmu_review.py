#! usr/bin/python3.6
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.any_object import AnyObject


class DMUReview(AnyObject):
    """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     DMUReview
                | 
                | Represents a DMU Review.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.dmu_review = com_object

    @property
    def activation(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property Activation() As long
                | 
                |     Returns or sets the activation.
                | 
                |     Returns:
                |         The activation
                | 
                |             0: the DMU Review is inactivated.
                |             1: the DMU Review is activated. 
                | 
                |     Example:
                | 
                |              This example retrieves the activation of the oDMUReview DMU Review
                |              and activates it.
                |             
                | 
                |             Activation = oDMUReview.Activation
                |             oDMUReview.Activation = 1

        :return: int
        """

        return self.dmu_review.Activation

    @activation.setter
    def activation(self, value):
        """
        :param int value:
        """

        self.dmu_review.Activation = value

    @property
    def dmu_reviews(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property DMUReviews() As DMUReviews (Read Only)
                | 
                |     Returns the DMUReviews Collection associated with the DMUReview
                |     (children).
                | 
                |     Example:
                | 
                |              This example retrieves the cDMUReviews collection
                |             from the oDMUReview DMU Review.
                |             
                | 
                |             Set cDMUReviews = oDMUReview.DMUReviews(9)

        :return: DMUReviews
        """
        from pycatia.navigator_interfaces.dmu_reviews import DMUReviews
        return DMUReviews(self.dmu_review.DMUReviews)

    def __repr__(self):
        return f'DmuReview(name="{self.name}")'
