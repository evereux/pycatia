#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.knowledge_interfaces.check import Check
from pycatia.knowledge_interfaces.real_param import RealParam


class OptimizationConstraint(Check):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     KnowledgeInterfaces.KnowledgeObject
                |                        KnowledgeInterfaces.KnowledgeActivateObject
                |                             KnowledgeInterfaces.Relation
                |                                 KnowledgeInterfaces.Check
                |                                     OptimizationConstraint
                | 
                | Represents an optimization constraint.
                | 
                | See also:
                |     OptimizationConstraints
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.optimization_constraint = com_object

    @property
    def distance_to_satisfaction(self) -> RealParam:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property DistanceToSatisfaction() As RealParam (Read Only)
                | 
                |     Returns the parameter containing the distance to constraint satisfaction.

        :rtype: RealParam
        """

        return RealParam(self.optimization_constraint.DistanceToSatisfaction)

    @property
    def precision(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property Precision() As double
                | 
                |     Returns or sets the constraint precision. Only for equality
                |     constraints.
                |     The constraint precision allows the system to know when an equality constraint can be declared as
                |     satisfied (when : distance to satisfaction < precision).

        :rtype: float
        """

        return self.optimization_constraint.Precision

    @precision.setter
    def precision(self, value: float):
        """
        :param float value:
        """

        self.optimization_constraint.Precision = value

    @property
    def satisfaction(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property Satisfaction() As boolean (Read Only)
                | 
                |     Returns the constraint satisfaction.

        :rtype: bool
        """

        return self.optimization_constraint.Satisfaction

    def __repr__(self):
        return f'OptimizationConstraint(name="{self.name}")'
