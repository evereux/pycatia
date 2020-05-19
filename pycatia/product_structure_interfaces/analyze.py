#! /usr/bin/python3.6
# module initially auto generated using V5Automation.chm from CATIA V5 R25

from pycatia.system_interfaces.base_object import AnyObject
from pycatia.system_interfaces.systemservice import SystemService


class Analyze(AnyObject):
    """
        .. note::
            CAA V5 Visual Basic help

                | Represents the analysis object associated with a product.

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.analyze = com_object

    @property
    def mass(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Mass
                | o Property Mass(    ) As double
                |
                | Returns the product mass value.  Example:    This example retrieves
                | MassValue from   the Analyze object associated with myProduct:
                | MassValue = myProduct.Analyze.Mass

        :return: float
        """
        return self.analyze.Mass

    @property
    def volume(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Volume
                | o Property Volume(    ) As double
                |
                | Returns the product volume value.  Example:    This example retrieves
                | VolumeValue from   the Analyze object associated with myProduct:
                | VolumeValue = myProduct.Analyze.Volume


                | Parameters:


        """
        return self.analyze.Volume

    @property
    def wet_area(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | WetArea
                | o Property WetArea(    ) As double
                |
                | Returns the product wet area (outer volume). Note: This method uses
                | mm2 instead of default Catia V5 unit.  Example:    This example
                | retrieves WetAreaValue from   the Analyze object associated with
                | myProduct:  WetAreaValue = myProduct.Analyze.WetArea


                | Parameters:


        """
        return self.analyze.WetArea

    def get_gravity_center(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetGravityCenter
                | o Sub GetGravityCenter(    CATSafeArrayVariant    oGravityCenterCoordinatesArray)
                |
                | Returns the gravity center coordinates of product.
                |
                | Parameters:
                | Coordinates
                |    The array storing the three gravity center coordinates.
                |    This array must be previously initialized.
                |
                | Examples:
                | This example retrieves the gravity center coordinates in
                | oGravityCenterCoordinatesArray from
                | the Analyze object associated with myProduct:
                |
                | ' Coordinates array initialization
                | Dim oGravityCenterCoordinatesArray ( 2 )
                | ' Get value in array
                | Myproduct.Analyze.GetGravityCenter oGravityCenterCoordinatesArray
        """

        vba_function_name = 'get_gravity_center'
        vba_function = 'GetGravityCenter'
        vba_code = f'''        
        Public Function {vba_function_name}(analyze)
            Dim coord(2)
            analyze.{vba_function} coord
            {vba_function_name} = coord
        End Function
        '''
        system_service = SystemService(self.application.SystemService)
        result = system_service.evaluate(vba_code, 0, vba_function_name, [self.analyze])

        return result

    def get_inertia(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetInertia
                | o Sub GetInertia(    CATSafeArrayVariant    oInertiaMatrixArray)
                |
                | Returns the inertia matrix array of product.


                | Parameters:
                | oInertiaMatrixArray
                |    The array storing successively the three columns of inertia matrix.
                |    This array must be previously initialized.


                | Examples:
                |
                | This example retrieves the inertia matrix components in
                | oInertiaMatrixArray from
                | the Analyze object associated with myProduct:
                |
                | ' Components array initialization
                | Dim oInertiaMatrixArray ( 8 )
                | ' Get value in array
                | Myproduct.Analyze.GetInertia oInertiaMatrixArray
                | ' oInertiaMatrixArray ( 0 ) is the Ixx component
                | ' oInertiaMatrixArray ( 1 ) is the Ixy component
                | ' oInertiaMatrixArray ( 2 ) is the Ixz component
                | ' oInertiaMatrixArray ( 3 ) is the Iyx component
                | ' oInertiaMatrixArray ( 4 ) is the Iyy component
                | ' oInertiaMatrixArray ( 5 ) is the Iyz component
                | ' oInertiaMatrixArray ( 6 ) is the Izx component
                | ' oInertiaMatrixArray ( 7 ) is the Izy component
                | ' oInertiaMatrixArray ( 8 ) is the Izz component
                |
                |
                |
        """
        vba_function_name = 'get_inertia'
        vba_function = 'GetInertia'
        vba_code = f'''        
        Public Function {vba_function_name}(analyze)
            Dim coord(8)
            analyze.{vba_function} coord
            {vba_function_name} = coord
        End Function
        '''
        system_service = SystemService(self.application.SystemService)
        result = system_service.evaluate(vba_code, 0, vba_function_name, [self.analyze])

        return result

    def __repr__(self):
        return f'Analyze()'
