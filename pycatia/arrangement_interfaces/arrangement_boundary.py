#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.arrangement_interfaces.arrangement_nodes import ArrangementNodes
from pycatia.system_interfaces.any_object import AnyObject


class ArrangementBoundary(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     ArrangementBoundary
                | 
                | Access properties and functions of an ArrangementBoundary
                | object.
                | Role: Use this interface to control the visualization mode, section parameters,
                | nodes that define the ArrangementBoundary object.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.arrangement_boundary = com_object

    @property
    def arrangement_nodes(self) -> ArrangementNodes:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ArrangementNodes() As ArrangementNodes (Read Only)
                | 
                |     Returns the collection of ArrangementNodes that make up the
                |     ArrangementBoundary.
                | 
                |     Example:
                |         This example gets the ArrangementNodes for the objBoundary1
                |         object.
                | 
                |          Dim objArrNodes   As ArrangementNodes
                |          Set objArrNodes = objBoundary1.ArrangementNodes

        :rtype: ArrangementNodes
        """

        return ArrangementNodes(self.arrangement_boundary.ArrangementNodes)

    @property
    def length(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Length() As double (Read Only)
                | 
                |     Returns the length of the ArrangementBoundary object.
                | 
                |     Example:
                |         This example retrieves the Length of the objBoundary1
                |         object.
                | 
                |          Dim dblBoundaryLength   As Double
                |          dblBoundaryLength  = objBoundary1.Length

        :rtype: float
        """

        return self.arrangement_boundary.Length

    @property
    def section_height(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property SectionHeight() As double
                | 
                |     Returns or sets the SectionHeight for an ArrangementBoundary
                |     object.
                | 
                |     Example:
                |         This example gets the SectionHeight for the objBoundary1
                |         object.
                | 
                |          Dim dblSectionHeight   As Double
                |          dblSectionHeight = objBoundary1.SectionHeight

        :rtype: float
        """

        return self.arrangement_boundary.SectionHeight

    @section_height.setter
    def section_height(self, value: float):
        """
        :param float value:
        """

        self.arrangement_boundary.SectionHeight = value

    @property
    def section_type(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property SectionType() As CATArrangementRouteSection
                | 
                |     Returns or sets the SectionType for an ArrangementBoundary
                |     object.
                |     Legal values:
                | 
                |     CatArrangementRouteSectionNone
                |     CatArrangementRouteSectionRectangular
                | 
                |     Example:
                |         This example sets the SectionType for the objBoundary1 object to
                |         CatArrangementRouteSectionRectangular.
                | 
                |          objBoundary1.SectionType = CatArrangementRouteSectionRectangular

        :return: enum cat_arrangement_route_section
        :rtype: int
        """

        return self.arrangement_boundary.SectionType

    @section_type.setter
    def section_type(self, value: int):
        """
        :param int value: enum cat_arrangement_route_section
        """

        self.arrangement_boundary.SectionType = value

    @property
    def section_width(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property SectionWidth() As double
                | 
                |     Returns or sets the SectionWidth for an ArrangementBoundary
                |     object.
                | 
                |     Example:
                |         This example gets the SectionWidth for the objBoundary1
                |         object.
                | 
                |          Dim dblSectionWidth   As Double
                |          dblSectionWidth = objBoundary1.SectionWidth

        :rtype: float
        """

        return self.arrangement_boundary.SectionWidth

    @section_width.setter
    def section_width(self, value: float):
        """
        :param float value:
        """

        self.arrangement_boundary.SectionWidth = value

    @property
    def visu_mode(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property VisuMode() As CATArrangementRouteVisuMode
                | 
                |     Returns or sets the Visualization Mode for an ArrangementBoundary
                |     object.
                | 
                |     Example:
                |         This example sets the Visualization Mode for the objBoundary1 object to
                |         CatArrangementRouteVisuModeSolid.
                | 
                |          objBoundary1.VisuMode = CatArrangementRouteVisuModeSolid

        :return: enum cat_arrangement_route_visu_mode
        :rtype: int
        """

        return self.arrangement_boundary.VisuMode

    @visu_mode.setter
    def visu_mode(self, value: int):
        """
        :param int value: enum cat_arrangement_route_visu_mode
        """

        self.arrangement_boundary.VisuMode = value

    def get_technological_object(self, i_application_type: str) -> AnyObject:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetTechnologicalObject(CATBSTR iApplicationType) As
                | CATBaseDispatch
                | 
                |     Returns the applicative data whose type is the given
                |     parameter.
                | 
                |     Parameters:
                | 
                |         iApplicationType
                |             The type of applicative data searched. 
                |         oApplicativeObj
                |             The matched applicative object.
                | 
                |             Example:
                |                 This example retrieves the desired applicative object from the
                |                 objBoundary1 object.
                | 
                |                  Dim objProd   As Product
                |                  objProd  = objBoundary1.GetTechnologicalObject("Product")

        :param str i_application_type:
        :rtype: AnyObject
        """
        return self.arrangement_boundary.GetTechnologicalObject(i_application_type)

    def __repr__(self):
        return f'ArrangementBoundary(name="{self.name}")'
