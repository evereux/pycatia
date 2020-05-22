#! /usr/bin/python3.6
# module initially auto generated using V5Automation.chm from CATIA R25 on 2020-05-22 12:54:36.956119

from pycatia.mec_mod_interfaces.hybridshape import HybridShape


class HybridShapeIntegratedLaw(HybridShape):
    """
        .. note::
            CAA V5 Visual Basic help

                | Represents the hybrid shape "integrated" law feature object.Role: To
                | access the data of the hybrid shape "integrated" law feature
                | object.Use the  CATIAHybridShapeFactory to create a
                | HybridShapeIntegratedLaw  object.

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_integrated_law = com_object     

    @property
    def advanced_law(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | AdvancedLaw
                | o Property AdvancedLaw(    ) As
                | 
                | Gets or sets the external law. Note: Used for law type =
                | 4(Advanced)

        :return:
        """
        return self.hybrid_shape_integrated_law.AdvancedLaw

    @property
    def end_param(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | EndParam
                | o Property EndParam(    ) As   (Read Only)
                | 
                | Gets end parameter. Note: Used for law type = 2(Linear) and
                | 3(SType).

        :return:
        """
        return self.hybrid_shape_integrated_law.EndParam

    @property
    def implicit_law_interpolation_mode(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | ImplicitLawInterpolationMode
                | o Property ImplicitLawInterpolationMode(    ) As
                | 
                | Gets or sets Interpolation mode for implicit law. Note: Used
                | for law type = 5(Implicit)

        :return:
        """
        return self.hybrid_shape_integrated_law.ImplicitLawInterpolationMode

    @property
    def invert_mapping_law(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | InvertMappingLaw
                | o Property InvertMappingLaw(    ) As
                | 
                | Gets or sets the mapping orientation of the law.

        :return:
        """
        return self.hybrid_shape_integrated_law.InvertMappingLaw

    @property
    def pitch_law_type(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | PitchLawType
                | o Property PitchLawType(    ) As
                | 
                | Gets or sets pitch law type.

        :return:
        """
        return self.hybrid_shape_integrated_law.PitchLawType

    @property
    def spine(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Spine
                | o Property Spine(    ) As
                | 
                | Gets or sets Spine for implicit law. Note: Used for law type
                | = 5 (Implicit)

        :return:
        """
        return self.hybrid_shape_integrated_law.Spine

    @property
    def start_param(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | StartParam
                | o Property StartParam(    ) As   (Read Only)
                | 
                | Gets start parameter. Note: Used for law type = 1(Constant)
                | ,2(Linear) and 3(SType)

        :return:
        """
        return self.hybrid_shape_integrated_law.StartParam

    def append_new_point_and_param(self, i_point, i_param):
        """
        .. note::
            CAA V5 Visual Basic help

                | AppendNewPointAndParam
                | o Sub AppendNewPointAndParam(        iPoint,
                |                                      iParam)
                | 
                | Sets 'Point on spine' and associated parameter. Note: Used
                | for law type = 5(Implicit)
                |
                | Parameters:
                | iPoint
                |        Point on spine
                |    
                |  iParam
                |        Corresponding parameter


        :param i_point:
        :param i_param:
        :return:
        """
        return self.hybrid_shape_integrated_law.AppendNewPointAndParam(i_point, i_param)

    def get_point_and_param(self, i_pos, o_point, o_param):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetPointAndParam
                | o Sub GetPointAndParam(        iPos,
                |                                oPoint,
                |                                oParam)
                | 
                | Gets the point on spine and associated parameter at a given
                | position. Note: Used for law type = 5(Implicit)
                |
                | Parameters:
                | iPos
                |         given position
                |    
                |  oPoint
                |         point on spine
                |    
                |  oParam
                |         corresponding parameter


        :param i_pos:
        :param o_point:
        :param o_param:
        :return:
        """
        return self.hybrid_shape_integrated_law.GetPointAndParam(i_pos, o_point, o_param)

    def get_size(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetSize
                | o Func GetSize(    ) As
                | 
                | Gets the size of the list in the law i.e. number of points
                | in the list of the law.
                |
                | Parameters:
                | oSize
                |         size of the list.


        :return:
        """
        return self.hybrid_shape_integrated_law.GetSize()

    def remove_all_points_and_params(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | RemoveAllPointsAndParams
                | o Sub RemoveAllPointsAndParams(    )
                | 
                | Removes all the points and associated parameters. Note: Used
                | for law type = 5(Implicit)
                |
                | Parameters:


        :return:
        """
        return self.hybrid_shape_integrated_law.RemoveAllPointsAndParams()

    def remove_point_and_param(self, i_point):
        """
        .. note::
            CAA V5 Visual Basic help

                | RemovePointAndParam
                | o Sub RemovePointAndParam(        iPoint)
                | 
                | Removes a point and its parameter. for law type =
                | 5(Implicit)
                |
                | Parameters:
                | iSpecPoint
                |         Point to remove


        :param i_point:
        :return:
        """
        return self.hybrid_shape_integrated_law.RemovePointAndParam(i_point)

    def set_end_param(self, i_end_param):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetEndParam
                | o Sub SetEndParam(        iEndParam)
                | 
                | Sets end parameter. Note: Used for law type = 2(Linear) and
                | 3(SType).
                |
                | Parameters:
                | iEndParam
                |        Parameter


        :param i_end_param:
        :return:
        """
        return self.hybrid_shape_integrated_law.SetEndParam(i_end_param)

    def set_start_param(self, i_start_param):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetStartParam
                | o Sub SetStartParam(        iStartParam)
                | 
                | Sets start parameter. Note: Used for law type = 1(Constant)
                | ,2(Linear) and 3(SType).
                |
                | Parameters:
                | iStartParam
                |        Parameter


        :param i_start_param:
        :return:
        """
        return self.hybrid_shape_integrated_law.SetStartParam(i_start_param)

    def __repr__(self):
        return f'HybridShapeIntegratedLaw()'
