#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.abq_automation_interfaces.abq_output_request import ABQOutputRequest


class ABQFHOutputRequest(ABQOutputRequest):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     ABQAutomationItf.ABQOutputRequest
                |                         ABQFHOutputRequest
                | 
                | Represents the base interface for field and history output request
                | objects.
                | Role: The ABQFHOutputRequest interface manages the common properties of field
                | and history output requests.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.abqfh_output_request = com_object

    @property
    def equally_spaced_incr(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property EquallySpacedIncr(long iAtEquallySpacedIncr) (Write
                | Only)
                | 
                |     For explicit dynamic step: Sets request for output results at equally
                |     spaced increments.
                | 
                |     Parameters:
                | 
                |         iAtEquallySpacedIncr
                |             The increment number which allows the user to set output results at
                |             this interval

        :rtype: int
        """

        return self.abqfh_output_request.EquallySpacedIncr

    @equally_spaced_incr.setter
    def equally_spaced_incr(self, value: int):
        """
        :param int value:
        """

        self.abqfh_output_request.EquallySpacedIncr = value

    @property
    def every_x_incr_of_time(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property EveryXIncrOfTime(double iAtEveryXIncr) (Write
                | Only)
                | 
                |     For explicit dynamic step: Sets request for output results at every
                |     specified units of time.
                | 
                |     Parameters:
                | 
                |         iAtEveryXIncr
                |             The time interval which allows the user to set output results at
                |             this interval

        :rtype: int
        """

        return self.abqfh_output_request.EveryXIncrOfTime

    @every_x_incr_of_time.setter
    def every_x_incr_of_time(self, value: int):
        """
        :param int value:
        """

        self.abqfh_output_request.EveryXIncrOfTime = value

    @property
    def output_at_def_or_all_sec_pts(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property OutputAtDefOrAllSecPts(ABQOutputAtSecPts iOutputAtSecPts) (Write
                | Only)
                | 
                |     Sets request for output results at section points.
                | 
                |     Parameters:
                | 
                |         iOutputAtSecPts
                |             The option to request output results at section points: Default or
                |             All
                | 
                |             Legal values:
                | 
                |             "ABQDEFAULTSECPTS"
                |             "ABQALLSECPTS"

        :return: enum abq_output_at_sec_pts
        :rtype: int
        """

        return self.abqfh_output_request.OutputAtDefOrAllSecPts

    @output_at_def_or_all_sec_pts.setter
    def output_at_def_or_all_sec_pts(self, value: int):
        """
        :param int value:
        """

        self.abqfh_output_request.OutputAtDefOrAllSecPts = int

    @property
    def pre_select_default_or_all(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property PreSelectDefaultOrAll(ABQOutputVariableType iOutputVarType) (Write
                | Only)
                | 
                |     Sets request for results for preselect default or ALL
                |     variables.
                | 
                |     Parameters:
                | 
                |         iOutputVarType
                |             The option to request output results for set of variables:
                |             Preselected or All
                | 
                |             Legal values:
                | 
                |             "ABQPRESELECTDEFVAR"
                |             "ABQALLVAR"

        :return: enum abq_output_variable_type
        :rtype: int
        """

        return self.abqfh_output_request.PreSelectDefaultOrAll

    @pre_select_default_or_all.setter
    def pre_select_default_or_all(self, value: int):
        """
        :param int value:
        """

        self.abqfh_output_request.PreSelectDefaultOrAll = value

    @property
    def specified_modes(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property SpecifiedModes(CATSafeArrayVariant iSpecifiedModes) (Write
                | Only)
                | 
                |     For frequency step: Sets request for output results at specified
                |     modes.
                | 
                |     Parameters:
                | 
                |         iSpecifiedModes
                |             The list of modes for which output is requested

        :rtype: int
        """

        return self.abqfh_output_request.SpecifiedModes

    @specified_modes.setter
    def specified_modes(self, value: int):
        """
        :param int value:
        """

        self.abqfh_output_request.SpecifiedModes = value

    @property
    def specified_output_variables(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property SpecifiedOutputVariables(CATBSTR iVariableNameBSTR) (Write
                | Only)
                | 
                |     Sets the specified variables for which results are
                |     requested.
                | 
                |     Parameters:
                | 
                |         iVariableNameBSTR
                |             The list of variables for which output is requested For example: If
                |             user wants to request output for variables 'U' and 'S', then iVariableNameBSTR
                |             will be "U, S"

        :rtype: int
        """

        return self.abqfh_output_request.SpecifiedOutputVariables

    @specified_output_variables.setter
    def specified_output_variables(self, value: int):
        """
        :param int value:
        """

        self.abqfh_output_request.SpecifiedOutputVariables = value

    @property
    def specified_sec_pts(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property SpecifiedSecPts(CATSafeArrayVariant iSpecifiedSecPts) (Write
                | Only)
                | 
                |     Sets request for output results at specified section
                |     points.
                | 
                |     Parameters:
                | 
                |         iSpecifiedSecPts
                |             The list of section points at which output is
                |             requested

        :rtype: int
        """

        return self.abqfh_output_request.SpecifiedSecPts

    @specified_sec_pts.setter
    def specified_sec_pts(self, value: int):
        """
        :param int value:
        """

        self.abqfh_output_request.SpecifiedSecPts = value

    @property
    def timing_flag(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property TimingFlag() As boolean
                | 
                |     Returns or sets a flag for output at approximate or exact times. A true
                |     value indicates that request for output results at approximate times and a
                |     false value for output results at exact times.
                | 
                |     Returns:
                |         A boolean specifying whether request for output results at approximate
                |         or exact times.

        :rtype: bool
        """

        return self.abqfh_output_request.TimingFlag

    @timing_flag.setter
    def timing_flag(self, value: bool):
        """
        :param bool value:
        """

        self.abqfh_output_request.TimingFlag = value

    def set_output_at_all_modes(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetOutputAtAllModes()
                | 
                |     For frequency step: Sets request for output results at all modes.

        :rtype: None
        """
        return self.abqfh_output_request.SetOutputAtAllModes()

    def __repr__(self):
        return f'ABQFHOutputRequest(name="{self.name}")'
