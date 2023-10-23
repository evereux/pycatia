#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-07-06 14:02:20.222384

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.in_interfaces.reference import Reference
from pycatia.mec_mod_interfaces.hybrid_shape import HybridShape


class HybridShapeTrim(HybridShape):
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
                |                         HybridShapeTrim
                | 
                | Represents the hybrid shape trim object.
                | Role: To access the data of the hybrid shape trim object. This data
                | includes:
                | 
                |     The first element (surface or curve) to be trimmed
                |     The second element (surface or curve) to be trimmed
                |     The orientation corresponding to the first element
                |     The orientation corresponding to the second element
                | 
                | Use the CATIAHybridShapeFactory to create a HybridShapeTrim
                | object.
                | 
                | See also:
                |     HybridShapeFactory
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_trim = com_object

    @property
    def automatic_extrapolation_mode(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property AutomaticExtrapolationMode() As boolean
                | 
                |     Gets or sets the automatic extrapolation mode status. AutomaticExtrapolationMode
                |     TRUE : Automatic extrapolation mode is on.
                |     FALSE : Automatic extrapolation mode is off.
                |
                |     This example retrieves in AutoExtrapolMode the automatic extrapolation mode status for the
                |     Trim hybrid shape feature.
                | 
                |      Dim AutoExtrapolMode As boolean
                |      AutoExtrapolMode = Trim.AutomaticExtrapolationMode

        :rtype: bool
        """

        return self.hybrid_shape_trim.AutomaticExtrapolationMode

    @automatic_extrapolation_mode.setter
    def automatic_extrapolation_mode(self, value: bool):
        """
        :param bool value:
        """

        self.hybrid_shape_trim.AutomaticExtrapolationMode = value

    @property
    def connex(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Connex() As boolean
                | 
                |     Gets or sets connected mode.
                |     Connex
                |     TRUE : the check of connexity is enable. Connex
                |     FALSE : the check of connexity is disable.
                |
                |     This example retrieves in Connex the connected mode for the Trim hybrid shape feature.
                | 
                |      Dim Connex As boolean
                |      Connex = Trim.Connex

        :rtype: bool
        """

        return self.hybrid_shape_trim.Connex

    @connex.setter
    def connex(self, value: bool):
        """
        :param bool value:
        """

        self.hybrid_shape_trim.Connex = value

    @property
    def first_elem(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property FirstElem() As Reference
                | 
                |     Deprecated:
                |         V5R17 CATIAHybridShapeTrim#GetElem Returns or sets the first element to
                |         be trimmed. 
                |     Example:
                | 
                |           This example retrieves in Surface1 the first element to be trimmed
                |           
                |          for the hybTrim hybrid shape feature.
                |          
                | 
                |          Dim Surface1 As Reference
                |          Set Surface1 = hybTrim.FirstElem

        :rtype: Reference
        """

        return Reference(self.hybrid_shape_trim.FirstElem)

    @first_elem.setter
    def first_elem(self, reference_element: Reference):
        """
        :param Reference reference_element:
        """

        self.hybrid_shape_trim.FirstElem = reference_element.com_object

    @property
    def first_orientation(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property FirstOrientation() As long
                | 
                |     Deprecated:
                |         V5R17 CATIAHybridShapeTrim#GetPreviousOrientation Returns or sets the
                |         first orientation used to compute the trim.
                |         Role: The orientation specifies the kept parts of the first element to
                |         be trimmed.
                | 
                |             When trimming surfaces:
                |                 If orientation value is 1: kept parts are specified by the
                |                 "natural" normal to the second object
                |                 If orientation value is -1: kept parts are specified by the
                |                 inverse of the "natural" normal to the second
                |                 object
                |             When trimming curves:
                |                 If orientation value is 1: kept parts are from the beginning of
                |                 the curve to the first intersection, and, if there is one, from the second to
                |                 the third intersection and so on until the end of the
                |                 curve
                |                 If orientation value is -1: kept parts are from the first
                |                 intersection to the second (if there is one), and, if there is one, from the
                |                 third to the fourth and so on until the end of the
                |                 curve.
                | 
                |     Example:
                | 
                |           This example retrieves in firstOrient the orientation
                |           of
                |          the first element used by the hybTrim hybrid shape
                |          feature.
                | 
                |          Dim firstOrient As long
                |          Set firstOrient = hybTrim.FirstOrientation

        :rtype: int
        """

        return self.hybrid_shape_trim.FirstOrientation

    @first_orientation.setter
    def first_orientation(self, value: int):
        """
        :param int value:
        """

        self.hybrid_shape_trim.FirstOrientation = value

    @property
    def intersection_computation(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property IntersectionComputation() As boolean
                | 
                |     Gets or sets Intersection computation mode.
                |    IntersectionComputation
                |    TRUE : Intersection is computed.
                |    FALSE : Intersection is not computed.
                |
                |     This example retrieves in Intersection the Intersection computation mode for the Trim hybrid
                |     shape feature.
                | 
                |      Dim Intersection As boolean
                |      Intersection = Trim.IntersectionComputation

        :rtype: bool
        """

        return self.hybrid_shape_trim.IntersectionComputation

    @intersection_computation.setter
    def intersection_computation(self, value: bool):
        """
        :param bool value:
        """

        self.hybrid_shape_trim.IntersectionComputation = value

    @property
    def keep_all_pieces(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property KeepAllPieces() As boolean
                | 
                |     Gets or Sets keep all pieces mode. Used for the trim pieces of shells only KeepAllPieces=
                |     TRUE : all the pieces are kept during update, KeepAllPieces=
                |     FALSE : only chosen pieces are kept during update (default).
                |
                |     This example retrieves in KeepAllPieces the Keep All Pieces mode for the Trim hybrid shape
                |     feature.
                | 
                |      Dim bKeepAllPieces As boolean
                |      bKeepAllPieces = Trim.KeepAllPieces

        :rtype: bool
        """

        return self.hybrid_shape_trim.KeepAllPieces

    @keep_all_pieces.setter
    def keep_all_pieces(self, value: bool):
        """
        :param bool value:
        """

        self.hybrid_shape_trim.KeepAllPieces = value

    @property
    def manifold(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Manifold() As boolean
                | 
                |     Gets or sets manifold mode.
                |     Manifold = TRUE : the check of manifold is enable.
                |     Manifold = FALSE : the check of manifold is disable.
                |
                |     This example retrieves in Manifold the manifold mode for the Trim hybrid shape feature.
                | 
                |      Dim Manifold As boolean
                |      Connex = Trim.Manifold

        :rtype: bool
        """

        return self.hybrid_shape_trim.Manifold

    @manifold.setter
    def manifold(self, value: bool):
        """
        :param bool value:
        """

        self.hybrid_shape_trim.Manifold = value

    @property
    def mode(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Mode() As long
                | 
                |    Gets or sets Trim mode. Mode =
                |    1 : Standard. =
                |    2 : Pieces.
                |
                |    This example retrieves in Mode the mode for the Trim hybrid shape feature.
                | 
                |    Dim Mode As long
                |    Mode = Trim.Mode

        :rtype: int
        """

        return self.hybrid_shape_trim.Mode

    @mode.setter
    def mode(self, value: int):
        """
        :param int value:
        """

        self.hybrid_shape_trim.Mode = value

    @property
    def second_elem(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property SecondElem() As Reference
                | 
                |     Deprecated:
                |         V5R17 CATIAHybridShapeTrim#GetElem Returns or sets the second element
                |         to be trimmed. 
                |     Example:
                | 
                |           This example retrieves in Surface2 the second element to be trimmed
                |           
                |          for the hybTrim hybrid shape trim object.
                |          
                | 
                |          Dim Surface2 As Reference
                |          Set Surface2 = hybTrim.SecondElem

        :rtype: Reference
        """

        return Reference(self.hybrid_shape_trim.SecondElem)

    @second_elem.setter
    def second_elem(self, reference_element: Reference):
        """
        :param Reference reference_element:
        """

        self.hybrid_shape_trim.SecondElem = reference_element.com_object

    @property
    def second_orientation(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property SecondOrientation() As long
                | 
                |     Deprecated:
                |         V5R17 CATIAHybridShapeTrim#GetPreviousOrientation Returns or sets the
                |         second orientation used to compute the trim.
                |         Role: The orientation specifies the kept parts of the second element to
                |         be trimmed.
                | 
                |             When trimming surfaces:
                |                 If orientation value is 1: kept parts are specified by the
                |                 "natural" normal to the first object
                |                 If orientation value is -1: kept parts are specified by the
                |                 inverse of the "natural" normal to the first
                |                 object
                |             When trimming curves:
                |                 If orientation value is 1: kept parts are from the beginning of
                |                 the curve to the first intersection, and, if there is one, from the second to
                |                 the third intersection and so on until the end of the
                |                 curve
                |                 If orientation value is -1: kept parts are from the first
                |                 intersection to the second (if there is one), and, if there is one, from the
                |                 third to the fourth and so on until the end of the
                |                 curve.
                | 
                |     Example:
                | 
                |           This example retrieves in secondOrient the orientation
                |           of
                |          the second element used by the hybTrim hybrid shape trim
                |          object.
                | 
                |          Dim secondOrient As long
                |          Set secondOrient = hybTrim.SecondOrientation

        :rtype: int
        """

        return self.hybrid_shape_trim.SecondOrientation

    @second_orientation.setter
    def second_orientation(self, value: int):
        """
        :param int value:
        """

        self.hybrid_shape_trim.SecondOrientation = value

    @property
    def simplify(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Simplify() As boolean
                | 
                |     Returns or sets whether the simplification of the resulting topology is or
                |     should be activated.
                |     Legal values: True to activate the simplification, and False
                |     otherwise.
                | 
                |     Example:
                | 
                |            This example activates the simplification of the resulting topology
                |            of
                |          the hybTrim hybrid shape trim object.
                |          
                | 
                |           hybTrim.Simplify = True

        :rtype: bool
        """

        return self.hybrid_shape_trim.Simplify

    @simplify.setter
    def simplify(self, value: bool):
        """
        :param bool value:
        """

        self.hybrid_shape_trim.Simplify = value

    @property
    def support(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Support() As Reference
                | 
                |     Returns or sets the support element.
                |     This support element may not exist.
                |     Sub-element(s) supported (see Boundary object): Face.
                | 
                |     Example:
                | 
                |           This example retrieves in supportElement the support
                |           element
                |          of the hybTrim hybrid shape trim object.
                |          
                | 
                |          Dim supportElement As Reference
                |          Set supportElement = hybTrim.Support

        :rtype: Reference
        """

        return Reference(self.hybrid_shape_trim.Support)

    @support.setter
    def support(self, reference_support: Reference):
        """
        :param Reference reference_support:
        """

        self.hybrid_shape_trim.Support = reference_support.com_object

    def add_element_to_keep(self, i_element: Reference) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
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
        :rtype: None
        """
        return self.hybrid_shape_trim.AddElementToKeep(i_element.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'add_element_to_keep'
        # # vba_code = """
        # # Public Function add_element_to_keep(hybrid_shape_trim)
        # #     Dim iElement (2)
        # #     hybrid_shape_trim.AddElementToKeep iElement
        # #     add_element_to_keep = iElement
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def add_element_to_remove(self, i_element: Reference) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
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
        :rtype: None
        """
        return self.hybrid_shape_trim.AddElementToRemove(i_element.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'add_element_to_remove'
        # # vba_code = """
        # # Public Function add_element_to_remove(hybrid_shape_trim)
        # #     Dim iElement (2)
        # #     hybrid_shape_trim.AddElementToRemove iElement
        # #     add_element_to_remove = iElement
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def add_piece_cutter(self, i_rank: int, i_cutter_elem: int, i_orientation: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub AddPieceCutter(long iRank,
                | long iCutterElem,
                | long iOrientation)
                | 
                |     Add piece Cutting element and its orientation. Used for trim pieces of
                |     shells only
                | 
                |     Parameters:
                | 
                |         iRank
                |             Index of the trimmed element (piece) 
                |         iCutterElemIdx
                |             index is the index of input shell except in case of multiple intersection between shells
                |             where Index=IndexInputShell+NbInputShells*(1-iw)
                |             (with iw=1... : wire index in case of multiple intersection)
                |         iOrientation
                |             cutter element orientation

        :param int i_rank:
        :param int i_cutter_elem:
        :param int i_orientation:
        :rtype: None
        """
        return self.hybrid_shape_trim.AddPieceCutter(i_rank, i_cutter_elem, i_orientation)

    def get_elem(self, i_rank: int) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetElem(long iRank) As Reference
                | 
                |     Gets the trimmed feature at a given index.
                | 
                |     Parameters:
                | 
                |         iRank
                |             Index of one of the trimmed features 
                |         oElem
                |             trimmed feature

        :param int i_rank:
        :rtype: Reference
        """
        return Reference(self.hybrid_shape_trim.GetElem(i_rank))

    def get_kept_elem(self, i_rank: int) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
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
        :rtype: Reference
        """
        return Reference(self.hybrid_shape_trim.GetKeptElem(i_rank))

    def get_nb_elem(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetNbElem() As long
                | 
                |     Gets the number of elements: couple(element, index of portion to keep on
                |     element).
                | 
                |     Parameters:
                | 
                |         oNbElem
                |             Number of elements

        :rtype: int
        """
        return self.hybrid_shape_trim.GetNbElem()

    def get_nb_elements_to_keep(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetNbElementsToKeep() As long
                | 
                |     Gets the number of elements to keep.
                | 
                |     Parameters:
                | 
                |         oNbElementsToKeep
                |             Number of elements to keep

        :rtype: int
        """
        return self.hybrid_shape_trim.GetNbElementsToKeep()

    def get_nb_elements_to_remove(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetNbElementsToRemove() As long
                | 
                |     Gets the number of elements to remove.
                | 
                |     Parameters:
                | 
                |         oNbElementsToRemove
                |             Number of elements to remove

        :rtype: int
        """
        return self.hybrid_shape_trim.GetNbElementsToRemove()

    def get_next_orientation(self, i_rank: int) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetNextOrientation(long iRank) As long
                | 
                |     Gets Orientation used to compute the feature, referring to the next trimmed
                |     element.
                | 
                |     Parameters:
                | 
                |         iRank
                |             index (of one of the trimmed features) - 1 iRank must be greater
                |             than 1 and lower than the number of elements - 1 
                |         oOrientation
                |             Orientation

        :param int i_rank:
        :rtype: int
        """
        return self.hybrid_shape_trim.GetNextOrientation(i_rank)

    def get_piece_cutter(self, i_rank: int, i_cutter_index: int, o_cutter_elem_idx: int, o_orientation: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub GetPieceCutter(long iRank,
                | long iCutterIndex,
                | long oCutterElemIdx,
                | long oOrientation)
                | 
                |     Gets piece Cutting element and its orientation. Used for trim pieces of
                |     shells only
                | 
                |     Parameters:
                | 
                |         iRank
                |             Index of the trimmed element (piece) 
                |         oCutterElemIdx
                |             index is the index of input shell except in case of multiple intersection between shells
                |             where Index=IndexInputShell+NbInputShells*(1-iw)
                |             (with iw=1... : wire index in case of multiple intersection)
                |         oCutterElem
                |             cutter element 
                |         oOrientation
                |             cutter element orientation

        :param int i_rank:
        :param int i_cutter_index:
        :param int o_cutter_elem_idx:
        :param int o_orientation:
        :rtype: None
        """
        return self.hybrid_shape_trim.GetPieceCutter(i_rank, i_cutter_index, o_cutter_elem_idx, o_orientation)

    def get_piece_discrimination_index(self, i_rank: int, o_index: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub GetPieceDiscriminationIndex(long iRank,
                | long oIndex)
                | 
                |     Gets the discrimination index. Used for the trim pieces of shells
                |     only
                | 
                |     Parameters:
                | 
                |         iRank
                |             Index of the trimmed element (piece) 
                |         oIndex
                |             Discrimination Index Used to discrimine pieces when cutters
                |             orientations are not enough

        :param int i_rank:
        :param int o_index:
        :rtype: None
        """
        return self.hybrid_shape_trim.GetPieceDiscriminationIndex(i_rank, o_index)

    def get_piece_nb_cutters(self, i_rank: int) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetPieceNbCutters(long iRank) As long
                | 
                |     Gets the number of cutters of a piece. Used for trim pieces of shells
                |     only
                | 
                |     Parameters:
                | 
                |         oNbCutters
                |             Number of cutters (except in case of multiple intersection between
                |             shells)

        :param int i_rank:
        :rtype: int
        """
        return self.hybrid_shape_trim.GetPieceNbCutters(i_rank)

    def get_portion_to_keep(self, i_rank: int) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetPortionToKeep(long iRank) As long
                | 
                |     Gets a portion to keep number, giving the index of the element. Used for
                |     trim pieces of wires
                | 
                |     Parameters:
                | 
                |         oPortionNumber
                |             Index of portion to keep on the element 
                |         iRank
                |             Index of the trimmed element

        :param int i_rank:
        :rtype: int
        """
        return self.hybrid_shape_trim.GetPortionToKeep(i_rank)

    def get_previous_orientation(self, i_rank: int) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetPreviousOrientation(long iRank) As long
                | 
                |     Gets Orientation used to compute the feature, referring to the previous
                |     trimmed element.
                | 
                |     Parameters:
                | 
                |         iRank
                |             index (of one of the trimmed features) - 1 iRank must be greater
                |             than 1 and lower than the number of elements - 1 
                |         oOrientation
                |             Orientation

        :param int i_rank:
        :rtype: int
        """
        return self.hybrid_shape_trim.GetPreviousOrientation(i_rank)

    def get_removed_elem(self, i_rank: int) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
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
        :rtype: Reference
        """
        return Reference(self.hybrid_shape_trim.GetRemovedElem(i_rank))

    def invert_first_orientation(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub InvertFirstOrientation()
                | 
                |     Deprecated:
                |         V5R17 CATIAHybridShapeTrim#SetPreviousOrientation Inverts the first
                |         orientation used to compute the trim. 
                |     Example:
                | 
                |           This example inverts the first orientation to
                |           compute
                |          the hybTrim hybrid shape trim object.
                | 
                |          hybTrim.InvertFirstOrientation

        :rtype: None
        """
        return self.hybrid_shape_trim.InvertFirstOrientation()

    def invert_second_orientation(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub InvertSecondOrientation()
                | 
                |     Deprecated:
                |         V5R17 CATIAHybridShapeTrim#SetPreviousOrientation Inverts the second
                |         orientation used to compute the trim. This example inverts the first
                |         orientation to compute the hybTrim hybrid shape trim
                |         object.
                | 
                |          hybTrim.InvertSecondOrientation

        :rtype: None
        """
        return self.hybrid_shape_trim.InvertSecondOrientation()

    def remove_element_to_keep(self, i_rank: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub RemoveElementToKeep(long iRank)
                | 
                |     Removes an element from specifications.
                | 
                |     Parameters:
                | 
                |         iRank
                |             Index of the kept element.

        :param int i_rank:
        :rtype: None
        """
        return self.hybrid_shape_trim.RemoveElementToKeep(i_rank)

    def remove_element_to_remove(self, i_rank: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub RemoveElementToRemove(long iRank)
                | 
                |     Removes an element from specifications.
                | 
                |     Parameters:
                | 
                |         iRank
                |             Index of the removed element.

        :param int i_rank:
        :rtype: None
        """
        return self.hybrid_shape_trim.RemoveElementToRemove(i_rank)

    def remove_piece_cutter(self, i_rank: int, i_cutter_index: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub RemovePieceCutter(long iRank,
                | long iCutterIndex)
                | 
                |     Remove piece Cutting element and its orientation. Used for trim pieces of
                |     shells only
                | 
                |     Parameters:
                | 
                |         iRank
                |             Index of the trimmed element (piece) 
                |         iCutterIndex
                |             Index in cutters list

        :param int i_rank:
        :param int i_cutter_index:
        :rtype: None
        """
        return self.hybrid_shape_trim.RemovePieceCutter(i_rank, i_cutter_index)

    def set_elem(self, i_rank: int, i_elem: Reference) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetElem(long iRank,
                | Reference iElem)
                | 
                |     Modifies the trimmed feature at a given index. Use AddElem method to
                |     specify a new trimmed element
                | 
                |     Parameters:
                | 
                |         iRank
                |             Index of one of the trimmed features 
                |         iElem
                |             trimmed feature

        :param int i_rank:
        :param Reference i_elem:
        :rtype: None
        """
        return self.hybrid_shape_trim.SetElem(i_rank, i_elem.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_elem'
        # # vba_code = """
        # # Public Function set_elem(hybrid_shape_trim)
        # #     Dim iRank (2)
        # #     hybrid_shape_trim.SetElem iRank
        # #     set_elem = iRank
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_next_orientation(self, i_rank: int, i_orientation: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetNextOrientation(long iRank,
                | long iOrientation)
                | 
                |     Sets the orientation used to compute the feature, referring to the next
                |     trimmed element.
                | 
                |     Parameters:
                | 
                |         iRank
                |             index (of one of the trimmed features) - 1 iRank must be greater
                |             than 1 and lower than the number of elements - 1 
                |         iOrientation
                |             Orientation

        :param int i_rank:
        :param int i_orientation:
        :rtype: None
        """
        return self.hybrid_shape_trim.SetNextOrientation(i_rank, i_orientation)

    def set_piece_discrimination_index(self, i_rank: int, i_index: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetPieceDiscriminationIndex(long iRank,
                | long iIndex)
                | 
                |     Sets the discrimination index. Used for the trim pieces of shells
                |     only
                | 
                |     Parameters:
                | 
                |         iRank
                |             Index of the trimmed element (piece) 
                |         iIndex
                |             Discrimination Index Used to discrimine pieces when cutters
                |             orientations are not enough

        :param int i_rank:
        :param int i_index:
        :rtype: None
        """
        return self.hybrid_shape_trim.SetPieceDiscriminationIndex(i_rank, i_index)

    def set_portion_to_keep(self, i_rank: int, i_portion_number: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetPortionToKeep(long iRank,
                | long iPortionNumber)
                | 
                |     Sets a portion to keep number in Pieces mode. Used for trim pieces of
                |     wires
                | 
                |     Parameters:
                | 
                |         iRank
                |             Index of the trimmed element 
                |         iPortionNumber
                |             Index of portion to keep on the element

        :param int i_rank:
        :param int i_portion_number:
        :rtype: None
        """
        return self.hybrid_shape_trim.SetPortionToKeep(i_rank, i_portion_number)

    def set_previous_orientation(self, i_rank: int, i_orientation: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetPreviousOrientation(long iRank,
                | long iOrientation)
                | 
                |     Sets the orientation used to compute the feature, referring to the previous
                |     trimmed element.
                | 
                |     Parameters:
                | 
                |         iRank
                |             index (of one of the trimmed features) - 1 iRank must be greater
                |             than 1 and lower than the number of elements - 1 
                |         iOrientation
                |             Orientation

        :param int i_rank:
        :param int i_orientation:
        :rtype: None
        """
        return self.hybrid_shape_trim.SetPreviousOrientation(i_rank, i_orientation)

    def __repr__(self):
        return f'HybridShapeTrim(name="{self.name}")'
