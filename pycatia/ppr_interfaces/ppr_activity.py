#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.dmaps_interfaces.activity import Activity
from pycatia.ppr_interfaces.ppr_products import PPRProducts


class PPRActivity(Activity):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     DMAPSInterfaces.Activity
                |                         PPRActivity
                | 
                | The interface is used to retrieve the items and resources of the current
                | Activity.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.ppr_activity = com_object

    @property
    def ppr_items(self) -> PPRProducts:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property PPRItems() As PPRProducts (Read Only)
                | 
                |     Retrieves the list of items as Products aggregated by the
                |     Activity.
                | 
                |     Returns:
                |         The list of items of the current Activity.

        :rtype: PPRProducts
        """

        return PPRProducts(self.ppr_activity.PPRItems)

    @property
    def ppr_items_and_fta(self) -> list:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property PPRItemsAndFTA() As CATIAPPRItems (Read Only)
                | 
                |     Retrieves the list of items as CATIAItems aggregated by the
                |     Activity.
                | 
                |     Returns:
                |         The list of items of the current Activity, including ASMPRODUCT and
                |         possibly FTA objects

        :rtype: list
        """

        return self.ppr_activity.PPRItemsAndFTA

    @property
    def ppr_resources(self) -> PPRProducts:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property PPRResources() As PPRProducts (Read Only)
                | 
                |     Retrieves the list of resources as Products aggregated by the
                |     Activity.
                | 
                |     Returns:
                |         The list of resources of the current Activity.

        :rtype: PPRProducts
        """

        return PPRProducts(self.ppr_activity.PPRResources)

    def __repr__(self):
        return f'PprActivity(name="{self.name}")'
