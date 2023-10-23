#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.any_object import AnyObject


class PCBArea(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     PCBArea

    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.pcb_area = com_object

    @property
    def area_type(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property AreaType() As CATBSTR (Read Only)
                | 
                |     Allow to get the Type of a constraint area The possible values are : ROUTE_OUTLINE,
                | 
                |     Returns:
                | 
                |             The result of the method:
                |             S_OK if succeeded
                |             E_FAIL if failed

        :rtype: str
        """

        return self.pcb_area.AreaType

    @property
    def height_max(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Heightmax() As double
                | 
                |     Allow to get and set the Height max of the constraint area This property is
                |     valid for the following constraints areas: OTHER_OUTLINE,
                |     PLACE_REGION
                | 
                |     Returns:
                | 
                |             The result of the method:
                |             S_OK if succeeded
                |             E_FAIL if failed

        :rtype: float
        """

        return self.pcb_area.Heightmax

    @height_max.setter
    def height_max(self, value: float):
        """
        :param float value:
        """

        self.pcb_area.Heightmax = value

    @property
    def height_min(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Heightmin() As double
                | 
                |     Allow to get and set the Height min of the constraint area This property is
                |     valid for the following constraints areas: PLACE_KEEPOUT
                | 
                |     Returns:
                | 
                |             The result of the method:
                |             S_OK if succeeded
                |             E_FAIL if failed

        :rtype: float
        """

        return self.pcb_area.Heightmin

    @height_min.setter
    def height_min(self, value: float):
        """
        :param float value:
        """

        self.pcb_area.Heightmin = value

    @property
    def identifier(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Identifier() As CATBSTR
                | 
                |     Allow to get and set the Identifier of the constraint area This property is
                |     valid for the following constraints areas: OTHER_OUTLINE,
                |     PLACE_REGION
                | 
                |     Returns:
                | 
                |             The result of the method:
                |             S_OK if succeeded
                |             E_FAIL if failed

        :rtype: str
        """

        return self.pcb_area.Identifier

    @identifier.setter
    def identifier(self, value: str):
        """
        :param str value:
        """

        self.pcb_area.Identifier = value

    @property
    def layer(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property LAYER() As CATBSTR (Read Only)
                | 
                |     Allow to get the position of a hole The possible values are :
                |     TOP,BOTTOM,BOTH,INNER,ALL It depends on the the type of the constraints
                |     area according to the IDF format This property is valid for the following
                |     constraints areas:
                |     OTHER_OUTLINE,
                |     ROUTING_OUTLINE,
                |     PLACE_OUTLINE,
                |     ROUTE_KEEPOUT,
                |     PLACE_KEEPOUT,
                |     PLACE_REGION,
                | 
                |     Returns:
                | 
                |             The result of the method:
                |             S_OK if succeeded
                |             E_FAIL if failed

        :rtype: str
        """

        return self.pcb_area.LAYER

    @property
    def owner(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property OWNER() As CATBSTR
                | 
                |     Allow to get and set the OWNER of the constraint area The possible value
                |     are MCAD,ECAD, UNOWNED
                | 
                |     Returns:
                | 
                |             The result of the method:
                |             S_OK if succeeded
                |             E_FAIL if failed

        :rtype: str
        """

        return self.pcb_area.OWNER

    @owner.setter
    def owner(self, value: str):
        """
        :param str value:
        """

        self.pcb_area.OWNER = value

    def __repr__(self):
        return f'PCBArea(name="{self.name}")'
