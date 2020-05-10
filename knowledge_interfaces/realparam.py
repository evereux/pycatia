#! /usr/bin/python3.6

from pycatia.knowledge_interfaces.parameter import Parameter


class RealParam(Parameter):
    def __init__(self, name=None, value=None, parameter=None, parent=None):
        super().__init__(parameter)
        if value and not isinstance(value, float):
            raise ValueError(f'Parameter value [{value}] has to be float()')

        self.parameters = self.set_parameters(parent)

        if parameter:
            self.parameter = parameter
        else:
            self.parameter = Parameter(self.parameters.CreateBoolean(name, value))

    def set_parameters(self, parent):
        try:
            # if parent is <class "Parameters">
            return parent.parameters
        except AttributeError:
            # if parent is something like Catia.ActiveDocument.Part.Parameters
            return parent

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
