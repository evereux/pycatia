#! /usr/bin/python3.7
from pywintypes import com_error
from .parameter import Parameter


class Parameters:
    """
    .. note::
        CAA V5 Visual Basic help

        Represents the Parameters collection of the part or the product.


    :param part: CATIA Parameter COM object.
    """

    def __init__(self, parameters):
        self.parameters = parameters

    def get_parameterset(self):
        return self.parameters

    @property
    def name(self):
        """
        :return: str - parameterset name
        """
        return self.parameters.Name

    def is_parameter(self, parameter_index):
        """

        :param str parameter_index: parameter name.
        :return: bool
        """
        try:
            if self.parameters.Item(parameter_index):
                return True
        except com_error:
            return False

    def get_parameter(self, parameter_index):
        """

        :param str parameter_index: parameter name.
        :return: parameter
        """
        if not self.is_parameter(parameter_index):
            raise AttributeError(f'Parameter [{parameter_index}] could not be found')

        return Parameter(self.parameters.Item(parameter_index))

    def count_parameters(self):
        """
        :return: int
        """
        return self.parameters.Count

    def has_parameters(self):
        """
        :return: bool
        """
        if self.parameters.Count > 0:
            return True

        return False

    def get_parameters(self):
        """

        :return: list(Parameter())
        """

        parameter = list()

        if self.has_parameters():
            for i in range(self.parameters.Count):
                para = Parameter(self.parameters.Item(i + 1))
                parameter.append(para)

        return parameter

    def add_bool_parameter(self, name, value):
        return BoolParam(name, value, self.parameters)
        # return self.parameters.CreateBoolean(name, value)

    def add_dim_parameter(self, name, unit_type, value):

        unit_types = ["LENGTH", "ANGLE"]
        if unit_type not in unit_types:
            raise ValueError(f'Dimension type must be in [{unit_types}]')

        return self.parameters.CreateDimension(name, unit_type, value)

    def add_int_parameter(self, name, value):
        return IntParam(name, value, self.parameters)

    def add_real_parameter(self, name, value):
        return RealParam(name, value, self.parameters)

    def add_list_parameter(self, name):
        return self.parameters.CreateList(name)

    def add_string_parameter(self, name, text):
        return StrParam(name, text, self.parameters)

    def remove_parameter(self, name):
        return self.parameters.Remove(name)


class IntParam(Parameter):
    def __init__(self, name, value, parameters):
        if not isinstance(value, int):
            raise ValueError(f'Parameter value [{value}] has to be int()')

        self.parameters = self.set_parameterset(parameters)
        self.parameter = self.parameters.CreateInteger(name, value)

    def set_parameterset(self, parameters):
        if isinstance(parameters, Parameters):
            return parameters.get_parameterset()
        else:
            return parameters

    @property
    def value(self):
        return self.parameter.Value

    @value.setter
    def value(self, value):
        self.parameter.Value = value

    @property
    def range_max(self):
        return self.parameter.RangeMax

    @range_max.setter
    def range_max(self, range_max):
        self.parameter.RangeMax = range_max

    @property
    def range_max_validity(self):
        return self.parameters.RangeMaxValidity

    @range_max_validity.setter
    def range_max_validity(self, range_max_validity):
        self.parameters.RangeMaxValidity = range_max_validity

    @property
    def range_min(self):
        return self.parameter.RangeMin

    @range_min.setter
    def range_min(self, range_min):
        self.parameter.RangeMin = range_min

    @property
    def range_min_validity(self):
        return self.parameters.RangeMinValidity

    @range_min_validity.setter
    def range_min_validity(self, range_min_validity):
        self.parameters.RangeMinValidity = range_min_validity


class BoolParam(Parameter):
    def __init__(self, name, value, parameters):
        if not isinstance(value, bool):
            raise ValueError(f'Parameter value [{value}] has to be bool()')

        self.parameters = self.set_parameterset(parameters)
        self.parameter = self.parameters.CreateBoolean(name, value)

    def set_parameterset(self, parameters):
        if isinstance(parameters, Parameters):
            return parameters.get_parameterset()
        else:
            return parameters

    @property
    def value(self):
        return self.parameter.Value

    @value.setter
    def value(self, value):
        self.parameter.Value = value


class StrParam(Parameter):
    def __init__(self, name, text, parameters):
        if not isinstance(text, str):
            raise ValueError(f'Parameter text [{text}] has to be str()')

        self.parameters = self.set_parameterset(parameters)
        self.parameter = self.parameters.CreateBoolean(name, text)

    def set_parameterset(self, parameters):
        if isinstance(parameters, Parameters):
            return parameters.get_parameterset()
        else:
            return parameters

    @property
    def text(self):
        return self.parameter.Value

    @text.setter
    def text(self, text):
        self.parameter.Value = text


class RealParam(Parameter):
    def __init__(self, name, value, parameters):
        if not isinstance(value, float):
            raise ValueError(f'Parameter value [{value}] has to be float()')

        self.parameters = self.set_parameterset(parameters)
        self.parameter = self.parameters.CreateBoolean(name, value)

    def set_parameterset(self, parameters):
        if isinstance(parameters, Parameters):
            return parameters.get_parameterset()
        else:
            return parameters

    @property
    def value(self):
        return self.parameter.Value

    @value.setter
    def value(self, value):
        self.parameter.Value = value

    @property
    def max_tolerance(self):
        return self.parameter.MaximumTolerance

    @max_tolerance.setter
    def max_tolerance(self, max_tolerance):
        self.parameter.MaximumTolerance = max_tolerance

    @property
    def min_tolerance(self):
        return self.parameter.MinimumTolerance

    @min_tolerance.setter
    def min_tolerance(self, min_tolerance):
        self.parameter.MinimumTolerance = min_tolerance

    @property
    def range_max(self):
        return self.parameter.RangeMax

    @range_max.setter
    def range_max(self, range_max):
        self.parameter.RangeMax = range_max

    @property
    def range_max_validity(self):
        return self.parameters.RangeMaxValidity

    @range_max_validity.setter
    def range_max_validity(self, range_max_validity):
        self.parameters.RangeMaxValidity = range_max_validity

    @property
    def range_min(self):
        return self.parameter.RangeMin

    @range_min.setter
    def range_min(self, range_min):
        self.parameter.RangeMin = range_min

    @property
    def range_min_validity(self):
        return self.parameters.RangeMinValidity

    @range_min_validity.setter
    def range_min_validity(self, range_min_validity):
        self.parameters.RangeMinValidity = range_min_validity
