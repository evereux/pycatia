#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from typing import TYPE_CHECKING

from pycatia.knowledge_interfaces.parameters import Parameters
from pycatia.system_interfaces.any_object import AnyObject

if TYPE_CHECKING:
    from pycatia.knowledge_interfaces.parameter_sets import ParameterSets

class ParameterSet(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     ParameterSet
                | 
                | Represents parameter set.
                | It is the node that contains user parameters.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.parameter_set = com_object

    @property
    def all_parameters(self) -> list:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic help
                | AllParameters
                | o Property AllParameters() As Parameters
                |
                | Returns all parameters under this set of parameter.
                | Parameters:

        :rtype: Parameters
        """
        from .parameter import Parameter
        items = []
        for i in range(0, self.parameter_set.AllParameters.Count):
            items.append(Parameter(self.parameter_set.AllParameters.Item(i + 1)))
        return items

    @property
    def direct_parameters(self) -> Parameters:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property DirectParameters() As Parameters (Read Only)
                | 
                |     Returns directly aggregated parameters.

        :rtype: Parameters
        """

        return Parameters(self.parameter_set.DirectParameters)

    @property
    def parameter_sets(self) -> 'ParameterSets':
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property ParameterSets() As ParameterSets (Read Only)
                | 
                |     Returns the children parameter sets.

        :rtype: ParameterSets
        """
        from pycatia.knowledge_interfaces.parameter_sets import ParameterSets
        return ParameterSets(self.parameter_set.ParameterSets)

    def __repr__(self):
        return f'ParameterSet(name="{self.name}")'
