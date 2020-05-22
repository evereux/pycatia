#! /usr/bin/python3.6
# module initially auto generated using V5Automation.chm from CATIA R25 on 2020-05-22 12:54:36.956119

from pycatia.mec_mod_interfaces.hybridshape import HybridShape


class Point(HybridShape):
    """
        .. note::
            CAA V5 Visual Basic help

                | Represents the hybrid shape Point feature object.Role: Declare  hybrid
                | shape Point root feature object.  All interfaces for different type of
                | Point derivates HybridShapePoint.Use the CATIAHybridShapeFactory to
                | create a HybridShapePoint objects.

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.point = com_object     

    def get_coordinates(self, o_coordinates):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetCoordinates
                | o Sub GetCoordinates(        oCoordinates)
                | 
                | Gets cartesian coordinates of the point.
                |
                | Parameters:
                | oCoordinates
                |     coordinates of the point.
                |  
                | 
                |  See also:


        :param o_coordinates:
        :return:
        """
        return self.point.GetCoordinates(o_coordinates)

    def set_coordinates(self, o_coordinates):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetCoordinates
                | o Sub SetCoordinates(        oCoordinates)
                | 
                | Sets cartesian coordinates of the point. Note:
                | SetCoordinates can only be used on
                | CATIAHybridShapePointCoord feature
                |
                | Parameters:
                | iCoordinates
                |     coordinates of the point.
                |  
                | 
                |  See also:


        :param o_coordinates:
        :return:
        """
        return self.point.SetCoordinates(o_coordinates)

    def __repr__(self):
        return f'Point()'
