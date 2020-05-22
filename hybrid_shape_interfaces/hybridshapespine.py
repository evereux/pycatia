#! /usr/bin/python3.6
# module initially auto generated using V5Automation.chm from CATIA R25 on 2020-05-22 12:54:36.956119

from pycatia.mec_mod_interfaces.hybridshape import HybridShape


class HybridShapeSpine(HybridShape):
    """
        .. note::
            CAA V5 Visual Basic help

                | Represents the hybrid spine curve feature object.Role:Use the
                | CATIAHybridShapeFactory to create a HybridShapeSpine object.

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_spine = com_object     

    @property
    def orientation(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Orientation
                | o Property Orientation(    ) As
                | 
                | Gets or Sets the orientation. Orientation by reference with
                | the normal to the first section/plane

        :return:
        """
        return self.hybrid_shape_spine.Orientation

    @property
    def start_point(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | StartPoint
                | o Property StartPoint(    ) As
                | 
                | Retuns or sets the start point of the spine.

        :return:
        """
        return self.hybrid_shape_spine.StartPoint

    def add_guide(self, i_guide):
        """
        .. note::
            CAA V5 Visual Basic help

                | AddGuide
                | o Sub AddGuide(        iGuide)
                | 
                | Adds a guide to the spine curve.
                |
                | Parameters:
                | iGuide
                |      The guide curve to be added


        :param i_guide:
        :return:
        """
        return self.hybrid_shape_spine.AddGuide(i_guide)

    def add_section(self, i_section):
        """
        .. note::
            CAA V5 Visual Basic help

                | AddSection
                | o Sub AddSection(        iSection)
                | 
                | Adds a section or a plane to the spine curve.
                |
                | Parameters:
                | iSection
                |      The section curve or plane to be added
                | Sub-element(s) supported (see 
                | 
                |  object):  
                | .


        :param i_section:
        :return:
        """
        return self.hybrid_shape_spine.AddSection(i_section)

    def get_guide(self, i_idx, op_ia_guide):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetGuide
                | o Sub GetGuide(        iIdx,
                |                        opIAGuide)
                | 
                | Retrieves a guide .
                |
                | Parameters:
                | iIdx
                |     The index of the guide
                |  
                |  opIAGuide
                |     The guide retrieved


        :param i_idx:
        :param op_ia_guide:
        :return:
        """
        return self.hybrid_shape_spine.GetGuide(i_idx, op_ia_guide)

    def get_number_of_guides(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetNumberOfGuides
                | o Func GetNumberOfGuides(    ) As
                | 
                | Retrieves number of guides in a spine curve.
                |
                | Parameters:
                | oNbGuides
                |     Number of guides in a spine curve


        :return:
        """
        return self.hybrid_shape_spine.GetNumberOfGuides()

    def get_number_of_sections(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetNumberOfSections
                | o Func GetNumberOfSections(    ) As
                | 
                | Retrieves number of sections in a spine curve.
                |
                | Parameters:
                | oNbSections
                |     Number of sections in a spine curve


        :return:
        """
        return self.hybrid_shape_spine.GetNumberOfSections()

    def get_section(self, i_idx, o_section):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetSection
                | o Sub GetSection(        iIdx,
                |                          oSection)
                | 
                | Retrieves a section or a plane.
                |
                | Parameters:
                | iIdx
                |     The index of the section
                |  
                |  oSection
                |     The section retrieved


        :param i_idx:
        :param o_section:
        :return:
        """
        return self.hybrid_shape_spine.GetSection(i_idx, o_section)

    def modify_guide_curve(self, ip_ia_guide, ip_ia_new_guide):
        """
        .. note::
            CAA V5 Visual Basic help

                | ModifyGuideCurve
                | o Sub ModifyGuideCurve(        ipIAGuide,
                |                                ipIANewGuide)
                | 
                | Modifies a guide from the spine curve.
                |
                | Parameters:
                | ipIAGuide
                |     The guide curve to be replaced.
                |  
                |  ipIANewGuide
                |     The new guide curve or plane which replaces the old one.


        :param ip_ia_guide:
        :param ip_ia_new_guide:
        :return:
        """
        return self.hybrid_shape_spine.ModifyGuideCurve(ip_ia_guide, ip_ia_new_guide)

    def modify_section_curve(self, ip_ia_section, ip_ia_new_section):
        """
        .. note::
            CAA V5 Visual Basic help

                | ModifySectionCurve
                | o Sub ModifySectionCurve(        ipIASection,
                |                                  ipIANewSection)
                | 
                | Modifies a section or a plane from the spine curve.
                |
                | Parameters:
                | ipIASection
                |     The section curve or plane to be replaced.
                |  
                |  ipIANewSection
                |     The new section curve or plane which replaces the old one.


        :param ip_ia_section:
        :param ip_ia_new_section:
        :return:
        """
        return self.hybrid_shape_spine.ModifySectionCurve(ip_ia_section, ip_ia_new_section)

    def remove_guide(self, i_guide):
        """
        .. note::
            CAA V5 Visual Basic help

                | RemoveGuide
                | o Sub RemoveGuide(        iGuide)
                | 
                | Removes a guide from the spine curve.
                |
                | Parameters:
                | iGuide
                |       The guide curve to be removed.


        :param i_guide:
        :return:
        """
        return self.hybrid_shape_spine.RemoveGuide(i_guide)

    def remove_section(self, i_section):
        """
        .. note::
            CAA V5 Visual Basic help

                | RemoveSection
                | o Sub RemoveSection(        iSection)
                | 
                | Removes a section or a plane from the spine curve.
                |
                | Parameters:
                | iSection
                |     The section curve or plane to be removed.
                |  Sub-element(s) supported (see 
                | 
                |  object):  
                | .


        :param i_section:
        :return:
        """
        return self.hybrid_shape_spine.RemoveSection(i_section)

    def set_start_point(self, i_point):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetStartPoint
                | o Sub SetStartPoint(        iPoint)
                | 
                | Sets the start point of the spine curve.
                |
                | Parameters:
                | iPoint
                |       The point to be set as the spine curve start point.
                |  Sub-element(s) supported (see 
                | 
                |  object):  
                | .


        :param i_point:
        :return:
        """
        return self.hybrid_shape_spine.SetStartPoint(i_point)

    def __repr__(self):
        return f'HybridShapeSpine()'
