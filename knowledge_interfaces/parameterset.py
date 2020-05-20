#! /usr/bin/python3.6
# module initially auto generated using V5Automation.chm from CATIA V5 R25

from pycatia.system_interfaces.base_object import AnyObject


class ParameterSet(AnyObject):
    """
        .. note::
            CAA V5 Visual Basic help

                | Represents parameter set.It is the node that contains user parameters.

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.parameterset = com_object

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
        from .parameter import Parameter
        items = []
        for i in range(0, self.parameterset.AllParameters.Count):
            items.append(Parameter(self.parameterset.AllParameters.Item(i + 1)))
        return items

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
        from .parameters import Parameters
        return Parameters(self.parameterset.DirectParameters)

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
        from .parametersets import ParameterSets
        return ParameterSets(self.parameterset.ParameterSets)

    def __repr__(self):
        return f'ParameterSet(name="{self.name}")'
