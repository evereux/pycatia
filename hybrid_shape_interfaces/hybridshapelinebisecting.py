#! /usr/bin/python3.6
# module initially auto generated using V5Automation.chm from CATIA R25 on 2020-05-22 12:54:36.956119

from pycatia.mec_mod_interfaces.hybridshape import HybridShape


class HybridShapeLineBisecting(HybridShape):
    """
        .. note::
            CAA V5 Visual Basic help

                | Represents the hybrid shape bisecting line feature object.Role: To
                | access the data of the hybrid shape bisecting line feature object.
                | This data includes:Use the  CATIAHybridShapeFactory to create a
                | HybridShapeAffinity object.

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_line_bisecting = com_object     

    @property
    def begin_offset(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | BeginOffset
                | o Property BeginOffset(    ) As   (Read Only)
                | 
                | Returns the start offset of the line.

        :return:
        """
        return self.hybrid_shape_line_bisecting.BeginOffset

    @property
    def elem1(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Elem1
                | o Property Elem1(    ) As
                | 
                | Returns or sets the first line used to create the bisecting
                | line. Sub-element(s) supported (see object): see or .

        :return:
        """
        return self.hybrid_shape_line_bisecting.Elem1

    @elem1.setter
    def elem1(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_line_bisecting.Elem1 = value 

    @property
    def elem2(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Elem2
                | o Property Elem2(    ) As
                | 
                | Returns or sets the second line used to create the bisecting
                | line. Sub-element(s) supported (see object): see or .

        :return:
        """
        return self.hybrid_shape_line_bisecting.Elem2

    @elem2.setter
    def elem2(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_line_bisecting.Elem2 = value 

    @property
    def end_offset(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | EndOffset
                | o Property EndOffset(    ) As   (Read Only)
                | 
                | Returns the end offset of the line.

        :return:
        """
        return self.hybrid_shape_line_bisecting.EndOffset

    @property
    def orientation(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Orientation
                | o Property Orientation(    ) As
                | 
                | Returns or sets the orientation used to compute the
                | bisecting line. Role: the orientation specifies bisecting
                | line position Legal values: The orientation can be the
                | same(1) or the inverse(-1)

        :return:
        """
        return self.hybrid_shape_line_bisecting.Orientation

    @orientation.setter
    def orientation(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_line_bisecting.Orientation = value 

    @property
    def ref_point(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | RefPoint
                | o Property RefPoint(    ) As
                | 
                | Returns or sets the reference point used to create the
                | bisecting line. Sub-element(s) supported (see object): see .

        :return:
        """
        return self.hybrid_shape_line_bisecting.RefPoint

    @ref_point.setter
    def ref_point(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_line_bisecting.RefPoint = value 

    @property
    def solution_type(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | SolutionType
                | o Property SolutionType(    ) As
                | 
                | Returns or sets the solution type. Role: The solution type
                | allows you to know where is the bisecting line.

        :return:
        """
        return self.hybrid_shape_line_bisecting.SolutionType

    @solution_type.setter
    def solution_type(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_line_bisecting.SolutionType = value 

    @property
    def support(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Support
                | o Property Support(    ) As
                | 
                | Returns or sets the support used to create the bisecting
                | line.

        :return:
        """
        return self.hybrid_shape_line_bisecting.Support

    @support.setter
    def support(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_line_bisecting.Support = value 

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
        return self.hybrid_shape_line_bisecting.GetLengthType()

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
        return self.hybrid_shape_line_bisecting.GetSymmetricalExtension()

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
        return self.hybrid_shape_line_bisecting.SetLengthType(i_type)

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
        return self.hybrid_shape_line_bisecting.SetSymmetricalExtension(i_sym)

    def __repr__(self):
        return f'HybridShapeLineBisecting()'
