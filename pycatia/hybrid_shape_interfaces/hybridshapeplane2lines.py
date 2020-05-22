#! /usr/bin/python3.6
# module initially auto generated using V5Automation.chm from CATIA R25 on 2020-05-22 12:54:36.956119

from pycatia.mec_mod_interfaces.hybridshape import HybridShape


class HybridShapePlane2Lines(HybridShape):
    """
        .. note::
            CAA V5 Visual Basic help

                | plane defined by two lines.Role: Allows to access data of the plane
                | feature passing though two lines.

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_plane2_lines = com_object     

    @property
    def first(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | First
                | o Property First(    ) As
                | 
                | Role: Get the first line.

        :return:
        """
        return self.hybrid_shape_plane2_lines.First

    @property
    def forbid_non_coplanar_lines(self, i_coplanar_lines):
        """
        .. note::
            CAA V5 Visual Basic help

                | ForbidNonCoplanarLines
                | o Property ForbidNonCoplanarLines(        iCoplanarLines)
                | 
                | if ForbidNonCoplanarLines = TRUE, both lines have to be on
                | the same plane. if ForbidNonCoplanarLines = FALSE, both
                | lines can be non coplanar.

        :param i_coplanar_lines:
        :return:
        """
        return self.hybrid_shape_plane2_lines.ForbidNonCoplanarLines

    @property
    def second(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Second
                | o Property Second(    ) As
                | 
                | Role: Get the second line.

        :return:
        """
        return self.hybrid_shape_plane2_lines.Second

    def __repr__(self):
        return f'HybridShapePlane2Lines()'
