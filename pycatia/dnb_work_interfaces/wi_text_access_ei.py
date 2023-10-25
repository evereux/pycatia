#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.any_object import AnyObject


class WITextAccessEi(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     WITextAccessEI

    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.wi_text_access_ei = com_object

    def get_geom_referred_by_annotation(
            self,
            i_opor_act: int,
            i_assigned_ei_index: int,
            i_assignment_type: int,
            io_point_geom: AnyObject
    ) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetGeomReferedByAnnotation(short iOporAct,
                | long iAssignedEIIndex,
                | ItemAssignmentType iAssignmentType,
                | CATBaseDispatch ioPointGeom)
                | 
                |     Gets the underlying geometry associated to FTA Text Annotation, an
                |     Engineering Intent which is added as an item to operation or to a WIText
                |     activity.
                | 
                |     Parameters:
                | 
                |         iOpOrAcr
                |             Flag to know whether assignment of EI is at operation level or at
                |             activity level. Legal values:
                |             1 : Assignment is done at Operation level.
                |             0 : Assignment is done at Activity level. 
                |         iAssignedEIIndex
                |             Index of EIs either assigned to operation or to activity.
                |             
                |         iAssignmentType
                |             Type of the Assignment (Item to the Process) 
                | 
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on failure

        :param int i_opor_act:
        :param int i_assigned_ei_index:
        :param int i_assignment_type: enum item_assignment_type
        :param AnyObject io_point_geom:
        :rtype: None
        """
        return self.wi_text_access_ei.GetGeomReferedByAnnotation(
            i_opor_act,
            i_assigned_ei_index,
            i_assignment_type,
            io_point_geom.com_object
        )

    def __repr__(self):
        return f'WITextAccessEi(name="{self.name}")'
