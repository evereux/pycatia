#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.manufacturing_interfaces.manufacturing_insert import ManufacturingInsert
from pycatia.manufacturing_interfaces.manufacturing_tool import ManufacturingTool
from pycatia.system_interfaces.any_object import AnyObject


class ManufacturingToolAssembly2(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     ManufacturingToolAssembly2
                | 
                | Represents the tool assembly.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.manufacturing_tool_assembly2 = com_object

    @property
    def insert(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Insert(ManufacturingInsert iMfgInsert) (Write
                | Only)
                | 
                |     Set the insert of an assembly.
                | 
                |     Parameters:
                | 
                |         iMfgInsert
                |             The insert to set to tool assembly

        :rtype: None
        """

        return None

    @insert.setter
    def insert(self, value: ManufacturingInsert):
        """
        :param ManufacturingInsert value:
        """

        self.manufacturing_tool_assembly2.Insert = value.com_object

    @property
    def tool(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Tool(ManufacturingTool iMfgTool) (Write Only)
                | 
                |     Set the tool of an assembly.
                | 
                |     Parameters:
                | 
                |         iMfgTool
                |             The tool to set to tool assembly

        :rtype: None
        """

        return None

    @tool.setter
    def tool(self, value: ManufacturingTool):
        """
        :param False value:
        """

        self.manufacturing_tool_assembly2.Tool = value.com_object

    def __repr__(self):
        return f'ManufacturingToolAssembly2(name="{self.name}")'
