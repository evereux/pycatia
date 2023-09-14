#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.dnb_human_modeling_interfaces.swk_body_element import SWKBodyElement


class SWKCenterOfGravity(SWKBodyElement):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     DNBHumanModelingInterfaces.SWKBodyElement
                |                         SWKCenterOfGravity
                | 
                | This interface represents the center of gravity of the
                | manikin.

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.swk_center_of_gravity = com_object

    def __repr__(self):
        return f'SWKCenterOfGravity(name="{self.name}")'
