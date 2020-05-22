#! /usr/bin/python3.6
# module initially auto generated using V5Automation.chm from CATIA R25 on 2020-05-22 12:54:36.956119

from pycatia.mec_mod_interfaces.hybridshape import HybridShape


class HybridShapeTrim(HybridShape):
    """
        .. note::
            CAA V5 Visual Basic help

                | Represents the hybrid shape trim object.Role: To access the data of
                | the hybrid shape trim object. This data includes:Use the
                | CATIAHybridShapeFactory to create a HybridShapeTrim object.

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_trim = com_object     

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
                | extrapolation mode status for the Trim hybrid shape feature.
                | Dim AutoExtrapolMode As boolean AutoExtrapolMode =
                | Trim.AutomaticExtrapolationMode

        :return:
        """
        return self.hybrid_shape_trim.AutomaticExtrapolationMode

    @property
    def connex(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Connex
                | o Property Connex(    ) As
                | 
                | Gets or sets connected mode. Connex = TRUE : the check of
                | connexity is enable. Connex = FALSE : the check of connexity
                | is disable. This example retrieves in Connex the connected
                | mode for the Trim hybrid shape feature. Dim Connex As
                | boolean Connex = Trim.Connex

        :return:
        """
        return self.hybrid_shape_trim.Connex

    @property
    def first_elem(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | FirstElem
                | o Property FirstElem(    ) As
                | 
                | Deprecated: V5R17 CATIAHybridShapeTrim#GetElem Returns or
                | sets the first element to be trimmed. 
                |
                | Example:
                | This example
                | retrieves in Surface1 the first element to be trimmed for
                | the hybTrim hybrid shape feature. Dim Surface1 As Reference
                | Set Surface1 = hybTrim.FirstElem

        :return:
        """
        return self.hybrid_shape_trim.FirstElem

    @first_elem.setter
    def first_elem(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_trim.FirstElem = value 

    @property
    def first_orientation(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | FirstOrientation
                | o Property FirstOrientation(    ) As
                | 
                | Deprecated: V5R17
                | CATIAHybridShapeTrim#GetPreviousOrientation Returns or sets
                | the first orientation used to compute the trim. Role: The
                | orientation specifies the kept parts of the first element to
                | be trimmed. When trimming surfaces: If orientation value is
                | 1: kept parts are specified by the "natural" normal to the
                | second object If orientation value is -1: kept parts are
                | specified by the inverse of the "natural" normal to the
                | second object When trimming curves: If orientation value is
                | 1: kept parts are from the beginning of the curve to the
                | first intersection, and, if there is one, from the second to
                | the third intersection and so on until the end of the curve
                | If orientation value is -1: kept parts are from the first
                | intersection to the second (if there is one), and, if there
                | is one, from the third to the fourth and so on until the end
                | of the curve. 
                |
                | Example:
                | This example retrieves in firstOrient
                | the orientation of the first element used by the hybTrim
                | hybrid shape feature. Dim firstOrient As long Set
                | firstOrient = hybTrim.FirstOrientation

        :return:
        """
        return self.hybrid_shape_trim.FirstOrientation

    @first_orientation.setter
    def first_orientation(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_trim.FirstOrientation = value 

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
                | Trim hybrid shape feature. Dim Intersection As boolean
                | Intersection = Trim.IntersectionComputation

        :return:
        """
        return self.hybrid_shape_trim.IntersectionComputation

    @property
    def keep_all_pieces(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | KeepAllPieces
                | o Property KeepAllPieces(    ) As
                | 
                | Gets or Sets keep all pieces mode. Used for the trim pieces
                | of shells only KeepAllPieces=TRUE : all the pieces are kept
                | during update, KeepAllPieces=FALSE : only chosen pieces are
                | kept during update (default). This example retrieves in
                | KeepAllPieces the Keep All Pieces mode for the Trim hybrid
                | shape feature. Dim bKeepAllPieces As boolean bKeepAllPieces
                | = Trim.KeepAllPieces

        :return:
        """
        return self.hybrid_shape_trim.KeepAllPieces

    @property
    def manifold(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Manifold
                | o Property Manifold(    ) As
                | 
                | Gets or sets manifold mode. Manifold = TRUE : the check of
                | manifold is enable. Manifold = FALSE : the check of manifold
                | is disable. This example retrieves in Manifold the manifold
                | mode for the Trim hybrid shape feature. Dim Manifold As
                | boolean Connex = Trim.Manifold

        :return:
        """
        return self.hybrid_shape_trim.Manifold

    @property
    def mode(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Mode
                | o Property Mode(    ) As
                | 
                | Gets or sets Trim mode. Mode = 1 : Standard. = 2 : Pieces.
                | This example retrieves in Mode the mode for the Trim hybrid
                | shape feature. Dim Mode As long Mode = Trim.Mode

        :return:
        """
        return self.hybrid_shape_trim.Mode

    @property
    def second_elem(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | SecondElem
                | o Property SecondElem(    ) As
                | 
                | Deprecated: V5R17 CATIAHybridShapeTrim#GetElem Returns or
                | sets the second element to be trimmed. 
                |
                | Example:
                | This example
                | retrieves in Surface2 the second element to be trimmed for
                | the hybTrim hybrid shape trim object. Dim Surface2 As
                | Reference Set Surface2 = hybTrim.SecondElem

        :return:
        """
        return self.hybrid_shape_trim.SecondElem

    @second_elem.setter
    def second_elem(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_trim.SecondElem = value 

    @property
    def second_orientation(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | SecondOrientation
                | o Property SecondOrientation(    ) As
                | 
                | Deprecated: V5R17
                | CATIAHybridShapeTrim#GetPreviousOrientation Returns or sets
                | the second orientation used to compute the trim. Role: The
                | orientation specifies the kept parts of the second element
                | to be trimmed. When trimming surfaces: If orientation value
                | is 1: kept parts are specified by the "natural" normal to
                | the first object If orientation value is -1: kept parts are
                | specified by the inverse of the "natural" normal to the
                | first object When trimming curves: If orientation value is
                | 1: kept parts are from the beginning of the curve to the
                | first intersection, and, if there is one, from the second to
                | the third intersection and so on until the end of the curve
                | If orientation value is -1: kept parts are from the first
                | intersection to the second (if there is one), and, if there
                | is one, from the third to the fourth and so on until the end
                | of the curve. 
                |
                | Example:
                | This example retrieves in
                | secondOrient the orientation of the second element used by
                | the hybTrim hybrid shape trim object. Dim secondOrient As
                | long Set secondOrient = hybTrim.SecondOrientation

        :return:
        """
        return self.hybrid_shape_trim.SecondOrientation

    @second_orientation.setter
    def second_orientation(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_trim.SecondOrientation = value 

    @property
    def simplify(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Simplify
                | o Property Simplify(    ) As
                | 
                | Returns or sets whether the simplification of the resulting
                | topology is or should be activated. Legal values: True to
                | activate the simplification, and False otherwise. Example:
                | This example activates the simplification of the resulting
                | topology of the hybTrim hybrid shape trim object.
                | hybTrim.Simplify = True

        :return:
        """
        return self.hybrid_shape_trim.Simplify

    @simplify.setter
    def simplify(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_trim.Simplify = value 

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
                | This example retrieves in supportElement the
                | support element of the hybTrim hybrid shape trim object. Dim
                | supportElement As Reference Set supportElement =
                | hybTrim.Support

        :return:
        """
        return self.hybrid_shape_trim.Support

    @support.setter
    def support(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_trim.Support = value 

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
        return self.hybrid_shape_trim.AddElementToKeep(i_element)

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
        return self.hybrid_shape_trim.AddElementToRemove(i_element)

    def add_piece_cutter(self, i_rank, i_cutter_elem, i_orientation):
        """
        .. note::
            CAA V5 Visual Basic help

                | AddPieceCutter
                | o Sub AddPieceCutter(        iRank,
                |                              iCutterElem,
                |                              iOrientation)
                | 
                | Add piece Cutting element and its orientation. Used for trim
                | pieces of shells only
                |
                | Parameters:
                | iRank
                |       Index of the trimmed element (piece)
                |    
                |  iCutterElemIdx
                |      index is the index of input shell
                |      except in case of multiple intersection between shells
                |      where Index=IndexInputShell+NbInputShells*(1-iw) 
                |      (whith iw=1... : wire index in case of multiple intersection)
                |    
                |  iOrientation
                |       cutter element orientation


        :param i_rank:
        :param i_cutter_elem:
        :param i_orientation:
        :return:
        """
        return self.hybrid_shape_trim.AddPieceCutter(i_rank, i_cutter_elem, i_orientation)

    def get_elem(self, i_rank):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetElem
                | o Func GetElem(        iRank) As
                | 
                | Gets the trimmed feature at a given index.
                |
                | Parameters:
                | iRank
                |       Index of one of the trimmed features  
                |    
                |  oElem
                |       trimmed feature


        :param i_rank:
        :return:
        """
        return self.hybrid_shape_trim.GetElem(i_rank)

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
        return self.hybrid_shape_trim.GetKeptElem(i_rank)

    def get_nb_elem(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetNbElem
                | o Func GetNbElem(    ) As
                | 
                | Gets the number of elements: couple(element, index of
                | portion to keep on element).
                |
                | Parameters:
                | oNbElem
                |       Number of elements


        :return:
        """
        return self.hybrid_shape_trim.GetNbElem()

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
        return self.hybrid_shape_trim.GetNbElementsToKeep()

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
        return self.hybrid_shape_trim.GetNbElementsToRemove()

    def get_next_orientation(self, i_rank):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetNextOrientation
                | o Func GetNextOrientation(        iRank) As
                | 
                | Gets Orientation used to compute the feature, referring to
                | the next trimmed element.
                |
                | Parameters:
                | iRank
                |        index (of one of the trimmed features) - 1
                |       iRank must be greater than 1 and lower than the number of elements - 1 
                |    
                |  oOrientation
                |         Orientation


        :param i_rank:
        :return:
        """
        return self.hybrid_shape_trim.GetNextOrientation(i_rank)

    def get_piece_cutter(self, i_rank, i_cutter_index, o_cutter_elem_idx, o_orientation):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetPieceCutter
                | o Sub GetPieceCutter(        iRank,
                |                              iCutterIndex,
                |                              oCutterElemIdx,
                |                              oOrientation)
                | 
                | Gets piece Cutting element and its orientation. Used for
                | trim pieces of shells only
                |
                | Parameters:
                | iRank
                |       Index of the trimmed element (piece)
                |    
                |  oCutterElemIdx
                |      index is the index of input shell
                |      except in case of multiple intersection between shells
                |      where Index=IndexInputShell+NbInputShells*(1-iw) 
                |      (whith iw=1... : wire index in case of multiple intersection)
                |    
                |  oCutterElem
                |       cutter element
                |    
                |  oOrientation
                |       cutter element orientation


        :param i_rank:
        :param i_cutter_index:
        :param o_cutter_elem_idx:
        :param o_orientation:
        :return:
        """
        return self.hybrid_shape_trim.GetPieceCutter(i_rank, i_cutter_index, o_cutter_elem_idx, o_orientation)

    def get_piece_discrimination_index(self, i_rank, o_index):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetPieceDiscriminationIndex
                | o Sub GetPieceDiscriminationIndex(        iRank,
                |                                           oIndex)
                | 
                | Gets the discrimination index. Used for the trim pieces of
                | shells only
                |
                | Parameters:
                | iRank
                |     Index of the trimmed element (piece)
                |    
                |  oIndex
                |     Discrimination Index
                |     Used to discrimine pieces when cutters orientations are not enough


        :param i_rank:
        :param o_index:
        :return:
        """
        return self.hybrid_shape_trim.GetPieceDiscriminationIndex(i_rank, o_index)

    def get_piece_nb_cutters(self, i_rank):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetPieceNbCutters
                | o Func GetPieceNbCutters(        iRank) As
                | 
                | Gets the number of cutters of a piece. Used for trim pieces
                | of shells only
                |
                | Parameters:
                | oNbCutters
                |       Number of cutters (except in case of multiple intersection between shells)


        :param i_rank:
        :return:
        """
        return self.hybrid_shape_trim.GetPieceNbCutters(i_rank)

    def get_portion_to_keep(self, i_rank):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetPortionToKeep
                | o Func GetPortionToKeep(        iRank) As
                | 
                | Gets a portion to keep number, giving the index of the
                | element. Used for trim pieces of wires
                |
                | Parameters:
                | oPortionNumber
                |       Index of portion to keep on the element
                |    
                |  iRank
                |       Index of the trimmed element


        :param i_rank:
        :return:
        """
        return self.hybrid_shape_trim.GetPortionToKeep(i_rank)

    def get_previous_orientation(self, i_rank):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetPreviousOrientation
                | o Func GetPreviousOrientation(        iRank) As
                | 
                | Gets Orientation used to compute the feature, referring to
                | the previous trimmed element.
                |
                | Parameters:
                | iRank
                |        index (of one of the trimmed features) - 1
                |       iRank must be greater than 1 and lower than the number of elements - 1 
                |    
                |  oOrientation
                |         Orientation


        :param i_rank:
        :return:
        """
        return self.hybrid_shape_trim.GetPreviousOrientation(i_rank)

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
        return self.hybrid_shape_trim.GetRemovedElem(i_rank)

    def invert_first_orientation(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | InvertFirstOrientation
                | o Sub InvertFirstOrientation(    )
                | 
                | Deprecated: V5R17
                | CATIAHybridShapeTrim#SetPreviousOrientation Inverts the
                | first orientation used to compute the trim. 
                |
                | Example:
                | This
                | example inverts the first orientation to compute the hybTrim
                | hybrid shape trim object. hybTrim.InvertFirstOrientation
                |
                | Parameters:


        :return:
        """
        return self.hybrid_shape_trim.InvertFirstOrientation()

    def invert_second_orientation(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | InvertSecondOrientation
                | o Sub InvertSecondOrientation(    )
                | 
                | Deprecated: V5R17
                | CATIAHybridShapeTrim#SetPreviousOrientation Inverts the
                | second orientation used to compute the trim. This example
                | inverts the first orientation to compute the hybTrim hybrid
                | shape trim object. hybTrim.InvertSecondOrientation
                |
                | Parameters:


        :return:
        """
        return self.hybrid_shape_trim.InvertSecondOrientation()

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
        return self.hybrid_shape_trim.RemoveElementToKeep(i_rank)

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
        return self.hybrid_shape_trim.RemoveElementToRemove(i_rank)

    def remove_piece_cutter(self, i_rank, i_cutter_index):
        """
        .. note::
            CAA V5 Visual Basic help

                | RemovePieceCutter
                | o Sub RemovePieceCutter(        iRank,
                |                                 iCutterIndex)
                | 
                | Remove piece Cutting element and its orientation. Used for
                | trim pieces of shells only
                |
                | Parameters:
                | iRank
                |       Index of the trimmed element (piece)
                |    
                |  iCutterIndex
                |       Index in cutters list


        :param i_rank:
        :param i_cutter_index:
        :return:
        """
        return self.hybrid_shape_trim.RemovePieceCutter(i_rank, i_cutter_index)

    def set_elem(self, i_rank, i_elem):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetElem
                | o Sub SetElem(        iRank,
                |                       iElem)
                | 
                | Modifies the trimmed feature at a given index. Use AddElem
                | method to specify a new trimmed element
                |
                | Parameters:
                | iRank
                |       Index of one of the trimmed features  
                |    
                |  iElem
                |       trimmed feature


        :param i_rank:
        :param i_elem:
        :return:
        """
        return self.hybrid_shape_trim.SetElem(i_rank, i_elem)

    def set_next_orientation(self, i_rank, i_orientation):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetNextOrientation
                | o Sub SetNextOrientation(        iRank,
                |                                  iOrientation)
                | 
                | Sets the orientation used to compute the feature, referring
                | to the next trimmed element.
                |
                | Parameters:
                | iRank
                |        index (of one of the trimmed features) - 1
                |       iRank must be greater than 1 and lower than the number of elements - 1 
                |    
                |  iOrientation
                |         Orientation


        :param i_rank:
        :param i_orientation:
        :return:
        """
        return self.hybrid_shape_trim.SetNextOrientation(i_rank, i_orientation)

    def set_piece_discrimination_index(self, i_rank, i_index):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetPieceDiscriminationIndex
                | o Sub SetPieceDiscriminationIndex(        iRank,
                |                                           iIndex)
                | 
                | Sets the discrimination index. Used for the trim pieces of
                | shells only
                |
                | Parameters:
                | iRank
                |     Index of the trimmed element (piece)
                |    
                |  iIndex
                |     Discrimination Index
                |     Used to discrimine pieces when cutters orientations are not enough


        :param i_rank:
        :param i_index:
        :return:
        """
        return self.hybrid_shape_trim.SetPieceDiscriminationIndex(i_rank, i_index)

    def set_portion_to_keep(self, i_rank, i_portion_number):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetPortionToKeep
                | o Sub SetPortionToKeep(        iRank,
                |                                iPortionNumber)
                | 
                | Sets a portion to keep number in Pieces mode. Used for trim
                | pieces of wires
                |
                | Parameters:
                | iRank
                |       Index of the trimmed element
                |    
                |  iPortionNumber
                |       Index of portion to keep on the element


        :param i_rank:
        :param i_portion_number:
        :return:
        """
        return self.hybrid_shape_trim.SetPortionToKeep(i_rank, i_portion_number)

    def set_previous_orientation(self, i_rank, i_orientation):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetPreviousOrientation
                | o Sub SetPreviousOrientation(        iRank,
                |                                      iOrientation)
                | 
                | Sets the orientation used to compute the feature, referring
                | to the previous trimmed element.
                |
                | Parameters:
                | iRank
                |        index (of one of the trimmed features) - 1
                |       iRank must be greater than 1 and lower than the number of elements - 1 
                |    
                |  iOrientation
                |         Orientation


        :param i_rank:
        :param i_orientation:
        :return:
        """
        return self.hybrid_shape_trim.SetPreviousOrientation(i_rank, i_orientation)

    def __repr__(self):
        return f'HybridShapeTrim()'
