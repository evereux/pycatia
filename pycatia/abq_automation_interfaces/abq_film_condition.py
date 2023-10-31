#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.abq_automation_interfaces.abq_load import ABQLoad


class ABQFilmCondition(ABQLoad):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     ABQAutomationItf.ABQLoad
                |                         ABQFilmCondition
                | 
                | Represents an Abaqus film condition (ABQFilmCondition) object.
                | Role: Access an Abaqus film condition object or determine its
                | properties.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.abq_film_condition = com_object

    @property
    def apply_user_subroutine(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ApplyUserSubroutine() As boolean
                | 
                |     Sets or returns the user subroutine flag.
                | 
                |     Returns:
                |         A boolean specifying whether a nonuniform film coefficient is defined
                |         in user subroutine FILM.

        :rtype: bool
        """

        return self.abq_film_condition.ApplyUserSubroutine

    @apply_user_subroutine.setter
    def apply_user_subroutine(self, value: bool):
        """
        :param bool value:
        """

        self.abq_film_condition.ApplyUserSubroutine = value

    @property
    def dependencies(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property dependencies() As long (Read Only)
                | 
                |     Returns the number of temperature-dependent film
                |     coefficients.
                | 
                |     Returns:
                |         The number of temperature-dependent film coefficients.

        :rtype: int
        """

        return self.abq_film_condition.dependencies

    @property
    def film_coefficient(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property filmCoeff() As double
                | 
                |     Sets or returns the reference film coefficient if the film condition is not
                |     temperature dependent.
                | 
                |     Returns:
                |         The reference film coefficient if the film condition is not temperature
                |         dependent.

        :rtype: float
        """

        return self.abq_film_condition.filmCoeff

    @film_coefficient.setter
    def film_coefficient(self, value: float):
        """
        :param float value:
        """

        self.abq_film_condition.filmCoeff = value

    @property
    def sink_temperature(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property sinkTemperature() As double
                | 
                |     Sets or returns the reference sink temperature.
                | 
                |     Returns:
                |         The reference sink temperature.

        :rtype: float
        """

        return self.abq_film_condition.sinkTemperature

    @sink_temperature.setter
    def sink_temperature(self, value: float):
        """
        :param float value:
        """

        self.abq_film_condition.sinkTemperature = value

    @property
    def temperature_dependency(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property temperatureDependency() As boolean
                | 
                |     Sets or returns the temperature dependency.
                | 
                |     Returns:
                |         A boolean specifying whether the film condition is dependent on
                |         temperature.

        :rtype: bool
        """

        return self.abq_film_condition.temperatureDependency

    @temperature_dependency.setter
    def temperature_dependency(self, value: bool):
        """
        :param bool value:
        """

        self.abq_film_condition.temperatureDependency = value

    def add_temp_dependent_film_coeff_table(self, i_film_coeff: tuple, i_temperature: tuple) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub AddTempDependentFilmCoeffTable(CATSafeArrayVariant
                | iFilmCoeff,
                | CATSafeArrayVariant iTemperature)
                | 
                |     Adds a list of temperature dependent film coefficients if the film
                |     condition is temperature dependent. The number of values in both of the
                |     parameters should match. If either list contains extra values, the extra values
                |     are discarded.
                | 
                |     Parameters:
                | 
                |         iFilmCoeff
                |             The list of film coefficients.
                |         iTemperature
                |             The list of temperatures.

        :param tuple i_film_coeff:
        :param tuple i_temperature:
        :rtype: None
        """
        return self.abq_film_condition.AddTempDependentFilmCoeffTable(i_film_coeff, i_temperature)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'add_temp_dependent_film_coeff_table'
        # # vba_code = """
        # # Public Function add_temp_dependent_film_coeff_table(abq_film_condition)
        # #     Dim iFilmCoeff (2)
        # #     abq_film_condition.AddTempDependentFilmCoeffTable iFilmCoeff
        # #     add_temp_dependent_film_coeff_table = iFilmCoeff
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_name_of_film_coeff_amplitude(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetNameOfFilmCoeffAmplitude(CATBSTR ofilmAmplitude)
                | 
                |     Returns the name of the amplitude that contains the variation of the the
                |     film coefficient with time.
                | 
                |     Parameters:
                | 
                |         ofilmAmplitude
                |             The name of the amplitude that contains the variation of the the
                |             film coefficient with time.

        :param str ofilm_amplitude:
        :rtype: None
        """
        return self.abq_film_condition.GetNameOfFilmCoeffAmplitude()

    def get_name_of_sink_amplitude(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetNameOfSinkAmplitude(CATBSTR osinkAmplitude)
                | 
                |     Returns the name of the amplitude that contains the variation of the sink
                |     temperature with time.
                | 
                |     Parameters:
                | 
                |         osinkAmplitude
                |             The name of the amplitude that contains the variation of the sink
                |             temperature with time.

        :param str osink_amplitude:
        :rtype: None
        """
        return self.abq_film_condition.GetNameOfSinkAmplitude()

    def get_temp_dependent_film_coeff_table(self) -> list:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetTempDependentFilmCoeffTable(CATSafeArrayVariant
                | oFilmCoeff,
                | CATSafeArrayVariant oTemperature)
                | 
                |     Returns a list of temperature dependent film coefficients if the film
                |     condition is temperature dependent.
                | 
                |     Parameters:
                | 
                |         oFilmCoeff
                |             The list of film coefficients.
                |         oTemperature
                |             The list of temperatures.

        :param tuple o_film_coeff:
        :param tuple o_temperature:
        :rtype: None
        """
        return self.abq_film_condition.GetTempDependentFilmCoeffTable()
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_temp_dependent_film_coeff_table'
        # # vba_code = """
        # # Public Function get_temp_dependent_film_coeff_table(abq_film_condition)
        # #     Dim oFilmCoeff (2)
        # #     abq_film_condition.GetTempDependentFilmCoeffTable oFilmCoeff
        # #     get_temp_dependent_film_coeff_table = oFilmCoeff
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_named_film_coeff_amplitude(self, ifilm_amplitude: str) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetNamedFilmCoeffAmplitude(CATBSTR ifilmAmplitude)
                | 
                |     Sets the name of the amplitude that gives the variation of the the film
                |     coefficient with time.
                | 
                |     Parameters:
                | 
                |         ifilmAmplitude
                |             The name of the amplitude that gives the variation of the the film
                |             coefficient with time.

        :param str ifilm_amplitude:
        :rtype: None
        """
        return self.abq_film_condition.SetNamedFilmCoeffAmplitude(ifilm_amplitude)

    def set_named_sink_amplitude(self, isink_amplitude: str) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetNamedSinkAmplitude(CATBSTR isinkAmplitude)
                | 
                |     Sets the name of the amplitude that contains the variation of the sink
                |     temperature with time.
                | 
                |     Parameters:
                | 
                |         isinkAmplitude
                |             The name of the amplitude that contains the variation of the sink
                |             temperature with time.

        :param str isink_amplitude:
        :rtype: None
        """
        return self.abq_film_condition.SetNamedSinkAmplitude(isink_amplitude)

    def __repr__(self):
        return f'ABQFilmCondition(name="{self.name}")'
