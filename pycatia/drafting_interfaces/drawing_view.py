#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
import inspect
from typing import TYPE_CHECKING, Tuple

from pycatia.drafting_interfaces.drawing_arrows import DrawingArrows
from pycatia.drafting_interfaces.drawing_components import DrawingComponents
from pycatia.drafting_interfaces.drawing_coord_dims import DrawingCoordDims
from pycatia.drafting_interfaces.drawing_dimensions import DrawingDimensions
from pycatia.drafting_interfaces.drawing_gdts import DrawingGDTs
from pycatia.drafting_interfaces.drawing_pictures import DrawingPictures
from pycatia.drafting_interfaces.drawing_tables import DrawingTables
from pycatia.drafting_interfaces.drawing_texts import DrawingTexts
from pycatia.drafting_interfaces.drawing_threads import DrawingThreads
from pycatia.drafting_interfaces.drawing_view_generative_behavior import DrawingViewGenerativeBehavior
from pycatia.drafting_interfaces.drawing_view_generative_links import DrawingViewGenerativeLinks
from pycatia.drafting_interfaces.drawing_weldings import DrawingWeldings
from pycatia.mec_mod_interfaces.geometric_elements import GeometricElements
from pycatia.sketcher_interfaces.factory_2D import Factory2D
from pycatia.system_interfaces.any_object import AnyObject

if TYPE_CHECKING:
    from pycatia.drafting_interfaces.drawing_text import DrawingText


