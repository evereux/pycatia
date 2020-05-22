#! /usr/bin/python3.6
# module initially auto generated using V5Automation.chm from CATIA R25 on 2020-05-22 12:54:36.956119

from pycatia.mec_mod_interfaces.hybridshape import HybridShape


class HybridShapeSweep(HybridShape):
    """
        .. note::
            CAA V5 Visual Basic help

                | Represents the hybrid shape Sweep feature object.Role: Declare  hybrid
                | shape Sweep root feature object.  All interfaces for different type of
                | sweep derivates HybridShapeSweep.Use the CATIAHybridShapeFactory to
                | create a HybridShapeSweep objects.

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_sweep = com_object     

    @property
    def c0_vertices_mode(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | C0VerticesMode
                | o Property C0VerticesMode(    ) As
                | 
                | Returns or sets the management mode of C0 vertices as
                | twisted areas. TRUE or FALSE.

        :return:
        """
        return self.hybrid_shape_sweep.C0VerticesMode

    @c0_vertices_mode.setter
    def c0_vertices_mode(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_sweep.C0VerticesMode = value 

    @property
    def fill_twisted_areas(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | FillTwistedAreas
                | o Property FillTwistedAreas(    ) As
                | 
                | Returns or sets the fill twisted areas mode.

        :return:
        """
        return self.hybrid_shape_sweep.FillTwistedAreas

    @fill_twisted_areas.setter
    def fill_twisted_areas(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_sweep.FillTwistedAreas = value 

    @property
    def setback_value(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetbackValue
                | o Property SetbackValue(    ) As
                | 
                | Returns or sets the setback value.

        :return:
        """
        return self.hybrid_shape_sweep.SetbackValue

    @setback_value.setter
    def setback_value(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_sweep.SetbackValue = value 

    def add_cut_points(self, i_element_1, i_element_2):
        """
        .. note::
            CAA V5 Visual Basic help

                | AddCutPoints
                | o Sub AddCutPoints(        iElement1,
                |                            iElement2)
                | 
                | Sets two cut points on the master guide. These points define
                | a zone to be kept on the final swept surface.
                |
                | Parameters:
                | iElement1
                |       First / start cut point.
                |    
                |  iElement2
                |       Second / end cut point.


        :param i_element_1:
        :param i_element_2:
        :return:
        """
        return self.hybrid_shape_sweep.AddCutPoints(i_element_1, i_element_2)

    def add_fill_points(self, i_element_1, i_element_2):
        """
        .. note::
            CAA V5 Visual Basic help

                | AddFillPoints
                | o Sub AddFillPoints(        iElement1,
                |                             iElement2)
                | 
                | Sets two fill points on the master guide. These points
                | define a zone to be filled on the final swept surface.
                |
                | Parameters:
                | iElement1
                |       First / start fill point.
                |    
                |  iElement2
                |       Second / end fill point.


        :param i_element_1:
        :param i_element_2:
        :return:
        """
        return self.hybrid_shape_sweep.AddFillPoints(i_element_1, i_element_2)

    def get_cut_point(self, i_rank):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetCutPoint
                | o Func GetCutPoint(        iRank) As
                | 
                |
                | Parameters:


        :param i_rank:
        :return:
        """
        return self.hybrid_shape_sweep.GetCutPoint(i_rank)

    def get_fill_point(self, i_rank):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetFillPoint
                | o Func GetFillPoint(        iRank) As
                | 
                |
                | Parameters:


        :param i_rank:
        :return:
        """
        return self.hybrid_shape_sweep.GetFillPoint(i_rank)

    def remove_all_cut_points(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | RemoveAllCutPoints
                | o Sub RemoveAllCutPoints(    )
                | 
                | Removes all cut points.
                |
                | Parameters:


        :return:
        """
        return self.hybrid_shape_sweep.RemoveAllCutPoints()

    def remove_all_fill_points(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | RemoveAllFillPoints
                | o Sub RemoveAllFillPoints(    )
                | 
                | Removes all fill points.
                |
                | Parameters:


        :return:
        """
        return self.hybrid_shape_sweep.RemoveAllFillPoints()

    def __repr__(self):
        return f'HybridShapeSweep()'
