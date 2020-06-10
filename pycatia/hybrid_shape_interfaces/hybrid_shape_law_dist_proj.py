#! usr/bin/python3.6
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-09 09:53:18.676780

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.in_interfaces.reference import Reference
from pycatia.mec_mod_interfaces.hybrid_shape import HybridShape


class HybridShapeLawDistProj(HybridShape):

    """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.HybridShape
                |                         HybridShapeLawDistProj
                | 
                | Interface to law feature.
                | Role: Allows you to access data of a law feature created by using a reference
                | line and a definition curve.
                | 
                | See also:
                |     HybridShapeFactory
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_law_dist_proj = com_object

    @property
    def applied_unit_symbol(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property AppliedUnitSymbol(CATBSTR iSymbol) (Write Only)
                | 
                |     Returns or sets the applied unit symbol for heterogeneous law.

        :return: False
        """

        return None

    @applied_unit_symbol.setter
    def applied_unit_symbol(self, value):
        """
        :param False value:
        """

        self.hybrid_shape_law_dist_proj.AppliedUnitSymbol = value

    @property
    def definition(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property Definition() As Reference
                | 
                |     Returns or sets the definition curve of the law.
                |     Sub-element(s) supported (see Boundary object): see TriDimFeatEdge or
                |     BiDimFeatEdge.

        :return: Reference
        """

        return Reference(self.hybrid_shape_law_dist_proj.Definition)

    @definition.setter
    def definition(self, value):
        """
        :param Reference value:
        """

        self.hybrid_shape_law_dist_proj.Definition = value

    @property
    def measure_unit_symbol(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property MeasureUnitSymbol(CATBSTR iSymbol) (Write Only)
                | 
                |     Returns or sets the measure unit symbol for heterogeneous law.

        :return: False
        """

        return None

    @measure_unit_symbol.setter
    def measure_unit_symbol(self, value):
        """
        :param False value:
        """

        self.hybrid_shape_law_dist_proj.MeasureUnitSymbol = value

    @property
    def parameter_on_definition(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property ParameterOnDefinition() As boolean
                | 
                |     Queries whether evolution parameter is on reference curve (default) or on definition curve,or sets evolution parameter on reference curve or on definition curve. Possible values of ParameterOnDefinition = TRUE : Parameter on definition curve. = FALSE : Parameter on reference curve. 
                | 
                | Example:
                |     This example retrieves in ParOnDef the ParameterOnDefinition status of the
                |     hybridShapeLawDist hybrid shape law feature.
                | 
                |      Dim ParOnDef As boolean
                |      ParOnDef = hybridShapeLawDist.ParameterOnDefinition

        :return: bool
        """

        return self.hybrid_shape_law_dist_proj.ParameterOnDefinition

    @parameter_on_definition.setter
    def parameter_on_definition(self, value):
        """
        :param bool value:
        """

        self.hybrid_shape_law_dist_proj.ParameterOnDefinition = value

    @property
    def positive_direction_orientation(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property PositiveDirectionOrientation() As long
                | 
                |     Returns or sets the positive value direction.

        :return: int
        """

        return self.hybrid_shape_law_dist_proj.PositiveDirectionOrientation

    @positive_direction_orientation.setter
    def positive_direction_orientation(self, value):
        """
        :param int value:
        """

        self.hybrid_shape_law_dist_proj.PositiveDirectionOrientation = value

    @property
    def reference(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property Reference() As Reference
                | 
                |     Returns or sets the reference line of the law.
                |     Sub-element(s) supported (see Boundary object): see
                |     RectilinearTriDimFeatEdge or RectilinearBiDimFeatEdge.

        :return: Reference
        """

        return Reference(self.hybrid_shape_law_dist_proj.Reference)

    @reference.setter
    def reference(self, value):
        """
        :param Reference value:
        """

        self.hybrid_shape_law_dist_proj.Reference = value

    @property
    def scaling(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property Scaling() As double
                | 
                |     Returns or sets the scaling ratio of the law.

        :return: float
        """

        return self.hybrid_shape_law_dist_proj.Scaling

    @scaling.setter
    def scaling(self, value):
        """
        :param float value:
        """

        self.hybrid_shape_law_dist_proj.Scaling = value

    def get_applied_unit_symbol(self, o_symbol=None):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Sub GetAppliedUnitSymbol(CATBSTR oSymbol)
                | 
                |     Returns the applied unit symbol.
                | 
                |     Parameters:
                | 
                |         oSymbol
                |             The symbol of applied unit 
                | 
                |     Example:
                |         This example retrieves in oSymbol the applied unit symbol of the
                |         hybridShapeLawDist hybrid shape law feature.
                | 
                |          Dim oSymbol
                |          hybridShapeLawDist.GetAppliedUnitSymboloSymbol

        :param str o_symbol:
        :return: None
        """
        return self.hybrid_shape_law_dist_proj.GetAppliedUnitSymbol(o_symbol)

    def get_measure_unit_symbol(self, o_symbol=None):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Sub GetMeasureUnitSymbol(CATBSTR oSymbol)
                | 
                |     Returns the measure unit symbol.
                | 
                |     Parameters:
                | 
                |         oSymbol
                |             The symbol of measure unit 
                | 
                |     Example:
                |         This example retrieves in oSymbol the measure unit symbol of the
                |         hybridShapeLawDist hybrid shape law feature.
                | 
                |          Dim oSymbol
                |          hybridShapeLawDist.GetMeasureUnitSymboloSymbol

        :param str o_symbol:
        :return: None
        """
        return self.hybrid_shape_law_dist_proj.GetMeasureUnitSymbol(o_symbol)

    def get_plane_normal(self, o_normal=None):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Sub GetPlaneNormal(CATSafeArrayVariant oNormal)
                | 
                |     Retrieves the support plane normal.
                | 
                |     Parameters:
                | 
                |         oNormal
                |             The support plane normal

        :param tuple o_normal:
        :return: None
        """
        return self.hybrid_shape_law_dist_proj.GetPlaneNormal(o_normal)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_plane_normal'
        # # vba_code = """
        # # Public Function get_plane_normal(hybrid_shape_law_dist_proj)
        # #     Dim oNormal (2)
        # #     hybrid_shape_law_dist_proj.GetPlaneNormal oNormal
        # #     get_plane_normal = oNormal
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def is_heterogeneous_law(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Func IsHeterogeneousLaw() As boolean
                | 
                |     Queries whether Heterogeneous Law mode is active or not.
                | 
                |     Parameters:
                | 
                |         oHeterogeneousLaw
                |             heterogeneous law mode = TRUE : Heterogeneous Law mode is active. = FALSE : Heterogeneous Law mode is inactive.

        :return: bool
        """
        return bool(self.hybrid_shape_law_dist_proj.IsHeterogeneousLaw())

    def put_plane_normal(self, i_normal=None):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Sub PutPlaneNormal(CATSafeArrayVariant iNormal)
                | 
                |     Sets the support plane normal.
                | 
                |     Parameters:
                | 
                |         iNormal
                |             The support plane normal

        :param tuple i_normal:
        :return: None
        """
        return self.hybrid_shape_law_dist_proj.PutPlaneNormal(i_normal)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'put_plane_normal'
        # # vba_code = """
        # # Public Function put_plane_normal(hybrid_shape_law_dist_proj)
        # #     Dim iNormal (2)
        # #     hybrid_shape_law_dist_proj.PutPlaneNormal iNormal
        # #     put_plane_normal = iNormal
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'HybridShapeLawDistProj(name="{ self.name }")'
