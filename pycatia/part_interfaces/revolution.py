#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.in_interfaces.reference import Reference
from pycatia.knowledge_interfaces.angle import Angle
from pycatia.part_interfaces.sketch_based_shape import SketchBasedShape


class Revolution(SketchBasedShape):
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
                |                             Revolution
                | 
                | Represents the revolution-based shapes.
                | It is the base objects for shaft and grooves.
                | 
                | See also:
                |     Shaft, Groove
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.revolution = com_object

    @property
    def first_angle(self) -> Angle:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property FirstAngle() As Angle (Read Only)
                | 
                |     Returns the revolution first angle. This angle is computed around the
                |     revolution axis, starting from the sketch plane trace on the plane
                |     perpendicular to the revolution axis, and is counted positive clockwise when
                |     looking at this plane in the revolution axis direction.
                | 
                |     Example:
                |         The following example returns in firstAngle the first angle of the
                |         MyRevolution revolution object:
                | 
                |          Set firstAngle = MyRevolution.FirstAngle

        :rtype: Angle
        """

        return Angle(self.revolution.FirstAngle)

    @property
    def is_thin(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property IsThin() As boolean
                | 
                |     Returns the Revol thin flag.
                |     It returns TRUE if the Revol is a thin Revol , FALSE if
                |     not.
                | 
                |     Returns:
                |         oIsThin The thin flag as a boolean
                | 
                |         Example:
                |             The following example saves in thinFlag the thin flag of Revol
                |             firstRevol, and then sets it so that it will be now thin
                |             :
                | 
                |              Set thinFlag = firstRevol.IsThin
                |              firstRevol.IsThin = TRUE

        :rtype: bool
        """

        return self.revolution.IsThin

    @is_thin.setter
    def is_thin(self, value: bool):
        """
        :param bool value:
        """

        self.revolution.IsThin = value

    @property
    def merge_end(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property MergeEnd() As boolean
                | 
                |     Returns the Revol merge end flag (for thin Revol only).
                |     It returns TRUE if merge ends is required , FALSE if not.
                | 
                |     Returns:
                |         oIsMergeEnd The merge end flag as a boolean
                | 
                |         Example:
                |             The following example saves in MergeEndFlag the merge end flag of
                |             Revol firstRevol, and then sets it so that merge end will be required
                |             :
                | 
                |              Set MergeEndFlag = firstRevol.IsMergeEnd
                |              firstRevol.IsMergeEnd = TRUE

        :rtype: bool
        """

        return self.revolution.MergeEnd

    @merge_end.setter
    def merge_end(self, value: bool):
        """
        :param bool value:
        """

        self.revolution.MergeEnd = value

    @property
    def neutral_fiber(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property NeutralFiber() As boolean
                | 
                |     Returns the Revol neutral fiber flag (for thin Revol
                |     only).
                |     It returns TRUE if the Revol is a neutral fiber Revol , FALSE if
                |     not.
                | 
                |     Returns:
                |         oIsNeutralFiber The neutral fiber flag as a boolean
                | 
                |         Example:
                |             The following example saves in NeutralFiberFlag the neutral fiber
                |             flag of Revol firstRevol, and then sets it so that it will be now neutral fiber
                |             :
                | 
                |              Set NeutralFiberFlag = firstRevol.IsNeutralFiber
                |              firstRevol.IsNeutralFiber = TRUE

        :rtype: bool
        """

        return self.revolution.NeutralFiber

    @neutral_fiber.setter
    def neutral_fiber(self, value: bool):
        """
        :param bool value:
        """

        self.revolution.NeutralFiber = value

    @property
    def revolute_axis(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property RevoluteAxis() As Reference
                | 
                |     Returns or sets the rotation axis for Revol.
                |     To set the property, you can use one of the following Boundary objects:
                |     RectilinearTriDimFeatEdge, RectilinearBiDimFeatEdge or
                |     RectilinearMonoDimFeatEdge.
                | 
                |     Example: This example retrieves in RevoluteAxis the rotation axis for the Rotate axis of the
                |     Revol feature Dim RevoluteAxis As Reference Set RevoluteAxis = Rotate.Axis

        :rtype: Reference
        """

        return Reference(self.revolution.RevoluteAxis)

    @revolute_axis.setter
    def revolute_axis(self, value: Reference):
        """
        :param Reference value:
        """

        self.revolution.RevoluteAxis = value.com_object

    @property
    def second_angle(self) -> Angle:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property SecondAngle() As Angle (Read Only)
                | 
                |     Returns the revolution second angle. This angle is computed around the
                |     revolution axis, starting from the sketch plane trace on the plane
                |     perpendicular to the revolution axis, and is counted positive counterclockwise
                |     when looking at this plane in the revolution axis direction. Its default value
                |     is 0.
                | 
                |     Example:
                |         The following example returns in secondAngle the second angle of the
                |         MyRevolution revolution object:
                | 
                |          Set secondAngle = MyRevolution.SecondAngle

        :rtype: Angle
        """

        return Angle(self.revolution.SecondAngle)

    def __repr__(self):
        return f'Revolution(name="{self.name}")'
