#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.abq_automation_interfaces.abq_boundary_condition import ABQBoundaryCondition
from pycatia.mec_mod_interfaces.axis_system import AxisSystem
from pycatia.product_structure_interfaces.product import Product
from pycatia.product_structure_interfaces.publication import Publication


class ABQDisplacementBC(ABQBoundaryCondition):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     ABQAutomationItf.ABQBoundaryCondition
                |                         ABQDisplacementBC
                | 
                | Represents an Abaqus displacement boundary condition (ABQDisplacementBC)
                | object.
                | Role: Access an Abaqus displacement boundary condition object or determine its
                | properties.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.abq_displacement_bc = com_object

    @property
    def use_local_csys(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property UselocalCsys() As boolean
                | 
                |     Sets or returns a boolean indicating whether local coordinate system is
                |     used in Displacement BC
                | 
                |     Returns:
                |         boolean specifying whether local csys is active.

        :rtype: bool
        """

        return self.abq_displacement_bc.UselocalCsys

    @use_local_csys.setter
    def use_local_csys(self, value: bool):
        """
        :param bool value:
        """

        self.abq_displacement_bc.UselocalCsys = value

    @property
    def local_csys(self) -> AxisSystem:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property localCsys() As AxisSystem
                | 
                |     Sets or returns the local coordinate system of the boundary condition's
                |     degrees of freedom.
                | 
                |     Returns:
                |         The local coordinate system.

        :rtype: AxisSystem
        """

        return AxisSystem(self.abq_displacement_bc.localCsys)

    @local_csys.setter
    def local_csys(self, value: AxisSystem):
        """
        :param AxisSystem value:
        """

        self.abq_displacement_bc.localCsys = value

    @property
    def u1(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property u1() As double
                | 
                |     Sets or returns the first translational component.
                | 
                |     Returns:
                |         The first translational component.

        :rtype: float
        """

        return self.abq_displacement_bc.u1

    @u1.setter
    def u1(self, value: float):
        """
        :param float value:
        """

        self.abq_displacement_bc.u1 = value

    @property
    def u2(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property u2() As double
                | 
                |     Sets or returns the second translational component.
                | 
                |     Returns:
                |         The second translational component.

        :rtype: float
        """

        return self.abq_displacement_bc.u2

    @u2.setter
    def u2(self, value: float):
        """
        :param float value:
        """

        self.abq_displacement_bc.u2 = value

    @property
    def u3(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property u3() As double
                | 
                |     Sets or returns the third translational component.
                | 
                |     Returns:
                |         The third translational component.

        :rtype: float
        """

        return self.abq_displacement_bc.u3

    @u3.setter
    def u3(self, value: float):
        """
        :param float value:
        """

        self.abq_displacement_bc.u3 = value

    @property
    def ur1(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ur1() As double
                | 
                |     Sets or returns the first rotational component.
                | 
                |     Returns:
                |         The second rotational component.

        :rtype: float
        """

        return self.abq_displacement_bc.ur1

    @ur1.setter
    def ur1(self, value: float):
        """
        :param float value:
        """

        self.abq_displacement_bc.ur1 = value

    @property
    def ur2(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ur2() As double
                | 
                |     Sets or returns the second rotational component.
                | 
                |     Returns:
                |         The second rotational component.

        :rtype: float
        """

        return self.abq_displacement_bc.ur2

    @ur2.setter
    def ur2(self, value: float):
        """
        :param float value:
        """

        self.abq_displacement_bc.ur2 = value

    @property
    def ur3(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ur3() As double
                | 
                |     Sets or returns the third rotational component.
                | 
                |     Returns:
                |         The third rotational component.

        :rtype: float
        """

        return self.abq_displacement_bc.ur3

    @ur3.setter
    def ur3(self, value: float):
        """
        :param float value:
        """

        self.abq_displacement_bc.ur3 = value

    def get_dof_activation(self, i_dof: int, o_flag: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetDOFActivation(long iDOF,
                | boolean oFlag)
                | 
                |     Gets the activation of a DOF for Displacement BC
                | 
                |     Parameters:
                | 
                |         iDOF
                |             The DOF number from 1 to 6, in order U1 = 1,...., UR3 = 6.
                |         oFlag
                |             DOF activation status true or false.

        :param int i_dof:
        :param bool o_flag:
        :rtype: None
        """
        return self.abq_displacement_bc.GetDOFActivation(i_dof, o_flag)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_dof_activation'
        # # vba_code = """
        # # Public Function get_dof_activation(abq_displacement_bc)
        # #     Dim iDOF (2)
        # #     abq_displacement_bc.GetDOFActivation iDOF
        # #     get_dof_activation = iDOF
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_local_csys_from_publication(self, o_product: Product, o_pub_axis_system: AxisSystem) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetLocalCsysFromPublication(Product oProduct,
                | AxisSystem oPubAxisSystem)
                | 
                |     Gets the published local coordinate system of the Displacement
                |     BC.
                | 
                |     Parameters:
                | 
                |         oProduct
                |             The CATIA Product specifying the local coordinate system
                |             publication.
                |         oPubAxisSystem
                |             The CATIA Axis system.
                | 
                |             Refer: CATIAAxisSystem

        :param Product o_product:
        :param AxisSystem o_pub_axis_system:
        :rtype: None
        """
        return self.abq_displacement_bc.GetLocalCsysFromPublication(o_product.com_object, o_pub_axis_system.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_local_csys_from_publication'
        # # vba_code = """
        # # Public Function get_local_csys_from_publication(abq_displacement_bc)
        # #     Dim oProduct (2)
        # #     abq_displacement_bc.GetLocalCsysFromPublication oProduct
        # #     get_local_csys_from_publication = oProduct
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_use_coordinate_system_type(self) -> int:
        """
        .. note::
            :class: toggle
    
            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetUseCoordinateSystemType() As ABQLocalCsysType
                |
                |     Get the user coordinate system type.
                |
                |     Parameters:
                |
                |         oCsystemType
                |             e.g. ABQ_CARTESIAN (for Cartesian coordinate system),
                |             ABQ_CYLINDRICAL (for Cylindrical coordinate system), ABQ_SPHERICAL (for
                |             Spherical coordinate system),
    
        :return: enum abq_local_csys_type
        :rtype: int
        """
        return self.abq_displacement_bc.GetUseCoordinateSystemType()

    def set_dof_activation(self, i_dof: int, i_flag: bool) -> None:
        """
        .. note::
            :class: toggle
    
            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetDOFActivation(long iDOF,
                | boolean iFlag)
                |
                |     Sets the activation of a DOF for Displacement BC
                |
                |     Parameters:
                |
                |         iDOF
                |             The DOF number from 1 to 6, in order U1 = 1,...., UR3 = 6.
                |         iFlag
                |             DOF activation status true or false.
    
        :param int i_dof:
        :param bool i_flag:
        :rtype: None
        """
        return self.abq_displacement_bc.SetDOFActivation(i_dof, i_flag)
        # # # # Autogenerated comment:
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_dof_activation'
        # # vba_code = """
        # # Public Function set_dof_activation(abq_displacement_bc)
        # #     Dim iDOF (2)
        # #     abq_displacement_bc.SetDOFActivation iDOF
        # #     set_dof_activation = iDOF
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_local_csys_from_publication(self, i_product: Product, i_pub_axis_system: Publication) -> None:
        """
        .. note::
            :class: toggle
    
            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetLocalCsysFromPublication(Product iProduct,
                | Publication iPubAxisSystem)
                |
                |     Sets the published local coordinate system of the Displacement
                |     BC.
                |
                |     Returns:
                |         Fails if the publication is not on the axis system.
                |     Parameters:
                |
                |         iProduct
                |             The CATIA Product specifying the local coordinate system
                |             publication.
                |         iPublication
                |             The CATIA Publication on the axis system.
                |
                |             Refer: CATIAPublication
    
        :param Product i_product:
        :param Publication i_pub_axis_system:
        :rtype: None
        """
        return self.abq_displacement_bc.SetLocalCsysFromPublication(i_product.com_object, i_pub_axis_system.com_object)
        # # # # Autogenerated comment:
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_local_csys_from_publication'
        # # vba_code = """
        # # Public Function set_local_csys_from_publication(abq_displacement_bc)
        # #     Dim iProduct (2)
        # #     abq_displacement_bc.SetLocalCsysFromPublication iProduct
        # #     set_local_csys_from_publication = iProduct
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_use_coordinate_system_type(self, i_csystem_type: int) -> None:
        """
        .. note::
            :class: toggle
    
            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetUseCoordinateSystemType(ABQLocalCsysType
                | iCsystemType)
                |
                |     Set the user coordinate system type.
                |
                |     Parameters:
                |
                |         iCsystemType
                |             e.g. ABQ_CARTESIAN (for Cartesian coordinate system),
                |             ABQ_CYLINDRICAL (for Cylindrical coordinate system), ABQ_SPHERICAL (for
                |             Spherical coordinate system),
    
        :param int i_csystem_type: enum abq_local_csys_type
        :rtype: None
        """
        return self.abq_displacement_bc.SetUseCoordinateSystemType(i_csystem_type)

    def __repr__(self):
        return f'ABQDisplacementBC(name="{self.name}")'
