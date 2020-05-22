#! /usr/bin/python3.6
# module initially auto generated using V5Automation.chm from CATIA R25 on 2020-05-22 12:54:36.956119

from pycatia.mec_mod_interfaces.hybridshape import HybridShape


class HybridShapeExtractMulti(HybridShape):
    """
        .. note::
            CAA V5 Visual Basic help

                | Represents the hybrid shape ExtractMulti feature object.Role: To
                | access the data of the hybrid shape ExtractMulti feature object.Use
                | the  CATIAHybridShapeFactory to create a HybridShapeExtractMulti
                | object.

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_extract_multi = com_object     

    def add_constraint(self, i_constraint, i_type, i_complementaire, i_is_federated, i_crvtre_thsld, i_pos):
        """
        .. note::
            CAA V5 Visual Basic help

                | AddConstraint
                | o Sub AddConstraint(        iConstraint,
                |                             iType,
                |                             iComplementaire,
                |                             iIsFederated,
                |                             iCrvtreThsld,
                |                             iPos)
                | 
                | Deprecated: V5R16
                | CATIAHybridShapeExtractMulti#AddConstraintTolerant Adds a
                | constraint to the list of Extracted Elements.
                |
                | Parameters:
                | iConstraint
                |          The constraint to add.
                |    
                |  iType
                |          the type of propagation for the ExtractMulti.
                |    
                |  iComplementaire
                |          the Complementary flag checked/unchecked for for the constraint.
                |    
                |  iIsFederated
                |          the Federated flag checked/unchecked for the constraint.
                |    
                |  iCrvtreThsld
                |          the CurvatureThreshold for the constraint.
                |    
                |  iPos
                |          The position at which the element is to be added in the list of constraints.

                | Examples:
                | This example adds a body in the list of constraints at
                | specified position with the type of propagation, the
                | Federated flag and the CurvatureThreshold of the
                | HybShpExtractMulti hybrid shape ExtractMulti. Dim iType as
                | long Dim iComplementaire as boolean Dim iIsFederated as
                | boolean Dim iCrvtreThsld as double
                | HybShpExtractMulti.AddConstraint iCst iType iComplementaire
                | iIsFederated iCrvtreThsld 1

        :param i_constraint:
        :param i_type:
        :param i_complementaire:
        :param i_is_federated:
        :param i_crvtre_thsld:
        :param i_pos:
        :return:
        """
        return self.hybrid_shape_extract_multi.AddConstraint(i_constraint, i_type, i_complementaire, i_is_federated, i_crvtre_thsld, i_pos)

    def add_constraint_tolerant(self, i_constraint, i_type, i_complementaire, i_is_federated, i_distre_thsld, i_angtre_thsld, i_crvtre_thsld, i_pos):
        """
        .. note::
            CAA V5 Visual Basic help

                | AddConstraintTolerant
                | o Sub AddConstraintTolerant(        iConstraint,
                |                                     iType,
                |                                     iComplementaire,
                |                                     iIsFederated,
                |                                     iDistreThsld,
                |                                     iAngtreThsld,
                |                                     iCrvtreThsld,
                |                                     iPos)
                | 
                | Adds a constraint to the list of Extracted Elements.
                |
                | Parameters:
                | iConstraint
                |          The constraint to add.
                |    
                |  iType
                |          the type of propagation for the ExtractMulti.
                |    
                |  iComplementaire
                |          the Complementary flag checked/unchecked for for the constraint.
                |    
                |  iIsFederated
                |          the Federated flag checked/unchecked for the constraint.
                |    
                |  iDistreThsld
                |          the DistanceThreshold for the constraint.
                |    
                |  iAngtreThsld
                |          the AngularThreshold for the constraint.
                |    
                |  iCrvtreThsld
                |          the CurvatureThreshold for the constraint.
                |    
                |  iPos
                |          The position at which the element is to be added in the list of constraints.

                | Examples:
                | This example adds a body in the list of constraints at
                | specified position with the type of propagation, the
                | Federated flag and the CurvatureThreshold of the
                | HybShpExtractMulti hybrid shape ExtractMulti. Dim iType as
                | long Dim iComplementaire as boolean Dim iIsFederated as
                | boolean Dim iDistreThsld as double Dim iAngtreThsld as
                | double Dim iCrvtreThsld as double
                | HybShpExtractMulti.AddConstraintTolerant iCst iType
                | iComplementaire iIsFederated iCrvtreThsld 1

        :param i_constraint:
        :param i_type:
        :param i_complementaire:
        :param i_is_federated:
        :param i_distre_thsld:
        :param i_angtre_thsld:
        :param i_crvtre_thsld:
        :param i_pos:
        :return:
        """
        return self.hybrid_shape_extract_multi.AddConstraintTolerant(i_constraint, i_type, i_complementaire, i_is_federated, i_distre_thsld, i_angtre_thsld, i_crvtre_thsld, i_pos)

    def get_angular_threshold(self, i_pos):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetAngularThreshold
                | o Func GetAngularThreshold(        iPos) As
                | 
                | Returns the AngularThreshold of the list of constraints at
                | specified position. 
                |
                | Example:
                | This example retrieves the
                | AngularThreshold in the list of constraints at specified
                | position of the hybShpExtractMulti in AngularThH. Dim
                | oAngtreThsld as double AngularThH =
                | HybShpExtractMulti.GetAngularThreshold(1)
                |
                | Parameters:


        :param i_pos:
        :return:
        """
        return self.hybrid_shape_extract_multi.GetAngularThreshold(i_pos)

    def get_angular_threshold_activity(self, i_pos):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetAngularThresholdActivity
                | o Func GetAngularThresholdActivity(        iPos) As
                | 
                | Returns the AngularThresholdActivity of the list of
                | constraints at specified position. 
                |
                | Example:
                | This example
                | retrieves the AngularThresholdActivity of the list of
                | constraints at specified position of the hybShpExtractMulti
                | in AngularActivity . Dim oAngtreThsldActivity as boolean
                | oAngtreThsldActivity =
                | HybShpExtractMulti.GetAngularThresholdActivity (1)
                |
                | Parameters:


        :param i_pos:
        :return:
        """
        return self.hybrid_shape_extract_multi.GetAngularThresholdActivity(i_pos)

    def get_complementary_extract_multi(self, i_pos):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetComplementaryExtractMulti
                | o Func GetComplementaryExtractMulti(        iPos) As
                | 
                | Returns the Complementary flag checked/unchecked of the list
                | of constraints at specified position. 
                |
                | Example:
                | This example
                | retrieves the Complementary flag in the list of constraints
                | at specified position of the hybShpExtractMulti in
                | Complementaire. Dim oComplementaire as boolean
                | oComplementaire =
                | HybShpExtractMulti.GetComplementaryExtractMulti(1)
                |
                | Parameters:


        :param i_pos:
        :return:
        """
        return self.hybrid_shape_extract_multi.GetComplementaryExtractMulti(i_pos)

    def get_curvature_threshold(self, i_pos):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetCurvatureThreshold
                | o Func GetCurvatureThreshold(        iPos) As
                | 
                | Returns the CurvatureThreshold of the list of constraints at
                | specified position. 
                |
                | Example:
                | This example retrieves the
                | CurvatureThreshold in the list of constraints at specified
                | position of the hybShpExtractMulti in CurvatureThH. Dim
                | oCrvtreThsld as double CurvatureThH =
                | HybShpExtractMulti.GetCurvatureThreshold(1)
                |
                | Parameters:


        :param i_pos:
        :return:
        """
        return self.hybrid_shape_extract_multi.GetCurvatureThreshold(i_pos)

    def get_curvature_threshold_activity(self, i_pos):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetCurvatureThresholdActivity
                | o Func GetCurvatureThresholdActivity(        iPos) As
                | 
                | Returns the CurvatureThresholdActivity of the list of
                | constraints at specified position. 
                |
                | Example:
                | This example
                | retrieves the CurvatureThresholdActivity of the list of
                | constraints at specified position of the hybShpExtractMulti
                | in CurvatureActivity . Dim oCrvtreThsldActivity as boolean
                | oCrvtreThsldActivity =
                | HybShpExtractMulti.GetCurvatureThresholdActivity (1)
                |
                | Parameters:


        :param i_pos:
        :return:
        """
        return self.hybrid_shape_extract_multi.GetCurvatureThresholdActivity(i_pos)

    def get_distance_threshold(self, i_pos):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetDistanceThreshold
                | o Func GetDistanceThreshold(        iPos) As
                | 
                | Returns the DistanceThreshold of the list of constraints at
                | specified position. 
                |
                | Example:
                | This example retrieves the
                | DistanceThreshold in the list of constraints at specified
                | position of the hybShpExtractMulti in DistanceThH. Dim
                | oDistreThsld as double DistanceThH =
                | HybShpExtractMulti.GetDistanceThreshold(1)
                |
                | Parameters:


        :param i_pos:
        :return:
        """
        return self.hybrid_shape_extract_multi.GetDistanceThreshold(i_pos)

    def get_distance_threshold_activity(self, i_pos):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetDistanceThresholdActivity
                | o Func GetDistanceThresholdActivity(        iPos) As
                | 
                | Returns the DistanceThresholdActivity of the list of
                | constraints at specified position. 
                |
                | Example:
                | This example
                | retrieves the DistanceThresholdActivity of the list of
                | constraints at specified position of the hybShpExtractMulti
                | in DistanceActivity . Dim oDistreThsldActivity as boolean
                | oDistreThsldActivity =
                | HybShpExtractMulti.GetDistanceThresholdActivity (1)
                |
                | Parameters:


        :param i_pos:
        :return:
        """
        return self.hybrid_shape_extract_multi.GetDistanceThresholdActivity(i_pos)

    def get_element(self, i_pos):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetElement
                | o Func GetElement(        iPos) As
                | 
                | Returns the sub element used as init for the propagation.
                | 
                |
                | Example:
                | This example retrieves the sub element in the list
                | of constraints at specified position of the
                | hybShpExtractMulti in Elem. Dim oElem as CATIAReference
                | oElem = HybShpExtractMulti.GetElement(1) See also:
                |
                | Parameters:


        :param i_pos:
        :return:
        """
        return self.hybrid_shape_extract_multi.GetElement(i_pos)

    def get_is_federated(self, i_pos):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetIsFederated
                | o Func GetIsFederated(        iPos) As
                | 
                | Returns the IsFederated flag checked/unchecked of the list
                | of constraints at specified position. 
                |
                | Example:
                | This example
                | retrieves the federated flag in the list of constraints at
                | specified position of the hybShpExtractMulti in IsFederated.
                | Dim oIsFederated as boolean oIsFederated =
                | HybShpExtractMulti.GetIsFederated(1)
                |
                | Parameters:


        :param i_pos:
        :return:
        """
        return self.hybrid_shape_extract_multi.GetIsFederated(i_pos)

    def get_list_of_constraints(self, o_list_of_extracted_constraints):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetListOfConstraints
                | o Sub GetListOfConstraints(        oListOfExtractedConstraints)
                | 
                | Returns the list of Extracted Elements.
                |
                | Parameters:
                | oListOfExtractedConstraints
                |          The list of constraints. It is returned as an array of nbconstraints in SafeArrayVariant.

                | Examples:
                | This example returns the list of constraints of the
                | HybShpExtractMulti hybrid shape ExtractMulti. Dim
                | oListOfExtractedConstraints as CATSafeArrayVariant
                | HybShpExtractMulti.GetListOfConstraints
                | (oListOfExtractedConstraints) Note: You can access each
                | constraint as follows: 1 is in
                | oListOfExtractedConstraints(0) 2 is in
                | oListOfExtractedConstraints(1) nbconstraints is in
                | oListOfExtractedConstraints(nbconstraints-1)

        :param o_list_of_extracted_constraints:
        :return:
        """
        return self.hybrid_shape_extract_multi.GetListOfConstraints(o_list_of_extracted_constraints)

    def get_nb_constraints(self, o_nb_constraints):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetNbConstraints
                | o Sub GetNbConstraints(        oNbConstraints)
                | 
                | Returns number of constraints in the list of Extracted
                | Elements.
                |
                | Parameters:
                | oNbConstraints
                |          number of constraints in the list of Extracted Elements.

                | Examples:
                | This example returns number of constraints in the list of
                | constraints of the HybShpExtractMulti hybrid shape
                | ExtractMulti. Dim oNbConstraints as long
                | HybShpExtractMulti.GetNbConstraints (oNbConstraints )

        :param o_nb_constraints:
        :return:
        """
        return self.hybrid_shape_extract_multi.GetNbConstraints(o_nb_constraints)

    def get_propagation_type(self, i_pos):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetPropagationType
                | o Func GetPropagationType(        iPos) As
                | 
                | Returns the type of propagation of the list of constraints
                | at specified position. The propagation types for the
                | ExtractMulti can have the following values: 1 for extraction
                | propagation in point continuity 2 for extraction propagation
                | in tangent continuity 3 for extraction without propagation 4
                | for extraction propagation in curvature continuity Example:
                | This example retrieves the PropagationType in the list of
                | constraints at specified position of the hybShpExtractMulti
                | in TypePropag. Dim oTypePropag as long oTypePropag =
                | HybShpExtractMulti.GetPropagationType(1)
                |
                | Parameters:


        :param i_pos:
        :return:
        """
        return self.hybrid_shape_extract_multi.GetPropagationType(i_pos)

    def get_support(self, i_pos):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetSupport
                | o Func GetSupport(        iPos) As
                | 
                | Returns the support of the list of constraints at specified
                | position.
                |
                | Parameters:
                | oSupport
                |          The support.


        :param i_pos:
        :return:
        """
        return self.hybrid_shape_extract_multi.GetSupport(i_pos)

    def remove_element(self, i_position):
        """
        .. note::
            CAA V5 Visual Basic help

                | RemoveElement
                | o Sub RemoveElement(        iPosition)
                | 
                | Removes the body to be extracted from the list of
                | constraints at specified position.
                |
                | Parameters:
                | iPosition
                |        Position at which the body is to be removed

                | Examples:
                | This example removes the body from the list of constraints
                | at specified position of the HybShpExtractMulti hybrid shape
                | ExtractMulti. HybShpExtractMulti.RemoveElement 1

        :param i_position:
        :return:
        """
        return self.hybrid_shape_extract_multi.RemoveElement(i_position)

    def replace_element(self, i_extract_to_replace, i_new_extract, i_pos):
        """
        .. note::
            CAA V5 Visual Basic help

                | ReplaceElement
                | o Sub ReplaceElement(        iExtractToReplace,
                |                              iNewExtract,
                |                              iPos)
                | 
                | Replaces an element to extract in the list of constraints at
                | specified position.
                |
                | Parameters:
                | iExtractToReplace
                |          The element to replace.
                |    
                |  iNewExtract
                |          The new element.
                |    
                |  iPos
                |          The position at which the element is to be replaced in the list of constraints.

                | Examples:
                | This example replaces the body from the list of constraints
                | at specified position of the HybShpExtractMulti hybrid shape
                | ExtractMulti. Dim RefToRep as CATIAReference Dim
                | RefNewExtract as CATIAReference
                | HybShpExtractMulti.ReplaceElement RefToRep RefNewExtract 1

        :param i_extract_to_replace:
        :param i_new_extract:
        :param i_pos:
        :return:
        """
        return self.hybrid_shape_extract_multi.ReplaceElement(i_extract_to_replace, i_new_extract, i_pos)

    def set_angular_threshold(self, i_pos, i_angtre_thsld):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetAngularThreshold
                | o Sub SetAngularThreshold(        iPos,
                |                                   iAngtreThsld)
                | 
                | Sets the AngularThreshold in the list of constraints at
                | specified position. 
                |
                | Example:
                | This example sets the
                | AngularThreshold of the list of constraints at specified
                | position of the hybShpExtractMulti in AngularThH. Dim
                | iAngtreThsld as double
                | HybShpExtractMulti.SetAngularThreshold 1 iAngtreThsld
                |
                | Parameters:


        :param i_pos:
        :param i_angtre_thsld:
        :return:
        """
        return self.hybrid_shape_extract_multi.SetAngularThreshold(i_pos, i_angtre_thsld)

    def set_angular_threshold_activity(self, i_pos, i_angtre_thsld_activity):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetAngularThresholdActivity
                | o Sub SetAngularThresholdActivity(        iPos,
                |                                           iAngtreThsldActivity)
                | 
                | Sets the AngularThresholdActivity in the list of constraints
                | at specified position. 
                |
                | Example:
                | This example sets the
                | AngularThresholdActivity in the list of constraints at
                | specified position of the hybShpExtractMulti in
                | AngularActivity . Dim iAngtreThsldActivity as boolean
                | iAngtreThsldActivity = TRUE
                | HybShpExtractMulti.SetAngularThresholdActivity 1
                | iAngtreThsldActivity
                |
                | Parameters:


        :param i_pos:
        :param i_angtre_thsld_activity:
        :return:
        """
        return self.hybrid_shape_extract_multi.SetAngularThresholdActivity(i_pos, i_angtre_thsld_activity)

    def set_complementary_extract_multi(self, i_pos, i_complementaire):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetComplementaryExtractMulti
                | o Sub SetComplementaryExtractMulti(        iPos,
                |                                            iComplementaire)
                | 
                | Sets the Complementary flag checked/unchecked in the list of
                | constraints at specified position. 
                |
                | Example:
                | This example
                | sets the Complementary flag of the list of constraints at
                | specified position of the hybShpExtractMulti in
                | Complementaire. Dim iComplementaire as boolean
                | iComplementaire = TRUE
                | HybShpExtractMulti.SetComplementaryExtractMulti 1
                | iComplementaire
                |
                | Parameters:


        :param i_pos:
        :param i_complementaire:
        :return:
        """
        return self.hybrid_shape_extract_multi.SetComplementaryExtractMulti(i_pos, i_complementaire)

    def set_curvature_threshold(self, i_pos, i_crvtre_thsld):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetCurvatureThreshold
                | o Sub SetCurvatureThreshold(        iPos,
                |                                     iCrvtreThsld)
                | 
                | Sets the CurvatureThreshold in the list of constraints at
                | specified position. 
                |
                | Example:
                | This example sets the
                | CurvatureThreshold of the list of constraints at specified
                | position of the hybShpExtractMulti in CurvatureThH. Dim
                | iCrvtreThsld as double
                | HybShpExtractMulti.SetCurvatureThreshold 1 iCrvtreThsld
                |
                | Parameters:


        :param i_pos:
        :param i_crvtre_thsld:
        :return:
        """
        return self.hybrid_shape_extract_multi.SetCurvatureThreshold(i_pos, i_crvtre_thsld)

    def set_curvature_threshold_activity(self, i_pos, i_crvtre_thsld_activity):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetCurvatureThresholdActivity
                | o Sub SetCurvatureThresholdActivity(        iPos,
                |                                             iCrvtreThsldActivity)
                | 
                | Sets the CurvatureThresholdActivity in the list of
                | constraints at specified position. 
                |
                | Example:
                | This example
                | sets the CurvatureThresholdActivity in the list of
                | constraints at specified position of the hybShpExtractMulti
                | in CurvatureActivity . Dim iCrvtreThsldActivity as boolean
                | iCrvtreThsldActivity = TRUE
                | HybShpExtractMulti.SetCurvatureThresholdActivity 1
                | iCrvtreThsldActivity
                |
                | Parameters:


        :param i_pos:
        :param i_crvtre_thsld_activity:
        :return:
        """
        return self.hybrid_shape_extract_multi.SetCurvatureThresholdActivity(i_pos, i_crvtre_thsld_activity)

    def set_distance_threshold(self, i_pos, i_distre_thsld):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetDistanceThreshold
                | o Sub SetDistanceThreshold(        iPos,
                |                                    iDistreThsld)
                | 
                | Sets the DistanceThreshold in the list of constraints at
                | specified position. 
                |
                | Example:
                | This example sets the
                | DistanceThreshold of the list of constraints at specified
                | position of the hybShpExtractMulti in DistanceThH. Dim
                | iDistreThsld as double
                | HybShpExtractMulti.SetDistanceThreshold 1 iDistreThsld
                |
                | Parameters:


        :param i_pos:
        :param i_distre_thsld:
        :return:
        """
        return self.hybrid_shape_extract_multi.SetDistanceThreshold(i_pos, i_distre_thsld)

    def set_distance_threshold_activity(self, i_pos, i_distre_thsld_activity):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetDistanceThresholdActivity
                | o Sub SetDistanceThresholdActivity(        iPos,
                |                                            iDistreThsldActivity)
                | 
                | Sets the DistanceThresholdActivity in the list of
                | constraints at specified position. 
                |
                | Example:
                | This example
                | sets the DistanceThresholdActivity in the list of
                | constraints at specified position of the hybShpExtractMulti
                | in DistanceActivity . Dim iDistreThsldActivity as boolean
                | iDistreThsldActivity = TRUE
                | HybShpExtractMulti.SetDistanceThresholdActivity 1
                | iDistreThsldActivity
                |
                | Parameters:


        :param i_pos:
        :param i_distre_thsld_activity:
        :return:
        """
        return self.hybrid_shape_extract_multi.SetDistanceThresholdActivity(i_pos, i_distre_thsld_activity)

    def set_element(self, i_pos, i_elem):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetElement
                | o Sub SetElement(        iPos,
                |                          iElem)
                | 
                | Sets the sub element used as init for the propagation.
                | 
                |
                | Example:
                | This example sets the sub element in the list of
                | constraints at specified position of the hybShpExtractMulti
                | in Elem. Dim iPos as long Dim iElem as CATIAReference
                | HybShpExtractMulti.SetElement 1 iElem See also:
                |
                | Parameters:


        :param i_pos:
        :param i_elem:
        :return:
        """
        return self.hybrid_shape_extract_multi.SetElement(i_pos, i_elem)

    def set_is_federated(self, i_pos, i_is_federated):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetIsFederated
                | o Sub SetIsFederated(        iPos,
                |                              iIsFederated)
                | 
                | Sets the IsFederated flag checked/unchecked in the list of
                | constraints at specified position. 
                |
                | Example:
                | This example
                | sets the federated flag in the list of constraints at
                | specified position of the hybShpExtractMulti in IsFederated.
                | Dim iIsFederated as boolean iIsFederated = TRUE
                | HybShpExtractMulti.SetIsFederated 1 iIsFederated
                |
                | Parameters:


        :param i_pos:
        :param i_is_federated:
        :return:
        """
        return self.hybrid_shape_extract_multi.SetIsFederated(i_pos, i_is_federated)

    def set_propagation_type(self, i_pos, i_type_propag):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetPropagationType
                | o Sub SetPropagationType(        iPos,
                |                                  iTypePropag)
                | 
                | Sets the type of propagation for the ExtractMulti in the
                | list of constraints at specified position. The propagation
                | types for the ExtractMulti can have the following values: 1
                | for extraction propagation in point continuity 2 for
                | extraction propagation in tangent continuity 3 for
                | extraction without propagation 4 for extraction propagation
                | in curvature continuity 
                |
                | Example:
                | This example sets the
                | PropagationType of the list of constraints at specified
                | position of the hybShpExtractMulti in TypePropag. Dim
                | iTypePropag as long iTypePropag = 1
                | HybShpExtractMulti.SetPropagationType 1 iTypePropag
                |
                | Parameters:


        :param i_pos:
        :param i_type_propag:
        :return:
        """
        return self.hybrid_shape_extract_multi.SetPropagationType(i_pos, i_type_propag)

    def set_support(self, i_pos, i_support):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetSupport
                | o Sub SetSupport(        iPos,
                |                          iSupport)
                | 
                | Sets the support of the list of constraints at specified
                | position.
                |
                | Parameters:
                | oSupport
                |          The support.


        :param i_pos:
        :param i_support:
        :return:
        """
        return self.hybrid_shape_extract_multi.SetSupport(i_pos, i_support)

    def __repr__(self):
        return f'HybridShapeExtractMulti()'
