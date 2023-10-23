#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.abq_automation_interfaces.abq_smooth_step_amplitude import ABQSmoothStepAmplitude
from pycatia.abq_automation_interfaces.abq_tabular_amplitude import ABQTabularAmplitude
from pycatia.analysis_interfaces.analysis_supports import AnalysisSupports
from pycatia.in_interfaces.reference import Reference
from pycatia.product_structure_interfaces.product import Product
from pycatia.product_structure_interfaces.publication import Publication
from pycatia.system_interfaces.any_object import AnyObject


class ABQBoundaryCondition(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     ABQBoundaryCondition
                | 
                | Represents the base interface for Abaqus boundary condition
                | objects.
                | Role: The ABQBoundaryCondition interface manages the common properties of any
                | boundary condition.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.abq_boundary_condition = com_object

    @property
    def activation_status(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ActivationStatus() As boolean
                | 
                |     Sets or Returns a boolean indicating whether the boundary condition is
                |     activated.
                | 
                |     Returns:
                |         The activation status.

        :rtype: bool
        """

        return self.abq_boundary_condition.ActivationStatus

    @activation_status.setter
    def activation_status(self, value: bool):
        """
        :param bool value:
        """

        self.abq_boundary_condition.ActivationStatus = value

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

        return self.abq_boundary_condition.ApplyUserSubroutine

    @apply_user_subroutine.setter
    def apply_user_subroutine(self, value: bool):
        """
        :param bool value:
        """

        self.abq_boundary_condition.ApplyUserSubroutine = value

    @property
    def regions(self) -> AnalysisSupports:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Regions() As AnalysisSupports (Read Only)
                | 
                |     Returns the region to which the boundary condition is
                |     applied.
                | 
                |     Returns:
                |         The region

        :rtype: AnalysisSupports
        """

        return AnalysisSupports(self.abq_boundary_condition.Regions)

    @property
    def smooth_amplitude(self) -> ABQSmoothStepAmplitude:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property SmoothAmplitude() As ABQSmoothStepAmplitude
                | 
                |     Sets or returns the Smooth Amplitude, given the reference of the Smooth
                |     amplitude.
                | 
                |     Returns:
                |         The amplitude object.

        :rtype: ABQSmoothStepAmplitude
        """

        return ABQSmoothStepAmplitude(self.abq_boundary_condition.SmoothAmplitude)

    @smooth_amplitude.setter
    def smooth_amplitude(self, value: ABQSmoothStepAmplitude):
        """
        :param ABQSmoothStepAmplitude value:
        """

        self.abq_boundary_condition.SmoothAmplitude = value

    @property
    def status(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Status() As CATBSTR (Read Only)
                | 
                |     Returns the propagating status of the boundary condition.
                | 
                |     Returns:
                |         The propagating status for example: if the boundary condition feature
                |         is created, it will return "CREATED" if the boundary condition feature is
                |         propagated from previous step, it will return "PROPAGATED"

        :rtype: str
        """

        return self.abq_boundary_condition.Status

    @property
    def tabular_amplitude(self) -> ABQTabularAmplitude:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property TabularAmplitude() As ABQTabularAmplitude
                | 
                |     Sets or returns the amplitude, given the Tabular amplitude
                |     reference.
                | 
                |     Returns:
                |         The amplitude object.

        :rtype: ABQTabularAmplitude
        """

        return ABQTabularAmplitude(self.abq_boundary_condition.TabularAmplitude)

    @tabular_amplitude.setter
    def tabular_amplitude(self, value: ABQTabularAmplitude):
        """
        :param ABQTabularAmplitude value:
        """

        self.abq_boundary_condition.TabularAmplitude = value

    @property
    def type(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Type() As CATBSTR (Read Only)
                | 
                |     Returns the type of the boundary condition.
                | 
                |     Returns:
                |         The type of the boundary condition

        :rtype: str
        """

        return self.abq_boundary_condition.Type

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
                |             The CATIA Product specifying the object to which the boundary
                |             condition is applied.
                |         iSupport
                |             The CATIA Reference specifying the region to which the boundary
                |             condition is applied.
                | 
                |             Refer: CATIAReference, CATIAProduct

        :param Product i_product:
        :param Reference i_support:
        :rtype: None
        """
        return self.abq_boundary_condition.AddSupportFromProduct(i_product.com_object, i_support.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'add_support_from_product'
        # # vba_code = """
        # # Public Function add_support_from_product(abq_boundary_condition)
        # #     Dim iProduct (2)
        # #     abq_boundary_condition.AddSupportFromProduct iProduct
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
                |             The CATIA Product specifying the object to which the boundary
                |             condition is applied.
                |         iPublication
                |             The CATIA Publication specifying the region to which the boundary
                |             condition is applied.
                | 
                |             Refer: CATIAPublication

        :param Product i_product:
        :param Publication i_publication:
        :rtype: None
        """
        return self.abq_boundary_condition.AddSupportFromPublication(i_product.com_object, i_publication.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'add_support_from_publication'
        # # vba_code = """
        # # Public Function add_support_from_publication(abq_boundary_condition)
        # #     Dim iProduct (2)
        # #     abq_boundary_condition.AddSupportFromPublication iProduct
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
                |             The CATIA Reference specifying the object to which the boundary
                |             condition is applied.
                |         iSupport
                |             The CATIA Reference specifying the region to which the boundary
                |             condition is applied.
                | 
                |             Refer: CATIAReference

        :param Reference i_reference:
        :param Reference i_support:
        :rtype: None
        """
        return self.abq_boundary_condition.AddSupportFromReference(i_reference.com_object, i_support.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'add_support_from_reference'
        # # vba_code = """
        # # Public Function add_support_from_reference(abq_boundary_condition)
        # #     Dim iReference (2)
        # #     abq_boundary_condition.AddSupportFromReference iReference
        # #     add_support_from_reference = iReference
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'ABQBoundaryCondition(name="{self.name}")'
