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


class SFMMemberCurve(SFMMember):
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
                |                                 SfmMemberCurve
                | 
                | Interface to manage Member created with one curve and a reference
                | surface.
                | Role: To manage member created with one curve and a reference
                | surface.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.sfm_member_curve = com_object

    @property
    def curve(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Curve() As Reference
                | 
                |     Returns or sets the curve.
                |     Sub-element(s) supported (see Boundary object): Edge.
                | 
                |     Example:
                |         This example retrieves in Curve the supporting curve for the
                |         SfmMemberCurve feature.
                | 
                |          Dim Curve As Reference
                |          Set Curve = SfmMemberCurve.Curve

        :rtype: Reference
        """

        return Reference(self.sfm_member_curve.Curve)

    @curve.setter
    def curve(self, value: Reference):
        """
        :param Reference value:
        """

        self.sfm_member_curve.Curve = value.com_object

    @property
    def reference_surface(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ReferenceSurface() As Reference
                | 
                |     Returns or sets the reference surface.
                | 
                |     Example:
                |         This example retrieves in ReferenceSurface the reference surface for
                |         the SfmMemberCurve feature.
                | 
                |          Dim ReferenceSurface As Reference
                |          Set ReferenceSurface = SfmMemberCurve.ReferenceSurface

        :rtype: Reference
        """

        return Reference(self.sfm_member_curve.ReferenceSurface)

    @reference_surface.setter
    def reference_surface(self, value: Reference):
        """
        :param Reference value:
        """

        self.sfm_member_curve.ReferenceSurface = value.com_object

    @property
    def reference_surface_orientation(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ReferenceSurfaceOrientation() As long
                | 
                |     Returns or sets the reference surface orientation.
                | 
                |     Example:
                |         This example retrieves in ReferenceSurfaceOrient the reference surface
                |         orientation for SfmMemberCurve feature.
                | 
                |          Dim ReferenceSurfaceOrient As Integer
                |          Set ReferenceSurfaceOrient = SfmMemberCurve.ReferenceSurfaceOrientation

        :rtype: int
        """

        return self.sfm_member_curve.ReferenceSurfaceOrientation

    @reference_surface_orientation.setter
    def reference_surface_orientation(self, value: int):
        """
        :param int value:
        """

        self.sfm_member_curve.ReferenceSurfaceOrientation = value

    def invert_reference_surface(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub InvertReferenceSurface()
                | 
                |     Inverts the reference surface orientation.
                | 
                |     Example:
                |         This example inverts the orientation of the reference surface for the
                |         SfmMemberCurve feature.
                | 
                |          SfmMemberCurve.InvertReferenceSurface

        :rtype: None
        """
        return self.sfm_member_curve.InvertReferenceSurface()

    def __repr__(self):
        return f'SFMMemberCurve(name="{self.name}")'
