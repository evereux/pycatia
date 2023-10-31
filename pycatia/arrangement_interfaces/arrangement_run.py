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


class ArrangementRun(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     ArrangementRun
                | 
                | Use this object to access the properties and methods of an ArrangementRun
                | object.
                | Role: Use this interface to control the visualization mode, section parameters,
                | nodes that define the ArrangementRun object.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.arrangement_run = com_object

    @property
    def arrangement_nodes(self) -> ArrangementNodes:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ArrangementNodes() As ArrangementNodes (Read Only)
                | 
                |     Returns the ArrangementNodes that make up the
                |     ArrangementRun.
                | 
                |     Example:
                |         This example gets the ArrangementNodes for the objRun1
                |         object.
                | 
                |          Dim objArrNodes   As ArrangementNodes
                |          Set objArrNodes = objRun1.ArrangementNodes

        :rtype: ArrangementNodes
        """

        return ArrangementNodes(self.arrangement_run.ArrangementNodes)

    @property
    def length(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Length() As double (Read Only)
                | 
                |     Returns the length of the ArrangementRun object.
                | 
                |     Example:
                |         This example retrieves the Length of the objRun1
                |         object.
                | 
                |          Dim dblLength   As Double
                |          dblLength  = objRun1.Length

        :rtype: float
        """

        return self.arrangement_run.Length

    @property
    def section_diameter(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property SectionDiameter() As double
                | 
                |     Returns or sets the SectionDiameter for an ArrangementRun
                |     object.
                | 
                |     Example:
                |         This example retrieves the SectionDiameter for the objRun1
                |         object.
                | 
                |          Dim dblSectionDia   As Double
                |          dblSectionDia = objRun1.SectionDiameter

        :rtype: float
        """

        return self.arrangement_run.SectionDiameter

    @section_diameter.setter
    def section_diameter(self, value: float):
        """
        :param float value:
        """

        self.arrangement_run.SectionDiameter = value

    @property
    def section_height(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property SectionHeight() As double
                | 
                |     Returns or sets the SectionHeight for an ArrangementRun
                |     object.
                | 
                |     Example:
                |         This example gets the SectionHeight for the objRun1
                |         object.
                | 
                |          Dim dblSectionHeight   As Double
                |          dblSectionHeight = objRun1.SectionHeight

        :rtype: float
        """

        return self.arrangement_run.SectionHeight

    @section_height.setter
    def section_height(self, value: float):
        """
        :param float value:
        """

        self.arrangement_run.SectionHeight = value

    @property
    def section_type(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property SectionType() As CATArrangementRouteSection
                | 
                |     Returns or sets the SectionType for an ArrangementRun
                |     object.
                | 
                |     Example:
                |         This example sets the SectionType for the objRun1 object to
                |         CatArrangementRouteSectionRectangular.
                | 
                |          objRun1.SectionType = CatArrangementRouteSectionRectangular

        :rtype: int
        """

        return self.arrangement_run.SectionType

    @section_type.setter
    def section_type(self, value: int):
        """
        :param int value:
        """

        self.arrangement_run.SectionType = value

    @property
    def section_width(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property SectionWidth() As double
                | 
                |     Returns or sets the SectionWidth for an ArrangementRun
                |     object.
                | 
                |     Example:
                |         This example gets the SectionWidth for the objRun1
                |         object.
                | 
                |          Dim dblSectionWidth   As Double
                |          dblSectionWidth = objRun1.SectionWidth

        :rtype: float
        """

        return self.arrangement_run.SectionWidth

    @section_width.setter
    def section_width(self, value: float):
        """
        :param float value:
        """

        self.arrangement_run.SectionWidth = value

    @property
    def visu_mode(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property VisuMode() As CATArrangementRouteVisuMode
                | 
                |     Returns or sets the Visualization Mode for an ArrangementRun
                |     object.
                | 
                |     Example:
                |         This example sets the Visualization Mode for the objRun1 object to
                |         CatArrangementRouteVisuModeSolid.
                | 
                |          objRun1.VisuMode = CatArrangementRouteVisuModeSolid

        :return: enum cat_arrangement_route_visu_mode
        :rtype: int
        """

        return self.arrangement_run.VisuMode

    @visu_mode.setter
    def visu_mode(self, value: int):
        """
        :param int value: enum cat_arrangement_route_visu_mode
        """

        self.arrangement_run.VisuMode = value

    def get_technological_object(self, i_application_type: str) -> AnyObject:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetTechnologicalObject(CATBSTR iApplicationType) As
                | CATBaseDispatch
                | 
                |     Returns the applicative data which type is the given
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
                |                 objRun1 object.
                | 
                |                  Dim objProd   As Product
                |                  objProd  = objRun1.GetTechnologicalObject("Product")

        :param str i_application_type:
        :rtype: AnyObject
        """
        return self.arrangement_run.GetTechnologicalObject(i_application_type)

    def __repr__(self):
        return f'ArrangementRun(name="{self.name}")'
