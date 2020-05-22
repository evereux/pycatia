#! /usr/bin/python3.6
# module initially auto generated using V5Automation.chm from CATIA R25 on 2020-05-22 12:54:36.956119

from pycatia.mec_mod_interfaces.hybridshape import HybridShape


class HybridShapeHealing(HybridShape):
    """
        .. note::
            CAA V5 Visual Basic help

                | Represents the hybrid shape healing feature object.Role: Allows to
                | access to the body to process for a Healing feature. Use the
                | CATIAHybridShapeFactory to create HybridShapeFeature object.

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_healing = com_object     

    @property
    def canonic_free_mode(self, i_mode):
        """
        .. note::
            CAA V5 Visual Basic help

                | CanonicFreeMode
                | o Property CanonicFreeMode(        iMode)
                | 
                | Returns or sets the Canonic Free Mode of the healing.
                | Examples:
                | This example sets and retrieves the CanonicFreeMode of the
                | healing of the HybShpHealing hybrid shape healing. Dim
                | HybShpHealMode As Long HybShpHealMode = ..set appropriate
                | value HybShpHealing.CanonicFreeMode = HybShpHealMode
                | HybShpHealCont = HybShpHealing.CanonicFreeMode

        :param i_mode:
        :return:
        """
        return self.hybrid_shape_healing.CanonicFreeMode

    @canonic_free_mode.setter
    def canonic_free_mode(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_healing.CanonicFreeMode = value 

    @property
    def continuity(self, i_continuity):
        """
        .. note::
            CAA V5 Visual Basic help

                | Continuity
                | o Property Continuity(        iContinuity)
                | 
                | Returns or sets the continuity type of the healing.
                | Examples:
                | This example sets and retrieves the Continuity of the
                | healing of the HybShpHealing hybrid shape healing. Dim
                | HybShpHealCont As Long HybShpHealCont = ..set appropriate
                | value HybShpHealing.Continuity = HybShpHealCont
                | HybShpHealCont = HybShpHealing.Continuity

        :param i_continuity:
        :return:
        """
        return self.hybrid_shape_healing.Continuity

    @continuity.setter
    def continuity(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_healing.Continuity = value 

    @property
    def distance_objective(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | DistanceObjective
                | o Property DistanceObjective(    ) As   (Read Only)
                | 
                | Returns the Distance Objective of the healing.
                | Examples:
                | This example retrieves the DistanceObjective of the healing
                | of the HybShpHealing hybrid shape healing. Dim
                | HybShpHealDistObjective As Length Set
                | HybShpHealDistObjective = HybShpHealing.DistanceObjective

        :return:
        """
        return self.hybrid_shape_healing.DistanceObjective

    @property
    def merging_distance(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | MergingDistance
                | o Property MergingDistance(    ) As   (Read Only)
                | 
                | Returns the Merging Distance of the healing.
                | Examples:
                | This example retrieves the MergingDistance of the healing of
                | the HybShpHealing hybrid shape healing. Dim
                | HybShpHealMergeDist As Length Set HybShpHealMergeDist =
                | HybShpHealing.MergingDistance

        :return:
        """
        return self.hybrid_shape_healing.MergingDistance

    @property
    def no_of_bodies_to_heal(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | NoOfBodiesToHeal
                | o Property NoOfBodiesToHeal(    ) As   (Read Only)
                | 
                | Returns the number of bodies to heal of the healing.
                | Examples:
                | This example retrieves the number of bodies to heal of the
                | HybShpHealing hybrid shape Healing. Dim NoOfBodiesToHeal As
                | long NoOfBodiesToHeal = HybShpHealing.NoOfBodiesToHeal

        :return:
        """
        return self.hybrid_shape_healing.NoOfBodiesToHeal

    @property
    def no_of_edges_to_keep_sharp(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | NoOfEdgesToKeepSharp
                | o Property NoOfEdgesToKeepSharp(    ) As   (Read Only)
                | 
                | Returns the number of edges to keep sharp of the healing.
                | Examples:
                | This example retrieves the number of edges to keep sharp of
                | the HybShpHealing hybrid shape Healing. Dim NoOfEdges As
                | long NoOfEdges = HybShpHealing.NoOfEdgesToKeepSharp

        :return:
        """
        return self.hybrid_shape_healing.NoOfEdgesToKeepSharp

    @property
    def no_of_elements_to_freeze(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | NoOfElementsToFreeze
                | o Property NoOfElementsToFreeze(    ) As   (Read Only)
                | 
                | Returns the number of elements to heal of the healing.
                | Examples:
                | This example retrieves the number of elements to freeze of
                | the HybShpHealing hybrid shape Healing. Dim
                | NoOfElementsToFreeze As long NoOfElementsToFreeze =
                | HybShpHealing.NoOfElementsToFreeze

        :return:
        """
        return self.hybrid_shape_healing.NoOfElementsToFreeze

    @property
    def sharpness_angle(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | SharpnessAngle
                | o Property SharpnessAngle(    ) As   (Read Only)
                | 
                | Returns the Sharpness Angle of the healing.
                | Examples:
                | This example retrieves the Sharpness Angle of the healing of
                | the HybShpHealing hybrid shape healing. Dim
                | HybShpHealSharpnessAngle As Angle Set
                | HybShpHealSharpnessAngle = HybShpHealing.SharpnessAngle

        :return:
        """
        return self.hybrid_shape_healing.SharpnessAngle

    @property
    def tangency_angle(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | TangencyAngle
                | o Property TangencyAngle(    ) As   (Read Only)
                | 
                | Returns the Tangency Angle of the healing.
                | Examples:
                | This example retrieves the TangencyAngle of the healing of
                | the HybShpHealing hybrid shape healing. Dim
                | HybShpHealTangencyAngle As Angle Set HybShpHealTangencyAngle
                | = HybShpHealing.TangencyAngle

        :return:
        """
        return self.hybrid_shape_healing.TangencyAngle

    @property
    def tangency_objective(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | TangencyObjective
                | o Property TangencyObjective(    ) As   (Read Only)
                | 
                | Returns the Tangency Objective of the healing.
                | Examples:
                | This example retrieves the TangencyObjective of the healing
                | of the HybShpHealing hybrid shape healing. Dim
                | HybShpHealTangencyObjective As Length Set
                | HybShpHealTangencyObjective =
                | HybShpHealing.TangencyObjective

        :return:
        """
        return self.hybrid_shape_healing.TangencyObjective

    def add_body_to_heal(self, i_body):
        """
        .. note::
            CAA V5 Visual Basic help

                | AddBodyToHeal
                | o Sub AddBodyToHeal(        iBody)
                | 
                | Adds the body to be healed to the list.
                |
                | Parameters:
                | Body
                |        Reference to the body to be added to the list.

                | Examples:
                | This example adds the body to the list. of the HybShpHealing
                | hybrid shape healing. HybShpHealing.AddBodyToHeal refBody

        :param i_body:
        :return:
        """
        return self.hybrid_shape_healing.AddBodyToHeal(i_body)

    def add_edge_to_keep_sharp(self, i_edge):
        """
        .. note::
            CAA V5 Visual Basic help

                | AddEdgeToKeepSharp
                | o Sub AddEdgeToKeepSharp(        iEdge)
                | 
                | Adds the edge to be kept sharp while healing, to the list.
                |
                | Parameters:
                | Edge
                |        Reference to the Edge to be kept sharp

                | Examples:
                | This example adds the Edge to the list of Edges to be kept
                | sharp. of the HybShpHealing hybrid shape healing.
                | HybShpHealing.AddEdgeToKeepSharp refEdge

        :param i_edge:
        :return:
        """
        return self.hybrid_shape_healing.AddEdgeToKeepSharp(i_edge)

    def add_elements_to_freeze(self, i_element):
        """
        .. note::
            CAA V5 Visual Basic help

                | AddElementsToFreeze
                | o Sub AddElementsToFreeze(        iElement)
                | 
                | Adds the body to be freezed while healing, to the list.
                |
                | Parameters:
                | Element
                |        Reference to the element to be freezed.

                | Examples:
                | This example adds the body to the list of bodies to be
                | freezed. of the HybShpHealing hybrid shape healing.
                | HybShpHealing.AddElementsToFreeze refElement

        :param i_element:
        :return:
        """
        return self.hybrid_shape_healing.AddElementsToFreeze(i_element)

    def get_body_to_heal(self, i_position):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetBodyToHeal
                | o Func GetBodyToHeal(        iPosition) As
                | 
                | Returns the body to be healed from the list at specified
                | position.
                |
                | Parameters:
                | Position
                |        Position at which the body is to be obtained
                |    
                |  Body
                |        Reference to the body obtained at specified position.

                | Examples:
                | This example gets the body from the list by specifying the
                | position. of the HybShpHealing hybrid shape healing. set
                | refBody = HybShpHealing.GetBodyToHeal 1

        :param i_position:
        :return:
        """
        return self.hybrid_shape_healing.GetBodyToHeal(i_position)

    def get_edge_to_keep_sharp(self, i_position):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetEdgeToKeepSharp
                | o Func GetEdgeToKeepSharp(        iPosition) As
                | 
                | Returns the edge to be kept sharp from the list at specified
                | position.
                |
                | Parameters:
                | Position
                |        Position at which the element is to be obtained
                |    
                |  Edge
                |        Reference to the element obtained at specified position.

                | Examples:
                | This example gets the Edge from the list of Edges to be kept
                | sharp by specifying the position of the HybShpHealing hybrid
                | shape healing. set refEdge =
                | HybShpHealing.GetEdgeToKeepSharp 1

        :param i_position:
        :return:
        """
        return self.hybrid_shape_healing.GetEdgeToKeepSharp(i_position)

    def get_element_to_freeze(self, i_position):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetElementToFreeze
                | o Func GetElementToFreeze(        iPosition) As
                | 
                | Returns the element to be freezed from the list at specified
                | position.
                |
                | Parameters:
                | Position
                |        Position at which the element is to be obtained
                |    
                |  Element
                |        Reference to the element obtained at specified position.

                | Examples:
                | This example gets the element from the list of bodies to be
                | freezed by specifying the position of the HybShpHealing
                | hybrid shape healing. set refElement =
                | HybShpHealing.GetElementToFreeze 1

        :param i_position:
        :return:
        """
        return self.hybrid_shape_healing.GetElementToFreeze(i_position)

    def remove_body_to_heal(self, i_position):
        """
        .. note::
            CAA V5 Visual Basic help

                | RemoveBodyToHeal
                | o Sub RemoveBodyToHeal(        iPosition)
                | 
                | Removes the body to be healed from the list at specified
                | position.
                |
                | Parameters:
                | iPosition
                |        Position at which the body is to be removed

                | Examples:
                | This example removes the body from the list at specifying
                | the position. of the HybShpHealing hybrid shape healing.
                | HybShpHealing.RemoveBodyToHeal 1

        :param i_position:
        :return:
        """
        return self.hybrid_shape_healing.RemoveBodyToHeal(i_position)

    def remove_edge_to_keep_sharp(self, i_position):
        """
        .. note::
            CAA V5 Visual Basic help

                | RemoveEdgeToKeepSharp
                | o Sub RemoveEdgeToKeepSharp(        iPosition)
                | 
                | Removes the edge from the list of edges to be kept sharp at
                | specified position.
                |
                | Parameters:
                | iPosition
                |        Position at which the edge is to be removed

                | Examples:
                | This example removes the edge from the list at specified
                | position. of the HybShpHealing hybrid shape healing.
                | HybShpHealing.RemoveEdgeToKeepSharp 1

        :param i_position:
        :return:
        """
        return self.hybrid_shape_healing.RemoveEdgeToKeepSharp(i_position)

    def remove_element_to_freeze(self, i_position):
        """
        .. note::
            CAA V5 Visual Basic help

                | RemoveElementToFreeze
                | o Sub RemoveElementToFreeze(        iPosition)
                | 
                | Removes the element from the list of elements to be freezed
                | at specified position.
                |
                | Parameters:
                | Position
                |        Position at which the element is to be removed

                | Examples:
                | This example removes the element from the list at specifying
                | the position. of the HybShpHealing hybrid shape healing.
                | HybShpHealing.RemoveElementToFreeze 1

        :param i_position:
        :return:
        """
        return self.hybrid_shape_healing.RemoveElementToFreeze(i_position)

    def replace_to_heal_element(self, i_index, i_new_heal):
        """
        .. note::
            CAA V5 Visual Basic help

                | ReplaceToHealElement
                | o Sub ReplaceToHealElement(        iIndex,
                |                                    iNewHeal)
                | 
                | Replaces an element to heal.
                |
                | Parameters:
                | iIndex
                |          The position of the element to replace.
                |    
                |  iNewHeal
                |          The new element.


        :param i_index:
        :param i_new_heal:
        :return:
        """
        return self.hybrid_shape_healing.ReplaceToHealElement(i_index, i_new_heal)

    def set_distance_objective(self, i_distance_objective):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetDistanceObjective
                | o Sub SetDistanceObjective(        iDistanceObjective)
                | 
                | Sets the distance objective for healing entity.
                |
                | Parameters:
                | DistanceObjective
                |        Parameter containg the value of the distance objective to be set.

                | Examples:
                | This example sets the distance objective for the healing of
                | the HybShpHealing hybrid shape healing.
                | HybShpHealing.SetDistanceObjective 2.5

        :param i_distance_objective:
        :return:
        """
        return self.hybrid_shape_healing.SetDistanceObjective(i_distance_objective)

    def set_merging_distance(self, i_merging_distance):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetMergingDistance
                | o Sub SetMergingDistance(        iMergingDistance)
                | 
                | Sets the Merging distance for healing entity.
                |
                | Parameters:
                | MergingDistance
                |        Parameter containg the value of the merging distance to be set.

                | Examples:
                | This example sets the merging distance for the healing of
                | the HybShpHealing hybrid shape healing.
                | HybShpHealing.SetMergingDistance 2.5

        :param i_merging_distance:
        :return:
        """
        return self.hybrid_shape_healing.SetMergingDistance(i_merging_distance)

    def set_sharpness_angle(self, i_sharpness_angle):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetSharpnessAngle
                | o Sub SetSharpnessAngle(        iSharpnessAngle)
                | 
                | Sets the Sharpness Angle for healing entity.
                |
                | Parameters:
                | SharpnessAngle
                |        Parameter containg the value of the Sharpness Angle to be set.

                | Examples:
                | This example sets the Sharpness Angle for the healing of the
                | HybShpHealing hybrid shape healing.
                | HybShpHealing.SetSharpnessAngle 2.5

        :param i_sharpness_angle:
        :return:
        """
        return self.hybrid_shape_healing.SetSharpnessAngle(i_sharpness_angle)

    def set_tangency_angle(self, i_tangency_angle):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetTangencyAngle
                | o Sub SetTangencyAngle(        iTangencyAngle)
                | 
                | Sets the distance objective for healing entity.
                |
                | Parameters:
                | TangencyAngle
                |        Parameter containg the value of the Tangency Angle to be set.

                | Examples:
                | This example sets the Tangency Angle for the healing of the
                | HybShpHealing hybrid shape healing.
                | HybShpHealing.SetTangencyAngle 2.5

        :param i_tangency_angle:
        :return:
        """
        return self.hybrid_shape_healing.SetTangencyAngle(i_tangency_angle)

    def set_tangency_objective(self, i_tangency_objective):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetTangencyObjective
                | o Sub SetTangencyObjective(        iTangencyObjective)
                | 
                | Sets the tangency objective for healing entity.
                |
                | Parameters:
                | TangencyObjective
                |        Parameter containg the value of the Tangency Objective to be set.

                | Examples:
                | This example sets the Tangency Objective for the healing of
                | the HybShpHealing hybrid shape healing.
                | HybShpHealing.SetTangencyObjective 2.5

        :param i_tangency_objective:
        :return:
        """
        return self.hybrid_shape_healing.SetTangencyObjective(i_tangency_objective)

    def __repr__(self):
        return f'HybridShapeHealing()'
