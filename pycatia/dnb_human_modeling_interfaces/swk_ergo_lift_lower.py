#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.any_object import AnyObject


class SWKErgoLiftLower(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SWKErgoLiftLower
                | 
                | This interface deals the lift/lower ergonomic analysis.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.swk_ergo_lift_lower = com_object

    @property
    def coupling(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Coupling() As CATBSTR
                | 
                |     Returns or sets the coupling condition for the lift/lower
                |     analysis.
                |     The value of the parameter must be either "Good", "Fair", or
                |     "Poor".
                | 
                |     N.B.: This coupling condition must be set before
                |     attempting
                |     to retrive any output value from the study, if the input gudeline
                |     is "NIOSH1991". Failure to do so will result in invalid output
                |     values.

        :rtype: str
        """

        return self.swk_ergo_lift_lower.Coupling

    @coupling.setter
    def coupling(self, value: str):
        """
        :param str value:
        """

        self.swk_ergo_lift_lower.Coupling = value

    @property
    def duration(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Duration() As double
                | 
                |     Returns or sets the lift duration.
                |     This frequency must be expressed in hours per day, cannot be greater
                |     than 8.0 and must be specified before attempting to retrive any output
                |     value from the study.
                |     Failure to do so will result in invalid output values.

        :rtype: float
        """

        return self.swk_ergo_lift_lower.Duration

    @duration.setter
    def duration(self, value: float):
        """
        :param float value:
        """

        self.swk_ergo_lift_lower.Duration = value

    @property
    def frequency(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Frequency() As double
                | 
                |     Returns or sets the lift frequecy.
                |     This frequency must be expressed in lifts per second, and must
                |     be specified before attempting to retrive any output value from the
                |     study.
                |     Failure to do so will result in invalid output values.

        :rtype: float
        """

        return self.swk_ergo_lift_lower.Frequency

    @frequency.setter
    def frequency(self, value: float):
        """
        :param float value:
        """

        self.swk_ergo_lift_lower.Frequency = value

    @property
    def guide_line(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property GuideLine() As CATBSTR
                | 
                |     Returns or sets the guideline for the lift/lower analysis.
                |     The value of the parameter must be either "NIOSH1981", "NIOSH1991", or
                |     "SnookCiriello1991".
                | 
                |     N.B.: This guideline must be set before attempting
                |     to retrive any output value from the study, otherwise these outputs
                |     will have invalid values.

        :rtype: str
        """

        return self.swk_ergo_lift_lower.GuideLine

    @guide_line.setter
    def guide_line(self, value: str):
        """
        :param str value:
        """

        self.swk_ergo_lift_lower.GuideLine = value

    @property
    def niosh_action_limit(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property NIOSH_ActionLimit() As CATBSTR (Read Only)
                | 
                |     This field is set to a valid value for the NIOSH 1981 analysis only.
                |     It is the weight below which the task could be considered reasonably
                |     safe.

        :rtype: str
        """

        return self.swk_ergo_lift_lower.NIOSH_ActionLimit

    @property
    def niosh_angle_of_asymmetry_final(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property NIOSH_AngleOfAsymmetryFinal() As CATBSTR (Read
                | Only)
                | 
                |     This field is set to a valid value for the NIOSH 1991 analysis
                |     only.
                |     This value provides the angular measure of how far the object is displaced
                |     from the front (mid-sagital plane) of the worker's body at the ending of the
                |     lift, in in the current V5 units.
                |     This property gives the asymmetry angle at the destination
                |     (i.e., given the final posture of the manikin).

        :rtype: str
        """

        return self.swk_ergo_lift_lower.NIOSH_AngleOfAsymmetryFinal

    @property
    def niosh_angle_of_asymmetry_initial(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property NIOSH_AngleOfAsymmetryInitial() As CATBSTR (Read
                | Only)
                | 
                |     This field is set to a valid value for the NIOSH 1991 analysis
                |     only.
                |     This value provides the angular measure of how far the object is displaced
                |     from the front (mid-sagital plane) of the worker's body at the beginning of the
                |     lift, in in the current V5 units.
                |     This property gives the asymmetry angle at the origin
                |     (i.e., given the initial posture of the manikin).

        :rtype: str
        """

        return self.swk_ergo_lift_lower.NIOSH_AngleOfAsymmetryInitial

    @property
    def niosh_asymmetric_multiplier_final(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property NIOSH_AsymmetricMultiplierFinal() As CATBSTR (Read
                | Only)
                | 
                |     This field is set to a valid value for the NIOSH 1991 analysis
                |     only.
                |     This value provides the asymmetric multiplier.
                |     This property gives the asymmetric multiplier at the
                |     destination
                |     (i.e., given the final posture of the manikin).

        :rtype: str
        """

        return self.swk_ergo_lift_lower.NIOSH_AsymmetricMultiplierFinal

    @property
    def niosh_asymmetric_multiplier_initial(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property NIOSH_AsymmetricMultiplierInitial() As CATBSTR (Read
                | Only)
                | 
                |     This field is set to a valid value for the NIOSH 1991 analysis
                |     only.
                |     This value provides the asymmetric multiplier.
                |     This property gives the asymmetric multiplier at the
                |     origin
                |     (i.e., given the initial posture of the manikin).

        :rtype: str
        """

        return self.swk_ergo_lift_lower.NIOSH_AsymmetricMultiplierInitial

    @property
    def niosh_coupling_multiplier_final(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property NIOSH_CouplingMultiplierFinal() As CATBSTR (Read
                | Only)
                | 
                |     This field is set to a valid value for the NIOSH 1991 analysis
                |     only.
                |     This value provides the coupling multiplier bases ont hte coupling
                |     classification and vertical location of the lift (V).
                |     This property gives the coupling multiplier at the
                |     destination
                |     (i.e., given the final

        :rtype: str
        """

        return self.swk_ergo_lift_lower.NIOSH_CouplingMultiplierFinal

    @property
    def niosh_coupling_multiplier_initial(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property NIOSH_CouplingMultiplierInitial() As CATBSTR (Read
                | Only)
                | 
                |     This field is set to a valid value for the NIOSH 1991 analysis
                |     only.
                |     This value provides the coupling multiplier bases ont hte coupling
                |     classification and vertical location of the lift (V).
                |     This property gives the coupling multiplier at the origin
                |     (i.e., given the initial posture of the manikin).

        :rtype: str
        """

        return self.swk_ergo_lift_lower.NIOSH_CouplingMultiplierInitial

    @property
    def niosh_distance_multiplier(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property NIOSH_DistanceMultiplier() As CATBSTR (Read Only)
                | 
                |     This field is set to a valid value for the NIOSH 1991 analysis
                |     only.
                |     This value provides the distance multiplier.
                |     This property gives the distance multiplier.

        :rtype: str
        """

        return self.swk_ergo_lift_lower.NIOSH_DistanceMultiplier

    @property
    def niosh_frequency_multiplier(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property NIOSH_FrequencyMultiplier() As CATBSTR (Read Only)
                | 
                |     This field is set to a valid value for the NIOSH 1991 analysis
                |     only.
                |     This value provides the frequency depending upon the average of lifts/min
                |     (F), the vertical location (V) of the hand at the origin, and the duration of
                |     continuous lifting.
                |     This property gives the frequency multiplier.

        :rtype: str
        """

        return self.swk_ergo_lift_lower.NIOSH_FrequencyMultiplier

    @property
    def niosh_horizontal_location_final(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property NIOSH_HorizontalLocationFinal() As CATBSTR (Read
                | Only)
                | 
                |     This field is set to a valid value for the NIOSH 1991 analysis
                |     only.
                |     This value provides the distance of the hands from the mid-point between
                |     the ankles, in in the current V5 units.
                |     This property gives the horizontal location at the
                |     destination
                |     (i.e., given the final posture of the manikin).

        :rtype: str
        """

        return self.swk_ergo_lift_lower.NIOSH_HorizontalLocationFinal

    @property
    def niosh_horizontal_location_initial(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property NIOSH_HorizontalLocationInitial() As CATBSTR (Read
                | Only)
                | 
                |     This field is set to a valid value for the NIOSH 1991 analysis
                |     only.
                |     This value provides the distance of the hands from the mid-point between
                |     the ankles, in in the current V5 units.
                |     This property gives the horizontal location at the origin
                |     (i.e., given the initial posture of the manikin).

        :rtype: str
        """

        return self.swk_ergo_lift_lower.NIOSH_HorizontalLocationInitial

    @property
    def niosh_horizontal_multiplier_final(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property NIOSH_HorizontalMultiplierFinal() As CATBSTR (Read
                | Only)
                | 
                |     This field is set to a valid value for the NIOSH 1991 analysis
                |     only.
                |     This value provides the horizontal multiplier.
                |     This property gives the horizontal multiplier at the
                |     destination
                |     (i.e., given the final posture of the manikin).

        :rtype: str
        """

        return self.swk_ergo_lift_lower.NIOSH_HorizontalMultiplierFinal

    @property
    def niosh_horizontal_multiplier_initial(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property NIOSH_HorizontalMultiplierInitial() As CATBSTR (Read
                | Only)
                | 
                |     This field is set to a valid value for the NIOSH 1991 analysis
                |     only.
                |     This value provides the horizontal multiplier.
                |     This property gives the horizontal multiplier at the
                |     origin
                |     (i.e., given the initial posture of the manikin).

        :rtype: str
        """

        return self.swk_ergo_lift_lower.NIOSH_HorizontalMultiplierInitial

    @property
    def niosh_li_final(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property NIOSH_LIFinal() As CATBSTR (Read Only)
                | 
                |     This field is set to a valid value for the NIOSH 1991 analysis
                |     only.
                |     This value provides a relative estimate of the level of physical
                |     stress.
                |     This property gives the lifting index at the destination
                |     (i.e., given the final posture of the manikin).

        :rtype: str
        """

        return self.swk_ergo_lift_lower.NIOSH_LIFinal

    @property
    def niosh_li_initial(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property NIOSH_LIInitial() As CATBSTR (Read Only)
                | 
                |     This field is set to a valid value for the NIOSH 1991 analysis
                |     only.
                |     This value provides a relative estimate of the level of physical
                |     stress.
                |     This property gives the lifting index at the origin
                |     (i.e., given the initial posture of the manikin).

        :rtype: str
        """

        return self.swk_ergo_lift_lower.NIOSH_LIInitial

    @property
    def niosh_load_constant(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property NIOSH_LoadConstant() As CATBSTR (Read Only)
                | 
                |     This field is set to a valid value for the NIOSH 1991 analysis
                |     only.
                |     This value provides the load constant.
                |     This property gives the load constant at the destination
                |     (i.e., given the final posture of the manikin).

        :rtype: str
        """

        return self.swk_ergo_lift_lower.NIOSH_LoadConstant

    @property
    def niosh_maximum_perm_limit(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property NIOSH_MaximumPermLimit() As CATBSTR (Read Only)
                | 
                |     This field is set to a valid value for the NIOSH 1981 analysis
                |     only.
                |     This value represents a weight limit, above which the
                |     task is considered dangerous and requires engineering controls.

        :rtype: str
        """

        return self.swk_ergo_lift_lower.NIOSH_MaximumPermLimit

    @property
    def niosh_rwl_final(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property NIOSH_RWLFinal() As CATBSTR (Read Only)
                | 
                |     This field is set to a valid value for the NIOSH 1991 analysis
                |     only.
                |     It represents the weight of the load, that healthy workers
                |     could
                |     perform over a certain period of time without risk.
                |     This property gives the recommended weight at the
                |     destination
                |     (i.e., given the final posture of the manikin).

        :rtype: str
        """

        return self.swk_ergo_lift_lower.NIOSH_RWLFinal

    @property
    def niosh_rwl_initial(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property NIOSH_RWLInitial() As CATBSTR (Read Only)
                | 
                |     This field is set to a valid value for the NIOSH 1991 analysis
                |     only.
                |     It represents the weight of the load that healthy workers
                |     could perform over a certain period of time without risk.
                |     This property gives the recommended weight at the origin
                |     (i.e., given the initial posture of the manikin).

        :rtype: str
        """

        return self.swk_ergo_lift_lower.NIOSH_RWLInitial

    @property
    def niosh_travel_distance(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property NIOSH_TravelDistance() As CATBSTR (Read Only)
                | 
                |     This field is set to a valid value for the NIOSH 1991 analysis
                |     only.
                |     This value provides the absolute value of the difference between the
                |     vertical heights at the destination and origin of the lift, in in the current
                |     V5 units.
                |     This property gives the travel distance

        :rtype: str
        """

        return self.swk_ergo_lift_lower.NIOSH_TravelDistance

    @property
    def niosh_vertical_location_final(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property NIOSH_VerticalLocationFinal() As CATBSTR (Read
                | Only)
                | 
                |     This field is set to a valid value for the NIOSH 1991 analysis
                |     only.
                |     This value provides the distance of the hands above the floor, in the
                |     current V5 units.
                |     This property gives the vertical location at the
                |     destination
                |     (i.e., given the final posture of the manikin).

        :rtype: str
        """

        return self.swk_ergo_lift_lower.NIOSH_VerticalLocationFinal

    @property
    def niosh_vertical_location_initial(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property NIOSH_VerticalLocationInitial() As CATBSTR (Read
                | Only)
                | 
                |     This field is set to a valid value for the NIOSH 1991 analysis
                |     only.
                |     This value provides the distance of the hands above the floor, in in the
                |     current V5 units.
                |     This property gives the vertical location at the origin
                |     (i.e., given the initial posture of the manikin).

        :rtype: str
        """

        return self.swk_ergo_lift_lower.NIOSH_VerticalLocationInitial

    @property
    def niosh_vertical_multiplier_final(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property NIOSH_VerticalMultiplierFinal() As CATBSTR (Read
                | Only)
                | 
                |     This field is set to a valid value for the NIOSH 1991 analysis
                |     only.
                |     This value provides the absolute value or deviation of V (vertical
                |     location) from an optimum height of 30 inches (75 cm).
                |     This property gives the vertical multiplier at the
                |     destination
                |     (i.e., given the final posture of the manikin).

        :rtype: str
        """

        return self.swk_ergo_lift_lower.NIOSH_VerticalMultiplierFinal

    @property
    def niosh_vertical_multiplier_initial(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property NIOSH_VerticalMultiplierInitial() As CATBSTR (Read
                | Only)
                | 
                |     This field is set to a valid value for the NIOSH 1991 analysis
                |     only.
                |     This value provides the absolute value or deviation of V (vertical
                |     location) from an optimum height of 30 inches (75 cm).
                |     This property gives the vertical multiplier at the origin
                |     (i.e., given the initial posture of the manikin).

        :rtype: str
        """

        return self.swk_ergo_lift_lower.NIOSH_VerticalMultiplierInitial

    @property
    def object_weight(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ObjectWeight() As CATBSTR
                | 
                |     Returns or sets the weight of the object being lifted.
                |     This weight must specified at least once, if the current input guideline is
                |     "NIOSH1991".
                |     Failure to do so will result in invalid output values.

        :rtype: str
        """

        return self.swk_ergo_lift_lower.ObjectWeight

    @object_weight.setter
    def object_weight(self, value: str):
        """
        :param str value:
        """

        self.swk_ergo_lift_lower.ObjectWeight = value

    @property
    def population(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Population() As double
                | 
                |     Returns or sets the percentage of the population that should be able to
                |     perform the lift/lower task safely.
                |     This property can only take the values 50.0, 75.0 and 90.0,and must be
                |     specified
                |     at least once, if the current input guideline is
                |     "NIOSH1991".
                |     Failure to do so will result in invalid output values.

        :rtype: float
        """

        return self.swk_ergo_lift_lower.Population

    @population.setter
    def population(self, value: float):
        """
        :param float value:
        """

        self.swk_ergo_lift_lower.Population = value

    @property
    def snook_maximum_weight(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Snook_MaximumWeight() As CATBSTR (Read Only)
                | 
                |     This field is set to a valid value for the Snook/Ciriello 1991 analysis
                |     only.
                |     It is the maximum acceptable weight of the load that the selected
                |     population
                |     can lift or carry with reasonable safety.

        :rtype: str
        """

        return self.swk_ergo_lift_lower.Snook_MaximumWeight

    @property
    def warning_message(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property WarningMessage() As CATBSTR (Read Only)
                | 
                |     Returns an eventual warning message generated along with the study.

        :rtype: str
        """

        return self.swk_ergo_lift_lower.WarningMessage

    def save_final_posture(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SaveFinalPosture()
                | 
                |     Saves the current posture of the mankin as the final posture for the
                |     lift/lower analysis.

        :rtype: None
        """
        return self.swk_ergo_lift_lower.SaveFinalPosture()

    def save_initial_posture(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SaveInitialPosture()
                | 
                |     Saves the current posture of the mankin as the initial posture for the
                |     lift/lower analysis.

        :rtype: None
        """
        return self.swk_ergo_lift_lower.SaveInitialPosture()

    def __repr__(self):
        return f'SWKErgoLiftLower(name="{self.name}")'
