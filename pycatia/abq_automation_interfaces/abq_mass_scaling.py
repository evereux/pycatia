#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.in_interfaces.reference import Reference
from pycatia.mec_mod_interfaces.body import Body
from pycatia.product_structure_interfaces.product import Product
from pycatia.product_structure_interfaces.publication import Publication
from pycatia.system_interfaces.any_object import AnyObject


class ABQMassScaling(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     ABQMassScaling
                | 
                | Represents an Abaqus Mass Scaling entity.
                | 
                | Role: Used to access the properties of a Mass Scaling entity.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.abq_mass_scaling = com_object

    @property
    def frequency_increment(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property FrequencyIncrement() As long
                | 
                |     Sets or returns the scaling frequency increment. Applies only when
                |     FrequencyType is ABQ_INCREMENT.

        :rtype: int
        """

        return self.abq_mass_scaling.FrequencyIncrement

    @frequency_increment.setter
    def frequency_increment(self, value: int):
        """
        :param int value:
        """

        self.abq_mass_scaling.FrequencyIncrement = value

    @property
    def frequency_interval(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property FrequencyInterval() As long
                | 
                |     Sets or returns the scaling frequency interval. Applies only when
                |     FrequencyType is ABQ_INTERVAL.

        :rtype: int
        """

        return self.abq_mass_scaling.FrequencyInterval

    @frequency_interval.setter
    def frequency_interval(self, value: int):
        """
        :param int value:
        """

        self.abq_mass_scaling.FrequencyInterval = value

    @property
    def frequency_type(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property FrequencyType() As AbqMsFrequencyType
                | 
                |     Sets or returns the scaling frequency type.

        :return: enum abq_ms_frequency_type
        :rtype: int
        """

        return self.abq_mass_scaling.FrequencyType

    @frequency_type.setter
    def frequency_type(self, value: int):
        """
        :param int value:
        """

        self.abq_mass_scaling.FrequencyType = value

    @property
    def global_(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Global() As boolean
                | 
                |     Sets or returns whether the mass scaling is global.

        :rtype: bool
        """

        return self.abq_mass_scaling.Global

    @global_.setter
    def global_(self, value: bool):
        """
        :param bool value:
        """

        self.abq_mass_scaling.Global = value

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

        return self.abq_mass_scaling.NumSupports

    @property
    def scale_factor(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ScaleFactor() As double
                | 
                |     Sets or returns the scale factor.

        :rtype: float
        """

        return self.abq_mass_scaling.ScaleFactor

    @scale_factor.setter
    def scale_factor(self, value: float):
        """
        :param float value:
        """

        self.abq_mass_scaling.ScaleFactor = value

    @property
    def scale_factor_on(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ScaleFactorOn() As boolean
                | 
                |     Sets or returns whether the scale factor is active.

        :rtype: bool
        """

        return self.abq_mass_scaling.ScaleFactorOn

    @scale_factor_on.setter
    def scale_factor_on(self, value: bool):
        """
        :param bool value:
        """

        self.abq_mass_scaling.ScaleFactorOn = value

    @property
    def target_method(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property TargetMethod() As AbqMsTargetMethod
                | 
                |     Sets or returns the target time scaling method. Applies only when target
                |     time is active.

        :return: enum abq_ms_target_method
        :rtype: int
        """

        return self.abq_mass_scaling.TargetMethod

    @target_method.setter
    def target_method(self, value: int):
        """
        :param int value:
        """

        self.abq_mass_scaling.TargetMethod = value

    @property
    def target_time(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property TargetTime() As double
                | 
                |     Sets or returns the scaling target time.

        :rtype: float
        """

        return self.abq_mass_scaling.TargetTime

    @target_time.setter
    def target_time(self, value: float):
        """
        :param float value:
        """

        self.abq_mass_scaling.TargetTime = value

    @property
    def target_time_on(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property TargetTimeOn() As boolean
                | 
                |     Sets or returns whether the target time scaling is active.

        :rtype: bool
        """

        return self.abq_mass_scaling.TargetTimeOn

    @target_time_on.setter
    def target_time_on(self, value: bool):
        """
        :param bool value:
        """

        self.abq_mass_scaling.TargetTimeOn = value

    @property
    def variable(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Variable() As boolean
                | 
                |     Sets or returns whether the mass scaling is variable.

        :rtype: bool
        """

        return self.abq_mass_scaling.Variable

    @variable.setter
    def variable(self, value: bool):
        """
        :param bool value:
        """

        self.abq_mass_scaling.Variable = value

    def add_support_for_body(self, i_product: Product, i_body: Body) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub AddSupportForBody(Product iProduct,
                | Body iBody)
                | 
                |     Adds the specified body as a support.
                | 
                |     Parameters:
                | 
                |         iProduct
                |             The CATIAProduct specifying the positioning object.
                |             
                |         iBody
                |             The CATIABody to serve as the support.
                |             Refer: CATIABody , CATIAProduct

        :param Product i_product:
        :param Body i_body:
        :rtype: None
        """
        return self.abq_mass_scaling.AddSupportForBody(i_product.com_object, i_body.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'add_support_for_body'
        # # vba_code = """
        # # Public Function add_support_for_body(abq_mass_scaling)
        # #     Dim iProduct (2)
        # #     abq_mass_scaling.AddSupportForBody iProduct
        # #     add_support_for_body = iProduct
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def add_support_from_product(self, i_product: Product, i_support: Reference) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub AddSupportFromProduct(Product iProduct,
                | Reference iSupport)
                | 
                |     Adds the specified product reference as a support. If the support already
                |     exists then it is removed.
                | 
                |     Parameters:
                | 
                |         iProduct
                |             The CATIAProduct specifying the positioning object.
                |             
                |         iSupport
                |             The CATIAReference to serve as the support.

        :param Product i_product:
        :param Reference i_support:
        :rtype: None
        """
        return self.abq_mass_scaling.AddSupportFromProduct(i_product.com_object, i_support.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'add_support_from_product'
        # # vba_code = """
        # # Public Function add_support_from_product(abq_mass_scaling)
        # #     Dim iProduct (2)
        # #     abq_mass_scaling.AddSupportFromProduct iProduct
        # #     add_support_from_product = iProduct
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def add_support_from_publication(self, i_product: Product, i_publication: Publication) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub AddSupportFromPublication(Product iProduct,
                | Publication iPublication)
                | 
                |     Adds a support from the publication. If the support already exists, it is
                |     removed.
                | 
                |     Parameters:
                | 
                |         iProduct
                |             The CATIA Product specifying the object to which the mass scaling
                |             is applied.
                |         iPublication
                |             The CATIA Publication specifying the region to which the mass
                |             scaling is applied.
                | 
                |             Refer: CATIAPublication

        :param Product i_product:
        :param Publication i_publication:
        :rtype: None
        """
        return self.abq_mass_scaling.AddSupportFromPublication(i_product.com_object, i_publication.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'add_support_from_publication'
        # # vba_code = """
        # # Public Function add_support_from_publication(abq_mass_scaling)
        # #     Dim iProduct (2)
        # #     abq_mass_scaling.AddSupportFromPublication iProduct
        # #     add_support_from_publication = iProduct
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def clear_supports(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub ClearSupports()
                | 
                |     Clear the list of supports.

        :rtype: None
        """
        return self.abq_mass_scaling.ClearSupports()

    def get_supports(self, o_products: tuple, o_supports: tuple) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetSupports(CATSafeArrayVariant oProducts,
                | CATSafeArrayVariant oSupports)
                | 
                |     Gets the supports that define the mass scaling region(s).
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
        return self.abq_mass_scaling.GetSupports(o_products, o_supports)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_supports'
        # # vba_code = """
        # # Public Function get_supports(abq_mass_scaling)
        # #     Dim oProducts (2)
        # #     abq_mass_scaling.GetSupports oProducts
        # #     get_supports = oProducts
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_supports(self, i_products: tuple, i_supports: tuple) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetSupports(CATSafeArrayVariant iProducts,
                | CATSafeArrayVariant iSupports)
                | 
                |     Sets the supports that define the mass scaling region(s). Any previously
                |     set support regions will be replaced with this new list. The list must contain
                |     at least one item.
                | 
                |     Parameters:
                | 
                |         iProducts
                |             Safe array of products for the supports as CATIAReferences. This
                |             array has a one-to-one mapping with the supports array.
                |             
                |         iSupports
                |             Safe array of supports as CATIAReferences. This array has a
                |             one-to-one mapping with the products array.

        :param tuple i_products:
        :param tuple i_supports:
        :rtype: None
        """
        return self.abq_mass_scaling.SetSupports(i_products, i_supports)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_supports'
        # # vba_code = """
        # # Public Function set_supports(abq_mass_scaling)
        # #     Dim iProducts (2)
        # #     abq_mass_scaling.SetSupports iProducts
        # #     set_supports = iProducts
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'ABQMassScaling(name="{self.name}")'
