#! /usr/bin/python3.6
# module initially auto generated using V5Automation.chm from CATIA R25 on 2020-05-22 12:54:36.956119

from pycatia.mec_mod_interfaces.hybridshape import HybridShape


class HybridShapeUnfold(HybridShape):
    """
        .. note::
            CAA V5 Visual Basic help

                | Represents the hybrid shape Unfold feature object.Role: To access the
                | data of the hybrid shape Unfold feature object. This data includes:Use
                | the  CATIAHybridShapeFactory to create a HybridShapeUnfold object.

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_unfold = com_object     

    @property
    def direction_to_unfold(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | DirectionToUnfold
                | o Property DirectionToUnfold(    ) As
                | 
                | Returns or sets the direction to unfold.

        :return:
        """
        return self.hybrid_shape_unfold.DirectionToUnfold

    @direction_to_unfold.setter
    def direction_to_unfold(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_unfold.DirectionToUnfold = value 

    @property
    def edge_to_tear_positioning_orientation(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | EdgeToTearPositioningOrientation
                | o Property EdgeToTearPositioningOrientation(    ) As
                | 
                | Returns or sets the positioning orientation when the
                | reference origin is located on an edge to tear. 0= The
                | orientation is undefined 1= The orientation is the default
                | one 2= The orientation is inversed

        :return:
        """
        return self.hybrid_shape_unfold.EdgeToTearPositioningOrientation

    @edge_to_tear_positioning_orientation.setter
    def edge_to_tear_positioning_orientation(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_unfold.EdgeToTearPositioningOrientation = value 

    @property
    def origin_to_unfold(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | OriginToUnfold
                | o Property OriginToUnfold(    ) As
                | 
                | Returns or sets the origin to unfold.

        :return:
        """
        return self.hybrid_shape_unfold.OriginToUnfold

    @origin_to_unfold.setter
    def origin_to_unfold(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_unfold.OriginToUnfold = value 

    @property
    def surface_to_unfold(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | SurfaceToUnfold
                | o Property SurfaceToUnfold(    ) As
                | 
                | Returns or sets the surface to unfold. Sub-element(s)
                | supported (see object): , and .

        :return:
        """
        return self.hybrid_shape_unfold.SurfaceToUnfold

    @surface_to_unfold.setter
    def surface_to_unfold(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_unfold.SurfaceToUnfold = value 

    @property
    def surface_type(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | SurfaceType
                | o Property SurfaceType(    ) As
                | 
                | Returns or sets the type of surface to unfold. 0= The type
                | of surface is not defined 1= The type of surface is ruled 2=
                | The type of surface is all

        :return:
        """
        return self.hybrid_shape_unfold.SurfaceType

    @surface_type.setter
    def surface_type(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_unfold.SurfaceType = value 

    @property
    def target_orientation_mode(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | TargetOrientationMode
                | o Property TargetOrientationMode(    ) As
                | 
                | Returns or sets the mode for target surface orientation. 0=
                | No axis inversion 1= U inversion axis 2= V inversion axis 3=
                | U inversion axis and V inversion axis 4= U inversion axis
                | and swap U and V axis 5= V inversion axis and swap U and V
                | axis 6= U inversion axis, V inversion axis and swap U and V
                | axis 7= Swap U and V axis

        :return:
        """
        return self.hybrid_shape_unfold.TargetOrientationMode

    @target_orientation_mode.setter
    def target_orientation_mode(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_unfold.TargetOrientationMode = value 

    @property
    def target_plane(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | TargetPlane
                | o Property TargetPlane(    ) As
                | 
                | Returns or sets the target plane. Sub-element(s) supported
                | (see object):

        :return:
        """
        return self.hybrid_shape_unfold.TargetPlane

    @target_plane.setter
    def target_plane(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_unfold.TargetPlane = value 

    def add_edge_to_tear(self, i_element):
        """
        .. note::
            CAA V5 Visual Basic help

                | AddEdgeToTear
                | o Sub AddEdgeToTear(        iElement)
                | 
                | Adds an edge to tear.
                |
                | Parameters:
                | iEdge
                | 		The edge to tear to add to the hybrid shape feature object.
                |  Sub-element(s) supported (see 
                | 
                |  object):  
                |  
                | Examples:
                |  
                |  The following example adds the iElement feature object to the 
                |  HybridShapeUnfold object.
                |  
                |  HybridShapeUnfold.AddEdgeToTear iElement


        :param i_element:
        :return:
        """
        return self.hybrid_shape_unfold.AddEdgeToTear(i_element)

    def add_element_to_transfer(self, i_element, i_type_of_transfer):
        """
        .. note::
            CAA V5 Visual Basic help

                | AddElementToTransfer
                | o Sub AddElementToTransfer(        iElement,
                |                                    iTypeOfTransfer)
                | 
                | Appends an element to transfer.
                |
                | Parameters:
                | iElement
                |       Specification to transfer 
                |    
                |  iTypeOfTransfer
                |       type of tranfer
                |       
                | 0= No transfer mode specified  
                | 1= Folded to unfolded 
                | 2= Unfolded to folded


        :param i_element:
        :param i_type_of_transfer:
        :return:
        """
        return self.hybrid_shape_unfold.AddElementToTransfer(i_element, i_type_of_transfer)

    def get_edge_to_tear(self, i_rank):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetEdgeToTear
                | o Func GetEdgeToTear(        iRank) As
                | 
                | Retrieves an element used by the hybrid shape unfold feature
                | object.
                |
                | Parameters:
                | iRank
                | 		The rank of the element to read.
                |  
                | Examples:
                |  
                |  The following example gets the oElement feature object of the 
                |  HybridShapeUnfold object at the position iRank.
                |  
                |  Dim oElement As Reference
                |  Set oElement = HybridShapeUnfold.GetEdgeToTear (iRank).


        :param i_rank:
        :return:
        """
        return self.hybrid_shape_unfold.GetEdgeToTear(i_rank)

    def get_element_to_transfer(self, i_rank, op_element, o_type_of_transfer):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetElementToTransfer
                | o Sub GetElementToTransfer(        iRank,
                |                                    opElement,
                |                                    oTypeOfTransfer)
                | 
                | Gets an element to transfer.
                |
                | Parameters:
                | iRank
                |       the position of the specification to get
                |    
                |  opElement
                |       Specification to transfer 
                |    
                |  oTypeOfTransfer
                |       type of tranfer
                |       
                | 0= No transfer mode specified  
                | 1= Folded to unfolded 
                | 2= Unfolded to folded


        :param i_rank:
        :param op_element:
        :param o_type_of_transfer:
        :return:
        """
        return self.hybrid_shape_unfold.GetElementToTransfer(i_rank, op_element, o_type_of_transfer)

    def remove_edge_to_tear(self, i_rank):
        """
        .. note::
            CAA V5 Visual Basic help

                | RemoveEdgeToTear
                | o Sub RemoveEdgeToTear(        iRank)
                | 
                | Removes an element used by the hybrid shape unfold feature
                | object.
                |
                | Parameters:
                | iRank
                | 		The rank of the element to remove.
                |  
                | Examples:
                |  
                |  The following example removes the feature object from the 
                |  HybridShapeUnfold object at the position iRank.
                |  
                |  HybridShapeUnfold.RemoveEdgeToTear iRank.


        :param i_rank:
        :return:
        """
        return self.hybrid_shape_unfold.RemoveEdgeToTear(i_rank)

    def remove_element_to_transfer(self, i_rank):
        """
        .. note::
            CAA V5 Visual Basic help

                | RemoveElementToTransfer
                | o Sub RemoveElementToTransfer(        iRank)
                | 
                | Remove an elements to transfer.
                |
                | Parameters:
                | iRank
                |       the position of the specification to remove


        :param i_rank:
        :return:
        """
        return self.hybrid_shape_unfold.RemoveElementToTransfer(i_rank)

    def replace_elements_to_transfer(self, i_rank, i_element):
        """
        .. note::
            CAA V5 Visual Basic help

                | ReplaceElementsToTransfer
                | o Sub ReplaceElementsToTransfer(        iRank,
                |                                         iElement)
                | 
                | Replace an elements to transfer.
                |
                | Parameters:
                | iRank
                |       the position of the specification to replace 
                |    
                |  iElement
                |       the specification to transfer to append.


        :param i_rank:
        :param i_element:
        :return:
        """
        return self.hybrid_shape_unfold.ReplaceElementsToTransfer(i_rank, i_element)

    def __repr__(self):
        return f'HybridShapeUnfold()'
