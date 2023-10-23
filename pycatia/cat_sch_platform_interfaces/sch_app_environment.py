#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.any_object import AnyObject


class SchAppEnvironment(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SchAppEnvironment
                | 
                | Manage the application environment in a schematic session.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.sch_app_environment = com_object

    def app_clean_up_when_application_ends(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub AppCleanUpWhenApplicationEnds()
                | 
                |     Initialize environment when schematic application ends.
                | 
                |     Example:
                | 
                |           
                | 
                |          Dim objThisIntf As SchAppEnvironment
                |           ...
                |          objThisIntf.AppCleanUpWhenApplicationEnds

        :rtype: None
        """
        return self.sch_app_environment.AppCleanUpWhenApplicationEnds()

    def app_init_when_application_starts(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub AppInitWhenApplicationStarts()
                | 
                |     Initialize environment when schematic application starts.
                | 
                |     Example:
                | 
                |           
                | 
                |          Dim objThisIntf As SchAppEnvironment
                |           ...
                |          objThisIntf.AppInitWhenApplicationStarts

        :rtype: None
        """
        return self.sch_app_environment.AppInitWhenApplicationStarts()

    def app_load_feat_files(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub AppLoadFeatFiles()
                | 
                |     Load all the necessary feat files.
                | 
                |     Example:
                | 
                |           
                | 
                |          Dim objThisIntf As SchAppEnvironment
                |           ...
                |          objThisIntf.AppLoadFeatFiles

        :rtype: None
        """
        return self.sch_app_environment.AppLoadFeatFiles()

    def __repr__(self):
        return f'SchAppEnvironment(name="{self.name}")'
