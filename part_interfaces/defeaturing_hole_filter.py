#! usr/bin/python3.6
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.part_interfaces.defeaturing_filter_with_range import DefeaturingFilterWithRange


class DefeaturingHoleFilter(DefeaturingFilterWithRange):

    """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     PartInterfaces.DefeaturingFilter
                |                        PartInterfaces.DefeaturingFilterWithRange
                |                             DefeaturingHoleFilter
                | 
                | Represents the defeaturing hole filter.
                | 
                | Copyright © 1999-2011, Dassault Systèmes. All rights reserved.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.defeaturing_hole_filter = com_object

    def __repr__(self):
        return f'DefeaturingHoleFilter(name="{ self.name }")'
