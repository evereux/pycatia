#! /usr/bin/python3.6
# module initially auto generated using V5Automation.chm from CATIA R25 on 2020-05-22 12:54:36.956119

from pycatia.mec_mod_interfaces.hybridshape import HybridShape


class HybridShapeSection(HybridShape):
    """
        .. note::
            CAA V5 Visual Basic help

                | Interface to hybrid shape section feature.Role: Allows you to access
                | data of the Hybrid Shape Section feature.

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_section = com_object     

    @property
    def section_plane(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | SectionPlane
                | o Property SectionPlane(    ) As
                | 
                | Returns or sets the section plane..
                | Examples:
                | This example retrieves in RefPlane the plane of the section
                | Dim RefPlane As Reference Set RefPlane =
                | HybridShapeSection.SectionPlane

        :return:
        """
        return self.hybrid_shape_section.SectionPlane

    @section_plane.setter
    def section_plane(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_section.SectionPlane = value 

    def __repr__(self):
        return f'HybridShapeSection()'
