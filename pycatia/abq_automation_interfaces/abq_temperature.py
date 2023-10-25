#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.abq_automation_interfaces.abq_job import ABQJob
from pycatia.in_interfaces.reference import Reference
from pycatia.product_structure_interfaces.product import Product
from pycatia.product_structure_interfaces.publication import Publication
from pycatia.system_interfaces.any_object import AnyObject


class ABQTemperature(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     ABQTemperature
                | 
                | Represents an Abaqus temperature object (ABQTemperature).
                | Role: Access an Abaqus temperature object or determine its properties. It has
                | common properties of ABQInitialTemperature,
                | ABQTemperatureHistory
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.abq_temperature = com_object

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

        return self.abq_temperature.ApplyUserSubroutine

    @apply_user_subroutine.setter
    def apply_user_subroutine(self, value: bool):
        """
        :param bool value:
        """

        self.abq_temperature.ApplyUserSubroutine = value

    @property
    def distribution(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Distribution() As Distribution_Type
                | 
                |     Sets or returns the distribution type associated with this temperature
                |     field.
                | 
                |       
                |     Legal values:
                |      UNIFORM
                |      JOB 
                |      USERDEFINED 
                |      JOB_USERDEFINED
                |      
                | 
                |     Example:
                |         This example sets the distribution type to
                |         USERDEFINED.
                | 
                |          Dim abqTemperature As ABQTemperature
                |          abqTemperature.Distribution = USERDEFINED

        :return: enum distribution_type
        :rtype: int
        """

        return self.abq_temperature.Distribution

    @distribution.setter
    def distribution(self, value: int):
        """
        :param int value:
        """

        self.abq_temperature.Distribution = value

    @property
    def job(self) -> ABQJob:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Job() As ABQJob
                | 
                |     Sets or returns the Abaqus job associated with this temperature field. *
                |     The job being attached to the temperature field must belong to a thermal case
                |     and must not belong to same analysis case to which the temperature field
                |     belongs.
                | 
                |     Example:
                |         This example retrieves the ABQJob abqJob.
                | 
                |          Dim abqTemperature As ABQTemperature
                |          Dim abqJob As ABQJob 
                |          Set abqJob = abqTemperature.Job

        :rtype: ABQJob
        """

        return ABQJob(self.abq_temperature.Job)

    @job.setter
    def job(self, value: ABQJob):
        """
        :param ABQJob value:
        """

        self.abq_temperature.Job = value

    @property
    def magnitude(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Magnitude() As double
                | 
                |     Sets or returns the magnitude of the temperature field.
                | 
                |     Returns:
                |         The magnitude of the temperature field.

        :rtype: float
        """

        return self.abq_temperature.Magnitude

    @magnitude.setter
    def magnitude(self, value: float):
        """
        :param float value:
        """

        self.abq_temperature.Magnitude = value

    @property
    def type(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Type() As CATBSTR (Read Only)
                | 
                |     Returns the type of the Temperature.
                | 
                |     Returns:
                |         The type of the Temperature.

        :rtype: str
        """

        return self.abq_temperature.Type

    def add_support_from_product(self, i_product: Product, i_support: Reference) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub AddSupportFromProduct(Product iProduct,
                | Reference iSupport)
                | 
                |     This adds the support from a product to the Field.
                | 
                |     Parameters:
                | 
                |         iProduct
                |             The CATIA Product specifying the object to which the field is
                |             applied.
                |         iSupport
                |             The CATIA Reference specifying the region to which the field is
                |             applied.
                |             Refer: CATIAReference , CATIAProduct

        :param Product i_product:
        :param Reference i_support:
        :rtype: None
        """
        return self.abq_temperature.AddSupportFromProduct(i_product.com_object, i_support.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'add_support_from_product'
        # # vba_code = """
        # # Public Function add_support_from_product(abq_temperature)
        # #     Dim iProduct (2)
        # #     abq_temperature.AddSupportFromProduct iProduct
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
                |             The CATIA Product specifying the object to which the field is
                |             applied.
                |         iPublication
                |             The CATIA Publication specifying the region to which the field is
                |             applied.
                | 
                |             Refer: CATIAPublication

        :param Product i_product:
        :param Publication i_publication:
        :rtype: None
        """
        return self.abq_temperature.AddSupportFromPublication(i_product.com_object, i_publication.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'add_support_from_publication'
        # # vba_code = """
        # # Public Function add_support_from_publication(abq_temperature)
        # #     Dim iProduct (2)
        # #     abq_temperature.AddSupportFromPublication iProduct
        # #     add_support_from_publication = iProduct
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'ABQTemperature(name="{self.name}")'
