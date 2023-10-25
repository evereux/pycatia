#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.knowledge_interfaces.parameter import Parameter
from pycatia.structure_interfaces.str_anchor_points import StrAnchorPoints
from pycatia.system_interfaces.any_object import AnyObject


class StrSection(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     StrSection
                | 
                | Represents the section object.
                | The section object is created from a part document in which a sketch has to be
                | defined.
                | The sketch object may contain one or several contour but all of them have to be
                | closed.
                | Predefined anchor points objects are calculated from the geometrical contour as
                | the top bottom point, the center gravity point, etc.
                | User anchor points can be created in the sketch using the parametric geometry
                | or not. However the names of these points have to prefixed by the string "Str"
                | to be recognized as structure anchor points.
                | Some attributes are defined on the section object but cannot be
                | modified.
                | A group of attributes defines the section name, the family name, and the the
                | name of the catalog where the section comes from.
                | Another attribute called the profile type defines the type of the parametric
                | contour used to create the section. The contour can be a Tee, an angle, a
                | channel, a square tube, and so on. These predefined contours are useful to
                | create a new catalog with some standard contours.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.str_section = com_object

    @property
    def catalog_name(self) -> Parameter:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property CatalogName() As Parameter (Read Only)
                | 
                |     Returns the parameter defining the catalog name.
                | 
                |     Example:
                | 
                |           
                | 
                |          Dim name As Parameter
                |          Set name = Section_1.CatalogName

        :rtype: Parameter
        """

        return Parameter(self.str_section.CatalogName)

    @property
    def family_name(self) -> Parameter:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property FamilyName() As Parameter (Read Only)
                | 
                |     Returns the parameter defining the family name.
                | 
                |     Example:
                | 
                |           
                | 
                |          Dim name As Parameter
                |          Set name = Section_1.FamilyName

        :rtype: Parameter
        """

        return Parameter(self.str_section.FamilyName)

    @property
    def profile_type(self) -> Parameter:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ProfileType() As Parameter (Read Only)
                | 
                |     Returns the parameter defining the profile type of the
                |     section.
                | 
                |     Example:
                | 
                |           
                | 
                |          Dim type As Parameter
                |          Set type = Section_1.ProfileType

        :rtype: Parameter
        """

        return Parameter(self.str_section.ProfileType)

    @property
    def section_name(self) -> Parameter:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property SectionName() As Parameter (Read Only)
                | 
                |     Returns the parameter defining the section name.
                | 
                |     Example:
                | 
                |           
                | 
                |          Dim name As Parameter
                |          Set name = Section_1.SectionName

        :rtype: Parameter
        """

        return Parameter(self.str_section.SectionName)

    @property
    def str_anchor_points(self) -> StrAnchorPoints:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property StrAnchorPoints() As StrAnchorPoints (Read Only)
                | 
                |     Returns the collection of anchor points.
                | 
                |      
                | 
                | 
                |       
                |      Example: 
                |      
                |       
                |          
                | 
                |           Dim anchorPts As StrAnchorPoints
                |          Set anchorPts = Section_1.StrAnchorPoints

        :rtype: StrAnchorPoints
        """

        return StrAnchorPoints(self.str_section.StrAnchorPoints)

    def get_property(self, i_property: int, o_value: float) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetProperty(CATStrSectionProperties iProperty,
                | double oValue)
                | 
                |     Get a property value.
                | 
                |     Example:
                | 
                |           
                | 
                |          Dim type As Parameter
                |          Set type = Section_1.GetProperty(CatStrArea)

        :param int i_property: enum cat_str_section_properties
        :param float o_value:
        :rtype: None
        """
        return self.str_section.GetProperty(i_property, o_value)

    def __repr__(self):
        return f'StrSection(name="{self.name}")'
