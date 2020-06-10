#! usr/bin/python3.6
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-09 09:53:18.676780

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.any_object import AnyObject
from pycatia.system_interfaces.cat_base_dispatch import CatBaseDispatch


class DrawingViewGenerativeBehavior(CatBaseDispatch):
    """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 DrawingViewGenerativeBehavior
                | 
                | Represents the generative behavior of a drawing view.
                | 
                | The generative behavior of a drawing view is an object that defines the
                | parameters used to generate the drawing view from the document it represents.
                | Main parameters include the type of the view, the plane on which the view is
                | projected, the document to represent, and additional parameters depending on
                | the view type.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.drawing_view_generative_behavior = com_object

    @property
    def color_inheritance_mode(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property ColorInheritanceMode() As
                | Cat3DColorInheritanceMode
                | 
                |     Returns or sets the view color inheritance mode.
                | 
                |     Example:
                | 
                |           This example sets the view color inheritance mode of the
                |           MyView
                |          drawing view to cat3DColorInheritanceModeOn to indicate
                |          that
                |          generated items inherit the color of the 3D elements they come
                |          from.
                |          
                | 
                |         
MyView.GenerativeBehavior.ColorInheritanceMode(cat3DColorInheritanceModeOn)

        :return: enum cat3_d_color_inheritance_mode
        """

        return self.drawing_view_generative_behavior.ColorInheritanceMode

    @color_inheritance_mode.setter
    def color_inheritance_mode(self, value):
        """
        :param enum cat3_d_color_inheritance_mode value:
        """

        self.drawing_view_generative_behavior.ColorInheritanceMode = value

    @property
    def document(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property Document() As AnyObject
                | 
                |     Returns or sets the document used to generate the drawing view. This
                |     document can be a CATIA Version 4 model, a CATIA Version 5 part or assembly.
                |     But it can be also just a body(partbody), according to the view links (then the
                |     document is the parent object). The document must be already loaded, that is it
                |     can be retrieved from the document collection managed by the CATIA
                |     application.
                | 
                |     Example:
                | 
                |           This example sets the document that the MyView drawing view
                |           should
                |          represent to the CATPart1 CATIA Version 5 part.
                |          
                | 
                |          Dim PartToDraw As Document
                |          Set PartToDraw = CATIA.Documents.Item("CATPart1")
                |          MyView.GenerativeBehavior.Document = PartToDraw

        :return: AnyObject
        """

        return AnyObject(self.drawing_view_generative_behavior.Document)

    @document.setter
    def document(self, value):
        """
        :param AnyObject value:
        """

        self.drawing_view_generative_behavior.Document = value

    @property
    def fillet_representation(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property FilletRepresentation() As CatFilletRepresentation
                | 
                |     Returns or sets the view Fillet representation mode. The Fillet
                |     representation indicates how to draw lines coming from
                |     fillets.
                | 
                |     Example:
                | 
                |           This example sets the view Fillet representation of the
                |           MyView
                |          drawing view to catFilletRepBoundary
                |          
                | 
                |          MyView.GenerativeBehavior.FilletRepresentation = catFilletRepBoundary

        :return: enum cat_fillet_representation
        """

        return self.drawing_view_generative_behavior.FilletRepresentation

    @fillet_representation.setter
    def fillet_representation(self, value):
        """
        :param enum cat_fillet_representation value:
        """

        self.drawing_view_generative_behavior.FilletRepresentation = value

    @property
    def hidden_line_mode(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property HiddenLineMode() As CatHiddenLineMode
                | 
                |     Returns or sets the view hidden line drawing mode. The hidden line drawing
                |     mode indicates whether to draw the hidden lines.
                | 
                |     Example:
                | 
                |           This example sets the view hidden line drawing mode of the
                |           MyView
                |          drawing view to catHLRModeOn to indicate that hidden lines must
                |          not
                |          be drawn.
                |          
                | 
                |          MyView.GenerativeBehavior.HiddenLineMode = catHLRModeOn

        :return: enum cat_hidden_line_mode
        """

        return self.drawing_view_generative_behavior.HiddenLineMode

    @hidden_line_mode.setter
    def hidden_line_mode(self, value):
        """
        :param enum cat_hidden_line_mode value:
        """

        self.drawing_view_generative_behavior.HiddenLineMode = value

    @property
    def image_view_mode(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property ImageViewMode() As CatImageViewMode
                | 
                |     Returns or sets the view generation mode as pixel image.
                | 
                |     Returns:
                |     S_OK
                |         if the operation succeeded. 
                |     E_FAIL
                |         For both methods, if an unspecified failure has occurred
                |         
                | 
                | Example:
                | 
                |       This example sets the view image generation mode of the
                |       MyView
                |      drawing view to catImageModeHRD to indicate that view is generated as
                |      an
                |      HRD image.
                |      
                | 
                |     
MyView.GenerativeBehavior.CatImageViewMode(catImageModeHRD)

        :return: enum cat_image_view_mode
        """

        return self.drawing_view_generative_behavior.ImageViewMode

    @image_view_mode.setter
    def image_view_mode(self, value):
        """
        :param enum cat_image_view_mode value:
        """

        self.drawing_view_generative_behavior.ImageViewMode = value

    @property
    def limit_bounding_box(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property LimitBoundingBox() As double
                | 
                |     Returns or sets the bounding box limits under which a part. will not be
                |     taken into account during view generation. The value 0. means that no part will
                |     be filtered.
                | 
                |     Returns:
                |     S_OK
                |         if the operation succeeded. 
                |     E_FAIL
                |         For both methods, if an unspecified failure has occurred

        :return: float
        """

        return self.drawing_view_generative_behavior.LimitBoundingBox

    @limit_bounding_box.setter
    def limit_bounding_box(self, value):
        """
        :param float value:
        """

        self.drawing_view_generative_behavior.LimitBoundingBox = value

    @property
    def parent_view(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property ParentView() As DrawingView (Read Only)
                | 
                |     Returns the parent view.
                | 
                |     Example:
                | 
                |           This example returns in MyParentView the parent view of
                |           the
                |          MyView drawing view.
                |          
                | 
                |          Dim MyParentView As DrawingView
                |          Set MyParentView = MyView.GenerativeBehavior.ParentView

        :return: DrawingView
        """
        from pycatia.drafting_interfaces.drawing_view import DrawingView
        return DrawingView(self.drawing_view_generative_behavior.ParentView)

    @property
    def points_projection_mode(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property PointsProjectionMode() As CatPointsProjectionMode
                | 
                |     Returns or sets projection mode for 3D points. This mode indicates whether
                |     to project 3D points.
                | 
                |     Example:
                | 
                |           This example sets the points projection mode of the
                |           MyView
                |          drawing view to catPointsProjectionModeOn to indicate that
                |          
                |          3D points must be projected.
                |          
                | 
                |          MyView.GenerativeBehavior.PointsProjectionMode = catPointsProjectionModeOn

        :return: enum cat_points_projection_mode
        """

        return self.drawing_view_generative_behavior.PointsProjectionMode

    @points_projection_mode.setter
    def points_projection_mode(self, value):
        """
        :param enum cat_points_projection_mode value:
        """

        self.drawing_view_generative_behavior.PointsProjectionMode = value

    @property
    def points_symbol(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property PointsSymbol() As short
                | 
                |     Returns or sets symbol for projected points. The 0 value means that
                |     projected points inherit the symbol of 3D points they come from.

        :return: enum
        """

        return self.drawing_view_generative_behavior.PointsSymbol

    @points_symbol.setter
    def points_symbol(self, value):
        """
        :param enum value:
        """

        self.drawing_view_generative_behavior.PointsSymbol = value

    @property
    def representation_mode(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property RepresentationMode() As CatRepresentationMode
                | 
                |     Returns or sets generated geometry representation mode.
                | 
                |     Returns:
                |     S_OK
                |         if the operation succeeded. 
                |     E_FAIL
                |         For both methods, if an unspecified failure has occurred and for the
                |         put_RepresentationMode method if the drawing view owns a detail, section or
                |         breakout specification. 
                | 
                | Example:
                | 
                |       This example sets the representation mode of the MyView
                |      drawing view to catPolyhedricMode to indicate that 
                |      it is generated from CGR data.
                |      
                | 
                |      MyView.GenerativeBehavior.RepresentationMode = catPolyhedricMode

        :return: enum cat_representation_mode
        """

        return self.drawing_view_generative_behavior.RepresentationMode

    @representation_mode.setter
    def representation_mode(self, value):
        """
        :param enum cat_representation_mode value:
        """

        self.drawing_view_generative_behavior.RepresentationMode = value

    def apply_breakout_to(self, i_parent_view=None):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Sub ApplyBreakoutTo(DrawingViewGenerativeBehavior
                | iParentView)
                | 
                |     If a view have gone through a breakout view operation, this method realize
                |     a breakout view on the view given as parameter, and the other types of the view
                |     remain.
                | 
                |     Example:
                | 
                |           This example apply the last breakout view done on MyView, if
                |           so,
                |          on the view MyDestinationView.
                |          
                | 
                |         
MyView.GenerativeBehavior.ApplyBreakoutTo(MyDestinationView)

        :param DrawingViewGenerativeBehavior i_parent_view:
        :return: None
        """
        return self.drawing_view_generative_behavior.ApplyBreakoutTo(i_parent_view)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'apply_breakout_to'
        # # vba_code = """
        # # Public Function apply_breakout_to(drawing_view_generative_behavior)
        # #     Dim iParentView (2)
        # #     drawing_view_generative_behavior.ApplyBreakoutTo iParentView
        # #     apply_breakout_to = iParentView
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def define_auxiliary_view(self, i_x_start_point=None, i_y_start_point=None, i_x_end_point=None, y_end_point=None,
                              i_side_to_draw=None, i_parent_view_generative_behavior=None):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Sub DefineAuxiliaryView(double iXStartPoint,
                | double iYStartPoint,
                | double iXEndPoint,
                | double YEndPoint,
                | short iSideToDraw,
                | DrawingViewGenerativeBehavior iParentViewGenerativeBehavior)
                | 
                |     Defines an auxiliary drawing view. The projection plane of this auxiliary
                |     drawing view is defined in its parent view using a line segment which
                |     represents the trace of the projection plane, considered as being normal to
                |     this parent view projection plane.
                | 
                |     Parameters:
                | 
                |         iXStartPoint,iYStartPoint
                |             The coordinates of the trace line segment start point, expressed
                |             with respect of the parent view axis system 
                |         iXEndPoint,iYEndPoint
                |             The coordinates of the trace line segment end point, expressed with
                |             respect of the parent view axis system 
                |         iSideToDraw
                |             This side is defined according to the trace line segment. This
                |             segment is oriented from its start point to its end point. When looking along
                |             this segment, from its start point towards its end point, setting iSideToDraw
                |             to 0 (clockwise) draws the auxiliary view as if it were seen from the left of
                |             the segment in the parent view. Setting iSideToDraw to 1 (counterclockwise)
                |             draws the auxiliary view as if it were seen from the right of the
                |             segment.
                |             0 Clockwise
                |             1 Counterclockwise 
                |         iParentViewGenerativeBehavior
                |             The generative behavior of the parent view in which the line
                |             segment representing the projection plane trace is defined
                |             
                | 
                |     Example:
                | 
                |           This example defines MyView as an auxiliary view of
                |          its parent view whose generative behavior is
                |          MyParentViewGB.
                |          The trace of the auxiliary view projection plane passes by the
                |          points
                |          of coordinates (100., 50.) and (500., 250.)
                |          respectively.
                |          The section is seen from the right of the trace line segment
                |          defining
                |          the auxiliary view projection plane.
                |          
                | 
                |          MyView.GenerativeBehavior.DefineAuxiliaryView 100., 50., 500., 250.,
                |          1, MyParentViewGB

        :param float i_x_start_point:
        :param float i_y_start_point:
        :param float i_x_end_point:
        :param float y_end_point:
        :param enum i_side_to_draw:
        :param DrawingViewGenerativeBehavior i_parent_view_generative_behavior:
        :return: None
        """
        return self.drawing_view_generative_behavior.DefineAuxiliaryView(i_x_start_point, i_y_start_point,
                                                                         i_x_end_point, y_end_point, i_side_to_draw,
                                                                         i_parent_view_generative_behavior)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'define_auxiliary_view'
        # # vba_code = """
        # # Public Function define_auxiliary_view(drawing_view_generative_behavior)
        # #     Dim iXStartPoint (2)
        # #     drawing_view_generative_behavior.DefineAuxiliaryView iXStartPoint
        # #     define_auxiliary_view = iXStartPoint
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def define_box3_d_view(self, i_boxable_object=None):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Sub DefineBox3DView(AnyObject iBoxableObject)
                | 
                |     Defines a drawing view intersected with a 3D box. The 3D box is defined by
                |     the interface CATIASection
                | 
                |     Parameters:
                | 
                |         iBoxableObject
                |             The 3D box object which must implement the CATIASection
                |             interface

        :param AnyObject i_boxable_object:
        :return: None
        """
        return self.drawing_view_generative_behavior.DefineBox3DView(i_boxable_object)

    def define_breakout(self, i_profil=None, i_plane1=None, i_plane2=None):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Sub DefineBreakout(CATSafeArrayVariant iProfil,
                | CATSafeArrayVariant iPlane1,
                | CATSafeArrayVariant iPlane2)
                | 
                |     Defines a breakout on the current view.
                | 
                |     Parameters:
                | 
                |         Profil
                |             the profile used, stored as a CATSafeArrayVariant of 2D
                |             coordinates, of dimension 2*n, n the number of control points on profile.
                |             
                |         Plane1
                |             the first reference plane, stored as a CATSafeArrayVariant [9] : Plane1 [0...2] : Plane origine coordinates Plane1 [3...5] : First direction vector coordinates Plane1 [6...8] : Second direction vector coordinates. This plane must intersect the 3D Volume. 
                |         Plane2
                |             the second reference plane, stored as a CATSafeArrayVariant [9] : This plane2 is not used. Returns
                |             Legal values : S_OK if breakout definition succeeded or E_FAIL if the breakout definition failed

        :param tuple i_profil:
        :param tuple i_plane1:
        :param tuple i_plane2:
        :return: None
        """
        return self.drawing_view_generative_behavior.DefineBreakout(i_profil, i_plane1, i_plane2)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'define_breakout'
        # # vba_code = """
        # # Public Function define_breakout(drawing_view_generative_behavior)
        # #     Dim iProfil (2)
        # #     drawing_view_generative_behavior.DefineBreakout iProfil
        # #     define_breakout = iProfil
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def define_broken_view(self, i_broken_lines_extremities=None, i_x_direction=None, i_y_direction=None):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Sub DefineBrokenView(CATSafeArrayVariant
                | iBrokenLinesExtremities,
                | double iXDirection,
                | double iYDirection)
                | 
                |     Defines a broken drawing view. The broken area is represented by two lines
                |     and a direction in the source view.
                | 
                |     Parameters:
                | 
                |         iBrokenLinesExtremities
                |             The lines defining the broken profile. This lines is passed as its
                |             point coordinate table. Only two lines have to be defined. It has the following
                |             contents:
                | 
                |             iBrokenLinesExtremities[0] = X1
                |                 x coordinate of the first point for the first line
                |                 
                |             iBrokenLinesExtremities[1] = Y1
                |                 y coordinate of the first point for the first line
                |                 
                |             iBrokenLinesExtremities[2] = X2
                |                 x coordinate of the second point for the first line
                |                 
                |             iBrokenLinesExtremities[3] = Y2
                |                 y coordinate of the second point for the first line
                |                 
                |             iBrokenLinesExtremities[4] = X3
                |                 x coordinate of the first point for the second line
                |                 
                |             iBrokenLinesExtremities[5] = Y3
                |                 y coordinate of the first point for the second line
                |                 
                |             iBrokenLinesExtremities[6] = X4
                |                 x coordinate of the second point for the second line
                |                 
                |             iBrokenLinesExtremities[7] = Y4
                |                 y coordinate of the second point for the second line
                |                 
                | 
                |         iXDirection,iYDirection
                |             The direction stands for the translation. The direction must be
                |             horizontal or vertical. 
                | 
                |     Example:
                | 
                |           This example defines MyView as a broken view.
                |          The direction for the translation is horizontal.
                |          The broken area is defined by to vertical lines.
                |          
                | 
                |          MyView.GenerativeBehavior.DefineBrokenView X1, Y1, X2, Y2, X3, Y3, X4,
                |          Y4, XDirection, YDirection

        :param tuple i_broken_lines_extremities:
        :param float i_x_direction:
        :param float i_y_direction:
        :return: None
        """
        return self.drawing_view_generative_behavior.DefineBrokenView(i_broken_lines_extremities, i_x_direction,
                                                                      i_y_direction)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'define_broken_view'
        # # vba_code = """
        # # Public Function define_broken_view(drawing_view_generative_behavior)
        # #     Dim iBrokenLinesExtremities (2)
        # #     drawing_view_generative_behavior.DefineBrokenView iBrokenLinesExtremities
        # #     define_broken_view = iBrokenLinesExtremities
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def define_circular_clipping_view(self, x_center=None, y_center=None, radius=None):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Sub DefineCircularClippingView(double XCenter,
                | double YCenter,
                | double Radius)
                | 
                |     Defines a Circular clipping on the current view.
                | 
                |     Parameters:
                | 
                |         XCenter,
                |             YCenter clipping circle center position. 
                |         Radius
                |             clipping circle radius. Returns
                |             Legal values : S_OK if clipping definition succeeded or E_FAIL if the clipping definition failed

        :param float x_center:
        :param float y_center:
        :param float radius:
        :return: None
        """
        return self.drawing_view_generative_behavior.DefineCircularClippingView(x_center, y_center, radius)

    def define_circular_detail_view(self, i_x_center=None, i_y_center=None, i_radius=None,
                                    i_parent_view_generative_behavior=None):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Sub DefineCircularDetailView(double iXCenter,
                | double iYCenter,
                | double iRadius,
                | DrawingViewGenerativeBehavior iParentViewGenerativeBehavior)
                | 
                |     Defines a detail or a clipped drawing view. The clipped area is represented
                |     by a circle in the parent view.
                | 
                |     Parameters:
                | 
                |         iXCenter,iYCenter
                |             The circle center coordinates, expressed in the parent view axis
                |             system 
                |         iRadius
                |             The circle radius 
                |         iParentViewGenerativeBehavior
                |             The generative behavior of the parent view in which the circular
                |             clipping is defined. For a clipped view, iParentViewGenerativeBehavior must be
                |             set to the current drawing view. 
                | 
                |     Example:
                | 
                |           This example defines MyView as a detail view of the
                |           view
                |          considered as its parent view whose generative behavior
                |          is
                |          MyParentViewGB.
                |          The clipped area is a circle defined using its center coordinates
                |          (100.,
                |          150.), and its radius (75.) with respsect to the parent view axis
                |          system.
                |          
                | 
                |          MyView.GenerativeBehavior.DefineCircularDetailView 100., 150., 75.,
                |          MyParentViewGB

        :param float i_x_center:
        :param float i_y_center:
        :param float i_radius:
        :param DrawingViewGenerativeBehavior i_parent_view_generative_behavior:
        :return: None
        """
        return self.drawing_view_generative_behavior.DefineCircularDetailView(i_x_center, i_y_center, i_radius,
                                                                              i_parent_view_generative_behavior)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'define_circular_detail_view'
        # # vba_code = """
        # # Public Function define_circular_detail_view(drawing_view_generative_behavior)
        # #     Dim iXCenter (2)
        # #     drawing_view_generative_behavior.DefineCircularDetailView iXCenter
        # #     define_circular_detail_view = iXCenter
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def define_circular_exact_clipping_view(self, x_center=None, y_center=None, radius=None):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Sub DefineCircularExactClippingView(double XCenter,
                | double YCenter,
                | double Radius)
                | 
                |     Defines a Circular exact clipping on the current view.
                | 
                |     Parameters:
                | 
                |         XCenter,
                |             YCenter clipping circle center position. 
                |         Radius
                |             clipping circle radius. Returns
                |             Legal values : S_OK if clipping definition succeeded or E_FAIL if the clipping definition failed

        :param float x_center:
        :param float y_center:
        :param float radius:
        :return: None
        """
        return self.drawing_view_generative_behavior.DefineCircularExactClippingView(x_center, y_center, radius)

    def define_front_view(self, i_x1=None, i_y1=None, i_z1=None, i_x2=None, i_y2=None, i_z2=None):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Sub DefineFrontView(double iX1,
                | double iY1,
                | double iZ1,
                | double iX2,
                | double iY2,
                | double iZ2)
                | 
                |     Defines a front drawing view. The front view is defined using its
                |     projection plane, passed as the components of two vectors V1 and V2. The cross
                |     product of vector V1(X1, Y1, Z1) by vector V2(X2, Y2, Z2) defines the
                |     projection direction.
                | 
                |     Parameters:
                | 
                |         iX1,iY1,iZ1
                |             The components of the first vector with respect to the document 3D
                |             axis system 
                |         iX2,iY2,iZ2
                |             The components of the second vector with respect to the document 3D
                |             axis system 
                | 
                |     Example:
                | 
                |           This example defines MyView as a front view by projecting
                |           the
                |          represented document in the YZ 3D plane.
                |          
                | 
                |          MyView.GenerativeBehavior.DefineFrontView 0., 1., 0., 0., 0.,
                |          1.

        :param float i_x1:
        :param float i_y1:
        :param float i_z1:
        :param float i_x2:
        :param float i_y2:
        :param float i_z2:
        :return: None
        """
        return self.drawing_view_generative_behavior.DefineFrontView(i_x1, i_y1, i_z1, i_x2, i_y2, i_z2)

    def define_isometric_view(self, i_x1=None, i_y1=None, i_z1=None, i_x2=None, i_y2=None, i_z2=None):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Sub DefineIsometricView(double iX1,
                | double iY1,
                | double iZ1,
                | double iX2,
                | double iY2,
                | double iZ2)
                | 
                |     Defines an isometric drawing view. The isometric view is defined using its
                |     projection plane, passed as the components of two vectors V1 and V2. The cross
                |     product of vector V1(X1, Y1, Z1) by vector V2(X2, Y2, Z2) defines the
                |     projection direction.
                | 
                |     Parameters:
                | 
                |         iX1,iY1,iZ1
                |             The components of the first vector with respect to the document 3D
                |             axis system 
                |         iX2,iY2,iZ2
                |             The components of the second vector with respect to the document 3D
                |             axis system 
                | 
                |     Example:
                | 
                |           This example defines MyView as an isometric view by projecting
                |           the
                |          represented document in the vertical plane making an angle of -45
                |          degrees
                |          with respect to the X axis.
                |          
                | 
                |          MyView.GenerativeBehavior.DefineIsometricView -0.707, 0.707, 0., 0.,
                |          0., 1.

        :param float i_x1:
        :param float i_y1:
        :param float i_z1:
        :param float i_x2:
        :param float i_y2:
        :param float i_z2:
        :return: None
        """
        return self.drawing_view_generative_behavior.DefineIsometricView(i_x1, i_y1, i_z1, i_x2, i_y2, i_z2)

    def define_polygonal_clipping_view(self, profil=None):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Sub DefinePolygonalClippingView(CATSafeArrayVariant
                | profil)
                | 
                |     Defines a polygonal clipping on the current view.
                | 
                |     Parameters:
                | 
                |         profil
                |             the profile used, stored as a CATSafeArrayVariant of 2D
                |             coordinates, of dimension 2*n, n the number of control points on profile.
                |             Returns
                |             Legal values : S_OK if clipping definition succeeded or E_FAIL if the clipping definition failed

        :param tuple profil:
        :return: None
        """
        return self.drawing_view_generative_behavior.DefinePolygonalClippingView(profil)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'define_polygonal_clipping_view'
        # # vba_code = """
        # # Public Function define_polygonal_clipping_view(drawing_view_generative_behavior)
        # #     Dim profil (2)
        # #     drawing_view_generative_behavior.DefinePolygonalClippingView profil
        # #     define_polygonal_clipping_view = profil
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def define_polygonal_detail_view(self, i_profile=None, i_parent_view_generative_behavior=None):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Sub DefinePolygonalDetailView(CATSafeArrayVariant
                | iProfile,
                | DrawingViewGenerativeBehavior iParentViewGenerativeBehavior)
                | 
                |     Defines a detail or a clipped drawing view. The clipped area is represented
                |     by a circle in the parent view.
                | 
                |     Parameters:
                | 
                |         iProfile
                |             The polyline defining the detail profile. This polyline is passed
                |             as its point coordinate table. The polyline is automatically closed. It has the
                |             following contents:
                | 
                |             iProfile[0] = X1
                |                 x coordinate of the first point 
                |             iProfile[1] = Y1
                |                 y coordinate of the first point 
                |             iProfile[2] = X2
                |                 x coordinate of the second point 
                |             iProfile[3] = Y2
                |                 y coordinate of the second point 
                |             ...
                |             iProfile[2n-2] = Xn
                |                 x coordinate of the nth and last point 
                |             iProfile[2n-1] = Yn
                |                 y coordinate of the nth and last point 
                | 
                |         iParentViewGenerativeBehavior
                |             The generative behavior of the parent view in which the poligonal
                |             clipping is defined. For a clipped view, iParentViewGenerativeBehavior must be
                |             set to the current drawing view. 
                | 
                |     Example:
                | 
                |           This example defines MyView as a detail view of the
                |           view
                |          considered as its parent view whose generative behavior
                |          is
                |          MyParentViewGB.
                |          The clipped area is a square defined using its four corners with
                |          respsect to the parent view axis system.
                |          
                | 
                |          MyView.GenerativeBehavior.DefinePolygonalDetailView 0., 0., 100., 0.,
                |          100., 100., 0., 100., MyParentViewGB

        :param tuple i_profile:
        :param DrawingViewGenerativeBehavior i_parent_view_generative_behavior:
        :return: None
        """
        return self.drawing_view_generative_behavior.DefinePolygonalDetailView(i_profile,
                                                                               i_parent_view_generative_behavior)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'define_polygonal_detail_view'
        # # vba_code = """
        # # Public Function define_polygonal_detail_view(drawing_view_generative_behavior)
        # #     Dim iProfile (2)
        # #     drawing_view_generative_behavior.DefinePolygonalDetailView iProfile
        # #     define_polygonal_detail_view = iProfile
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def define_polygonal_exact_clipping_view(self, profil=None):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Sub DefinePolygonalExactClippingView(CATSafeArrayVariant
                | profil)
                | 
                |     Defines a polygonal exact clipping on the current view.
                | 
                |     Parameters:
                | 
                |         profil
                |             the profile used, stored as a CATSafeArrayVariant of 2D
                |             coordinates, of dimension 2*n, n the number of control points on profile.
                |             Returns
                |             Legal values : S_OK if clipping definition succeeded or E_FAIL if the clipping definition failed

        :param tuple profil:
        :return: None
        """
        return self.drawing_view_generative_behavior.DefinePolygonalExactClippingView(profil)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'define_polygonal_exact_clipping_view'
        # # vba_code = """
        # # Public Function define_polygonal_exact_clipping_view(drawing_view_generative_behavior)
        # #     Dim profil (2)
        # #     drawing_view_generative_behavior.DefinePolygonalExactClippingView profil
        # #     define_polygonal_exact_clipping_view = profil
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def define_projection_view(self, i_parent_view_generative_behavior=None, i_type=None):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Sub DefineProjectionView(DrawingViewGenerativeBehavior
                | iParentViewGenerativeBehavior,
                | CatProjViewType iType)
                | 
                |     Defines a projection drawing view.
                | 
                |     Parameters:
                | 
                |         iParentViewGenerativeBehavior
                |             The generative behavior of the parent view. 
                |         iType
                |             The type of the drawing view with respect to its parent view
                |             
                | 
                |     Example:
                | 
                |           This example defines MyView as a right view of the front
                |           view
                |          considered as its parent view whose generative behavior
                |          is
                |          MyParentViewGB.
                |          
                | 
                |          MyView.GenerativeBehavior.DefineProjectionView MyParentViewGB,
                |          catRightView

        :param DrawingViewGenerativeBehavior i_parent_view_generative_behavior:
        :param CatProjViewType i_type:
        :return: None
        """
        return self.drawing_view_generative_behavior.DefineProjectionView(i_parent_view_generative_behavior, i_type)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'define_projection_view'
        # # vba_code = """
        # # Public Function define_projection_view(drawing_view_generative_behavior)
        # #     Dim iParentViewGenerativeBehavior (2)
        # #     drawing_view_generative_behavior.DefineProjectionView iParentViewGenerativeBehavior
        # #     define_projection_view = iParentViewGenerativeBehavior
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def define_section_view(self, i_profile=None, i_section_type=None, i_profile_type=None, i_side_to_draw=None,
                            i_parent_view_generative_behavior=None):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Sub DefineSectionView(CATSafeArrayVariant iProfile,
                | CATBSTR iSectionType,
                | CATBSTR iProfileType,
                | short iSideToDraw,
                | DrawingViewGenerativeBehavior iParentViewGenerativeBehavior)
                | 
                |     Defines a section drawing view. A section drawing view is defined using a
                |     section profile defined itself as a polyline, a section type to indicate
                |     whether to draw the section or only the section cut, a section profile type
                |     that can be offset or aligned, the side of the section to draw, and the
                |     generative behavior of the parent view.
                | 
                |     Parameters:
                | 
                |         iProfile
                |             The polyline defining the section profile. This polyline is passed
                |             as its point coordinate table. It has the following
                |             contents:
                | 
                |             iProfile[0] = X1
                |                 x coordinate of the first point 
                |             iProfile[1] = Y1
                |                 y coordinate of the first point 
                |             iProfile[2] = X2
                |                 x coordinate of the second point 
                |             iProfile[3] = Y2
                |                 y coordinate of the second point 
                |             ...
                |             iProfile[2n-2] = Xn
                |                 x coordinate of the nth and last point 
                |             iProfile[2n-1] = Yn
                |                 y coordinate of the nth and last point 
                | 
                |         iSectionType
                |             The section type: SectionCut or SectionView 
                |         iProfileType
                |             The cutting profile type: Offset or Aligned 
                |         iSideToDraw
                |             The side of the section to draw. This side is defined according to
                |             the first segment of the section profile. This segment is oriented from its
                |             start point to its end point. When looking along this segment, from its start
                |             point towards its end point, setting iSideToDraw to 0 (clockwise) draws the
                |             section seen from the left of the segment. Setting iSideToDraw to 1
                |             (counterclockwise)draws the section seen from the right of the
                |             segment.
                |             0 Clockwise
                |             1 Counterclockwise 
                |         iParentViewGenerativeBehavior
                |             The generative behavior of the parent view. The section profile is
                |             defined with respect to this parent view axis system
                |             
                | 
                |     Example:
                | 
                |           This example defines MyView as an offset section view of the
                |           view
                |          considered as its parent view whose generative behavior
                |          is
                |          MyParentViewGB.
                |          The section is seen from the left of the first section profile
                |          segment.
                |          The section profile is defined in the SectionProfile
                |          array.
                |          
                | 
                |          Dim SectionProfile
                |          ReDim SectionProfile(7)
                |          SectionProfile(0) = 10.
                |          SectionProfile(1) = 200.
                |          SectionProfile(2) = 100.
                |          SectionProfile(3) = 200.
                |          SectionProfile(4) = 100.
                |          SectionProfile(5) = 50.
                |          SectionProfile(6) = 300.
                |          SectionProfile(7) = 50.
                |          MyView.GenerativeBehavior.DefineSectionView SectionProfile,
                |          SectionView, Offset, 0, MyParentViewGB

        :param tuple i_profile:
        :param str i_section_type:
        :param str i_profile_type:
        :param enum i_side_to_draw:
        :param DrawingViewGenerativeBehavior i_parent_view_generative_behavior:
        :return: None
        """
        return self.drawing_view_generative_behavior.DefineSectionView(i_profile, i_section_type, i_profile_type,
                                                                       i_side_to_draw,
                                                                       i_parent_view_generative_behavior)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'define_section_view'
        # # vba_code = """
        # # Public Function define_section_view(drawing_view_generative_behavior)
        # #     Dim iProfile (2)
        # #     drawing_view_generative_behavior.DefineSectionView iProfile
        # #     define_section_view = iProfile
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def define_stand_alone_section(self, profil=None, type_of_section=None, type_of_profile=None, i_plane=None,
                                   i_side=None):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Sub DefineStandAloneSection(CATSafeArrayVariant profil,
                | CATBSTR type_of_section,
                | CATBSTR type_of_profile,
                | CATSafeArrayVariant iPlane,
                | short iSide)
                | 
                |     Defines a section view without a reference view.
                | 
                |     Parameters:
                | 
                |         profil
                |             the profile used, stored as a CATSafeArrayVariant of 2D
                |             coordinates, of dimension 2*n, n the number of control points on profile.
                |             
                |         type_of_section
                | 
                |             Legal values : SectionCut SectionView 
                |         type_of_profile
                | 
                |             Legal values : Aligned Offset 
                |         iPlane
                |             the reference plane, on which the profile lies Plane1 [0...2] : Plane origine coordinates Plane1 [3...5] : First direction vector coordinates Plane1 [6...8] : Second direction vector coordinates. 
                |         iSide
                | 
                |             Legal values : 1 -1 
                | 
                |     Returns:
                |     S_OK
                |         if the section was correctly defined 
                |     E_FAIL
                |         if the operation failed. 
                | 
                | Example:
                | 
                |      // 3 points profile 
                |     Dim arrayOfVariantOfDouble1(5)
                |     arrayOfVariantOfDouble1(0) = -30.000000
                |     arrayOfVariantOfDouble1(1) = -150.000000
                |     arrayOfVariantOfDouble1(2) = -30.000000
                |     arrayOfVariantOfDouble1(3) = -50.000000
                |     arrayOfVariantOfDouble1(4) = 21.997045
                |     arrayOfVariantOfDouble1(5) = -50.000000
                |     // XY plane
                |     Dim arrayOfVariantOfDouble2(8)
                |     arrayOfVariantOfDouble2(0) =  0.000000
                |     arrayOfVariantOfDouble2(1) =  0.000000
                |     arrayOfVariantOfDouble2(2) =  0.000000
                |     arrayOfVariantOfDouble2(3) =  1.000000
                |     arrayOfVariantOfDouble2(4) =  0.000000
                |     arrayOfVariantOfDouble2(5) =  0.000000
                |     arrayOfVariantOfDouble2(6) =  0.000000
                |     arrayOfVariantOfDouble2(7) =  1.000000
                |     arrayOfVariantOfDouble2(8) =  0.000000
                |     // defines offset sectionview
                |     drawingViewGenerativeBehavior1.DefineStandAloneSection
                |     arrayOfVariantOfDouble1, "SectionView", "Offset", arrayOfVariantOfDouble2,
                |     1

        :param tuple profil:
        :param str type_of_section:
        :param str type_of_profile:
        :param tuple i_plane:
        :param enum i_side:
        :return: None
        """
        return self.drawing_view_generative_behavior.DefineStandAloneSection(profil, type_of_section, type_of_profile,
                                                                             i_plane, i_side)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'define_stand_alone_section'
        # # vba_code = """
        # # Public Function define_stand_alone_section(drawing_view_generative_behavior)
        # #     Dim profil (2)
        # #     drawing_view_generative_behavior.DefineStandAloneSection profil
        # #     define_stand_alone_section = profil
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def define_tps_section_view(self, i_profile=None, i_section_type=None, i_profile_type=None, i_side_to_draw=None,
                                i_parent_view_generative_behavior=None):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Sub DefineTPSSectionView(CATSafeArrayVariant iProfile,
                | CATBSTR iSectionType,
                | CATBSTR iProfileType,
                | short iSideToDraw,
                | DrawingViewGenerativeBehavior iParentViewGenerativeBehavior)
                | 
                |     Defines a TPS section drawing view. A section TPS drawing view is defined
                |     using a section profile defined itself as a polyline, a section type to
                |     indicate whether to draw the section or only the section cut, a section profile
                |     type that can be offset or aligned, the side of the section to draw, and the
                |     generative behavior of the parent view.
                | 
                |     Parameters:
                | 
                |         iProfile
                |             The polyline defining the section profile. This polyline is passed
                |             as its point coordinate table. It has the following
                |             contents:
                | 
                |             iProfile[0] = X1
                |                 x coordinate of the first point 
                |             iProfile[1] = Y1
                |                 y coordinate of the first point 
                |             iProfile[2] = X2
                |                 x coordinate of the second point 
                |             iProfile[3] = Y2
                |                 y coordinate of the second point 
                |             ...
                |             iProfile[2n-2] = Xn
                |                 x coordinate of the nth and last point 
                |             iProfile[2n-1] = Yn
                |                 y coordinate of the nth and last point 
                | 
                |         iSectionType
                |             The section type: SectionCut or SectionView 
                |         iProfileType
                |             The cutting profile type: Offset or Aligned 
                |         iSideToDraw
                |             The side of the section to draw. This side is defined according to
                |             the first segment of the section profile. This segment is oriented from its
                |             start point to its end point. When looking along this segment, from its start
                |             point towards its end point, setting iSideToDraw to 0 (clockwise) draws the
                |             section seen from the left of the segment. Setting iSideToDraw to 1
                |             (counterclockwise)draws the section seen from the right of the
                |             segment.
                |             0 Clockwise
                |             1 Counterclockwise 
                |         iParentViewGenerativeBehavior
                |             The generative behavior of the parent view. The section profile is
                |             defined with respect to this parent view axis system
                |             
                | 
                |     Example:
                | 
                |           This example defines MyView as an offset section view of the
                |           view
                |          considered as its parent view whose generative behavior
                |          is
                |          MyParentViewGB.
                |          The section is seen from the left of the first section profile
                |          segment.
                |          The section profile is defined in the SectionProfile
                |          array.
                |          
                | 
                |          Dim SectionProfile
                |          ReDim SectionProfile(7)
                |          SectionProfile(0) = 10.
                |          SectionProfile(1) = 200.
                |          SectionProfile(2) = 100.
                |          SectionProfile(3) = 200.
                |          SectionProfile(4) = 100.
                |          SectionProfile(5) = 50.
                |          SectionProfile(6) = 300.
                |          SectionProfile(7) = 50.
                |          MyView.GenerativeBehavior.DefineSectionView SectionProfile,
                |          SectionView, Offset, 0, MyParentViewGB

        :param tuple i_profile:
        :param str i_section_type:
        :param str i_profile_type:
        :param enum i_side_to_draw:
        :param DrawingViewGenerativeBehavior i_parent_view_generative_behavior:
        :return: None
        """
        return self.drawing_view_generative_behavior.DefineTPSSectionView(i_profile, i_section_type, i_profile_type,
                                                                          i_side_to_draw,
                                                                          i_parent_view_generative_behavior)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'define_tps_section_view'
        # # vba_code = """
        # # Public Function define_tps_section_view(drawing_view_generative_behavior)
        # #     Dim iProfile (2)
        # #     drawing_view_generative_behavior.DefineTPSSectionView iProfile
        # #     define_tps_section_view = iProfile
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def define_unfolded_view(self, i_x1=None, i_y1=None, i_z1=None, i_x2=None, i_y2=None, i_z2=None):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Sub DefineUnfoldedView(double iX1,
                | double iY1,
                | double iZ1,
                | double iX2,
                | double iY2,
                | double iZ2)
                | 
                |     Defines a unfolded drawing view. The unfolded view is defined using its
                |     projection plane, passed as the components of two vectors V1 and V2. The cross
                |     product of vector V1(X1, Y1, Z1) by vector V2(X2, Y2, Z2) defines the
                |     projection direction.
                | 
                |     Parameters:
                | 
                |         iX1,iY1,iZ1
                |             The components of the first vector with respect to the document 3D
                |             axis system 
                |         iX2,iY2,iZ2
                |             The components of the second vector with respect to the document 3D
                |             axis system 
                | 
                |     Example:
                | 
                |           This example defines MyView as a unfolded view by projecting
                |           the
                |          represented document in the YZ 3D plane.
                |          
                | 
                |          MyView.GenerativeBehavior.DefineUnfoldedView 0., 1., 0., 0., 0.,
                |          1.

        :param float i_x1:
        :param float i_y1:
        :param float i_z1:
        :param float i_x2:
        :param float i_y2:
        :param float i_z2:
        :return: None
        """
        return self.drawing_view_generative_behavior.DefineUnfoldedView(i_x1, i_y1, i_z1, i_x2, i_y2, i_z2)

    def force_update(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Sub ForceUpdate()
                | 
                |     Forces the Update the drawing view even if not necessary.
                | 
                |     Example:
                | 
                |           This example updates the  MyView drawing view.
                |          
                | 
                |          MyView.GenerativeBehavior.ForceUpdate()

        :return: None
        """
        return self.drawing_view_generative_behavior.ForceUpdate()

    def get_axis_systeme(self, o_product=None, o_axis_systeme=None):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Sub GetAxisSysteme(AnyObject oProduct,
                | AnyObject oAxisSysteme)
                | 
                |     Retrieves the axis systeme associated with the view.
                | 
                |     Parameters:
                | 
                |         oProduct
                |             The reference product stored as a CATIABase. 
                |         oAxisSysteme
                |             The axis system stored as a CATIABase.

        :param AnyObject o_product:
        :param AnyObject o_axis_systeme:
        :return: None
        """
        return self.drawing_view_generative_behavior.GetAxisSysteme(o_product, o_axis_systeme)

    def get_gps_name(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Func GetGPSName() As CATBSTR
                | 
                |     Retrieves the set of generative parameters currently applied to the view.
                |     Parameters will be taken into account at view update time.
                | 
                |     Parameters:
                | 
                |         ioGPSName
                |             The XML file where generative parameters are retrieved from
                |             
                | 
                |     Returns:
                |     S_OK
                |         if the operation succeeded. 
                |     E_FAIL
                | 
                | Example:
                | 
                |       This example retrieves the generative parameters file applied to the
                |       MyView drawing view as GPSFile.
                |      
                | 
                |      MyView.GenerativeBehavior.GetGPSName GPSFile

        :return: str
        """
        return str(self.drawing_view_generative_behavior.GetGPSName())

    def get_projection_plane(self, o_x1=None, o_y1=None, o_z1=None, o_x2=None, o_y2=None, o_z2=None):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Sub GetProjectionPlane(double oX1,
                | double oY1,
                | double oZ1,
                | double oX2,
                | double oY2,
                | double oZ2)
                | 
                |     Returns the drawing view projection plane.
                | 
                |     Parameters:
                | 
                |         oX1,oY1,oZ1
                |             The components of the first vector with respect to the document 3D
                |             axis system 
                |         oX2,oY2,oZ2
                |             The components of the second vector with respect to the document 3D
                |             axis system 
                | 
                |     Example:
                | 
                |           This example retrieves the projection plane of the MyView
                |           drawing
                |          view as two sets of components, X1, Y1, and Z1 for the first
                |          vector,
                |          X2, Y2, and Z2 for the second vector.
                |          
                | 
                |          MyView.GenerativeBehavior.GetProjectionPlane X1, Y1, Z1, X2, Y2, Z2

        :param float o_x1:
        :param float o_y1:
        :param float o_z1:
        :param float o_x2:
        :param float o_y2:
        :param float o_z2:
        :return: None
        """
        return self.drawing_view_generative_behavior.GetProjectionPlane(o_x1, o_y1, o_z1, o_x2, o_y2, o_z2)

    def get_projection_plane_normal(self, o_x_normal=None, o_y_normal=None, o_z_normal=None):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Sub GetProjectionPlaneNormal(double oXNormal,
                | double oYNormal,
                | double oZNormal)
                | 
                |     Returns the normal vector of the drawing view projection plane. This
                |     represents the direction of projection.
                | 
                |     Parameters:
                | 
                |         oXNormal,oYNormal,oZNormal
                |             The components of the projection plane normal vector with respect
                |             to the document 3D axis system 
                | 
                |     Example:
                | 
                |           This example retrieves the projection plane normal vector of
                |           the
                |          MyView drawing view as three components Xn, Yn, and
                |          Zn.
                |          
                | 
                |          MyView.GenerativeBehavior.GetProjectionPlaneNormal Xn, Yn, Zn

        :param float o_x_normal:
        :param float o_y_normal:
        :param float o_z_normal:
        :return: None
        """
        return self.drawing_view_generative_behavior.GetProjectionPlaneNormal(o_x_normal, o_y_normal, o_z_normal)

    def set_axis_systeme(self, i_product=None, i_axis_systeme=None):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Sub SetAxisSysteme(AnyObject iProduct,
                | AnyObject iAxisSysteme)
                | 
                |     Defines an axis systeme in the view.
                | 
                |     Parameters:
                | 
                |         iProduct
                |             The reference product stored as a CATIABase. 
                |         iAxisSysteme
                |             The axis system stored as a CATIABase.

        :param AnyObject i_product:
        :param AnyObject i_axis_systeme:
        :return: None
        """
        return self.drawing_view_generative_behavior.SetAxisSysteme(i_product, i_axis_systeme)

    def set_gps_name(self, i_gps_name=None):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Sub SetGPSName(CATBSTR iGPSName)
                | 
                |     Applies a set of generative parameters to the current view. Parameters will
                |     be taken into account at view update time.
                | 
                |     Parameters:
                | 
                |         iGPSName
                |             The XML file where generative parameters are retrieved from
                |             
                | 
                |     Returns:
                |     S_OK
                |         if the operation succeeded. 
                |     E_FAIL
                | 
                | Example:
                | 
                |       This example applied the GPSFile1 to the MyView drawing
                |       view.
                |      
                | 
                |      MyView.GenerativeBehavior.SetGPSName "GPSFile1.xml"

        :param str i_gps_name:
        :return: None
        """
        return self.drawing_view_generative_behavior.SetGPSName(i_gps_name)

    def set_projection_plane(self, i_x1=None, i_y1=None, i_z1=None, i_x2=None, i_y2=None, i_z2=None):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Sub SetProjectionPlane(double iX1,
                | double iY1,
                | double iZ1,
                | double iX2,
                | double iY2,
                | double iZ2)
                | 
                |     Sets the drawing view projection plane. The projection plane is the plane
                |     to which the document's geometrical objects are projected and is used as the
                |     drawing view plane. This plane is defined in the document 3D space using the
                |     components of two of its vectors. The cross product of vector V1(X1, Y1, Z1) by
                |     vector V2(X2, Y2, Z2) defines the projection direction. This method can be used
                |     with front views and isometric views to change the projection plane defined
                |     when such views were created. It should not be used with the other types of
                |     views, since their projection planes are defined with respect to their parent
                |     view projection plane.
                | 
                |     Parameters:
                | 
                |         iX1,iY1,iZ1
                |             The components of the first vector with respect to the document 3D
                |             axis system 
                |         iX2,iY2,iZ2
                |             The components of the second vector with respect to the document 3D
                |             axis system 
                | 
                |     Example:
                | 
                |           This example sets the projection plane of the MyView drawing
                |           view
                |          to the XY plane, that is the plane defined with the vectors (1., 0.,
                |          0.) and
                |          (0., 1., 0.).
                |          
                | 
                |          MyView.GenerativeBehavior.SetProjectionPlane 1., 0., 0., 0., 1., 0.

        :param float i_x1:
        :param float i_y1:
        :param float i_z1:
        :param float i_x2:
        :param float i_y2:
        :param float i_z2:
        :return: None
        """
        return self.drawing_view_generative_behavior.SetProjectionPlane(i_x1, i_y1, i_z1, i_x2, i_y2, i_z2)

    def un_break(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Sub UnBreak()
                | 
                |     If a view have been broken with lines in order to hide an area of this
                |     view, this method undoes this modification of the view, and the other types of
                |     view remain.
                | 
                |     Example:
                | 
                |           This example removes the BrokenView type from MyView if
                |           so.
                |          
                | 
                |          MyView.GenerativeBehavior.UnBreak()

        :return: None
        """
        return self.drawing_view_generative_behavior.UnBreak()

    def un_breakout(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Sub UnBreakout()
                | 
                |     If a view have gone through a breakout view operation, this method removes
                |     all the breakout view done on this view, and the other types of view
                |     remain.
                | 
                |     Example:
                | 
                |           This example removes all the breakouts view done on MyView if
                |           so.
                |          
                | 
                |          MyView.GenerativeBehavior.UnBreakout()

        :return: None
        """
        return self.drawing_view_generative_behavior.UnBreakout()

    def un_breakout_num(self, i_breakout_number=None):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Sub UnBreakoutNum(short iBreakoutNumber)
                | 
                |     If a view have gone through a breakout view operation, this method removes
                |     the specified breakout view done on this view, and the other types of view
                |     remain.
                | 
                |     Parameters:
                | 
                |         iBreakoutNumber
                |             The reference number of the breakout view to be removed (1 to n)
                |             
                | 
                |     Example:
                | 
                |           This example removes the first breakout view done on MyView if
                |           so.
                |          
                | 
                |          MyView.GenerativeBehavior.UnBreakout(1)

        :param enum i_breakout_number:
        :return: None
        """
        return self.drawing_view_generative_behavior.UnBreakoutNum(i_breakout_number)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'un_breakout_num'
        # # vba_code = """
        # # Public Function un_breakout_num(drawing_view_generative_behavior)
        # #     Dim iBreakoutNumber (2)
        # #     drawing_view_generative_behavior.UnBreakoutNum iBreakoutNumber
        # #     un_breakout_num = iBreakoutNumber
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def un_clip(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Sub UnClip()
                | 
                |     If a view have been clipped, this method removes the last clipping view
                |     done on this view, and the other types of view remain.
                | 
                |     Example:
                | 
                |           This example removes the last clipping view done on MyView if
                |           so.
                |          
                | 
                |          MyView.GenerativeBehavior.UnClip()

        :return: None
        """
        return self.drawing_view_generative_behavior.UnClip()

    def update(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Sub Update()
                | 
                |     Updates the drawing view. This update is performed with respect to any
                |     modification of its DrawingView.GenerativeBehavior
                |     property.
                | 
                |     Example:
                | 
                |           This example updates the  MyView drawing view.
                |          
                | 
                |          MyView.GenerativeBehavior.Update()

        :return: None
        """
        return self.drawing_view_generative_behavior.Update()

    def __repr__(self):
        return f'DrawingViewGenerativeBehavior(name="{self.name}")'
