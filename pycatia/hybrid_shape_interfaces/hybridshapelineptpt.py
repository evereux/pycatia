#! /usr/bin/python3.6
# module initially auto generated using V5Automation.chm from CATIA R25 on 2020-05-22 12:54:36.956119

from pycatia.mec_mod_interfaces.hybridshape import HybridShape


class HybridShapeLinePtPt(HybridShape):
    """
        .. note::
            CAA V5 Visual Basic help

                | Represents the hybrid shape line between two points feature
                | object.Role: To access the data of the line feature created between
                | two points.Use the  CATIAHybridShapeFactory to create a
                | HybridShapeLinePtPt object.

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_line_pt_pt = com_object

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
                | offset length for the LinePtPt hybrid shape feature. Dim
                | oStart As CATIALength Set oStart = LinePtPt.BeginOffset

        :return:
        """
        return self.hybrid_shape_line_pt_pt.BeginOffset

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
                | LinePtPt hybrid shape feature. Dim oEnd As CATIALength Set
                | oEnd = LinePtPt.EndOffset

        :return:
        """
        return self.hybrid_shape_line_pt_pt.EndOffset

    @property
    def pt_extremity(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | PtExtremity
                | o Property PtExtremity(    ) As
                | 
                | Returns or Sets the extremity point of the LinePtPt(Second
                | Point). Sub-element(s) supported (see object): . Example:
                | This example retrieves in oPtExtremity the ending point for
                | the LinePtPt hybrid shape feature. Dim oPtExtremity As
                | Reference Set oPtExtremity = LinePtPt.PtExtremity

        :return:
        """
        return self.hybrid_shape_line_pt_pt.PtExtremity

    @property
    def pt_origine(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | PtOrigine
                | o Property PtOrigine(    ) As
                | 
                | Returns or Sets the origin point of the LinePtPt(First
                | point). Sub-element(s) supported (see object): . Example:
                | This example retrieves in oPtOrigine the initial point for
                | the LinePtPt hybrid shape feature. Dim oPtOrigine As
                | Reference Set oPtOrigine = LinePtPt.PtOrigine

        :return:
        """
        return self.hybrid_shape_line_pt_pt.PtOrigine

    @property
    def support(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Support
                | o Property Support(    ) As
                | 
                | Returns or Sets the supporting surface. Note: the support
                | surface is not mandatory for LinePtPt Sub-element(s)
                | supported (see object): . 
                |
                | Example:
                | This example retrieves in
                | oSurface the supporting surface (if it exist) for the
                | LinePtPt hybrid shape feature. Dim oSurface As Reference Set
                | oSurface = LinePtPt.Surface

        :return:
        """
        return self.hybrid_shape_line_pt_pt.Support

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
        return self.hybrid_shape_line_pt_pt.GetLengthType()

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
        return self.hybrid_shape_line_pt_pt.GetSymmetricalExtension()

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
        return self.hybrid_shape_line_pt_pt.RemoveSupport()

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
        return self.hybrid_shape_line_pt_pt.SetLengthType(i_type)

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
        return self.hybrid_shape_line_pt_pt.SetSymmetricalExtension(i_sym)

    def __repr__(self):
        return f'HybridShapeLinePtPt(name="{self.name}")'
