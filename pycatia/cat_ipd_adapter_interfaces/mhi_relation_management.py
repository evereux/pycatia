#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.any_object import AnyObject


class MhiRelationManagement(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MHIRelationManagement
                | 
                | Interface to access all supported relation types and a relation object's
                | atrribute provider to access it's attributes Role:
                | 
                | This interface, given a V5 process, product(or resource) object and the
                | relation type will get the handle to the relation object's attribute
                | provider.
                | 
                | This interface expect caller to use relation types defined in PPR Server which
                | can be obtained by the GetSupportedRelations method
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.mhi_relation_management = com_object

    def get_relation_object(self, i_relation_name: str, i_assigned_object: AnyObject) -> AnyObject:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetRelationObject(CATBSTR iRelationName,
                | CATBaseDispatch iAssignedObject) As CATBaseDispatch
                | 
                |     This method provides handle to the E5 provider on the relation object that
                |     exists between selected activity and an item/resource
                | 
                |     Parameters:
                | 
                |         iRelationName
                |             Name of the relation existing between the selected activity and the
                |             item/resource The possible values for relation name can be obtained through a
                |             call to "DNBIAMHIRelationManagement#GetSupportedRelations" method
                |             
                |         iAssignedObject
                |             The item/resource that is related to the selected activity
                |             
                |         oRelationObjAttrProvider
                |             E5 provider on the relation object that exists between selected
                |             activity and an item/resource 
                | 
                |     Returns:
                |         S_OK or E_FAIL

        :param str i_relation_name:
        :param AnyObject i_assigned_object:
        :rtype: AnyObject
        """
        return self.mhi_relation_management.GetRelationObject(i_relation_name, i_assigned_object.com_object)

    def get_supported_relations(self) -> tuple:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetSupportedRelations() As CATSafeArrayVariant
                | 
                |     This method lists all the possible values that can passed as the relation
                |     name for "DNBIAMHIRelationManagement#GetRelationObject"
                |     method.
                | 
                |     Parameters:
                | 
                |         oListSupportedRelations
                |             The possible relation names can that are supported by the method
                |             GetRelationObject 
                | 
                |     Returns:
                |         S_OK or E_FAIL

        :rtype: tuple
        """
        return self.mhi_relation_management.GetSupportedRelations()

    def __repr__(self):
        return f'MhiRelationManagement(name="{self.name}")'
