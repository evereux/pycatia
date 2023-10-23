#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-07-06 14:02:20.222384

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.in_interfaces.reference import Reference
from pycatia.knowledge_interfaces.length import Length
from pycatia.mec_mod_interfaces.hybrid_shape import HybridShape


class HybridShapeIntegratedLaw(HybridShape):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.HybridShape
                |                         HybridShapeIntegratedLaw
                | 
                | Represents the hybrid shape "integrated" law feature object.
                | Role: To access the data of the hybrid shape "integrated" law feature
                | object.
                | 
                | Use the CATIAHybridShapeFactory to create a HybridShapeIntegratedLaw
                | object.
                | 
                | See also:
                |     HybridShapeFactory.AddNewIntegratedLaw
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_integrated_law = com_object

    @property
    def advanced_law(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property AdvancedLaw() As Reference
                | 
                |     Gets or sets the external law.
                |     Note: Used for law type = 4(Advanced)
                | 
                |     Parameters:
                | 
                |         AdvancedLaw
                |             External Law This example retrieves in ALaw the external law for
                |             the IntegratedLaw hybrid shape feature.
                | 
                |              Dim ALaw
                |              Set ALaw = IntegratedLaw.AdvancedLaw

        :rtype: Reference
        """

        return Reference(self.hybrid_shape_integrated_law.AdvancedLaw)

    @advanced_law.setter
    def advanced_law(self, reference_law: Reference):
        """
        :param Reference reference_law:
        """

        self.hybrid_shape_integrated_law.AdvancedLaw = reference_law.com_object

    @property
    def end_param(self) -> Length:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property EndParam() As Length (Read Only)
                | 
                |     Gets end parameter.
                |     Note: Used for law type = 2(Linear) and 3(SType).
                | 
                |     Parameters:
                | 
                |         EndParam
                |             Parameter This example retrieves in EParam the end parameter for
                |             the IntegratedLaw hybrid shape feature.
                | 
                |              Dim EParam
                |              Set EParam = IntegratedLaw.EndParam

        :rtype: Length
        """

        return Length(self.hybrid_shape_integrated_law.EndParam)

    @property
    def implicit_law_interpolation_mode(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property ImplicitLawInterpolationMode() As long
                | 
                |     Gets or sets Interpolation mode for implicit law.
                |     Note: Used for law type = 5(Implicit)
                | 
                |     Parameters:
                | 
                |         ImplicitLawInterpolationMode
                |             Implicit law interpolation mode ImplicitLawInterpolationMode =
                |             0 : CATGSMImplicitLawInterpo_None =
                |             1 : CATGSMImplicitLawInterpo_Linear =
                |             2 : CATGSMImplicitLawInterpo_Cubic This example retrieves in InterpolLawMode the
                |                 Interpolation mode for the IntegratedLaw hybrid shape feature.
                | 
                |              Dim InterpolLawMode
                |              Set InterpolLawMode = IntegratedLaw.ImplicitLawInterpolationMode

        :rtype: int
        """

        return self.hybrid_shape_integrated_law.ImplicitLawInterpolationMode

    @implicit_law_interpolation_mode.setter
    def implicit_law_interpolation_mode(self, value: int):
        """
        :param int value:
        """

        self.hybrid_shape_integrated_law.ImplicitLawInterpolationMode = value

    @property
    def invert_mapping_law(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property InvertMappingLaw() As boolean
                | 
                |     Gets or sets the mapping orientation of the law.
                | 
                |     Parameters:
                | 
                |         InvertMappingLaw
                |             False : Law is applied from the beginning to the end of the curve
                |                     (mapping is not inverted).
                |             True : Law is applied from the end to the beginning of the curve (mapping is inverted).
                |                    This example retrieves in IMappingLaw the mapping orientation of the law for the
                |                    IntegratedLaw hybrid shape feature.
                | 
                |              Dim IMappingLaw
                |              Set IMappingLaw = IntegratedLaw.InvertMappingLaw

        :rtype: bool
        """

        return self.hybrid_shape_integrated_law.InvertMappingLaw

    @invert_mapping_law.setter
    def invert_mapping_law(self, value: bool):
        """
        :param bool value:
        """

        self.hybrid_shape_integrated_law.InvertMappingLaw = value

    @property
    def pitch_law_type(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property PitchLawType() As long
                | 
                |     Gets or sets pitch law type.
                | 
                |     Parameters:
                | 
                |         PitchLawType
                |             Type of law PitchLawType = 0 : None = 1 : Constant = 2 : Linear = 3 : SType =
                |             4 : Advanced = 5 : Implicit
                |
                |     This example retrieves in PLawType the pitch law type for the IntegratedLaw hybrid shape feature.
                | 
                |     Dim PLawType
                |     Set PLawType = IntegratedLaw.PitchLawType

        :rtype: int
        """

        return self.hybrid_shape_integrated_law.PitchLawType

    @pitch_law_type.setter
    def pitch_law_type(self, value: int):
        """
        :param int value:
        """

        self.hybrid_shape_integrated_law.PitchLawType = value

    @property
    def spine(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Spine() As Reference
                | 
                |     Gets or sets Spine for implicit law.
                |     Note: Used for law type = 5 (Implicit)
                | 
                |     Parameters:
                | 
                |         Spine
                |             Spine on which implicit law inputs points are defined This example
                |             retrieves in Spine1 the spine for the IntegratedLaw hybrid shape
                |             feature.
                | 
                |              Dim Spine1
                |              Set Spine1 = IntegratedLaw.Spine

        :rtype: Reference
        """

        return Reference(self.hybrid_shape_integrated_law.Spine)

    @spine.setter
    def spine(self, reference_spine: Reference):
        """
        :param Reference reference_spine:
        """

        self.hybrid_shape_integrated_law.Spine = reference_spine.com_object

    @property
    def start_param(self) -> Length:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property StartParam() As Length (Read Only)
                | 
                |     Gets start parameter.
                |     Note: Used for law type = 1(Constant) ,2(Linear) and 3(SType)
                | 
                |     Parameters:
                | 
                |         StartParam
                |             Parameter This example retrieves in SParam the start parameter for
                |             the IntegratedLaw hybrid shape feature.
                | 
                |              Dim SParam
                |              Set SParam = IntegratedLaw.StartParam

        :rtype: Length
        """

        return Length(self.hybrid_shape_integrated_law.StartParam)

    def append_new_point_and_param(self, i_point: Reference, i_param: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub AppendNewPointAndParam(Reference iPoint,
                | long iParam)
                | 
                |     Sets 'Point on spine' and associated parameter.
                |     Note: Used for law type = 5(Implicit)
                | 
                |     Parameters:
                | 
                |         iPoint
                |             Point on spine 
                |         iParam
                |             Corresponding parameter

        :param Reference i_point:
        :param int i_param:
        :rtype: None
        """
        return self.hybrid_shape_integrated_law.AppendNewPointAndParam(i_point.com_object, i_param)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'append_new_point_and_param'
        # # vba_code = """
        # # Public Function append_new_point_and_param(hybrid_shape_integrated_law)
        # #     Dim iPoint (2)
        # #     hybrid_shape_integrated_law.AppendNewPointAndParam iPoint
        # #     append_new_point_and_param = iPoint
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_point_and_param(self, i_pos: int, o_point: Reference, o_param: Reference) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub GetPointAndParam(long iPos,
                | Reference oPoint,
                | Reference oParam)
                | 
                |     Gets the point on spine and associated parameter at a given
                |     position.
                |     Note: Used for law type = 5(Implicit)
                | 
                |     Parameters:
                | 
                |         iPos
                |             given position 
                |         oPoint
                |             point on spine 
                |         oParam
                |             corresponding parameter

        :param int i_pos:
        :param Reference o_point:
        :param Reference o_param:
        :rtype: None
        """
        return self.hybrid_shape_integrated_law.GetPointAndParam(i_pos, o_point.com_object, o_param.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_point_and_param'
        # # vba_code = """
        # # Public Function get_point_and_param(hybrid_shape_integrated_law)
        # #     Dim iPos (2)
        # #     hybrid_shape_integrated_law.GetPointAndParam iPos
        # #     get_point_and_param = iPos
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_size(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetSize() As long
                | 
                |     Gets the size of the list in the law i.e. number of points in the list of
                |     the law.
                | 
                |     Parameters:
                | 
                |         oSize
                |             size of the list.

        :rtype: int
        """
        return self.hybrid_shape_integrated_law.GetSize()

    def remove_all_points_and_params(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub RemoveAllPointsAndParams()
                | 
                |     Removes all the points and associated parameters.
                |     Note: Used for law type = 5(Implicit)

        :rtype: None
        """
        return self.hybrid_shape_integrated_law.RemoveAllPointsAndParams()

    def remove_point_and_param(self, i_point: Reference) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub RemovePointAndParam(Reference iPoint)
                | 
                |     Removes a point and its parameter. for law type = 5(Implicit)
                | 
                |     Parameters:
                | 
                |         iSpecPoint
                |             Point to remove

        :param Reference i_point:
        :rtype: None
        """
        return self.hybrid_shape_integrated_law.RemovePointAndParam(i_point.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'remove_point_and_param'
        # # vba_code = """
        # # Public Function remove_point_and_param(hybrid_shape_integrated_law)
        # #     Dim iPoint (2)
        # #     hybrid_shape_integrated_law.RemovePointAndParam iPoint
        # #     remove_point_and_param = iPoint
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_end_param(self, i_end_param: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetEndParam(long iEndParam)
                | 
                |     Sets end parameter.
                |     Note: Used for law type = 2(Linear) and 3(SType).
                | 
                |     Parameters:
                | 
                |         iEndParam
                |             Parameter

        :param int i_end_param:
        :rtype: None
        """
        return self.hybrid_shape_integrated_law.SetEndParam(i_end_param)

    def set_start_param(self, i_start_param: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetStartParam(long iStartParam)
                | 
                |     Sets start parameter.
                |     Note: Used for law type = 1(Constant) ,2(Linear) and 3(SType).
                | 
                |     Parameters:
                | 
                |         iStartParam
                |             Parameter

        :param int i_start_param:
        :rtype: None
        """
        return self.hybrid_shape_integrated_law.SetStartParam(i_start_param)

    def __repr__(self):
        return f'HybridShapeIntegratedLaw(name="{self.name}")'
