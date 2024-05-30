#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.cat_str_functional_interfaces.sfm_member import SFMMember
from pycatia.in_interfaces.reference import Reference
from pycatia.knowledge_interfaces.length import Length


class SFMMember2Points(SFMMember):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     CATStrFunctionalInterfaces.SfmObject
                |                         CATStrFunctionalInterfaces.SfmProfile
                |                            CATStrFunctionalInterfaces.SfmMember
                |                                 SfmMember2Points
                | 
                | Interface to manage Member created with one curve and a reference
                | surface.
                | Role: To manage member created with one curve and a reference
                | surface.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.sfm_member2_points = com_object

    @property
    def end_point_on_crv_curve(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property EndPointOnCrvCurve() As Reference

        :rtype: Reference
        """

        return Reference(self.sfm_member2_points.EndPointOnCrvCurve)

    @end_point_on_crv_curve.setter
    def end_point_on_crv_curve(self, value: Reference):
        """
        :param Reference value:
        """

        self.sfm_member2_points.EndPointOnCrvCurve = value.com_object

    @property
    def end_point_on_crv_mode(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property EndPointOnCrvMode() As boolean

        :rtype: bool
        """

        return self.sfm_member2_points.EndPointOnCrvMode

    @end_point_on_crv_mode.setter
    def end_point_on_crv_mode(self, value: bool):
        """
        :param bool value:
        """

        self.sfm_member2_points.EndPointOnCrvMode = value

    @property
    def end_point_on_crv_offset(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property EndPointOnCrvOffset() As double

        :rtype: float
        """

        return self.sfm_member2_points.EndPointOnCrvOffset

    @end_point_on_crv_offset.setter
    def end_point_on_crv_offset(self, value: float):
        """
        :param float value:
        """

        self.sfm_member2_points.EndPointOnCrvOffset = value

    @property
    def end_point_on_crv_offset_param(self) -> Length:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property EndPointOnCrvOffsetParam() As Length (Read Only)

        :rtype: Length
        """

        return Length(self.sfm_member2_points.EndPointOnCrvOffsetParam)

    @property
    def end_point_on_crv_orientation(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property EndPointOnCrvOrientation() As long

        :rtype: int
        """

        return self.sfm_member2_points.EndPointOnCrvOrientation

    @end_point_on_crv_orientation.setter
    def end_point_on_crv_orientation(self, value: int):
        """
        :param int value:
        """

        self.sfm_member2_points.EndPointOnCrvOrientation = value

    @property
    def end_point_spec(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property EndPointSpec() As Reference

        :rtype: Reference
        """

        return Reference(self.sfm_member2_points.EndPointSpec)

    @end_point_spec.setter
    def end_point_spec(self, value: Reference):
        """
        :param Reference value:
        """

        self.sfm_member2_points.EndPointSpec = value.com_object

    @property
    def start_point_on_crv_curve(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property StartPointOnCrvCurve() As Reference
                | 
                |     Returns or sets the point on curve information: curve, ratio or length
                |     mode, offset and orientation.
                | 
                |     Example:
                |         This example retrieves in Curve the supporting curve for the
                |         SfmMember2Points feature.
                | 
                |          Dim Curve As Reference
                |          Set Curve = SfmMember2Points.StartPointOnCrvCurve

        :rtype: Reference
        """

        return Reference(self.sfm_member2_points.StartPointOnCrvCurve)

    @start_point_on_crv_curve.setter
    def start_point_on_crv_curve(self, value: Reference):
        """
        :param Reference value:
        """

        self.sfm_member2_points.StartPointOnCrvCurve = value.com_object

    @property
    def start_point_on_crv_mode(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property StartPointOnCrvMode() As boolean

        :rtype: bool
        """

        return self.sfm_member2_points.StartPointOnCrvMode

    @start_point_on_crv_mode.setter
    def start_point_on_crv_mode(self, value: bool):
        """
        :param bool value:
        """

        self.sfm_member2_points.StartPointOnCrvMode = value

    @property
    def start_point_on_crv_offset(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property StartPointOnCrvOffset() As double

        :rtype: float
        """

        return self.sfm_member2_points.StartPointOnCrvOffset

    @start_point_on_crv_offset.setter
    def start_point_on_crv_offset(self, value: float):
        """
        :param float value:
        """

        self.sfm_member2_points.StartPointOnCrvOffset = value

    @property
    def start_point_on_crv_offset_param(self) -> Length:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property StartPointOnCrvOffsetParam() As Length (Read Only)

        :rtype: Length
        """

        return Length(self.sfm_member2_points.StartPointOnCrvOffsetParam)

    @property
    def start_point_on_crv_orientation(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property StartPointOnCrvOrientation() As long

        :rtype: int
        """

        return self.sfm_member2_points.StartPointOnCrvOrientation

    @start_point_on_crv_orientation.setter
    def start_point_on_crv_orientation(self, value: int):
        """
        :param int value:
        """

        self.sfm_member2_points.StartPointOnCrvOrientation = value

    @property
    def start_point_spec(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property StartPointSpec() As Reference
                | 
                |     Returns or sets the point.
                |     Sub-element(s) supported (see Boundary object): Vertex.
                | 
                |     Example:
                |         This example retrieves in Point the supporting curve for the
                |         SfmMember2Points feature.
                | 
                |          Dim Point As Reference
                |          Set Point = SfmMember2Points.StartPointSpec

        :rtype: Reference
        """

        return Reference(self.sfm_member2_points.StartPointSpec)

    @start_point_spec.setter
    def start_point_spec(self, value: Reference):
        """
        :param Reference value:
        """

        self.sfm_member2_points.StartPointSpec = value.com_object

    def invert_end_point_on_crv_orientation(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub InvertEndPointOnCrvOrientation()

        :rtype: None
        """
        return self.sfm_member2_points.InvertEndPointOnCrvOrientation()

    def invert_start_point_on_crv_orientation(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub InvertStartPointOnCrvOrientation()
                | 
                |     Inverts the orientation of the offset for an extremity
                |     point.
                | 
                |     Example:
                |         This example inverts the orientation of the start point on curve
                |         extremity of the SfmMember2Points feature.
                | 
                |          SfmMember2Points.InvertStartPointOnCrvOrientation

        :rtype: None
        """
        return self.sfm_member2_points.InvertStartPointOnCrvOrientation()

    def __repr__(self):
        return f'SFMMember2Points(name="{self.name}")'
