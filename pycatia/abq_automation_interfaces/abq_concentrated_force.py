#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.abq_automation_interfaces.abq_load import ABQLoad
from pycatia.in_interfaces.reference import Reference
from pycatia.mec_mod_interfaces.axis_system import AxisSystem
from pycatia.product_structure_interfaces.product import Product
from pycatia.product_structure_interfaces.publication import Publication


class ABQConcentratedForce(ABQLoad):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     ABQAutomationItf.ABQLoad
                |                         ABQConcentratedForce
                | 
                | Represents an Abaqus concentrated force object
                | (ABQConcentratedForce).
                | Role: Access an Abaqus concentrated force object or determine its
                | properties.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.abq_concentrated_force = com_object

    @property
    def apply_user_subroutine(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ApplyUserSubroutine() As boolean
                | 
                |     Sets or returns the user subroutine flag.
                | 
                |     Returns:
                |         A boolean specifying whether a user subroutine will be
                |         applied.

        :rtype: bool
        """

        return self.abq_concentrated_force.ApplyUserSubroutine

    @apply_user_subroutine.setter
    def apply_user_subroutine(self, value: bool):
        """
        :param bool value:
        """

        self.abq_concentrated_force.ApplyUserSubroutine = value

    @property
    def follow_nodal_rotation(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property FollowNodalRotation() As boolean
                | 
                |     Sets or returns the follow nodal rotation flag.

        :rtype: bool
        """

        return self.abq_concentrated_force.FollowNodalRotation

    @follow_nodal_rotation.setter
    def follow_nodal_rotation(self, value: bool):
        """
        :param bool value:
        """

        self.abq_concentrated_force.FollowNodalRotation = value

    @property
    def load_type(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property LoadType() As ABQConcForceLoad_Type
                | 
                |     Sets or returns the load type whether Point Load, Distributed Load or Load
                |     Density.
                | 
                |     Returns:
                |         The load type.
                | 
                |         Legal values:
                | 
                |         POINTLOAD
                |         DISTRIBUTEDLOAD
                |         LOADDENSITY

        :return: enum abq_conc_force_load_type
        :rtype: int
        """

        return self.abq_concentrated_force.LoadType

    @load_type.setter
    def load_type(self, value: int):
        """
        :param int value: enum abq_conc_force_load_type
        """

        self.abq_concentrated_force.LoadType = value

    @property
    def uselocal_csys(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property UselocalCsys() As boolean
                | 
                |     Sets or returns a boolean indicating whether local coordinate system is
                |     used in Conc force
                | 
                |     Returns:
                |         boolean specifying whether local csys is active.

        :rtype: bool
        """

        return self.abq_concentrated_force.UselocalCsys

    @uselocal_csys.setter
    def uselocal_csys(self, value: bool):
        """
        :param bool value:
        """

        self.abq_concentrated_force.UselocalCsys = value

    @property
    def cf1(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property cf1() As double
                | 
                |     Sets or returns the concentrated force component in the
                |     1-direction.
                | 
                |     Returns:
                |         The concentrated force component in the 1-direction.

        :rtype: float
        """

        return self.abq_concentrated_force.cf1

    @cf1.setter
    def cf1(self, value: float):
        """
        :param float value:
        """

        self.abq_concentrated_force.cf1 = value

    @property
    def cf2(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property cf2() As double
                | 
                |     Sets or returns the concentrated force component in the
                |     2-direction.
                | 
                |     Returns:
                |         The concentrated force component in the 2-direction.

        :rtype: float
        """

        return self.abq_concentrated_force.cf2

    @cf2.setter
    def cf2(self, value: float):
        """
        :param float value:
        """

        self.abq_concentrated_force.cf2 = value

    @property
    def cf3(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property cf3() As double
                | 
                |     Sets or returns the concentrated force component in the
                |     3-direction.
                | 
                |     Returns:
                |         The concentrated force component in the 3-direction.

        :rtype: float
        """

        return self.abq_concentrated_force.cf3

    @cf3.setter
    def cf3(self, value: float):
        """
        :param float value:
        """

        self.abq_concentrated_force.cf3 = value

    @property
    def cm1(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property cm1() As double
                | 
                |     Sets or returns the concentrated moment component in the
                |     1-direction.
                | 
                |     Returns:
                |         The concentrated moment component in the 1-direction.

        :rtype: float
        """

        return self.abq_concentrated_force.cm1

    @cm1.setter
    def cm1(self, value: float):
        """
        :param float value:
        """

        self.abq_concentrated_force.cm1 = value

    @property
    def cm2(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property cm2() As double
                | 
                |     Sets or returns the concentrated moment component in the
                |     2-direction.
                | 
                |     Returns:
                |         The concentrated moment component in the 2-direction.

        :rtype: float
        """

        return self.abq_concentrated_force.cm2

    @cm2.setter
    def cm2(self, value: float):
        """
        :param float value:
        """

        self.abq_concentrated_force.cm2 = value

    @property
    def cm3(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property cm3() As double
                | 
                |     Sets or returns the concentrated moment component in the
                |     3-direction.
                | 
                |     Returns:
                |         The concentrated moment component in the 3-direction.

        :rtype: float
        """

        return self.abq_concentrated_force.cm3

    @cm3.setter
    def cm3(self, value: float):
        """
        :param float value:
        """

        self.abq_concentrated_force.cm3 = value

    @property
    def local_csys(self) -> AxisSystem:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property localCsys() As AxisSystem
                | 
                |     Sets or returns the local coordinate system of the concentrated
                |     force.
                | 
                |     Returns:
                |         The local coordinate system.

        :rtype: AxisSystem
        """

        return AxisSystem(self.abq_concentrated_force.localCsys)

    @local_csys.setter
    def local_csys(self, value: AxisSystem):
        """
        :param AxisSystem value:
        """

        self.abq_concentrated_force.localCsys = value

    def get_handler(self, o_product: Reference, o_ref: Reference) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetHandler(Reference oProduct,
                | Reference oRef)
                | 
                |     Returns the handler for the distributed load.
                | 
                |     Parameters:
                | 
                |         oProduct
                |             The product for the handler. 
                |         oRef
                |             The reference to the handler.

        :param Reference o_product:
        :param Reference o_ref:
        :rtype: None
        """
        return self.abq_concentrated_force.GetHandler(o_product.com_object, o_ref.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_handler'
        # # vba_code = """
        # # Public Function get_handler(abq_concentrated_force)
        # #     Dim oProduct (2)
        # #     abq_concentrated_force.GetHandler oProduct
        # #     get_handler = oProduct
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
                |     Gets the published local coordinate system of the concentrated
                |     force.
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
        return self.abq_concentrated_force.GetLocalCsysFromPublication(o_product.com_object,
                                                                       o_pub_axis_system.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_local_csys_from_publication'
        # # vba_code = """
        # # Public Function get_local_csys_from_publication(abq_concentrated_force)
        # #     Dim oProduct (2)
        # #     abq_concentrated_force.GetLocalCsysFromPublication oProduct
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
                |             e.g. ABQ_CARTESIAN, ABQ_CYLINDRICAL, ABQ_SPHERICAL,
                |             ABQ_DEFAULTAXIS

        :rtype: enum abq_local_csys_type
        :rtype: int
        """
        return self.abq_concentrated_force.GetUseCoordinateSystemType()

    def set_handler(self, i_product: Reference, i_ref: Reference) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetHandler(Reference iProduct,
                | Reference iRef)
                |
                |     Sets the handler for the distributed load. Any previously set handler will
                |     be replaced with this new value.
                |
                |     Parameters:
                |
                |         iProduct
                |             The product for the handler.
                |         iRef
                |             The reference to the handler.

        :param Reference i_product:
        :param Reference i_ref:
        :rtype: None
        """
        return self.abq_concentrated_force.SetHandler(i_product.com_object, i_ref.com_object)
        # # # # Autogenerated comment:
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_handler'
        # # vba_code = """
        # # Public Function set_handler(abq_concentrated_force)
        # #     Dim iProduct (2)
        # #     abq_concentrated_force.SetHandler iProduct
        # #     set_handler = iProduct
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
                |     Sets the published local coordinate system of the concentrated
                |     force.
                |
                |     Returns:
                |         Fails if the publication is not an axis system.
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
        return self.abq_concentrated_force.SetLocalCsysFromPublication(i_product.com_object,
                                                                       i_pub_axis_system.com_object)
        # # # # Autogenerated comment:
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_local_csys_from_publication'
        # # vba_code = """
        # # Public Function set_local_csys_from_publication(abq_concentrated_force)
        # #     Dim iProduct (2)
        # #     abq_concentrated_force.SetLocalCsysFromPublication iProduct
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
                |     set the user coordinate system type.
                |
                |     Parameters:
                |
                |         iCsystemType
                |             e.g. ABQ_CARTESIAN, ABQ_CYLINDRICAL, ABQ_SPHERICAL,
                |             ABQ_DEFAULTAXIS

        :param int i_csystem_type: enum abq_local_csys_type
        :rtype: None
        """
        return self.abq_concentrated_force.SetUseCoordinateSystemType(i_csystem_type)

    def __repr__(self):
        return f'ABQConcentratedForce(name="{self.name}")'
