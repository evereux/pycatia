#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.any_object import AnyObject


class PCBObject(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     PCBObject

    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.pcb_object = com_object

    @property
    def electronic_type(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ElectronicType() As CatElectronicType (Read Only)
                | 
                |     Allow to know if : a Product is a BOARD, a PANEL or a COMPONENT, a Hole is a PBD Hole
                |     a pattenr is a PCB pattern, a Pad is a constraint area.
                | 
                |     Parameters:
                | 
                |         oType
                |             This parameter is the type of the object ( BOARD, PANEL, COMPONENT )
                | 
                |     Returns:
                | 
                |             The result of the method:
                |             S_OK if succeeded
                |             E_FAIL if failed

        :return: enum cat_electronic_type
        :rtype: int
        """

        return self.pcb_object.ElectronicType

    def remove_electronic_behaviour(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub RemoveElectronicBehaviour()
                | 
                |     Allow to remove a PCB behaviour of an object
                | 
                |     Returns:
                | 
                |             The result of the method:
                |             S_OK if succeeded
                |             E_FAIL if failed

        :rtype: None
        """
        return self.pcb_object.RemoveElectronicBehaviour()

    def __repr__(self):
        return f'PCBObject(name="{self.name}")'
