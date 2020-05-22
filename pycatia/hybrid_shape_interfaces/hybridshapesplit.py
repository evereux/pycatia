#! /usr/bin/python3.6
# module initially auto generated using V5Automation.chm from CATIA R25 on 2020-05-22 12:54:36.956119

from pycatia.mec_mod_interfaces.hybridshape import HybridShape


class HybridShapeSplit(HybridShape):
    """
        .. note::
            CAA V5 Visual Basic help

                | Represents the hybrid shape split feature object.Role: To access data
                | of the hybrid shape split feature. This data includes:

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_split = com_object     

    @property
    def automatic_extrapolation_mode(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | AutomaticExtrapolationMode
                | o Property AutomaticExtrapolationMode(    ) As
                | 
                | Gets or sets the automatic extrapolation mode status.
                | AutomaticExtrapolationMode = TRUE : Automatic extrapolation
                | mode is on. = FALSE : Automatic extrapolation mode is off.
                | This example retrieves in AutoExtrapolMode the automatic
                | extrapolation mode status for the Split hybrid shape
                | feature. Dim AutoExtrapolMode As boolean AutoExtrapolMode =
                | Split.AutomaticExtrapolationMode

        :return:
        """
        return self.hybrid_shape_split.AutomaticExtrapolationMode

    @property
    def both_sides_mode(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | BothSidesMode
                | o Property BothSidesMode(    ) As
                | 
                | Gets or sets both sides computation mode. BothSidesMode =
                | TRUE : Both sides are computed. = FALSE : Both sides are not
                | computed. This example retrieves in BothSides the both sides
                | computation mode for the Split hybrid shape feature. Dim
                | BothSides As boolean BothSides = Split.BothSidesMode

        :return:
        """
        return self.hybrid_shape_split.BothSidesMode

    @property
    def cutting_elem(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | CuttingElem
                | o Property CuttingElem(    ) As
                | 
                | Returns or sets the cutting element. Sub-element(s)
                | supported (see object): , , or . 
                |
                | Example:
                | This example
                | retrieves in CuttingElement the cutting element for the
                | Split hybrid shape feature. Dim CuttingElement As Reference
                | Set CuttingElement = Split.CuttingElem

        :return:
        """
        return self.hybrid_shape_split.CuttingElem

    @cutting_elem.setter
    def cutting_elem(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_split.CuttingElem = value 

    @property
    def elem_to_cut(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | ElemToCut
                | o Property ElemToCut(    ) As
                | 
                | Returns or sets the element to cut. 
                |
                | Example:
                | This example
                | retrieves in Element the element to cut for the Split hybrid
                | shape feature. Dim Element As Reference Set Element =
                | Split.ElemToCut

        :return:
        """
        return self.hybrid_shape_split.ElemToCut

    @elem_to_cut.setter
    def elem_to_cut(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_split.ElemToCut = value 

    @property
    def intersection_computation(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | IntersectionComputation
                | o Property IntersectionComputation(    ) As
                | 
                | Gets or sets Intersection computation mode.
                | IntersectionComputation = TRUE : Intersection is computed. =
                | FALSE : Intersection is not computed. This example retrieves
                | in Intersection the Intersection computation mode for the
                | Split hybrid shape feature. Dim Intersection As boolean
                | Intersection = Split.IntersectionComputation

        :return:
        """
        return self.hybrid_shape_split.IntersectionComputation

    @property
    def orientation(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Orientation
                | o Property Orientation(    ) As
                | 
                | Returns or sets the orientation used to compute the split.
                | Role: Orientation specifies kept parts of cut feature. When
                | splitting a surface by a surface : - If orientation value is
                | 1: kept parts are specified by the "natural" normal to the
                | cutting feature - If orientation value -1: kept parts are
                | specified by the inverse of the "natural" normal to the
                | cutting feature When splitting a surface by a curve : - If
                | orientation value is 1: kept parts are specified by the
                | result of the cross product : normal(surface)^tangent(curve)
                | - If orientation value is -1: Kept parts are specified by
                | the inverse of the result of the cross product :
                | normal(surface)^tangent(curve) When splitting a curve by a
                | point or a curve (without support specified) : - If
                | orientation value is 1: Kept parts are from beginning of the
                | curve to the first intersection, and, if there is one, from
                | the second to the third intersection and so on until the end
                | of the curve. - If orientation value is -1: Kept parts are
                | from the first intersection to the second (if there is one),
                | and, if there is one, from the third to the fourth and so on
                | until the end of the curve. When splitting a curve on
                | support: - If orientation value is 1: Kept parts are
                | specified by the result of the cross product :
                | normal(support surface)^tangent(cutting curve) - If
                | orientation value is -1: Kept parts are specified by the
                | inverse of the result of the cross product : normal(support
                | surface)^tangent(cutting curve) When splitting a curve by a
                | surface: - If orientation value is 1: Kept parts are
                | specified by the inverse of the normal to the surface - If
                | orientation value is -1: Kept parts are specified by the
                | normal to the surface Example This example retrieves in
                | OrientValue the orientation value for the Split hybrid shape
                | feature. Dim OrientValue As long Set OrientValue =
                | Split.Orientation

        :return:
        """
        return self.hybrid_shape_split.Orientation

    @orientation.setter
    def orientation(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_split.Orientation = value 

    @property
    def support(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Support
                | o Property Support(    ) As
                | 
                | Returns or sets the support element. This support element
                | may not exist. Sub-element(s) supported (see object): .
                | 
                |
                | Example:
                | This example retrieves in Element the support
                | element for the Split hybrid shape feature. Dim Element As
                | Reference Set Element = Split.Support

        :return:
        """
        return self.hybrid_shape_split.Support

    @support.setter
    def support(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_split.Support = value 

    @property
    def volume_result(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | VolumeResult
                | o Property VolumeResult(    ) As
                | 
                | Returns or sets the Result Type. Result type: : 0 -> Surface
                | : 1 -> Volume, The resultant split will be volume. If input
                | is element to cut is volume. Note: Setting volume result
                | requires GSO License. 
                |
                | Example:
                | This example retrieves in
                | ResultType the result type for the Split hybrid shape
                | feature. Dim RType As long Set RType = Split.ResultType

        :return:
        """
        return self.hybrid_shape_split.VolumeResult

    @volume_result.setter
    def volume_result(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_split.VolumeResult = value 

    def add_cutting_elem(self, i_elem, i_orientation):
        """
        .. note::
            CAA V5 Visual Basic help

                | AddCuttingElem
                | o Sub AddCuttingElem(        iElem,
                |                              iOrientation)
                | 
                | Adds a cutting feature.
                |
                | Parameters:
                | iElem
                |       cutting feature 
                |    
                |  iOrientation
                |        Orientation
                |       iOrientation =  1 : SameOrientation
                | 					 = -1 : InvertOrientation
                | 					 =  2 : KoOrientation


        :param i_elem:
        :param i_orientation:
        :return:
        """
        return self.hybrid_shape_split.AddCuttingElem(i_elem, i_orientation)

    def add_element_to_keep(self, i_element):
        """
        .. note::
            CAA V5 Visual Basic help

                | AddElementToKeep
                | o Sub AddElementToKeep(        iElement)
                | 
                | Adds an element to specifications. This element will be
                | kept.
                |
                | Parameters:
                | iElement
                |    Element to keep.


        :param i_element:
        :return:
        """
        return self.hybrid_shape_split.AddElementToKeep(i_element)

    def add_element_to_remove(self, i_element):
        """
        .. note::
            CAA V5 Visual Basic help

                | AddElementToRemove
                | o Sub AddElementToRemove(        iElement)
                | 
                | Adds an element to specifications. This element will be
                | removed.
                |
                | Parameters:
                | iElement
                |    Element to remove.


        :param i_element:
        :return:
        """
        return self.hybrid_shape_split.AddElementToRemove(i_element)

    def get_cutting_elem(self, i_rank):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetCuttingElem
                | o Func GetCuttingElem(        iRank) As
                | 
                | Gets the cutting feature at a given index (a point, a curve
                | or a surface).
                |
                | Parameters:
                | oElem
                |       cutting feature 
                |    
                |  iRank
                |       Index of one of the cutting features


        :param i_rank:
        :return:
        """
        return self.hybrid_shape_split.GetCuttingElem(i_rank)

    def get_intersection(self, i_rank):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetIntersection
                | o Func GetIntersection(        iRank) As
                | 
                | Gets the intersection at a given index.
                |
                | Parameters:
                | oElem
                |       Intersection
                |    
                |  iRank
                |       Index of one of the intersection features


        :param i_rank:
        :return:
        """
        return self.hybrid_shape_split.GetIntersection(i_rank)

    def get_kept_elem(self, i_rank):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetKeptElem
                | o Func GetKeptElem(        iRank) As
                | 
                | Gets the kept feature at a given index.
                |
                | Parameters:
                | oElem
                |       Kept feature 
                |    
                |  iRank
                |       Index of one of the kept features


        :param i_rank:
        :return:
        """
        return self.hybrid_shape_split.GetKeptElem(i_rank)

    def get_nb_cutting_elem(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetNbCuttingElem
                | o Func GetNbCuttingElem(    ) As
                | 
                | Gets the number of cutting features.
                |
                | Parameters:
                | oNbCuttingElem
                |       Number of  cutting features


        :return:
        """
        return self.hybrid_shape_split.GetNbCuttingElem()

    def get_nb_elements_to_keep(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetNbElementsToKeep
                | o Func GetNbElementsToKeep(    ) As
                | 
                | Gets the number of elements to keep.
                |
                | Parameters:
                | oNbElementsToKeep
                |       Number of elements to keep


        :return:
        """
        return self.hybrid_shape_split.GetNbElementsToKeep()

    def get_nb_elements_to_remove(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetNbElementsToRemove
                | o Func GetNbElementsToRemove(    ) As
                | 
                | Gets the number of elements to remove.
                |
                | Parameters:
                | oNbElementsToRemove
                |       Number of elements to remove


        :return:
        """
        return self.hybrid_shape_split.GetNbElementsToRemove()

    def get_orientation(self, i_rank):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetOrientation
                | o Func GetOrientation(        iRank) As
                | 
                | Gets Orientation used to compute the split.
                |
                | Parameters:
                | oOrientation
                |         Orientation
                |    
                |  iRank
                |        index of the cutting feature 
                |       oOrientation =  1 : SameOrientation
                | 					 = -1 : InvertOrientation
                | 					 =  2 : KoOrientation


        :param i_rank:
        :return:
        """
        return self.hybrid_shape_split.GetOrientation(i_rank)

    def get_other_side(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetOtherSide
                | o Func GetOtherSide(    ) As
                | 
                | Gets the other side.
                |
                | Parameters:
                | oElem
                |       Other side


        :return:
        """
        return self.hybrid_shape_split.GetOtherSide()

    def get_removed_elem(self, i_rank):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetRemovedElem
                | o Func GetRemovedElem(        iRank) As
                | 
                | Gets the removed feature at a given index.
                |
                | Parameters:
                | oElem
                |       Removed feature 
                |    
                |  iRank
                |       Index of one of the removed features


        :param i_rank:
        :return:
        """
        return self.hybrid_shape_split.GetRemovedElem(i_rank)

    def invert_orientation(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | InvertOrientation
                | o Sub InvertOrientation(    )
                | 
                | Inverts the orientation used to compute the split.
                |
                | Parameters:


        :return:
        """
        return self.hybrid_shape_split.InvertOrientation()

    def remove_cutting_elem(self, i_elem):
        """
        .. note::
            CAA V5 Visual Basic help

                | RemoveCuttingElem
                | o Sub RemoveCuttingElem(        iElem)
                | 
                | Removes a cutting feature.
                |
                | Parameters:
                | iElem
                |       cutting feature


        :param i_elem:
        :return:
        """
        return self.hybrid_shape_split.RemoveCuttingElem(i_elem)

    def remove_element_to_keep(self, i_rank):
        """
        .. note::
            CAA V5 Visual Basic help

                | RemoveElementToKeep
                | o Sub RemoveElementToKeep(        iRank)
                | 
                | Removes an element from specifications.
                |
                | Parameters:
                | iRank
                |    Index of the kept element.


        :param i_rank:
        :return:
        """
        return self.hybrid_shape_split.RemoveElementToKeep(i_rank)

    def remove_element_to_remove(self, i_rank):
        """
        .. note::
            CAA V5 Visual Basic help

                | RemoveElementToRemove
                | o Sub RemoveElementToRemove(        iRank)
                | 
                | Removes an element from specifications.
                |
                | Parameters:
                | iRank
                |    Index of the removed element.


        :param i_rank:
        :return:
        """
        return self.hybrid_shape_split.RemoveElementToRemove(i_rank)

    def set_orientation(self, i_rank, i_orientation):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetOrientation
                | o Sub SetOrientation(        iRank,
                |                              iOrientation)
                | 
                | Sets the orientation used to compute the split.
                |
                | Parameters:
                | iOrientation
                |         Orientation
                |    
                |  iRank
                |        index of the cutting feature 
                |       iOrientation =  1 : SameOrientation
                | 					 = -1 : InvertOrientation
                | 					 =  2 : KoOrientation


        :param i_rank:
        :param i_orientation:
        :return:
        """
        return self.hybrid_shape_split.SetOrientation(i_rank, i_orientation)

    def __repr__(self):
        return f'HybridShapeSplit()'
