#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.cat_sch_platform_interfaces.sch_grr import SchGRR
from pycatia.cat_sch_platform_interfaces.sch_list_of_bst_rs import SchListOfBSTRs
from pycatia.cat_sch_platform_interfaces.sch_list_of_objects import SchListOfObjects
from pycatia.system_interfaces.any_object import AnyObject


class SchConnectable(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SchConnectable
                | 
                | Represents schematic objects that can be connected to others.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.sch_connectable = com_object

    def list_connectors(self, i_l_cntr_class_filter: SchListOfBSTRs, i_grr: SchGRR) -> SchListOfObjects:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func ListConnectors(SchListOfBSTRs iLCntrClassFilter,
                | SchGRR iGRR) As SchListOfObjects
                | 
                |     Find all the connectors of this schematic object on a specific graphical
                |     image.
                | 
                |     Parameters:
                | 
                |         oLCntrClassFilter
                |             A list of all the class types for filtering the output connector
                |             list. 
                |         iGRR
                |             Pointer to the graphical image 
                |         oLCntrs
                |             A list of connectors included in this connection. (members are
                |             CATISchAppConnector interface pointers). 
                | 
                |     Example:
                |
                |          Dim objThisIntf As SchConnectable
                |          Dim objArg1 As SchListOfBSTRs
                |          Dim objArg2 As SchGRR
                |          Dim objArg3 As SchListOfObjects
                |           ...
                |          Set objArg3 = objThisIntf.ListConnectors(objArg1,objArg2)

        :param SchListOfBSTRs i_l_cntr_class_filter:
        :param SchGRR i_grr:
        :rtype: SchListOfObjects
        """
        return SchListOfObjects(self.sch_connectable.ListConnectors(i_l_cntr_class_filter.com_object, i_grr.com_object))

    def __repr__(self):
        return f'SchConnectable(name="{self.name}")'
