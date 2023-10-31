#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from typing import TYPE_CHECKING

from pycatia.system_interfaces.any_object import AnyObject

if TYPE_CHECKING:
    from pycatia.navigator_interfaces.dmu_reviews import DMUReviews


class DMUReview(AnyObject):
    """
        .. note::
            :class: toggle

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
    def activation(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
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

        :rtype: int
        """

        return self.dmu_review.Activation

    @activation.setter
    def activation(self, value: int):
        """
        :param int value:
        """

        self.dmu_review.Activation = value

    @property
    def dmu_reviews(self) -> 'DMUReviews':
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
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

        :rtype: DMUReviews
        """
        from pycatia.navigator_interfaces.dmu_reviews import DMUReviews
        return DMUReviews(self.dmu_review.DMUReviews)

    def __repr__(self):
        return f'DmuReview(name="{self.name}")'
