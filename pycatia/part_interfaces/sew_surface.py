#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.in_interfaces.reference import Reference
from pycatia.part_interfaces.surface_based_shape import SurfaceBasedShape


class SewSurface(SurfaceBasedShape):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.Shape
                |                         PartInterfaces.SurfaceBasedShape
                |                             SewSurface
                | 
                | Represents the sewing operation.
                | It sews a shape using a sewing element, such as a surface or a
                | face
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.sew_surface = com_object

    @property
    def deviation(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Deviation() As double
                | 
                |     Sets or Gets the maximum deviation allowed for smoothing operation in
                |     sewing command. This value must be set in SI unit (m).
                | 
                |     Example: This example retrieves in DeviationValue the maximum deviation
                |     value for the Sewfeature.
                | 
                |      Dim DeviationValue As double
                |      Set DeviationValue = Sew.MaximumDeviationValue

        :rtype: float
        """

        return self.sew_surface.Deviation

    @deviation.setter
    def deviation(self, value: float):
        """
        :param float value:
        """

        self.sew_surface.Deviation = value

    @property
    def deviation_mode(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property DeviationMode() As long
                | 
                |     Returns or sets the Deviation mode taken into account during Sew
                |     construction.
                |     Legal values:
                | 
                |     0
                |         Unknown Deviation mode.
                |     1
                |         None Deviation mode. Error thrown if maximum deviation exceeds CATIA
                |         resolution.
                |     2
                |         Automatic Deviation mode. Error thrown if maximum deviation exceeds 100
                |         times CATIA resolution.
                |     3
                |         Manual Deviation mode. Error thrown if maximum deviation exceeds input
                |         user deviation.
                | 
                |     Example:
                |         This example retrieves in oMode the Deviation mode for the Sew
                |         feature.
                | 
                |          Dim oMode
                |          Set oMode = Sew.DeviationMode

        :rtype: int
        """

        return self.sew_surface.DeviationMode

    @deviation_mode.setter
    def deviation_mode(self, value: int):
        """
        :param int value:
        """

        self.sew_surface.DeviationMode = value

    @property
    def sewing_intersection_mode(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property SewingIntersectionMode() As
                | CatSewingIntersectionMode
                | 
                |     Returns or sets the sewing mode . The sewing side is the side of the body
                |     kept after the sewing. A positive side refers to the same orientation than the
                |     sewing element normal vector.
                | 
                |     Example:
                |         The following example returns in sptSide the sewing side of the sew
                |         shape mySew, and then sets it to catPositiveSide:
                | 
                |          Set sptSide = mySew.SewingSide
                |          mySew.SewingSide = catPositiveSide

        :return: enum cat_sewing_intersection_mode
        :rtype: int
        """

        return self.sew_surface.SewingIntersectionMode

    @sewing_intersection_mode.setter
    def sewing_intersection_mode(self, value: int):
        """
        :param int value: enum cat_sewing_intersection_mode
        """

        self.sew_surface.SewingIntersectionMode = value

    @property
    def sewing_side(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property SewingSide() As CatSplitSide
                | 
                |     Returns or sets the sewing side . The sewing side is the side of the body
                |     kept after the sewing. A positive side refers to the same orientation than the
                |     sewing element normal vector.
                | 
                |     Example:
                |         The following example returns in sptSide the sewing side of the sew
                |         shape mySew, and then sets it to catPositiveSide:
                | 
                |          Set sptSide = mySew.SewingSide
                |          mySew.SewingSide = catPositiveSide

        :return: enum cat_split_side
        :rtype: int
        """

        return self.sew_surface.SewingSide

    @sewing_side.setter
    def sewing_side(self, value: int):
        """
        :param int value: enum cat_split_side
        """

        self.sew_surface.SewingSide = value

    def set_surface_support(self, i_support_surface: Reference) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetSurfaceSupport(Reference iSupportSurface)
                | 
                |     Sets the surface support for surfacic sew surface.
                | 
                |     Parameters:
                | 
                |         iSupportSurface
                |             A Reference object to a surface (see 
                | 
                |         Reference for more information)

        :param Reference i_support_surface:
        :rtype: None
        """
        return self.sew_surface.SetSurfaceSupport(i_support_surface.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_surface_support'
        # # vba_code = """
        # # Public Function set_surface_support(sew_surface)
        # #     Dim iSupportSurface (2)
        # #     sew_surface.SetSurfaceSupport iSupportSurface
        # #     set_surface_support = iSupportSurface
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_volume_support(self, i_volume: Reference) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetVolumeSupport(Reference iVolume)
                | 
                |     Sets the volume support for volume sew surface.
                | 
                |     Parameters:
                | 
                |         iVolume
                |             A Reference object to a volume (see 
                | 
                |         Reference for more information)
                | 
                |         Example:
                |             The following example sets the volume support of SewSurface
                |             firstSewSurface to volumeExtrude volume reference
                |             :
                | 
                |              firstSewSurface.SetVolumeSupport volumeExtrudeRef

        :param Reference i_volume:
        :rtype: None
        """
        return self.sew_surface.SetVolumeSupport(i_volume.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_volume_support'
        # # vba_code = """
        # # Public Function set_volume_support(sew_surface)
        # #     Dim iVolume (2)
        # #     sew_surface.SetVolumeSupport iVolume
        # #     set_volume_support = iVolume
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'SewSurface(name="{self.name}")'
