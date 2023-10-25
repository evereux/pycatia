#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from typing import TYPE_CHECKING

from pycatia.in_interfaces.move import Move
from pycatia.in_interfaces.position import Position
from pycatia.navigator_interfaces.group import Group
from pycatia.system_interfaces.any_object import AnyObject

if TYPE_CHECKING:
    from pycatia.fitting_interfaces.shuttles import Shuttles


class Shuttle(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     Shuttle
                | 
                | The interface to access a CATIAShuttle.
                | Role: The shuttle object is used to define a grouping of products. Once
                | products have been placed in the shuttle then they can be moved all at once.
                | Also the shuttle has a base location defined by the shuttle
                | axis.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.shuttle = com_object

    @property
    def angle_limit(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property AngleLimit() As double
                | 
                |     Returns/Stores the angle limit attribute. Role:/b> Retrieves/stores the
                |     shuttle's angle limit attribute.

        :rtype: float
        """

        return self.shuttle.AngleLimit

    @angle_limit.setter
    def angle_limit(self, value: float):
        """
        :param float value:
        """

        self.shuttle.AngleLimit = value

    @property
    def angle_validation(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property AngleValidation() As boolean
                | 
                |     Returns/Stores the angle validation attribute. Role:/b> Retrieves/stores
                |     the shuttle's angle validation attribute.

        :rtype: bool
        """

        return self.shuttle.AngleValidation

    @angle_validation.setter
    def angle_validation(self, value: bool):
        """
        :param bool value:
        """

        self.shuttle.AngleValidation = value

    @property
    def group(self) -> Group:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Group() As Group
                | 
                |     Returns or sets the associated group object. Role:/b> Retrieves/stores the
                |     objects within the shuttle as a group, that is a CATIAGroup.

        :rtype: Group
        """

        return Group(self.shuttle.Group)

    @group.setter
    def group(self, value: Group):
        """
        :param Group value:
        """

        self.shuttle.Group = value

    @property
    def move(self) -> Move:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Move() As Move (Read Only)
                | 
                |     Returns the shuttle's move object. The move object is aggregated by the
                |     shuttle object and itself aggregates a movable object to which you can apply a
                |     move transformation by means of an isometry matrix. It moves your shuttle
                |     according to this isometry.
                | 
                |     Example:
                | 
                |           This example retrieves the move object for the
                |          Engine shuttle.
                |          
                | 
                |          Dim EngineMoveObject As Move
                |          Set EngineMoveObject = Engine.Move

        :rtype: Move
        """

        return Move(self.shuttle.Move)

    @property
    def move_mode(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property MoveMode() As CatShuttleMoveMode
                | 
                |     Returns/Stores the shuttle move mode. Role:/b> Retrieves/stores the shuttle
                |     move mode. This can be either shuttle mode (to move the shuttle) or axis mode
                |     (to simply move the shuttle axis).

        :return: enum cat_shuttle_move_mode
        :rtype: int
        """

        return self.shuttle.MoveMode

    @move_mode.setter
    def move_mode(self, value: int):
        """
        :param int value: enum cat_shuttle_move_mode
        """

        self.shuttle.MoveMode = value

    @property
    def position(self) -> Position:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Position() As Position (Read Only)
                | 
                |     Returns the shuttle's position object. The position object is the object
                |     aggregated by the ahuttle object that holds the position of the shuttle in the
                |     space.
                | 
                |     Example:
                | 
                |           This example retrieves the position object for the
                |          Engine shuttle.
                |          
                | 
                |          Dim EnginePositionObject As Position
                |          Set EnginePositionObject = Engine.Position

        :rtype: Position
        """

        return Position(self.shuttle.Position)

    @property
    def reference(self) -> AnyObject:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Reference() As CATBaseDispatch
                | 
                |     Returns or sets the associated reference object. Role:/b> Retrieves/stores
                |     the shuttle's reference object.

        :rtype: AnyObject
        """

        return AnyObject(self.shuttle.Reference)

    @reference.setter
    def reference(self, value: AnyObject):
        """
        :param AnyObject value:
        """

        self.shuttle.Reference = value

    @property
    def sub_shuttles(self) -> 'Shuttles':
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property SubShuttles() As Shuttles (Read Only)
                | 
                |     Returns any shuttles that are contained within the current shuttle.
                |     Role:/b> Returns any shuttles that are contained within the current shuttle.

        :rtype: Shuttles
        """

        from pycatia.fitting_interfaces.shuttles import Shuttles
        return Shuttles(self.shuttle.SubShuttles)

    @property
    def vector(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Vector() As CatShuttleVector
                | 
                |     Returns/Stores the validation vector attribute. Role:/b> Retrieves/stores
                |     the validation vector attribute.

        :return: enum cat_shuttle_vector
        :rtype: int
        """

        return self.shuttle.Vector

    @vector.setter
    def vector(self, value: int):
        """
        :param int value: enum cat_shuttle_vector
        """

        self.shuttle.Vector = value

    def __repr__(self):
        return f'Shuttle(name="{self.name}")'
