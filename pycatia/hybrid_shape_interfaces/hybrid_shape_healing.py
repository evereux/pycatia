#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-07-06 14:02:20.222384

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.in_interfaces.reference import Reference
from pycatia.knowledge_interfaces.angle import Angle
from pycatia.knowledge_interfaces.length import Length
from pycatia.mec_mod_interfaces.hybrid_shape import HybridShape


class HybridShapeHealing(HybridShape):

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
                |                         HybridShapeHealing
                | 
                | Represents the hybrid shape healing feature object.
                | Role: Allows to access to the body to process for a Healing feature. Use the
                | CATIAHybridShapeFactory to create HybridShapeFeature object.
                | 
                | See also:
                |     HybridShapeFactory.AddNewHealing
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_healing = com_object

    @property
    def canonic_free_mode(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property CanonicFreeMode(long iMode)
                | 
                |     Returns or sets the Canonic Free Mode of the healing.
                | 
                |     Parameters:
                | 
                |         oMode
                |             (For get_CanonicFreeMode) Long parameter for retrieving the
                |             CanonicFreeMode. 
                |         iMode
                |             (For set_CanonicFreeMode) Long parameter for settingthe
                |             CanonicFreeMode.
                | 
                |             Example:
                |                 This example sets and retrieves the CanonicFreeMode of the
                |                 healing of the HybShpHealing hybrid shape
                |                 healing.
                | 
                |                  Dim HybShpHealMode As  Long
                |                  HybShpHealMode = ..set appropriate value
                |                  HybShpHealing.CanonicFreeMode = HybShpHealMode
                |                  HybShpHealCont = HybShpHealing.CanonicFreeMode

        :rtype: int
        """

        return self.hybrid_shape_healing.CononicFreeMode

    @canonic_free_mode.setter
    def canonic_free_mode(self, mode: int):
        """
        :param int mode:
        """

        self.hybrid_shape_healing.CanonicFreeMode = mode

    @property
    def continuity(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Continuity(long iContinuity)
                | 
                |     Returns or sets the continuity type of the healing.
                | 
                |     Parameters:
                | 
                |         Continuity
                |             Parameter for the continuity. Legal values are 0 and
                |             1
                | 
                |             Example:
                |                 This example sets and retrieves the Continuity of the healing
                |                 of the HybShpHealing hybrid shape healing.
                | 
                |                  Dim HybShpHealCont As  Long
                |                  HybShpHealCont = ..set appropriate value
                |                  HybShpHealing.Continuity = HybShpHealCont
                |                  HybShpHealCont = HybShpHealing.Continuity

        :rtype: False
        """

        return self.hybrid_shape_healing.Continuity

    @continuity.setter
    def continuity(self, value: int):
        """
        :param int value:
        """

        self.hybrid_shape_healing.Continuity = value

    @property
    def distance_objective(self) -> Length:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property DistanceObjective() As Length (Read Only)
                | 
                |     Returns the Distance Objective of the healing.
                | 
                |     Parameters:
                | 
                |         DistanceObjective
                |             Length parameter for retrieving the Distance
                |             Objective.
                | 
                |             Example:
                |                 This example retrieves the DistanceObjective of the healing of
                |                 the HybShpHealing hybrid shape healing.
                | 
                |                  Dim HybShpHealDistObjective As Length
                |                  Set HybShpHealDistObjective = HybShpHealing.DistanceObjective

        :rtype: Length
        """

        return Length(self.hybrid_shape_healing.DistanceObjective)

    @property
    def merging_distance(self) -> Length:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property MergingDistance() As Length (Read Only)
                | 
                |     Returns the Merging Distance of the healing.
                | 
                |     Parameters:
                | 
                |         MergingDistance
                |             Length parameter for retrieving the Merging
                |             Distance.
                | 
                |             Example:
                |                 This example retrieves the MergingDistance of the healing of
                |                 the HybShpHealing hybrid shape healing.
                | 
                |                  Dim HybShpHealMergeDist As Length
                |                  Set HybShpHealMergeDist = HybShpHealing.MergingDistance

        :rtype: Length
        """

        return Length(self.hybrid_shape_healing.MergingDistance)

    @property
    def no_of_bodies_to_heal(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property NoOfBodiesToHeal() As long (Read Only)
                | 
                |     Returns the number of bodies to heal of the healing.
                | 
                |     Parameters:
                | 
                |         NumberOfbodies
                |             Number of bodies to heal in the healing.
                | 
                |             Example:
                |                 This example retrieves the number of bodies to heal of the
                |                 HybShpHealing hybrid shape Healing.
                | 
                |                  Dim NoOfBodiesToHeal As  long
                |                  NoOfBodiesToHeal = HybShpHealing.NoOfBodiesToHeal

        :rtype: int
        """

        return self.hybrid_shape_healing.NoOfBodiesToHeal

    @property
    def no_of_edges_to_keep_sharp(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property NoOfEdgesToKeepSharp() As long (Read Only)
                | 
                |     Returns the number of edges to keep sharp of the healing.
                | 
                |     Parameters:
                | 
                |         NumberOfEdges
                |             Number of edges to keep sharp.
                | 
                |             Example:
                |                 This example retrieves the number of edges to keep sharp of the
                |                 HybShpHealing hybrid shape Healing.
                | 
                |                  Dim NoOfEdges As  long
                |                  NoOfEdges = HybShpHealing.NoOfEdgesToKeepSharp

        :rtype: int
        """

        return self.hybrid_shape_healing.NoOfEdgesToKeepSharp

    @property
    def no_of_elements_to_freeze(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property NoOfElementsToFreeze() As long (Read Only)
                | 
                |     Returns the number of elements to heal of the healing.
                | 
                |     Parameters:
                | 
                |         NumberOfElements
                |             Number of elements to freeze in the healing.
                | 
                |             Example:
                |                 This example retrieves the number of elements to freeze of the
                |                 HybShpHealing hybrid shape Healing.
                | 
                |                  Dim NoOfElementsToFreeze As  long
                |                  NoOfElementsToFreeze = HybShpHealing.NoOfElementsToFreeze

        :rtype: int
        """

        return self.hybrid_shape_healing.NoOfElementsToFreeze

    @property
    def sharpness_angle(self) -> Angle:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property SharpnessAngle() As Angle (Read Only)
                | 
                |     Returns the Sharpness Angle of the healing.
                | 
                |     Parameters:
                | 
                |         SharpnessAngle
                |             Angle parameter for retrieving the Sharpness
                |             Angle.
                | 
                |             Example:
                |                 This example retrieves the Sharpness Angle of the healing of
                |                 the HybShpHealing hybrid shape healing.
                | 
                |                  Dim HybShpHealSharpnessAngle As Angle
                |                  Set HybShpHealSharpnessAngle = HybShpHealing.SharpnessAngle

        :rtype: Angle
        """

        return Angle(self.hybrid_shape_healing.SharpnessAngle)

    @property
    def tangency_angle(self) -> Angle:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property TangencyAngle() As Angle (Read Only)
                | 
                |     Returns the Tangency Angle of the healing.
                | 
                |     Parameters:
                | 
                |         TangencyAngle
                |             Angle parameter for retrieving the TangencyAngle.
                | 
                |             Example:
                |                 This example retrieves the TangencyAngle of the healing of the
                |                 HybShpHealing hybrid shape healing.
                | 
                |                  Dim HybShpHealTangencyAngle As Angle
                |                  Set HybShpHealTangencyAngle = HybShpHealing.TangencyAngle

        :rtype: Angle
        """

        return Angle(self.hybrid_shape_healing.TangencyAngle)

    @property
    def tangency_objective(self) -> Length:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property TangencyObjective() As Length (Read Only)
                | 
                |     Returns the Tangency Objective of the healing.
                | 
                |     Parameters:
                | 
                |         TangencyObjective
                |             Length parameter for retrieving the Tangency
                |             Objective.
                | 
                |             Example:
                |                 This example retrieves the TangencyObjective of the healing of
                |                 the HybShpHealing hybrid shape healing.
                | 
                |                  Dim HybShpHealTangencyObjective As Length
                |                  Set HybShpHealTangencyObjective = HybShpHealing.TangencyObjective

        :rtype: Length
        """

        return Length(self.hybrid_shape_healing.TangencyObjective)

    def add_body_to_heal(self, i_body: Reference) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub AddBodyToHeal(Reference iBody)
                | 
                |     Adds the body to be healed to the list.
                | 
                |     Parameters:
                | 
                |         Body
                |             Reference to the body to be added to the list.
                | 
                |             Example:
                |                 This example adds the body to the list. of the HybShpHealing
                |                 hybrid shape healing.
                | 
                |                  HybShpHealing.AddBodyToHeal refBody

        :param Reference i_body:
        :rtype: None
        """
        return self.hybrid_shape_healing.AddBodyToHeal(i_body.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'add_body_to_heal'
        # # vba_code = """
        # # Public Function add_body_to_heal(hybrid_shape_healing)
        # #     Dim iBody (2)
        # #     hybrid_shape_healing.AddBodyToHeal iBody
        # #     add_body_to_heal = iBody
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def add_edge_to_keep_sharp(self, i_edge: Reference) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub AddEdgeToKeepSharp(Reference iEdge)
                | 
                |     Adds the edge to be kept sharp while healing, to the list.
                | 
                |     Parameters:
                | 
                |         Edge
                |             Reference to the Edge to be kept sharp
                | 
                |             Example:
                |                 This example adds the Edge to the list of Edges to be kept
                |                 sharp. of the HybShpHealing hybrid shape
                |                 healing.
                | 
                |                  HybShpHealing.AddEdgeToKeepSharp refEdge

        :param Reference i_edge:
        :rtype: None
        """
        return self.hybrid_shape_healing.AddEdgeToKeepSharp(i_edge.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'add_edge_to_keep_sharp'
        # # vba_code = """
        # # Public Function add_edge_to_keep_sharp(hybrid_shape_healing)
        # #     Dim iEdge (2)
        # #     hybrid_shape_healing.AddEdgeToKeepSharp iEdge
        # #     add_edge_to_keep_sharp = iEdge
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def add_elements_to_freeze(self, i_element: Reference) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub AddElementsToFreeze(Reference iElement)
                | 
                |     Adds the body to be freezed while healing, to the list.
                | 
                |     Parameters:
                | 
                |         Element
                |             Reference to the element to be freezed.
                | 
                |             Example:
                |                 This example adds the body to the list of bodies to be freezed.
                |                 of the HybShpHealing hybrid shape healing.
                | 
                |                  HybShpHealing.AddElementsToFreeze refElement

        :param Reference i_element:
        :rtype: None
        """
        return self.hybrid_shape_healing.AddElementsToFreeze(i_element.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'add_elements_to_freeze'
        # # vba_code = """
        # # Public Function add_elements_to_freeze(hybrid_shape_healing)
        # #     Dim iElement (2)
        # #     hybrid_shape_healing.AddElementsToFreeze iElement
        # #     add_elements_to_freeze = iElement
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_body_to_heal(self, i_position: int) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetBodyToHeal(long iPosition) As Reference
                | 
                |     Returns the body to be healed from the list at specified
                |     position.
                | 
                |     Parameters:
                | 
                |         Position
                |             Position at which the body is to be obtained 
                |         Body
                |             Reference to the body obtained at specified
                |             position.
                | 
                |             Example:
                |                 This example gets the body from the list by specifying the
                |                 position. of the HybShpHealing hybrid shape
                |                 healing.
                | 
                |                  set refBody = HybShpHealing.GetBodyToHeal  1

        :param int i_position:
        :rtype: Reference
        """
        return Reference(self.hybrid_shape_healing.GetBodyToHeal(i_position))

    def get_edge_to_keep_sharp(self, i_position: int) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetEdgeToKeepSharp(long iPosition) As Reference
                | 
                |     Returns the edge to be kept sharp from the list at specified
                |     position.
                | 
                |     Parameters:
                | 
                |         Position
                |             Position at which the element is to be obtained 
                |         Edge
                |             Reference to the element obtained at specified
                |             position.
                | 
                |             Example:
                |                 This example gets the Edge from the list of Edges to be kept
                |                 sharp by specifying the position of the HybShpHealing hybrid shape
                |                 healing.
                | 
                |                  set refEdge = HybShpHealing.GetEdgeToKeepSharp  1

        :param int i_position:
        :rtype: Reference
        """
        return Reference(self.hybrid_shape_healing.GetEdgeToKeepSharp(i_position))

    def get_element_to_freeze(self, i_position: int) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetElementToFreeze(long iPosition) As Reference
                | 
                |     Returns the element to be freezed from the list at specified
                |     position.
                | 
                |     Parameters:
                | 
                |         Position
                |             Position at which the element is to be obtained 
                |         Element
                |             Reference to the element obtained at specified
                |             position.
                | 
                |             Example:
                |                 This example gets the element from the list of bodies to be
                |                 freezed by specifying the position of the HybShpHealing hybrid shape
                |                 healing.
                | 
                |                  set refElement = HybShpHealing.GetElementToFreeze  1

        :param int i_position:
        :rtype: Reference
        """
        return Reference(self.hybrid_shape_healing.GetElementToFreeze(i_position))

    def remove_body_to_heal(self, i_position: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub RemoveBodyToHeal(long iPosition)
                | 
                |     Removes the body to be healed from the list at specified
                |     position.
                | 
                |     Parameters:
                | 
                |         iPosition
                |             Position at which the body is to be removed
                | 
                |             Example:
                |                 This example removes the body from the list at specifying the
                |                 position. of the HybShpHealing hybrid shape
                |                 healing.
                | 
                |                  HybShpHealing.RemoveBodyToHeal  1

        :param int i_position:
        :rtype: None
        """
        return self.hybrid_shape_healing.RemoveBodyToHeal(i_position)

    def remove_edge_to_keep_sharp(self, i_position: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub RemoveEdgeToKeepSharp(long iPosition)
                | 
                |     Removes the edge from the list of edges to be kept sharp at specified
                |     position.
                | 
                |     Parameters:
                | 
                |         iPosition
                |             Position at which the edge is to be removed
                | 
                |             Example:
                |                 This example removes the edge from the list at specified
                |                 position. of the HybShpHealing hybrid shape
                |                 healing.
                | 
                |                  HybShpHealing.RemoveEdgeToKeepSharp  1

        :param int i_position:
        :rtype: None
        """
        return self.hybrid_shape_healing.RemoveEdgeToKeepSharp(i_position)

    def remove_element_to_freeze(self, i_position: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub RemoveElementToFreeze(long iPosition)
                | 
                |     Removes the element from the list of elements to be freezed at specified
                |     position.
                | 
                |     Parameters:
                | 
                |         Position
                |             Position at which the element is to be removed
                | 
                |             Example:
                |                 This example removes the element from the list at specifying
                |                 the position. of the HybShpHealing hybrid shape
                |                 healing.
                | 
                |                  HybShpHealing.RemoveElementToFreeze  1

        :param int i_position:
        :rtype: None
        """
        return self.hybrid_shape_healing.RemoveElementToFreeze(i_position)

    def replace_to_heal_element(self, i_index: int, i_new_heal: Reference) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub ReplaceToHealElement(long iIndex,
                | Reference iNewHeal)
                | 
                |     Replaces an element to heal.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The position of the element to replace. 
                |         iNewHeal
                |             The new element.

        :param int i_index:
        :param Reference i_new_heal:
        :rtype: None
        """
        return self.hybrid_shape_healing.ReplaceToHealElement(i_index, i_new_heal.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'replace_to_heal_element'
        # # vba_code = """
        # # Public Function replace_to_heal_element(hybrid_shape_healing)
        # #     Dim iIndex (2)
        # #     hybrid_shape_healing.ReplaceToHealElement iIndex
        # #     replace_to_heal_element = iIndex
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_distance_objective(self, i_distance_objective: float) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetDistanceObjective(double iDistanceObjective)
                | 
                |     Sets the distance objective for healing entity.
                | 
                |     Parameters:
                | 
                |         DistanceObjective
                |             Parameter containg the value of the distance objective to be
                |             set.
                | 
                |             Example:
                |                 This example sets the distance objective for the healing of the
                |                 HybShpHealing hybrid shape healing.
                | 
                |                  HybShpHealing.SetDistanceObjective 2.5

        :param float i_distance_objective:
        :rtype: None
        """
        return self.hybrid_shape_healing.SetDistanceObjective(i_distance_objective)

    def set_merging_distance(self, i_merging_distance: float) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetMergingDistance(double iMergingDistance)
                | 
                |     Sets the Merging distance for healing entity.
                | 
                |     Parameters:
                | 
                |         MergingDistance
                |             Parameter containg the value of the merging distance to be
                |             set.
                | 
                |             Example:
                |                 This example sets the merging distance for the healing of the
                |                 HybShpHealing hybrid shape healing.
                | 
                |                  HybShpHealing.SetMergingDistance 2.5

        :param float i_merging_distance:
        :rtype: None
        """
        return self.hybrid_shape_healing.SetMergingDistance(i_merging_distance)

    def set_sharpness_angle(self, i_sharpness_angle: float) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetSharpnessAngle(double iSharpnessAngle)
                | 
                |     Sets the Sharpness Angle for healing entity.
                | 
                |     Parameters:
                | 
                |         SharpnessAngle
                |             Parameter containg the value of the Sharpness Angle to be
                |             set.
                | 
                |             Example:
                |                 This example sets the Sharpness Angle for the healing of the
                |                 HybShpHealing hybrid shape healing.
                | 
                |                  HybShpHealing.SetSharpnessAngle 2.5

        :param float i_sharpness_angle:
        :rtype: None
        """
        return self.hybrid_shape_healing.SetSharpnessAngle(i_sharpness_angle)

    def set_tangency_angle(self, i_tangency_angle: float) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetTangencyAngle(double iTangencyAngle)
                | 
                |     Sets the distance objective for healing entity.
                | 
                |     Parameters:
                | 
                |         TangencyAngle
                |             Parameter containg the value of the Tangency Angle to be
                |             set.
                | 
                |             Example:
                |                 This example sets the Tangency Angle for the healing of the
                |                 HybShpHealing hybrid shape healing.
                | 
                |                  HybShpHealing.SetTangencyAngle 2.5

        :param float i_tangency_angle:
        :rtype: None
        """
        return self.hybrid_shape_healing.SetTangencyAngle(i_tangency_angle)

    def set_tangency_objective(self, i_tangency_objective: float) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetTangencyObjective(double iTangencyObjective)
                | 
                |     Sets the tangency objective for healing entity.
                | 
                |     Parameters:
                | 
                |         TangencyObjective
                |             Parameter containg the value of the Tangency Objective to be
                |             set.
                | 
                |             Example:
                |                 This example sets the Tangency Objective for the healing of the
                |                 HybShpHealing hybrid shape healing.
                | 
                |                  HybShpHealing.SetTangencyObjective 2.5

        :param float i_tangency_objective:
        :rtype: None
        """
        return self.hybrid_shape_healing.SetTangencyObjective(i_tangency_objective)

    def __repr__(self):
        return f'HybridShapeHealing(name="{ self.name }")'
