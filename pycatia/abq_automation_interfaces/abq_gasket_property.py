#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.abq_automation_interfaces.abq_property import ABQProperty
from pycatia.analysis_interfaces.analysis_entity import AnalysisEntity


class ABQGasketProperty(ABQProperty):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     ABQAutomationItf.ABQProperty
                |                         ABQGasketProperty

    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.abq_gasket_property = com_object

    @property
    def initial_gap(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property InitialGap() As double
                | 
                |     Sets or returns the Initial gap value

        :rtype: float
        """

        return self.abq_gasket_property.InitialGap

    @initial_gap.setter
    def initial_gap(self, value: float):
        """
        :param float value:
        """

        self.abq_gasket_property.InitialGap = value

    @property
    def initial_thickness(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property InitialThickness() As double
                | 
                |     Sets or returns the Initial thickness value

        :rtype: float
        """

        return self.abq_gasket_property.InitialThickness

    @initial_thickness.setter
    def initial_thickness(self, value: float):
        """
        :param float value:
        """

        self.abq_gasket_property.InitialThickness = value

    @property
    def initial_thickness_type(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property InitialThicknessType() As InitialThickness_Type
                | 
                |     Sets or returns the Initial thickness type

        :return: enum initial_thickness_type
        :rtype: int
        """

        return self.abq_gasket_property.InitialThicknessType

    @initial_thickness_type.setter
    def initial_thickness_type(self, value: int):
        """
        :param int value: enum initial_thickness_type
        """

        self.abq_gasket_property.InitialThicknessType = value

    @property
    def initial_void(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property InitialVoid() As double
                | 
                |     Sets or returns the Initial void value

        :rtype: float
        """

        return self.abq_gasket_property.InitialVoid

    @initial_void.setter
    def initial_void(self, value: float):
        """
        :param float value:
        """

        self.abq_gasket_property.InitialVoid = value

    @property
    def stabilization_stiffness(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property StabilizationStiffness() As double
                | 
                |     Sets or returns the Stabilization stiffness value

        :rtype: float
        """

        return self.abq_gasket_property.StabilizationStiffness

    @stabilization_stiffness.setter
    def stabilization_stiffness(self, value: float):
        """
        :param float value:
        """

        self.abq_gasket_property.StabilizationStiffness = value

    @property
    def stabilization_stiffness_type(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property StabilizationStiffnessType() As
                | StabilizationStiffness_Type
                | 
                |     Sets or returns the Stabilization stiffness type

        :return: enum stabilization_stiffness_type
        :rtype: int
        """

        return self.abq_gasket_property.StabilizationStiffnessType

    @stabilization_stiffness_type.setter
    def stabilization_stiffness_type(self, value: int):
        """
        :param int value: enum stabilization_stiffness_type
        """

        self.abq_gasket_property.StabilizationStiffnessType = value

    @property
    def support_property(self) -> AnalysisEntity:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property SupportProperty() As AnalysisEntity
                | 
                |     Sets or returns the 3D structrel property.

        :rtype: AnalysisEntity
        """

        return AnalysisEntity(self.abq_gasket_property.SupportProperty)

    @support_property.setter
    def support_property(self, value: AnalysisEntity):
        """
        :param AnalysisEntity value:
        """

        self.abq_gasket_property.SupportProperty = value

    def __repr__(self):
        return f'ABQGasketProperty(name="{self.name}")'
