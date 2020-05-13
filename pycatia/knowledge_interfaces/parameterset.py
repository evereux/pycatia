#! /usr/bin/python3.6

from pycatia.knowledge_interfaces import parameters
from pycatia.knowledge_interfaces import parametersets


class ParameterSet:
    def __init__(self, parameterset):
        self.parameterset = parameterset

    @property
    def name(self):
        return self.parameterset.Name

    def all_parameters(self):
        return parameters.Parameters(self.parameterset.AllParameters)

    def direct_parameters(self):
        return parameters.Parameters(self.parameterset.DirectParameters)

    def root_parameter_sets(self):
        return parametersets.ParameterSets(self.parameterset.ParameterSets)

    def __repr__(self):
        return 'ParameterSet()'
