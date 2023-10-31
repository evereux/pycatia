#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.dnb_human_modeling_interfaces.swk_anthro_variable import SWKAnthroVariable
from pycatia.dnb_human_modeling_interfaces.swk_manikin_part import SWKManikinPart


class SWKAnthro(SWKManikinPart):
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
                |                         SWKAnthro
                | 
                | This interface manages the anthropometry of the manikin.
                | It provides access to the anthropometry data (variables,
                | sex...)
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.swk_anthro = com_object

    @property
    def construction_type(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ConstructionType() As CATBSTR
                | 
                |     Return or sets the construction type of the manikin. This property can take
                |     the following two values: "Standing" and "Sitting".
                |     If the construction is set to "Standing",
                |     then the manikin is constructed as of type 'standing'.
                |     If the construction is set to "Sitting",
                |     then the manikin is constructed as of type 'sitting'.
                | 
                |     The chosen construction type influences the way the manikin's hips,
                |     thighs and knees are constructed to reflect the changes in those body
                |     parts when a human changes from a standing to a sitting posture.

        :rtype: str
        """

        return self.swk_anthro.ConstructionType

    @construction_type.setter
    def construction_type(self, value: str):
        """
        :param str value:
        """

        self.swk_anthro.ConstructionType = value

    @property
    def gender(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Gender() As CATBSTR
                | 
                |     Returns or sets the gender of the manikin.

        :rtype: str
        """

        return self.swk_anthro.Gender

    @gender.setter
    def gender(self, value: str):
        """
        :param str value:
        """

        self.swk_anthro.Gender = value

    @property
    def interpolation_method(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property InterpolationMethod() As CATBSTR
                | 
                |     Returns or sets the interpolation. The interpolation is an
                |     algorithm
                |     that restricts the values entered by the user to a certain minimum and
                |     maximum value. Valid values are "None" or "Multinormal".

        :rtype: str
        """

        return self.swk_anthro.InterpolationMethod

    @interpolation_method.setter
    def interpolation_method(self, value: str):
        """
        :param str value:
        """

        self.swk_anthro.InterpolationMethod = value

    @property
    def limit_bound(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property LimitBound() As double
                | 
                |     Returns or sets the population accommodation, in terms of a limit
                |     bound.
                |     The population accommodation is used in the multi-normal
                |     algorithm, to calculate the limits of the automatic
                |     variables
                |     when a user-defined anthropometry is entered.
                |     The greater the population accommodation is, the wider the limits
                |     on the automatic variables will be. The value of this property must le
                |     within the range [0.0, 4.0].

        :rtype: float
        """

        return self.swk_anthro.LimitBound

    @limit_bound.setter
    def limit_bound(self, value: float):
        """
        :param float value:
        """

        self.swk_anthro.LimitBound = value

    @property
    def number_of_variables(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property NumberOfVariables() As long (Read Only)
                | 
                |     Returns the number of variables contained in this anthropometry.

        :rtype: int
        """

        return self.swk_anthro.NumberOfVariables

    @property
    def population(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Population() As CATBSTR
                | 
                |     Return or sets the Population of the manikin. The population provided must
                |     be one of the default populations ("American", "Canadian", "French",
                |     "Japanese", "Korean", "German" or "Chinese (Taiwan)"), or an external
                |     population defined by the user. Please note that no user-defined population
                |     should bear the name of one of the default populations.

        :rtype: str
        """

        return self.swk_anthro.Population

    @population.setter
    def population(self, value: str):
        """
        :param str value:
        """

        self.swk_anthro.Population = value

    @property
    def population_accommodation(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property PopulationAccommodation() As double
                | 
                |     Returns or sets the population accommodation. The population accommodation
                |     is used in the multi-normal
                |     algorithm, to calculate the limits of the automatic
                |     variables
                |     when a user-defined anthropometry is entered.
                |     The greater the population accommodation is, the wider the
                |     limits
                |     on the automatic variables will be. The value of this property must le
                |     within the range [0.0, 100.0].

        :rtype: float
        """

        return self.swk_anthro.PopulationAccommodation

    @population_accommodation.setter
    def population_accommodation(self, value: float):
        """
        :param float value:
        """

        self.swk_anthro.PopulationAccommodation = value

    def get_variable_at_index(self, pi_index: int) -> SWKAnthroVariable:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetVariableAtIndex(long piIndex) As SWKAnthroVariable
                | 
                |     Returns the variable at the specified index.
                | 
                |     Parameters:
                | 
                |         piIndex
                |             The index of the variable to retrieve.

        :param int pi_index:
        :rtype: SWKAnthroVariable
        """
        return SWKAnthroVariable(self.swk_anthro.GetVariableAtIndex(pi_index))

    def get_variable_from_us_number(self, pi_ref_number: int) -> SWKAnthroVariable:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetVariableFromUsNumber(long piRefNumber) As
                | SWKAnthroVariable
                | 
                |     Returns the variable from a specified us number.
                | 
                |     Parameters:
                | 
                |         piRefNumber
                |             The reference number of the variable to retrieve (ex.: 3 for us3,
                |             100 for us100, etc).

        :param int pi_ref_number:
        :rtype: SWKAnthroVariable
        """
        return SWKAnthroVariable(self.swk_anthro.GetVariableFromUsNumber(pi_ref_number))

    def reset(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub Reset()
                | 
                |     Reset the anthtropometry. This method resets each variable back to the
                |     automatic mode, and then updates the anthropometry.

        :rtype: None
        """
        return self.swk_anthro.Reset()

    def __repr__(self):
        return f'SWKAnthro(name="{self.name}")'
