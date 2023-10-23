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


class MountActivity(Activity):
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
                |                         MountActivity
                | 
                | Interface representing a Mount Activity.
                | 
                | Role: This interface is used to retieve/assign the value of motion
                | targets/attrs for the move activity.
                | The following code snippet can be used to obtain a MoveJointActivity from a
                | selected Activity
                | 
                |    Dim oSelectAct As Activity
                |    set oSelectAct = CATIA.ActiveDocument.Selection.FindObject("CATIAActivity")
                |    Dim objMountAct As MountActivity
                |    set objMountAct = oSelectAct.GetTechnologicalObject("MountActivity")
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.mount_activity = com_object

    @property
    def tool(self) -> AnyObject:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Tool() As AnyObject
                | 
                |     This property returns and sets the tool to mount.
                | 
                |     Returns:
                |         oTool The tool to mount. 
                |     Parameters:
                | 
                |         iTool
                |             The tool to mount. 
                | 
                |     Example:
                |
                |            Dim objMountAct As MountActivity
                |                   ......
                |            Dim  objTool As Product
                |            set objTool=objMountAct.Tool
                |            ..
                |            objMountAct.Tool=objTool

        :rtype: AnyObject
        """

        return AnyObject(self.mount_activity.Tool)

    @tool.setter
    def tool(self, value: AnyObject):
        """
        :param AnyObject value:
        """

        self.mount_activity.Tool = value

    @property
    def tool_profile(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ToolProfile() As CATBSTR
                | 
                |     Sets and Retreives Tool Profile to use after mounting
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
                |            Dim objMountAct As MountActivity
                |                   ......
                |            Dim  ToolPrName As String
                |            set ToolPrName=objMountAct.ToolProfile
                |            ToolPrName  = "Tool.1"
                |            objMountAct.ToolProfile=ToolPrName

        :rtype: str
        """

        return self.mount_activity.ToolProfile

    @tool_profile.setter
    def tool_profile(self, value: str):
        """
        :param str value:
        """

        self.mount_activity.ToolProfile = value

    def __repr__(self):
        return f'MountActivity(name="{self.name}")'
