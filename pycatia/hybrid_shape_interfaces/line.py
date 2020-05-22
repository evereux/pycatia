#! /usr/bin/python3.6
# module initially auto generated using V5Automation.chm from CATIA R25 on 2020-05-22 12:54:36.956119

from pycatia.mec_mod_interfaces.hybridshape import HybridShape


class Line(HybridShape):
    """
        .. note::
            CAA V5 Visual Basic help

                | Represents the hybrid shape Line feature object.Role: Declare  hybrid
                | shape Line root feature object.  All interfaces for different type of
                | Line derivates HybridShapeLine.Use the CATIAHybridShapeFactory to
                | create a HybridShapeLine objects.

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.line = com_object     

    @property
    def first_upto_elem(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | FirstUptoElem
                | o Property FirstUptoElem(    ) As
                | 
                | Role: Gets the First upto element of the line.

        :return:
        """
        return self.line.FirstUptoElem

    @property
    def second_upto_elem(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | SecondUptoElem
                | o Property SecondUptoElem(    ) As
                | 
                | Role: Gets the Second upto element of the line.

        :return:
        """
        return self.line.SecondUptoElem

    def get_direction(self, o_direction):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetDirection
                | o Sub GetDirection(        oDirection)
                | 
                | Role: Returns the unit-vector pointing in the direction of
                | the line.
                |
                | Parameters:
                | oDirection
                |  
                |  oDirection[0]
                |    The X Coordinate of the unit vector pointing in the
                |    direction of the line
                |    
                |  oDirection[1]
                |    The Y Coordinate of the unit vector pointing in the
                |    direction of the line
                |    
                |  oDirection[2]
                |    The Z Coordinate of the unit vector pointing in the
                |    direction of the line
                |  
                | 
                |  Returns:
                |   HRESULT    S_OK   if Ok 
                |    E_FAIL else 
                |    return error code for C++ Implementations
                |  
                |    See also:


        :param o_direction:
        :return:
        """
        return self.line.GetDirection(o_direction)

    def get_origin(self, o_origin):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetOrigin
                | o Sub GetOrigin(        oOrigin)
                | 
                | Role: Returns the origin of the line.
                |
                | Parameters:
                | oOrigin
                |  
                |  oOrigin[0]
                |    The X Coordinate of a point lying on the line
                |    
                |  oOrigin[1]
                |    The Y Coordinate of a point lying on the line
                |    
                |  oOrigin[2]
                |    The Z Coordinate of a point lying on the line
                |    The Origin is evaluated from the geometry of the line.
                |  
                | 
                |  Returns:
                |   HRESULT    S_OK   if Ok 
                |    E_FAIL else 
                |    return error code for C++ Implementations
                |  
                |    See also:


        :param o_origin:
        :return:
        """
        return self.line.GetOrigin(o_origin)

    def put_direction(self, i_direction):
        """
        .. note::
            CAA V5 Visual Basic help

                | PutDirection
                | o Sub PutDirection(        iDirection)
                | 
                | Role: Sets the unit-vector pointing in the direction of the
                | line.
                |
                | Parameters:
                | iDirection
                |  
                |  iDirection[0]
                |    The X Coordinate of the unit vector pointing in the
                |    direction of the line
                |    
                |  iDirection[1]
                |    The Y Coordinate of the unit vector pointing in the
                |    direction of the line
                |    
                |  iDirection[2]
                |    The Z Coordinate of the unit vector pointing in the
                |    direction of the line
                |  
                | 
                |  Returns:
                |   HRESULT    S_OK   if Ok 
                |    E_FAIL else 
                |    return error code for C++ Implementations
                |  
                |    See also:


        :param i_direction:
        :return:
        """
        return self.line.PutDirection(i_direction)

    def __repr__(self):
        return f'Line()'
