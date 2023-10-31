#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.dmaps_interfaces.activity import Activity
from pycatia.dnb_human_sim_interfaces.auto_walk_activity import AutoWalkActivity
from pycatia.dnb_human_sim_interfaces.collision_free_walk import CollisionFreeWalk
from pycatia.dnb_human_sim_interfaces.human_activity_group import HumanActivityGroup
from pycatia.dnb_human_sim_interfaces.human_call_task import HumanCallTask
from pycatia.dnb_human_sim_interfaces.human_task import HumanTask
from pycatia.dnb_human_sim_interfaces.move_to_posture_activity import MoveToPostureActivity
from pycatia.dnb_human_sim_interfaces.pick_activity import PickActivity
from pycatia.dnb_human_sim_interfaces.place_activity import PlaceActivity
from pycatia.dnb_human_sim_interfaces.walk_activity import WalkActivity
from pycatia.product_structure_interfaces.product import Product
from pycatia.system_interfaces.any_object import AnyObject


class HumanActsFactory(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     HumanActsFactory
                | 
                | The object that represents the Human Activity Factory.
                | 
                | Following activity types could be created using the HumanActivity
                | Factory.
                | MoveToPostureActivity
                | WalkActivity (Forward/Backward/SideStep)
                | AutoWalkActivity
                | PickActivity
                | PlaceActivity
                | CollisionFreeWalkActivity(Forward and Backward)
                | HumanActivityGroup
                | HumanCallTaskActivity
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.human_acts_factory = com_object

    def create_auto_walk(self, o_prev_act: Activity) -> AutoWalkActivity:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func CreateAutoWalk(Activity oPrevAct) As AutoWalkActivity
                | 
                |     Returns newly created AutoWalkActivity.
                | 
                |     Parameters:
                | 
                |         iPrevAct
                |             previous activity 
                | 
                |     Returns:
                |         oCreatedAutoWalk newly created AutoWalkActivity
                |
                |     Example:
                | 
                |              This example creates AutoWalk Activity on Plane 
                |
                |            ' Get the Human Acts factory and Human Task List
                |         Dim oHumActsFactory As HumanActsFactory
                |            Dim oHumanTask As HumanTask
                |            Dim iPevAct As Activity
                |         Dim oHT as HumanTask
                |         Dim ActList As Activities
                |         Dim iPrevAct As Activity
                |         Dim oHumTaskList As HumanTaskList
                |         Set oHT = oHumTaskList.Item(1)
                |         Set ActList = oHT.ChildrenActivities
                |         Set iPrevAct = ActList.Item(2) ' MoveToPosture.1
                |         Dim oCreatedAutoWalk as AutoWalkActivity
                |            ....
                |            ....
                |            Set oHumActsFactory = oHumanTask.GetTechnologicalObject("HumanActsFactory")
                | 
                |            ' Create AutoWalk Activity
                |            Set oCreatedAutoWalk = oHumActsFactory.CreateAutoWalk(iPrevAct)

        :param Activity o_prev_act:
        :rtype: AutoWalkActivity
        """
        return AutoWalkActivity(self.human_acts_factory.CreateAutoWalk(o_prev_act.com_object))

    def create_collision_free_walk_bwd_on_arr_area(
            self,
            i_prev_act: Activity,
            i_arr_area: Product,
            i_num_points: int,
            i_search_int: int,
            i_clearence: float,
            i_points: tuple
    ) -> CollisionFreeWalk:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func CreateCollisionFreeWalkBwdOnArrArea(Activity
                | iPrevAct,
                | Product iArrArea,
                | long iNumPoints,
                | HTSSearchIntensity iSearchInt,
                | double iClearence,
                | CATSafeArrayVariant iPoints) As CollisionFreeWalk
                | 
                |     Returns newly created Collision free Walk Backward Activity on Arrangement
                |     Area.
                | 
                |     Parameters:
                | 
                |         iPrevAct
                |             previous activity 
                |         iArrArea
                |             Arrangment Area - Plane of Walk 
                |         iNumPoints
                |             Number of Coplanar-Points defining the Walk Path 
                |         iSearchInt
                |             (see 
                | 
                |         HTSSearchIntensity for list of possible values) 
                |     iClearance
                |         The clearance value to be used for detecting collision between objects
                |         
                |     iPoints
                |         Point values x1,y1,z1 , x2,y2,z2, .... in iArrArea coordinates
                |         
                |     Returns:
                |         oCreatedWalk newly created WalkActivity
                |
                |     Example:
                | 
                |              This example creates WalkBackward Activity on Arrangement
                |              Area
                |
                |         ' From the ProductList get the Arrangement Area
                |         Dim oPPRDoc As PPRDocument
                |         Dim pprprodsProdList As PPRProducts
                |         Dim prodAreasFather As Product
                |         Dim prodAreaFathersChildren As Products
                | 
                |         Set oPPRDoc = DELMIA.ActiveDocument.PPRDocument
                |         Set pprprodsProdList = oPPRDoc.Products
                |         Set prodAreasFather = pprprodsProdList.Item(1)
                |         Set prodAreaFathersChildren = prodAreasFather.Products
                | 
                |         Dim iArrArea As Product
                |         Set iArrArea = prodAreaFathersChildren.GetItem("Area1.1")
                | 
                |         ' Specify the number of coplanar points defining the walk
                |         path
                |         Dim iNumPoints as Long
                |         iNumPoints = 2
                | 
                |         ' Specify the point values for the walk path in oArrArea
                |         co-ordinates
                |         Dim iPoints(6) as Double
                |         iPoints(0) = 0.0         ' Point1 - X
                |         iPoints(1) = 0.0         ' Point1 - Y
                |         iPoints(2) = 0.0         ' Point1 - Z
                |         iPoints(3) = 2000.0      ' Point2 - X
                |         iPoints(4) = 0.0         ' Point2 - Y
                |         iPoints(5) = 0.0         ' Point2 - Z
                | 
                |            ' Get the Human Acts factory
                |         Dim oHumActsFactory As HumanActsFactory
                |            Dim oHumanTask As HumanTask
                |            Dim iPrevAct As Activity
                |         Dim oCreatedWalk as DNBIACollisionFreeWalk
                |            ....
                |            ....
                |            Set oHumActsFactory = oHumanTask.GetTechnologicalObject("HumanActsFactory")
                | 
                |            ' Create Collision free WalkBackward Activity on Arrangement
                |            area
                |            Set oCreatedWalk = oHumActsFactory.CreateCollisionFreeWalkBwdOnArrArea(iPrevAct,
                |                                                                                   iArrArea,
                |                                                                                   iNumPoints,
                |                                                                                   iSearchInt,
                |                                                                                   iClearance,
                |                                                                                   iPoints)
                |         ' Generate constituting MTPs
                |         oCreatedWalk.Update 
                |            ....
                |            ....

        :param Activity i_prev_act:
        :param Product i_arr_area:
        :param int i_num_points:
        :param int i_search_int: enum hts_search_intensity
        :param float i_clearence:
        :param tuple i_points:
        :rtype: CollisionFreeWalk
        """
        return CollisionFreeWalk(
            self.human_acts_factory.CreateCollisionFreeWalkBwdOnArrArea(
                i_prev_act.com_object,
                i_arr_area.com_object,
                i_num_points,
                i_search_int,
                i_clearence,
                i_points
            )
        )

    def create_collision_free_walk_bwd_on_plane(
            self,
            i_prev_act: Activity,
            i_plane_prod: Product,
            i_plane_def: tuple,
            i_num_points: int,
            i_search_int: int,
            i_clearence: float,
            i_points: tuple
    ) -> CollisionFreeWalk:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func CreateCollisionFreeWalkBwdOnPlane(Activity iPrevAct,
                | Product iPlaneProd,
                | CATSafeArrayVariant iPlaneDef,
                | long iNumPoints,
                | HTSSearchIntensity iSearchInt,
                | double iClearence,
                | CATSafeArrayVariant iPoints) As CollisionFreeWalk
                | 
                |     Returns newly created Collision free Walk Backward
                |     Activity.
                | 
                |     Parameters:
                | 
                |         iPrevAct
                |             previous activity 
                |         iPlaneProd
                |             Handle to Product 
                |         iPlaneDef
                |             Walk Plane definition - 9 doubles FirstAxis(i,j,k),
                |             SecondAxis(i,j,k), OriginOfPlane(x,y,z) in iPlaneProd Coordinates
                |             
                |         iNumPoints
                |         iSearchInt
                |             (see 
                | 
                |         HTSSearchIntensity for list of possible values) 
                |     iClearance
                |         The clearance value to be used for detecting collision between objects
                |         Number of Coplanar-Points defining the Walk Path in Plane
                |         
                |     iPoints
                |         Point values x1,y1,z1 , x2,y2,z2, .... iPlaneDef coordinates
                |         
                |     Returns:
                |         oCreatedWalk newly created WalkActivity
                |
                |     Example:
                | 
                |              This example creates WalkBackward Activity on Plane
                |
                | 
                |         ' From the ProductList get the Walk Plane product
                |         Dim oPPRDoc As PPRDocument
                |         Dim pprprodsProdList As PPRProducts
                |         Set oPPRDoc = DELMIA.ActiveDocument.PPRDocument
                |         Set pprprodsProdList = oPPRDoc.Products
                |         Dim oPlaneProd As Product
                |         Set oPlaneProd = pprprodsProdList.Item(2)
                | 
                |         ' Plane Definition.. w.r.to Product
                | 
                |         Dim iPlaneDef(9) as Double
                |         iPlaneDef(0) = 1.0         ' First Axis  - i vec
                |         iPlaneDef(1) = 0.0         ' First Axis  - j vec
                |         iPlaneDef(2) = 0.0         ' First Axis  - k vec
                |         iPlaneDef(3) = 0.0         ' Second Axis - i vec
                |         iPlaneDef(4) = 1.0         ' Second Axis - j vec
                |         iPlaneDef(5) = 0.0         ' Second Axis - k vec
                |         iPlaneDef(6) = 0.0         ' Origin      - X
                |         iPlaneDef(7) = 0.0         ' Origin      - Y
                |         iPlaneDef(8) = 0.0         ' Origin      - Z
                | 
                |         ' Specify the number of coplanar points defining the walk
                |         path
                |         Dim iNumPoints as Long
                |         iNumPoints = 2
                | 
                |         ' Specify the point values for the walk path in oArrArea
                |         co-ordinates
                |         Dim iPoints(6) as Double
                |         iPoints(0) = 0.0         ' Point1 - X
                |         iPoints(1) = 0.0         ' Point1 - Y
                |         iPoints(2) = 0.0         ' Point1 - Z
                |         iPoints(3) = 2000.0      ' Point2 - X
                |         iPoints(4) = 0.0         ' Point2 - Y
                |         iPoints(5) = 0.0         ' Point2 - Z
                | 
                |            ' Get the Human Acts factory
                |         Dim oHumActsFactory As HumanActsFactory
                |            Dim oHumanTask As HumanTask
                |            Dim iPrevAct As Activity
                |         Dim oCreatedWalk as DNBIACollisionFreeWalk
                |            ....
                |            ....
                |            Set oHumActsFactory = oHumanTask.GetTechnologicalObject("HumanActsFactory")
                | 
                |            ' Create Collision free WalkBackward Activity on
                |            Plane
                |            Set oCreatedWalk = oHumActsFactory.CreateCollisionFreeWalkBwdOnPlane(iPrevAct,
                |                                                                                 iPlaneProd,
                |                                                                                 iPlaneDef,
                |                                                                                 iNumPoints,
                |                                                                                 iSearchInt,
                |                                                                                 iClearance,
                |                                                                                 iPoints)
                |         ' Generate constituting MTPs
                |         oCreatedWalk.Update 
                |            ....
                |            ....

        :param Activity i_prev_act:
        :param Product i_plane_prod:
        :param tuple i_plane_def:
        :param int i_num_points:
        :param int i_search_int: enum hts_search_intensity
        :param float i_clearence:
        :param tuple i_points:
        :rtype: CollisionFreeWalk
        """
        return CollisionFreeWalk(
            self.human_acts_factory.CreateCollisionFreeWalkBwdOnPlane(
                i_prev_act.com_object,
                i_plane_prod.com_object,
                i_plane_def,
                i_num_points,
                i_search_int,
                i_clearence,
                i_points
            )
        )

    def create_collision_free_walk_fwd_on_arr_area(
            self,
            i_prev_act: Activity,
            i_arr_area: Product,
            i_num_points: int,
            i_search_int: int,
            i_clearence: float,
            i_points: tuple
    ) -> CollisionFreeWalk:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func CreateCollisionFreeWalkFwdOnArrArea(Activity
                | iPrevAct,
                | Product iArrArea,
                | long iNumPoints,
                | HTSSearchIntensity iSearchInt,
                | double iClearence,
                | CATSafeArrayVariant iPoints) As CollisionFreeWalk
                | 
                |     Returns newly created Collision free Walk Forward
                |     Activity.
                | 
                |     Parameters:
                | 
                |         iPrevAct
                |             Previous Activity 
                |         iArrArea
                |             Arrangment Area - Plane of Walk 
                |         iNumPoints
                |             Number of Coplanar-Points defining the Walk Path 
                |         iSearchInt
                |             (see 
                | 
                |         HTSSearchIntensity for list of possible values) 
                |     iClearance
                |         The clearance value to be used for detecting collision between objects
                |         
                |     iPoints
                |         Point values x1,y1,z1 , x2,y2,z2, .... in iArrArea coordinates
                |         
                |     Returns:
                |         oCreatedWalk Newly created WalkActivity 
                |     Example:
                | 
                |              This example creates Collision free WalkForward Activity on
                |              Arrangement Area
                |          
                | 
                |         ' From the ProductList get the Arrangement Area
                |         Dim oPPRDoc As PPRDocument
                |         Dim pprprodsProdList As PPRProducts
                |         Dim prodAreasFather As Product
                |         Dim prodAreaFathersChildren As Products
                | 
                |         Set oPPRDoc = DELMIA.ActiveDocument.PPRDocument
                |         Set pprprodsProdList = oPPRDoc.Products
                |         Set prodAreasFather = pprprodsProdList.Item(1)
                |         Set prodAreaFathersChildren = prodAreasFather.Products
                | 
                |         Dim iArrArea As Product
                |         Set iArrArea = prodAreaFathersChildren.GetItem("Area1.1")
                | 
                |         ' Specify the number of coplanar points defining the walk
                |         path
                |         Dim iNumPoints as Long
                |         iNumPoints = 2
                | 
                |         ' Specify the point values for the walk path in oArrArea
                |         co-ordinates
                |         Dim iPoints(6) as Double
                |         iPoints(0) = 0.0         ' Point1 - X
                |         iPoints(1) = 0.0         ' Point1 - Y
                |         iPoints(2) = 0.0         ' Point1 - Z
                |         iPoints(3) = 2000.0      ' Point2 - X
                |         iPoints(4) = 0.0         ' Point2 - Y
                |         iPoints(5) = 0.0         ' Point2 - Z
                | 
                |            ' Get the Human Acts factory
                |         Dim oHumActsFactory As HumanActsFactory
                |            Dim oHumanTask As HumanTask
                |            Dim iPrevAct As Activity
                |         Dim oCreatedWalk as DNBIACollisionFreeWalk
                |            ....
                |            ....
                |            Set oHumActsFactory = oHumanTask.GetTechnologicalObject("HumanActsFactory")
                |         Dim iClearance as Double
                |         iClearance = 170
                |         Dim iSearchInt as Long
                |         iSearchInt = 1
                | 
                |            ' Create Collision free WalkForward Activity on Arrangement
                |            area
                |            Set oCreatedWalk = oHumActsFactory.CreateCollisionFreeWalkFwdOnArrArea(iPrevAct,
                |                                                                                   iArrArea,
                |                                                                                   iNumPoints,
                |                                                                                   iSearchInt,
                |                                                                                   iClearance,
                |                                                                                   iPoints)
                |         ' Generate constituting MTPs
                |         oCreatedWalk.Update 
                |            ....
                |            ....

        :param Activity i_prev_act:
        :param Product i_arr_area:
        :param int i_num_points:
        :param int i_search_int: enum hts_search_intensity
        :param float i_clearence:
        :param tuple i_points:
        :rtype: CollisionFreeWalk
        """
        return CollisionFreeWalk(
            self.human_acts_factory.CreateCollisionFreeWalkFwdOnArrArea(
                i_prev_act.com_object,
                i_arr_area.com_object,
                i_num_points,
                i_search_int,
                i_clearence,
                i_points
            )
        )

    def create_collision_free_walk_fwd_on_plane(
            self,
            i_prev_act: Activity,
            i_plane_prod: Product,
            i_plane_def: tuple,
            i_num_points: int,
            i_search_int: int,
            i_clearence: float,
            i_points: tuple
    ) -> CollisionFreeWalk:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func CreateCollisionFreeWalkFwdOnPlane(Activity iPrevAct,
                | Product iPlaneProd,
                | CATSafeArrayVariant iPlaneDef,
                | long iNumPoints,
                | HTSSearchIntensity iSearchInt,
                | double iClearence,
                | CATSafeArrayVariant iPoints) As CollisionFreeWalk
                | 
                |     Returns newly created Collision free Walk Forward Activity
                | 
                |     Parameters:
                | 
                |         iPrevAct
                |             previous activity 
                |         iPlaneProd
                |             Handle to Walk plane product 
                |         iPlaneDef
                |             Walk Plane definition - 9 doubles FirstAxis(i,j,k),
                |             SecondAxis(i,j,k), OriginOfPlane(x,y,z) in iPlaneProd Coordinates
                |             
                |         iNumPoints
                |             Number of Coplanar-Points defining the Walk Path in Plane
                |             
                |         iSearchInt
                |             (see 
                | 
                |         HTSSearchIntensity for list of possible values) 
                |     iClearance
                |         The clearance value to be used for detecting collision between objects
                |         
                |     iPoints
                |         Point values x1,y1,z1 , x2,y2,z2, .... iPlaneDef coordinates
                |         
                |     Returns:
                |         oCreatedWalk newly created WalkActivity
                |
                |     Example:
                | 
                |              This example creates WalkForward Activity on Plane
                |
                |         ' From the ProductList get the Walk Plane product
                |         Dim oPPRDoc As PPRDocument
                |         Dim pprprodsProdList As PPRProducts
                |         Set oPPRDoc = DELMIA.ActiveDocument.PPRDocument
                |         Set pprprodsProdList = oPPRDoc.Products
                |         Dim oPlaneProd As Product
                |         Set oPlaneProd = pprprodsProdList.Item(2)
                | 
                |         ' Plane Definition.. w.r.to Product
                | 
                |         Dim iPlaneDef(9) as Double
                |         iPlaneDef(0) = 1.0         ' First Axis  - i vec
                |         iPlaneDef(1) = 0.0         ' First Axis  - j vec
                |         iPlaneDef(2) = 0.0         ' First Axis  - k vec
                |         iPlaneDef(3) = 0.0         ' Second Axis - i vec
                |         iPlaneDef(4) = 1.0         ' Second Axis - j vec
                |         iPlaneDef(5) = 0.0         ' Second Axis - k vec
                |         iPlaneDef(6) = 0.0         ' Origin      - X
                |         iPlaneDef(7) = 0.0         ' Origin      - Y
                |         iPlaneDef(8) = 0.0         ' Origin      - Z
                | 
                |         ' Specify the number of coplanar points defining the walk
                |         path
                |         Dim iNumPoints as Long
                |         iNumPoints = 2
                | 
                |         ' Specify the point values for the walk path in oArrArea
                |         co-ordinates
                |         Dim iPoints(6) as Double
                |         iPoints(0) = 0.0         ' Point1 - X
                |         iPoints(1) = 0.0         ' Point1 - Y
                |         iPoints(2) = 0.0         ' Point1 - Z
                |         iPoints(3) = 2000.0      ' Point2 - X
                |         iPoints(4) = 0.0         ' Point2 - Y
                |         iPoints(5) = 0.0         ' Point2 - Z
                | 
                |            ' Get the Human Acts factory
                |         Dim oHumActsFactory As HumanActsFactory
                |            Dim oHumanTask As HumanTask
                |            Dim iPrevAct As Activity
                |         Dim oCreatedWalk as DNBIACollisionFreeWalk
                |            ....
                |            ....
                |            Set oHumActsFactory = oHumanTask.GetTechnologicalObject("HumanActsFactory")
                | 
                |            ' Create Collision free WalkForward Activity on
                |            Plane
                |            Set oCreatedWalk = oHumActsFactory.CreateCollisionFreeWalkFwdOnPlane(iPrevAct, iPlaneProd, iPlaneDef, iNumPoints, iPoints) 
                |         ' Generate constituting MTPs
                |         oCreatedWalk.Update 
                |            ....
                |            ....

        :param Activity i_prev_act:
        :param Product i_plane_prod:
        :param tuple i_plane_def:
        :param int i_num_points:
        :param int i_search_int: enum hts_search_intensity
        :param float i_clearence:
        :param tuple i_points:
        :rtype: CollisionFreeWalk
        """
        return CollisionFreeWalk(
            self.human_acts_factory.CreateCollisionFreeWalkFwdOnPlane(
                i_prev_act.com_object,
                i_plane_prod.com_object,
                i_plane_def,
                i_num_points,
                i_search_int,
                i_clearence,
                i_points
            )
        )

    def create_human_activity_group(self, i_prev_act: Activity) -> HumanActivityGroup:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func CreateHumanActivityGroup(Activity iPrevAct) As
                | HumanActivityGroup
                | 
                |     Returns newly created HumanActivityGroupActivity.
                | 
                |     Parameters:
                | 
                |         iPrevAct
                |             previous activity 
                | 
                |     Returns:
                |         oHAG newly created HumanActivityGroup
                |
                |     Example:
                | 
                |              This example creates Human Activity Group
                |              Activity
                |
                |            ' Get the Human Acts factory
                |         Dim oHumActsFactory As HumanActsFactory
                |            Dim oHumanTask As HumanTask
                |         ...
                |            Dim iPrevAct As Activity
                |         Dim oCreatedHAG as DNBIAHumanActivityGroup
                |            ....
                |            ....
                |            Set oHumActsFactory = oHumanTask.GetTechnologicalObject("HumanActsFactory")
                | 
                |            ' Create Human Activity Group
                |            Set oCreatedHAG = oHumActsFactory.CreateHumanActivityGroup(iPrevAct)

        :param Activity i_prev_act:
        :rtype: HumanActivityGroup
        """
        return HumanActivityGroup(self.human_acts_factory.CreateHumanActivityGroup(i_prev_act.com_object))

    def create_human_call_task(self, i_previous_activity: Activity, i_called_task: HumanTask) -> HumanCallTask:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func CreateHumanCallTask(Activity iPreviousActivity,
                | HumanTask iCalledTask) As HumanCallTask
                | 
                |     Returns newly created HumanCallTask.
                | 
                |     Parameters:
                | 
                |         iPrevAct
                |             previous activity 
                |         iCalledTask
                |             The Human Task that has to be called from the Call Task Activity
                |             
                | 
                |     Returns:
                |         oCreatedHumanCallTaskAct newly created Human Call Task activity
                |         
                |     Example:
                | 
                |              This example creates Human CallTask Activity
                |
                |            ' Get the Human Acts factory
                |         Dim oHumActsFactory As HumanActsFactory
                |            Dim oHumanTask As HumanTask ' The parent task that will have the
                |            call task activity as child
                |         ...
                |            Dim iPrevAct As Activity
                |         Dim iCalledTask As HumanTask ' The human task that will be called from
                |         CallTask activity
                |         ...
                |         Dim oCreatedHumanCallTaskAct as
                |         DNBIAHumanCallTaskActivity
                |            ....
                |            ....
                |            Set oHumActsFactory = oHumanTask.GetTechnologicalObject("HumanActsFactory")
                | 
                |            ' Create Human Call Task Activity
                |            Set oCreatedHumanCallTaskAct = oHumActsFactory.CreateHumanCallTask(iPrevAct, iCalledTask)

        :param Activity i_previous_activity:
        :param HumanTask i_called_task:
        :rtype: HumanCallTask
        """
        return HumanCallTask(
            self.human_acts_factory.CreateHumanCallTask(i_previous_activity.com_object, i_called_task.com_object))

    def create_move_to_posture(self, i_prev_act: Activity) -> MoveToPostureActivity:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func CreateMoveToPosture(Activity iPrevAct) As
                | MoveToPostureActivity
                | 
                |     Returns newly created MoveToPostureActivity.
                |     Current posture of Manikin is set as joint-values for created
                |     MoveToPostureActivity. Use MoveToPostureActivity APIs to change
                |     joint-values.
                | 
                |     Parameters:
                | 
                |         iPrevAct
                |             previous activity 
                | 
                |     Returns:
                |         oCreatedMTP newly created MoveToPostureActivity
                |
                |     Example:
                | 
                |              This example creates MoveToPosture Activity 
                |
                |            ' Get the Human Acts factory
                |         Dim oHumActsFactory As HumanActsFactory
                |            Dim oHumanTask As HumanTask
                |            Dim iPrevAct As Activity
                |         Dim oCreatedMTP as MoveToPostureActivity
                |            ....
                |            ....
                |            Set oHumActsFactory = oHumanTask.GetTechnologicalObject("HumanActsFactory")
                | 
                |            ' Create MoveToPosture Activity
                |            Set oCreatedMTP = oHumActsFactory.CreateMoveToPosture(iPrevAct) 
                |            ....
                |            ....

        :param Activity i_prev_act:
        :rtype: MoveToPostureActivity
        """
        return MoveToPostureActivity(self.human_acts_factory.CreateMoveToPosture(i_prev_act.com_object))

    def create_pick(
            self,
            i_prev_act: Activity,
            i_pick_type: int,
            b_create_cst_with_picking_hand: bool,
            i_picking_hand: int,
            i_picked_products: tuple
    ) -> PickActivity:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func CreatePick(Activity iPrevAct,
                | HTSPickType iPickType,
                | boolean bCreateCstWithPickingHand,
                | HTSHand iPickingHand,
                | CATSafeArrayVariant iPickedProducts) As PickActivity
                | 
                |     Returns newly created Pick Activity.
                | 
                |     Parameters:
                | 
                |         iPrevAct
                |             previous activity 
                |         iPickType
                |             Pick Type: SINGLE_HAND or BOTH_HANDS 
                |         bCreateCstWithPickingHand
                |             Boolean flag to indicate whether constraint has to be created
                |             between the picked object and picking hand 
                |         iPickingHand
                |             picking hand: HAND_RIGHT or HAND_LEFT 
                |         iPickedProducts
                |             List of picked products 
                | 
                |     Returns:
                |         oCreatedPick newly created PickActivity
                |
                |     Example:
                | 
                |              This example creates Pick Activity
                |
                |            ' Get the Human Acts factory and Human Task List
                |         Dim oHumActsFactory As HumanActsFactory
                |            Dim oHumanTask As HumanTask
                |         Dim oHT as HumanTask
                |         Dim ActList As Activities
                |         Dim iPrevAct As Activity
                |         Dim oHumTaskList As HumanTaskList
                |         Set oHT = oHumTaskList.Item(1)
                |         Set ActList = oHT.ChildrenActivities
                |         Set iPrevAct = ActList.Item(2) ' MoveToPosture.1
                |         Dim oCreatedPick as PickActivity
                |            ....
                |         ' Specify the picked products
                |         Dim iPickedProds(1) As AnyObject
                |         Dim oPPRDoc As PPRDocument
                |         Dim pprprodsProdList As PPRProducts
                |         Set pprprodsProdList = oPPRDoc.Products
                |         Set iPickedProducts = pprprodsProdList.Item(2)
                |            ....
                |            Set oHumActsFactory = oHumanTask.GetTechnologicalObject("HumanActsFactory")
                | 
                |            ' Create Pick Activity
                |            Set oCreatePick = oHumActsFactory.CreatePick(iPrevAct,SINGLE_HAND, TRUE, HAND_RIGHT, iPickedProducts)

        :param Activity i_prev_act:
        :param int i_pick_type: enum hts_pick_type
        :param bool b_create_cst_with_picking_hand:
        :param int i_picking_hand: enum hts_hand
        :param tuple i_picked_products:
        :rtype: PickActivity
        """
        return PickActivity(
            self.human_acts_factory.CreatePick(
                i_prev_act.com_object,
                i_pick_type,
                b_create_cst_with_picking_hand,
                i_picking_hand,
                i_picked_products
            )
        )

    def create_place(self, i_prev_act: Activity, i_placed_products: tuple, i_offset: tuple) -> PlaceActivity:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func CreatePlace(Activity iPrevAct,
                | CATSafeArrayVariant iPlacedProducts,
                | CATSafeArrayVariant iOffset) As PlaceActivity
                | 
                |     Returns newly created Place Activity.
                | 
                |     Parameters:
                | 
                |         iPrevAct
                |             previous activity 
                |         iPlacedProducts
                |             List of products to be placed 
                |         iPlaceOffset
                |             Offset to be maintainted between the placing hand and the object.
                |             The offset has to be specified as the relative trnsformation between the
                |             placing hand and the object to be placed. The first 9 entries correspond to the
                |             rotation matrix and the next 3 entries correspond to the position
                |             vector.
                |             R1x R1y R1z
                |             R2x R2y R2z
                |             R3x R3y R3z
                |             Px Py Pz
                |             R1x:x-component of x axis
                |             R2x:y-component of x axis
                |             R3x:z-component of x axis
                |             R1y:x-component of y axis
                |             R2y:y-component of y axis
                |             R3y:z-component of y axis
                |             R1z:x-component of z axis
                |             R2z:y-component of z axis
                |             R3z:z-component of z axis
                | 
                |     Returns:
                |         oCreatedPlace Newly created PlaceActivity
                |
                |     Example:
                | 
                |              This example creates Place Activity
                |
                |            ' Get the Human Acts factory and Human Task List
                |         Dim oHumActsFactory As HumanActsFactory
                |            Dim oHumanTask As HumanTask
                |         Dim oHT as HumanTask
                |         Dim ActList As Activities
                |         Dim iPrevAct As Activity
                |         Dim oHumTaskList As HumanTaskList
                |         Set oHT = oHumTaskList.Item(1)
                |         Set ActList = oHT.ChildrenActivities
                |         Set iPrevAct = ActList.Item(2) ' MoveToPosture.1
                |         Dim oCreatedPlace as Placectivity
                |            ....
                |         ' Get the list of picked products from the Pick
                |         Activity
                |         Dim iPickedProducts As AnyObject
                |          'Example of 45 degree rotation around the x-axis of placing
                |          hand
                |         Dim iPlaceOffset(12) As Double ' 12 doubles - 0 to 11; relative
                |         transformation between hand and object 
                |         ' X axis rotation component
                |         iPlaceOffset( 0 )  = 1
                |         iPlaceOffset( 3 )  = 0
                |         iPlaceOffset( 6 )  = 0
                |         ' Y axis rotation component
                |         iPlaceOffset( 1 )  =0
                |         iPlaceOffset( 4 )  =0.707
                |         iPlaceOffset( 7 )  = 0.707
                |         ' Z axis rotation component
                |         iPlaceOffset( 2 )  = 0
                |         iPlaceOffset( 5 ) = -0.707
                |         iPlaceOffset( 8 ) = 0.707
                |         ' position vector (relative vector between the hand and
                |         object)
                |         iPlaceOffset( 9 )  = 0
                |         iPlaceOffset( 10 )  = 0
                |         iPlaceOffset( 11 )  = 0
                |            Set oHumActsFactory = oHumanTask.GetTechnologicalObject("HumanActsFactory")
                | 
                |            ' Create Place Activity
                |            Set oCreatedPlace = oHumActsFactory.CreatePlace(iPrevAct,iPickedProducts, iPlaceOffset);

        :param Activity i_prev_act:
        :param tuple i_placed_products:
        :param tuple i_offset:
        :rtype: PlaceActivity
        """
        return PlaceActivity(self.human_acts_factory.CreatePlace(i_prev_act.com_object, i_placed_products, i_offset))

    def create_side_step_on_arr_area(
            self,
            i_prev_act: Activity,
            i_arr_area: Product,
            i_start_pt: tuple,
            i_end_pt: tuple
    ) -> WalkActivity:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func CreateSideStepOnArrArea(Activity iPrevAct,
                | Product iArrArea,
                | CATSafeArrayVariant iStartPt,
                | CATSafeArrayVariant iEndPt) As WalkActivity
                | 
                |     Returns newly created Side-Step Activity.
                | 
                |     Parameters:
                | 
                |         iPrevAct
                |             previous activity 
                |         iArrArea
                |             Arrangment Area - Plane of Walk 
                |         iStartPt
                |             Start Point - x,y,z in iArrArea coordinates 
                |         iEndPt
                |             End Point - x,y,z in iArrArea coordinates 
                | 
                |     Returns:
                |         oCreatedWalk newly created WalkActivity
                | 
                |         ' From the ProductList get the Arrangement Area
                |         Dim oPPRDoc As PPRDocument
                |         Dim pprprodsProdList As PPRProducts
                |         Dim prodAreasFather As Product
                |         Dim prodAreaFathersChildren As Products
                | 
                |         Set oPPRDoc = DELMIA.ActiveDocument.PPRDocument
                |         Set pprprodsProdList = oPPRDoc.Products
                |         Set prodAreasFather = pprprodsProdList.Item(1)
                |         Set prodAreaFathersChildren = prodAreasFather.Products
                | 
                |         Dim iArrArea As Product
                |         Set iArrArea = prodAreaFathersChildren.GetItem("Area1.1")
                | 
                |         ' Specify the Start and End  points for the side step walk
                |         activity
                |         Dim iStart(3) as Double
                |         Dim iEnd(3) as Double
                |         iStart(0) = 0
                |         iStart(1) = 0
                |         iStart(2) = 0.0
                |         iEnd(0) = 2000
                |         iEnd(1) = 0
                |         iEnd(2) = 0.0
                | 
                |            ' Get the Human Acts factory
                |         Dim oHumActsFactory As HumanActsFactory
                |            Dim oHumanTask As HumanTask
                |            Dim iPrevAct As Activity
                |         Dim oCreatedWalk as WalkActivity
                |            ....
                |            ....
                |            Set oHumActsFactory = oHumanTask.GetTechnologicalObject("HumanActsFactory")
                | 
                |            ' Create SideStep Activity on Arrangement area
                |            oCreatedWalk = oHumActsFactory.CreateSideStepOnArrArea(iPrevAct, iArrArea, iStartPt, iEndPt) 
                |         ' Generate constituting MTPs
                |         oCreatedWalk.Update

        :param Activity i_prev_act:
        :param Product i_arr_area:
        :param tuple i_start_pt:
        :param tuple i_end_pt:
        :rtype: WalkActivity
        """
        return WalkActivity(
            self.human_acts_factory.CreateSideStepOnArrArea(
                i_prev_act.com_object,
                i_arr_area.com_object,
                i_start_pt,
                i_end_pt
            )
        )

    def create_side_step_on_plane(
            self,
            i_prev_act: Activity,
            i_plane_prod: Product,
            i_plane_def: tuple,
            i_start_pt: tuple,
            id_end_pt: tuple
    ) -> WalkActivity:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func CreateSideStepOnPlane(Activity iPrevAct,
                | Product iPlaneProd,
                | CATSafeArrayVariant iPlaneDef,
                | CATSafeArrayVariant iStartPt,
                | CATSafeArrayVariant idEndPt) As WalkActivity
                | 
                |     Returns newly created Side-Step Activity.
                | 
                |     Parameters:
                | 
                |         iPrevAct
                |             previous activity 
                |         iPlaneProd
                |             Handle to Product 
                |         iPlaneDef
                |             Walk Plane definition - 9 doubles FirstAxis(i,j,k),
                |             SecondAxis(i,j,k), OriginOfPlane(x,y,z) in oCGRProd Coordinates
                |             
                |         iStartPt
                |             Start Point - x,y,z in iPlaneDef coordinates 
                |         iEndPt
                |             End Point - x,y,z in iPlaneDef coordinates 
                | 
                |     Returns:
                |         oCreatedWalk newly created WalkActivity 
                |     Example:
                | 
                |              This example creates SideStep Activity on Plane 
                |          
                | 
                |         ' From the ProductList get the Walk Plane product
                |         Dim oPPRDoc As PPRDocument
                |         Dim pprprodsProdList As PPRProducts
                |         Set oPPRDoc = DELMIA.ActiveDocument.PPRDocument
                |         Set pprprodsProdList = oPPRDoc.Products
                |         Dim oPlaneProd As Product
                |         Set oPlaneProd = pprprodsProdList.Item(2)
                | 
                |         ' Plane Definition.. w.r.to Product
                | 
                |         Dim adPlaneDef(9) as Double
                |         adPlaneDef(0) = 1.0         ' First Axis  - i vec
                |         adPlaneDef(1) = 0.0         ' First Axis  - j vec
                |         adPlaneDef(2) = 0.0         ' First Axis  - k vec
                |         adPlaneDef(3) = 0.0         ' Second Axis - i vec
                |         adPlaneDef(4) = 1.0         ' Second Axis - j vec
                |         adPlaneDef(5) = 0.0         ' Second Axis - k vec
                |         adPlaneDef(6) = 0.0         ' Origin      - X
                |         adPlaneDef(7) = 0.0         ' Origin      - Y
                |         adPlaneDef(8) = 0.0         ' Origin      - Z
                | 
                |         ' Specify the number of coplanar points defining the walk
                |         path
                |         Dim iNumPoints as Long
                |         iNumPoints = 2
                | 
                |         ' Specify the point values for the walk path in oArrArea
                |         co-ordinates
                |         Dim adStart(3) as Double
                |         Dim adEnd(3) as Double
                |         adStart(0) = 0
                |         adStart(1) = 0
                |         adStart(2) = 0.0
                |         adEnd(0) = 2000
                |         adEnd(1) = 0
                |         adEnd(2) = 0.0
                | 
                |            ' Get the Human Acts factory
                |         Dim oHumActsFactory As HumanActsFactory
                |            Dim oHumanTask As HumanTask
                |            Dim iPeviousActivity As Activity
                |         Dim oCreatedWalk as WalkActivity
                |            ....
                |            ....
                |            Set oHumActsFactory = oHumanTask.GetTechnologicalObject("HumanActsFactory")
                | 
                |            ' Create SideStep Activity on Plane
                |            oCreatedWalk = oHumActsFactory.CreateSideStepOnPlane(iPrevAct, iPlaneProd, iPlaneDef, iStartPt, iEndPt) 
                |         ' Generate constituting MTPs
                |         oCreatedWalk.Update 
                |            ....
                |            ....

        :param Activity i_prev_act:
        :param Product i_plane_prod:
        :param tuple i_plane_def:
        :param tuple i_start_pt:
        :param tuple id_end_pt:
        :rtype: WalkActivity
        """
        return WalkActivity(
            self.human_acts_factory.CreateSideStepOnPlane(
                i_prev_act.com_object,
                i_plane_prod.com_object,
                i_plane_def,
                i_start_pt,
                id_end_pt
            )
        )

    def create_walk_bwd_on_arr_area(
            self,
            i_prev_act: Activity,
            i_arr_area: Product,
            i_num_points: int,
            i_points: tuple) -> WalkActivity:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func CreateWalkBwdOnArrArea(Activity iPrevAct,
                | Product iArrArea,
                | long iNumPoints,
                | CATSafeArrayVariant iPoints) As WalkActivity
                | 
                |     Returns newly created Walk Backward Activity on Arrangement
                |     Area.
                | 
                |     Parameters:
                | 
                |         iPrevAct
                |             previous activity 
                |         iArrArea
                |             Arrangment Area - Plane of Walk 
                |         iNumPoints
                |             Number of Coplanar-Points defining the Walk Path 
                |         iPoints
                |             Point values x1,y1,z1 , x2,y2,z2, .... in iArrArea coordinates
                |
                |     Returns:
                |         oCreatedWalk newly created WalkActivity
                |
                |     Example:
                | 
                |              This example creates WalkBackward Activity on Arrangement
                |              Area
                |
                |         ' From the ProductList get the Arrangement Area
                |         Dim oPPRDoc As PPRDocument
                |         Dim pprprodsProdList As PPRProducts
                |         Dim prodAreasFather As Product
                |         Dim prodAreaFathersChildren As Products
                | 
                |         Set oPPRDoc = DELMIA.ActiveDocument.PPRDocument
                |         Set pprprodsProdList = oPPRDoc.Products
                |         Set prodAreasFather = pprprodsProdList.Item(1)
                |         Set prodAreaFathersChildren = prodAreasFather.Products
                | 
                |         Dim iArrArea As Product
                |         Set iArrArea = prodAreaFathersChildren.GetItem("Area1.1")
                | 
                |         ' Specify the number of coplanar points defining the walk
                |         path
                |         Dim iNumPoints as Long
                |         iNumPoints = 2
                | 
                |         ' Specify the point values for the walk path in oArrArea
                |         co-ordinates
                |         Dim iPoints(6) as Double
                |         iPoints(0) = 0.0         ' Point1 - X
                |         iPoints(1) = 0.0         ' Point1 - Y
                |         iPoints(2) = 0.0         ' Point1 - Z
                |         iPoints(3) = 2000.0      ' Point2 - X
                |         iPoints(4) = 0.0         ' Point2 - Y
                |         iPoints(5) = 0.0         ' Point2 - Z
                | 
                |            ' Get the Human Acts factory
                |         Dim oHumActsFactory As HumanActsFactory
                |            Dim oHumanTask As HumanTask
                |            Dim iPrevAct As Activity
                |         Dim oCreatedWalk as WalkActivity
                |            ....
                |            ....
                |            Set oHumActsFactory = oHumanTask.GetTechnologicalObject("HumanActsFactory")
                | 
                |            ' Create WalkBackward Activity on Arrangement area
                |            Set oCreatedWalk = oHumActsFactory.CreateWalkBwdOnArrArea(iPrevAct, iArrArea, iNumPoints, iPoints) 
                |         ' Generate constituting MTPs
                |         oCreatedWalk.Update 
                |            ....
                |            ....

        :param Activity i_prev_act:
        :param Product i_arr_area:
        :param int i_num_points:
        :param tuple i_points:
        :rtype: WalkActivity
        """
        return WalkActivity(
            self.human_acts_factory.CreateWalkBwdOnArrArea(
                i_prev_act.com_object,
                i_arr_area.com_object,
                i_num_points,
                i_points
            )
        )

    def create_walk_bwd_on_plane(
            self,
            i_prev_act: Activity,
            i_plane_prod: Product,
            i_plane_def: tuple,
            i_num_points: int,
            i_points: tuple
    ) -> WalkActivity:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func CreateWalkBwdOnPlane(Activity iPrevAct,
                | Product iPlaneProd,
                | CATSafeArrayVariant iPlaneDef,
                | long iNumPoints,
                | CATSafeArrayVariant iPoints) As WalkActivity
                | 
                |     Returns newly created Walk Backward Activity.
                | 
                |     Parameters:
                | 
                |         iPrevAct
                |             previous activity 
                |         iPlaneProd
                |             Handle to Product 
                |         iPlaneDef
                |             Walk Plane definition - 9 doubles FirstAxis(i,j,k),
                |             SecondAxis(i,j,k), OriginOfPlane(x,y,z) in iPlaneProd Coordinates
                |             
                |         iNumPoints
                |             Number of Coplanar-Points defining the Walk Path in Plane
                |             
                |         iPoints
                |             Point values x1,y1,z1 , x2,y2,z2, .... iPlaneDef coordinates
                |             
                | 
                |     Returns:
                |         oCreatedWalk newly created WalkActivity
                |
                |     Example:
                | 
                |              This example creates WalkBackward Activity on Plane
                |
                |         ' From the ProductList get the Walk Plane product
                |         Dim oPPRDoc As PPRDocument
                |         Dim pprprodsProdList As PPRProducts
                |         Set oPPRDoc = DELMIA.ActiveDocument.PPRDocument
                |         Set pprprodsProdList = oPPRDoc.Products
                |         Dim oPlaneProd As Product
                |         Set oPlaneProd = pprprodsProdList.Item(2)
                | 
                |         ' Plane Definition.. w.r.to Product
                | 
                |         Dim iPlaneDef(9) as Double
                |         iPlaneDef(0) = 1.0         ' First Axis  - i vec
                |         iPlaneDef(1) = 0.0         ' First Axis  - j vec
                |         iPlaneDef(2) = 0.0         ' First Axis  - k vec
                |         iPlaneDef(3) = 0.0         ' Second Axis - i vec
                |         iPlaneDef(4) = 1.0         ' Second Axis - j vec
                |         iPlaneDef(5) = 0.0         ' Second Axis - k vec
                |         iPlaneDef(6) = 0.0         ' Origin      - X
                |         iPlaneDef(7) = 0.0         ' Origin      - Y
                |         iPlaneDef(8) = 0.0         ' Origin      - Z
                | 
                |         ' Specify the number of coplanar points defining the walk
                |         path
                |         Dim iNumPoints as Long
                |         iNumPoints = 2
                | 
                |         ' Specify the point values for the walk path in oArrArea
                |         co-ordinates
                |         Dim iPoints(6) as Double
                |         iPoints(0) = 0.0         ' Point1 - X
                |         iPoints(1) = 0.0         ' Point1 - Y
                |         iPoints(2) = 0.0         ' Point1 - Z
                |         iPoints(3) = 2000.0      ' Point2 - X
                |         iPoints(4) = 0.0         ' Point2 - Y
                |         iPoints(5) = 0.0         ' Point2 - Z
                | 
                |            ' Get the Human Acts factory
                |         Dim oHumActsFactory As HumanActsFactory
                |            Dim oHumanTask As HumanTask
                |            Dim iPrevAct As Activity
                |         Dim oCreatedWalk as WalkActivity
                |            ....
                |            ....
                |            Set oHumActsFactory = oHumanTask.GetTechnologicalObject("HumanActsFactory")
                | 
                |            ' Create WalkBackward Activity on Plane
                |            Set oCreatedWalk = oHumActsFactory.CreateWalkBwdOnPlane(iPrevAct, iPlaneProd, iPlaneDef, iNumPoints, iPoints) 
                |         ' Generate constituting MTPs
                |         oCreatedWalk.Update 
                |            ....
                |            ....

        :param Activity i_prev_act:
        :param Product i_plane_prod:
        :param tuple i_plane_def:
        :param int i_num_points:
        :param tuple i_points:
        :rtype: WalkActivity
        """
        return WalkActivity(
            self.human_acts_factory.CreateWalkBwdOnPlane(
                i_prev_act.com_object,
                i_plane_prod.com_object,
                i_plane_def,
                i_num_points,
                i_points
            )
        )

    def create_walk_fwd_on_arr_area(
            self,
            i_prev_act: Activity,
            i_arr_area: Product,
            i_num_points: int,
            i_points: tuple
    ) -> WalkActivity:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func CreateWalkFwdOnArrArea(Activity iPrevAct,
                | Product iArrArea,
                | long iNumPoints,
                | CATSafeArrayVariant iPoints) As WalkActivity
                | 
                |     Returns newly created Walk Forward Activity.
                | 
                |     Parameters:
                | 
                |         iPrevAct
                |             previous activity 
                |         iArrArea
                |             Arrangment Area - Plane of Walk 
                |         iNumPoints
                |             Number of Coplanar-Points defining the Walk Path 
                |         iPoints
                |             Point values x1,y1,z1 , x2,y2,z2, .... in iArrArea coordinates
                |
                |     Returns:
                |         oCreatedWalk newly created WalkActivity
                |
                |     Example:
                | 
                |              This example creates WalkForward Activity on Arrangement
                |              Area
                |
                |         ' From the ProductList get the Arrangement Area
                |         Dim oPPRDoc As PPRDocument
                |         Dim pprprodsProdList As PPRProducts
                |         Dim prodAreasFather As Product
                |         Dim prodAreaFathersChildren As Products
                | 
                |         Set oPPRDoc = DELMIA.ActiveDocument.PPRDocument
                |         Set pprprodsProdList = oPPRDoc.Products
                |         Set prodAreasFather = pprprodsProdList.Item(1)
                |         Set prodAreaFathersChildren = prodAreasFather.Products
                | 
                |         Dim iArrArea As Product
                |         Set iArrArea = prodAreaFathersChildren.GetItem("Area1.1")
                | 
                |         ' Specify the number of coplanar points defining the walk
                |         path
                |         Dim iNumPoints as Long
                |         iNumPoints = 2
                | 
                |         ' Specify the point values for the walk path in oArrArea
                |         co-ordinates
                |         Dim iPoints(6) as Double
                |         iPoints(0) = 0.0         ' Point1 - X
                |         iPoints(1) = 0.0         ' Point1 - Y
                |         iPoints(2) = 0.0         ' Point1 - Z
                |         iPoints(3) = 2000.0      ' Point2 - X
                |         iPoints(4) = 0.0         ' Point2 - Y
                |         iPoints(5) = 0.0         ' Point2 - Z
                | 
                |            ' Get the Human Acts factory
                |         Dim oHumActsFactory As HumanActsFactory
                |            Dim oHumanTask As HumanTask
                |            Dim iPrevAct As Activity
                |         Dim oCreatedWalk as WalkActivity
                |            ....
                |            ....
                |            Set oHumActsFactory = oHumanTask.GetTechnologicalObject("HumanActsFactory")
                | 
                |            ' Create WalkForward Activity on Arrangement area
                |            Set oCreatedWalk = oHumActsFactory.CreateWalkFwdOnArrArea(iPrevAct, iArrArea, iNumPoints, iPoints) 
                |         ' Generate constituting MTPs
                |         oCreatedWalk.Update 
                |            ....
                |            ....

        :param Activity i_prev_act:
        :param Product i_arr_area:
        :param int i_num_points:
        :param tuple i_points:
        :rtype: WalkActivity
        """
        return WalkActivity(
            self.human_acts_factory.CreateWalkFwdOnArrArea(
                i_prev_act.com_object,
                i_arr_area.com_object,
                i_num_points,
                i_points
            )
        )

    def create_walk_fwd_on_plane(
            self,
            i_prev_act: Activity,
            i_prod: Product,
            i_plane_def: tuple,
            i_num_points: int,
            i_points: tuple
    ) -> WalkActivity:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func CreateWalkFwdOnPlane(Activity iPrevAct,
                | Product iProd,
                | CATSafeArrayVariant iPlaneDef,
                | long iNumPoints,
                | CATSafeArrayVariant iPoints) As WalkActivity
                | 
                |     Returns newly created Walk Forward Activity
                | 
                |     Parameters:
                | 
                |         iPrevAct
                |             previous activity 
                |         iPlaneProd
                |             Handle to Walk plane product 
                |         iPlaneDef
                |             Walk Plane definition - 9 doubles FirstAxis(i,j,k),
                |             SecondAxis(i,j,k), OriginOfPlane(x,y,z) in iPlaneProd Coordinates
                |             
                |         iNumPoints
                |             Number of Coplanar-Points defining the Walk Path in Plane
                |             
                |         iPoints
                |             Point values x1,y1,z1 , x2,y2,z2, .... iPlaneDef coordinates
                |
                |     Returns:
                |         oCreatedWalk newly created WalkActivity
                |
                |     Example:
                | 
                |              This example creates WalkForward Activity on Plane
                |
                |         ' From the ProductList get the Walk Plane product
                |         Dim oPPRDoc As PPRDocument
                |         Dim pprprodsProdList As PPRProducts
                |         Set oPPRDoc = DELMIA.ActiveDocument.PPRDocument
                |         Set pprprodsProdList = oPPRDoc.Products
                |         Dim oPlaneProd As Product
                |         Set oPlaneProd = pprprodsProdList.Item(2)
                | 
                |         ' Plane Definition.. w.r.to Product
                | 
                |         Dim iPlaneDef(9) as Double
                |         iPlaneDef(0) = 1.0         ' First Axis  - i vec
                |         iPlaneDef(1) = 0.0         ' First Axis  - j vec
                |         iPlaneDef(2) = 0.0         ' First Axis  - k vec
                |         iPlaneDef(3) = 0.0         ' Second Axis - i vec
                |         iPlaneDef(4) = 1.0         ' Second Axis - j vec
                |         iPlaneDef(5) = 0.0         ' Second Axis - k vec
                |         iPlaneDef(6) = 0.0         ' Origin      - X
                |         iPlaneDef(7) = 0.0         ' Origin      - Y
                |         iPlaneDef(8) = 0.0         ' Origin      - Z
                | 
                |         ' Specify the number of coplanar points defining the walk
                |         path
                |         Dim iNumPoints as Long
                |         iNumPoints = 2
                | 
                |         ' Specify the point values for the walk path in oArrArea
                |         co-ordinates
                |         Dim iPoints(6) as Double
                |         iPoints(0) = 0.0         ' Point1 - X
                |         iPoints(1) = 0.0         ' Point1 - Y
                |         iPoints(2) = 0.0         ' Point1 - Z
                |         iPoints(3) = 2000.0      ' Point2 - X
                |         iPoints(4) = 0.0         ' Point2 - Y
                |         iPoints(5) = 0.0         ' Point2 - Z
                | 
                |            ' Get the Human Acts factory
                |         Dim oHumActsFactory As HumanActsFactory
                |            Dim oHumanTask As HumanTask
                |            Dim iPrevAct As Activity
                |         Dim oCreatedWalk as WalkActivity
                |            ....
                |            ....
                |            Set oHumActsFactory = oHumanTask.GetTechnologicalObject("HumanActsFactory")
                | 
                |            ' Create WalkForward Activity on Plane
                |            Set oCreatedWalk = oHumActsFactory.CreateWalkFwdOnPlane(iPrevAct, iPlaneProd, iPlaneDef, iNumPoints, iPoints) 
                |         ' Generate constituting MTPs
                |         oCreatedWalk.Update 
                |            ....
                |            ....

        :param Activity i_prev_act:
        :param Product i_prod:
        :param tuple i_plane_def:
        :param int i_num_points:
        :param tuple i_points:
        :rtype: WalkActivity
        """
        return WalkActivity(
            self.human_acts_factory.CreateWalkFwdOnPlane(
                i_prev_act.com_object,
                i_prod.com_object,
                i_plane_def,
                i_num_points,
                i_points
            )
        )

    def __repr__(self):
        return f'HumanActsFactory(name="{self.name}")'
