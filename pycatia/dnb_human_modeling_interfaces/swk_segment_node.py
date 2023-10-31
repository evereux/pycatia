#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.dnb_human_modeling_interfaces.swk_segment import SWKSegment
from pycatia.system_interfaces.any_object import AnyObject


class SWKSegmentNode(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SWKSegmentNode
                | 
                | This interface characterizes a segment node.
                | 
                | A segment node is a convenient way to regroup segments. The segment nodes are
                | the entities that appear under the manikin in the specification tree, and that
                | regroup segments together (i.e. "Trunk", "Cervical", "Right
                | Fingers").
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.swk_segment_node = com_object

    @property
    def nb_children_nodes(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property NbChildrenNodes() As long (Read Only)
                | 
                |     Returns the number of children segment nodes under this node.

        :rtype: int
        """

        return self.swk_segment_node.NbChildrenNodes

    @property
    def nb_children_segments(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property NbChildrenSegments() As long (Read Only)
                | 
                |     Returns the number of children segments under this node.

        :rtype: int
        """

        return self.swk_segment_node.NbChildrenSegments

    def get_segment(self, pi_index: int) -> SWKSegment:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetSegment(long piIndex) As SWKSegment
                | 
                |     Returns a specific child of the segment node, based on an
                |     index.
                | 
                |     Parameters:
                | 
                |         piIndex
                |             The index of the segment to retrieve.
                |             The first segment is at index 0.
                |             The value of this parameter should not be higher than the number of
                |             segments on this segment node, minus 1.

        :param int pi_index:
        :rtype: SWKSegment
        """
        return SWKSegment(self.swk_segment_node.GetSegment(pi_index))

    def get_segment_node(self, pi_index: int) -> 'SWKSegmentNode':
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetSegmentNode(long piIndex) As SWKSegmentNode
                | 
                |     Returns a specific child of the segment node, based on an
                |     index.
                | 
                |     Parameters:
                | 
                |         piIndex
                |             The index of the segment node to retrieve.
                |             The first segment is at index 0.
                |             The value of this parameter should not be higher than the number of
                |             children nodes on this segment node, minus 1.

        :param int pi_index:
        :rtype: SWKSegmentNode
        """
        return SWKSegmentNode(self.swk_segment_node.GetSegmentNode(pi_index))

    def mirror_copy_posture(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub MirrorCopyPosture()
                | 
                |     Copy the posture on the equivalent segment node, on the other side of the
                |     manikin. For instance, it copies the posture from the right leg to the left
                |     leg.

        :rtype: None
        """
        return self.swk_segment_node.MirrorCopyPosture()

    def reset_posture(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub ResetPosture()
                | 
                |     Set the posture of all segment under this node back to their default
                |     position.

        :rtype: None
        """
        return self.swk_segment_node.ResetPosture()

    def swap_posture(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SwapPosture()
                | 
                |     Swap the posture with the equivalent segment node, on the other side of the
                |     manikin. For instance, the right leg takes the posture of the left leg, and
                |     vice versa.

        :rtype: None
        """
        return self.swk_segment_node.SwapPosture()

    def __repr__(self):
        return f'SWKSegmentNode(name="{self.name}")'
