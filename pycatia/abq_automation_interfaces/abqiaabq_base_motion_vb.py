#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.abq_automation_interfaces.abq_boundary_condition import ABQBoundaryCondition
from pycatia.abq_automation_interfaces.abq_clamp_bc import ABQClampBC
from pycatia.abq_automation_interfaces.abq_displacement_bc import ABQDisplacementBC
from pycatia.in_interfaces.reference import Reference
from pycatia.product_structure_interfaces.product import Product


class ABQIAABQBaseMotionVB(ABQBoundaryCondition):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     ABQAutomationItf.ABQBoundaryCondition
                |                         ABQIAABQBaseMotionVB
                | 
                | Interface representing xxx.
                | 
                | Role: Components that implement ABQIAABQBaseMotion are ...
                | 
                | Do not use the ABQIAABQBaseMotion interface for such and such ClassReference,
                | Class#MethodReference, #InternalMethod...
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.abqiaabq_base_motion_vb = com_object

    @property
    def base_motion_type(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property BaseMotionType() As CATBSTR

        :rtype: str
        """

        return self.abqiaabq_base_motion_vb.BaseMotionType

    @base_motion_type.setter
    def base_motion_type(self, value: str):
        """
        :param str value:
        """

        self.abqiaabq_base_motion_vb.BaseMotionType = value

    @property
    def base_type(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property BaseType() As short

        :rtype: int
        """

        return self.abqiaabq_base_motion_vb.BaseType

    @base_type.setter
    def base_type(self, value: int):
        """
        :param int value:
        """

        self.abqiaabq_base_motion_vb.BaseType = value

    @property
    def clamp_support(self) -> ABQClampBC:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ClampSupport() As ABQClampBC

        :rtype: ABQClampBC
        """

        return ABQClampBC(self.abqiaabq_base_motion_vb.ClampSupport)

    @clamp_support.setter
    def clamp_support(self, value: ABQClampBC):
        """
        :param ABQClampBC value:
        """

        self.abqiaabq_base_motion_vb.ClampSupport = value

    @property
    def dof(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property DOF() As double

        :rtype: float
        """

        return self.abqiaabq_base_motion_vb.DOF

    @dof.setter
    def dof(self, value: float):
        """
        :param float value:
        """

        self.abqiaabq_base_motion_vb.DOF = value

    @property
    def data_type(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property DataType() As boolean

        :rtype: bool
        """

        return self.abqiaabq_base_motion_vb.DataType

    @data_type.setter
    def data_type(self, value: bool):
        """
        :param bool value:
        """

        self.abqiaabq_base_motion_vb.DataType = value

    @property
    def disp_bc_support(self) -> ABQDisplacementBC:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property DispBCSupport() As ABQDisplacementBC

        :rtype: ABQDisplacementBC
        """

        return ABQDisplacementBC(self.abqiaabq_base_motion_vb.DispBCSupport)

    @disp_bc_support.setter
    def disp_bc_support(self, value: ABQDisplacementBC):
        """
        :param ABQDisplacementBC value:
        """

        self.abqiaabq_base_motion_vb.DispBCSupport = value

    @property
    def frequency_data_values(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property FrequencyDataValues(CATSafeArrayVariant iFreqDataVal) (Write
                | Only)

        :rtype: int
        """

        return self.abqiaabq_base_motion_vb.FrequencyDataValues

    @frequency_data_values.setter
    def frequency_data_values(self, value: int):
        """
        :param int value:
        """

        self.abqiaabq_base_motion_vb.FrequencyDataValues = value

    @property
    def imaginary_data_values(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ImaginaryDataValues(CATSafeArrayVariant iImaginaryDataValues)
                | (Write Only)

        :rtype: False
        """

        return self.abqiaabq_base_motion_vb.ImaginaryDataValues

    @imaginary_data_values.setter
    def imaginary_data_values(self, value: int):
        """
        :param int value:
        """

        self.abqiaabq_base_motion_vb.ImaginaryDataValues = value

    @property
    def real_data_values(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property RealDataValues(CATSafeArrayVariant iRealDataVal) (Write
                | Only)

        :rtype: False
        """

        return self.abqiaabq_base_motion_vb.RealDataValues

    @real_data_values.setter
    def real_data_values(self, value: int):
        """
        :param int value:
        """

        self.abqiaabq_base_motion_vb.RealDataValues = value

    @property
    def scale(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Scale() As double

        :rtype: float
        """

        return self.abqiaabq_base_motion_vb.Scale

    @scale.setter
    def scale(self, value: float):
        """
        :param float value:
        """

        self.abqiaabq_base_motion_vb.Scale = value

    def add_centre_of_rotation(self, i_product: Product, i_ref: Reference) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub AddCentreOfRotation(Product iProduct,
                | Reference iRef)

        :param Product i_product:
        :param Reference i_ref:
        :rtype: None
        """
        return self.abqiaabq_base_motion_vb.AddCentreOfRotation(i_product.com_object, i_ref.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'add_centre_of_rotation'
        # # vba_code = """
        # # Public Function add_centre_of_rotation(abqiaabq_base_motion_vb)
        # #     Dim iProduct (2)
        # #     abqiaabq_base_motion_vb.AddCentreOfRotation iProduct
        # #     add_centre_of_rotation = iProduct
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'ABQIAABQBaseMotionVB(name="{self.name}")'
