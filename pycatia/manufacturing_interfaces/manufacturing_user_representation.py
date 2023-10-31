#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.any_object import AnyObject


class ManufacturingUserRepresentation(AnyObject):

    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     ManufacturingUserRepresentation
                | 
                | Interface dedicated to objects representation management.
                | Role: This interface offers services to manage mainly the user
                | representation.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.manufacturing_user_representation = com_object

    def set_representation(self, i_path_name: str) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetRepresentation(CATBSTR iPathName)
                | 
                |     Sets the User Representation Associated to the Object.
                | 
                |     Parameters:
                | 
                |         iPathName
                |             The complete absolute path name to the External
                |             Object

        :param str i_path_name:
        :rtype: None
        """
        return self.manufacturing_user_representation.SetRepresentation(i_path_name)

    def __repr__(self):
        return f'ManufacturingUserRepresentation(name="{ self.name }")'
