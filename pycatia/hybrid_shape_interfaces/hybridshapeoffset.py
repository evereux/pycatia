#! /usr/bin/python3.6
# module initially auto generated using V5Automation.chm from CATIA R25 on 2020-05-22 12:54:36.956119

from pycatia.mec_mod_interfaces.hybridshape import HybridShape


class HybridShapeOffset(HybridShape):
    """
        .. note::
            CAA V5 Visual Basic help

                | Represents the hybrid shape offset feature object.Role: To access the
                | data of the hybrid shape offset feature object. This data includes:Use
                | the  CATIAHybridShapeFactory to create a HybridShapeOffset object.

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_offset = com_object     

    @property
    def offset_direction(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | OffsetDirection
                | o Property OffsetDirection(    ) As
                | 
                | Returns or sets whether the offset direction is to be
                | inverted. True to invert the offset direction.

        :return:
        """
        return self.hybrid_shape_offset.OffsetDirection

    @offset_direction.setter
    def offset_direction(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_offset.OffsetDirection = value 

    @property
    def offset_value(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | OffsetValue
                | o Property OffsetValue(    ) As
                | 
                | Returns or sets the offset value.

        :return:
        """
        return self.hybrid_shape_offset.OffsetValue

    @offset_value.setter
    def offset_value(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_offset.OffsetValue = value 

    @property
    def offseted_object(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | OffsetedObject
                | o Property OffsetedObject(    ) As
                | 
                | Returns or sets the face to offset. Sub-element(s) supported
                | (see object): .

        :return:
        """
        return self.hybrid_shape_offset.OffsetedObject

    @offseted_object.setter
    def offseted_object(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_offset.OffsetedObject = value 

    @property
    def suppress_mode(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | SuppressMode
                | o Property SuppressMode(    ) As
                | 
                | Returns or sets suppress mode. True to activate suppress
                | mode

        :return:
        """
        return self.hybrid_shape_offset.SuppressMode

    @suppress_mode.setter
    def suppress_mode(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_offset.SuppressMode = value 

    def add_tricky_face(self, i_tricky_face):
        """
        .. note::
            CAA V5 Visual Basic help

                | AddTrickyFace
                | o Sub AddTrickyFace(        iTrickyFace)
                | 
                | Adds a tricky face object on the object.
                |
                | Parameters:


        :param i_tricky_face:
        :return:
        """
        return self.hybrid_shape_offset.AddTrickyFace(i_tricky_face)

    def get_tricky_face(self, i_rank):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetTrickyFace
                | o Func GetTrickyFace(        iRank) As
                | 
                | Returns the invalid face object on the object. param : iRank
                | =position of faces ionvalid for offset
                |
                | Parameters:


        :param i_rank:
        :return:
        """
        return self.hybrid_shape_offset.GetTrickyFace(i_rank)

    def remove_tricky_face(self, i_rank):
        """
        .. note::
            CAA V5 Visual Basic help

                | RemoveTrickyFace
                | o Sub RemoveTrickyFace(        iRank)
                | 
                | Remove the tricky face object on the object. param : iRank
                | =position of the face in the list of TrickyFaces
                |
                | Parameters:


        :param i_rank:
        :return:
        """
        return self.hybrid_shape_offset.RemoveTrickyFace(i_rank)

    def set_offset_value(self, i_offset):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetOffsetValue
                | o Sub SetOffsetValue(        iOffset)
                | 
                | Set Offset value with input as double. To be replace in
                | further release by integration in the pragma put_xxx
                |
                | Parameters:


        :param i_offset:
        :return:
        """
        return self.hybrid_shape_offset.SetOffsetValue(i_offset)

    def __repr__(self):
        return f'HybridShapeOffset()'