class DrawingView(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     DrawingView
                | 
                | Represents a drawing view in a drawing sheet.
                | 
                | The drawing view is included in a drawing sheet and contains texts,leaders,
                | dimensions, arrows, pictures, tables, 2D Geometry and 2D
                | component.
                | Warning: This interface is not available with 2D Layout for 3D
                | Design.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.drawing_view = com_object

    @property
    def angle(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property Angle() As double
                | 
                |     Returns or sets the angle of the drawing view. The angle is measured
                |     between the axis system of the drawing view and the axis system of the drawing
                |     sheet where the drawing view lies. The angle is measured in radians and is
                |     counted counterclockwise.
                |     Warning: This method is not available with 2D Layout for 3D
                |     Design.
                | 
                |     Example:
                |         This example sets the angle of the MyView drawing view to 90 degrees
                |         clockwise. You first need to compute the angle in radians and set the minus
                |         sign to indicate the rotation is clockwise.
                | 
                |          PI = 3.1415926535
                |          Angle90Clockwise = -PI/2
                |          MyView.Angle = Angle90Clockwise

        :rtype: float
        """

        return self.drawing_view.Angle

    @angle.setter
    def angle(self, value: float):
        """
        :param float value:
        """

        self.drawing_view.Angle = value

    @property
    def arrows(self) -> DrawingArrows:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property Arrows() As DrawingArrows (Read Only)
                | 
                |     Returns the drawing arrow collection of the drawing view.
                |     Warning: This method is not available with 2D Layout for 3D
                |     Design.
                | 
                |     Example:
                |         This example retrieves in ArrowCollection the collection of arrows of
                |         the MyView drawing view.
                | 
                |          Dim ArrowCollection As DrawingArrows
                |          Set ArrowCollection = MyView.Arrows

        :rtype: DrawingArrows
        """

        return DrawingArrows(self.drawing_view.Arrows)

    @property
    def components(self) -> DrawingComponents:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property Components() As DrawingComponents (Read Only)
                | 
                |     Returns the drawing component instances collection (i.e. ditto collection)
                |     of the drawing view.
                |     Warning: This method is not available with 2D Layout for 3D
                |     Design.
                | 
                |     Example:
                |         This example retrieves in ComponentCollection the collection of
                |         component instances of the MyView drawing view.
                | 
                |          Dim ComponentCollection As DrawingComponents
                |          Set ComponentCollection = MyView.Components

        :rtype: DrawingComponents
        """

        return DrawingComponents(self.drawing_view.Components)

    @property
    def coord_dims(self) -> DrawingCoordDims:
        """

        Introduced in V5-6R2018.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2024-08-20 16:04:57.203445)
                | Property CoordDims() As DrawingCoordDims (Read Only)
                |     Returns the drawing CoordDim collection of the drawing
                |     view.
                |     Warning: This method is not available with 2D Layout for 3D
                |     Design.
                |
                |     Example:
                |         This example retrieves in CoordDimCollection the collection of
                |         CoordDims of the MyView drawing view.
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

        return DrawingCoordDims(self.drawing_view.CoordDims)

    @property
    def dimensions(self) -> DrawingDimensions:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property Dimensions() As DrawingDimensions (Read Only)
                | 
                |     Returns the drawing dimension collection of the drawing
                |     view.
                |     Warning: This method is not available with 2D Layout for 3D
                |     Design.
                | 
                |     Example:
                |         This example retrieves in DimensionCollection the collection of
                |         dimensions of the MyView drawing view.
                | 
                |          Dim DimensionCollection As DrawingDimensions
                |          Set DimensionCollection = MyView.Dimensions

        :rtype: DrawingDimensions
        """

        return DrawingDimensions(self.drawing_view.Dimensions)

    @property
    def factory_2d(self) -> Factory2D:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property Factory2D() As Factory2D (Read Only)
                | 
                |     Returns the 2D factory of the drawing view. Take care that you must open
                |     edition on a sketch before adding or modifying elements in it. Take care that
                |     you must close edition on a sketch to keep all modifications before saving
                |     document.
                |     Warning: This method is not available with 2D Layout for 3D Design. To get
                |     Sketch from factory2D:
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

        return Factory2D(self.drawing_view.Factory2D)

    @property
    def frame_visualization(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property FrameVisualization() As boolean
                | 
                |     Returns or sets the drawing view frame visualization
                |     state.
                |     True if the drawing view frame is visible.
                |     Warning: This method is not available with 2D Layout for 3D
                |     Design.
                | 
                |     Example:
                |         This example shows the frame of the MyView drawing
                |         view.
                | 
                |          MyView.FrameVisualization = True

        :rtype: bool
        """

        return self.drawing_view.FrameVisualization

    @frame_visualization.setter
    def frame_visualization(self, value: bool):
        """
        :param bool value:
        """

        self.drawing_view.FrameVisualization = value

    @property
    def gdts(self) -> DrawingGDTs:
        """

        Introduced in V5-6R2018.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2024-08-20 16:04:57.203445)
                | Property GDTs() As DrawingGDTs (Read Only)
                |     Returns the drawing GDT collection of the drawing view.
                |     Warning: This method is not available with 2D Layout for 3D
                |     Design.
                |
                |     Example:
                |         This example retrieves in GDTCollection the collection of GDTs of the
                |         MyView drawing view.
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

        return DrawingGDTs(self.drawing_view.GDTs)

    @property
    def generative_behavior(self) -> DrawingViewGenerativeBehavior:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property GenerativeBehavior() As DrawingViewGenerativeBehavior (Read
                | Only)
                | 
                |     Returns the generative behavior of the drawing view.
                |     Warning: This method is not available with 2D Layout for 3D
                |     Design.
                | 
                |     Example:
                |         This example retrieves in MyViewGenBehavior the generative behavior of
                |         the MyView drawing view.
                | 
                |          Dim MyViewGenBehavior As
                |          DrawingViewGenerativeBehavior
                |          Set MyViewGenBehavior = MyView.GenerativeBehavior

        :rtype: DrawingViewGenerativeBehavior
        """

        return DrawingViewGenerativeBehavior(self.drawing_view.GenerativeBehavior)

    @property
    def generative_links(self) -> DrawingViewGenerativeLinks:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property GenerativeLinks() As DrawingViewGenerativeLinks (Read
                | Only)
                | 
                |     Returns the generative links of the drawing view.
                |     Warning: This method is not available with 2D Layout for 3D
                |     Design.
                | 
                |     Example:
                |         This example retrieves in MyViewGenLinks the generative links of the
                |         MyView drawing view.
                | 
                |          Dim MyViewGenLinks As DrawingViewGenerativeLinks
                |          Set MyViewGenLinks = MyView.GenerativeLinks

        :rtype: DrawingViewGenerativeLinks
        """

        return DrawingViewGenerativeLinks(self.drawing_view.GenerativeLinks)

    @property
    def geometric_elements(self) -> GeometricElements:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property GeometricElements() As GeometricElements (Read
                | Only)
                | 
                |     Returns the collection of geometric elements included in the drawing view
                |     sketch.
                |     Warning: This method is not available with 2D Layout for 3D
                |     Design.
                | 
                |     Example:
                |         The following example returns in colGeometry the list of geometric
                |         elements in the view myView:
                | 
                |          Dim colGeometry As GeometricElements
                |          Set colGeometry = myView.GeometricElements

        :rtype: GeometricElements
        """

        return GeometricElements(self.drawing_view.GeometricElements)

    @property
    def lock_status(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property LockStatus() As boolean
                | 
                |     Returns or sets the lock status of a drawing view.
                |     Warning: This method is not available with 2D Layout for 3D
                |     Design.
                |     precondition: This property does not exist for the detail view. In this
                |     case, the method returns failed.
                | 
                |     Example:
                |         This example locks the ViewToWorkOn drawing view.
                | 
                |          ViewToWorkOn.LockStatus = True

        :rtype: bool
        """

        return self.drawing_view.LockStatus

    @lock_status.setter
    def lock_status(self, value: bool):
        """
        :param bool value:
        """

        self.drawing_view.LockStatus = value

    @property
    def pictures(self) -> DrawingPictures:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property Pictures() As DrawingPictures (Read Only)
                | 
                |     Returns the drawing picture collection of the drawing
                |     view.
                |     Warning: This method is not available with 2D Layout for 3D
                |     Design.
                | 
                |     Example:
                |         This example retrieves in PictureCollection the collection of pictures
                |         of the MyView drawing view.
                | 
                |          Dim PictureCollection As DrawingPictures
                |          Set PictureCollection = MyView.Pictures

        :rtype: DrawingPictures
        """

        return DrawingPictures(self.drawing_view.Pictures)

    @property
    def reference_view(self) -> 'DrawingView':
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property ReferenceView() As DrawingView
                | 
                |     Returns or sets the reference view. The reference view is also the parent
                |     view to which the current drawing view is linked and which is used as reference
                |     for alignment. Generally, the reference view is the front view, and the other
                |     views, such as the top, bottom, left, and right views, are linked to it. This
                |     reference drawing view is used:
                | 
                |         When moving the current drawing view. Its location remains constrained
                |         to the reference view, depending on its type. For example, a left view can move
                |         horizontally and a top view can move vertically.
                |         To update the scale of the current drawing view according to the
                |         modification performed to the one of the reference drawing
                |         view.
                | 
                | 
                |     Warning: This method is not available with 2D Layout for 3D
                |     Design.
                | 
                |     Example:
                |         This example retrieves in ReferenceView the view used as reference by
                |         the MyView drawing view.
                | 
                |          Dim ReferenceView As DrawingView
                |          Set ReferenceView = MyView.RefView

        :rtype: DrawingView
        """

        return DrawingView(self.drawing_view.ReferenceView)

    @reference_view.setter
    def reference_view(self, value: 'DrawingView'):
        """
        :param DrawingView value:
        """

        self.drawing_view.ReferenceView = value

    @property
    def scale(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property Scale() As double
                | 
                |     Returns or sets the scale of the drawing view.
                |     Warning: This method is not available with 2D Layout for 3D
                |     Design.
                | 
                |     Example:
                |         This example sets the scale of the MyView drawing view to
                |         0.5.
                | 
                |          MyView.Scale = 0.5

        :rtype: float
        """

        return self.drawing_view.Scale

    @scale.setter
    def scale(self, value: float):
        """
        :param float value:
        """

        self.drawing_view.Scale = value

    @property
    def scale2(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property Scale2() As double
                | 
                |     Returns or sets the scale of the drawing view (Workaround for VBA
                |     keyword).
                |     Warning: This method is not available with 2D Layout for 3D
                |     Design.
                | 
                |     Example:
                |         This example sets the scale of the MyView drawing view to
                |         0.5.
                | 
                |          MyView.Scale2 = 0.5

        :rtype: float
        """

        return self.drawing_view.Scale2

    @scale2.setter
    def scale2(self, value: float):
        """
        :param float value:
        """

        self.drawing_view.Scale2 = value

    @property
    def tables(self) -> DrawingTables:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property Tables() As DrawingTables (Read Only)
                | 
                |     Returns the drawing table collection of the drawing view.
                |     Warning: This method is not available with 2D Layout for 3D
                |     Design.
                | 
                |     Example:
                |         This example retrieves in TextCollection the collection of texts of the
                |         MyView drawing view.
                | 
                |          Dim TableCollection As DrawingTables
                |          Set TableCollection = MyView.Tables

        :rtype: DrawingTables
        """

        return DrawingTables(self.drawing_view.Tables)

    @property
    def texts(self) -> DrawingTexts:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property Texts() As DrawingTexts (Read Only)
                | 
                |     Returns the drawing text collection of the drawing view.
                |     Warning: This method is not available with 2D Layout for 3D
                |     Design.
                | 
                |     Example:
                |         This example retrieves in TextCollection the collection of texts of the
                |         MyView drawing view.
                | 
                |          Dim TextCollection As DrawingTexts
                |          Set TextCollection = MyView.Texts

        :rtype: DrawingTexts
        """

        return DrawingTexts(self.drawing_view.Texts)

    @property
    def threads(self) -> DrawingThreads:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property Threads() As DrawingThreads (Read Only)
                | 
                |     Returns the drawing thread collection of the drawing view.
                |     Warning: This method is not available with 2D Layout for 3D
                |     Design.
                | 
                |     Example:
                |         This example retrieves in ThreadCollection the collection of threads of
                |         the MyView drawing view.
                | 
                |          Dim ThreadCollection As DrawingThreads
                |          Set ThreadCollection = MyView.Threads

        :rtype: DrawingThreads
        """

        return DrawingThreads(self.drawing_view.Threads)

    @property
    def view_type(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property ViewType() As CatDrawingViewType (Read Only)
                | 
                |     Returns the drawing view type.
                |     Warning: This method is not available with 2D Layout for 3D Design.

        :return: enum cat_drawing_view_type
        :rtype: int
        """

        return self.drawing_view.ViewType

    @property
    def weldings(self) -> DrawingWeldings:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property Weldings() As DrawingWeldings (Read Only)
                | 
                |     Returns the drawing welding collection of the drawing
                |     view.
                |     Warning: This method is not available with 2D Layout for 3D
                |     Design.
                | 
                |     Example:
                |         This example retrieves in weldingCollection the collection of weldings
                |         of the MyView drawing view.
                | 
                |          Dim weldingCollection As DrawingWeldings
                |          Set weldingCollection = MyView.Weldings

        :rtype: DrawingWeldings
        """

        return DrawingWeldings(self.drawing_view.Weldings)

    @property
    def x(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property x() As double
                | 
                |     For an interactive view, get_x and put_x methods are equivalents to
                |     get_xAxisData, put_xAxisData In a generative case, get_x. put_x returns or sets
                |     the x coordinate of the projection of the 3D centre of gravity. It is expressed
                |     with respect to the sheet coordinate system. This coordinate, like any length,
                |     is measured in millimeters.
                |     Warning: This method is not available with 2D Layout for 3D
                |     Design.
                | 
                |     Example:
                |         This example retrieves the x coordinate of the view relative position
                |         MyView.
                | 
                |          X = MyView.x

        :rtype: float
        """

        return self.drawing_view.x

    @x.setter
    def x(self, value: float):
        """
        :param float value:
        """

        self.drawing_view.x = value

    @property
    def x_axis_data(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property xAxisData() As double
                | 
                |     Returns or sets the x coordinate of the drawing view coordinate system
                |     origin. It is expressed with respect to the sheet coordinate system. This
                |     coordinate, like any length, is measured in millimeters.
                |     Warning: This method is not available with 2D Layout for 3D
                |     Design.
                | 
                |     Example:
                |         This example retrieves the x coordinate of the coordinate system origin
                |         of the MyView drawing view.
                | 
                |          X = MyView.xAxisData

        :rtype: float
        """

        return self.drawing_view.xAxisData

    @x_axis_data.setter
    def x_axis_data(self, value: float):
        """
        :param float value:
        """

        self.drawing_view.xAxisData = value

    @property
    def y(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property y() As double
                | 
                |     For an interactive view, get_y and put_y methods are equivalents to
                |     get_yAxisData, put_yAxisData In a generative case, get_y. put_y returns or sets
                |     the y coordinate of the projection of the 3D centre of gravity. It is expressed
                |     with respect to the sheet coordinate system. This coordinate, like any length,
                |     is measured in millimeters.
                |     Warning: This method is not available with 2D Layout for 3D
                |     Design.
                | 
                |     Example:
                |         This example sets the y coordinate of the view relative position MyView
                |         to 5 inches. You need first to convert the 5 inches into
                |         millimeters.
                | 
                |          NewYCoordinate = 5*25.4
                |          MyView.y = NewYCoordinate

        :rtype: float
        """

        return self.drawing_view.y

    @y.setter
    def y(self, value: float):
        """
        :param float value:
        """

        self.drawing_view.y = value

    @property
    def y_axis_data(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property yAxisData() As double
                | 
                |     Returns or sets the y coordinate of the drawing view coordinate system
                |     origin. It is expressed with respect to the sheet coordinate system. This
                |     coordinate, like any length, is measured in millimeters.
                |     Warning: This method is not available with 2D Layout for 3D
                |     Design.
                | 
                |     Example:
                |         This example sets the y coordinate of the coordinate system origin of
                |         the MyView drawing view to 5 inches. You need first to convert the 5 inches
                |         into millimeters.
                | 
                |          NewYCoordinate = 5*25.4
                |          MyView.yAxisData = NewYCoordinate

        :rtype: float
        """

        return self.drawing_view.yAxisData

    @y_axis_data.setter
    def y_axis_data(self, value: float):
        """
        :param float value:
        """

        self.drawing_view.yAxisData = value

    def activate(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub Activate()
                | 
                |     Activates the drawing view. Activating a drawing view means that this
                |     drawing view is the one on which the end-user is now
                |     working.
                |     Warning: This method is not available with 2D Layout for 3D
                |     Design.
                | 
                |     Example:
                |         This example activates the ViewToWorkOn drawing view.
                | 
                |          ViewToWorkOn.Activate()

        :rtype: None
        """
        return self.drawing_view.Activate()

    def aligned_with_reference_view(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub AlignedWithReferenceView()
                | 
                |     Activates the alignment with the reference view. Activating the alignment
                |     with the reference view restores the constraints that the reference view
                |     imposes to the current drawing view.
                |     Warning: This method is not available with 2D Layout for 3D
                |     Design.
                | 
                |     Example:
                |         This example activates the alignment from the MyView drawing view to
                |         its reference view.
                | 
                |          MyView.AlignedWithReferenceView()

        :rtype: None
        """
        return self.drawing_view.AlignedWithReferenceView()

    def get_view_name(self, i_view_name_prefix: str, i_view_name_ident: str, i_view_name_suffix: str) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub GetViewName(CATBSTR iViewNamePrefix,
                | CATBSTR iViewNameIdent,
                | CATBSTR iViewNameSuffix)
                | 
                |     Returns the prefix, the ident and the suffix of the name of the drawing
                |     view. The method returns an error in case of 2D component
                |     reference.
                |     Note: Prefix of drawing view can be also retrieved across name property
                |     defined in CATIABase
                |     Warning: This method is not available with 2D Layout for 3D
                |     Design.
                | 
                |     Example:
                | 
                |           This example gets the prefix, the ident, and the suffix of the name
                |           
                |          of the MyView drawing view
                |          
                | 
                |          Dim MyPrefix, MyIdent, MySuffix As CATBSTR
                |          MyView.GetViewName (MyPrefix, MyIdent, MySuffix)

        :param str i_view_name_prefix:
        :param str i_view_name_ident:
        :param str i_view_name_suffix:
        :rtype: None
        """
        return self.drawing_view.GetViewName(i_view_name_prefix, i_view_name_ident, i_view_name_suffix)

    def insert_view_angle(self, i_first: int, io_text: 'DrawingText') -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub InsertViewAngle(long iFirst,
                | DrawingText ioText)
                | 
                |     Insert the Angle parameter in the text of the drawing
                |     text.
                |     Warning: This method is not available with 2D Layout for 3D
                |     Design.
                | 
                |     Parameters:
                | 
                |         iFirst
                |             The first character from which the parameter is inserted
                |             
                |         ioText
                |             The text on wich the scale parameter will be inserted
                |             
                |         Example:
                |             This example insert the Angle parameter of MyView drawing view at
                |             the end of MyText drawing text.
                | 
                | 
                |              index = Len(MyText.Text)+1
                |              MyView.InsertViewScale index, MyText

        :param int i_first:
        :param DrawingText io_text:
        :rtype: None
        """
        return self.drawing_view.InsertViewAngle(i_first, io_text.com_object)

    def insert_view_scale(self, i_first: int, io_text: 'DrawingText') -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub InsertViewScale(long iFirst,
                | DrawingText ioText)
                | 
                |     Insert the scale parameter in the text of the drawing
                |     text.
                |     Warning: This method is not available with 2D Layout for 3D
                |     Design.
                | 
                |     Parameters:
                | 
                |         iFirst
                |             The first character from which the parameter is inserted
                |             
                |         ioText
                |             The text on wich the scale parameter will be inserted
                |             
                |         Example:
                |             This example insert the Scale parameter of MyView drawing view at
                |             the first character of MyText drawing text.
                | 
                | 
                |              MyView.InsertViewScale 1, MyText

        :param int i_first:
        :param DrawingText io_text:
        :rtype: None
        """
        return self.drawing_view.InsertViewScale(i_first, io_text.com_object)

    def is_generative(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func IsGenerative() As boolean
                | 
                |     Returns whether the drawing view has a generative
                |     behavior.
                |     Warning: This method is not available with 2D Layout for 3D
                |     Design.
                |     True if the drawing view has a generative behavior.
                | 
                |     Example:
                |         This example retrieves in GenView if the MyView drawing view has a
                |         generative behavior property set.
                | 
                |          GenView = MyView.IsGenerative()

        :rtype: bool
        """
        return self.drawing_view.IsGenerative()

    def isolate(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub Isolate()
                | 
                |     Isolates the drawing view.
                |     Warning: This method is not available with 2D Layout for 3D
                |     Design.
                | 
                |     Example:
                |         This example isolates the MyView drawing view.
                | 
                |          MyView.Isolate

        :rtype: None
        """
        return self.drawing_view.Isolate()

    def save_edition(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub SaveEdition()
                | 
                |     Saves the Sketch Edition. Once you have finished working with the drawing
                |     view, you must save its edition in order to register modification for
                |     UNDO/REDO. Indeed when activating a view, this view is open in edition while
                |     the previous active view is closed in edition. So calling SaveEdition() before
                |     exiting a macro without changing active view will allow a correct UNDO/REDO
                |     behavior.
                |     Warning: This method is not available with 2D Layout for 3D
                |     Design.
                | 
                |     Example:
                |         The following example saves the edition of the drawing view
                |         MyView:
                | 
                |          MyView.SaveEdition

        :rtype: None
        """
        return self.drawing_view.SaveEdition()

    def set_view_name(self, i_view_name_prefix: str, i_view_name_ident: str, i_view_name_suffix: str) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub SetViewName(CATBSTR iViewNamePrefix,
                | CATBSTR iViewNameIdent,
                | CATBSTR iViewNameSuffix)
                | 
                |     Sets the prefix, the ident and the suffix of the name of the drawing view.
                |     The method returns an error in case of 2D component
                |     reference.
                |     Note: Prefix of drawing view can be also modified across name property
                |     defined in CATIABase
                |     Warning: This method is not available with 2D Layout for 3D
                |     Design.
                | 
                |     Example:
                | 
                |           This example sets the prefix, the ident, and the suffix of the name
                |           
                |          of the MyView drawing view respectively to "MyPrefix",
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
        return self.drawing_view.SetViewName(i_view_name_prefix, i_view_name_ident, i_view_name_suffix)

    def size(self) -> Tuple[float, float, float, float]:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub Size(CATSafeArrayVariant oValues)
                |
                |     Returns the bounding box of the drawing view.
                |     Warning: This method is not available with 2D Layout for 3D
                |     Design.
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
                |              This example gets the bounding box of the ViewToWorkOn drawing
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
        vba_function_name = "size"
        vba_code = """
        Public Function size(drawing_view)
            Dim oXY(4)
            drawing_view.Size oXY
            size = oXY
        End Function
        """

        system_service = self.application.system_service
        value = system_service.evaluate(
            vba_code, 0, vba_function_name, [self.com_object]
        )

        # we don't return value directly as CATIA returns for example
        # "(-15.0, 30.0, -15.0, 30.0, None)" I don't know what the additional
        # value None at the end represents.
        return value[0], value[1], value[2], value[3]

    def un_aligned_with_reference_view(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub UnAlignedWithReferenceView()
                | 
                |     Deactivates the alignment with the reference view. Deactivating the
                |     alignment to the reference view removes the constraints that the reference view
                |     imposes to the current drawing view. You can then, for example, move and
                |     position it freely.
                |     Warning: This method is not available with 2D Layout for 3D
                |     Design.
                | 
                |     Example:
                |         This example deactivates the alignment from the MyView drawing view to
                |         its reference view.
                | 
                |          MyView.UnAlignedWithReferenceView()

        :rtype: None
        """
        return self.drawing_view.UnAlignedWithReferenceView()

    def __repr__(self):
        return f'DrawingView(name="{self.name}")'
