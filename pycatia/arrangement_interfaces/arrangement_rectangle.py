#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.any_object import AnyObject


class ArrangementRectangle(AnyObject):

    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     ArrangementRectangle
                | 
                | Use this object to access the properties and methods of an ArrangementRectangle
                | object.
                | Role: The ArrangementRectangle object is a geometric shape used for defining
                | Contours of Areas. The ArrangementRectangle is defined by width and length and
                | its Product position (which is the min-x, min-y corner of the
                | rectangle).
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.arrangement_rectangle = com_object

    @property
    def x_length(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property XLength() As double
                | 
                |     Returns or sets the XLength of the ArrangementRectangle.
                | 
                |     Example:
                |         This example retrieves the XLength for the objRectangle1
                |         object.
                | 
                |          Dim dblXLength  As Double
                |          dblXLength = objRectangle1.XLength

        :rtype: float
        """

        return self.arrangement_rectangle.XLength

    @x_length.setter
    def x_length(self, value: float):
        """
        :param float value:
        """

        self.arrangement_rectangle.XLength = value

    @property
    def y_length(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property YLength() As double
                | 
                |     Returns or sets the YLength of the ArrangementRectangle.
                | 
                |     Example:
                |         This example retrieves the YLength for the objRectangle1
                |         object.
                | 
                |          Dim dblYLength  As Double
                |          dblYLength = objRectangle1.YLength

        :rtype: float
        """

        return self.arrangement_rectangle.YLength

    @y_length.setter
    def y_length(self, value: float):
        """
        :param float value:
        """

        self.arrangement_rectangle.YLength = value

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
                |                 objRectangle1 object.
                | 
                |                  Dim objProd   As Product
                |                  objProd  = objRectangle1.GetTechnologicalObject("Product")

        :param str i_application_type:
        :rtype: AnyObject
        """
        return self.arrangement_rectangle.GetTechnologicalObject(i_application_type)

    def __repr__(self):
        return f'ArrangementRectangle(name="{ self.name }")'
