#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.cat_sch_platform_interfaces.sch_component import SchComponent
from pycatia.cat_sch_platform_interfaces.sch_grr_comp import SchGRRComp
from pycatia.system_interfaces.any_object import AnyObject


class SchReplace(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SchReplace
                | 
                | Manage existing schematic component instances.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.sch_replace = com_object

    def replace(self, i_grr_to_be_placed: SchGRRComp, i_sch_comp_to_be_removed: SchComponent) -> SchComponent:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func Replace(SchGRRComp iGRRToBePlaced,
                | SchComponent iSchCompToBeRemoved) As SchComponent
                | 
                |     Replace an existing component with this component.
                | 
                |     Parameters:
                | 
                |         iGRRToBePlaced
                |             Pointer to the component graphical representation of this component
                |             to be placed. if NULL the first representation found will be used.
                |             
                |         iSchCompToBeRemoved
                |             Pointer to the existing component to be replaced by this component.
                |             
                |         oNewComponent
                |             Interface pointer to the new component instance placed.
                |
                |     Example:
                |
                |          Dim objThisIntf As SchReplace
                |          Dim objArg1 As SchGRRComp
                |          Dim objArg2 As SchComponent
                |          Dim objArg3 As SchComponent
                |           ...
                |          Set objArg3 = objThisIntf.Replace(objArg1,objArg2)

        :param SchGRRComp i_grr_to_be_placed:
        :param SchComponent i_sch_comp_to_be_removed:
        :rtype: SchComponent
        """
        return SchComponent(
            self.sch_replace.Replace(
                i_grr_to_be_placed.com_object,
                i_sch_comp_to_be_removed.com_object
            )
        )

    def __repr__(self):
        return f'SchReplace(name="{self.name}")'
