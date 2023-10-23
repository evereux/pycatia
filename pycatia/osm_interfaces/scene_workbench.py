#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.in_interfaces.workbench import Workbench
from pycatia.osm_interfaces.scenes import Scenes


class SceneWorkbench(Workbench):
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
                |                         SceneWorkbench
                | 
                | Represent the access point to scenes management.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.scene_workbench = com_object

    @property
    def work_scenes(self) -> Scenes:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property WorkScenes() As Scenes (Read Only)
                | 
                |     Returns the Scenes collection.
                | 
                |     Example:
                | 
                |               This example retrieves the WorkScenes collection of the active
                |               document.
                |
                |             Dim TheWorkSceneWorkbench As Workbench
                |             Set TheWorkSceneWorkbench = CATIA.ActiveDocument.GetWorkbench ( "SceneWorkbench" )
                |             Dim TheScenesList As WorkScenes
                |             Set TheScenesList = TheWorkSceneWorkbench.WorkScenes

        :rtype: Scenes
        """

        return Scenes(self.scene_workbench.WorkScenes)

    def __repr__(self):
        return f'SceneWorkbench(name="{self.name}")'
