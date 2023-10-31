#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.in_interfaces.reference import Reference
from pycatia.knowledge_interfaces.length import Length
from pycatia.system_interfaces.any_object import AnyObject


class Limit(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     Limit
                | 
                | Represents the limit of a prism or a hole shape.
                | 
                | See also:
                |     Prism, Hole
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.limit = com_object

    @property
    def dimension(self) -> Length:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Dimension() As Length (Read Only)
                | 
                |     Returns or sets the limit dimension. This property is valid for the offset
                |     limit mode only, that is when CatLimitMode is set to catOffsetLimit .

        :rtype: Length
        """

        return Length(self.limit.Dimension)

    @property
    def limit_mode(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property LimitMode() As CatLimitMode
                | 
                |     Returns or sets the limit mode.

        :return: enum cat_limit_mode
        :rtype: int
        """

        return self.limit.LimitMode

    @limit_mode.setter
    def limit_mode(self, value: int):
        """
        :param int value: enum cat_limit_mode
        """

        self.limit.LimitMode = value

    @property
    def limiting_element(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property LimitingElement() As Reference
                | 
                |     Returns or sets the limiting element. This property is valid when the
                |     limiting object is a surface or a plane, that is when CatLimitMode is set to
                |     catUpToSurfaceLimit and catUpToPlaneLimit.
                |     To set the property, you can use the following Boundary object: Face.

        :rtype: Reference
        """

        return Reference(self.limit.LimitingElement)

    @limiting_element.setter
    def limiting_element(self, value: Reference):
        """
        :param Reference value:
        """

        self.limit.LimitingElement = value.com_object

    def __repr__(self):
        return f'Limit(name="{self.name}")'
