#! usr/bin/python3.6
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.in_interfaces.reference import Reference
from pycatia.knowledge_interfaces.angle import Angle
from pycatia.knowledge_interfaces.length import Length
from pycatia.knowledge_interfaces.str_param import StrParam
from pycatia.part_interfaces.limit import Limit
from pycatia.part_interfaces.sketch_based_shape import SketchBasedShape


class Hole(SketchBasedShape):
    """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.Shape
                |                         PartInterfaces.SketchBasedShape
                |                             Hole
                | 
                | Hole Feature in Part Design.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hole = com_object

    @property
    def anchor_mode(self) -> int:
        """
        .. note::
            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property AnchorMode() As CatHoleAnchorMode
                | 
                |     Returns the hole anchor mode.
                |     This information is pertinent when hole type is Counterbored or
                |     Counterdrilled only.
                | 
                |     Returns:
                |         oMode The hole anchor mode (see CatHoleAnchorMode for list of possible
                |         types)
                | 
                |         Example:
                |             The following example returns in holeAnchorMode the anchor mode of
                |             hole firstHole:
                | 
                |              Set holeAnchorMode = firstHole.AnchorMode

        :return: int
        :rtype: int
        """

        return self.hole.AnchorMode

    @anchor_mode.setter
    def anchor_mode(self, value: int):
        """
        :param int value:
        """

        self.hole.AnchorMode = value

    @property
    def bottom_angle(self) -> Angle:
        """
        .. note::
            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property BottomAngle() As Angle (Read Only)
                | 
                |     Returns the hole bottom angle.
                |     This call is valid when the hole bottom type is : VBottom.
                | 
                |     Returns:
                |         oBottomAngle An Angle object controlling the hole bottom angle (see
                |         Angle for more information)
                | 
                |         Example:
                |             The following example returns in holeBottomAngle the bottom angle
                |             of hole firstHole:
                | 
                |              Set holeBottomAngle = firstHole.BottomAngle

        :return: Angle
        :rtype: Angle
        """

        return Angle(self.hole.BottomAngle)

    @property
    def bottom_limit(self) -> Limit:
        """
        .. note::
            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property BottomLimit() As Limit (Read Only)
                | 
                |     Returns the bottom limit.
                |     This call is valid when the hole bottom type is : BlindHole or ThruHole.
                | 
                |     Returns:
                |         oBottomLimit A Limit object controlling the hole bottom limit (see
                |         Limit for more information)
                | 
                |         Example:
                |             The following example returns in holeBottomLimit the bottom limit
                |             of hole firstHole:
                | 
                |              Set holeBottomLimit = firstHole.BottomLimit

        :return: Limit
        :rtype: Limit
        """

        return Limit(self.hole.BottomLimit)

    @property
    def bottom_type(self) -> int:
        """
        .. note::
            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property BottomType() As CatHoleBottomType
                | 
                |     Returns the hole bottom type.
                | 
                |     Returns:
                |         oBottomType The hole bottom type (see CatHoleBottomType for list of
                |         possible types)
                | 
                |         Example:
                |             The following example returns in holeBottomType the bottom type of
                |             hole firstHole:
                | 
                |              Set holeBottomType = firstHole.BottomType

        :return: int
        :rtype: int
        """

        return self.hole.BottomType

    @bottom_type.setter
    def bottom_type(self, value: int):
        """
        :param int value:
        """

        self.hole.BottomType = value

    @property
    def counter_sunk_mode(self) -> int:
        """
        .. note::
            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property CounterSunkMode() As CatCSHoleMode
                | 
                |     Returns the mode of a countersunk hole .
                | 
                |     Returns:
                |         CSMode Value of the countersunk mode (see CatCSHoleMode for list of
                |         possible types)
                | 
                |         Example:
                |             The following example returns in CSMode the CSMode of hole
                |             firsthole:
                | 
                |              Set CSMode = firsthole.CounterSunkMode

        :return: int
        :rtype: int
        """

        return self.hole.CounterSunkMode

    @counter_sunk_mode.setter
    def counter_sunk_mode(self, value: int):
        """
        :param int value:
        """

        self.hole.CounterSunkMode = value

    @property
    def diameter(self) -> Length:
        """
        .. note::
            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Diameter() As Length (Read Only)
                | 
                |     Returns the hole diameter.
                | 
                |     Returns:
                |         oDiameter A Length object controlling the hole diameter (see Length for
                |         more information)
                | 
                |         Example:
                |             The following example returns in holeDiam the diameter of hole
                |             firstHole:
                | 
                |              Set holeDiam = firstHole.Diameter

        :return: Length
        :rtype: Length
        """

        return Length(self.hole.Diameter)

    @property
    def head_angle(self) -> Angle:
        """
        .. note::
            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property HeadAngle() As Angle (Read Only)
                | 
                |     Returns the hole head angle.
                |     This call is valid when the hole type is : Tapered or Counterdrilled or Countersunk.
                | 
                |     Returns:
                |         oHeadAngle An Angle object controlling the hole head angle (see Angle
                |         for more information)
                | 
                |         Example:
                |             The following example returns in holeHeadAngle the head angle of
                |             hole firstHole:
                | 
                |              Set holeHeadAngle = firstHole.HeadAngle

        :return: Angle
        :rtype: Angle
        """

        return Angle(self.hole.HeadAngle)

    @property
    def head_depth(self) -> Length:
        """
        .. note::
            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property HeadDepth() As Length (Read Only)
                | 
                |     Returns the hole head depth.
                |     This call is valid when the hole type is : Counterbored or Counterdrilled or Countersunk.
                | 
                |     Returns:
                |         oHeadDepth A Length object controlling the hole head depth (see Length
                |         for more information)
                | 
                |         Example:
                |             The following example returns in holeHeadDepth the head depth of
                |             hole firstHole:
                | 
                |              Set holeHeadDepth = firstHole.HeadDepth

        :return: Length
        :rtype: Length
        """

        return Length(self.hole.HeadDepth)

    @property
    def head_diameter(self) -> Length:
        """
        .. note::
            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property HeadDiameter() As Length (Read Only)
                | 
                |     Returns the hole head diameter.
                |     This call is valid when the hole type is : Counterbored or Counterdrilled.
                | 
                |     Returns:
                |         oHeadDiameter A Length object controlling the hole head diameter (see
                |         Length for more information)
                | 
                |         Example:
                |             The following example returns in holeHeadDiam the head diameter of
                |             hole firstHole:
                | 
                |              Set holeHeadDiam = firstHole.HeadDiameter

        :return: Length
        :rtype: Length
        """

        return Length(self.hole.HeadDiameter)

    @property
    def hole_thread_description(self) -> StrParam:
        """
        .. note::
            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property HoleThreadDescription() As StrParam (Read Only)
                | 
                |     Returns the hole thread description parameter.
                |     This call is valid when the hole threading mode is : CATThreadedHoleThreading.
                |     This call is valid only when a standard/user design table
                |     exists
                | 
                |     Returns:
                |         oThreadDescParam A Parameter object controlling the hole thread
                |         description (see StrParam for more information)
                | 
                |         Example:
                |             The following example returns in holeThreadDescription the thread
                |             description (M12 etc) of hole firstHole:
                | 
                |              Set holeThreadDescription = firstHole.HoleThreadDescription

        :return: StrParam
        :rtype: StrParam
        """

        return StrParam(self.hole.HoleThreadDescription)

    @property
    def thread_depth(self) -> Length:
        """
        .. note::
            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property ThreadDepth() As Length (Read Only)
                | 
                |     Returns the hole thread depth.
                |     This call is valid when the hole threading mode is : CATThreadedHoleThreading.
                | 
                |     Returns:
                |         oThreadDepth A Length object controlling the hole thread depth (see
                |         Length for more information)
                | 
                |         Example:
                |             The following example returns in holeThreadDepth the thread depth
                |             of hole firstHole:
                | 
                |              Set holeThreadDepth = firstHole.ThreadDepth

        :return: Length
        :rtype: Length
        """

        return Length(self.hole.ThreadDepth)

    @property
    def thread_diameter(self) -> Length:
        """
        .. note::
            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property ThreadDiameter() As Length (Read Only)
                | 
                |     Returns the hole thread diameter.
                |     This call is valid when the hole threading mode is : CATThreadedHoleThreading.
                | 
                |     Returns:
                |         oThreadDiameter A Length object controlling the hole thread diameter
                |         (see Length for more information)
                | 
                |         Example:
                |             The following example returns in holeThreadDiameter the thread
                |             diameter of hole firstHole:
                | 
                |              Set holeThreadDiameter = firstHole.ThreadDiameter

        :return: Length
        :rtype: Length
        """

        return Length(self.hole.ThreadDiameter)

    @property
    def thread_pitch(self) -> Length:
        """
        .. note::
            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property ThreadPitch() As Length (Read Only)
                | 
                |     Returns the hole thread pitch.
                |     This call is valid when the hole threading mode is : CATThreadedHoleThreading.
                | 
                |     Returns:
                |         oThreadPitch A Length object controlling the hole thread pitch (see
                |         Length for more information)
                | 
                |         Example:
                |             The following example returns in holeThreadPitch the thread pitch
                |             of hole firstHole:
                | 
                |              Set holeThreadPitch = firstHole.ThreadPitch

        :return: Length
        :rtype: Length
        """

        return Length(self.hole.ThreadPitch)

    @property
    def thread_side(self) -> int:
        """
        .. note::
            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property ThreadSide() As CatHoleThreadSide
                | 
                |     Returns the hole thread side.
                | 
                |     Returns:
                |         oThreadSide The hole thread side (see CatHoleThreadSide for list of
                |         possible sides)
                | 
                |         Example:
                |             The following example returns in holeThreadSide the thread side of
                |             hole firstHole:
                | 
                |              Set holeThreadSide = firstHole.ThreadSide

        :return: int
        :rtype: int
        """

        return self.hole.ThreadSide

    @thread_side.setter
    def thread_side(self, value: int):
        """
        :param int value:
        """

        self.hole.ThreadSide = value

    @property
    def threading_mode(self) -> int:
        """
        .. note::
            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property ThreadingMode() As CatHoleThreadingMode
                | 
                |     Returns the hole threading mode.
                | 
                |     Returns:
                |         oThreadingMode The hole threading mode (see CatHoleThreadingMode for
                |         list of possible types)
                | 
                |         Example:
                |             The following example returns in holeThreadingMode the threading
                |             mode of hole firstHole:
                | 
                |              Set holeThreadingMode = firstHole.ThreadingMode

        :return: int
        :rtype: int
        """

        return self.hole.ThreadingMode

    @threading_mode.setter
    def threading_mode(self, value: int):
        """
        :param int value:
        """

        self.hole.ThreadingMode = value

    @property
    def type(self) -> int:
        """
        .. note::
            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Type() As CatHoleType
                | 
                |     Returns the hole type.
                | 
                |     Returns:
                |         oType The hole type (see CatHoleType for list of possible
                |         types)
                | 
                |         Example:
                |             The following example returns in holeType the type of hole
                |             firstHole:
                | 
                |              Set holeType = firstHole.Type

        :return: int
        :rtype: int
        """

        return self.hole.Type

    @type.setter
    def type(self, value: int):
        """
        :param int value:
        """

        self.hole.Type = value

    def create_standard_thread_design_table(self, i_standard_type: int) -> None:
        """
        .. note::
            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub CreateStandardThreadDesignTable(CatHoleThreadStandard
                | iStandardType)
                | 
                |     Creates a Standard Thread design table .
                |     This call is valid when the hole threading mode is : CATThreadedHoleThreading.
                | 
                |     Parameters:
                | 
                |         iStandardType
                |             Standard type for thread (see 
                | 
                |         CatHoleThreadStandard for list of possible types)
                | 
                |         Example:
                |             The following example creates a standard table for MetricThinPitch
                |             for hole firstHole:
                | 
                |              firstHole.CreateStandardThreadDesignTable
                |              catHoleMetricThinPitch

        :param int i_standard_type:
        :return: None
        :rtype: None
        """
        return self.hole.CreateStandardThreadDesignTable(i_standard_type)

    def create_user_standard_design_table(self, i_standard_name: str, i_path: str) -> None:
        """
        .. note::
            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub CreateUserStandardDesignTable(CATBSTR iStandardName,
                | CATBSTR iPath)
                | 
                |     Creates a UserStandard Thread design table .
                |     This call is valid when the hole threading mode is : CATThreadedHoleThreading.
                | 
                |     Parameters:
                | 
                |         iStandardName
                |             Name of the UserStandard thread. iStandardName should be empty if
                |             filepath is to be defined. 
                |         iPath
                |             Path of the UserStandard file. iPath is empty if the filepath is
                |             already defined through CATReffilesPath.
                | 
                |             Example1:
                |                 The following example creates a standard table for UserStandard
                |                 for hole firstHole. The file path is already defined thru
                |                 CATReffilesPath:
                | 
                |                  firstHole.CreateUserStandardDesignTable
                |                  "UserStandard",""
                | 
                |             Example2:
                |                 The following example creates a standard table for UserStandard
                |                 for hole firstHole when file path is not defined thru
                |                 CATReffilesPath:
                | 
                |                  firstHole.CreateUserStandardDesignTable
                |                  "","E:\\user\\standard\\UserStandard.txt"

        :param str i_standard_name:
        :param str i_path:
        :return: None
        :rtype: None
        """
        return self.hole.CreateUserStandardDesignTable(i_standard_name, i_path)

    def get_direction(self, io_direction: tuple) -> None:
        """
        .. note::
            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub GetDirection(CATSafeArrayVariant ioDirection)
                | 
                |     Returns the hole direction with absolute coordinates.
                |     It provides a safe array with 3 elements : X, Y, Z direction coordinates
                | 
                |     Returns:
                |         oDirection The direction coordinates
                | 
                |         Example:
                |             The following example returns in dirArray the direction coordinates
                |             of hole firstHole:
                | 
                |              Call firstHole.GetDirection dirArray
                |              Set x = dirArray[1]
                |              Set y = dirArray[2]
                |              Set z = dirArray[3]

        :param tuple io_direction:
        :return: None
        :rtype: None
        """
        return self.hole.GetDirection(io_direction)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_direction'
        # # vba_code = """
        # # Public Function get_direction(hole)
        # #     Dim ioDirection (2)
        # #     hole.GetDirection ioDirection
        # #     get_direction = ioDirection
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_origin(self, io_origin: tuple) -> None:
        """
        .. note::
            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub GetOrigin(CATSafeArrayVariant ioOrigin)
                | 
                |     Returns the origin point which the hole is anchored to.
                |     This point belongs to a tangent plane.
                | 
                |     Returns:
                |         oOrigin A Safe Array made up of 3 doubles : X, Y, Z - Hole origin point coordinates
                | 
                |         Example:
                |             The following example returns in coordArray the coordinates of hole
                |             firstHole:
                | 
                |              Call firstHole.GetOrigin coordArray
                |              Set x = coordArray[1]
                |              Set y = coordArray[2]
                |              Set z = coordArray[3]

        :param tuple io_origin:
        :return: None
        :rtype: None
        """
        return self.hole.GetOrigin(io_origin)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_origin'
        # # vba_code = """
        # # Public Function get_origin(hole)
        # #     Dim ioOrigin (2)
        # #     hole.GetOrigin ioOrigin
        # #     get_origin = ioOrigin
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def reverse(self) -> None:
        """
        .. note::
            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub Reverse()
                | 
                |     Reverses the hole direction .
                | 
                |     Example:
                |         The following example reverses the current direction of hole
                |         firstHole:
                | 
                |          firstHole.Reverse()

        :return: None
        :rtype: None
        """
        return self.hole.Reverse()

    def set_direction(self, i_direction: Reference) -> None:
        """
        .. note::
            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetDirection(Reference iDirection)
                | 
                |     Sets the hole associative direction.
                | 
                |     Parameters:
                | 
                |         iDirection
                |             A Reference object to an edge or a line (see 
                | 
                |         Reference for more information)
                |         The following Boundary objects are supported:
                |         RectilinearTriDimFeatEdge, RectilinearBiDimFeatEdge and
                |         RectilinearMonoDimFeatEdge.
                | 
                |         Example:
                |             The following example sets the support direction of hole firstHole
                |             with holeDirRef direction reference :
                | 
                |              firstHole.SetDirection holeDirref

        :param Reference i_direction:
        :return: None
        :rtype: None
        """
        return self.hole.SetDirection(i_direction.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_direction'
        # # vba_code = """
        # # Public Function set_direction(hole)
        # #     Dim iDirection (2)
        # #     hole.SetDirection iDirection
        # #     set_direction = iDirection
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_origin(self, i_x: float, i_y: float, i_z: float) -> None:
        """
        .. note::
            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetOrigin(double iX,
                | double iY,
                | double iZ)
                | 
                |     Sets the origin point which the hole is anchored to.
                |     If mandatory, the entry point will be projected onto a tangent
                |     plane.
                | 
                |     Parameters:
                | 
                |         iX
                |             Origin point x absolute coordinate 
                |         iY
                |             Origin point y absolute coordinate 
                |         iZ
                |             Origin point z absolute coordinate
                | 
                |             Example:
                |                 The following example sets the coordinates of hole firstHole to
                |                 10., 20., -5. :
                | 
                |                  firstHole.SetOrigin 10., 20., 5.

        :param float i_x:
        :param float i_y:
        :param float i_z:
        :return: None
        :rtype: None
        """
        return self.hole.SetOrigin(i_x, i_y, i_z)

    def __repr__(self):
        return f'Hole(name="{self.name}")'
