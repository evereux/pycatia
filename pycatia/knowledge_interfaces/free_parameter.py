#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.knowledge_interfaces.real_param import RealParam
from pycatia.system_interfaces.any_object import AnyObject


class FreeParameter(AnyObject):

    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     FreeParameter
                | 
                | Interface to access a CATIAFreeParameter.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.free_parameter = com_object

    @property
    def inf_range(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property InfRange() As double
                | 
                |     Returns or sets the inferior bound of the free parameter object. The
                |     optimization cannot escape those bounds.

        :rtype: float
        """

        return self.free_parameter.InfRange

    @inf_range.setter
    def inf_range(self, value: float):
        """
        :param float value:
        """

        self.free_parameter.InfRange = value

    @property
    def parameter(self) -> RealParam:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property Parameter() As RealParam
                | 
                |     Returns or sets which parameter (CATIAParameter) is linked to this object.
                |     The parameter must be real.

        :rtype: RealParam
        """

        return RealParam(self.free_parameter.Parameter)

    @parameter.setter
    def parameter(self, value: RealParam):
        """
        :param RealParam value:
        """

        self.free_parameter.Parameter = value

    @property
    def step(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property Step() As double
                | 
                |     Returns or sets the initial step used by the optimisation to look for a
                |     better solution. This step is just a preliminary indication. It will vary
                |     during the optimisation process.

        :rtype: float
        """

        return self.free_parameter.Step

    @step.setter
    def step(self, value: float):
        """
        :param float value:
        """

        self.free_parameter.Step = value

    @property
    def sup_range(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property SupRange() As double
                | 
                |     Returns or sets the superior bound of the free parameter object. The
                |     optimization cannot escape those bounds.

        :rtype: float
        """

        return self.free_parameter.SupRange

    @sup_range.setter
    def sup_range(self, value: float):
        """
        :param float value:
        """

        self.free_parameter.SupRange = value

    def __repr__(self):
        return f'FreeParameter(name="{ self.name }")'
