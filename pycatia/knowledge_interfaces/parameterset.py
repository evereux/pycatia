#! /usr/bin/python3.6
# module initially auto generated using V5Automation.chm from CATIA V5 R25


class ParameterSet:
    """
        .. note::
            CAA V5 Visual Basic help

                | Represents parameter set.It is the node that contains user parameters.

    """

    def __init__(self, parameterset):
        self.parameterset = parameterset

    @property
    def all_parameters(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | AllParameters
                | o Property AllParameters(    ) As Parameters
                |
                | Returns all parameters under this set of parameter.


                | Parameters:


        """
        return self.parameterset.AllParameters

    @property
    def direct_parameters(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | DirectParameters
                | o Property DirectParameters(    ) As Parameters
                |
                | Returns directly aggregated parameters.


                | Parameters:


        """
        return self.parameterset.DirectParameters

    @property
    def parameter_sets(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | ParameterSets
                | o Property ParameterSets(    ) As ParameterSets
                |
                | Returns the children parameter sets.


                | Parameters:


        """
        return self.parameterset.ParameterSets

    def __repr__(self):
        return f'ParameterSet()'
