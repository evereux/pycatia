#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.abq_automation_interfaces.abq_interaction import ABQInteraction
from pycatia.analysis_interfaces.analysis_entity import AnalysisEntity


class ABQFastenedConnectionEnhancement(ABQInteraction):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     ABQAutomationItf.ABQInteraction
                |                         ABQFastenedConnectionEnhancement
                | 
                | This interface has been deprecated.
                | Please use ABQFastenedPair instead.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.abq_fastened_connection_enhancement = com_object

    @property
    def adjust_slave_node(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property AdjustSlaveNode() As boolean
                | 
                |     Sets or returns the adjust slave node flag.

        :rtype: bool
        """

        return self.abq_fastened_connection_enhancement.AdjustSlaveNode

    @adjust_slave_node.setter
    def adjust_slave_node(self, value: bool):
        """
        :param bool value:
        """

        self.abq_fastened_connection_enhancement.AdjustSlaveNode = value

    @property
    def connection_property(self) -> AnalysisEntity:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ConnectionProperty() As AnalysisEntity
                | 
                |     Sets or returns the connection property.

        :rtype: AnalysisEntity
        """

        return AnalysisEntity(self.abq_fastened_connection_enhancement.ConnectionProperty)

    @connection_property.setter
    def connection_property(self, value: AnalysisEntity):
        """
        :param AnalysisEntity value:
        """

        self.abq_fastened_connection_enhancement.ConnectionProperty = value

    @property
    def formulation_option(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property FormulationOption() As FormulationOption_Type
                | 
                |     Sets or returns the formulation option.
                | 
                |     Returns:
                |         The formulation option.
                | 
                |         Legal values:
                | 
                |         SOLVERDEFAULT
                |         SURFACETOSURFACE
                |         NODETOSURFACE

        :return: enum formulation_option_type
        :rtype: int
        """

        return self.abq_fastened_connection_enhancement.FormulationOption

    @formulation_option.setter
    def formulation_option(self, value: int):
        """
        :param int value: enum formulation_option_type
        """

        self.abq_fastened_connection_enhancement.FormulationOption = value

    @property
    def include_shell_thickness(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property IncludeShellThickness() As boolean
                | 
                |     Sets or returns the include shell element thickness flag.

        :rtype: bool
        """

        return self.abq_fastened_connection_enhancement.IncludeShellThickness

    @include_shell_thickness.setter
    def include_shell_thickness(self, value: bool):
        """
        :param bool value:
        """

        self.abq_fastened_connection_enhancement.IncludeShellThickness = value

    @property
    def invert_master_surface(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property InvertMasterSurface() As boolean
                | 
                |     Sets or returns the invert master surface flag.

        :rtype: bool
        """

        return self.abq_fastened_connection_enhancement.InvertMasterSurface

    @invert_master_surface.setter
    def invert_master_surface(self, value: bool):
        """
        :param bool value:
        """

        self.abq_fastened_connection_enhancement.InvertMasterSurface = value

    @property
    def invert_slave_surface(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property InvertSlaveSurface() As boolean
                | 
                |     Sets or returns the invert slave surface flag.

        :rtype: bool
        """

        return self.abq_fastened_connection_enhancement.InvertSlaveSurface

    @invert_slave_surface.setter
    def invert_slave_surface(self, value: bool):
        """
        :param bool value:
        """

        self.abq_fastened_connection_enhancement.InvertSlaveSurface = value

    @property
    def position_tolerance(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property PositionTolerance() As PositionTolerance_Type
                | 
                |     Sets or returns the position tolerance.
                | 
                |     Returns:
                |         The position tolerance.
                | 
                |         Legal values:
                | 
                |         COMPUTED
                |         SPECIFIED

        :return: enum position_tolerance_type
        :rtype: int
        """

        return self.abq_fastened_connection_enhancement.PositionTolerance

    @position_tolerance.setter
    def position_tolerance(self, value: int):
        """
        :param int value: enum position_tolerance_type
        """

        self.abq_fastened_connection_enhancement.PositionTolerance = value

    @property
    def position_tolerance_val(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property PositionToleranceVal() As double
                | 
                |     Sets or returns the position tolerance value

        :rtype: float
        """

        return self.abq_fastened_connection_enhancement.PositionToleranceVal

    @position_tolerance_val.setter
    def position_tolerance_val(self, value: float):
        """
        :param float value:
        """

        self.abq_fastened_connection_enhancement.PositionToleranceVal = value

    @property
    def swap_master_slave(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property SwapMasterSlave() As boolean
                | 
                |     Sets or returns the swap master/slave surface flag.

        :rtype: bool
        """

        return self.abq_fastened_connection_enhancement.SwapMasterSlave

    @swap_master_slave.setter
    def swap_master_slave(self, value: bool):
        """
        :param bool value:
        """

        self.abq_fastened_connection_enhancement.SwapMasterSlave = value

    def __repr__(self):
        return f'ABQFastenedConnectionEnhancement(name="{self.name}")'
