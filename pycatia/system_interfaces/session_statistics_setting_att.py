#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-09 09:53:18.676780

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.general_statistics_setting_att import GeneralStatisticsSettingAtt


class SessionStatisticsSettingAtt(GeneralStatisticsSettingAtt):

    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     System.SettingController
                |                         System.GeneralStatisticsSettingAtt
                |                             SessionStatisticsSettingAtt
                | 
                | Interface for Session statistic Controller
                | Role: the session statistics controller manages the values of all or only a part
                | of the attributes available for the thematic.
                | 
                | For the definitions of methods and variables common to every thematic, see the
                | GeneralStatisticsSettingAtt
                | 
                | Copyright © 1999-2011, Dassault Systèmes. All rights reserved.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.session_statistics_setting_att = com_object

    def __repr__(self):
        return f'SessionStatisticsSettingAtt(name="{ self.name }")'
