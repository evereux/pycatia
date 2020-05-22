#! /usr/bin/python3.6
# module initially auto generated using V5Automation.chm from CATIA R25 on 2020-05-22 12:54:36.956119

from pycatia.mec_mod_interfaces.hybridshape import HybridShape


class Plane(HybridShape):
    """
        .. note::
            CAA V5 Visual Basic help

                | Represents the hybrid shape Plane feature object.Role: Declare  hybrid
                | shape Plane root feature object.  All interfaces for different type of
                | Plane derivates HybridShapePlane.Use the CATIAHybridShapeFactory to
                | create a HybridShapePlane objects.

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.plane = com_object     

    def get_first_axis(self, o_first_axis):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetFirstAxis
                | o Sub GetFirstAxis(        oFirstAxis)
                | 
                | Returns the coordinates of the first plane axis.
                |
                | Parameters:
                | oFirstAxis[0]
                |    The X Coordinate of the first plane axis
                |    
                |  oFirstAxis[1]
                |    The Y Coordinate of the first plane axis
                |    
                |  oFirstAxis[2]
                |    The Z Coordinate of the first plane axis
                |  
                | 
                |  See also:


        :param o_first_axis:
        :return:
        """
        return self.plane.GetFirstAxis(o_first_axis)

    def get_origin(self, o_origin):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetOrigin
                | o Sub GetOrigin(        oOrigin)
                | 
                | Returns the origin of the plane.
                |
                | Parameters:
                | oOrigin[0]
                |    The X Coordinate of the plane origin
                |    
                |  oOrigin[1]
                |    The Y Coordinate of the plane origin
                |    
                |  oOrigin[2]
                |    The Z Coordinate of the plane origin
                |  
                | 
                |  See also:


        :param o_origin:
        :return:
        """
        return self.plane.GetOrigin(o_origin)

    def get_position(self, o_x, o_y, o_z):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetPosition
                | o Sub GetPosition(        oX,
                |                           oY,
                |                           oZ)
                | 
                | Gets the position where the plane is displayed.
                |
                | Parameters:
                | oX
                |        X coordinates 
                |  
                |  oY
                |        Y coordinates 
                |  
                |  oZ
                |        Z coordinates 
                |  
                | 
                |  Returns:
                |    S_OK if the position has been set before, E_FAIL else.


        :param o_x:
        :param o_y:
        :param o_z:
        :return:
        """
        return self.plane.GetPosition(o_x, o_y, o_z)

    def get_second_axis(self, o_second_axis):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetSecondAxis
                | o Sub GetSecondAxis(        oSecondAxis)
                | 
                | Returns the coordinates of the second plane axis.
                |
                | Parameters:
                | oSecondAxis[0]
                |     The X Coordinate of the second plane axis
                |    
                |  oSecondAxis[1]
                |    The Y Coordinate of the second plane axis
                |    
                |  oSecondAxis[2]
                |    The Z Coordinate of the second plane axis
                |  
                | 
                |  See also:


        :param o_second_axis:
        :return:
        """
        return self.plane.GetSecondAxis(o_second_axis)

    def is_a_ref_plane(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | IsARefPlane
                | o Func IsARefPlane(    ) As
                | 
                | Queries whether the plane is a reference plane (fixed axis
                | plane). Returns: 0 when the plane is a reference plane, 1
                | else.
                |
                | Parameters:


        :return:
        """
        return self.plane.IsARefPlane()

    def put_first_axis(self, i_first_axis):
        """
        .. note::
            CAA V5 Visual Basic help

                | PutFirstAxis
                | o Sub PutFirstAxis(        iFirstAxis)
                | 
                | Sets the first axis. The first plane axis must be a point-
                | direction line. Note: This method can only be used on
                | CATIAHybridShapePlane2Lines feature
                |
                | Parameters:
                | iFirstAxis[0]
                |    The X Coordinate of the first plane axis
                |    
                |  iFirstAxis[1]
                |    The Y Coordinate of the first plane axis
                |    
                |  iFirstAxis[2]
                |    The Z Coordinate of the first plane axis
                |  
                | 
                |  See also:


        :param i_first_axis:
        :return:
        """
        return self.plane.PutFirstAxis(i_first_axis)

    def put_origin(self, i_origin):
        """
        .. note::
            CAA V5 Visual Basic help

                | PutOrigin
                | o Sub PutOrigin(        iOrigin)
                | 
                | Sets the origin of the plane. Note: This method can only be
                | used on CATIAHybridShapePlane2Lines feature
                |
                | Parameters:
                | iOrigin[0]
                |    The X Coordinate of the plane origin
                |    
                |  iOrigin[1]
                |    The Y Coordinate of the plane origin
                |    
                |  iOrigin[2]
                |    The Z Coordinate of the plane origin
                |  
                | 
                |  See also:


        :param i_origin:
        :return:
        """
        return self.plane.PutOrigin(i_origin)

    def put_second_axis(self, i_second_axis):
        """
        .. note::
            CAA V5 Visual Basic help

                | PutSecondAxis
                | o Sub PutSecondAxis(        iSecondAxis)
                | 
                | Sets the coordinates of the second plane axis. The second
                | plane axis must be a point-direction line Note: This method
                | can only be used on CATIAHybridShapePlane2Lines feature
                |
                | Parameters:
                | iSecondAxis[0]
                |    The X Coordinate of the second plane axis
                |    
                |  iSecondAxis[1]
                |    The Y Coordinate of the second plane axis
                |    
                |  iSecondAxis[2]
                |    The Z Coordinate of the second plane axis
                |  
                | 
                |  See also:


        :param i_second_axis:
        :return:
        """
        return self.plane.PutSecondAxis(i_second_axis)

    def remove_position(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | RemovePosition
                | o Sub RemovePosition(    )
                | 
                | Removes reference position of a plane. Note: When removed,
                | the plane is displayed at its default position.
                |
                | Parameters:


        :return:
        """
        return self.plane.RemovePosition()

    def set_position(self, i_x, i_y, i_z):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetPosition
                | o Sub SetPosition(        iX,
                |                           iY,
                |                           iZ)
                | 
                | Sets the position where the plane is displayed.
                |
                | Parameters:
                | iX
                |        X coordinates 
                |  
                |  iY
                |        Y coordinates 
                |  
                |  iZ
                |        Z coordinates


        :param i_x:
        :param i_y:
        :param i_z:
        :return:
        """
        return self.plane.SetPosition(i_x, i_y, i_z)

    def __repr__(self):
        return f'Plane()'
