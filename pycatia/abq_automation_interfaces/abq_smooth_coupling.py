#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.abq_automation_interfaces.abq_interaction import ABQInteraction
from pycatia.in_interfaces.reference import Reference
from pycatia.mec_mod_interfaces.axis_system import AxisSystem
from pycatia.product_structure_interfaces.product import Product
from pycatia.product_structure_interfaces.publication import Publication


class ABQSmoothCoupling(ABQInteraction):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     ABQAutomationItf.ABQInteraction
                |                         ABQSmoothCoupling
                | 
                | Represents an Abaqus smooth coupling (ABQSmoothCoupling)
                | object.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.abq_smooth_coupling = com_object

    @property
    def num_exclusion_regions(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property NumExclusionRegions() As long (Read Only)
                | 
                |     Retrieves the number of currently active exclusion regions.

        :rtype: int
        """

        return self.abq_smooth_coupling.NumExclusionRegions

    @property
    def num_supports(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property NumSupports() As long (Read Only)
                | 
                |     Retrieves the number of supports.

        :rtype: int
        """

        return self.abq_smooth_coupling.NumSupports

    @property
    def ur1(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property UR1() As boolean
                | 
                |     Returns or sets the UR1 degree of freedom.

        :rtype: bool
        """

        return self.abq_smooth_coupling.UR1

    @ur1.setter
    def ur1(self, value: bool):
        """
        :param bool value:
        """

        self.abq_smooth_coupling.UR1 = value

    @property
    def ur2(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property UR2() As boolean
                | 
                |     Returns or sets the UR2 degree of freedom.

        :rtype: bool
        """

        return self.abq_smooth_coupling.UR2

    @ur2.setter
    def ur2(self, value: bool):
        """
        :param bool value:
        """

        self.abq_smooth_coupling.UR2 = value

    @property
    def ur3(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property UR3() As boolean
                | 
                |     Returns or sets the UR3 degree of freedom.

        :rtype: bool
        """

        return self.abq_smooth_coupling.UR3

    @ur3.setter
    def ur3(self, value: bool):
        """
        :param bool value:
        """

        self.abq_smooth_coupling.UR3 = value

    @property
    def local_csys(self) -> AxisSystem:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property localCsys() As AxisSystem
                | 
                |     Returns or sets the local coordinate system. If nothing is passed in then
                |     it defaults to the global coordinate system.

        :rtype: AxisSystem
        """

        return AxisSystem(self.abq_smooth_coupling.localCsys)

    @local_csys.setter
    def local_csys(self, value: AxisSystem):
        """
        :param AxisSystem value:
        """

        self.abq_smooth_coupling.localCsys = value

    def add_support_from_publication(self, i_product: Product, i_publication: Publication) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub AddSupportFromPublication(Product iProduct,
                | Publication iPublication)
                | 
                |     Adds a support to the coupling. If the support already exists, it is
                |     removed from the coupling. If an attempt to remove the last support is made,
                |     the support is maintained and an error is returned.
                | 
                |     Parameters:
                | 
                |         iProduct
                |             The CATIA Product specifying the object to which the smooth
                |             coupling is applied.
                |         iPublication
                |             The CATIA Publication specifying the region to which the smooth
                |             coupling is applied.
                | 
                |             Refer: CATIAPublication

        :param Product i_product:
        :param Publication i_publication:
        :rtype: None
        """
        return self.abq_smooth_coupling.AddSupportFromPublication(i_product.com_object, i_publication.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'add_support_from_publication'
        # # vba_code = """
        # # Public Function add_support_from_publication(abq_smooth_coupling)
        # #     Dim iProduct (2)
        # #     abq_smooth_coupling.AddSupportFromPublication iProduct
        # #     add_support_from_publication = iProduct
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def add_support_from_reference(self, i_reference: Reference, i_support: Reference) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub AddSupportFromReference(Reference iReference,
                | Reference iSupport)
                | 
                |     AddSupportFromReference - adds a support to the coupling. If the support
                |     already exists, it is removed from the coupling. If an attempt to remove the
                |     last support is made, the support is maintained and an error is
                |     returned.
                | 
                |     Parameters:
                | 
                |         iReference
                |             The reference to the product as a CATIAReference. 
                |         iSupport
                |             The reference to the support as a CATIAReference.

        :param Reference i_reference:
        :param Reference i_support:
        :rtype: None
        """
        return self.abq_smooth_coupling.AddSupportFromReference(i_reference.com_object, i_support.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'add_support_from_reference'
        # # vba_code = """
        # # Public Function add_support_from_reference(abq_smooth_coupling)
        # #     Dim iReference (2)
        # #     abq_smooth_coupling.AddSupportFromReference iReference
        # #     add_support_from_reference = iReference
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def clear_exclusion_regions(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub ClearExclusionRegions()
                | 
                |     Clears the exclusion regions list.

        :rtype: None
        """
        return self.abq_smooth_coupling.ClearExclusionRegions()

    def clear_handler(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub ClearHandler()
                | 
                |     Clears the handler.

        :rtype: None
        """
        return self.abq_smooth_coupling.ClearHandler()

    def get_exclusion_regions(self, o_products: tuple, o_regions: tuple) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetExclusionRegions(CATSafeArrayVariant oProducts,
                | CATSafeArrayVariant oRegions)
                | 
                |     Returns the exclusion regions for the coupling. param oProducts Returned
                |     safe array of products for the excluded region, as CATIAReferences. This array
                |     has a one-to-one mapping with the regions array.
                | 
                |     Parameters:
                | 
                |         oRegions
                |             Returned safe array of regions to exclude, as CATIAReferences. This
                |             array has a one-to-one mapping with the products
                |             array.

        :param tuple o_products:
        :param tuple o_regions:
        :rtype: None
        """
        return self.abq_smooth_coupling.GetExclusionRegions(o_products, o_regions)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_exclusion_regions'
        # # vba_code = """
        # # Public Function get_exclusion_regions(abq_smooth_coupling)
        # #     Dim oProducts (2)
        # #     abq_smooth_coupling.GetExclusionRegions oProducts
        # #     get_exclusion_regions = oProducts
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_handler(self, o_product: Reference, o_ref: Reference) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetHandler(Reference oProduct,
                | Reference oRef)
                | 
                |     Returns the handler for the coupling.
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
        return self.abq_smooth_coupling.GetHandler(o_product.com_object, o_ref.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_handler'
        # # vba_code = """
        # # Public Function get_handler(abq_smooth_coupling)
        # #     Dim oProduct (2)
        # #     abq_smooth_coupling.GetHandler oProduct
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
                |     Gets the published local coordinate system of for the
                |     coupling.
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
        return self.abq_smooth_coupling.GetLocalCsysFromPublication(o_product.com_object, o_pub_axis_system.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_local_csys_from_publication'
        # # vba_code = """
        # # Public Function get_local_csys_from_publication(abq_smooth_coupling)
        # #     Dim oProduct (2)
        # #     abq_smooth_coupling.GetLocalCsysFromPublication oProduct
        # #     get_local_csys_from_publication = oProduct
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_supports(self, o_products: tuple, o_supports: tuple) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetSupports(CATSafeArrayVariant oProducts,
                | CATSafeArrayVariant oSupports)
                | 
                |     Returns the supports for the coupling.
                | 
                |     Parameters:
                | 
                |         oProducts
                |             Returned safe array of products for the supports, as
                |             CATIAReferences. This array has a one-to-one mapping with the supports array.
                |             
                |         oSupports
                |             Returned safe array of supports, as CATIAReferences. This array has
                |             a one-to-one mapping with the products array.

        :param tuple o_products:
        :param tuple o_supports:
        :rtype: None
        """
        return self.abq_smooth_coupling.GetSupports(o_products, o_supports)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_supports'
        # # vba_code = """
        # # Public Function get_supports(abq_smooth_coupling)
        # #     Dim oProducts (2)
        # #     abq_smooth_coupling.GetSupports oProducts
        # #     get_supports = oProducts
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_exclusion_regions(self, i_products: tuple, i_regions: tuple) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetExclusionRegions(CATSafeArrayVariant iProducts,
                | CATSafeArrayVariant iRegions)
                | 
                |     Sets the exclusion regions for the coupling. Any previously set exclusion
                |     regions will be replaced with this new list. The list of excluded regions can
                |     be cleared by passing in two empty lists for the products and the regions.
                |     Note: null values for products and regions are not
                |     accepted.
                | 
                |     Parameters:
                | 
                |         iProducts
                |             Safe array of products for the excluded region, as CATIAReferences.
                |             This array has a one-to-one mapping with the regions array.
                |             
                |         iRegions
                |             Safe array of regions to exclude, as CATIAReferences. This array
                |             has a one-to-one mapping with the products array.

        :param tuple i_products:
        :param tuple i_regions:
        :rtype: None
        """
        return self.abq_smooth_coupling.SetExclusionRegions(i_products, i_regions)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_exclusion_regions'
        # # vba_code = """
        # # Public Function set_exclusion_regions(abq_smooth_coupling)
        # #     Dim iProducts (2)
        # #     abq_smooth_coupling.SetExclusionRegions iProducts
        # #     set_exclusion_regions = iProducts
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_handler(self, i_product: Reference, i_ref: Reference) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetHandler(Reference iProduct,
                | Reference iRef)
                | 
                |     Sets the handler for the coupling. Any previously set handler will be
                |     replaced with this new value.
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
        return self.abq_smooth_coupling.SetHandler(i_product.com_object, i_ref.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_handler'
        # # vba_code = """
        # # Public Function set_handler(abq_smooth_coupling)
        # #     Dim iProduct (2)
        # #     abq_smooth_coupling.SetHandler iProduct
        # #     set_handler = iProduct
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_handler_from_publication(self, i_product: Product, i_publication: Publication) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetHandlerFromPublication(Product iProduct,
                | Publication iPublication)
                | 
                |     Sets the handler for the coupling. Any previously set handler will be
                |     replaced with this new value.
                | 
                |     Parameters:
                | 
                |         iProduct
                |             The CATIA Product for handeler.
                |         iPublication
                |             The CATIA Publication for handeler.
                | 
                |             Refer: CATIAPublication

        :param Product i_product:
        :param Publication i_publication:
        :rtype: None
        """
        return self.abq_smooth_coupling.SetHandlerFromPublication(i_product.com_object, i_publication.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_handler_from_publication'
        # # vba_code = """
        # # Public Function set_handler_from_publication(abq_smooth_coupling)
        # #     Dim iProduct (2)
        # #     abq_smooth_coupling.SetHandlerFromPublication iProduct
        # #     set_handler_from_publication = iProduct
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
                |     Sets the published local coordinate system for the coupling. Fails if the
                |     publication is not an axis system.
                | 
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
        return self.abq_smooth_coupling.SetLocalCsysFromPublication(i_product.com_object, i_pub_axis_system.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_local_csys_from_publication'
        # # vba_code = """
        # # Public Function set_local_csys_from_publication(abq_smooth_coupling)
        # #     Dim iProduct (2)
        # #     abq_smooth_coupling.SetLocalCsysFromPublication iProduct
        # #     set_local_csys_from_publication = iProduct
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_supports(self, i_products: tuple, i_regions: tuple) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetSupports(CATSafeArrayVariant iProducts,
                | CATSafeArrayVariant iRegions)
                | 
                |     Sets the support regions for the coupling. Any previously set support
                |     regions will be replaced with this new list. At least one item in the list is
                |     required.
                | 
                |     Parameters:
                | 
                |         iProducts
                |             Safe array of products for the support region as CATIAReferences.
                |             This array has a one-to-one mapping with the regions array.
                |             
                |         iRegions
                |             Safe array of supports as CATIAReferences. This array has a
                |             one-to-one mapping with the products array.

        :param tuple i_products:
        :param tuple i_regions:
        :rtype: None
        """
        return self.abq_smooth_coupling.SetSupports(i_products, i_regions)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_supports'
        # # vba_code = """
        # # Public Function set_supports(abq_smooth_coupling)
        # #     Dim iProducts (2)
        # #     abq_smooth_coupling.SetSupports iProducts
        # #     set_supports = iProducts
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'ABQSmoothCoupling(name="{self.name}")'
