#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.part_interfaces.defeaturing_filters import DefeaturingFilters
from pycatia.part_interfaces.dress_up_shape import DressUpShape


class Defeaturing(DressUpShape):

    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.Shape
                |                         PartInterfaces.DressUpShape
                |                             Defeaturing
                | 
                | Represents the defeaturing.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.defeaturing = com_object

    @property
    def filters(self) -> DefeaturingFilters:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Filters() As DefeaturingFilters (Read Only)
                | 
                |     Returns the filter collection of the Defeaturing. The returned object is
                |     the filter collection associated to this Defeaturing object. All changes
                |     applied to the returned collection will be automatically applied to the
                |     Defeaturing object. As a consequence there is no need to affect the collection
                |     to the defeaturing after the change to update the
                |     property.
                | 
                |     Returns:
                |         oFilters The filter collection (see DefeaturingFilters for list of
                |         possible actions)
                | 
                |         Example:
                |             The following example returns in myDefeaturingFiltersCollection the
                |             filter collection of the Defeaturing
                |             firstDefeaturing:
                | 
                |              Set myDefeaturingFiltersCollection = firstDefeaturing.Filters

        :rtype: DefeaturingFilters
        """

        return DefeaturingFilters(self.defeaturing.Filters)

    def __repr__(self):
        return f'Defeaturing(name="{ self.name }")'
