#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.abq_automation_interfaces.abq_property import ABQProperty


class ABQThermalConnBehavior(ABQProperty):
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
                |                         ABQThermalConnBehavior
                | 
                | Represents an Abaqus thermal connection behavior (ABQThermalConnBehavior)
                | object.
                | Role: Access an Abaqus thermal connection behaviour object or determine its
                | properties.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.abq_thermal_conn_behavior = com_object

    @property
    def conductance_table_size(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ConductanceTableSize() As long (Read Only)
                | 
                |     Returns the size of the conductance table.
                | 
                |     Returns:
                |         The size of the conductance table.

        :return: int
        :rtype: int
        """

        return self.abq_thermal_conn_behavior.ConductanceTableSize

    @property
    def description(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Description() As CATBSTR
                | 
                |     Sets or returns the description.
                | 
                |     Returns:
                |         The description of the step.

        :return: str
        :rtype: str
        """

        return self.abq_thermal_conn_behavior.Description

    @description.setter
    def description(self, value: str):
        """
        :param str value:
        """

        self.abq_thermal_conn_behavior.Description = value

    @property
    def temperature_dependency(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property temperatureDependency() As boolean
                | 
                |     Sets or returns the temperature dependency.
                | 
                |     Returns:
                |         A boolean specifying whether the values are dependent on temperature.

        :return: bool
        :rtype: bool
        """

        return self.abq_thermal_conn_behavior.temperatureDependency

    @temperature_dependency.setter
    def temperature_dependency(self, value: bool):
        """
        :param bool value:
        """

        self.abq_thermal_conn_behavior.temperatureDependency = value

    def add_gap_conduction_table(self, i_conductance: tuple, i_clearance: tuple, i_temperature: tuple) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub AddGapConductionTable(CATSafeArrayVariant
                | iConductance,
                | CATSafeArrayVariant iClearance,
                | CATSafeArrayVariant iTemperature)
                | 
                |     Adds a gap-conductance table using three lists containing gap, conductance,
                |     and temperature values. Temperature list will be ignored if the temperature
                |     dependency is OFF. The number of values in all of the parameter lists must
                |     match. If either list contains extra values, the extra values are
                |     discarded.
                | 
                |     Parameters:
                | 
                |         iConductance
                |             The list of conductance values (in W/degK/m^2).
                |         iClearance
                |             The list of clearance values (in meter).
                |         iTemperature
                |             The list of temperature values (in degK).

        :param tuple i_conductance:
        :param tuple i_clearance:
        :param tuple i_temperature:
        :return: None
        :rtype: None
        """
        return self.abq_thermal_conn_behavior.AddGapConductionTable(i_conductance, i_clearance, i_temperature)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'add_gap_conduction_table'
        # # vba_code = """
        # # Public Function add_gap_conduction_table(abq_thermal_conn_behavior)
        # #     Dim iConductance (2)
        # #     abq_thermal_conn_behavior.AddGapConductionTable iConductance
        # #     add_gap_conduction_table = iConductance
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_gap_conduction_table(self, o_conductance: tuple, o_clearance: tuple, o_temperature: tuple) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetGapConductionTable(CATSafeArrayVariant
                | oConductance,
                | CATSafeArrayVariant oClearance,
                | CATSafeArrayVariant oTemperature)
                | 
                |     Returns list(s) containing gap, conductance, and temperature
                |     values.
                | 
                |     Returns:
                |         The lists of gap, conductance, and temperature values. The list of
                |         temperature values will be ignored if the temperature dependency is OFF.
                |         
                |     Parameters:
                | 
                |         oConductance
                |             The list of conductance values (in W/degK/m^2).
                |         oClearance
                |             The list of clearance values (in mm).
                |         oTemperature
                |             The list of temperature values (in degK).

        :param tuple o_conductance:
        :param tuple o_clearance:
        :param tuple o_temperature:
        :return: None
        :rtype: None
        """
        return self.abq_thermal_conn_behavior.GetGapConductionTable(o_conductance, o_clearance, o_temperature)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_gap_conduction_table'
        # # vba_code = """
        # # Public Function get_gap_conduction_table(abq_thermal_conn_behavior)
        # #     Dim oConductance (2)
        # #     abq_thermal_conn_behavior.GetGapConductionTable oConductance
        # #     get_gap_conduction_table = oConductance
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'ABQThermalConnBehavior(name="{self.name}")'
