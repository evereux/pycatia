#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.cat_str_functional_interfaces.sfm_welds import SFMWelds
from pycatia.in_interfaces.reference import Reference
from pycatia.in_interfaces.references import References
from pycatia.system_interfaces.any_object import AnyObject
from pycatia.types.general import cat_variant


class SFMManager(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SfmManager
                | 
                | Services about Structure Functional Modeler applications: SFD and
                | SDD.
                | Role: To manage some services.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.sfm_manager = com_object

    def add_hull(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub AddHull()
                | 
                |     Add the Hull feature according to the PRM resources.
                |     Role: Allows adding the Hull feature according to the PRM
                |     resources.
                | 
                |     Returns:
                |         S_OK if everything ran ok.

        :rtype: None
        """
        return self.sfm_manager.AddHull()

    def get_all_uc1_welds(self) -> SFMWelds:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetAllUC1Welds() As SfmWelds
                | 
                |     Gets all UC1 Weld features in Part.
                | 
                |     Parameters:
                | 
                |         oWelds
                |             [out] The retrieved UC1 Weld features. 
                | 
                |     Returns:
                |         S_OK if everything ran ok.
                | 
                |         Example :
                |             This example gets welds features in Part.
                | 
                |              Dim Welds As SfmWelds
                |              Set Welds = ManagerObj.GetWelds(Nothing)

        :rtype: SFMWelds
        """
        return SFMWelds(self.sfm_manager.GetAllUC1Welds())

    def get_hull(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetHull() As Reference
                | 
                |     Returns the Hull feature in the part.
                | 
                |     Example:
                |         This example retrieves in Hull the Hull object.
                | 
                |          Dim Hull As Reference
                |          SfmManager.GetHull Hull

        :rtype: Reference
        """
        return Reference(self.sfm_manager.GetHull())

    def get_plane_systems(self) -> References:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetPlaneSystems() As References
                | 
                |     Returns the list of PlaneSystems in the part.
                | 
                |     Example:
                |         This example retrieves in PlaneSystems the list of PlaneSystems
                |         objects.
                | 
                |          Dim PlaneSystems As References
                |          SfmManager.GetPlaneSystems PlaneSystems

        :rtype: References
        """
        return References(self.sfm_manager.GetPlaneSystems())

    def get_reference_plane(self, i_plane_system_index: cat_variant, i_plane_index: cat_variant) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetReferencePlane(CATVariant iPlaneSystemIndex,
                | CATVariant iPlaneIndex) As Reference
                | 
                |     Returns a reference plane in the specific PlaneSystems.
                | 
                |     Example:
                |         This example retrieves in RefPlane the reference planes contained into
                |         the 1st PlaneSystem, and which has CROSS.12 as a name.
                | 
                |          Dim RefPlane As Reference
                |          SfmManager.GetReferencePlane 1, "CROSS.12", RefPlane

        :param cat_variant i_plane_system_index:
        :param cat_variant i_plane_index:
        :rtype: Reference
        """
        return Reference(
            self.sfm_manager.GetReferencePlane(
                i_plane_system_index,
                i_plane_index
            )
        )

    def get_super_members(self) -> References:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetSuperMembers() As References
                | 
                |     Returns the list of SuperMembers in the part.
                | 
                |     Example:
                |         This example retrieves in SuperMembers the list of SuperMembers
                |         objects.
                | 
                |          Dim SuperMembers As References
                |          SfmManager.GetSuperMembers SuperMembers

        :rtype: References
        """
        return References(self.sfm_manager.GetSuperMembers())

    def get_super_plates(self) -> References:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetSuperPlates() As References
                | 
                |     Returns the list of SuperPlates in the part.
                | 
                |     Example:
                |         This example retrieves in SuperPlates the list of SuperPlates
                |         objects.
                | 
                |          Dim SuperPlates As References
                |          SfmManager.GetSuperPlates SuperPlates

        :rtype: References
        """
        return References(self.sfm_manager.GetSuperPlates())

    def get_super_stiffeners(self) -> References:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetSuperStiffeners() As References
                | 
                |     Returns the list of SuperStiffeners in the part.
                | 
                |     Example:
                |         This example retrieves in SuperStiffeners the list of SuperStiffeners
                |         objects.
                | 
                |          Dim SuperStiffeners As References
                |          SfmManager.GetSuperStiffeners SuperStiffeners

        :rtype: References
        """
        return References(self.sfm_manager.GetSuperStiffeners())

    def get_super_stiffeners_on_free_edge(self) -> References:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetSuperStiffenersOnFreeEdge() As References
                | 
                |     Returns the list of SuperStiffenersOnFreeEdge in the part.
                | 
                |     Example:
                |         This example retrieves in SuperStiffenersOnFreeEdge the list of
                |         SuperStiffenersOnFreeEdge objects.
                | 
                |          Dim SuperStiffenersOnFreeEdge As References
                |          SfmManager.GetSuperStiffenersOnFreeEdge
                |          SuperStiffenersOnFreeEdge

        :rtype: References
        """
        return References(self.sfm_manager.GetSuperStiffenersOnFreeEdge())

    def init_resources(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub InitResources()
                | 
                |     Initialize environment (PRM resources).
                |     Role: Allows initializing environment (PRM resources).
                | 
                |     Returns:
                |         S_OK if everything ran ok.

        :rtype: None
        """
        return self.sfm_manager.InitResources()

    def synchronize_hull(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SynchronizeHull()
                | 
                |     Synchronize PlaneSystems according with the PRM resources.
                |     Role: Allows synchronizing the PlaneSystems with the PRM
                |     resources.
                | 
                |     Returns:
                |         S_OK if everything ran ok.

        :rtype: None
        """
        return self.sfm_manager.SynchronizeHull()

    def synchronize_planes(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SynchronizePlanes()
                | 
                |     Synchronize PlaneSystems according with the PRM resources.
                |     Role: Allows synchronizing the PlaneSystems with the PRM
                |     resources.
                | 
                |     Returns:
                |         S_OK if everything ran ok.

        :rtype: None
        """
        return self.sfm_manager.SynchronizePlanes()

    def __repr__(self):
        return f'SFMManager(name="{self.name}")'
