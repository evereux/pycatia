#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.dmaps_interfaces.activity import Activity
from pycatia.system_interfaces.any_object import AnyObject


class UnmountActivity(Activity):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     DMAPSInterfaces.Activity
                |                         UnmountActivity
                | 
                | Interface representing a Unmount Activity.
                | 
                | Role: This interface is used to retieve/assign the value of motion
                | targets/attrs for the move activity.
                | The following code snippet can be used to obtain a MoveJointActivity from a
                | selected Activity
                | 
                |    Dim oSelectAct As Activity
                |    set oSelectAct = CATIA.ActiveDocument.Selection.FindObject("CATIAActivity")
                |    Dim objUnmountAct As UnmountActivity
                |    set objUnmountAct = oSelectAct.GetTechnologicalObject("UnmountActivity")
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.unmount_activity = com_object

    @property
    def tool(self) -> AnyObject:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Tool() As AnyObject
                | 
                |     This property returns and sets the tool to Unmount.
                | 
                |     Returns:
                |         oTool The tool to Unmount. 
                |     Parameters:
                | 
                |         iTool
                |             The tool to Unmount. 
                | 
                |     Example:
                |
                |            Dim objUnmountAct As UnmountActivity
                |                   ......
                |            Dim  objTool As Product
                |            set objTool=objUnmountAct.Tool
                |            ..
                |            objUnmountAct.Tool=objTool

        :rtype: AnyObject
        """

        return AnyObject(self.unmount_activity.Tool)

    @tool.setter
    def tool(self, value: AnyObject):
        """
        :param AnyObject value:
        """

        self.unmount_activity.Tool = value

    @property
    def tool_profile(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ToolProfile() As CATBSTR
                | 
                |     Sets and Retreives Tool Profile to use after Unmounting
                | 
                |     Returns:
                |         oToolProfile Name of the tool profile available in the Generic Robot
                |         Controller set. 
                |     Parameters:
                | 
                |         iToolProfile
                |             Name of the tool profile available in the Generic Robot Controller
                |             to set. 
                | 
                |     Example:
                |
                |            Dim objUnmountAct As UnmountActivity
                |                   ......
                |            Dim  ToolPrName As String
                |            set ToolPrName=objUnmountAct.ToolProfile
                |            ToolPrName  = "Tool.1"
                |            objUnmountAct.ToolProfile=ToolPrName

        :rtype: str
        """

        return self.unmount_activity.ToolProfile

    @tool_profile.setter
    def tool_profile(self, value: str):
        """
        :param str value:
        """

        self.unmount_activity.ToolProfile = value

    def __repr__(self):
        return f'UnmountActivity(name="{self.name}")'
