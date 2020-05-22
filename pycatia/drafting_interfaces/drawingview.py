#! /usr/bin/python3.6
# module initially auto generated using V5Automation.chm from CATIA R25 on 2020-05-18 09:45:39.224078

from pycatia.system_interfaces.base_object import AnyObject


class DrawingView(AnyObject):
    """
        .. note::
            CAA V5 Visual Basic help

                | Represents a drawing view in a drawing sheet.

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.drawing_view = com_object

    @property
    def angle(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Angle
                | o Property Angle(    ) As
                | 
                | Returns or sets the angle of the drawing view. The angle is
                | measured between the axis system of the drawing view and the
                | axis system of the drawing sheet where the drawing view
                | lies. The angle is measured in radians and is counted
                | counterclockwise. Warning: This method is not available with
                | 2D Layout for 3D Design.
                |
                | Example:
                | This example sets the
                | angle of the MyView drawing view to 90 degrees clockwise.
                | You first need to compute the angle in radians and set the
                | minus sign to indicate the rotation is clockwise. PI =
                | 3.1415926535 Angle90Clockwise = -PI/2 MyView.Angle =
                | Angle90Clockwise

        :return: float
        """
        return self.drawing_view.Angle

    @angle.setter
    def angle(self, value):
        self.drawing_view.Angle = value

    @property
    def arrows(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Arrows
                | o Property Arrows(    ) As   (Read Only)
                | 
                | Returns the drawing arrow collection of the drawing view.
                | Warning: This method is not available with 2D Layout for 3D
                | Design. Example: This example retrieves in ArrowCollection
                | the collection of arrows of the MyView drawing view. Dim
                | ArrowCollection As DrawingArrows Set ArrowCollection =
                | MyView.Arrows

        :return: DrawingArrows()
        """
        return self.drawing_view.Arrows

    @property
    def components(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Components
                | o Property Components(    ) As   (Read Only)
                | 
                | Returns the drawing component instances collection (i.e.
                | ditto collection) of the drawing view.
                | Warning: This method is not available with 2D Layout for 3D Design.
                |
                | Example:
                | This example retrieves in ComponentCollection the collection of
                | component instances of the MyView drawing view.
                | Dim ComponentCollection As DrawingComponents
                | Set ComponentCollection = MyView.Components

        :return:
        """
        return self.drawing_view.Components

    @property
    def dimensions(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Dimensions
                | o Property Dimensions(    ) As   (Read Only)
                | 
                | Returns the drawing dimension collection of the drawing
                | view. Warning: This method is not available with 2D Layout
                | for 3D Design.
                |
                | Example: This example retrieves in
                | DimensionCollection the collection of dimensions of the
                | MyView drawing view.
                | Dim DimensionCollection As DrawingDimensions
                | Set DimensionCollection = MyView.Dimensions


        :return:
        """
        return self.drawing_view.Dimensions

    @property
    def factory2_d(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Factory2D
                | o Property Factory2D(    ) As   (Read Only)
                | 
                | Returns the 2D factory of the drawing view. Take care that
                | you must open edition on a sketch before adding or modifying
                | elements in it. Take care that you must close edition on a
                | sketch to keep all modifications before saving document.
                | Warning: This method is not available with 2D Layout for 3D
                | Design. To get Sketch from factory2D: Set mySketch =
                | my2DFactory.GetParent
                |
                | Example: The following example returns
                | in my2DFactory the 2D factory of the view myView:
                | Set my2DFactory = myView.Factory2D

        :return:
        """
        return self.drawing_view.Factory2D

    @property
    def frame_visualization(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | FrameVisualization
                | o Property FrameVisualization(    ) As
                | 
                | Returns or sets the drawing view frame visualization state.
                | True if the drawing view frame is visible. Warning: This
                | method is not available with 2D Layout for 3D Design.
                |
                | Example:
                | This example shows the frame of the MyView drawing
                | view.
                | MyView.FrameVisualization = True

        :return:
        """
        return self.drawing_view.FrameVisualization

    @frame_visualization.setter
    def frame_visualization(self, value):
        self.drawing_view.FrameVisualization = value

    @property
    def generative_behavior(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | GenerativeBehavior
                | o Property GenerativeBehavior(    ) As   (Read Only)
                | 
                | Returns the generative behavior of the drawing view.
                | Warning: This method is not available with 2D Layout for 3D
                | Design.
                |
                | Example:
                | This example retrieves in MyViewGenBehavior
                | the generative behavior of the MyView drawing view.
                |
                | Dim MyViewGenBehavior As DrawingViewGenerativeBehavior
                | Set MyViewGenBehavior = MyView.GenerativeBehavior

        :return:
        """
        return self.drawing_view.GenerativeBehavior

    @property
    def generative_links(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | GenerativeLinks
                | o Property GenerativeLinks(    ) As   (Read Only)
                | 
                | Returns the generative links of the drawing view. Warning:
                | This method is not available with 2D Layout for 3D Design.
                |
                | Example:
                | This example retrieves in MyViewGenLinks the
                | generative links of the MyView drawing view.
                | Dim MyViewGenLinks As DrawingViewGenerativeLinks
                | Set MyViewGenLinks = MyView.GenerativeLinks

        :return:
        """
        return self.drawing_view.GenerativeLinks

    @property
    def geometric_elements(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | GeometricElements
                | o Property GeometricElements(    ) As   (Read Only)
                | 
                | Returns the collection of geometric elements included in the
                | drawing view sketch. Warning: This method is not available
                | with 2D Layout for 3D Design.
                |
                | Example:
                | The following example
                | returns in colGeometry the list of geometric elements in the
                | view myView:
                | Dim colGeometry As GeometricElements Set
                | colGeometry = myView.GeometricElements

        :return:
        """
        return self.drawing_view.GeometricElements

    @property
    def lock_status(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | LockStatus
                | o Property LockStatus(    ) As
                | 
                | Returns or sets the lock status of a drawing view. Warning:
                | This method is not available with 2D Layout for 3D Design.
                | precondition: This property does not exist for the detail
                | view. In this case, the method returns failed. Example: This
                | example locks the ViewToWorkOn drawing view.
                | ViewToWorkOn.LockStatus = True

        :return: bool
        """
        return self.drawing_view.LockStatus

    @lock_status.setter
    def lock_status(self, value):
        """
        :param bool value:
        """
        self.drawing_view.LockStatus = value

    @property
    def pictures(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Pictures
                | o Property Pictures(    ) As   (Read Only)
                | 
                | Returns the drawing picture collection of the drawing view.
                | Warning: This method is not available with 2D Layout for 3D
                | Design. Example: This example retrieves in PictureCollection
                | the collection of pictures of the MyView drawing view.
                | Dim PictureCollection As DrawingPictures
                | Set PictureCollection = MyView.Pictures

        :return:
        """
        return self.drawing_view.Pictures

    @property
    def reference_view(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | ReferenceView
                | o Property ReferenceView(    ) As
                | 
                | Returns or sets the reference view. The reference view is
                | also the parent view to which the current drawing view is
                | linked and which is used as reference for alignment.
                | Generally, the reference view is the front view, and the
                | other views, such as the top, bottom, left, and right views,
                | are linked to it. This reference drawing view is used: When
                | moving the current drawing view. Its location remains
                | constrained to the reference view, depending on its type.
                | For example, a left view can move horizontally and a top
                | view can move vertically. To update the scale of the current
                | drawing view according to the modification performed to the
                | one of the reference drawing view.
                | Warning: This method is
                | not available with 2D Layout for 3D Design.
                |
                | Example:
                | This example retrieves in ReferenceView the view used as
                | reference by the MyView drawing view.
                | Dim ReferenceView As

        :return:
        """
        return self.drawing_view.ReferenceView

    @reference_view.setter
    def reference_view(self, value):
        """
        :param bool value:
        """
        self.reference_view.ReferenceView = value

    @property
    def scale(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Scale
                | o Property Scale(    ) As
                | 
                | Returns or sets the scale of the drawing view. Warning: This
                | method is not available with 2D Layout for 3D Design.
                |
                | Example:
                | This example sets the scale of the MyView drawing view to 0.5.
                | MyView.Scale = 0.5

        :return: float
        """
        return self.drawing_view.Scale

    @scale.setter
    def scale(self, value):
        """
        :param float value:
        """
        self.reference_view.Scale = value

    @property
    def scale2(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Scale2
                | o Property Scale2(    ) As
                | 
                | Returns or sets the scale of the drawing view (Workaround
                | for VBA keyword). Warning: This method is not available with
                | 2D Layout for 3D Design.
                |
                | Example:
                | This example sets the scale of the MyView drawing view to 0.5.
                | MyView.Scale2 = 0.5

        :return: float
        """
        return self.drawing_view.Scale2

    @scale2.setter
    def scale2(self, value):
        """
        :param float value:
        """
        self.reference_view.Scale2 = value

    @property
    def tables(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Tables
                | o Property Tables(    ) As   (Read Only)
                | 
                | Returns the drawing table collection of the drawing view.
                | Warning: This method is not available with 2D Layout for 3D
                | Design. Example: This example retrieves in TextCollection
                | the collection of texts of the MyView drawing view.
                | Dim TableCollection As DrawingTables
                | Set TableCollection = MyView.Tables

        :return:
        """
        return self.drawing_view.Tables

    @property
    def texts(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Texts
                | o Property Texts(    ) As   (Read Only)
                | 
                | Returns the drawing text collection of the drawing view.
                | Warning: This method is not available with 2D Layout for 3D
                | Design.
                |
                | Example:
                | This example retrieves in TextCollection
                | the collection of texts of the MyView drawing view.
                | Dim TextCollection As DrawingTexts
                | Set TextCollection = MyView.Texts

        :return:
        """
        return self.drawing_view.Texts

    @property
    def threads(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Threads
                | o Property Threads(    ) As   (Read Only)
                | 
                | Returns the drawing thread collection of the drawing view.
                | Warning: This method is not available with 2D Layout for 3D
                | Design.
                |
                | Example:
                | This example retrieves in ThreadCollection
                | the collection of threads of the MyView drawing view.
                | Dim ThreadCollection As DrawingThreads
                | Set ThreadCollection = MyView.Threads

        :return:
        """
        return self.drawing_view.Threads

    @property
    def view_type(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | ViewType
                | o Property ViewType(    ) As   (Read Only)
                | 
                | Returns the drawing view type. Warning: This method is not
                | available with 2D Layout for 3D Design.

        :return:
        """
        return self.drawing_view.ViewType

    @property
    def weldings(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Weldings
                | o Property Weldings(    ) As   (Read Only)
                | 
                | Returns the drawing welding collection of the drawing view.
                | Warning: This method is not available with 2D Layout for 3D
                | Design. Example: This example retrieves in weldingCollection
                | the collection of weldings of the MyView drawing view.
                | Dim weldingCollection As DrawingWeldings
                | Set weldingCollection = MyView.Weldings

        :return:
        """
        return self.drawing_view.Weldings

    @property
    def x(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | x
                | o Property x(    ) As
                | 
                | For an interactive view, get_x and put_x methods are
                | equivalents to get_xAxisData, put_xAxisData In a generative
                | case, get_x. put_x returns or sets the x coordinate of the
                | projection of the 3D centre of gravity. It is expressed with
                | respect to the sheet coordinate system. This coordinate,
                | like any length, is measured in millimeters. Warning: This
                | method is not available with 2D Layout for 3D Design.
                |
                | Example:
                | This example retrieves the x coordinate of the view
                | relative position MyView.
                | X = MyView.x

        :return:
        """
        return self.drawing_view.x

    @property
    def x_axis_data(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | xAxisData
                | o Property xAxisData(    ) As
                | 
                | Returns or sets the x coordinate of the drawing view
                | coordinate system origin. It is expressed with respect to
                | the sheet coordinate system. This coordinate, like any
                | length, is measured in millimeters. Warning: This method is
                | not available with 2D Layout for 3D Design.
                |
                | Example:
                | This example retrieves the x coordinate of the coordinate system
                | origin of the MyView drawing view.
                | X = MyView.xAxisData

        :return:
        """
        return self.drawing_view.xAxisData

    @x_axis_data.setter
    def x_axis_data(self, value):
        """
        :param float value:
        """
        self.reference_view.xAxisData = value

    @property
    def y(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | y
                | o Property y(    ) As
                | 
                | For an interactive view, get_y and put_y methods are
                | equivalents to get_yAxisData, put_yAxisData In a generative
                | case, get_y. put_y returns or sets the y coordinate of the
                | projection of the 3D centre of gravity. It is expressed with
                | respect to the sheet coordinate system. This coordinate,
                | like any length, is measured in millimeters. Warning: This
                | method is not available with 2D Layout for 3D Design.
                |
                | Example:
                | This example sets the y coordinate of the view
                | relative position MyView to 5 inches. You need first to
                | convert the 5 inches into millimeters.
                | NewYCoordinate = 5*25.4
                | MyView.y = NewYCoordinate

        :return:
        """
        return self.drawing_view.y

    @property
    def y_axis_data(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | yAxisData
                | o Property yAxisData(    ) As
                | 
                | Returns or sets the y coordinate of the drawing view
                | coordinate system origin. It is expressed with respect to
                | the sheet coordinate system. This coordinate, like any
                | length, is measured in millimeters. Warning: This method is
                | not available with 2D Layout for 3D Design.
                |
                | Example:
                | This example sets the y coordinate of the coordinate system
                | origin of the MyView drawing view to 5 inches. You need
                | first to convert the 5 inches into millimeters.
                | NewYCoordinate = 5*25.4
                | MyView.yAxisData = NewYCoordinate

        :return:
        """
        return self.drawing_view.yAxisData

    @y_axis_data.setter
    def y_axis_data(self, value):
        """
        :param float value:
        """
        self.reference_view.yAxisData = value

    def activate(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Activate
                | o Sub Activate(    )
                | 
                | Activates the drawing view. Activating a drawing view means
                | that this drawing view is the one on which the end-user is
                | now working. Warning: This method is not available with 2D
                | Layout for 3D Design.
                |
                | Example:
                | This example activates the ViewToWorkOn drawing view.
                | ViewToWorkOn.Activate()

        :return:
        """
        return self.drawing_view.Activate()

    def aligned_with_reference_view(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | AlignedWithReferenceView
                | o Sub AlignedWithReferenceView(    )
                | 
                | Activates the alignment with the reference view. Activating
                | the alignment with the reference view restores the
                | constraints that the reference view imposes to the current
                | drawing view. Warning: This method is not available with 2D
                | Layout for 3D Design.
                |
                | Example:
                | This example activates the
                | alignment from the MyView drawing view to its reference
                | view.
                | MyView.AlignedWithReferenceView()

        :return:
        """
        return self.drawing_view.AlignedWithReferenceView()

    def get_view_name(self, i_view_name_prefix, i_view_name_ident, i_view_name_suffix):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetViewName
                | o Sub GetViewName(        iViewNamePrefix,
                |                           iViewNameIdent,
                |                           iViewNameSuffix)
                | 
                | Returns the prefix, the ident and the suffix of the name of
                | the drawing view. The method returns an error in case of 2D
                | component reference. Note: Prefix of drawing view can be
                | also retrieved across name property defined in CATIABase
                | Warning: This method is not available with 2D Layout for 3D
                | Design.
                |
                | Example:
                | This example gets the prefix, the ident,
                | and the suffix of the name of the MyView drawing view
                | Dim MyPrefix, MyIdent, MySuffix As CATBSTR
                | MyView.GetViewName(MyPrefix, MyIdent, MySuffix)

        :param i_view_name_prefix:
        :param i_view_name_ident:
        :param i_view_name_suffix:
        :return:
        """
        return self.drawing_view.GetViewName(i_view_name_prefix, i_view_name_ident, i_view_name_suffix)

    def insert_view_angle(self, i_first, io_text):
        """
        .. note::
            CAA V5 Visual Basic help

                | InsertViewAngle
                | o Sub InsertViewAngle(        iFirst,
                |                               ioText)
                | 
                | Insert the Angle parameter in the text of the drawing text.
                | Warning: This method is not available with 2D Layout for 3D
                | Design.
                |
                | Parameters:
                | iFirst
                |    The first character from which the parameter is inserted 
                |  ioText
                |    The text on which the scale parameter will be inserted
                |
                | Examples:
                | This example insert the Angle parameter of MyView drawing
                | view at the end of MyText drawing text.
                | index = Len(MyText.Text)+1
                | MyView.InsertViewScale index, MyText

        :param i_first:
        :param io_text:
        :return:
        """
        return self.drawing_view.InsertViewAngle(i_first, io_text)

    def insert_view_scale(self, i_first, io_text):
        """
        .. note::
            CAA V5 Visual Basic help

                | InsertViewScale
                | o Sub InsertViewScale(        iFirst,
                |                               ioText)
                | 
                | Insert the scale parameter in the text of the drawing text.
                | Warning: This method is not available with 2D Layout for 3D
                | Design.
                |
                | Parameters:
                | iFirst
                |   The first character from which the parameter is inserted
                | ioText
                |   The text on wich the scale parameter will be inserted
                |
                | Examples:
                | This example insert the Scale parameter of MyView drawing
                | view at the first character of MyText drawing text.
                | MyView.InsertViewScale 1, MyText

        :param i_first:
        :param io_text:
        :return:
        """
        return self.drawing_view.InsertViewScale(i_first, io_text)

    def is_generative(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | IsGenerative
                | o Func IsGenerative(    ) As
                | 
                | Returns whether the drawing view has a generative behavior.
                | Warning: This method is not available with 2D Layout for 3D
                | Design. True if the drawing view has a generative behavior.
                |
                | Example:
                | This example retrieves in GenView if the MyView
                | drawing view has a generative behavior property set.
                | GenView = MyView.IsGenerative()

        :return:
        """
        return self.drawing_view.IsGenerative()

    def isolate(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Isolate
                | o Sub Isolate(    )
                | 
                | Isolates the drawing view. Warning: This method is not
                | available with 2D Layout for 3D Design.
                |
                | Example: This example isolates the MyView drawing view.
                | MyView.Isolate

        :return:
        """
        return self.drawing_view.Isolate()

    def save_edition(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | SaveEdition
                | o Sub SaveEdition(    )
                | 
                | Saves the Sketch Edition. Once you have finished working
                | with the drawing view, you must save its edition in order to
                | register modification for UNDO/REDO. Indeed when activating
                | a view, this view is open in edition while the previous
                | active view is closed in edition. So calling SaveEdition()
                | before exiting a macro without changing active view will
                | allow a correct UNDO/REDO behavior.
                |
                | Warning: This method is not available with 2D Layout for 3D Design.
                |
                | Example:
                | The following example saves the edition of the drawing view
                | MyView: MyView.SaveEdition

        :return:
        """
        return self.drawing_view.SaveEdition()

    def set_view_name(self, i_view_name_prefix, i_view_name_ident, i_view_name_suffix):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetViewName
                | o Sub SetViewName(        iViewNamePrefix,
                |                           iViewNameIdent,
                |                           iViewNameSuffix)
                | 
                | Sets the prefix, the ident and the suffix of the name of the
                | drawing view. The method returns an error in case of 2D
                | component reference. Note: Prefix of drawing view can be
                | also modified across name property defined in CATIABase
                | Warning: This method is not available with 2D Layout for 3D
                | Design.
                |
                | Example:
                | This example sets the prefix, the ident,
                | and the suffix of the name of the MyView drawing view
                | respectively to "MyPrefix", "MyIdent", and "MySuffix".
                | MyView.SetViewName ("MyPrefix", "MyIdent", "MySuffix")

        :param i_view_name_prefix:
        :param i_view_name_ident:
        :param i_view_name_suffix:
        :return:
        """
        return self.drawing_view.SetViewName(i_view_name_prefix, i_view_name_ident, i_view_name_suffix)

    def size(self, o_values):
        """
        .. note::
            CAA V5 Visual Basic help

                | Size
                | o Sub Size(        oValues)
                | 
                | Returns the bounding box of the drawing view. Warning: This
                | method is not available with 2D Layout for 3D Design.
                |
                | Parameters:
                | oValues
                |    The values of the view bounding box: Xmin, Xmax, Ymin, Ymax
                |
                | Examples:
                | This example gets the bounding box of the ViewToWorkOn
                | drawing view.
                | Dim oXY(4) As Double
                | ViewToWorkOn.Size oXY
                | Xmin = oXY(0)
                | Xmax = oXY(1)
                | Ymin = oXY(2)
                | Ymax = oXY(3)

        :param o_values:
        :return:
        """
        return self.drawing_view.Size(o_values)

    def un_aligned_with_reference_view(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | UnAlignedWithReferenceView
                | o Sub UnAlignedWithReferenceView(    )
                | 
                | Deactivates the alignment with the reference view.
                | Deactivating the alignment to the reference view removes the
                | constraints that the reference view imposes to the current
                | drawing view. You can then, for example, move and position
                | it freely. Warning: This method is not available with 2D
                | Layout for 3D Design.
                |
                | Example: This example deactivates the
                | alignment from the MyView drawing view to its reference
                | view.
                | MyView.UnAlignedWithReferenceView()

        :return:
        """
        return self.drawing_view.UnAlignedWithReferenceView()

    def __repr__(self):
        return f'DrawingView()'
