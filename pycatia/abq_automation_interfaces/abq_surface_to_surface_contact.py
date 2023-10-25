#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.abq_automation_interfaces.abq_interaction import ABQInteraction
from pycatia.abq_automation_interfaces.abq_property import ABQProperty
from pycatia.analysis_interfaces.analysis_entity import AnalysisEntity
from pycatia.in_interfaces.reference import Reference
from pycatia.mec_mod_interfaces.constraint import Constraint
from pycatia.product_structure_interfaces.product import Product


class ABQSurfaceToSurfaceContact(ABQInteraction):
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
                |                         ABQSurfaceToSurfaceContact
                | 
                | Represents an Abaqus contact pair (ABQSurfaceToSurfaceContact)
                | object.
                | Role: Access an Abaqus contact pair object or determine its
                | properties.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.abq_surface_to_surface_contact = com_object

    @property
    def adjust_method(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property AdjustMethod() As AdjustMethod_Type
                | 
                |     Sets or returns the method type in a contact pair.
                | 
                |     Returns:
                |         The method type.
                | 
                |         Legal values:
                | 
                |         OVERCLOSED
                |         TOLERANCE

        :return: enum adjust_method_type
        :rtype: int
        """

        return self.abq_surface_to_surface_contact.AdjustMethod

    @adjust_method.setter
    def adjust_method(self, value: int):
        """
        :param int value: enum adjust_method_type
        """

        self.abq_surface_to_surface_contact.AdjustMethod = value

    @property
    def adjust_tolerance_val(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property AdjustToleranceVal() As double
                | 
                |     Sets or returns the tolerance value of the contact pair.
                | 
                |     Returns:
                |         The tolerance value of the contact pair.

        :rtype: float
        """

        return self.abq_surface_to_surface_contact.AdjustToleranceVal

    @adjust_tolerance_val.setter
    def adjust_tolerance_val(self, value: float):
        """
        :param float value:
        """

        self.abq_surface_to_surface_contact.AdjustToleranceVal = value

    @property
    def connection_property(self) -> AnalysisEntity:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ConnectionProperty() As AnalysisEntity
                | 
                |     Sets or returns the connection property in a contact pair.
                | 
                |     Returns:
                |         The connection property.

        :rtype: AnalysisEntity
        """

        return AnalysisEntity(self.abq_surface_to_surface_contact.ConnectionProperty)

    @connection_property.setter
    def connection_property(self, value: AnalysisEntity):
        """
        :param AnalysisEntity value:
        """

        self.abq_surface_to_surface_contact.ConnectionProperty = value

    @property
    def formulation_option(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property FormulationOption() As FormulationOption_Type
                | 
                |     Sets or returns the formulation option in a contact pair.
                | 
                |     Returns:
                |         Formulation option type.
                | 
                |         Legal values:
                | 
                |         SURFACETOSURFACE
                |         NODETOSURFACE

        :return: enum formulation_option_type
        :rtype: int
        """

        return self.abq_surface_to_surface_contact.FormulationOption

    @formulation_option.setter
    def formulation_option(self, value: int):
        """
        :param int value: enum formulation_option_type
        """

        self.abq_surface_to_surface_contact.FormulationOption = value

    @property
    def interaction_property(self) -> ABQProperty:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property InteractionProperty() As ABQProperty
                | 
                |     Sets or returns the interaction property in a contact
                |     pair.
                | 
                |     Returns:
                |         The specified ABQMechConnBehavior.

        :rtype: ABQProperty
        """

        return ABQProperty(self.abq_surface_to_surface_contact.InteractionProperty)

    @interaction_property.setter
    def interaction_property(self, value: ABQProperty):
        """
        :param ABQProperty value:
        """

        self.abq_surface_to_surface_contact.InteractionProperty = value

    @property
    def interference_fit(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property InterferenceFit() As double
                | 
                |     Assigns / gets interference fit of a contact pair. This can be assigned to
                |     contact pairs created in structual case except initialization
                |     step.
                | 
                |     Returns:
                |         The interference magnitude for gradual interference with uniform
                |         overclosure.
                |         returns 0 if no interference fit is defined. Usage: Dim abqSurfCont As ABQSurfaceToSurfaceContact Dim clearance As double Set clearance = 2.5 abqSurfCont.InterferenceFit = clearance

        :rtype: float
        """

        return self.abq_surface_to_surface_contact.InterferenceFit

    @interference_fit.setter
    def interference_fit(self, value: float):
        """
        :param float value:
        """

        self.abq_surface_to_surface_contact.InterferenceFit = value

    @property
    def interference_fit_amplitude(self) -> ABQProperty:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property InterferenceFitAmplitude() As ABQProperty
                | 
                |     Assigns / gets interference fit amplitude of a contact
                |     pair.
                | 
                |     Returns:
                |         The interference fit amplitude for gradual interference with uniform
                |         overclosure.
                |         returns NULL if no interference fit is defined.
                |         returns E_FAIL if unable to find amplitude object. Usage: Dim abqSurfCont As ABQSurfaceToSurfaceContact Dim clearance As double Set clearance = 2.5 abqSurfCont.InterferenceFit = clearance Dim Amp As ABQProperty ....(Get the amplitude property) abqSurfCont.InterferenceFitAmplitude = Amp;

        :rtype: ABQProperty
        """

        return ABQProperty(self.abq_surface_to_surface_contact.InterferenceFitAmplitude)

    @interference_fit_amplitude.setter
    def interference_fit_amplitude(self, value: ABQProperty):
        """
        :param ABQProperty value:
        """

        self.abq_surface_to_surface_contact.InterferenceFitAmplitude = value

    @property
    def sliding(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Sliding() As Sliding_Type
                | 
                |     Sets or returns the sliding type in a contact pair.
                | 
                |     Returns:
                |         The sliding type.
                | 
                |         Legal values:
                | 
                |         FINITE
                |         SMALL

        :return: enum sliding_type
        :rtype: int
        """

        return self.abq_surface_to_surface_contact.Sliding

    @sliding.setter
    def sliding(self, value: int):
        """
        :param int value: enum sliding_type
        """

        self.abq_surface_to_surface_contact.Sliding = value

    @property
    def swap_master_slave(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property SwapMasterSlave() As boolean
                | 
                |     Returns the activation status if the master surface is swapped as slave
                |     surface.
                | 
                |     Returns:
                |         A boolean specifying whether the master surface surface is swapped as
                |         slave.

        :rtype: bool
        """

        return self.abq_surface_to_surface_contact.SwapMasterSlave

    @swap_master_slave.setter
    def swap_master_slave(self, value: bool):
        """
        :param bool value:
        """

        self.abq_surface_to_surface_contact.SwapMasterSlave = value

    @property
    def use_automatic_geometry_smoothing(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property UseAutomaticGeometrySmoothing() As boolean
                | 
                |     Returns a boolean indicating whether automatic geometry smoothing is used
                |     for the contact pair
                | 
                |     Returns:
                |         boolean specifying whether automatic geometry smoothing is
                |         active.
                | 
                |         Legal values:
                | 
                |         TRUE
                |         FALSE

        :rtype: bool
        """

        return self.abq_surface_to_surface_contact.UseAutomaticGeometrySmoothing

    @use_automatic_geometry_smoothing.setter
    def use_automatic_geometry_smoothing(self, value: bool):
        """
        :param bool value:
        """

        self.abq_surface_to_surface_contact.UseAutomaticGeometrySmoothing = value

    @property
    def use_interference_fit_amplitude(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property UseInterferenceFitAmplitude() As boolean (Read
                | Only)
                | 
                |     Returns a boolean indicating whether amplitude is used in the interference
                |     fit for a contact pair
                | 
                |     Returns:
                |         boolean specifying whether user defined amplitude is active.

        :rtype: bool
        """

        return self.abq_surface_to_surface_contact.UseInterferenceFitAmplitude

    @property
    def use_master_negative_side(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property UseMasterNegativeSide() As boolean
                | 
                |     Returns the activation status if the master surface is specified as the
                |     negative side.
                | 
                |     Returns:
                |         A boolean specifying whether the master surface is specified as the
                |         negative side.

        :rtype: bool
        """

        return self.abq_surface_to_surface_contact.UseMasterNegativeSide

    @use_master_negative_side.setter
    def use_master_negative_side(self, value: bool):
        """
        :param bool value:
        """

        self.abq_surface_to_surface_contact.UseMasterNegativeSide = value

    @property
    def use_slave_negative_side(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property UseSlaveNegativeSide() As boolean
                | 
                |     Returns the activation status if the slave surface is specified as the
                |     negative side.
                | 
                |     Returns:
                |         A boolean specifying whether the slave surface is specified as the
                |         negative side.

        :rtype: bool
        """

        return self.abq_surface_to_surface_contact.UseSlaveNegativeSide

    @use_slave_negative_side.setter
    def use_slave_negative_side(self, value: bool):
        """
        :param bool value:
        """

        self.abq_surface_to_surface_contact.UseSlaveNegativeSide = value

    def add_support_from_constraint(self, i_reference: Product, i_support: Constraint) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub AddSupportFromConstraint(Product iReference,
                | Constraint iSupport)
                | 
                |     Creates a new support and adds it to the description of the Analysis
                |     Entity.
                | 
                |     Parameters:
                | 
                |         iProduct
                |             The CATIA Product specifying the object to which the contact is
                |             applied.
                |         iSupport
                |             The CATIA Constraint specifying the region to which the contact is
                |             applied.
                | 
                |             Refer: CATIAReference, CATIAProduct

        :param Product i_reference:
        :param Constraint i_support:
        :rtype: None
        """
        return self.abq_surface_to_surface_contact.AddSupportFromConstraint(
            i_reference.com_object,
            i_support.com_object
        )
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'add_support_from_constraint'
        # # vba_code = """
        # # Public Function add_support_from_constraint(abq_surface_to_surface_contact)
        # #     Dim iReference (2)
        # #     abq_surface_to_surface_contact.AddSupportFromConstraint iReference
        # #     add_support_from_constraint = iReference
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
                |             The CATIA Reference specifying the object to which the contact is
                |             applied.
                |         iSupport
                |             The CATIA Reference specifying the region to which the contact is
                |             applied.
                | 
                |             Refer: CATIAReference

        :param Reference i_reference:
        :param Reference i_support:
        :rtype: None
        """
        return self.abq_surface_to_surface_contact.AddSupportFromReference(i_reference.com_object, i_support.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'add_support_from_reference'
        # # vba_code = """
        # # Public Function add_support_from_reference(abq_surface_to_surface_contact)
        # #     Dim iReference (2)
        # #     abq_surface_to_surface_contact.AddSupportFromReference iReference
        # #     add_support_from_reference = iReference
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def remove_interference_fit(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub RemoveInterferenceFit()
                | 
                |     Removes interference fit from a contact pair feature.

        :rtype: None
        """
        return self.abq_surface_to_surface_contact.RemoveInterferenceFit()

    def __repr__(self):
        return f'ABQSurfaceToSurfaceContact(name="{self.name}")'
