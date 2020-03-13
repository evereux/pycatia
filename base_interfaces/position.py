#! /usr/bin/python3.6


class Position:
    """
            .. note::
                CAA V5 Visual Basic help

                | Represents the position object.
                | The position object is the 3D-axis system associated with an object.
    """

    def __init__(self, _object):
        self.position = _object.Position

    def get_components(self, catia):
        """

        .. note::
            CAA V5 Visual Basic help

            Returns the components of an object's position. This returns the 3D-axis system associated with the object.

            Parameters:
            oAxisComponentsArray

            The array used to store the twelve components retrieved from the objet's position. The first nine
            represent succcessively the components of the x-axis, y-axis, and z-axis. The last three represent the
            coordinates of the origin point.
            | Example:
            | This example retrieves in oAxisComponentsArray the 3D-axis system components from the Position object
            | associated with MyObject:
            |     Dim oAxisComponentsArray ( 11 )
            |     MyObject.Position.GetComponents oAxisComponentsArray

        :param catia:
        :return:
        """

        # return self.object.Position.GetComponents
        vba_function_name = 'get_components'
        vba_function = 'GetComponents'
        vba_code = f'''        
        Public Function {vba_function_name}(position)
            Dim oAxisComponentsArray (11)
            position.{vba_function} oAxisComponentsArray
            {vba_function_name} = oAxisComponentsArray
        End Function
        '''

        return catia.evaluate(vba_code, vba_function_name, [self.position])

    def set_components(self):
        """

        .. note::
            CAA V5 Visual Basic help

            Sets the components of an object's position. This sets the 3D-axis system associated with the object.

            Parameters:
            iAxisComponentsArray
            The array initialized with the components to set to the object's position. The first nine represent
            succcessively the components of the x-axis, y-axis, and z-axis. The last three represent the coordinates
            of the origin point.

            | Example:
            | This example sets the 3D-axis system components stored in iAxisComponentsArray to the Position object
            | associated with MyObject:
            |     Dim iAxisComponentsArray( 11 )
            |     ' x axis components
            |     iAxisComponentsArray( 0 )  = 1.000
            |     iAxisComponentsArray( 1 )  = 0
            |     iAxisComponentsArray( 2 )  = 0.707
            |     ' y axis components
            |     iAxisComponentsArray( 3 )  = 0
            |     iAxisComponentsArray( 4 )  = 0
            |     iAxisComponentsArray( 5 )  = 0.707
            |     ' z axis components
            |     iAxisComponentsArray( 6 )  = 0
            |     iAxisComponentsArray( 7 )  = -0.707
            |     iAxisComponentsArray( 8 )  = 0.707
            |     ' origin point coordinates
            |     iAxisComponentsArray( 9 )  = 1.000
            |     iAxisComponentsArray( 10 ) = 2.000
            |     iAxisComponentsArray( 11 ) = 3.000
            |     MyObject.Position.SetComponents iAxisComponentsArray



        :return:
        """

        # todo
        return False
