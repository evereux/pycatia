#! usr/bin/python3.6
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.in_interfaces.reference import Reference
from pycatia.mec_mod_interfaces.hybrid_shape import HybridShape


class HybridShapeUnfold(HybridShape):

    """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.HybridShape
                |                         HybridShapeUnfold
                | 
                | Represents the hybrid shape Unfold feature object.
                | Role: To access the data of the hybrid shape Unfold feature object. This data
                | includes:
                | 
                |     The shell to unfold
                |     The edges to tear
                | 
                | Use the CATIAHybridShapeFactory to create a HybridShapeUnfold
                | object.
                | 
                | See also:
                |     HybridShapeFactory
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_unfold = com_object

    @property
    def direction_to_unfold(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property DirectionToUnfold() As Reference
                | 
                |     Returns or sets the direction to unfold.

        :return: Reference
        """

        return Reference(self.hybrid_shape_unfold.DirectionToUnfold)

    @direction_to_unfold.setter
    def direction_to_unfold(self, value):
        """
        :param Reference value:
        """

        self.hybrid_shape_unfold.DirectionToUnfold = value

    @property
    def edge_to_tear_positioning_orientation(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property EdgeToTearPositioningOrientation() As long
                | 
                |     Returns or sets the positioning orientation when the reference origin is
                |     located on an edge to tear.
                | 
                |         0= The orientation is undefined
                |         1= The orientation is the default one
                |         2= The orientation is inversed

        :return: int
        """

        return self.hybrid_shape_unfold.EdgeToTearPositioningOrientation

    @edge_to_tear_positioning_orientation.setter
    def edge_to_tear_positioning_orientation(self, value):
        """
        :param int value:
        """

        self.hybrid_shape_unfold.EdgeToTearPositioningOrientation = value

    @property
    def origin_to_unfold(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property OriginToUnfold() As Reference
                | 
                |     Returns or sets the origin to unfold.

        :return: Reference
        """

        return Reference(self.hybrid_shape_unfold.OriginToUnfold)

    @origin_to_unfold.setter
    def origin_to_unfold(self, value):
        """
        :param Reference value:
        """

        self.hybrid_shape_unfold.OriginToUnfold = value

    @property
    def surface_to_unfold(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property SurfaceToUnfold() As Reference
                | 
                |     Returns or sets the surface to unfold.
                |     Sub-element(s) supported (see Boundary object): Face, TriDimFeatEdge and
                |     BiDimFeatEdge.

        :return: Reference
        """

        return Reference(self.hybrid_shape_unfold.SurfaceToUnfold)

    @surface_to_unfold.setter
    def surface_to_unfold(self, value):
        """
        :param Reference value:
        """

        self.hybrid_shape_unfold.SurfaceToUnfold = value

    @property
    def surface_type(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property SurfaceType() As long
                | 
                |     Returns or sets the type of surface to unfold.
                | 
                |         0= The type of surface is not defined
                |         1= The type of surface is ruled
                |         2= The type of surface is all

        :return: int
        """

        return self.hybrid_shape_unfold.SurfaceType

    @surface_type.setter
    def surface_type(self, value):
        """
        :param int value:
        """

        self.hybrid_shape_unfold.SurfaceType = value

    @property
    def target_orientation_mode(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property TargetOrientationMode() As long
                | 
                |     Returns or sets the mode for target surface orientation.
                | 
                |         0= No axis inversion
                |         1= U inversion axis
                |         2= V inversion axis
                |         3= U inversion axis and V inversion axis
                |         4= U inversion axis and swap U and V axis
                |         5= V inversion axis and swap U and V axis
                |         6= U inversion axis, V inversion axis and swap U and V
                |         axis
                |         7= Swap U and V axis

        :return: int
        """

        return self.hybrid_shape_unfold.TargetOrientationMode

    @target_orientation_mode.setter
    def target_orientation_mode(self, value):
        """
        :param int value:
        """

        self.hybrid_shape_unfold.TargetOrientationMode = value

    @property
    def target_plane(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property TargetPlane() As Reference
                | 
                |     Returns or sets the target plane.
                |     Sub-element(s) supported (see Boundary object):

        :return: Reference
        """

        return Reference(self.hybrid_shape_unfold.TargetPlane)

    @target_plane.setter
    def target_plane(self, value):
        """
        :param Reference value:
        """

        self.hybrid_shape_unfold.TargetPlane = value

    def add_edge_to_tear(self, i_element):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub AddEdgeToTear(Reference iElement)
                | 
                |     Adds an edge to tear.
                | 
                |     Parameters:
                | 
                |         iEdge
                |             The edge to tear to add to the hybrid shape feature
                |             object.
                |             Sub-element(s) supported (see 
                | 
                |         Boundary object): Edge 
                | 
                | Examples:
                |     The following example adds the iElement feature object to the
                |     HybridShapeUnfold object.
                | 
                |      HybridShapeUnfold.AddEdgeToTear iElement

        :param Reference i_element:
        :return: None
        """
        return self.hybrid_shape_unfold.AddEdgeToTear(i_element.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'add_edge_to_tear'
        # # vba_code = """
        # # Public Function add_edge_to_tear(hybrid_shape_unfold)
        # #     Dim iElement (2)
        # #     hybrid_shape_unfold.AddEdgeToTear iElement
        # #     add_edge_to_tear = iElement
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def add_element_to_transfer(self, i_element, i_type_of_transfer):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub AddElementToTransfer(Reference iElement,
                | long iTypeOfTransfer)
                | 
                |     Appends an element to transfer.
                | 
                |     Parameters:
                | 
                |         iElement
                |             Specification to transfer 
                |         iTypeOfTransfer
                |             type of tranfer
                | 
                |                 0= No transfer mode specified
                |                 1= Folded to unfolded
                |                 2= Unfolded to folded

        :param Reference i_element:
        :param int i_type_of_transfer:
        :return: None
        """
        return self.hybrid_shape_unfold.AddElementToTransfer(i_element.com_object, i_type_of_transfer)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'add_element_to_transfer'
        # # vba_code = """
        # # Public Function add_element_to_transfer(hybrid_shape_unfold)
        # #     Dim iElement (2)
        # #     hybrid_shape_unfold.AddElementToTransfer iElement
        # #     add_element_to_transfer = iElement
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_edge_to_tear(self, i_rank):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func GetEdgeToTear(long iRank) As Reference
                | 
                |     Retrieves an element used by the hybrid shape unfold feature
                |     object.
                | 
                |     Parameters:
                | 
                |         iRank
                |             The rank of the element to read. 
                | 
                |     Examples:
                |         The following example gets the oElement feature object of the
                |         HybridShapeUnfold object at the position iRank.
                | 
                |          Dim oElement As Reference
                |          Set oElement = HybridShapeUnfold.GetEdgeToTear (iRank).

        :param int i_rank:
        :return: Reference
        """
        return Reference(self.hybrid_shape_unfold.GetEdgeToTear(i_rank))

    def get_element_to_transfer(self, i_rank, op_element, o_type_of_transfer):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub GetElementToTransfer(long iRank,
                | Reference opElement,
                | long oTypeOfTransfer)
                | 
                |     Gets an element to transfer.
                | 
                |     Parameters:
                | 
                |         iRank
                |             the position of the specification to get 
                |         opElement
                |             Specification to transfer 
                |         oTypeOfTransfer
                |             type of tranfer
                | 
                |                 0= No transfer mode specified
                |                 1= Folded to unfolded
                |                 2= Unfolded to folded

        :param int i_rank:
        :param Reference op_element:
        :param int o_type_of_transfer:
        :return: None
        """
        return self.hybrid_shape_unfold.GetElementToTransfer(i_rank, op_element.com_object, o_type_of_transfer)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_element_to_transfer'
        # # vba_code = """
        # # Public Function get_element_to_transfer(hybrid_shape_unfold)
        # #     Dim iRank (2)
        # #     hybrid_shape_unfold.GetElementToTransfer iRank
        # #     get_element_to_transfer = iRank
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def remove_edge_to_tear(self, i_rank):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub RemoveEdgeToTear(long iRank)
                | 
                |     Removes an element used by the hybrid shape unfold feature
                |     object.
                | 
                |     Parameters:
                | 
                |         iRank
                |             The rank of the element to remove. 
                | 
                |     Examples:
                |         The following example removes the feature object from the
                |         HybridShapeUnfold object at the position iRank.
                | 
                |          HybridShapeUnfold.RemoveEdgeToTear iRank.

        :param int i_rank:
        :return: None
        """
        return self.hybrid_shape_unfold.RemoveEdgeToTear(i_rank)

    def remove_element_to_transfer(self, i_rank):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub RemoveElementToTransfer(long iRank)
                | 
                |     Remove an elements to transfer.
                | 
                |     Parameters:
                | 
                |         iRank
                |             the position of the specification to remove

        :param int i_rank:
        :return: None
        """
        return self.hybrid_shape_unfold.RemoveElementToTransfer(i_rank)

    def replace_elements_to_transfer(self, i_rank, i_element):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub ReplaceElementsToTransfer(long iRank,
                | Reference iElement)
                | 
                |     Replace an elements to transfer.
                | 
                |     Parameters:
                | 
                |         iRank
                |             the position of the specification to replace 
                |         iElement
                |             the specification to transfer to append.

        :param int i_rank:
        :param Reference i_element:
        :return: None
        """
        return self.hybrid_shape_unfold.ReplaceElementsToTransfer(i_rank, i_element.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'replace_elements_to_transfer'
        # # vba_code = """
        # # Public Function replace_elements_to_transfer(hybrid_shape_unfold)
        # #     Dim iRank (2)
        # #     hybrid_shape_unfold.ReplaceElementsToTransfer iRank
        # #     replace_elements_to_transfer = iRank
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'HybridShapeUnfold(name="{ self.name }")'
