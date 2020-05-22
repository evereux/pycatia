#! /usr/bin/python3.6
# module initially auto generated using V5Automation.chm from CATIA R25 on 2020-05-22 12:54:36.956119

from pycatia.mec_mod_interfaces.hybridshape import HybridShape


class HybridShapeLineTangency(HybridShape):
    """
        .. note::
            CAA V5 Visual Basic help

                | Line tangent to a curve.Role: To access data of the line feature
                | created to  be tangent to a curve at a given point.Use the
                | CATIAHybridShapeFactory to create a HybridShapeLineTangency object.

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_line_tangency = com_object     

    @property
    def begin_offset(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | BeginOffset
                | o Property BeginOffset(    ) As   (Read Only)
                | 
                | Returns the start length of the line. Start length :
                | extension of the line, beginning at the starting point
                | 
                |
                | Example:
                | This example retrieves in oStart the beginning
                | offset length for the LineTangency hybrid shape feature. Dim
                | oStart As CATIALength Set oStart = LineTangency.BeginOffset

        :return:
        """
        return self.hybrid_shape_line_tangency.BeginOffset

    @property
    def curve(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Curve
                | o Property Curve(    ) As
                | 
                | Returns or Sets the curve to which the line will be tangent.
                | Sub-element(s) supported (see object): or . 
                |
                | Example:
                | This
                | example retrieves in oCurve the reference curve for the
                | LineTangency hybrid shape feature. Dim oCurve As Reference
                | Set oCurve = LineTangency.Curve

        :return:
        """
        return self.hybrid_shape_line_tangency.Curve

    @property
    def end_offset(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | EndOffset
                | o Property EndOffset(    ) As   (Read Only)
                | 
                | Returns the end length of the line. End length : extension
                | of the line, beginning at the ending point 
                |
                | Example:
                | This
                | example retrieves in oEnd the starting length for the
                | LineTangency hybrid shape feature. Dim oEnd As CATIALength
                | Set oEnd = LineTangency.EndOffset

        :return:
        """
        return self.hybrid_shape_line_tangency.EndOffset

    @property
    def orientation(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Orientation
                | o Property Orientation(    ) As
                | 
                | Returns or Sets the line orientation. Orientation allows to
                | reverse the line direction from the reference point. For a
                | line of L length, it is the same as creating this line with
                | -L length : Orientation : can be 1 or -1 
                |
                | Example:
                | This
                | example retrieves in oOrientation the starting length for
                | the LineTangency hybrid shape feature. Dim oOrientation As
                | long Set oOrientation = LineTangency.Orientation

        :return:
        """
        return self.hybrid_shape_line_tangency.Orientation

    @property
    def point(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Point
                | o Property Point(    ) As
                | 
                | Returns or Sets the starting point of the line. Sub-
                | element(s) supported (see object): . 
                |
                | Example:
                | This example
                | retrieves in oPoint the starting point for the LineTangency
                | hybrid shape feature. Dim oPoint As Reference Set oPoint =
                | LineTangency.Point

        :return:
        """
        return self.hybrid_shape_line_tangency.Point

    @property
    def support(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Support
                | o Property Support(    ) As
                | 
                | Returns or Sets the support surface. Note: Support surface
                | is not mandatory Sub-element(s) supported (see object): .
                | 
                |
                | Example:
                | This example retrieves in oSurface the suupporting
                | Surface (if exist) for the LineTangency hybrid shape
                | feature. Dim oSurface As Reference Set oSurface =
                | LineTangency.Surface

        :return:
        """
        return self.hybrid_shape_line_tangency.Support

    def get_length_type(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetLengthType
                | o Func GetLengthType(    ) As
                | 
                | Gets the length type Default is 0.
                |
                | Parameters:
                | oType
                |    The length type = 0 : length               - the line is limited by its extremities
                |                    = 1 : infinite             - the line is infinite
                |                    = 2 : infinite start point - the line is infinite on the side of the start point
                |                    = 3 : infinite end point   - the line is infinite on the side of the end point


        :return:
        """
        return self.hybrid_shape_line_tangency.GetLengthType()

    def get_symmetrical_extension(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetSymmetricalExtension
                | o Func GetSymmetricalExtension(    ) As
                | 
                | Gets whether the symmetrical extension of the line is
                | active.
                |
                | Parameters:
                | oSym
                |        Symetry flag


        :return:
        """
        return self.hybrid_shape_line_tangency.GetSymmetricalExtension()

    def remove_support(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | RemoveSupport
                | o Sub RemoveSupport(    )
                | 
                | Removes the support surface.
                |
                | Parameters:


        :return:
        """
        return self.hybrid_shape_line_tangency.RemoveSupport()

    def set_length_type(self, i_type):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetLengthType
                | o Sub SetLengthType(        iType)
                | 
                | Sets the length type Default is 0.
                |
                | Parameters:
                | iType
                |    The length type = 0 : length               - the line is limited by its extremities
                |                    = 1 : infinite             - the line is infinite
                |                    = 2 : infinite start point - the line is infinite on the side of the start point
                |                    = 3 : infinite end point   - the line is infinite on the side of the end point


        :param i_type:
        :return:
        """
        return self.hybrid_shape_line_tangency.SetLengthType(i_type)

    def set_symmetrical_extension(self, i_sym):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetSymmetricalExtension
                | o Sub SetSymmetricalExtension(        iSym)
                | 
                | Sets the symmetrical extension of the line (start = -end).
                |
                | Parameters:
                | iSym
                |        Symetry flag


        :param i_sym:
        :return:
        """
        return self.hybrid_shape_line_tangency.SetSymmetricalExtension(i_sym)

    def __repr__(self):
        return f'HybridShapeLineTangency()'
