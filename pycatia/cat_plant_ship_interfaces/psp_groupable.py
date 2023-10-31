#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.cat_plant_ship_interfaces.psp_list_of_objects import PSPListOfObjects
from pycatia.system_interfaces.any_object import AnyObject


class PSPGroupable(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     PspGroupable
                | 
                | Represent the Groupable object that can be grouped by Group
                | object.
                | Role: It is used to query the group object link to this
                | object.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.psp_groupable = com_object

    @property
    def groups(self) -> PSPListOfObjects:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Groups() As PspListOfObjects (Read Only)
                | 
                |     Returns a list of Groups to which this object is a member.
                | 
                |     Example:
                |
                |          Dim objThisIntf As PspGroupable  
                |          Dim objArg1 As PspListOfObjects
                |          
                |           ...
                |          Set ObjArg1 = objThisIntf.Groups

        :rtype: PSPListOfObjects
        """

        return PSPListOfObjects(self.psp_groupable.Groups)

    def __repr__(self):
        return f'PSPGroupable(name="{self.name}")'
