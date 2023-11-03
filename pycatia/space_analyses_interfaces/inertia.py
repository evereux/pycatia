#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.any_object import AnyObject


class Inertia(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     Inertia
                | 
                | Represents the Inertia object.
                | The Inertia object can be associated with any relevant object of a document in
                | order to get or compute its inertia data. It takes into account all bodies of a
                | part.
                | 
                | This version allows you to compute the following data:
                | 
                |     mass
                |     density
                |     position of the center of gravity
                |     inertia matrix
                |     principal axes
                |     principal moments 
                | 
                | of a product.
                | 
                | The units are:
                | 
                |     Kilogram (Kg) for Mass
                |     Square meter (M^2) for Wet Area
                |     Cubic meter (M^3) for Volume
                |     Meter (M) for Position
                |     Square Kilogram meter ((KgM)^2) for Inertia Matrix and Principal
                |     Moments
                |     Kilogram per cubic meter (Kg/M^3) for Density 
                | 
                | The method GetTechnologicalObject("Inertia") on the product to analyze, allows
                | you to retrieve this object.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.inertia = com_object

    @property
    def density(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Density() As double
                | 
                |     Returns or sets the density for the computation.
                | 
                |     The density value is set to:
                | 
                |         0: the computation must use densities attached to each
                |         object.
                |         any positive value: the computation has to use this value.
                |
                |     The density value is returned as:
                | 
                |         1: a default value is used (there is no density attached to
                |         objects).
                |         -1: the density is not homogeneous for each object.
                |         other positive values: the density attached to all objects.
                |
                |     Example:
                | 
                |              The first example gets the density of NewInertia
                |              inertia.
                |
                |             Dim ADensity As double
                |             ADensity = NewInertia.Density
                |
                |                 The second example sets the density of NewInertia
                |                 inertia.
                |
                |                 NewInertia.Density = 10.

        :rtype: float
        """

        return self.inertia.Density

    @density.setter
    def density(self, value: float):
        """
        :param float value:
        """

        self.inertia.Density = value

    @property
    def granularity_mode(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property GranularityMode() As long
                | 
                |     Returns or sets the Granularity Mode for Inertia
                |     Computation.
                | 
                |     The Granularity value is set to:
                | 
                |         0: Only main bodies option is selected => the computation must not use
                |         All bodies.
                |         1: Only main bodies option is not selected => the computation must use
                |         All bodies. 
                | 
                |     The Granularity value is returned as:
                | 
                |         0: the computation had considered only main bodies.
                |         1: the computation had not considered only main bodies.
                |         
                |     Example:
                | 
                |              The first example gets the Granularity of NewInertia
                |              inertia.
                |
                |             Dim AGranularityMode As Integer
                |             AGranularityMode = NewInertia.GranularityMode
                |
                |                 The second example sets the Granularity of NewInertia inertia
                |                 to deselect the "only main bodies".
                |
                |                 NewInertia.GranularityMode = 1

        :rtype: int
        """

        return self.inertia.GranularityMode

    @granularity_mode.setter
    def granularity_mode(self, value: int):
        """
        :param int value:
        """

        self.inertia.GranularityMode = value

    @property
    def mass(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Mass() As double (Read Only)
                | 
                |     Returns the mass.
                | 
                |     Example:
                | 
                |              This example retrieves the mass of NewInertia
                |              inertia.
                |
                |             Dim AMass As double
                |             AMass = NewInertia.Mass

        :rtype: float
        """

        return self.inertia.Mass

    def get_cog_position(self) -> tuple:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub GetCOGPosition(CATSafeArrayVariant oCoordinates)
                | 
                |     Retrieves the position of the center of gravity.
                | 
                |     Parameters:
                | 
                |         oCoordinates
                |             The position of the center of gravity with respect to the product
                |             coordinate system:
                | 
                |                 oCoordinates(0) is the X coordinate
                |                 oCoordinates(1) is the Y coordinate
                |                 oCoordinates(2) is the Z coordinate 
                | 
                |     Example:
                | 
                |              This example retrieves the position of the center of gravity of
                |              NewInertia inertia.
                |
                |             Dim Coordinates (2)
                |             NewInertia.GetCOGPosition Coordinates

        :rtype: tuple
        """

        vba_function_name = 'get_cog_position'
        vba_code = """
        Public Function get_cog_position(inertia)
            Dim oCoordinates (2)
            inertia.GetCOGPosition oCoordinates
            get_cog_position = oCoordinates
        End Function
        """

        system_service = self.application.system_service
        return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_inertia_matrix(self) -> tuple:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub GetInertiaMatrix(CATSafeArrayVariant oMatrix)
                | 
                |     Retrieves the matrix of inertia.
                | 
                |     Parameters:
                | 
                |         oMatrix
                |             The matrix of inertia array:
                | 
                |                 oMatrix(0) is the Ixx component
                |                 oMatrix(1) is the Ixy component
                |                 oMatrix(2) is the Ixz component
                |                 oMatrix(3) is the Iyx component
                |                 oMatrix(4) is the Iyy component
                |                 oMatrix(5) is the Iyz component
                |                 oMatrix(6) is the Izx component
                |                 oMatrix(7) is the Izy component
                |                 oMatrix(8) is the Izz component 
                | 
                |     Example:
                | 
                |              This example retrieves the matrix of inertia of NewInertia
                |              inertia.
                |
                |             Dim Matrix (8)
                |             NewInertia.GetInertiaMatrix Matrix

        :rtype: tuple
        """

        vba_function_name = 'get_inertia_matrix'
        vba_code = """
        Public Function get_inertia_matrix(inertia)
            Dim oMatrix (8)
            inertia.GetInertiaMatrix oMatrix
            get_inertia_matrix = oMatrix
        End Function
        """

        system_service = self.application.system_service
        return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_principal_axes(self) -> tuple:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub GetPrincipalAxes(CATSafeArrayVariant oComponents)
                | 
                |     Retrieves the principal axes of inertia.
                | 
                |     Parameters:
                | 
                |         oComponents
                |             The principal axes of inertia array (A1, A2 and A3 are the
                |             principal axes of inertia):
                | 
                |                 oComponents(0) is the A1x component
                |                 oComponents(1) is the A2x component
                |                 oComponents(2) is the A3x component
                |                 oComponents(3) is the A1y component
                |                 oComponents(4) is the A2y component
                |                 oComponents(5) is the A3y component
                |                 oComponents(6) is the A1z component
                |                 oComponents(7) is the A2z component
                |                 oComponents(8) is the A3z component 
                | 
                |     Example:
                | 
                |              This example retrieves the principal axes of inertia of NewInertia
                |              inertia.
                |
                |             Dim Components (8)
                |             NewInertia.GetPrincipalAxes Components

        :rtype: tuple
        """
        vba_function_name = 'get_principal_axes'
        vba_code = """
        Public Function get_principal_axes(inertia)
            Dim oComponents(8)
            inertia.GetPrincipalAxes oComponents
            get_principal_axes = oComponents
        End Function
        """

        system_service = self.application.system_service
        return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_principal_moments(self) -> tuple:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub GetPrincipalMoments(CATSafeArrayVariant oValues)
                | 
                |     Retrieves the principal moments of inertia.
                | 
                |     Parameters:
                | 
                |         oValues
                |             The principal moments of inertia array:
                | 
                |                 oValues(0) is the M1 value with respect to the first principal
                |                 exes of inertia
                |                 oValues(1) is the M2 value with respect to the second principal
                |                 exes of inertia
                |                 oValues(2) is the M3 value with respect to the third principal
                |                 exes of inertia 
                | 
                |     Example:
                | 
                |              This example retrieves principal moments of inertia of NewInertia
                |              inertia.
                |
                |             Dim Values (2)
                |             NewInertia.GetPrincipalMoments Values

        :rtype: tuple
        """

        vba_function_name = 'get_principal_moments'
        vba_code = """
        Public Function get_principal_moments(inertia)
            Dim oValues (2)
            inertia.GetPrincipalMoments oValues
            get_principal_moments = oValues
        End Function
        """

        system_service = self.application.system_service
        return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'Inertia(name="{self.name}")'
