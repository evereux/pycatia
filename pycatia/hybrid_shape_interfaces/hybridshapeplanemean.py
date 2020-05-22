#! /usr/bin/python3.6
# module initially auto generated using V5Automation.chm from CATIA R25 on 2020-05-22 12:54:36.956119

from pycatia.mec_mod_interfaces.hybridshape import HybridShape


class HybridShapePlaneMean(HybridShape):
    """
        .. note::
            CAA V5 Visual Basic help

                | Represents the hybrid shape mean plane feature object.Role: To access
                | the data of the hybrid shape mean plane feature object. This data
                | includes:Use the  CATIAHybridShapeFactory to create a
                | HybridShapePlaneMean object.

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_plane_mean = com_object     

    def add_point(self, i_passing_point):
        """
        .. note::
            CAA V5 Visual Basic help

                | AddPoint
                | o Sub AddPoint(        iPassingPoint)
                | 
                | Adds a point to the mean plane.
                |
                | Parameters:
                | iPassingPoint
                |     The point to add
                | Sub-element(s) supported (see 
                | 
                |  object):  
                | .


        :param i_passing_point:
        :return:
        """
        return self.hybrid_shape_plane_mean.AddPoint(i_passing_point)

    def get_point(self, i_rank, o_passing_point):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetPoint
                | o Sub GetPoint(        iRank,
                |                        oPassingPoint)
                | 
                | Retrieves the point at a given position.
                |
                | Parameters:
                | iRank
                |     The rank of the point to retrieve
                |  
                |  oPassingPoint
                |     The point retrieved at this rank


        :param i_rank:
        :param o_passing_point:
        :return:
        """
        return self.hybrid_shape_plane_mean.GetPoint(i_rank, o_passing_point)

    def get_pos(self, i_point):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetPos
                | o Func GetPos(        iPoint) As
                | 
                | Gets the position of an element in the list.
                |
                | Parameters:
                | iPoint
                |       point 
                |    
                |  oPos
                |       position of point


        :param i_point:
        :return:
        """
        return self.hybrid_shape_plane_mean.GetPos(i_point)

    def get_size(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetSize
                | o Func GetSize(    ) As
                | 
                | Gets the size of the list (number of points).
                |
                | Parameters:
                | oSize
                |        position of point


        :return:
        """
        return self.hybrid_shape_plane_mean.GetSize()

    def remove_all(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | RemoveAll
                | o Sub RemoveAll(    )
                | 
                | Removes all elements in the list of points.
                |
                | Parameters:


        :return:
        """
        return self.hybrid_shape_plane_mean.RemoveAll()

    def remove_element(self, i_rank):
        """
        .. note::
            CAA V5 Visual Basic help

                | RemoveElement
                | o Sub RemoveElement(        iRank)
                | 
                | Removes a point in the list.
                |
                | Parameters:
                | iRank
                |     The rank of the point to remove


        :param i_rank:
        :return:
        """
        return self.hybrid_shape_plane_mean.RemoveElement(i_rank)

    def replace_point_at_position(self, i_point, i_pos):
        """
        .. note::
            CAA V5 Visual Basic help

                | ReplacePointAtPosition
                | o Sub ReplacePointAtPosition(        iPoint,
                |                                      iPos)
                | 
                | Replaces a point in the list at the given position.
                |
                | Parameters:
                | oPoint
                |       point 
                |    
                |  iPos
                |       position of point


        :param i_point:
        :param i_pos:
        :return:
        """
        return self.hybrid_shape_plane_mean.ReplacePointAtPosition(i_point, i_pos)

    def __repr__(self):
        return f'HybridShapePlaneMean()'
