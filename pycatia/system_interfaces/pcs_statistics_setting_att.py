#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-09 09:53:18.676780

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.general_statistics_setting_att import GeneralStatisticsSettingAtt


class PcsStatisticsSettingAtt(GeneralStatisticsSettingAtt):

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
                |                             PCSStatisticsSettingAtt
                | 
                | Interface for PCS statistic Controller
                | Role: the PCS statistics controller manages the values of all or only a part of
                | the attributes available for the thematic.
                | 
                | For the definitions of methods and variables common to every thematic, see the
                | GeneralStatisticsSettingAtt
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.pcs_statistics_setting_att = com_object

    @property
    def mem_use(self):
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property MemUse() As boolean
                | 
                |     Returns or sets the state ot the memory field.
                |     Role: Returns or sets the state ot the workbench name
                |     field.
                | 
                |     Parameters:
                | 
                |         oStatus
                |             Legal values:
                |             TRUE : the field is activated
                |             FALSE: the field is not activated

        :return: bool
        """

        return self.pcs_statistics_setting_att.MemUse

    @mem_use.setter
    def mem_use(self, value):
        """
        :param bool value:
        """

        self.pcs_statistics_setting_att.MemUse = value

    def __repr__(self):
        return f'PcsStatisticsSettingAtt(name="{ self.name }")'
