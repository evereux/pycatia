#! usr/bin/python3.6
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.any_object import AnyObject


class AssociatedRefFrame(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     AssociatedRefFrame
                | 
                | Interface dedicated to manage Datum Reference Frame associated to a
                | TPS.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.associated_ref_frame = com_object

    @property
    def reference_frame(self) -> 'Annotation':
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ReferenceFrame() As Annotation (Read Only)
                | 
                |     Retrieves the Datum Reference Frame associated to a TPS. Deprecated method:
                |     ReferenceFrame method is replaced by ReferenceFrame2 has.

        :return: Annotation
        :rtype: Annotation
        """

        import pycatia.tps_interfaces.annotation
        return pycatia.tps_interfaces.annotation.Annotation(self.associated_ref_frame.ReferenceFrame)

    @property
    def reference_frame_2(self) -> 'Annotation2':
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ReferenceFrame2() As Annotation2 (Read Only)
                | 
                |     Retrieves the Datum Reference Frame associated to a TPS.

        :return: Annotation2
        :rtype: Annotation2
        """

        import pycatia.tps_interfaces.annotation_2
        return pycatia.tps_interfaces.annotation_2.Annotation2(self.associated_ref_frame.ReferenceFrame2)

    def __repr__(self):
        return f'AssociatedRefFrame(name="{self.name}")'
