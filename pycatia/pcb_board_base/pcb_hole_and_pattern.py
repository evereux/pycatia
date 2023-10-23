#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.any_object import AnyObject


class PCBHoleAndPattern(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     PCBHoleAndPattern

    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.pcb_hole_and_pattern = com_object

    @property
    def associated_part_name(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property AssociatedPartName() As CATBSTR
                | 
                |     Allow to get and set the Associated Part of a hole
                |     The possible values are : the name of the instance of component in which the hole is defined.
                |     BOARD if the hole is defined in the Board part
                |     PANEL If the hole is defined in the Panel part
                |     NOREFDES is the hole is defined in a non Electronic Part.
                | 
                |     Returns:
                | 
                |             The result of the method:
                |             S_OK if succeeded
                |             E_FAIL if failed

        :rtype: str
        """

        return self.pcb_hole_and_pattern.AssociatedPartName

    @associated_part_name.setter
    def associated_part_name(self, value: str):
        """
        :param str value:
        """

        self.pcb_hole_and_pattern.AssociatedPartName = value

    @property
    def hole_owner(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property HoleOwner() As CATBSTR
                | 
                |     Allow to get and set the Operating power rating of a component The possible
                |     value are MCAD,ECAD, UNOWNED
                | 
                |     Returns:
                | 
                |             The result of the method:
                |             S_OK if succeeded
                |             E_FAIL if failed

        :rtype: str
        """

        return self.pcb_hole_and_pattern.HoleOwner

    @hole_owner.setter
    def hole_owner(self, value: str):
        """
        :param str value:
        """

        self.pcb_hole_and_pattern.HoleOwner = value

    @property
    def hole_type(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property HoleType() As CATBSTR
                | 
                |     Allow to get and set the function of the hole The different values are :
                |     PIN if the hole is associated with a component pin
                |     VIA if the hole is associated with a conductive via
                |     MTG if the hole is used for mounting purposes
                |     TOOL if the hole is used for tooling purposes Other ( User defined )
                | 
                |     Returns:
                | 
                |             The result of the method:
                |             S_OK if succeeded
                |             E_FAIL if failed

        :rtype: str
        """

        return self.pcb_hole_and_pattern.HoleType

    @hole_type.setter
    def hole_type(self, value: str):
        """
        :param str value:
        """

        self.pcb_hole_and_pattern.HoleType = value

    @property
    def plating_style(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property PlatingStyle() As CATBSTR
                | 
                |     Allow to get and set the Plating Style of a hole The possible values are : PTH, NPTH
                | 
                |     Returns:
                | 
                |             The result of the method:
                |             S_OK if succeeded
                |             E_FAIL if failed

        :rtype: str
        """

        return self.pcb_hole_and_pattern.PlatingStyle

    @plating_style.setter
    def plating_style(self, value: str):
        """
        :param str value:
        """

        self.pcb_hole_and_pattern.PlatingStyle = value

    def __repr__(self):
        return f'PCBHoleAndPattern(name="{self.name}")'
