#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
import inspect

from pycatia.drafting_interfaces.drawing_arrows import DrawingArrows
from pycatia.drafting_interfaces.drawing_components import DrawingComponents
from pycatia.drafting_interfaces.drawing_coord_dims import DrawingCoordDims
from pycatia.drafting_interfaces.drawing_dimensions import DrawingDimensions
from pycatia.drafting_interfaces.drawing_gdts import DrawingGDTs
from pycatia.drafting_interfaces.drawing_pictures import DrawingPictures
from pycatia.drafting_interfaces.drawing_tables import DrawingTables
from pycatia.drafting_interfaces.drawing_texts import DrawingTexts
from pycatia.drafting_interfaces.drawing_threads import DrawingThreads
from pycatia.drafting_interfaces.drawing_weldings import DrawingWeldings
from pycatia.mec_mod_interfaces.geometric_elements import GeometricElements
from pycatia.sketcher_interfaces.factory_2D import Factory2D
from pycatia.system_interfaces.any_object import AnyObject


class Layout2DView(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     Layout2DView
                | 
                | The interface to access a Layout2D View.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.layout_2d_view = com_object

    @property
    def angle(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Angle() As double
                | 
                |     Returns or sets the angle of the Layout2D view. The angle is measured
                |     between the axis system of the Layout2D view and the axis system of the
                |     Layout2D sheet where the Layout2D view lies. The angle is measured in radians
                |     and is counted counterclockwise.
                | 
                |     Example:
                |         This example sets the angle of the MyView Layout2D view to 90 degrees
                |         clockwise. You first need to compute the angle in radians and set the minus
                |         sign to indicate the rotation is clockwise.
                | 
                |          PI = 3.1415926535
                |          Angle90Clockwise = -PI/2
                |          MyView.Angle = Angle90Clockwise

        :rtype: float
        """

        return self.layout_2d_view.Angle

    @angle.setter
    def angle(self, value: float):
        """
        :param float value:
        """

        self.layout_2d_view.Angle = value

    @property
    def arrows(self) -> DrawingArrows:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Arrows() As DrawingArrows (Read Only)
                | 
                |     Returns the drawing arrow collection of the Layout2D view.
                | 
                |     Example:
                |         This example retrieves in ArrowCollection the collection of arrows of
                |         the MyView Layout2D view.
                | 
                |          Dim ArrowCollection As DrawingArrows
                |          Set ArrowCollection = MyView.Arrows

        :rtype: DrawingArrows
        """

        return DrawingArrows(self.layout_2d_view.Arrows)

    @property
    def components(self) -> DrawingComponents:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Components() As DrawingComponents (Read Only)
                | 
                |     Returns the Layout2D component instances collection (i.e. ditto collection)
                |     of the Layout2D view.
                | 
                |     Example:
                |         This example retrieves in ComponentCollection the collection of
                |         component instances of the MyView Layout2D view.
                | 
                |          Dim ComponentCollection As DrawingComponents
                |          Set ComponentCollection = MyView.Components

        :rtype: DrawingComponents
        """

        return DrawingComponents(self.layout_2d_view.Components)

    @property
    def coord_dims(self) -> DrawingCoordDims:
        """

        Introduced in V5-6R2018.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2024-08-20 16:04:57.203445)
                | Property CoordDims() As DrawingCoordDims (Read Only)
                |     Returns the drawing CoordDim collection of the Layout2D
                |     view.
                |
                |     Example:
                |         This example retrieves in CoordDimCollection the collection of
                |         CoordDims of the MyView Layout2D view.
                |
                |          Dim CoordDimCollection As DrawingCoordDims
                |          Set CoordDimCollection = MyView.CoordDims

        :rtype: DrawingCoordDims
        """

        self.release_check(
            self.application.system_configuration.release,
            28,
            f'{self.__class__.__name__}.{inspect.stack()[0][3]}',
        )

        return DrawingCoordDims(self.layout_2d_view.CoordDims)

    @property
    def dimensions(self) -> DrawingDimensions:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Dimensions() As DrawingDimensions (Read Only)
                | 
                |     Returns the drawing dimension collection of the Layout2D
                |     view.
                | 
                |     Example:
                |         This example retrieves in DimensionCollection the collection of
                |         dimensions of the MyView Layout2D view.
                | 
                |          Dim DimensionCollection As DrawingDimensions
                |          Set DimensionCollection = MyView.Dimensions

        :rtype: DrawingDimensions
        """

        return DrawingDimensions(self.layout_2d_view.Dimensions)

    @property
    def factory_2d(self) -> Factory2D:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Factory2D() As Factory2D (Read Only)
                | 
                |     Returns the 2D factory of the Layout2D view. Take care that you must open
                |     edition on a sketch before adding or modifying elements in it. Take care that
                |     you must close edition on a sketch to keep all modifications before saving
                |     document. To get Sketch from factory2D:
                | 
                |       Set mySketch = my2DFactory.GetParent
                |      
                | 
                |     Example:
                |         The following example returns in my2DFactory the 2D
                |         factory
                |         of the view myView:
                | 
                |          Set my2DFactory = myView.Factory2D

        :rtype: Factory2D
        """

        return Factory2D(self.layout_2d_view.Factory2D)

    @property
    def frame_visualization(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property FrameVisualization() As boolean
                | 
                |     Returns or sets the Layout2D view frame visualization
                |     state.
                |     True if the Layout2D view frame is visible.
                | 
                |     Example:
                |         This example shows the frame of the MyView Layout2D
                |         view.
                | 
                |          MyView.FrameVisualization = True

        :rtype: bool
        """

        return self.layout_2d_view.FrameVisualization

    @frame_visualization.setter
    def frame_visualization(self, value: bool):
        """
        :param bool value:
        """

        self.layout_2d_view.FrameVisualization = value

    @property
    def gdts(self) -> DrawingGDTs:
        """

        Introduced in V5-6R2018.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2024-08-20 16:04:57.203445)
                | Property GDTs() As DrawingGDTs (Read Only)
                |     Returns the drawing GDT collection of the Layout2D view.
                |
                |     Example:
                |         This example retrieves in GDTCollection the collection of GDTs of the
                |         MyView Layout2D view.
                |
                |          Dim GDTCollection As DrawingGDTs
                |          Set GDTCollection = MyView.GDTs

        :rtype: DrawingGDTs
        """

        self.release_check(
            self.application.system_configuration.release,
            28,
            f'{self.__class__.__name__}.{inspect.stack()[0][3]}',
        )

        return DrawingGDTs(self.layout_2d_view.GDTs)

    @property
    def geometric_elements(self) -> GeometricElements:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property GeometricElements() As GeometricElements (Read
                | Only)
                | 
                |     Returns the collection of geometric elements included in the Layout2D view
                |     sketch.
                | 
                |     Example:
                |         The following example returns in colGeometry the list of geometric
                |         elements in the view myView:
                | 
                |          Dim colGeometry As GeometricElements
                |          Set colGeometry = MyView.GeometricElements

        :rtype: GeometricElements
        """

        return GeometricElements(self.layout_2d_view.GeometricElements)

    @property
    def lock_status(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property LockStatus() As boolean
                | 
                |     Returns or sets the lock status of a Layout2D view.
                |     precondition: This property does not exist for the detail view. In this
                |     case, the method returns failed.
                | 
                |     Example:
                |         This example locks the ViewToWorkOn Layout2D view.
                | 
                |          ViewToWorkOn.LockStatus = True

        :rtype: bool
        """

        return self.layout_2d_view.LockStatus

    @lock_status.setter
    def lock_status(self, value: bool):
        """
        :param bool value:
        """

        self.layout_2d_view.LockStatus = value

    @property
    def pictures(self) -> DrawingPictures:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Pictures() As DrawingPictures (Read Only)
                | 
                |     Returns the drawing picture collection of the Layout2D
                |     view.
                | 
                |     Example:
                |         This example retrieves in PictureCollection the collection of pictures
                |         of the MyView Layout2D view.
                | 
                |          Dim PictureCollection As DrawingPictures
                |          Set PictureCollection = MyView.Pictures

        :rtype: DrawingPictures
        """

        return DrawingPictures(self.layout_2d_view.Pictures)

    @property
    def reference_view(self) -> 'Layout2DView':
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ReferenceView() As Layout2DView
                | 
                |     Returns or sets the reference view. The reference view is also the parent
                |     view to which the current Layout2D view is linked and which is used as
                |     reference for alignment. Generally, the reference view is the front view, and
                |     the other views, such as the top, bottom, left, and right views, are linked to
                |     it. This reference Layout2D view is used:
                | 
                |         When moving the current Layout2D view. Its location remains constrained
                |         to the reference view, depending on its type. For example, a left view can move
                |         horizontally and a top view can move vertically.
                |         To update the scale of the current Layout2D view according to the
                |         modification performed to the one of the reference Layout2D
                |         view.
                | 
                |     Example:
                |         This example retrieves in ReferenceView the view used as reference by
                |         the MyView Layout2D view.
                | 
                |          Dim ReferenceView As Layout2DView
                |          Set ReferenceView = MyView.RefView

        :rtype: Layout2DView
        """

        return Layout2DView(self.layout_2d_view.ReferenceView)

    @reference_view.setter
    def reference_view(self, value: 'Layout2DView'):
        """
        :param Layout2DView value:
        """

        self.layout_2d_view.ReferenceView = value

    @property
    def tables(self) -> DrawingTables:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Tables() As DrawingTables (Read Only)
                | 
                |     Returns the drawing table collection of the drawing view.
                | 
                |     Example:
                |         This example retrieves in TextCollection the collection of texts of the
                |         MyView Layout2D view.
                | 
                |          Dim TableCollection As DrawingTables
                |          Set TableCollection = MyView.Tables

        :rtype: DrawingTables
        """

        return DrawingTables(self.layout_2d_view.Tables)

    @property
    def texts(self) -> DrawingTexts:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Texts() As DrawingTexts (Read Only)
                | 
                |     Returns the drawing text collection of the Layout2D view.
                | 
                |     Example:
                |         This example retrieves in TextCollection the collection of texts of the
                |         MyView Layout2D view.
                | 
                |          Dim TextCollection As DrawingTexts
                |          Set TextCollection = MyView.Texts

        :rtype: DrawingTexts
        """

        return DrawingTexts(self.layout_2d_view.Texts)

    @property
    def threads(self) -> DrawingThreads:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Threads() As DrawingThreads (Read Only)
                | 
                |     Returns the drawing thread collection of the Layout2D
                |     view.
                | 
                |     Example:
                |         This example retrieves in ThreadCollection the collection of threads of
                |         the MyView Layout2D view.
                | 
                |          Dim ThreadCollection As DrawingThreads
                |          Set ThreadCollection = MyView.Threads

        :rtype: DrawingThreads
        """

        return DrawingThreads(self.layout_2d_view.Threads)

    @property
    def view_scale(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ViewScale() As double
                | 
                |     Returns or sets the scale of the Layout2D view.
                | 
                |     Example:
                |         This example sets the scale of the MyView Layout2D view to
                |         0.5.
                | 
                |          MyView.Scale = 0.5

        :rtype: float
        """

        return self.layout_2d_view.ViewScale

    @view_scale.setter
    def view_scale(self, value: float):
        """
        :param float value:
        """

        self.layout_2d_view.ViewScale = value

    @property
    def visu_2d_mode(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Visu2DMode() As CatView2DModeVisu
                | 
                |     Sets/Gets the 2D mode for background visualization of the
                |     view.
                | 
                |     See also:
                |         CatView2DModeVisu 
                |     Example:
                |
                |              This example shows how to switch on the background 2D
                |              mode
                |
                |              View1.Visu2DMode = catView2DModeNoShow

        :return: enum cat_view_2d_mode_visu
        :rtype: int
        """

        return self.layout_2d_view.Visu2DMode

    @visu_2d_mode.setter
    def visu_2d_mode(self, value: int):
        """
        :param int value: enum cat_view_2d_mode_visu
        """

        self.layout_2d_view.Visu2DMode = value

    @property
    def visu_background(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property VisuBackground() As CatVisuBackgroundMode
                | 
                |     Sets/Gets the 2D-3D background visu mode of the view ie in the 3D windows
                |     and in the background of each view in every 2D context.
                | 
                |     See also:
                |         CatVisuBackgroundMode 
                |     Example:
                | 
                |           
                | 
                |              This example shows how to set the background to
                |              LowInt
                |              
                | 
                |              View1.VisuBackground = catLowIntPick

        :return: enum cat_visu_background_mode
        :rtype: int
        """

        return self.layout_2d_view.VisuBackground

    @visu_background.setter
    def visu_background(self, value: int):
        """
        :param int value: enum cat_visu_background_mode
        """

        self.layout_2d_view.VisuBackground = value

    @property
    def visu_in_3d(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property VisuIn3D() As CatVisuIn3DMode
                | 
                |     Sets/Gets the 3D visualization mode of the view in the 3D Viewer ie in the
                |     3D windows and in the background of each view in every 2D
                |     context.
                | 
                |     See also:
                |         CatVisuIn3DMode 
                |     Example:
                | 
                |              This example shows how to make the View1 Layout2D view visible in
                |              3D
                |
                |              View1.HideIn3DSize = catShowAll

        :return: enum cat_visu_in_3d_mode
        :rtype: int
        """

        return self.layout_2d_view.VisuIn3D

    @visu_in_3d.setter
    def visu_in_3d(self, value: int):
        """
        :param int value: enum cat_visu_in_3d_mode
        """

        self.layout_2d_view.VisuIn3D = value

    @property
    def weldings(self) -> DrawingWeldings:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Weldings() As DrawingWeldings (Read Only)
                | 
                |     Returns the drawing welding collection of the Layout2D
                |     view.
                | 
                |     Example:
                |         This example retrieves in weldingCollection the collection of weldings
                |         of the MyView Layout2D view.
                | 
                |          Dim weldingCollection As DrawingWeldings
                |          Set weldingCollection = MyView.Weldings

        :rtype: DrawingWeldings
        """

        return DrawingWeldings(self.layout_2d_view.Weldings)

    @property
    def x(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property x() As double
                | 
                |     Returns or sets the x coordinate of the Layout2D view coordinate system
                |     origin. It is expressed with respect to the sheet coordinate system. This
                |     coordinate, like any length, is measured in millimeters.
                | 
                |     Example:
                |         This example retrieves the x coordinate of the coordinate system origin
                |         of the MyView.
                | 
                |          X = MyView.x

        :rtype: float
        """

        return self.layout_2d_view.x

    @x.setter
    def x(self, value: float):
        """
        :param float value:
        """

        self.layout_2d_view.x = value

    @property
    def y(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property y() As double
                | 
                |     Returns or sets the y coordinate of the Layout2D view coordinate system
                |     origin. It is expressed with respect to the sheet coordinate system. This
                |     coordinate, like any length, is measured in millimeters.
                | 
                |     Example:
                |         This example sets the y coordinate of the coordinate system origin of
                |         the MyView to 5 inches. You need first to convert the 5 inches into
                |         millimeters.
                | 
                |          NewYCoordinate = 5*25.4
                |          MyView.y = NewYCoordinate

        :rtype: float
        """

        return self.layout_2d_view.y

    @y.setter
    def y(self, value: float):
        """
        :param float value:
        """

        self.layout_2d_view.y = value

    def activate(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub Activate()
                | 
                |     Activates the Layout2D view. Activating a Layout2D view means that this
                |     Layout2D view is the one on which the end-user is now
                |     working.
                | 
                |     Example:
                |         This example activates the ViewToWorkOn Layout2D view.
                | 
                |          ViewToWorkOn.Activate()

        :rtype: None
        """
        return self.layout_2d_view.Activate()

    def aligned_with_reference_view(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub AlignedWithReferenceView()
                | 
                |     Activates the alignment with the reference view. Activating the alignment
                |     with the reference view restores the constraints that the reference view
                |     imposes to the current Layout2D view.
                | 
                |     Example:
                |         This example activates the alignment from the MyView Layout2D view to
                |         its reference view.
                | 
                |          MyView.AlignedWithReferenceView()

        :rtype: None
        """
        return self.layout_2d_view.AlignedWithReferenceView()

    def get_view_name(self, i_view_name_prefix: str, i_view_name_ident: str, i_view_name_suffix: str) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetViewName(CATBSTR iViewNamePrefix,
                | CATBSTR iViewNameIdent,
                | CATBSTR iViewNameSuffix)
                | 
                |     Returns the prefix, the ident and the suffix of the name of the Layout2D
                |     view. The method returns an error in case of 2D component reference. Do not
                |     confuse with the method Name which can be different.
                | 
                |     Example:
                | 
                |           This example gets the prefix, the ident, and the suffix of the name
                |           
                |          of the MyView Layout2D view
                |          
                | 
                |          Dim MyPrefix, MyIdent, MySuffix As CATBSTR
                |          MyView.GetViewName (MyPrefix, MyIdent, MySuffix)

        :param str i_view_name_prefix:
        :param str i_view_name_ident:
        :param str i_view_name_suffix:
        :rtype: None
        """
        return self.layout_2d_view.GetViewName(i_view_name_prefix, i_view_name_ident, i_view_name_suffix)

    def save_edition(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SaveEdition()
                | 
                |     Saves the Sketch Edition. Once you have finished working with the Layout2D
                |     view, you must save its edition in order to register modification for
                |     UNDO/REDO. Indeed when activating a view, this view is open in edition while
                |     the previous active view is closed in edition. So calling SaveEdition() before
                |     exiting a macro without changing active view will allow a correct UNDO/REDO
                |     behavior.
                | 
                |     Example:
                |         The following example saves the edition of the Layout2D view
                |         MyView:
                | 
                |          MyView.SaveEdition

        :rtype: None
        """
        return self.layout_2d_view.SaveEdition()

    def set_view_name(self, i_view_name_prefix: str, i_view_name_ident: str, i_view_name_suffix: str) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetViewName(CATBSTR iViewNamePrefix,
                | CATBSTR iViewNameIdent,
                | CATBSTR iViewNameSuffix)
                | 
                |     Sets the prefix, the ident and the suffix of the name of the Layout2D view.
                |     The method returns an error in case of 2D component reference. Do not confuse
                |     with the method Name which can be different.
                | 
                |     Example:
                | 
                |           This example sets the prefix, the ident, and the suffix of the name
                |           
                |          of the MyView Layout2D view respectively to "MyPrefix",
                |          "MyIdent",
                |          and "MySuffix".
                |          
                | 
                |          MyView.SetViewName ("MyPrefix", "MyIdent",
                |          "MySuffix")

        :param str i_view_name_prefix:
        :param str i_view_name_ident:
        :param str i_view_name_suffix:
        :rtype: None
        """
        return self.layout_2d_view.SetViewName(i_view_name_prefix, i_view_name_ident, i_view_name_suffix)

    def size(self, o_values: tuple) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub Size(CATSafeArrayVariant oValues)
                | 
                |     Returns the bounding box of the Layout2D view.
                |     Warning: This method is not implemented.
                | 
                |     Parameters:
                | 
                |         oValues
                |             The values of the view bounding box: Xmin, Xmax, Ymin, Ymax
                |             
                | 
                |     Example:
                | 
                |           
                | 
                |              This example gets the bounding box of the ViewToWorkOn Layout2D
                |              view.
                |              
                | 
                |              Dim oXY(4) As Double
                |              ViewToWorkOn.Size oXY
                |              Xmin = oXY(0)
                |              Xmax = oXY(1)
                |              Ymin = oXY(2)
                |              Ymax = oXY(3)

        :param tuple o_values:
        :rtype: Double
        """
        return self.layout_2d_view.Size(o_values)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'size'
        # # vba_code = """
        # # Public Function size(layout2_d_view)
        # #     Dim oValues (2)
        # #     layout2_d_view.Size oValues
        # #     size = oValues
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def un_aligned_with_reference_view(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub UnAlignedWithReferenceView()
                | 
                |     Deactivates the alignment with the reference view. Deactivating the
                |     alignment to the reference view removes the constraints that the reference view
                |     imposes to the current Layout2D view. You can then, for example, move and
                |     position it freely.
                | 
                |     Example:
                |         This example deactivates the alignment from the MyView Layout2D view to
                |         its reference view.
                | 
                |          MyView.UnAlignedWithReferenceView()

        :rtype: None
        """
        return self.layout_2d_view.UnAlignedWithReferenceView()

    def __repr__(self):
        return f'Layout2DView(name="{self.name}")'
