#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.dnb_human_modeling_interfaces.swk_manikin_part import SWKManikinPart


class SWKDOF(SWKManikinPart):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     DNBHumanModelingInterfaces.SWKManikinPart
                |                         SWKDOF
                | 
                | This interface deals with a degree of freedom (DOF) of a
                | manikin.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.swkdof = com_object

    @property
    def default_value(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property DefaultValue() As double (Read Only)
                | 
                |     Returns the default value of a DOF. The value read is always in radians.

        :rtype: float
        """

        return self.swkdof.DefaultValue

    @property
    def full_name(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property FullName() As CATBSTR (Read Only)
                | 
                |     Returns the full name of the degree of freedom (e.g.
                |     "flexion/extension").
                |     This property is different from the property Name of
                |     AnyObject, which gives the short name or abbreviated name
                |     of the DOF (e.g. "DOF1").

        :rtype: str
        """

        return self.swkdof.FullName

    @property
    def limits_locked(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property LimitsLocked() As boolean
                | 
                |     Sets a lock on the limits.
                |     When the value of this property is TRUE, the DOF travel limits are locked,
                |     therefore the min and max values cannot be changed.
                |     When the value is FALSE, the DOF limits are unlocked and can be changed. By
                |     default, the DOF limits are locked and the application must unlock these limits
                |     before changing them.

        :rtype: bool
        """

        return self.swkdof.LimitsLocked

    @limits_locked.setter
    def limits_locked(self, value: bool):
        """
        :param bool value:
        """

        self.swkdof.LimitsLocked = value

    @property
    def max_mean(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property MaxMean() As double (Read Only)
                | 
                |     Returns the mean value of the upper limit of the DOF (in
                |     radians).

        :rtype: float
        """

        return self.swkdof.MaxMean

    @property
    def max_mean_inter_segment(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property MaxMeanInterSegment() As double (Read Only)

        :rtype: float
        """

        return self.swkdof.MaxMeanInterSegment

    @property
    def max_score(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property MaxScore() As double (Read Only)
                | 
                |     Returns the highest score that this DOF can take.

        :rtype: float
        """

        return self.swkdof.MaxScore

    @property
    def max_std_dev(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property MaxStdDev() As double (Read Only)
                | 
                |     Returns the standard deviation value of the upper limit of the DOF (in
                |     radians).

        :rtype: float
        """

        return self.swkdof.MaxStdDev

    @property
    def max_value(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property MaxValue() As double
                | 
                |     Returns or sets the highest value that a DOF can take.
                |     When setting the value, the new value given
                |     cannot be higher than the statistical value found
                |     in the limits database. This statistical maximum
                |     value can be obtained by a call to property
                |     StatisticalMaxValue.

        :rtype: float
        """

        return self.swkdof.MaxValue

    @max_value.setter
    def max_value(self, value: float):
        """
        :param float value:
        """

        self.swkdof.MaxValue = value

    @property
    def max_value_as_percentile(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property MaxValueAsPercentile() As double
                | 
                |     Returns or sets the highest value that a DOF can take.
                |     When reading the value, the number returned
                |     will take a percentile format, that is, will
                |     be between 0.0 and 100.0 inclusive.
                | 
                |     When setting the value, the new value given
                |     must also lie in the range [ 0.0 ; 100.0 ].

        :rtype: float
        """

        return self.swkdof.MaxValueAsPercentile

    @max_value_as_percentile.setter
    def max_value_as_percentile(self, value: float):
        """
        :param float value:
        """

        self.swkdof.MaxValueAsPercentile = value

    @property
    def min_mean(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property MinMean() As double (Read Only)
                | 
                |     Returns the mean value of the lower limit of the DOF (in
                |     radians).

        :rtype: float
        """

        return self.swkdof.MinMean

    @property
    def min_mean_inter_segment(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property MinMeanInterSegment() As double (Read Only)

        :rtype: float
        """

        return self.swkdof.MinMeanInterSegment

    @property
    def min_std_dev(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property MinStdDev() As double (Read Only)
                | 
                |     Returns the standard deviation value of the lower limit of
                |     the DOF (in radians).

        :rtype: float
        """

        return self.swkdof.MinStdDev

    @property
    def min_value(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property MinValue() As double
                | 
                |     Returns or sets the lowest value that a DOF can take.
                |     When setting the value, the new value given
                |     cannot be lower than the statistical value found
                |     in the limits database. This statistical minimum
                |     value can be obtained by a call to property
                |     StatisticalMinValue.

        :rtype: float
        """

        return self.swkdof.MinValue

    @min_value.setter
    def min_value(self, value: float):
        """
        :param float value:
        """

        self.swkdof.MinValue = value

    @property
    def min_value_as_percentile(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property MinValueAsPercentile() As double
                | 
                |     Returns or sets the lowest value that a DOF can take.
                |     When reading the value, the number returned
                |     will take a percentile format, that is, will
                |     be between 0.0 and 100.0 exclusive.
                | 
                |     When setting the value, the new value given
                |     must also lie in the range [ 0.0 ; 100.0 ].

        :rtype: float
        """

        return self.swkdof.MinValueAsPercentile

    @min_value_as_percentile.setter
    def min_value_as_percentile(self, value: float):
        """
        :param float value:
        """

        self.swkdof.MinValueAsPercentile = value

    @property
    def min_value_inter_segment(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property MinValueInterSegment() As double (Read Only)

        :rtype: float
        """

        return self.swkdof.MinValueInterSegment

    @property
    def number(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Number() As long (Read Only)
                | 
                |     Returns the number of the DOF. This number is an integer between 0 and
                |     2.
                | 
                |     See also:
                |         SWKSegment

        :rtype: int
        """

        return self.swkdof.Number

    @property
    def score(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Score() As double (Read Only)
                | 
                |     Returns the score corresponding to the DOF's current value.

        :rtype: float
        """

        return self.swkdof.Score

    @property
    def value(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Value() As double
                | 
                |     Returns or sets the value of a DOF.
                |     The value read or set is always in radians.

        :rtype: float
        """

        return self.swkdof.Value

    @value.setter
    def value(self, value: float):
        """
        :param float value:
        """

        self.swkdof.Value = value

    @property
    def value_as_string(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ValueAsString() As CATBSTR
                | 
                |     Returns or sets the value of a DOF, as a string.
                | 
                |     Example:
                | 
                |           myManikin.Body.GetSegment("LSLeTh").
                |          ValueAsString = "10deg"

        :rtype: str
        """

        return self.swkdof.ValueAsString

    @value_as_string.setter
    def value_as_string(self, value: str):
        """
        :param str value:
        """

        self.swkdof.ValueAsString = value

    @property
    def value_locked(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ValueLocked() As boolean
                | 
                |     Sets a lock on the value.
                |     When the value of this property is TRUE, the DOF's current value is locked
                |     and cannot be changed.
                |     When this property is set to FALSE, the DOF value is unlocked and can be
                |     changed again. Locking a value on a DOF means that this DOF will ne take any
                |     other value than the current one, and will not be changed by an inverse
                |     kinematics resolution, for instance.

        :rtype: bool
        """

        return self.swkdof.ValueLocked

    @value_locked.setter
    def value_locked(self, value: bool):
        """
        :param bool value:
        """

        self.swkdof.ValueLocked = value

    def reset_value(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub ResetValue()
                | 
                |     Sets the value of the DOF to its default value.

        :rtype: None
        """
        return self.swkdof.ResetValue()

    def set_limits_to_match_best_pref_angle(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetLimitsToMatchBestPrefAngle()
                | 
                |     Set the angular limitations to match with the best pref angle. The purpose
                |     of this method is to set the angular limitations of this DOF so that these
                |     limitations correspond to the best range of motion, that is, the range of
                |     motion where the postural score is the highest.
                | 
                |     This method travels the different preferred angles on the DOF, then chooses
                |     the one with the highest score. If several preferred angles are found with the
                |     highest score, then the last one with the highest score is
                |     taken.
                | 
                |     If no preferred angles have been defined on this DOF, then the angular
                |     limitations are not modified.

        :rtype: None
        """
        return self.swkdof.SetLimitsToMatchBestPrefAngle()

    def __repr__(self):
        return f'SWKdof(name="{self.name}")'
