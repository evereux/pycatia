#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.any_object import AnyObject


class AsySimActivity(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     AsySimActivity
                | 
                | Interface for a Delmia Simulation Activity.
                | Currently the main focus is to synchronize an activity with the simulation
                | world.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.asy_sim_activity = com_object

    def synchronize(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub Synchronize()
                | 
                |     Updates the simulation world up to this activity.
                |     Role: Updates the simulation world (and its contents) to the end of the
                |     specified activity. Please note that no animation will occur, and the execution
                |     will wait for the simulation to finish before this method is complete.

        :rtype: None
        """
        return self.asy_sim_activity.Synchronize()

    def __repr__(self):
        return f'AsySimActivity(name="{self.name}")'
