#! /usr/bin/python3.6
# module initially auto generated using V5Automation.chm from CATIA V5 R25

from pycatia.system_interfaces.base_object import AnyObject


class GeometricElement(AnyObject):
    """
        .. note::
            CAA V5 Visual Basic help

                | 2D or 3D wireframe geometric element.

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.geometric_element = com_object

    @property
    def geometric_type(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | GeometricType
                | o Property GeometricType(    ) As CatGeometricType
                | 
                | Returns the type of the underlying geometrical element


                | Parameters:
                | oType
                |        Specific type of the geometric interface

        :return: int

        """
        return self.geometric_element.GeometricType

    def __repr__(self):
        return f'GeometricElement({self.name()})'
