#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.in_interfaces.reference import Reference
from pycatia.product_structure_interfaces.product import Product
from pycatia.product_structure_interfaces.publication import Publication
from pycatia.system_interfaces.any_object import AnyObject


class ABQOutputRequest(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     ABQOutputRequest
                | 
                | Represents the base interface for all output request objects.
                | Role: The ABQOutputRequest interface manages the common attributes of any
                | output requests.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.abq_output_request = com_object

    @property
    def activation_status(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ActivationStatus() As boolean
                | 
                |     Sets or returns the activation status.
                | 
                |     Returns:
                |         A boolean specifying whether the output request is activated or
                |         deactivated.

        :rtype: bool
        """

        return self.abq_output_request.ActivationStatus

    @activation_status.setter
    def activation_status(self, value: bool):
        """
        :param bool value:
        """

        self.abq_output_request.ActivationStatus = value

    @property
    def num_increment_frequency(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property NumIncrementFrequency(long iNumIncrementFrequency) (Write
                | Only)
                | 
                |     Sets request for output results at specified increment.

        :rtype: int
        """

        return self.abq_output_request.NumIncrementFrequency

    @num_increment_frequency.setter
    def num_increment_frequency(self, value: int):
        """
        :param int value:
        """

        self.abq_output_request.NumIncrementFrequency = value

    @property
    def status(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Status() As CATBSTR (Read Only)
                | 
                |     Returns the propagating status of the output request.
                | 
                |     Returns:
                |         The propagating status for example: if the output request feature is
                |         created, it will return "CREATED" if the output request feature is propagated
                |         from previous step, it will return "PROPAGATED" if the output request feature
                |         is modified in current step, it will return "MODIFIED"

        :rtype: str
        """

        return self.abq_output_request.Status

    @property
    def type(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Type() As CATBSTR (Read Only)
                | 
                |     Returns the type of the output request.
                | 
                |     Returns:
                |         The string representing the type of the output request.

        :rtype: str
        """

        return self.abq_output_request.Type

    @property
    def whole_model_as_supp(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property WholeModelAsSupp() As boolean
                | 
                |     Sets or returns whether the whole model is selected as support. A value of
                |     true indicates that the whole model is selected as
                |     support.
                | 
                |     Returns:
                |         A boolean specifying whether the whole model is selected as support.

        :rtype: bool
        """

        return self.abq_output_request.WholeModelAsSupp

    @whole_model_as_supp.setter
    def whole_model_as_supp(self, value: bool):
        """
        :param bool value:
        """

        self.abq_output_request.WholeModelAsSupp = value

    def add_support_from_product(self, i_product: Product, i_support: Reference) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub AddSupportFromProduct(Product iProduct,
                | Reference iSupport)
                | 
                |     Creates a new support and adds it to the description of the Analysis
                |     Entity.
                | 
                |     Parameters:
                | 
                |         iProduct
                |             The CATIA Product specifying the object to which the output request
                |             is applied.
                |         iSupport
                |             The CATIA Reference specifying the region to which the output
                |             request is applied.
                | 
                |             Refer: CATIAReference , CATIAProduct

        :param Product i_product:
        :param Reference i_support:
        :rtype: None
        """
        return self.abq_output_request.AddSupportFromProduct(i_product.com_object, i_support.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'add_support_from_product'
        # # vba_code = """
        # # Public Function add_support_from_product(abq_output_request)
        # #     Dim iProduct (2)
        # #     abq_output_request.AddSupportFromProduct iProduct
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
                |     Creates a new support and adds it to the description of the Analysis
                |     Entity.
                | 
                |     Parameters:
                | 
                |         iProduct
                |             The CATIA Product specifying the object to which the output request
                |             is applied.
                |         iPublication
                |             The CATIA Publication specifying the region to which the output
                |             request is applied.
                | 
                |             Refer: CATIAPublication

        :param Product i_product:
        :param Publication i_publication:
        :rtype: None
        """
        return self.abq_output_request.AddSupportFromPublication(i_product.com_object, i_publication.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'add_support_from_publication'
        # # vba_code = """
        # # Public Function add_support_from_publication(abq_output_request)
        # #     Dim iProduct (2)
        # #     abq_output_request.AddSupportFromPublication iProduct
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
                |     Creates a new support and adds it to the description of the Analysis
                |     Entity.
                | 
                |     Parameters:
                | 
                |         iReference
                |             The CATIA Reference specifying the object to which the output
                |             request is applied.
                |         iSupport
                |             The CATIA Reference specifying the region to which the output
                |             request is applied.
                | 
                |             Refer: CATIAReference

        :param Reference i_reference:
        :param Reference i_support:
        :rtype: None
        """
        return self.abq_output_request.AddSupportFromReference(i_reference.com_object, i_support.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'add_support_from_reference'
        # # vba_code = """
        # # Public Function add_support_from_reference(abq_output_request)
        # #     Dim iReference (2)
        # #     abq_output_request.AddSupportFromReference iReference
        # #     add_support_from_reference = iReference
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_output_at_last_increment(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetOutputAtLastIncrement()
                | 
                |     Sets request for output results at last increment.

        :rtype: None
        """
        return self.abq_output_request.SetOutputAtLastIncrement()

    def __repr__(self):
        return f'ABQOutputRequest(name="{self.name}")'
