#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from typing import TYPE_CHECKING

from pycatia.dnb_human_modeling_interfaces.swk_anthro import SWKAnthro
from pycatia.dnb_human_modeling_interfaces.swk_ergo import SWKErgo
from pycatia.dnb_human_modeling_interfaces.swk_line_of_sight_node import SWKLineOfSightNode
from pycatia.dnb_human_modeling_interfaces.swk_manikin_part import SWKManikinPart
from pycatia.dnb_human_modeling_interfaces.swk_node import SWKNode
from pycatia.dnb_human_modeling_interfaces.swk_segment_node import SWKSegmentNode
from pycatia.dnb_human_modeling_interfaces.swk_vision import SWKVision
from pycatia.in_interfaces.move import Move

if TYPE_CHECKING:
    from pycatia.dnb_human_modeling_interfaces.swk_body import SWKBody
    from pycatia.dnb_human_modeling_interfaces.swkik_manager import SWKIKManager


class SWKManikin(SWKManikinPart):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     DNBHumanModelingInterfaces.SWKManikinPart
                |                         SWKManikin
                | 
                | This interface groups the methods directly related to the definition of a
                | manikin.
                | 
                | Its main purpose is to provide bridges to the other interfaces related to a
                | manikin.
                | Once these interfaces are recovered, it is possible to have access to their
                | specific functionalities.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.swk_manikin = com_object

    @property
    def anthro(self) -> SWKAnthro:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Anthro() As SWKAnthro (Read Only)
                | 
                |     Returns the anthropometry of the current manikin. The anthropometry can
                |     also be obtained by invoking method GetItem (from AnyObject) with the character
                |     string "Anthro" as an argument.

        :rtype: SWKAnthro
        """

        return SWKAnthro(self.swk_manikin.Anthro)

    @property
    def body(self) -> 'SWKBody':
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Body() As SWKBody (Read Only)
                | 
                |     Returns the body of the current manikin. The body can also be obtained by
                |     invoking method GetItem (from AnyObject) with the character string "Body" as an
                |     argument.

        :rtype: SWKBody
        """

        from pycatia.dnb_human_modeling_interfaces.swk_body import SWKBody
        return SWKBody(self.swk_manikin.Body)

    @property
    def body_node(self) -> SWKSegmentNode:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property BodyNode() As SWKSegmentNode (Read Only)
                | 
                |     Returns the body node of the current manikin. The body node is the node
                |     named "Body", as it appears underneath the manikin in the specification tree.
                |     This body node can also be obtained by invoking method GetItem (from AnyObject)
                |     with the character string "BodyNode" as an argument.

        :rtype: SWKSegmentNode
        """

        return SWKSegmentNode(self.swk_manikin.BodyNode)

    @property
    def ergo(self) -> SWKErgo:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Ergo() As SWKErgo (Read Only)
                | 
                |     Returns the ergonomic analysis of the current manikin. The ergo can also be
                |     obtained by invoking method GetItem (from AnyObject) with the character string
                |     "Ergo" as an argument.

        :rtype: SWKErgo
        """

        return SWKErgo(self.swk_manikin.Ergo)

    @property
    def ik_manager(self) -> 'SWKIKManager':
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property IKManager() As SWKIKManager (Read Only)
                | 
                |     Returns the inverse kinematics (IK) engine of the current manikin. The IK
                |     manager can also be obtained by invoking method GetItem (from AnyObject) with
                |     the character string "IKManager" as an argument.

        :rtype: SWKIKManager
        """
        
        from pycatia.dnb_human_modeling_interfaces.swkik_manager import SWKIKManager
        return SWKIKManager(self.swk_manikin.IKManager)

    @property
    def line_of_sight_node(self) -> SWKLineOfSightNode:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property LineOfSightNode() As SWKLineOfSightNode (Read
                | Only)
                | 
                |     Returns the Line of sight node of the current manikin. The Line of sight
                |     node can also be obtained by invoking method GetItem (from AnyObject) with the
                |     character string "LineOfSightNode" as an argument.

        :rtype: SWKLineOfSightNode
        """

        return SWKLineOfSightNode(self.swk_manikin.LineOfSightNode)

    @property
    def move(self) -> Move:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Move() As Move (Read Only)
                | 
                |     Returns the manikin's move object. The move object is aggregated by the
                |     manikin object and itself aggregates a movable object to which you can apply a
                |     move transformation by means of an isometry matrix. It moves the manikin's
                |     representation according to this isometry.
                | 
                |     Example:
                | 
                |           This example retrieves the move object for the manikin myManikin.
                |
                |          Dim myManikinMoveObject As Move
                |          Set myManikinMoveObject = myManikin.Move

        :rtype: Move
        """

        return Move(self.swk_manikin.Move)

    @property
    def profiles_node(self) -> SWKNode:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ProfilesNode() As SWKNode (Read Only)
                | 
                |     Returns the Profiles node of the current manikin. The Profiles node can
                |     also be obtained by invoking method GetItem (from AnyObject) with the character
                |     string "ProfilesNode" as an argument.

        :rtype: SWKNode
        """

        return SWKNode(self.swk_manikin.ProfilesNode)

    @property
    def settings_node(self) -> SWKNode:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property SettingsNode() As SWKNode (Read Only)
                | 
                |     Returns the settings node of the current manikin. The Settings node can
                |     also be obtained by invoking method GetItem (from AnyObject) with the character
                |     string "SettingsNode" as an argument.

        :rtype: SWKNode
        """

        return SWKNode(self.swk_manikin.SettingsNode)

    @property
    def vision(self) -> SWKVision:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Vision() As SWKVision (Read Only)
                | 
                |     Returns the vision of the current manikin. The vision can also be obtained
                |     by invoking method GetItem (from AnyObject) with the character string "Vision"
                |     as an argument.

        :rtype: SWKVision
        """

        return SWKVision(self.swk_manikin.Vision)

    def __repr__(self):
        return f'SWKManikin(name="{self.name}")'
