#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.in_interfaces.workbench import Workbench
from pycatia.kinematics_interfaces.mechanisms import Mechanisms


class KinematicsWorkbench(Workbench):
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
                |                         KinematicsWorkbench
                | 
                | Interface to access all Kinematics entities.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.kinematics_workbench = com_object

    @property
    def mechanisms(self) -> Mechanisms:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Mechanisms() As Mechanisms (Read Only)
                | 
                |     Returns the Mechanisms collection.
                | 
                |     Returns:
                |         The Mechanisms collection 
                |     Example:
                |         This example retrieves the Mechanisms collection of the active
                |         document.
                | 
                |             Dim TheKinWorkbench As Workbench
                |             Set TheKinWorkbench = CATIA.ActiveDocument.GetWorkbench ( "KinematicsWorkbench" )
                |             Dim TheMechanismsList As Mechanisms
                |             Set TheMechanismsList = TheKinWorkbench.Mechanisms

        :rtype: Mechanisms
        """

        return Mechanisms(self.kinematics_workbench.Mechanisms)

    def __repr__(self):
        return f'KinematicsWorkbench(name="{self.name}")'
