#! /usr/bin/python3.6
# module initially auto generated using V5Automation.chm from CATIA R25 on 2020-05-22 12:54:36.956119

from pycatia.mec_mod_interfaces.hybridshape import HybridShape


class HybridShapeAssemble(HybridShape):
    """
        .. note::
            CAA V5 Visual Basic help

                | Represents the hybrid shape assemble feature object.Role: To access
                | the data of the hybrid shape assemble feature object. This data
                | includes:Use the  CATIAHybridShapeFactory to create a
                | HybridShapeAssemble object.

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_assemble = com_object

    @property
    def invert(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Invert
                | o Property Invert(    ) As
                | 
                | Returns or sets the invert mode. Legal values: True the
                | result is inverted. False the result is not inverted.
                | 
                |
                | Example:
                | This example sets the invert mode of the
                | HybShpAssemble hybrid shape assemble feature to True.
                | HybShpAssemble.Invert = True

        :return:
        """
        return self.hybrid_shape_assemble.Invert

    @invert.setter
    def invert(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_assemble.Invert = value

    def add_element(self, i_element):
        """
        .. note::
            CAA V5 Visual Basic help

                | AddElement
                | o Sub AddElement(        iElement)
                | 
                | Adds an element to the hybrid shape assemble feature object.
                |
                | Parameters:
                | iElement
                | 		The element to add to the hybrid shape assemble feature object.
                |  Sub-element(s) supported (see 
                | 
                |  object):  
                | , 
                |  and 
                | . 
                | Examples:
                |  
                |  The following example adds the iElement feature object to the 
                |  HybridShapeAssemble object.
                |  
                |  HybridShapeAssemble.AddElement iElement


        :param i_element:
        :return:
        """
        return self.hybrid_shape_assemble.AddElement(i_element)

    def add_sub_element(self, i_sub_element):
        """
        .. note::
            CAA V5 Visual Basic help

                | AddSubElement
                | o Sub AddSubElement(        iSubElement)
                | 
                | Adds a sub element to the hybrid shape assemble feature
                | object.
                |
                | Parameters:
                | iSubElement
                | 		The sub element to remove to the hybrid shape assemble feature object.


        :param i_sub_element:
        :return:
        """
        return self.hybrid_shape_assemble.AddSubElement(i_sub_element)

    def append_federated_element(self, i_element):
        """
        .. note::
            CAA V5 Visual Basic help

                | AppendFederatedElement
                | o Sub AppendFederatedElement(        iElement)
                | 
                | Appends an init to the list of elements to federate.
                |
                | Parameters:
                | iElement
                |       Element to append.
                |    
                | 
                |  See also:


        :param i_element:
        :return:
        """
        return self.hybrid_shape_assemble.AppendFederatedElement(i_element)

    def get_angular_tolerance(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetAngularTolerance
                | o Func GetAngularTolerance(    ) As
                | 
                | Get the anglular tolerance.
                |
                | Parameters:
                | oValue
                | 		The anglular tolerance.


        :return:
        """
        return self.hybrid_shape_assemble.GetAngularTolerance()

    def get_angular_tolerance_mode(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetAngularToleranceMode
                | o Func GetAngularToleranceMode(    ) As
                | 
                | Get the anglular tolerance mode.
                |
                | Parameters:
                | oValue
                | 		The anglular tolerance mode.


        :return:
        """
        return self.hybrid_shape_assemble.GetAngularToleranceMode()

    def get_connex(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetConnex
                | o Func GetConnex(    ) As
                | 
                | Get the connex checker flag.
                |
                | Parameters:
                | oConnex


        :return:
        """
        return self.hybrid_shape_assemble.GetConnex()

    def get_deviation(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetDeviation
                | o Func GetDeviation(    ) As
                | 
                | Get the deviation value.
                |
                | Parameters:
                | odeviation
                | 		The deviation.


        :return:
        """
        return self.hybrid_shape_assemble.GetDeviation()

    def get_element(self, i_rank):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetElement
                | o Func GetElement(        iRank) As
                | 
                | Retrieves an element used by the hybrid shape assemble
                | feature object.
                |
                | Parameters:
                | iRank
                | 		The rank of the element to read.
                |  
                | Examples:
                |  
                |  The following example gets the oElement feature object of the 
                |  HybridShapeAssemble object at the position iRank.
                |  
                |  Dim oElement As Reference
                |  Set oElement = HybridShapeAssemble.GetElement (iRank).


        :param i_rank:
        :return:
        """
        return self.hybrid_shape_assemble.GetElement(i_rank)

    def get_elements_size(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetElementsSize
                | o Func GetElementsSize(    ) As
                | 
                | Returns the size of the list of elements to assemble in the
                | hybrid shape assemble feature object.
                |
                | Parameters:
                | oSize
                |      Number of elements in the Assemble.

                | Examples:
                | This example retrieves the number of elements in the
                | HybShpAssemble hybrid shape assemble. Dim oSize As long
                | oSize = HybShpAssemble.GetElementsSize

        :return:
        """
        return self.hybrid_shape_assemble.GetElementsSize()

    def get_federated_element(self, i_rank):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetFederatedElement
                | o Func GetFederatedElement(        iRank) As
                | 
                | Retrieves an federated inits used by the hybrid shape
                | assemble feature object.
                |
                | Parameters:
                | iRank
                | 		The rank of the element to read.
                |  
                |  oElement
                |      The federated element.
                |    
                | 
                |  See also:


        :param i_rank:
        :return:
        """
        return self.hybrid_shape_assemble.GetFederatedElement(i_rank)

    def get_federated_elements_size(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetFederatedElementsSize
                | o Func GetFederatedElementsSize(    ) As
                | 
                | Gets the number of federated inits.
                |
                | Parameters:
                | Size
                |       Number of elements.


        :return:
        """
        return self.hybrid_shape_assemble.GetFederatedElementsSize()

    def get_federation_propagation(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetFederationPropagation
                | o Func GetFederationPropagation(    ) As
                | 
                | Gets the propagation mode of the federation.
                |
                | Parameters:
                | i
                |       type of propagation (0: No, 1: All, 2: Continuity, 3:Tangency).


        :return:
        """
        return self.hybrid_shape_assemble.GetFederationPropagation()

    def get_manifold(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetManifold
                | o Func GetManifold(    ) As
                | 
                | Get the manifold checker flag.
                |
                | Parameters:
                | oManifold


        :return:
        """
        return self.hybrid_shape_assemble.GetManifold()

    def get_simplify(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetSimplify
                | o Func GetSimplify(    ) As
                | 
                | Get the simplify flag.
                |
                | Parameters:
                | oSimplify


        :return:
        """
        return self.hybrid_shape_assemble.GetSimplify()

    def get_sub_element(self, i_rank):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetSubElement
                | o Func GetSubElement(        iRank) As
                | 
                | Retrieves a sub element used by the hybrid shape assemble
                | feature object.
                |
                | Parameters:
                | iRank
                | 		The rank of the subelement to read.


        :param i_rank:
        :return:
        """
        return self.hybrid_shape_assemble.GetSubElement(i_rank)

    def get_sub_elements_size(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetSubElementsSize
                | o Func GetSubElementsSize(    ) As
                | 
                | Returns the size of the list of sub-elements to remove in
                | the hybrid shape assemble feature object.
                |
                | Parameters:
                | oSize
                |      Number of sub elements in the Assemble.

                | Examples:
                | This example retrieves the number of sub elements in the
                | HybShpAssemble hybrid shape assemble. Dim oSize As long
                | oSize = HybShpAssemble.GetSubElementsSize

        :return:
        """
        return self.hybrid_shape_assemble.GetSubElementsSize()

    def get_suppress_mode(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetSuppressMode
                | o Func GetSuppressMode(    ) As
                | 
                | Get the SuppressMode flag.
                |
                | Parameters:
                | oSuppressMode


        :return:
        """
        return self.hybrid_shape_assemble.GetSuppressMode()

    def get_tangency_continuity(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetTangencyContinuity
                | o Func GetTangencyContinuity(    ) As
                | 
                | Get the tangency continuity checker flag.
                |
                | Parameters:
                | oTangencyContinuity


        :return:
        """
        return self.hybrid_shape_assemble.GetTangencyContinuity()

    def remove_element(self, i_rank):
        """
        .. note::
            CAA V5 Visual Basic help

                | RemoveElement
                | o Sub RemoveElement(        iRank)
                | 
                | Removes an element used by the hybrid shape assemble feature
                | object.
                |
                | Parameters:
                | iRank
                | 		The rank of the element to remove.
                |  
                | Examples:
                |  
                |  The following example removes the feature object from the 
                |  HybridShapeAssemble object at the position iRank.
                |  
                |  HybridShapeAssemble.RemoveElement iRank.


        :param i_rank:
        :return:
        """
        return self.hybrid_shape_assemble.RemoveElement(i_rank)

    def remove_federated_element(self, i_rank):
        """
        .. note::
            CAA V5 Visual Basic help

                | RemoveFederatedElement
                | o Sub RemoveFederatedElement(        iRank)
                | 
                | Removes an element to the list of elements to federate.
                |
                | Parameters:
                | iRank
                |       Position of the element to remove.


        :param i_rank:
        :return:
        """
        return self.hybrid_shape_assemble.RemoveFederatedElement(i_rank)

    def remove_sub_element(self, i_rank):
        """
        .. note::
            CAA V5 Visual Basic help

                | RemoveSubElement
                | o Sub RemoveSubElement(        iRank)
                | 
                | Removes a sub element used by the hybrid shape assemble
                | feature object.
                |
                | Parameters:
                | iRank
                | 		The rank of the element to remove.


        :param i_rank:
        :return:
        """
        return self.hybrid_shape_assemble.RemoveSubElement(i_rank)

    def replace_element(self, i_pos, i_element):
        """
        .. note::
            CAA V5 Visual Basic help

                | ReplaceElement
                | o Sub ReplaceElement(        iPos,
                |                              iElement)
                | 
                | Replaces the element at specified position in the hybrid
                | shape assemble feature object.
                |
                | Parameters:
                | iPos
                |      Position at which the element should be replaced.
                |  
                |  iElement
                |       Reference of the element to be inserted.

                | Examples:
                | This example replaces the element in the HybShpAssemble
                | assemble feature at specified position iPos
                | HybShpAssemble.ReplaceElement iPos,iElement

        :param i_pos:
        :param i_element:
        :return:
        """
        return self.hybrid_shape_assemble.ReplaceElement(i_pos, i_element)

    def set_angular_tolerance(self, i_value):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetAngularTolerance
                | o Sub SetAngularTolerance(        iValue)
                | 
                | Set the anglular tolerance.
                |
                | Parameters:
                | iValue
                | 		The anglular tolerance.


        :param i_value:
        :return:
        """
        return self.hybrid_shape_assemble.SetAngularTolerance(i_value)

    def set_angular_tolerance_mode(self, i_value):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetAngularToleranceMode
                | o Sub SetAngularToleranceMode(        iValue)
                | 
                | Set the anglular tolerance mode.
                |
                | Parameters:
                | iValue
                | 		The anglular tolerance mode.


        :param i_value:
        :return:
        """
        return self.hybrid_shape_assemble.SetAngularToleranceMode(i_value)

    def set_connex(self, i_connex):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetConnex
                | o Sub SetConnex(        iConnex)
                | 
                | Set the connex checker flag.
                |
                | Parameters:
                | iConnex


        :param i_connex:
        :return:
        """
        return self.hybrid_shape_assemble.SetConnex(i_connex)

    def set_deviation(self, ideviation):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetDeviation
                | o Sub SetDeviation(        ideviation)
                | 
                | Set the deviation value.
                |
                | Parameters:
                | ideviation
                | 		The deviation.


        :param ideviation:
        :return:
        """
        return self.hybrid_shape_assemble.SetDeviation(ideviation)

    def set_federation_propagation(self, i_mode):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetFederationPropagation
                | o Sub SetFederationPropagation(        iMode)
                | 
                | Sets the propagation mode of federation.
                |
                | Parameters:
                | i
                |       type of propagation (0: No, 1: All, 2: Continuity, 3:Tangency).


        :param i_mode:
        :return:
        """
        return self.hybrid_shape_assemble.SetFederationPropagation(i_mode)

    def set_manifold(self, i_manifold):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetManifold
                | o Sub SetManifold(        iManifold)
                | 
                | Set the manifold checker flag.
                |
                | Parameters:
                | iManifold


        :param i_manifold:
        :return:
        """
        return self.hybrid_shape_assemble.SetManifold(i_manifold)

    def set_simplify(self, i_simplify):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetSimplify
                | o Sub SetSimplify(        iSimplify)
                | 
                | Set the simplify flag.
                |
                | Parameters:
                | iSimplify


        :param i_simplify:
        :return:
        """
        return self.hybrid_shape_assemble.SetSimplify(i_simplify)

    def set_suppress_mode(self, i_suppress_mode):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetSuppressMode
                | o Sub SetSuppressMode(        iSuppressMode)
                | 
                | Set the SuppressMode flag.
                |
                | Parameters:
                | iSuppressMode


        :param i_suppress_mode:
        :return:
        """
        return self.hybrid_shape_assemble.SetSuppressMode(i_suppress_mode)

    def set_tangency_continuity(self, i_tangency_continuity):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetTangencyContinuity
                | o Sub SetTangencyContinuity(        iTangencyContinuity)
                | 
                | Set the tangency continuity checker flag.
                |
                | Parameters:
                | iTangencyContinuity


        :param i_tangency_continuity:
        :return:
        """
        return self.hybrid_shape_assemble.SetTangencyContinuity(i_tangency_continuity)

    def __repr__(self):
        return f'HybridShapeAssemble()'
