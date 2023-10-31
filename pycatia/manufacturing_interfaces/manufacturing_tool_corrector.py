#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.any_object import AnyObject


class ManufacturingToolCorrector(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     ManufacturingToolCorrector
                | 
                | Manufacturing tool corrector.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.manufacturing_tool_corrector = com_object

    @property
    def diameter(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Diameter() As double (Read Only)
                | 
                |     Gives the corrector diameter tool diameter.
                |     Returns HRESULT.

        :rtype: float
        """

        return self.manufacturing_tool_corrector.Diameter

    @property
    def length_number(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property LengthNumber() As short (Read Only)
                | 
                |     Gives the corrector length number.
                |     Returns HRESULT.

        :rtype: int
        """

        return self.manufacturing_tool_corrector.LengthNumber

    @property
    def number(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Number() As short (Read Only)
                | 
                |     Gives the corrector number.
                |     Returns HRESULT.

        :rtype: int
        """

        return self.manufacturing_tool_corrector.Number

    @property
    def point(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Point() As CATBSTR (Read Only)
                | 
                |     Gives the corrector type point.
                |     oPoint : Type point (Ex: P1, ..., P9)
                |     Returns HRESULT.

        :rtype: str
        """

        return self.manufacturing_tool_corrector.Point

    @property
    def radius_number(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property RadiusNumber() As short (Read Only)
                | 
                |     Gives the corrector radius number.
                |     Returns HRESULT.

        :rtype: int
        """

        return self.manufacturing_tool_corrector.RadiusNumber

    def get_values(self) -> tuple:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetValues(CATBSTR oPoint,
                | short oNumber,
                | short oLengthNumber,
                | short oRadiusNumber,
                | double oDiameter)
                | 
                |     Gives the corrector values.
                |     oPoint : Type point (Ex: P1, ..., P9)
                |     oNumber : Corrector Number
                |     oLengthNumber : Corrector Length Number
                |     oRadiusNumber : Corrector Radius Number
                |     oDiameter : Tool Diameter where corrector applyes (if non fixed corrector)
                |     Returns HRESULT.

        :rtype: tuple
        """
        return self.manufacturing_tool_corrector.GetValues()

    def set_values(
            self,
            o_point: str,
            o_number: int,
            o_length_number: int,
            o_radius_number: int,
            o_diameter: float
    ) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetValues(CATBSTR oPoint,
                | short oNumber,
                | short oLengthNumber,
                | short oRadiusNumber,
                | double oDiameter)
                | 
                |     Defines the corrector values.
                |     iPoint : Type point (Ex: P1, ..., P9)
                |     iNumber : Corrector Number
                |     iLengthNumber : Corrector Length Number
                |     iRadiusNumber : Corrector Radius Number
                |     iDiameter : Tool Diameter where corrector applyes (if non fixed corrector)
                |     Returns HRESULT.

        :param str o_point:
        :param int o_number:
        :param int o_length_number:
        :param int o_radius_number:
        :param float o_diameter:
        :rtype: None
        """
        return self.manufacturing_tool_corrector.SetValues(
            o_point,
            o_number,
            o_length_number,
            o_radius_number,
            o_diameter
        )

    def __repr__(self):
        return f'ManufacturingToolCorrector(name="{self.name}")'
