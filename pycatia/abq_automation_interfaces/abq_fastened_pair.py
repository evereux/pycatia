#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.abq_automation_interfaces.abq_interaction import ABQInteraction
from pycatia.analysis_interfaces.analysis_entity import AnalysisEntity
from pycatia.mec_mod_interfaces.constraint import Constraint
from pycatia.product_structure_interfaces.product import Product


class ABQFastenedPair(ABQInteraction):
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
                |                         ABQFastenedPair
                | 
                | Represents an Abaqus Fastened Pair (ABQFastenedPair) object.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.abq_fastened_pair = com_object

    @property
    def adjust_slave_node(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property AdjustSlaveNode() As boolean
                | 
                |     Sets or returns the adjust slave node flag.

        :rtype: bool
        """

        return self.abq_fastened_pair.AdjustSlaveNode

    @adjust_slave_node.setter
    def adjust_slave_node(self, value: bool):
        """
        :param bool value:
        """

        self.abq_fastened_pair.AdjustSlaveNode = value

    @property
    def connection_property(self) -> AnalysisEntity:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ConnectionProperty() As AnalysisEntity
                | 
                |     This property has been deprecated. Use the AddSupportFromAnalysisEntity
                |     instead.

        :rtype: AnalysisEntity
        """

        return AnalysisEntity(self.abq_fastened_pair.ConnectionProperty)

    @connection_property.setter
    def connection_property(self, value: AnalysisEntity):
        """
        :param AnalysisEntity value:
        """

        self.abq_fastened_pair.ConnectionProperty = value

    @property
    def formulation_option(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property FormulationOption() As FormulationOption_Type
                | 
                |     Sets or returns the formulation option.
                | 
                |     Returns:
                |         The formulation option.
                | 
                |         Legal values:
                | 
                |         SOLVERDEFAULT
                |         SURFACETOSURFACE
                |         NODETOSURFACE

        :return: enum formulation_option_type
        :rtype: int
        """

        return self.abq_fastened_pair.FormulationOption

    @formulation_option.setter
    def formulation_option(self, value: int):
        """
        :param int value: enum formulation_option_type
        """

        self.abq_fastened_pair.FormulationOption = value

    @property
    def include_shell_thickness(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property IncludeShellThickness() As boolean
                | 
                |     Sets or returns the include shell element thickness flag.

        :rtype: bool
        """

        return self.abq_fastened_pair.IncludeShellThickness

    @include_shell_thickness.setter
    def include_shell_thickness(self, value: bool):
        """
        :param bool value:
        """

        self.abq_fastened_pair.IncludeShellThickness = value

    @property
    def invert_master_surface(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property InvertMasterSurface() As boolean
                | 
                |     Sets or returns the invert master surface flag.

        :rtype: bool
        """

        return self.abq_fastened_pair.InvertMasterSurface

    @invert_master_surface.setter
    def invert_master_surface(self, value: bool):
        """
        :param bool value:
        """

        self.abq_fastened_pair.InvertMasterSurface = value

    @property
    def invert_slave_surface(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property InvertSlaveSurface() As boolean
                | 
                |     Sets or returns the invert slave surface flag.

        :rtype: bool
        """

        return self.abq_fastened_pair.InvertSlaveSurface

    @invert_slave_surface.setter
    def invert_slave_surface(self, value: bool):
        """
        :param bool value:
        """

        self.abq_fastened_pair.InvertSlaveSurface = value

    @property
    def position_tolerance(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property PositionTolerance() As PositionTolerance_Type
                | 
                |     Sets or returns the position tolerance.
                | 
                |     Returns:
                |         The position tolerance
                | 
                |         Legal values:
                | 
                |         COMPUTED
                |         SPECIFIED

        :return: enum position_tolerance_type
        :rtype: int
        """

        return self.abq_fastened_pair.PositionTolerance

    @position_tolerance.setter
    def position_tolerance(self, value: int):
        """
        :param int value: enum position_tolerance_type
        """

        self.abq_fastened_pair.PositionTolerance = value

    @property
    def position_tolerance_val(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property PositionToleranceVal() As double
                | 
                |     Sets or returns the position tolerance value.

        :rtype: float
        """

        return self.abq_fastened_pair.PositionToleranceVal

    @position_tolerance_val.setter
    def position_tolerance_val(self, value: float):
        """
        :param float value:
        """

        self.abq_fastened_pair.PositionToleranceVal = value

    @property
    def swap_master_slave(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property SwapMasterSlave() As boolean
                | 
                |     Sets or returns the swap master/slave surface flag.

        :rtype: bool
        """

        return self.abq_fastened_pair.SwapMasterSlave

    @swap_master_slave.setter
    def swap_master_slave(self, value: bool):
        """
        :param bool value:
        """

        self.abq_fastened_pair.SwapMasterSlave = value

    def add_support_from_analysis_entity(self, i_product: Product, i_entity: AnalysisEntity) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub AddSupportFromAnalysisEntity(Product iProduct,
                | AnalysisEntity iEntity)
                | 
                |     Creates a new support and adds it to the description of the Analysis
                |     Entity.
                | 
                |     Parameters:
                | 
                |         iProduct
                |             The CATIA Product specifying the object to which the contact is
                |             applied.
                |         iEntity
                |             The CATIA Analysis Entity specifying the region to which the
                |             contact is applied.

        :param Product i_product:
        :param AnalysisEntity i_entity:
        :rtype: None
        """
        return self.abq_fastened_pair.AddSupportFromAnalysisEntity(i_product.com_object, i_entity.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'add_support_from_analysis_entity'
        # # vba_code = """
        # # Public Function add_support_from_analysis_entity(abq_fastened_pair)
        # #     Dim iProduct (2)
        # #     abq_fastened_pair.AddSupportFromAnalysisEntity iProduct
        # #     add_support_from_analysis_entity = iProduct
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def add_support_from_constraint(self, i_product: Product, i_constraint: Constraint) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub AddSupportFromConstraint(Product iProduct,
                | Constraint iConstraint)
                | 
                |     Creates a new support and adds it to the description of the Analysis
                |     Entity.
                | 
                |     Parameters:
                | 
                |         iProduct
                |             The CATIA Product specifying the object to which the contact is
                |             applied.
                |         iConstraint
                |             The CATIA Constraint specifying the region to which the contact is
                |             applied.

        :param Product i_product:
        :param Constraint i_constraint:
        :rtype: None
        """
        return self.abq_fastened_pair.AddSupportFromConstraint(i_product.com_object, i_constraint.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'add_support_from_constraint'
        # # vba_code = """
        # # Public Function add_support_from_constraint(abq_fastened_pair)
        # #     Dim iProduct (2)
        # #     abq_fastened_pair.AddSupportFromConstraint iProduct
        # #     add_support_from_constraint = iProduct
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'ABQFastenedPair(name="{self.name}")'
