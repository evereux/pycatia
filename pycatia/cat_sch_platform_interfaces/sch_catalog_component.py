#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.cat_sch_platform_interfaces.sch_comp_group_ext import SchCompGroupExt
from pycatia.cat_sch_platform_interfaces.sch_grr_comp import SchGRRComp
from pycatia.system_interfaces.any_object import AnyObject


class SchCatalogComponent(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SchCatalogComponent
                | 
                | Manage a schematic component catalog.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.sch_catalog_component = com_object

    def query_drop_ability(self, o_b_yes: bool) -> SchGRRComp:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func QueryDropAbility(boolean oBYes) As SchGRRComp
                | 
                |     Check to see if it is OK to be dropped to the current
                |     document.
                | 
                |     Parameters:
                | 
                |         oBYes
                |             If TRUE, then it is OK to be dropped. 
                |         oPointedToComp
                |             Graphical representation of a component pointed-to by the catalog
                |             description 
                | 
                |     Example:
                |
                |          Dim objThisIntf As SchCatalogComponent
                |          Dim bVar1 As boolean
                |          Dim objArg2 As SchGRRComp
                |           ...
                |          Set objArg2 = objThisIntf.QueryDropAbility

        :param bool o_b_yes:
        :rtype: SchGRRComp
        """
        return SchGRRComp(self.sch_catalog_component.QueryDropAbility(o_b_yes))

    def query_drop_comp_group_ability(self, o_b_yes: bool) -> SchCompGroupExt:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func QueryDropCompGroupAbility(boolean oBYes) As
                | SchCompGroupExt
                | 
                |     Check to see if it is OK to be dropped a component group to the current
                |     document.
                | 
                |     Parameters:
                | 
                |         oBYes
                |             If TRUE, then it is OK to be dropped. 
                |         oPointedToGroup
                |             Component group extension pointed-to by the catalog description
                |
                |     Example:
                |
                |          Dim objThisIntf As SchCatalogComponent
                |          Dim bVar1 As boolean
                |          Dim objArg2 As SchCompGroupExt
                |           ...
                |          Set objArg2 = objThisIntf.QueryDropCompGroupAbility

        :param bool o_b_yes:
        :rtype: SchCompGroupExt
        """
        return SchCompGroupExt(self.sch_catalog_component.QueryDropCompGroupAbility(o_b_yes))

    def __repr__(self):
        return f'SchCatalogComponent(name="{self.name}")'
