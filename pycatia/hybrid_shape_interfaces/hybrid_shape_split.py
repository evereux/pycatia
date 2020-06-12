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


class HybridShapeSplit(HybridShape):
    """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.HybridShape
                |                         HybridShapeSplit
                | 
                | Represents the hybrid shape split feature object.
                | Role: To access data of the hybrid shape split feature. This data
                | includes:
                | 
                |     The element to be cut (surface or curve)
                |     The cutting element ( surface, curve or point)
                |     An orientation to specify which side has to be kept
                | 
                | LICENSING INFORMATION: Creation of volume result requires GSO
                | License
                | if GSO License is not granted , setting of Volume context has not
                | effect
                | Use the CATIAHybridShapeFactory to create HybridShapeFeature
                | object.
                | 
                | See also:
                |     HybridShapeFactory
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_split = com_object

    @property
    def automatic_extrapolation_mode(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property AutomaticExtrapolationMode() As boolean
                | 
                |     Gets or sets the automatic extrapolation mode status.
                |     AutomaticExtrapolationMode = TRUE :
                |     Automatic extrapolation mode is on. = FALSE :
                |     Automatic extrapolation mode is off.
                |     This example retrieves in AutoExtrapolMode the automatic extrapolation mode status for the
                |     Split hybrid shape feature.
                | 
                |      Dim AutoExtrapolMode As boolean
                |      AutoExtrapolMode = Split.AutomaticExtrapolationMode

        :return: bool
        """

        return self.hybrid_shape_split.AutomaticExtrapolationMode

    @automatic_extrapolation_mode.setter
    def automatic_extrapolation_mode(self, value):
        """
        :param bool value:
        """

        self.hybrid_shape_split.AutomaticExtrapolationMode = value

    @property
    def both_sides_mode(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property BothSidesMode() As boolean
                | 
                |     Gets or sets both sides computation mode.
                |     BothSidesMode = TRUE :
                |     Both sides are computed. = FALSE :
                |     Both sides are not computed.
                |     This example retrieves in BothSides the both sides computation mode for the Split hybrid shape
                |     feature.
                | 
                |      Dim BothSides As boolean
                |      BothSides = Split.BothSidesMode

        :return: bool
        """

        return self.hybrid_shape_split.BothSidesMode

    @both_sides_mode.setter
    def both_sides_mode(self, value):
        """
        :param bool value:
        """

        self.hybrid_shape_split.BothSidesMode = value

    @property
    def cutting_elem(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property CuttingElem() As Reference
                | 
                |     Returns or sets the cutting element.
                |     Sub-element(s) supported (see Boundary object): Face, TriDimFeatEdge,
                |     BiDimFeatEdge or Vertex.
                | 
                |     Example:
                |         This example retrieves in CuttingElement the cutting element for the
                |         Split hybrid shape feature.
                | 
                |          Dim CuttingElement As Reference
                |          Set CuttingElement = Split.CuttingElem

        :return: Reference
        """

        return Reference(self.hybrid_shape_split.CuttingElem)

    @cutting_elem.setter
    def cutting_elem(self, value):
        """
        :param Reference value:
        """

        self.hybrid_shape_split.CuttingElem = value

    @property
    def elem_to_cut(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property ElemToCut() As Reference
                | 
                |     Returns or sets the element to cut.
                | 
                |     Example:
                |         This example retrieves in Element the element to cut for the Split
                |         hybrid shape feature.
                | 
                |          Dim Element As Reference
                |          Set Element = Split.ElemToCut

        :return: Reference
        """

        return Reference(self.hybrid_shape_split.ElemToCut)

    @elem_to_cut.setter
    def elem_to_cut(self, value):
        """
        :param Reference value:
        """

        self.hybrid_shape_split.ElemToCut = value

    @property
    def extrapolation_type(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property ExtrapolationType() As long
                | 
                |     Gets or sets the extrapolation type.
                |     ExtrapolationType = CATGSMExtrapolationType_None(0).
                |     = CATGSMExtrapolationType_Tangent(1).
                |     = CATGSMExtrapolationType_Curvature(2).
                |     This example retrieves in ExtrapolateType the extrapolation type for the Split hybrid shape
                |     feature.

        :return: int
        """

        return self.hybrid_shape_split.ExtrapolationType

    @extrapolation_type.setter
    def extrapolation_type(self, value):
        """
        :param int value:
        """

        self.hybrid_shape_split.ExtrapolationType = value

    @property
    def intersection_computation(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property IntersectionComputation() As boolean
                | 
                |     Gets or sets Intersection computation mode.
                |     IntersectionComputation
                |     = TRUE : Intersection is computed.
                |     = FALSE : Intersection is not computed.
                |     This example retrieves in Intersection the Intersection computation mode for the Split hybrid
                |     shape feature.
                | 
                |      Dim Intersection As boolean
                |      Intersection = Split.IntersectionComputation

        :return: bool
        """

        return self.hybrid_shape_split.IntersectionComputation

    @intersection_computation.setter
    def intersection_computation(self, value):
        """
        :param bool value:
        """

        self.hybrid_shape_split.IntersectionComputation = value

    @property
    def orientation(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property Orientation() As long
                | 
                |     Returns or sets the orientation used to compute the split.
                |     Role:
                |     Orientation specifies kept parts of cut feature.
                | 
                |     When splitting a surface by a surface :
                |     - If orientation value is 1: kept parts are specified by the "natural"
                |     normal to the cutting feature
                |     - If orientation value -1: kept parts are specified by the inverse of the
                |     "natural" normal to the cutting feature
                | 
                |     When splitting a surface by a curve :
                |     - If orientation value is 1: kept parts are specified by the result of the cross product :
                |         normal(surface)^tangent(curve)
                |     - If orientation value is -1: Kept parts are specified by the inverse of the result of the cross
                |         product : normal(surface)^tangent(curve)
                | 
                |     When splitting a curve by a point or a curve (without support specified)
                |     :
                |     - If orientation value is 1: Kept parts are from beginning of the curve to
                |     the first intersection,
                |     and, if there is one, from the second to the third intersection and so on
                |     until the end of the curve.
                |     - If orientation value is -1: Kept parts are from the first intersection to
                |     the second (if there is one),
                |     and, if there is one, from the third to the fourth and so on until the end
                |     of the curve.
                | 
                |     When splitting a curve on support:
                |     - If orientation value is 1: Kept parts are specified by the result of the cross product :
                |         normal(support surface)^tangent(cutting curve)
                |     - If orientation value is -1: Kept parts are specified by the inverse of the result of the cross
                |         product : normal(support surface)^tangent(cutting curve)
                | 
                |     When splitting a curve by a surface:
                |     - If orientation value is 1: Kept parts are specified by the inverse of the
                |     normal to the surface
                |     - If orientation value is -1: Kept parts are specified by the normal to the
                |     surface
                | 
                |     Example
                |         This example retrieves in OrientValue the orientation value for the
                |         Split hybrid shape feature.
                | 
                |          Dim OrientValue As long
                |          Set OrientValue = Split.Orientation

        :return: int
        """

        return self.hybrid_shape_split.Orientation

    @orientation.setter
    def orientation(self, value):
        """
        :param int value:
        """

        self.hybrid_shape_split.Orientation = value

    @property
    def support(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property Support() As Reference
                | 
                |     Returns or sets the support element.
                |     This support element may not exist.
                |     Sub-element(s) supported (see Boundary object): Face.
                | 
                |     Example:
                |         This example retrieves in Element the support element for the Split
                |         hybrid shape feature.
                | 
                |          Dim Element As Reference
                |          Set Element = Split.Support

        :return: Reference
        """

        return Reference(self.hybrid_shape_split.Support)

    @support.setter
    def support(self, value):
        """
        :param Reference value:
        """

        self.hybrid_shape_split.Support = value

    @property
    def volume_result(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property VolumeResult() As long
                | 
                |     Returns or sets the Result Type.
                |     Result type:
                | 
                |         : 0 -> Surface
                |         : 1 -> Volume
                |         , The resultant split will be volume. If input is element to cut is
                |         volume. 
                | 
                | 
                |     Note: Setting volume result requires GSO License.
                | 
                |     Example: This example retrieves in ResultType the result type for the Split
                |     hybrid shape feature.
                | 
                |      Dim RType As long
                |      Set RType = Split.ResultType

        :return: int
        """

        return self.hybrid_shape_split.VolumeResult

    @volume_result.setter
    def volume_result(self, value):
        """
        :param int value:
        """

        self.hybrid_shape_split.VolumeResult = value

    def add_cutting_elem(self, i_elem, i_orientation):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub AddCuttingElem(Reference iElem,
                | long iOrientation)
                | 
                |     Adds a cutting feature.
                | 
                |     Parameters:
                | 
                |         iElem
                |             cutting feature 
                |         iOrientation
                |             Orientation
                |                 iOrientation = 1 : SameOrientation = -1 : InvertOrientation = 2 : KoOrientation

        :param Reference i_elem:
        :param int i_orientation:
        :return: None
        """
        return self.hybrid_shape_split.AddCuttingElem(i_elem.com_object, i_orientation)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'add_cutting_elem'
        # # vba_code = """
        # # Public Function add_cutting_elem(hybrid_shape_split)
        # #     Dim iElem (2)
        # #     hybrid_shape_split.AddCuttingElem iElem
        # #     add_cutting_elem = iElem
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def add_element_to_keep(self, i_element):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub AddElementToKeep(Reference iElement)
                | 
                |     Adds an element to specifications. This element will be
                |     kept.
                | 
                |     Parameters:
                | 
                |         iElement
                |             Element to keep.

        :param Reference i_element:
        :return: None
        """
        return self.hybrid_shape_split.AddElementToKeep(i_element.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'add_element_to_keep'
        # # vba_code = """
        # # Public Function add_element_to_keep(hybrid_shape_split)
        # #     Dim iElement (2)
        # #     hybrid_shape_split.AddElementToKeep iElement
        # #     add_element_to_keep = iElement
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def add_element_to_remove(self, i_element):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub AddElementToRemove(Reference iElement)
                | 
                |     Adds an element to specifications. This element will be
                |     removed.
                | 
                |     Parameters:
                | 
                |         iElement
                |             Element to remove.

        :param Reference i_element:
        :return: None
        """
        return self.hybrid_shape_split.AddElementToRemove(i_element.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'add_element_to_remove'
        # # vba_code = """
        # # Public Function add_element_to_remove(hybrid_shape_split)
        # #     Dim iElement (2)
        # #     hybrid_shape_split.AddElementToRemove iElement
        # #     add_element_to_remove = iElement
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_cutting_elem(self, i_rank):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func GetCuttingElem(long iRank) As Reference
                | 
                |     Gets the cutting feature at a given index (a point, a curve or a
                |     surface).
                | 
                |     Parameters:
                | 
                |         oElem
                |             cutting feature 
                |         iRank
                |             Index of one of the cutting features

        :param int i_rank:
        :return: Reference
        """
        return Reference(self.hybrid_shape_split.GetCuttingElem(i_rank))

    def get_intersection(self, i_rank):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func GetIntersection(long iRank) As Reference
                | 
                |     Gets the intersection at a given index.
                | 
                |     Parameters:
                | 
                |         oElem
                |             Intersection 
                |         iRank
                |             Index of one of the intersection features

        :param int i_rank:
        :return: Reference
        """
        return Reference(self.hybrid_shape_split.GetIntersection(i_rank))

    def get_kept_elem(self, i_rank):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func GetKeptElem(long iRank) As Reference
                | 
                |     Gets the kept feature at a given index.
                | 
                |     Parameters:
                | 
                |         oElem
                |             Kept feature 
                |         iRank
                |             Index of one of the kept features

        :param int i_rank:
        :return: Reference
        """
        return Reference(self.hybrid_shape_split.GetKeptElem(i_rank))

    def get_nb_cutting_elem(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func GetNbCuttingElem() As long
                | 
                |     Gets the number of cutting features.
                | 
                |     Parameters:
                | 
                |         oNbCuttingElem
                |             Number of cutting features

        :return: int
        """
        return self.hybrid_shape_split.GetNbCuttingElem()

    def get_nb_elements_to_keep(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func GetNbElementsToKeep() As long
                | 
                |     Gets the number of elements to keep.
                | 
                |     Parameters:
                | 
                |         oNbElementsToKeep
                |             Number of elements to keep

        :return: int
        """
        return self.hybrid_shape_split.GetNbElementsToKeep()

    def get_nb_elements_to_remove(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func GetNbElementsToRemove() As long
                | 
                |     Gets the number of elements to remove.
                | 
                |     Parameters:
                | 
                |         oNbElementsToRemove
                |             Number of elements to remove

        :return: int
        """
        return self.hybrid_shape_split.GetNbElementsToRemove()

    def get_orientation(self, i_rank):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func GetOrientation(long iRank) As long
                | 
                |     Gets Orientation used to compute the split.
                | 
                |     Parameters:
                | 
                |         oOrientation
                |             Orientation 
                |         iRank
                |             index of the cutting feature oOrientation = 1 : SameOrientation = -1 :
                |             InvertOrientation = 2 : KoOrientation

        :param int i_rank:
        :return: int
        """
        return self.hybrid_shape_split.GetOrientation(i_rank)

    def get_other_side(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func GetOtherSide() As Reference
                | 
                |     Gets the other side.
                | 
                |     Parameters:
                | 
                |         oElem
                |             Other side

        :return: Reference
        """
        return Reference(self.hybrid_shape_split.GetOtherSide())

    def get_removed_elem(self, i_rank):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func GetRemovedElem(long iRank) As Reference
                | 
                |     Gets the removed feature at a given index.
                | 
                |     Parameters:
                | 
                |         oElem
                |             Removed feature 
                |         iRank
                |             Index of one of the removed features

        :param int i_rank:
        :return: Reference
        """
        return Reference(self.hybrid_shape_split.GetRemovedElem(i_rank))

    def invert_orientation(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub InvertOrientation()
                | 
                |     Inverts the orientation used to compute the split.

        :return: None
        """
        return self.hybrid_shape_split.InvertOrientation()

    def remove_cutting_elem(self, i_elem):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub RemoveCuttingElem(Reference iElem)
                | 
                |     Removes a cutting feature.
                | 
                |     Parameters:
                | 
                |         iElem
                |             cutting feature

        :param Reference i_elem:
        :return: None
        """
        return self.hybrid_shape_split.RemoveCuttingElem(i_elem.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'remove_cutting_elem'
        # # vba_code = """
        # # Public Function remove_cutting_elem(hybrid_shape_split)
        # #     Dim iElem (2)
        # #     hybrid_shape_split.RemoveCuttingElem iElem
        # #     remove_cutting_elem = iElem
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def remove_element_to_keep(self, i_rank):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub RemoveElementToKeep(long iRank)
                | 
                |     Removes an element from specifications.
                | 
                |     Parameters:
                | 
                |         iRank
                |             Index of the kept element.

        :param int i_rank:
        :return: None
        """
        return self.hybrid_shape_split.RemoveElementToKeep(i_rank)

    def remove_element_to_remove(self, i_rank):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub RemoveElementToRemove(long iRank)
                | 
                |     Removes an element from specifications.
                | 
                |     Parameters:
                | 
                |         iRank
                |             Index of the removed element.

        :param int i_rank:
        :return: None
        """
        return self.hybrid_shape_split.RemoveElementToRemove(i_rank)

    def set_orientation(self, i_rank, i_orientation):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub SetOrientation(long iRank,
                | long iOrientation)
                | 
                |     Sets the orientation used to compute the split.
                | 
                |     Parameters:
                | 
                |         iOrientation
                |             Orientation 
                |         iRank
                |             index of the cutting feature iOrientation = 1 : SameOrientation = -1 :
                |             InvertOrientation = 2 : KoOrientation

        :param int i_rank:
        :param int i_orientation:
        :return: None
        """
        return self.hybrid_shape_split.SetOrientation(i_rank, i_orientation)

    def __repr__(self):
        return f'HybridShapeSplit(name="{self.name}")'
