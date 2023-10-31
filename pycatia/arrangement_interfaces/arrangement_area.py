#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.arrangement_interfaces.arrangement_contours import ArrangementContours
from pycatia.system_interfaces.any_object import AnyObject


class ArrangementArea(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     ArrangementArea
                | 
                | Use this object to access an ArrangementArea object's properties and
                | functions.
                | Role: The ArrangementArea object is a type of Arrangement Object defining an
                | area containing other objects.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.arrangement_area = com_object

    @property
    def arrangement_contours(self) -> ArrangementContours:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ArrangementContours() As ArrangementContours (Read
                | Only)
                | 
                |     Returns the ArrangementContours collection object associated with an
                |     ArrangementArea object.
                | 
                |     Example:
                |         This example retrieves the ArrangementContours collection object for
                |         the objArea1 object.
                | 
                |          Dim objArrContours   As ArrangementContours
                |          Set objArrContours  = objArea1.ArrangementContours

        :rtype: ArrangementContours
        """

        return ArrangementContours(self.arrangement_area.ArrangementContours)

    @property
    def height(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Height() As double
                | 
                |     Returns or sets the Height of an ArrangementArea object.
                | 
                |     Example:
                |         This example retrieves the Height for the objArea1
                |         object.
                | 
                |          Dim dblAreaHeight   As Double
                |          dblAreaHeight  = objArea1.Height

        :rtype: float
        """

        return self.arrangement_area.Height

    @height.setter
    def height(self, value: float):
        """
        :param float value:
        """

        self.arrangement_area.Height = value

    @property
    def size(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Size() As double (Read Only)
                | 
                |     Returns the Size of the ArrangementArea.
                | 
                |     Example:
                |         This example retrieves the Size of the objArea1
                |         object.
                | 
                |          Dim dblAreaSize   As Double
                |          dblAreaSize  = objArea1.Size

        :rtype: float
        """

        return self.arrangement_area.Size

    @property
    def visu_mode(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property VisuMode() As CATArrangementAreaVisuMode
                | 
                |     Returns or sets the Visualization Mode for an ArrangementArea
                |     object.
                | 
                |     Example:
                |         This example sets the Visualization Mode for the objArea1 object to
                |         CatArrangementAreaVisuModeVolume.
                | 
                |          objArea1.VisuMode = CatArrangementAreaVisuModeVolume

        :return: enum cat_arrangement_area_visu_mode
        :rtype: int
        """

        return self.arrangement_area.VisuMode

    @visu_mode.setter
    def visu_mode(self, value: int):
        """
        :param int value: enum cat_arrangement_area_visu_mode
        """

        self.arrangement_area.VisuMode = value

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
                | 
                |     Returns:
                |         oApplicativeObj The matched applicative object.
                | 
                |         Example:
                |             This example retrieves the desired applicative object from the
                |             objArea1 object.
                | 
                |              Dim objProd   As Product
                |              objProd  = objArea1.GetTechnologicalObject("Product")

        :param str i_application_type:
        :rtype: AnyObject
        """
        return self.arrangement_area.GetTechnologicalObject(i_application_type)

    def __repr__(self):
        return f'ArrangementArea(name="{self.name}")'
