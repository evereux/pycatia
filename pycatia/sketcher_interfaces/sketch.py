#! usr/bin/python3.6
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-09 09:53:18.676780

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.mec_mod_interfaces.constraints import Constraints
from pycatia.mec_mod_interfaces.geometric_elements import GeometricElements
from pycatia.system_interfaces.any_object import AnyObject


class Sketch(AnyObject):

    """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)

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
    def absolute_axis(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
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

        :return: Axis2D
        """

        return Axis2D(self.sketch.AbsoluteAxis)

    @property
    def center_line(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
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

        :return: Line2D
        """

        return Line2D(self.sketch.CenterLine)

    @center_line.setter
    def center_line(self, value):
        """
        :param Line2D value:
        """

        self.sketch.CenterLine = value

    @property
    def constraints(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
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

        :return: Constraints
        """

        return Constraints(self.sketch.Constraints)

    @property
    def factory2_d(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
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

        :return: Factory2D
        """

        return Factory2D(self.sketch.Factory2D)

    @property
    def geometric_elements(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
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

        :return: GeometricElements
        """

        return GeometricElements(self.sketch.GeometricElements)

    def close_edition(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
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

        :return: None
        """
        return self.sketch.CloseEdition()

    def evaluate(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Sub Evaluate()
                | 
                |     Evaluate the constraint system of the sketch

        :return: None
        """
        return self.sketch.Evaluate()

    def get_absolute_axis_data(self, o_axis_data=None):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
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

        :param tuple o_axis_data:
        :return: None
        """
        return self.sketch.GetAbsoluteAxisData(o_axis_data)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_absolute_axis_data'
        # # vba_code = """
        # # Public Function get_absolute_axis_data(sketch)
        # #     Dim oAxisData (2)
        # #     sketch.GetAbsoluteAxisData oAxisData
        # #     get_absolute_axis_data = oAxisData
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def inverse_orientation(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Sub InverseOrientation()
                | 
                |     Inverse Orientation Of Sketch

        :return: None
        """
        return self.sketch.InverseOrientation()

    def open_edition(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
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

        :return: Factory2D
        """
        return Factory2D(self.sketch.OpenEdition())

    def set_absolute_axis_data(self, i_axis_data=None):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
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
        :return: None
        """
        return self.sketch.SetAbsoluteAxisData(i_axis_data)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_absolute_axis_data'
        # # vba_code = """
        # # Public Function set_absolute_axis_data(sketch)
        # #     Dim iAxisData (2)
        # #     sketch.SetAbsoluteAxisData iAxisData
        # #     set_absolute_axis_data = iAxisData
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'Sketch(name="{ self.name }")'
