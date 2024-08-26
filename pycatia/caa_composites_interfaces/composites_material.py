#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R31 on 2024-08-20 16:04:57.203445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.

"""
import inspect

from pycatia.system_interfaces.any_object import AnyObject


class CompositesMaterial(AnyObject):
    """

    Introduced in V5-6R2020.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2024-08-20 16:04:57.203445)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     CompositesMaterial
                |
                | Represents a Composites Material object.

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.composites_material = com_object

    @property
    def cured_thickness(self) -> float:
        """

        Introduced in V5-6R2020.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2024-08-20 16:04:57.203445)
                | Property CuredThickness() As double
                |     returns or set the cured thicknes defined in Composites tab in mm.

        :rtype: float
        """

        self.release_check(
            self.application.system_configuration.release,
            30,
            f'{self.__class__.__name__}.{inspect.stack()[0][3]}',
        )

        return self.composites_material.CuredThickness

    @cured_thickness.setter
    def cured_thickness(self, value: float):
        """
        :param float value:
        """

        self.composites_material.CuredThickness = value

    @property
    def fabric_width(self) -> float:
        """

        Introduced in V5-6R2020.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2024-08-20 16:04:57.203445)
                | Property FabricWidth() As double
                |     returns or set the fabric width defined in Composites tab in mm.

        :rtype: float
        """

        self.release_check(
            self.application.system_configuration.release,
            30,
            f'{self.__class__.__name__}.{inspect.stack()[0][3]}',
        )

        return self.composites_material.FabricWidth

    @fabric_width.setter
    def fabric_width(self, value: float):
        """
        :param float value:
        """

        self.composites_material.FabricWidth = value

    @property
    def limit_deformation(self) -> float:
        """

        Introduced in V5-6R2020.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2024-08-20 16:04:57.203445)
                | Property LimitDeformation() As double
                |     returns or set the limit deformation defined in Composites tab in radian.

        :rtype: float
        """

        self.release_check(
            self.application.system_configuration.release,
            30,
            f'{self.__class__.__name__}.{inspect.stack()[0][3]}',
        )

        return self.composites_material.LimitDeformation

    @limit_deformation.setter
    def limit_deformation(self, value: float):
        """
        :param float value:
        """

        self.composites_material.LimitDeformation = value

    @property
    def mass_cost(self) -> float:
        """

        Introduced in V5-6R2020.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2024-08-20 16:04:57.203445)
                | Property MassCost() As double
                |     returns or set the cost per mess defined in Composites tab in $ per kg.

        :rtype: float
        """

        self.release_check(
            self.application.system_configuration.release,
            30,
            f'{self.__class__.__name__}.{inspect.stack()[0][3]}',
        )

        return self.composites_material.MassCost

    @mass_cost.setter
    def mass_cost(self, value: float):
        """
        :param float value:
        """

        self.composites_material.MassCost = value

    @property
    def material_type(self) -> int:
        """

        Introduced in V5-6R2020.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2024-08-20 16:04:57.203445)
                | Property MaterialType() As short
                |     returns or set the material type defined in Composites tab. the input or
                |     output value is the following: 1 for Undefiened 2 for Unidirectional 3 for Bi
                |     Directional 4 for NCF (Non Crimp Fabric) 5 for Non Structural

        :rtype: int
        """

        self.release_check(
            self.application.system_configuration.release,
            30,
            f'{self.__class__.__name__}.{inspect.stack()[0][3]}',
        )

        return self.composites_material.MaterialType

    @material_type.setter
    def material_type(self, value: int):
        """
        :param int value:
        """

        self.composites_material.MaterialType = value

    @property
    def max_deformation(self) -> float:
        """

        Introduced in V5-6R2020.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2024-08-20 16:04:57.203445)
                | Property MaxDeformation() As double
                |     returns or set the maximum deformation defined in Composites tab in radian.

        :rtype: float
        """

        self.release_check(
            self.application.system_configuration.release,
            30,
            f'{self.__class__.__name__}.{inspect.stack()[0][3]}',
        )

        return self.composites_material.MaxDeformation

    @max_deformation.setter
    def max_deformation(self, value: float):
        """
        :param float value:
        """

        self.composites_material.MaxDeformation = value

    @property
    def surfacic_weigth(self) -> float:
        """

        Introduced in V5-6R2020.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2024-08-20 16:04:57.203445)
                | Property SurfacicWeigth() As double
                |     returns or set the surfacic weigth defined in Composites tab in kg per m2.

        :rtype: float
        """

        self.release_check(
            self.application.system_configuration.release,
            30,
            f'{self.__class__.__name__}.{inspect.stack()[0][3]}',
        )

        return self.composites_material.SurfacicWeigth

    @surfacic_weigth.setter
    def surfacic_weigth(self, value: float):
        """
        :param float value:
        """

        self.composites_material.SurfacicWeigth = value

    @property
    def uncured_thickness(self) -> float:
        """

        Introduced in V5-6R2020.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2024-08-20 16:04:57.203445)
                | Property UncuredThickness() As double
                |     returns or set the uncured thicknes defined in Composites tab in mm.

        :rtype: float
        """

        self.release_check(
            self.application.system_configuration.release,
            30,
            f'{self.__class__.__name__}.{inspect.stack()[0][3]}',
        )

        return self.composites_material.UncuredThickness

    @uncured_thickness.setter
    def uncured_thickness(self, value: float):
        """
        :param float value:
        """

        self.composites_material.UncuredThickness = value

    def create_composites_data(self) -> None:
        """

        Introduced in V5-6R2020.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2024-08-20 16:04:57.203445)
                | Sub CreateCompositesData()
                |     Create a default composites properties on the current material.

        :rtype: None
        """

        self.release_check(
            self.application.system_configuration.release,
            30,
            f'{self.__class__.__name__}.{inspect.stack()[0][3]}',
        )

        return self.composites_material.CreateCompositesData()

    def exist_composites_data(self) -> int:
        """

        Introduced in V5-6R2020.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2024-08-20 16:04:57.203445)
                | Func ExistCompositesData() As short
                |     Returns true if a composites properties exists on the current material.

        :rtype: int
        """

        self.release_check(
            self.application.system_configuration.release,
            30,
            f'{self.__class__.__name__}.{inspect.stack()[0][3]}',
        )

        return self.composites_material.ExistCompositesData()

    def __repr__(self):
        return f'CompositesMaterial(name="{self.name}")'
