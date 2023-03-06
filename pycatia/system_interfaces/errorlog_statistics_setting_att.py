#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-09 09:53:18.676780

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.general_statistics_setting_att import GeneralStatisticsSettingAtt


class ErrorlogStatisticsSettingAtt(GeneralStatisticsSettingAtt):

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
                |                             ErrorlogStatisticsSettingAtt
                | 
                | Interface for Errorlog statistic Controller.
                | 
                | Role: the errorlog statistics controller manages the values of all or only a
                | part of the attributes available for the thematic.
                | For the definitions of methods and variables common to every thematic, see the
                | GeneralStatisticsSettingAtt
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.errorlog_statistics_setting_att = com_object

    @property
    def abnd(self):
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property ABND() As boolean
                | 
                |     Returns or sets the state ot the abend severity level
                |     field.
                |     Role: Returns or sets the state ot the abend severity level
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

        return self.errorlog_statistics_setting_att.ABND

    @abnd.setter
    def abnd(self, value):
        """
        :param bool value:
        """

        self.errorlog_statistics_setting_att.ABND = value

    @property
    def cerr(self):
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property CERR() As boolean
                | 
                |     Returns or sets the state ot the critical error severity level
                |     field.
                |     Role: Returns or sets the state ot the critical error severity level
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

        return self.errorlog_statistics_setting_att.CERR

    @cerr.setter
    def cerr(self, value):
        """
        :param bool value:
        """

        self.errorlog_statistics_setting_att.CERR = value

    @property
    def cmnd(self):
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property CMND() As boolean
                | 
                |     Returns or sets the state ot the command name field.
                |     Role: Returns or sets the state ot the command name field.
                | 
                |     Parameters:
                | 
                |         oStatus
                |             Legal values:
                |             TRUE : the field is activated
                |             FALSE: the field is not activated

        :return: bool
        """

        return self.errorlog_statistics_setting_att.CMND

    @cmnd.setter
    def cmnd(self, value):
        """
        :param bool value:
        """

        self.errorlog_statistics_setting_att.CMND = value

    @property
    def comt(self):
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property COMT() As boolean
                | 
                |     Returns or sets the state ot the abend comment level
                |     field.
                |     Role: Returns or sets the state ot the comment severity level
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

        return self.errorlog_statistics_setting_att.COMT

    @comt.setter
    def comt(self, value):
        """
        :param bool value:
        """

        self.errorlog_statistics_setting_att.COMT = value

    @property
    def msge(self):
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property MSGE() As boolean
                | 
                |     Returns or sets the state ot the message field.
                |     Role: Returns or sets the state ot the message field.
                | 
                |     Parameters:
                | 
                |         oStatus
                |             Legal values:
                |             TRUE : the field is activated
                |             FALSE: the field is not activated

        :return: bool
        """

        return self.errorlog_statistics_setting_att.MSGE

    @msge.setter
    def msge(self, value):
        """
        :param bool value:
        """

        self.errorlog_statistics_setting_att.MSGE = value

    @property
    def urep(self):
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property UREP() As boolean
                | 
                |     Returns or sets the state ot the user report severity level
                |     field.
                |     Role: Returns or sets the state ot the user report severity level
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

        return self.errorlog_statistics_setting_att.UREP

    @urep.setter
    def urep(self, value):
        """
        :param bool value:
        """

        self.errorlog_statistics_setting_att.UREP = value

    @property
    def warn(self):
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property WARN() As boolean
                | 
                |     Returns or sets the state ot the warning severity level
                |     field.
                |     Role: Returns or sets the state ot the warning severity level
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

        return self.errorlog_statistics_setting_att.WARN

    @warn.setter
    def warn(self, value):
        """
        :param bool value:
        """

        self.errorlog_statistics_setting_att.WARN = value

    @property
    def wkbn(self):
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property WKBN() As boolean
                | 
                |     Returns or sets the state ot the workbench name field.
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

        return self.errorlog_statistics_setting_att.WKBN

    @wkbn.setter
    def wkbn(self, value):
        """
        :param bool value:
        """

        self.errorlog_statistics_setting_att.WKBN = value

    def __repr__(self):
        return f'ErrorlogStatisticsSettingAtt(name="{ self.name }")'
