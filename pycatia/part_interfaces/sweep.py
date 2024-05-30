#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.in_interfaces.reference import Reference
from pycatia.part_interfaces.sketch_based_shape import SketchBasedShape
from pycatia.sketcher_interfaces.sketch import Sketch


class Sweep(SketchBasedShape):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.Shape
                |                         PartInterfaces.SketchBasedShape
                |                             Sweep
                | 
                | Represents the sweep shape.
                | It is the base object for ribs and slots.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.sweep = com_object

    @property
    def anchor_dir_reverse(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property AnchorDirReverse() As boolean
                | 
                |     Returns the Sweep AnchorDirReverse flag (for Sweep Move Profile
                |     only).
                |     It returns TRUE if Anchor direction is reversed , FALSE if
                |     not.
                | 
                |     Returns:
                |         oAnchorDirReverse The oAnchorDirReverse flag as a
                |         boolean
                | 
                |         Example:

        :rtype: bool
        """

        return self.sweep.AnchorDirReverse

    @anchor_dir_reverse.setter
    def anchor_dir_reverse(self, value: bool):
        """
        :param bool value:
        """

        self.sweep.AnchorDirReverse = value

    @property
    def center_curve(self) -> Sketch:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property CenterCurve() As Sketch (Read Only)
                | 
                |     Returns the sketch used as the sweep center curve. The sweep is built along
                |     this sketch.
                | 
                |     Example:
                |         The following example returns in centerCurve the sketch used as center
                |         curve by the firstSweep sweep object:
                | 
                |          Set centerCurve = firstSweep.CenterCurve

        :rtype: Sketch
        """

        return Sketch(self.sweep.CenterCurve)

    @property
    def center_curve_element(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property CenterCurveElement() As Reference
                | 
                |     Returns or sets the center curve .
                |     To set the property, you can use the following Boundary object:
                |     TriDimFeatEdge.

        :rtype: Reference
        """

        return Reference(self.sweep.CenterCurveElement)

    @center_curve_element.setter
    def center_curve_element(self, value: Reference):
        """
        :param Reference value:
        """

        self.sweep.CenterCurveElement = value.com_object

    @property
    def is_thin(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property IsThin() As boolean
                | 
                |     Returns the Sweep thin flag.
                |     It returns TRUE if the Sweep is a thin Sweep , FALSE if
                |     not.
                | 
                |     Returns:
                |         oIsThin The thin flag as a boolean
                | 
                |         Example:
                |             The following example saves in thinFlag the thin flag of Sweep
                |             firstSweep, and then sets it so that it will be now thin
                |             :
                | 
                |              Set thinFlag = firstSweep.IsThin
                |              firstSweep.IsThin = TRUE

        :rtype: bool
        """

        return self.sweep.IsThin

    @is_thin.setter
    def is_thin(self, value: bool):
        """
        :param bool value:
        """

        self.sweep.IsThin = value

    @property
    def merge_end(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property MergeEnd() As boolean
                | 
                |     Returns the Sweep merge end flag (for thin Sweep only).
                |     It returns TRUE if merge ends is required , FALSE if not.
                | 
                |     Returns:
                |         oIsMergeEnd The merge end flag as a boolean
                | 
                |         Example:
                |             The following example saves in MergeEndFlag the merge end flag of
                |             Sweep firstSweep, and then sets it so that merge end will be required
                |             :
                | 
                |              Set MergeEndFlag = firstSweep.IsMergeEnd
                |              firstSweep.IsMergeEnd = TRUE

        :rtype: bool
        """

        return self.sweep.MergeEnd

    @merge_end.setter
    def merge_end(self, value: bool):
        """
        :param bool value:
        """

        self.sweep.MergeEnd = value

    @property
    def merge_mode(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property MergeMode() As CatMergeMode
                | 
                |     Returns or sets the end mode .

        :return: enum cat_merge_mode
        :rtype: int
        """

        return self.sweep.MergeMode

    @merge_mode.setter
    def merge_mode(self, value: int):
        """
        :param int value: enum cat_merge_mode
        """

        self.sweep.MergeMode = value

    @property
    def move_profile_to_path(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property MoveProfileToPath() As boolean
                | 
                |     Returns the Sweep MoveProfileToPath flag (for Sweep Move Profile
                |     only).
                |     It returns TRUE if move profile is required , FALSE if
                |     not.
                | 
                |     Returns:
                |         oIsMoveProfileToPath The MoveProfileToPath flag as a
                |         boolean
                | 
                |         Example:

        :rtype: bool
        """

        return self.sweep.MoveProfileToPath

    @move_profile_to_path.setter
    def move_profile_to_path(self, value: bool):
        """
        :param bool value:
        """

        self.sweep.MoveProfileToPath = value

    @property
    def neutral_fiber(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property NeutralFiber() As boolean
                | 
                |     Returns the Sweep neutral fiber flag (for thin Sweep
                |     only).
                |     It returns TRUE if the Sweep is a neutral fiber Sweep , FALSE if
                |     not.
                | 
                |     Returns:
                |         oIsNeutralFiber The neutral fiber flag as a boolean
                | 
                |         Example:
                |             The following example saves in NeutralFiberFlag the neutral fiber
                |             flag of Sweep firstSweep, and then sets it so that it will be now neutral fiber
                |             :
                | 
                |              Set NeutralFiberFlag = firstSweep.IsNeutralFiber
                |              firstSweep.IsNeutralFiber = TRUE

        :rtype: bool
        """

        return self.sweep.NeutralFiber

    @neutral_fiber.setter
    def neutral_fiber(self, value: bool):
        """
        :param bool value:
        """

        self.sweep.NeutralFiber = value

    @property
    def normal_axis_dir_reverse(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property NormalAxisDirReverse() As boolean
                | 
                |     Returns the Sweep NormalAxisDirReverse flag (for Sweep Move Profile
                |     only).
                |     It returns TRUE if Normal Axis direction is reversed , FALSE if
                |     not.
                | 
                |     Returns:
                |         oNormalAxisDirReverse The oNormalAxisDirReverse flag as a
                |         boolean
                | 
                |         Example:

        :rtype: bool
        """

        return self.sweep.NormalAxisDirReverse

    @normal_axis_dir_reverse.setter
    def normal_axis_dir_reverse(self, value: bool):
        """
        :param bool value:
        """

        self.sweep.NormalAxisDirReverse = value

    @property
    def pulling_dir_element(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property PullingDirElement() As Reference
                | 
                |     Returns or sets the pulling direction .
                |     To set the property, you can use one of the following Boundary objects:
                |     PlanarFace, RectilinearTriDimFeatEdge, RectilinearBiDimFeatEdge,
                |     RectilinearMonoDimFeatEdge.

        :rtype: Reference
        """

        return Reference(self.sweep.PullingDirElement)

    @pulling_dir_element.setter
    def pulling_dir_element(self, value: Reference):
        """
        :param Reference value:
        """

        self.sweep.PullingDirElement = value.com_object

    @property
    def reference_surface_element(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property ReferenceSurfaceElement() As Reference
                | 
                |     Returns or sets the reference surface .
                |     To set the property, you can use the following Boundary object: Face.

        :rtype: Reference
        """

        return Reference(self.sweep.ReferenceSurfaceElement)

    @reference_surface_element.setter
    def reference_surface_element(self, value: Reference):
        """
        :param Reference value:
        """

        self.sweep.ReferenceSurfaceElement = value.com_object

    def set_keep_angle_option(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetKeepAngleOption()
                | 
                |     Actives KeepAngleOption.

        :rtype: None
        """
        return self.sweep.SetKeepAngleOption()

    def __repr__(self):
        return f'Sweep(name="{self.name}")'
