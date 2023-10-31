#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.abq_automation_interfaces.abq_load import ABQLoad
from pycatia.mec_mod_interfaces.axis_system import AxisSystem
from pycatia.product_structure_interfaces.product import Product
from pycatia.product_structure_interfaces.publication import Publication


class ABQGravity(ABQLoad):
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
                |                         ABQGravity
                | 
                | Represents an Abaqus gravity (ABQGravity) object.
                | Role: Access an Abaqus gravity load object or determine its
                | properties.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.abq_gravity = com_object

    @property
    def use_local_csys(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property UselocalCsys() As boolean
                | 
                |     Sets or returns a boolean indicating whether local coordinate system is
                |     used in Gravity load.
                | 
                |     Returns:
                |         boolean specifying whether local csys is active.

        :rtype: bool
        """

        return self.abq_gravity.UselocalCsys

    @use_local_csys.setter
    def use_local_csys(self, value: bool):
        """
        :param bool value:
        """

        self.abq_gravity.UselocalCsys = value

    @property
    def comp1(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property comp1() As double
                | 
                |     Sets or returns the gravity component in the 1-direction.
                | 
                |     Returns:
                |         The gravity component in the 1-direction.

        :rtype: float
        """

        return self.abq_gravity.comp1

    @comp1.setter
    def comp1(self, value: float):
        """
        :param float value:
        """

        self.abq_gravity.comp1 = value

    @property
    def comp2(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property comp2() As double
                | 
                |     Sets or returns the gravity component in the 2-direction.
                | 
                |     Returns:
                |         The gravity component in the 2-direction.

        :rtype: float
        """

        return self.abq_gravity.comp2

    @comp2.setter
    def comp2(self, value: float):
        """
        :param float value:
        """

        self.abq_gravity.comp2 = value

    @property
    def comp3(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property comp3() As double
                | 
                |     Sets or returns the gravity component in the 3-direction.
                | 
                |     Returns:
                |         The gravity component in the 3-direction.

        :rtype: float
        """

        return self.abq_gravity.comp3

    @comp3.setter
    def comp3(self, value: float):
        """
        :param float value:
        """

        self.abq_gravity.comp3 = value

    @property
    def local_csys(self) -> AxisSystem:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property localCsys() As AxisSystem
                | 
                |     Sets or returns the local coordinate system of the gravity
                |     load.
                | 
                |     Returns:
                |         The local coordinate system.

        :rtype: AxisSystem
        """

        return AxisSystem(self.abq_gravity.localCsys)

    @local_csys.setter
    def local_csys(self, value: AxisSystem):
        """
        :param AxisSystem value:
        """

        self.abq_gravity.localCsys = value

    def get_local_csys_from_publication(self, o_product: Product, o_pub_axis_system: AxisSystem) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetLocalCsysFromPublication(Product oProduct,
                | AxisSystem oPubAxisSystem)
                | 
                |     Gets the published local coordinate system of the gravity
                |     load.
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
        return self.abq_gravity.GetLocalCsysFromPublication(o_product.com_object, o_pub_axis_system.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_local_csys_from_publication'
        # # vba_code = """
        # # Public Function get_local_csys_from_publication(abq_gravity)
        # #     Dim oProduct (2)
        # #     abq_gravity.GetLocalCsysFromPublication oProduct
        # #     get_local_csys_from_publication = oProduct
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
                |     Sets the published local coordinate system of the gravity
                |     load.
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
        return self.abq_gravity.SetLocalCsysFromPublication(i_product.com_object, i_pub_axis_system.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_local_csys_from_publication'
        # # vba_code = """
        # # Public Function set_local_csys_from_publication(abq_gravity)
        # #     Dim iProduct (2)
        # #     abq_gravity.SetLocalCsysFromPublication iProduct
        # #     set_local_csys_from_publication = iProduct
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'ABQGravity(name="{self.name}")'
