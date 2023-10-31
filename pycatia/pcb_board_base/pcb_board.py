#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.part_interfaces.hole import Hole
from pycatia.part_interfaces.pad import Pad
from pycatia.part_interfaces.pattern import Pattern
from pycatia.system_interfaces.any_object import AnyObject


class PCBBoard(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     PCBBoard

    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.pcb_board = com_object

    @property
    def owner(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Owner() As CATBSTR
                | 
                |     Allow to get and set the attribute owner of a Panel or a Board The possible
                |     values are MCAD, ECAD, UNKNOWN
                | 
                |     Returns:
                | 
                |             The result of the method:
                |             S_OK if succeeded
                |             E_FAIL if failed

        :rtype: str
        """

        return self.pcb_board.Owner

    @owner.setter
    def owner(self, value: str):
        """
        :param str value:
        """

        self.pcb_board.Owner = value

    @property
    def part(self) -> Pad:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Part() As Pad
                | 
                |     set the pad of a Board or a component or a panel.

        :rtype: Pad
        """

        return Pad(self.pcb_board.Part)

    @part.setter
    def part(self, value: Pad):
        """
        :param Pad value:
        """

        self.pcb_board.Part = value

    def create_pcbhole(
            self,
            i_hole: Hole,
            iplating_style: str,
            i_associated_part_name: str,
            i_hole_type: str,
            i_hole_owner: str
    ) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub create_pcbhole(Hole iHole,
                | CATBSTR iplatingStyle,
                | CATBSTR iAssociatedPartName,
                | CATBSTR iHoleType,
                | CATBSTR iHoleOwner)
                | 
                |     This method allows to add a Pcb hole to a board or a
                |     panel.
                | 
                |     Parameters:
                | 
                |         iHole
                |             This parameter represents the hole to transform in Pcb hole
                |             
                |         iplatingStyle
                |             This parameter represents the plating style of the hole. The
                |             differents values are PTH or NPTH 
                |         iAssociatedPartName
                |             This parameter represents name of the associated part to the hole.
                |             The possible values are : the name of the instance of component in which the
                |             hole is defined.
                |             BOARD if the hole is defined in the Board part
                |             PANEL If the hole is defined in the Panel part
                |             NOREFDES is the hole is defined in a non Electronic Part.
                |         iHoleType
                |             This parameter represents the function of the hole. The
                |             differents values are :
                |             PIN if the hole is associated with a component pin
                |             VIA if the hole is associated with a conductive via
                |             MTG if the hole is used for mounting purposes
                |             TOOL if the hole is used for tooling purposes Other ( User defined )
                |         iHoleOwner
                |             The parameter represents the owner of the hole.
                |             The possible values are : MCAD, ECAD, UNOWNED
                | 
                |     Returns:
                | 
                |             The result of the method:
                |             S_OK if succeeded
                |             E_FAIL if failed

        :param Hole i_hole:
        :param str iplating_style:
        :param str i_associated_part_name:
        :param str i_hole_type:
        :param str i_hole_owner:
        :rtype: None
        """
        return self.pcb_board.create_pcbhole(
            i_hole.com_object,
            iplating_style,
            i_associated_part_name,
            i_hole_type,
            i_hole_owner
        )
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'create_pcbhole'
        # # vba_code = """
        # # Public Function create_pcbhole(pcb_board)
        # #     Dim iHole (2)
        # #     pcb_board.create_pcbhole iHole
        # #     create_pcbhole = iHole
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def create_pcbpattern(
            self,
            i_pattern: Pattern,
            iplating_style: str,
            i_associated_part_name: str,
            i_hole_type: str,
            i_hole_owner: str
    ) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub create_pcbpattern(Pattern iPattern,
                | CATBSTR iplatingStyle,
                | CATBSTR iAssociatedPartName,
                | CATBSTR iHoleType,
                | CATBSTR iHoleOwner)
                | 
                |     This method allows to add a Pcb pattern of hole to a board or a panel. If
                |     the motif hole of the pattern is pcb hole, the input value are not taken into
                |     account
                | 
                |     Parameters:
                | 
                |         iPattern
                |             This parameter represents the Pattern to transform in Pcb Pattern
                |             
                |         iplatingStyle
                |             This parameter represents the plating style of the hole. The
                |             differents values are PTH or NPTH 
                |         iAssociatedPartName
                |             This parameter represents name of the associated part to the hole.
                |             The possible values are : the name of the instance of component in which the hole is defined.
                |             BOARD if the hole is defined in the Board part
                |             PANEL If the hole is defined in the Panel part
                |             NOREFDES is the hole is defined in a non Electronic Part.
                |         iHoleType
                |             This parameter represents the function of the hole. The differents values are :
                |             PIN if the hole is associated with a component pin
                |             VIA if the hole is associated with a conductive via
                |             MTG if the hole is used for mounting purposes
                |             TOOL if the hole is used for tooling purposes Other ( User defined )
                |         iHoleOwner
                |             The parameter represents the owner of the hole.
                |             The possible values are : MCAD, ECAD, UNOWNED
                | 
                |     Returns:
                | 
                |             The result of the method:
                |             S_OK if succeeded
                |             E_FAIL if failed

        :param Pattern i_pattern:
        :param str iplating_style:
        :param str i_associated_part_name:
        :param str i_hole_type:
        :param str i_hole_owner:
        :rtype: None
        """
        return self.pcb_board.create_pcbpattern(
            i_pattern.com_object,
            iplating_style,
            i_associated_part_name,
            i_hole_type,
            i_hole_owner
        )
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'create_pcbpattern'
        # # vba_code = """
        # # Public Function create_pcbpattern(pcb_board)
        # #     Dim iPattern (2)
        # #     pcb_board.create_pcbpattern iPattern
        # #     create_pcbpattern = iPattern
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def create_zone(self, zonetype: str, i_pad: Pad) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub create_zone(CATBSTR zonetype,
                | Pad iPad)
                | 
                |     This method allows to add a constraint area to a board.
                | 
                |     Parameters:
                | 
                |         zonetype
                |             This parameter represents the type of the zone to create The
                |             differents values are ROUTE_OUTLINE, PLACE_OUTLINE, OTHER_OUTLINE, VIA_KEEPOUT,
                |             PLACE_KEEPOUT, PLACE_REGION, ROUTE_KEEPOUT 
                | 
                |     Returns:
                | 
                |             The result of the method:
                |             S_OK if succeeded
                |             E_FAIL if failed

        :param str zonetype:
        :param Pad i_pad:
        :rtype: None
        """
        return self.pcb_board.create_zone(zonetype, i_pad.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'create_zone'
        # # vba_code = """
        # # Public Function create_zone(pcb_board)
        # #     Dim zonetype (2)
        # #     pcb_board.create_zone zonetype
        # #     create_zone = zonetype
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'PCBBoard(name="{self.name}")'
