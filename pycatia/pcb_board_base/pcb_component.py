#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.any_object import AnyObject


class PCBComponent(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     PCBComponent

    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.pcb_component = com_object

    @property
    def capacitance(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property CAPACITANCE() As CATBSTR
                | 
                |     Allow to get and set the CAPACITANCE Type of a component.
                | 
                |     Returns:
                | 
                |             The result of the method:
                |             S_OK if succeeded
                |             E_FAIL if failed

        :rtype: str
        """

        return self.pcb_component.CAPACITANCE

    @capacitance.setter
    def capacitance(self, value: str):
        """
        :param str value:
        """

        self.pcb_component.CAPACITANCE = value

    @property
    def power_opr(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property POWEROPR() As CATBSTR
                | 
                |     Allow to get and set the Operating power rating of a component The possible
                |     value are MECHANICAL or ELECTRICAL
                | 
                |     Returns:
                | 
                |             The result of the method:
                |             S_OK if succeeded
                |             E_FAIL if failed

        :rtype: str
        """

        return self.pcb_component.POWEROPR

    @power_opr.setter
    def power_opr(self, value: str):
        """
        :param str value:
        """

        self.pcb_component.POWEROPR = value

    @property
    def power_max(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property POWER_MAX() As CATBSTR
                | 
                |     Allow to get and set the POWER MAX of a component.
                | 
                |     Returns:
                | 
                |             The result of the method:
                |             S_OK if succeeded
                |             E_FAIL if failed

        :rtype: str
        """

        return self.pcb_component.POWER_MAX

    @power_max.setter
    def power_max(self, value: str):
        """
        :param str value:
        """

        self.pcb_component.POWER_MAX = value

    @property
    def package_number(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property PackageNumber() As CATBSTR
                | 
                |     Allow to get and set the Package number of a component
                | 
                |     Returns:
                | 
                |             The result of the method:
                |             S_OK if succeeded
                |             E_FAIL if failed

        :rtype: str
        """

        return self.pcb_component.PackageNumber

    @package_number.setter
    def package_number(self, value: str):
        """
        :param str value:
        """

        self.pcb_component.PackageNumber = value

    @property
    def resistance(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property RESISTANCE() As CATBSTR
                | 
                |     Allow to get and set the RESISTANCE of a component.
                | 
                |     Returns:
                | 
                |             The result of the method:
                |             S_OK if succeeded
                |             E_FAIL if failed

        :rtype: str
        """

        return self.pcb_component.RESISTANCE

    @resistance.setter
    def resistance(self, value: str):
        """
        :param str value:
        """

        self.pcb_component.RESISTANCE = value

    @property
    def therm_cond(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property THERM_COND() As CATBSTR
                | 
                |     Allow to get and set the thermal conductivity of a
                |     component.
                | 
                |     Returns:
                | 
                |             The result of the method:
                |             S_OK if succeeded
                |             E_FAIL if failed

        :rtype: str
        """

        return self.pcb_component.THERM_COND

    @therm_cond.setter
    def therm_cond(self, value: str):
        """
        :param str value:
        """

        self.pcb_component.THERM_COND = value

    @property
    def theta_jb(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property THETA_JB() As CATBSTR
                | 
                |     Allow to get and set the junction to board thermal resistance of a
                |     component.
                | 
                |     Returns:
                | 
                |             The result of the method:
                |             S_OK if succeeded
                |             E_FAIL if failed

        :rtype: str
        """

        return self.pcb_component.THETA_JB

    @theta_jb.setter
    def theta_jb(self, value: str):
        """
        :param str value:
        """

        self.pcb_component.THETA_JB = value

    @property
    def theta_jc(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property THETA_JC() As CATBSTR
                | 
                |     Allow to get and set the junction to case thermal resistance of a
                |     component.
                | 
                |     Returns:
                | 
                |             The result of the method:
                |             S_OK if succeeded
                |             E_FAIL if failed

        :rtype: str
        """

        return self.pcb_component.THETA_JC

    @theta_jc.setter
    def theta_jc(self, value: str):
        """
        :param str value:
        """

        self.pcb_component.THETA_JC = value

    @property
    def tolerance(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property TOLERANCE() As CATBSTR
                | 
                |     Allow to get and set the TOLERANCE of a component.
                | 
                |     Returns:
                | 
                |             The result of the method:
                |             S_OK if succeeded
                |             E_FAIL if failed

        :rtype: str
        """

        return self.pcb_component.TOLERANCE

    @tolerance.setter
    def tolerance(self, value: str):
        """
        :param str value:
        """

        self.pcb_component.TOLERANCE = value

    def __repr__(self):
        return f'PCBComponent(name="{self.name}")'
