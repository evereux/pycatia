#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.dnb_human_sim_interfaces.walk_activity import WalkActivity


class CollisionFreeWalk(WalkActivity):
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
                |                         DNBHumanSimInterfaces.WorkerActivity
                |                             DNBHumanSimInterfaces.WalkActivity
                |                                 CollisionFreeWalk
                | 
                | Interface representing Collision free walk activity
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.collision_free_walk = com_object

    @property
    def collision_clearance(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property CollisionClearance() As double
                | 
                |     Returns and sets the value for 'collision clearance' in a collision free
                |     walk.
                |     Role: Returns and sets the value of 'colllision clearance' from a collision
                |     free walk Activity
                | 
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on failure

        :rtype: float
        """

        return self.collision_free_walk.CollisionClearance

    @collision_clearance.setter
    def collision_clearance(self, value: float):
        """
        :param float value:
        """

        self.collision_free_walk.CollisionClearance = value

    @property
    def search_intensity(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property SearchIntensity() As HTSSearchIntensity
                | 
                |     Returns and sets the value for 'Search Intensity' in a collision free walk.
                |     Refer DNBIAHumanSimDefs for setting the HTSSearchIntensity option
                |     Role: Returns and sets the value of 'Search Intensity' from a collision
                |     free walk Activity
                | 
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on failure

        :return: enum hts_search_intensity
        :rtype: int
        """

        return self.collision_free_walk.SearchIntensity

    @search_intensity.setter
    def search_intensity(self, value: int):
        """
        :param int value: enum hts_search_intensity
        """

        self.collision_free_walk.SearchIntensity = value

    def __repr__(self):
        return f'CollisionFreeWalk(name="{self.name}")'
