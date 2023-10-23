#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from typing import TYPE_CHECKING

from pycatia.system_interfaces.any_object import AnyObject

if TYPE_CHECKING:
    from pycatia.dnb_human_modeling_interfaces.swk_manikin import SWKManikin


class SWKBodyElement(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SWKBodyElement
                | 
                | This interface is used to access a body element (segment, ellipse,
                | ...) It provides common services for all body elements of the
                | manikin.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.swk_body_element = com_object

    @property
    def full_name(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property FullName() As CATBSTR (Read Only)
                | 
                |     Returns the full name of the body element.
                |     This property is different from the property
                |     Name of AnyObject,
                |     which gives the short name or abbreviated name
                |     of the body element.
                | 
                |     For instance, if the body element in question is
                |     the left leg segment, then property Name
                |     yields "LSLeLe", whereas
                |     property FullName yields the character
                |     string "Left Leg".

        :rtype: str
        """

        return self.swk_body_element.FullName

    @property
    def manikin(self) -> 'SWKManikin':
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Manikin() As SWKManikin (Read Only)
                | 
                |     Returns the manikin which owns this body element.

        :rtype: SWKManikin
        """
        
        from pycatia.dnb_human_modeling_interfaces.swk_manikin import SWKManikin
        return SWKManikin(self.swk_body_element.Manikin)

    @property
    def position_x(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property PositionX() As double (Read Only)
                | 
                |     Returns the x coordinate of the position of the body
                |     element.
                |     If this body element is the body, then the position returned is
                |     the x-coordinate of global position of the manikin. If the
                |     body element is a segment or a line of sight, the position
                |     returned is the x-coordinate of the beginning of that segment
                |     or line of sight. If the body element is an ellipse, the
                |     x-coordinate of the center of that ellipse is returned.

        :rtype: float
        """

        return self.swk_body_element.PositionX

    @property
    def position_y(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property PositionY() As double (Read Only)
                | 
                |     Returns the y coordinate of the position of the body
                |     element.
                |     If this body element is the body, then the position returned is
                |     the y-coordinate of global position of the manikin. If the
                |     body element is a segment or a line of sight, the position
                |     returned is the y-coordinate of the beginning of that segment
                |     or line of sight. If the body element is an ellipse, the
                |     y-coordinate of the center is returned.

        :rtype: float
        """

        return self.swk_body_element.PositionY

    @property
    def position_z(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property PositionZ() As double (Read Only)
                | 
                |     Returns the z coordinate of the position of the body
                |     element.
                |     If this body element is the body, then the position returned is
                |     the z-coordinate of global position of the manikin. If the
                |     body element is a segment or a line of sight, the position
                |     returned is the z-coordinate of the beginning of that segment
                |     or line of sight. If the body element is an ellipse, the
                |     z-coordinate of the center is returned.

        :rtype: float
        """

        return self.swk_body_element.PositionZ

    @property
    def refresh_display(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property RefreshDisplay() As boolean
                | 
                |     Enables or disables the update of the display during the
                |     script replay.
                |     To improve performance, this update can be temporarily
                |     disabled by setting this property to False in the script.
                | 
                |     The property is True if the elements display is refreshed after each
                |     posture change (value set by default).
                | 
                |     Example:
                |         This example makes the update of a manikin display disabled during a
                |         portion of the script replay.
                | 
                |          myManikin.Body.RefreshDisplay = False

        :rtype: bool
        """

        return self.swk_body_element.RefreshDisplay

    @refresh_display.setter
    def refresh_display(self, value: bool):
        """
        :param bool value:
        """

        self.swk_body_element.RefreshDisplay = value

    def get_global_position(self, po_global_position: tuple) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetGlobalPosition(CATSafeArrayVariant
                | poGlobalPosition)
                | 
                |     Returns the global position ofthe body element.
                |     If this body element is the body, then the position returned
                |     is the global position of the manikin. If the
                |     body element is a segment or a line of sight, the position
                |     returned is the global position of the beginning of that segment
                |     or line of sight. If the body element is an ellipse, the global
                |     position of the center of that ellipse is returned.

        :param tuple po_global_position:
        :rtype: None
        """
        return self.swk_body_element.GetGlobalPosition(po_global_position)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_global_position'
        # # vba_code = """
        # # Public Function get_global_position(swk_body_element)
        # #     Dim poGlobalPosition (2)
        # #     swk_body_element.GetGlobalPosition poGlobalPosition
        # #     get_global_position = poGlobalPosition
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def refresh_3d(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub Refresh3D()
                | 
                |     Refreshes the 3D representation of the current element.

        :rtype: None
        """
        return self.swk_body_element.Refresh3D()

    def __repr__(self):
        return f'SWKBodyElement(name="{self.name}")'
