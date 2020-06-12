#! usr/bin/python3.6
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.in_interfaces.reference import Reference
from pycatia.mec_mod_interfaces.hybrid_shape import HybridShape


class HybridShapeSection(HybridShape):

    """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.HybridShape
                |                         HybridShapeSection
                | 
                | Interface to hybrid shape section feature.
                | Role: Allows you to access data of the Hybrid Shape Section
                | feature.
                | 
                | See also:
                |     HybridShapeFactory.AddNewSection
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_section = com_object

    @property
    def section_plane(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property SectionPlane() As Reference
                | 
                |     Returns or sets the section plane..
                | 
                |     Parameters:
                | 
                |         oPlane
                |             The section oPlane
                | 
                |             Example:
                |                 This example retrieves in RefPlane the plane of the
                |                 section
                | 
                |                  Dim RefPlane As Reference 
                |                  Set RefPlane = HybridShapeSection.SectionPlane

        :return: Reference
        """

        return Reference(self.hybrid_shape_section.SectionPlane)

    @section_plane.setter
    def section_plane(self, value):
        """
        :param Reference value:
        """

        self.hybrid_shape_section.SectionPlane = value

    def __repr__(self):
        return f'HybridShapeSection(name="{ self.name }")'
