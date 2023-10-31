#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.mec_mod_interfaces.constraints import Constraints
from pycatia.mec_mod_interfaces.geometric_elements import GeometricElements
from pycatia.sketcher_interfaces.axis_2D import Axis2D
from pycatia.sketcher_interfaces.factory_2D import Factory2D
from pycatia.sketcher_interfaces.line_2D import Line2D
from pycatia.system_interfaces.any_object import AnyObject
from pycatia.system_interfaces.system_service import SystemService


class Sketch(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     Sketch
                | 
                | The Sketch is a 2D based element comprising constrained 2D geometrical
                | elements.
                | The Sketch is created by giving a 2D support.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.sketch = com_object

    @property
    def absolute_axis(self) -> Axis2D:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property AbsoluteAxis() As Axis2D (Read Only)
                | 
                |     Returns the 2D absolute axis of the sketch. The absolute axis is used for
                |     constraining the sketch in 3D space, and its constituting horizontal and
                |     vertical directions can also be used to constrain horizontally or vertically
                |     subsequent geometrical elements in the sketch.
                | 
                |     Returns:
                |         oAxis The absolute axis of the sketch (@see CATIAAxis2D for more
                |         information).
                | 
                |         Example:
                |             The following example places in myAxis the absolute
                |             axis
                |             of the sketch mySketch:
                | 
                |              Set myAxis = mySketch.AbsoluteAxis

        :rtype: Axis2D
        """

        return Axis2D(self.sketch.AbsoluteAxis)

    @property
    def center_line(self) -> Line2D:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property CenterLine() As Line2D
                | 
                |     Returns the geometric 2D line defined as the center line of the sketch.
                |     Center lines are then used for creating shafts.
                | 
                |     Returns:
                |         oLine The center line of the sketch(@see CATIALine2D for more
                |         information).
                | 
                |         Example:
                |             The following example returns in myCenterLine the center
                |             line
                |             in the sketch mySketch:
                | 
                |              Set myCenterLine = mySketch.CenterLine

        :rtype: Line2D
        """

        return Line2D(self.sketch.CenterLine)

    @center_line.setter
    def center_line(self, value: Line2D):
        """
        :param Line2D value:
        """

        self.sketch.CenterLine = value

    @property
    def constraints(self) -> Constraints:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Constraints() As Constraints (Read Only)
                | 
                |     Returns the list of constraints included in the sketch.
                | 
                |     Returns:
                |         oConstraints The list of constraints in the sketch (@see
                |         CATIAConstraints
                |         for more information).
                | 
                |         Example:
                |             The following example returns in colConstraint the list of
                |             constraints
                |             in the sketch mySketch:
                | 
                |              Set colConstraint = mySketch.Constraints

        :rtype: Constraints
        """

        return Constraints(self.sketch.Constraints)

    @property
    def factory_2d(self) -> Factory2D:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Factory2D() As Factory2D (Read Only)
                | 
                |     Returns the 2D factory of the sketch. Take care that you must open
                |     edition
                |     on a sketch before adding or modifying elements in it.
                | 
                |     Returns:
                |         oFactory The 2D geometrical factory of the sketch (@see
                |         CATIAFactory2D
                |         for more information).
                | 
                |         Example:
                |             The following example returns in my2DFactory the 2D
                |             factory
                |             of the sketch mySketch:
                | 
                |              Set my2DFactory = mySketch.Factory2D

        :rtype: Factory2D
        """

        return Factory2D(self.sketch.Factory2D)

    @property
    def geometric_elements(self) -> GeometricElements:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property GeometricElements() As GeometricElements (Read
                | Only)
                | 
                |     Returns the list of geometrical elements included in the
                |     sketch.
                | 
                |     Returns:
                |         oGeometricElements The list of geometric elements in the sketch (@see
                |         CATIAGeometricElements
                |         for more information).
                | 
                |         Example:
                |             The following example returns in colGeometry the list of
                |             geometrical
                |             elements in the sketch mySketch:
                | 
                |              Set colGeometry = mySketch.GeometricElements

        :rtype: GeometricElements
        """

        return GeometricElements(self.sketch.GeometricElements)

    def close_edition(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub CloseEdition()
                | 
                |     Closes the Sketch Edition. Once you have finished working with the sketch,
                |     you
                |     must close its edition before using it for sketch-based
                |     shapes.
                | 
                |     Example:
                |         The following example closes the edition of the sketch
                |         mySketch:
                | 
                |          mySketch.CloseEdition

        :rtype: None
        """
        return self.sketch.CloseEdition()

    def evaluate(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub Evaluate()
                | 
                |     Evaluate the constraint system of the sketch

        :rtype: None
        """
        return self.sketch.Evaluate()

    def get_absolute_axis_data(self) -> tuple:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub GetAbsoluteAxisData(CATSafeArrayVariant oAxisData)
                | 
                |     Returns the sketch axis coordinates in 3D space. The matrix returned
                |     comprises 9 doubles, the first 3 being the coordinates
                |     of the axis origin, the next 3 being those of the horizontal axis, and
                |     the
                |     last 3 those of the vertical axis.
                |     The sketch horizontal axis is in fact computed from the first non null
                |     projection of one of the 3 3D space axes on the sketch
                |     plane.
                | 
                |     Returns:
                |         oAxisData The matrix of the axis in 3D space.
                | 
                |         Example:
                |             The following example reads the coordinates of the
                |             axis
                |             of the sketch mySketch:
                | 
                |              Dim myAxisCoordinate (8)
                |              mySketch.GetAbsoluteAxisData myAxisCoordinate
                |              Set OriginX = myAxisCoordinate(1)
                |              Set OriginY = myAxisCoordinate(2)
                |              Set OriginZ = myAxisCoordinate(3)
                |              Set HorizontalX = myAxisCoordinate(4)
                |              Set HorizontalY = myAxisCoordinate(5)
                |              Set HorizontalZ = myAxisCoordinate(6)
                |              Set VerticalX = myAxisCoordinate(7)
                |              Set VerticalY = myAxisCoordinate(8)
                |              Set VerticalZ = myAxisCoordinate(9)

        :rtype: tuple
        """

        vba_function_name = 'get_absolute_axis_data'
        vba_code = """
        Public Function get_absolute_axis_data(sketch)
            Dim oAxisData(8)
            sketch.GetAbsoluteAxisData oAxisData
            get_absolute_axis_data = oAxisData
        End Function
        """

        system_service = self.application.system_service
        return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def inverse_orientation(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub InverseOrientation()
                | 
                |     Inverse Orientation Of Sketch

        :rtype: None
        """
        return self.sketch.InverseOrientation()

    def open_edition(self) -> Factory2D:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func OpenEdition() As Factory2D
                | 
                |     Opens the Sketch Edition. You must open edition on a sketch before you can
                |     add
                |     elements in it. The CATIAFactory2D returned then enables you to create
                |     2D
                |     geometrical elements in the sketch.
                | 
                |     Returns:
                |         oFactory Returns the 2D FACTORY.
                | 
                |         Example:
                |             The following example opens edition on the sketch
                |             mySketch
                |             and places the factory in my2DFactory:
                | 
                |              Set my2DFactory = mySketch.OpenEdition

        :rtype: Factory2D
        """
        return Factory2D(self.sketch.OpenEdition())

    def set_absolute_axis_data(self, i_axis_data: tuple) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetAbsoluteAxisData(CATSafeArrayVariant iAxisData)
                | 
                |     Sets the absolute axis of the sketch in 3D space.
                | 
                |     Parameters:
                | 
                |         oAxisData
                |             The matrix comprises 9 doubles, the first 3 being the
                |             coordinates
                |             of the axis origin, the next 3 being those of the horizontal
                |             axis,
                |             and the last 3 those of the vertical axis of the absolute
                |             axis.

        :param tuple i_axis_data:
        :rtype: None
        """
        return self.sketch.SetAbsoluteAxisData(i_axis_data)

    def __repr__(self):
        return f'Sketch(name="{self.name}")'
