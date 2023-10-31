#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-07-06 14:02:20.222384

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.in_interfaces.move import Move
from pycatia.system_interfaces.system_service import SystemService


class Position(Move):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     InfInterfaces.Move
                |                         Position
                | 
                | Represents the position object.
                | The position object is the 3D-axis system associated with an
                | object.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.position = com_object

    def get_components(self) -> tuple:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub GetComponents(CATSafeArrayVariant
                | oAxisComponentsArray)
                | 
                |     Returns the components of an object's position. This returns the 3D-axis
                |     system associated with the object.
                | 
                |     Parameters:
                | 
                |         oAxisComponentsArray
                |             The array used to store the twelve components retrieved from the
                |             objet's position. The first nine represent succcessively the components of the
                |             x-axis, y-axis, and z-axis. The last three represent the coordinates of the
                |             origin point. 
                | 
                |     Example:
                | 
                |           This example retrieves in oAxisComponentsArray
                |          the 3D-axis system components from 
                |          the Position object associated with MyObject:
                |          
                | 
                |          Dim oAxisComponentsArray ( 11 )
                |          MyObject.Position.GetComponents oAxisComponentsArray

        :rtype: tuple
        """
        vba_function_name = 'get_components'
        vba_code = """
        Public Function get_components(position)
            Dim oAxisComponentsArray(11)
            position.GetComponents oAxisComponentsArray
            get_components = oAxisComponentsArray
        End Function
        """

        system_service = self.application.system_service
        return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_components(self, i_axis_components_array: tuple) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetComponents(CATSafeArrayVariant
                | iAxisComponentsArray)
                | 
                |     Sets the components of an object's position. This sets the 3D-axis system
                |     associated with the object.
                | 
                |     Parameters:
                | 
                |         iAxisComponentsArray
                |             The array initialized with the components to set to the object's
                |             position. The first nine represent succcessively the components of the x-axis,
                |             y-axis, and z-axis. The last three represent the coordinates of the origin
                |             point. 
                | 
                |     Example:
                | 
                |           This example sets the 3D-axis system components stored
                |           in
                |          iAxisComponentsArray to
                |          the Position object associated with MyObject:
                |          
                | 
                |          Dim iAxisComponentsArray( 11 )
                |          ' x axis components
                |          iAxisComponentsArray( 0 )  = 1.000
                |          iAxisComponentsArray( 1 )  = 0
                |          iAxisComponentsArray( 2 )  = 0.707
                |          ' y axis components
                |          iAxisComponentsArray( 3 )  = 0
                |          iAxisComponentsArray( 4 )  = 0
                |          iAxisComponentsArray( 5 )  = 0.707
                |          ' z axis components
                |          iAxisComponentsArray( 6 )  = 0
                |          iAxisComponentsArray( 7 )  = -0.707
                |          iAxisComponentsArray( 8 )  = 0.707
                |          ' origin point coordinates
                |          iAxisComponentsArray( 9 )  = 1.000
                |          iAxisComponentsArray( 10 ) = 2.000
                |          iAxisComponentsArray( 11 ) = 3.000
                |          MyObject.Position.SetComponents iAxisComponentsArray

        :param tuple i_axis_components_array:
        :rtype: None
        """
        return self.position.SetComponents(i_axis_components_array)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_components'
        # # vba_code = """
        # # Public Function set_components(position)
        # #     Dim iAxisComponentsArray (2)
        # #     position.SetComponents iAxisComponentsArray
        # #     set_components = iAxisComponentsArray
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'Position(name="{self.name}")'
