#! /usr/bin/python3.6
# module initially auto generated using V5Automation.chm from CATIA R25 on 2020-05-22 12:54:36.956119

from pycatia.mec_mod_interfaces.hybridshape import HybridShape


class HybridShapeLawDistProj(HybridShape):
    """
        .. note::
            CAA V5 Visual Basic help

                | Interface to law feature.Role: Allows you to access data of a law
                | feature created by using   a reference line and a definition curve.

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_law_dist_proj = com_object     

    @property
    def applied_unit_symbol(self, i_symbol):
        """
        .. note::
            CAA V5 Visual Basic help

                | AppliedUnitSymbol
                | o Property AppliedUnitSymbol(        iSymbol) (Write Only)
                | 
                | Returns or sets the applied unit symbol for heterogeneous
                | law.

        :param i_symbol:
        :return:
        """
        return self.hybrid_shape_law_dist_proj.AppliedUnitSymbol

    @applied_unit_symbol.setter
    def applied_unit_symbol(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_law_dist_proj.AppliedUnitSymbol = value 

    @property
    def definition(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Definition
                | o Property Definition(    ) As
                | 
                | Returns or sets the definition curve of the law. Sub-
                | element(s) supported (see object): see or .

        :return:
        """
        return self.hybrid_shape_law_dist_proj.Definition

    @definition.setter
    def definition(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_law_dist_proj.Definition = value 

    @property
    def measure_unit_symbol(self, i_symbol):
        """
        .. note::
            CAA V5 Visual Basic help

                | MeasureUnitSymbol
                | o Property MeasureUnitSymbol(        iSymbol) (Write Only)
                | 
                | Returns or sets the measure unit symbol for heterogeneous
                | law.

        :param i_symbol:
        :return:
        """
        return self.hybrid_shape_law_dist_proj.MeasureUnitSymbol

    @measure_unit_symbol.setter
    def measure_unit_symbol(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_law_dist_proj.MeasureUnitSymbol = value 

    @property
    def parameter_on_definition(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | ParameterOnDefinition
                | o Property ParameterOnDefinition(    ) As
                | 
                | Queries whether evolution parameter is on reference curve
                | (default) or on definition curve,or sets evolution parameter
                | on reference curve or on definition curve. Possible values
                | of ParameterOnDefinition = TRUE : Parameter on definition
                | curve. = FALSE : Parameter on reference curve.

        :return:
        """
        return self.hybrid_shape_law_dist_proj.ParameterOnDefinition

    @property
    def positive_direction_orientation(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | PositiveDirectionOrientation
                | o Property PositiveDirectionOrientation(    ) As
                | 
                | Returns or sets the positive value direction.

        :return:
        """
        return self.hybrid_shape_law_dist_proj.PositiveDirectionOrientation

    @positive_direction_orientation.setter
    def positive_direction_orientation(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_law_dist_proj.PositiveDirectionOrientation = value 

    @property
    def reference(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Reference
                | o Property Reference(    ) As
                | 
                | Returns or sets the reference line of the law. Sub-
                | element(s) supported (see object): see or .

        :return:
        """
        return self.hybrid_shape_law_dist_proj.Reference

    @reference.setter
    def reference(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_law_dist_proj.Reference = value 

    @property
    def scaling(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Scaling
                | o Property Scaling(    ) As
                | 
                | Returns or sets the scaling ratio of the law.

        :return:
        """
        return self.hybrid_shape_law_dist_proj.Scaling

    @scaling.setter
    def scaling(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_law_dist_proj.Scaling = value 

    def get_applied_unit_symbol(self, o_symbol):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetAppliedUnitSymbol
                | o Sub GetAppliedUnitSymbol(        oSymbol)
                | 
                | Returns the applied unit symbol.
                |
                | Parameters:
                | oSymbol
                |     The symbol of applied unit

                | Examples:
                | This example retrieves in oSymbol the applied unit symbol of
                | the hybridShapeLawDist hybrid shape law feature. Dim oSymbol
                | hybridShapeLawDist.GetAppliedUnitSymboloSymbol

        :param o_symbol:
        :return:
        """
        return self.hybrid_shape_law_dist_proj.GetAppliedUnitSymbol(o_symbol)

    def get_measure_unit_symbol(self, o_symbol):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetMeasureUnitSymbol
                | o Sub GetMeasureUnitSymbol(        oSymbol)
                | 
                | Returns the measure unit symbol.
                |
                | Parameters:
                | oSymbol
                |     The symbol of measure unit

                | Examples:
                | This example retrieves in oSymbol the measure unit symbol of
                | the hybridShapeLawDist hybrid shape law feature. Dim oSymbol
                | hybridShapeLawDist.GetMeasureUnitSymboloSymbol

        :param o_symbol:
        :return:
        """
        return self.hybrid_shape_law_dist_proj.GetMeasureUnitSymbol(o_symbol)

    def get_plane_normal(self, o_normal):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetPlaneNormal
                | o Sub GetPlaneNormal(        oNormal)
                | 
                | Retrieves the support plane normal.
                |
                | Parameters:
                | oNormal
                |    The support plane normal


        :param o_normal:
        :return:
        """
        return self.hybrid_shape_law_dist_proj.GetPlaneNormal(o_normal)

    def is_heterogeneous_law(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | IsHeterogeneousLaw
                | o Func IsHeterogeneousLaw(    ) As
                | 
                | Queries whether Heterogeneous Law mode is active or not.
                |
                | Parameters:
                | oHeterogeneousLaw
                |        heterogeneous law mode =  TRUE  :  Heterogeneous Law mode is active.
                |                               =  FALSE : Heterogeneous Law mode is inactive.


        :return:
        """
        return self.hybrid_shape_law_dist_proj.IsHeterogeneousLaw()

    def put_plane_normal(self, i_normal):
        """
        .. note::
            CAA V5 Visual Basic help

                | PutPlaneNormal
                | o Sub PutPlaneNormal(        iNormal)
                | 
                | Sets the support plane normal.
                |
                | Parameters:
                | iNormal
                |    The support plane normal


        :param i_normal:
        :return:
        """
        return self.hybrid_shape_law_dist_proj.PutPlaneNormal(i_normal)

    def __repr__(self):
        return f'HybridShapeLawDistProj()'
