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


class SFMMemberSurfSurf(SFMMember):
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
                |                                 SfmMemberSurfSurf
                | 
                | Interface to manage Member created by the intersection of two
                | surfaces.
                | Role: To manage member created by the intersection of two
                | surfaces.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.sfm_member_surf_surf = com_object

    @property
    def first_surface(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property FirstSurface() As Reference
                | 
                |     Returns or sets the SuperMember's first surface.
                | 
                |     Example:
                |         This example retrieves in FirstSurface the first surface of the
                |         SuperMember feature.
                | 
                |          Dim Surface As Reference
                |          Set Surface = SuperMember.FirstSurface

        :rtype: Reference
        """

        return Reference(self.sfm_member_surf_surf.FirstSurface)

    @first_surface.setter
    def first_surface(self, value: Reference):
        """
        :param Reference value:
        """

        self.sfm_member_surf_surf.FirstSurface = value.com_object

    @property
    def first_surface_offset(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property FirstSurfaceOffset() As double
                | 
                |     Returns or sets the SuperMember's first surface offset.
                | 
                |     Example:
                |         This example retrieves in Offset the first surface offset of the
                |         SuperMember feature.
                | 
                |          Dim Offset As Double
                |          Set Offset = SuperMember.FirstSurfaceOffset

        :rtype: float
        """

        return self.sfm_member_surf_surf.FirstSurfaceOffset

    @first_surface_offset.setter
    def first_surface_offset(self, value: float):
        """
        :param float value:
        """

        self.sfm_member_surf_surf.FirstSurfaceOffset = value

    @property
    def first_surface_offset_param(self) -> Length:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property FirstSurfaceOffsetParam() As Length (Read Only)

        :rtype: Length
        """

        return Length(self.sfm_member_surf_surf.FirstSurfaceOffsetParam)

    @property
    def first_surface_orientation(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property FirstSurfaceOrientation() As long
                | 
                |     Returns or sets the SuperMember's first surface
                |     orientation.
                | 
                |     Example:
                |         This example retrieves in Orient the first surface orientation for
                |         SuperMember feature.
                | 
                |          Dim Orient As Integer
                |          Set Orient = SuperMember.FirstSurfaceOrientation

        :rtype: int
        """

        return self.sfm_member_surf_surf.FirstSurfaceOrientation

    @first_surface_orientation.setter
    def first_surface_orientation(self, value: int):
        """
        :param int value:
        """

        self.sfm_member_surf_surf.FirstSurfaceOrientation = value

    @property
    def second_surface(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property SecondSurface() As Reference
                | 
                |     Returns the SuperMember's second surface.
                | 
                |     Example:
                |         This example retrieves in Surface the second surface of the SuperMember
                |         feature.
                | 
                |          Dim Surface As Reference
                |          Set Surface = SuperMember.SecondSurface

        :rtype: Reference
        """

        return Reference(self.sfm_member_surf_surf.SecondSurface)

    @second_surface.setter
    def second_surface(self, value: Reference):
        """
        :param Reference value:
        """

        self.sfm_member_surf_surf.SecondSurface = value.com_object

    @property
    def second_surface_offset(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property SecondSurfaceOffset() As double
                | 
                |     Returns or sets the SuperMember's second surface offset.
                | 
                |     Example:
                |         This example retrieves in Offset the second surface offset of the
                |         SuperMember feature.
                | 
                |          Dim Offset As Double
                |          Set Offset = SuperMember.SecondSurfaceOffset

        :rtype: float
        """

        return self.sfm_member_surf_surf.SecondSurfaceOffset

    @second_surface_offset.setter
    def second_surface_offset(self, value: float):
        """
        :param float value:
        """

        self.sfm_member_surf_surf.SecondSurfaceOffset = value

    @property
    def second_surface_offset_param(self) -> Length:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property SecondSurfaceOffsetParam() As Length (Read Only)

        :rtype: Length
        """

        return Length(self.sfm_member_surf_surf.SecondSurfaceOffsetParam)

    @property
    def second_surface_orientation(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property SecondSurfaceOrientation() As long
                | 
                |     Returns or sets the SuperMember's second surface
                |     orientation.
                | 
                |     Example:
                |         This example retrieves in Orient the second surface orientation for
                |         SuperMember feature.
                | 
                |          Dim Orient As Integer
                |          Set Orient = SuperMember.SecondSurfaceOrientation

        :rtype: int
        """

        return self.sfm_member_surf_surf.SecondSurfaceOrientation

    @second_surface_orientation.setter
    def second_surface_orientation(self, value: int):
        """
        :param int value:
        """

        self.sfm_member_surf_surf.SecondSurfaceOrientation = value

    def __repr__(self):
        return f'SFMMemberSurfSurf(name="{self.name}")'
