#! /usr/bin/python3.6
# module initially auto generated using V5Automation.chm from CATIA R25 on 2020-05-22 12:54:36.956119

from pycatia.mec_mod_interfaces.hybridshape import HybridShape


class HybridShapeMidSurface(HybridShape):
    """
        .. note::
            CAA V5 Visual Basic help

                | Represents the hybrid shape MidSurface feature object.Role: To access
                | the data of the hybrid shape MidSurface feature object.This data
                | includes:Use the  CATIAHybridShapeFactory to create a
                | HybridShapeMidSurface object.

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_mid_surface = com_object     

    @property
    def creation_mode(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | CreationMode
                | o Property CreationMode(    ) As
                | 
                | Returns or sets CreationMode. Face Pairs : 0, Faces To
                | Offset : 1, Automatic : 2 (Only Automatic Creation Mode
                | Available for Automation)

        :return:
        """
        return self.hybrid_shape_mid_surface.CreationMode

    @creation_mode.setter
    def creation_mode(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_mid_surface.CreationMode = value 

    @property
    def support(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Support
                | o Property Support(    ) As
                | 
                | Returns or sets Support Body. .

        :return:
        """
        return self.hybrid_shape_mid_surface.Support

    @support.setter
    def support(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_mid_surface.Support = value 

    @property
    def threshold(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Threshold
                | o Property Threshold(    ) As
                | 
                | Returns or sets Threshold Thickness. .

        :return:
        """
        return self.hybrid_shape_mid_surface.Threshold

    @threshold.setter
    def threshold(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_mid_surface.Threshold = value 

    def __repr__(self):
        return f'HybridShapeMidSurface()'
