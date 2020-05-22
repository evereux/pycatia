#! /usr/bin/python3.6
# module initially auto generated using V5Automation.chm from CATIA R25 on 2020-05-22 12:54:36.956119

from pycatia.mec_mod_interfaces.hybridshape import HybridShape


class HybridShapeFilletTriTangent(HybridShape):
    """
        .. note::
            CAA V5 Visual Basic help

                | Fillet Tri-Tangent feature.Role: Manipulation of Fillet Tri-Tangent
                | feature Allows to access data of the Fillet Tri-Tangent feature
                | created by using three support surfaces, their orientation, and
                | options (supports trimming and fillet extremities type)

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_fillet_tri_tangent = com_object     

    @property
    def first_elem(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | FirstElem
                | o Property FirstElem(    ) As
                | 
                | Returns or sets the first support surface feature. Example:
                | This example retrieves in FirstElem the first support
                | element used by the HybShpFilletTriTangent hybrid shape
                | feature. Dim FirstElem As Reference Set FirstElem =
                | HybShpFilletTriTangent.FirstElem

        :return:
        """
        return self.hybrid_shape_fillet_tri_tangent.FirstElem

    @first_elem.setter
    def first_elem(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_fillet_tri_tangent.FirstElem = value 

    @property
    def first_orientation(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | FirstOrientation
                | o Property FirstOrientation(    ) As
                | 
                | Returns or sets the first orientation used to specify fillet
                | center position. Note; Orientation is same or inverse than
                | the normal to the first surface support

        :return:
        """
        return self.hybrid_shape_fillet_tri_tangent.FirstOrientation

    @first_orientation.setter
    def first_orientation(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_fillet_tri_tangent.FirstOrientation = value 

    @property
    def remove_elem(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | RemoveElem
                | o Property RemoveElem(    ) As
                | 
                | Returns or sets the support surface to remove feature.

        :return:
        """
        return self.hybrid_shape_fillet_tri_tangent.RemoveElem

    @remove_elem.setter
    def remove_elem(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_fillet_tri_tangent.RemoveElem = value 

    @property
    def remove_orientation(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | RemoveOrientation
                | o Property RemoveOrientation(    ) As
                | 
                | Returns or sets the third orientation used to specify fillet
                | center position. note: Orientation is same or inverse than
                | the normal to the surface support to remove

        :return:
        """
        return self.hybrid_shape_fillet_tri_tangent.RemoveOrientation

    @remove_orientation.setter
    def remove_orientation(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_fillet_tri_tangent.RemoveOrientation = value 

    @property
    def ribbon_relimitation_mode(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | RibbonRelimitationMode
                | o Property RibbonRelimitationMode(    ) As
                | 
                | Returns or sets fillet ribbon relimitation mode (or fillet
                | extremities mode). note: Smooth(0) or Straight(1) or
                | Maximum(2) or Minimum(3)

        :return:
        """
        return self.hybrid_shape_fillet_tri_tangent.RibbonRelimitationMode

    @ribbon_relimitation_mode.setter
    def ribbon_relimitation_mode(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_fillet_tri_tangent.RibbonRelimitationMode = value 

    @property
    def second_elem(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | SecondElem
                | o Property SecondElem(    ) As
                | 
                | Returns or sets the Second support surface feature. Example:
                | This example retrieves in SecondElem the Second support
                | element used by the HybShpFilletTriTangent hybrid shape
                | feature. Dim SecondElem As Reference Set SecondElem =
                | HybShpFilletTriTangent.SecondElem

        :return:
        """
        return self.hybrid_shape_fillet_tri_tangent.SecondElem

    @second_elem.setter
    def second_elem(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_fillet_tri_tangent.SecondElem = value 

    @property
    def second_orientation(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | SecondOrientation
                | o Property SecondOrientation(    ) As
                | 
                | Returns or sets the Second orientation used to specify
                | fillet center position. note: Orientation is same or inverse
                | than the normal to the Second surface support

        :return:
        """
        return self.hybrid_shape_fillet_tri_tangent.SecondOrientation

    @second_orientation.setter
    def second_orientation(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_fillet_tri_tangent.SecondOrientation = value 

    @property
    def supports_trim_mode(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | SupportsTrimMode
                | o Property SupportsTrimMode(    ) As
                | 
                | Returns or sets whether support surfaces are trimmed or not.
                | Trim (1) or NoTrim(0) note: if "Trim" the 2 supports are
                | trimmed and assembled with the fillet ribbon.

        :return:
        """
        return self.hybrid_shape_fillet_tri_tangent.SupportsTrimMode

    @supports_trim_mode.setter
    def supports_trim_mode(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_fillet_tri_tangent.SupportsTrimMode = value 

    def invert_first_orientation(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | InvertFirstOrientation
                | o Sub InvertFirstOrientation(    )
                | 
                | Inverts first orientation used to specify fillet center
                | position.
                |
                | Parameters:


        :return:
        """
        return self.hybrid_shape_fillet_tri_tangent.InvertFirstOrientation()

    def invert_remove_orientation(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | InvertRemoveOrientation
                | o Sub InvertRemoveOrientation(    )
                | 
                | Inverts third orientation used to specify fillet center
                | position.
                |
                | Parameters:


        :return:
        """
        return self.hybrid_shape_fillet_tri_tangent.InvertRemoveOrientation()

    def invert_second_orientation(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | InvertSecondOrientation
                | o Sub InvertSecondOrientation(    )
                | 
                | Inverts second orientation used to specify fillet center
                | position.
                |
                | Parameters:


        :return:
        """
        return self.hybrid_shape_fillet_tri_tangent.InvertSecondOrientation()

    def __repr__(self):
        return f'HybridShapeFilletTriTangent()'
