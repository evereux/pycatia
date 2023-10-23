#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.in_interfaces.workbench import Workbench
from pycatia.system_interfaces.any_object import AnyObject


class SchWorkbench(Workbench):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     InfInterfaces.Workbench
                |                         SchWorkbench
                | 
                | Represents a workbench on a schematic document.
                | Role:A workbench is a set of commands that can be used to create, modify and
                | edit the objects making up the document.
                | 
                | See also:
                |     Document
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.sch_workbench = com_object

    def find_interface(self, i_interface_name: str, i_object: AnyObject) -> AnyObject:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func FindInterface(CATBSTR iInterfaceName,
                | CATBaseDispatch iObject) As CATBaseDispatch
                | 
                |     This method returns an interface handle to an object.
                | 
                |     Parameters:
                | 
                |         iInterfaceName
                |             interface name to search for ("CATIAxxxx") 
                |         iObject
                |             The object to search for the required interface. 
                |         oInterfaceFound
                |             interface handle found 
                | 
                |     Example:
                | 
                |           The following example retrieves a CATIAInterfaceNameToFind handle to
                |           the
                |          CATIAxxxx_iObject in interfaceFound using the Schematics workbench
                |          object
                |          schWorkbench.
                |
                |          Dim interfaceFound As AnyObject
                |          Set interfaceFound = CATIASchWorkbench.FindInterface("InterfaceNameToFind",CATIAProduct_iObject)

        :param str i_interface_name:
        :param AnyObject i_object:
        :rtype: AnyObject
        """
        return self.sch_workbench.FindInterface(i_interface_name, i_object.com_object)

    def __repr__(self):
        return f'SchWorkbench(name="{self.name}")'
