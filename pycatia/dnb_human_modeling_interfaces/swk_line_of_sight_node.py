#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.any_object import AnyObject


class SWKLineOfSightNode(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SWKLineOfSightNode
                | 
                | This interface characterizes a node.
                | 
                | A node is a convenient way to regroup different attributes of the
                | manikin.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.swk_line_of_sight_node = com_object

    def lock_posture(self, pi_dof_id: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub LockPosture(long piDOFId)
                | 
                |     Lock the posture of the line of sight for the dof piDOFId.

        :param int pi_dof_id:
        :rtype: None
        """
        return self.swk_line_of_sight_node.LockPosture(pi_dof_id)

    def optimize(self, pi_dof_id: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub Optimize(long piDOFId)
                | 
                |     Sets the limits to match the best PrefAngle for the DOF piDOFId

        :param int pi_dof_id:
        :rtype: None
        """
        return self.swk_line_of_sight_node.Optimize(pi_dof_id)

    def reset_angular_limitations(self, pi_dof_id: int, pi_reset: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub ResetAngularLimitations(long piDOFId,
                | long piReset)
                | 
                |     Reset the angular limitations of the line of sight depending on piReset: 0
                |     -> 2 OR 3 OR 4 depending of the first encountered. 1 -> 2 AND 3 AND 4 2 ->
                |     Unlock the value 3 -> Restore the angular limitations if it is "No Limits" 4 ->
                |     Set back the angular limitations to their default value (50.0%)

        :param int pi_dof_id:
        :param int pi_reset:
        :rtype: None
        """
        return self.swk_line_of_sight_node.ResetAngularLimitations(pi_dof_id, pi_reset)

    def reset_posture(self, pi_dof_id: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub ResetPosture(long piDOFId)
                | 
                |     Reset the posture of the line of sight for the dof piDOFId.

        :param int pi_dof_id:
        :rtype: None
        """
        return self.swk_line_of_sight_node.ResetPosture(pi_dof_id)

    def reset_pref_angles(self, pi_dof_id: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub ResetPrefAngles(long piDOFId)
                | 
                |     Reset the preferred angles of the line of sight for the dof piDOFId.

        :param int pi_dof_id:
        :rtype: None
        """
        return self.swk_line_of_sight_node.ResetPrefAngles(pi_dof_id)

    def set_percentage(self, pi_percentage: float, pi_dof_id: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetPercentage(double piPercentage,
                | long piDOFId)
                | 
                |     Sets the angular limitations to a percentage for the DOF piDOFId

        :param float pi_percentage:
        :param int pi_dof_id:
        :rtype: None
        """
        return self.swk_line_of_sight_node.SetPercentage(pi_percentage, pi_dof_id)

    def __repr__(self):
        return f'SWKLineOfSightNode(name="{self.name}")'
