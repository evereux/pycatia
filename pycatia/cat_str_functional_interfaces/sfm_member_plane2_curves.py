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


class SFMMemberPlane2Curves(SFMMember):
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
                |                                 SfmMemberPlane2Curves
                | 
                | Interface to manage a Member created with two curves and a
                | plane.
                | Role: To manage member created with two curves and a plane.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.sfm_member_plane2_curves = com_object

    @property
    def first_curve(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property FirstCurve() As Reference
                | 
                |     Returns or sets the first and second curve.
                | 
                |     Example:
                |         This example retrieves in Curve the first curve for the
                |         SfmMemberPlane2Curves feature.
                | 
                |          Dim Curve As Reference
                |          Set Curve = SfmMemberPlane2Curves.FirstCurve

        :rtype: Reference
        """

        return Reference(self.sfm_member_plane2_curves.FirstCurve)

    @first_curve.setter
    def first_curve(self, value: Reference):
        """
        :param Reference value:
        """

        self.sfm_member_plane2_curves.FirstCurve = value.com_object

    @property
    def first_member(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property FirstMember(Reference iFirstMember)
                | 
                |     Returns or sets the first Member.
                | 
                |     Example:
                |         This example retrieves in Member the first Member for the
                |         SfmMemberPlane2Curves feature.
                | 
                |          Dim Member1 As Reference
                |          Set Member1 = SfmMemberPlane2Curves.FirstMember

        :rtype: False
        """

        return self.sfm_member_plane2_curves.FirstMember

    @first_member.setter
    def first_member(self, value: Reference):
        """
        :param Reference value:
        """

        self.sfm_member_plane2_curves.FirstMember = value.com_object

    @property
    def plane(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Plane() As Reference
                | 
                |     Returns or sets the intersecting plane.
                | 
                |     Example:
                |         This example retrieves in Plane the intersecting plane for the
                |         SfmMemberPlane2Curves feature.
                | 
                |          Dim Plane As Reference
                |          Set Plane = SfmMemberPlane2Curves.Plane

        :rtype: Reference
        """

        return Reference(self.sfm_member_plane2_curves.Plane)

    @plane.setter
    def plane(self, value: Reference):
        """
        :param Reference value:
        """

        self.sfm_member_plane2_curves.Plane = value.com_object

    @property
    def second_curve(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property SecondCurve() As Reference

        :rtype: Reference
        """

        return Reference(self.sfm_member_plane2_curves.SecondCurve)

    @second_curve.setter
    def second_curve(self, value: Reference):
        """
        :param Reference value:
        """

        self.sfm_member_plane2_curves.SecondCurve = value.com_object

    @property
    def second_member(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property SecondMember(Reference iSecondMember)
                | 
                |     Returns or sets the Second Member.
                | 
                |     Example:
                |         This example retrieves in Member the Second Member for the
                |         SfmMemberPlane2Curves feature.
                | 
                |          Dim Member2 As Reference
                |          Set Member2 = SfmMemberPlane2Curves.SecondMember

        :rtype: False
        """

        return self.sfm_member_plane2_curves.SecondMember

    @second_member.setter
    def second_member(self, value: Reference):
        """
        :param Reference value:
        """

        self.sfm_member_plane2_curves.SecondMember = value.com_object

    def __repr__(self):
        return f'SFMMemberPlane2Curves(name="{self.name}")'
