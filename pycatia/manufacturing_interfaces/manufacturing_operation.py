#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.knowledge_interfaces.parameter import Parameter
from pycatia.manufacturing_interfaces.manufacturing_activity import ManufacturingActivity
from pycatia.manufacturing_interfaces.manufacturing_feature import ManufacturingFeature
from pycatia.manufacturing_interfaces.manufacturing_tool_motion import ManufacturingToolMotion
from pycatia.manufacturing_interfaces.manufacturing_tool_motions import MFGToolMotions
from pycatia.product_structure_interfaces.product import Product
from pycatia.system_interfaces.any_object import AnyObject


class ManufacturingOperation(ManufacturingActivity):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     DMAPSInterfaces.Activity
                |                        ManufacturingInterfaces.ManufacturingActivity
                |                             ManufacturingOperation
                | 
                | ManufacturingOperation defines a set of methods.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.manufacturing_operation = com_object

    @property
    def comment(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Comment() As CATBSTR
                | 
                |     Return the Comment linked to a Manufacturing Operation.
                | 
                |     Example:
                |         The following example returns the Comment ThisComment linked to a
                |         manufacturing operation CurrentMo
                | 
                |          Set ThisComment = CurrentMo.Comment

        :rtype: str
        """

        return self.manufacturing_operation.Comment

    @comment.setter
    def comment(self, value: str):
        """
        :param str value:
        """

        self.manufacturing_operation.Comment = value

    def add_clearance(self, i_type_macro: str, i_a: float, i_b: float, i_c: float, i_d: float) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub AddClearance(CATBSTR iTypeMacro,
                | double iA,
                | double iB,
                | double iC,
                | double iD)
                | 
                |     Add a 'clearance to a plane' path to a Manufacturing
                |     Operation.
                | 
                |     Example:
                |         The following example add a path (clerarance) on approach macro of
                |         operation
                | 
                |          call Operation.AddClearance("Approach", A, B, C, D)

        :param str i_type_macro:
        :param float i_a:
        :param float i_b:
        :param float i_c:
        :param float i_d:
        :rtype: None
        """
        return self.manufacturing_operation.AddClearance(i_type_macro, i_a, i_b, i_c, i_d)

    def add_distance_along_aline_motion(
            self,
            i_type: str,
            i_distance: float,
            i_line: AnyObject,
            i_product: Product
    ) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub AddDistanceAlongAlineMotion(CATBSTR iType,
                | double iDistance,
                | AnyObject iLine,
                | Product iProduct)
                | 
                |     Add a path 'distance along a line' to a Manufacturing
                |     Operation.
                | 
                |     Example:
                |         The following example add a path (distance along a line) on the
                |         approach group of path of the Linking macro of
                |         operation
                | 
                |          call Operation.AddDistanceAlongAlineMotion("LinkingApproach",
                |          distance, iLine, iProduct)

        :param str i_type:
        :param float i_distance:
        :param AnyObject i_line:
        :param Product i_product:
        :rtype: None
        """
        return self.manufacturing_operation.AddDistanceAlongAlineMotion(
            i_type,
            i_distance,
            i_line.com_object,
            i_product.com_object
        )
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'add_distance_along_aline_motion'
        # # vba_code = """
        # # Public Function add_distance_along_aline_motion(manufacturing_operation)
        # #     Dim iType (2)
        # #     manufacturing_operation.AddDistanceAlongAlineMotion iType
        # #     add_distance_along_aline_motion = iType
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def add_distance_along_aline_motion_feed(
            self,
            i_type: str,
            i_distance: float,
            i_line: AnyObject,
            i_product: Product,
            i_feedrate_type: str,
            i_feedrate_value: float
    ) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub AddDistanceAlongAlineMotionFeed(CATBSTR iType,
                | double iDistance,
                | AnyObject iLine,
                | Product iProduct,
                | CATBSTR iFeedrateType,
                | double iFeedrateValue)
                | 
                |     Add a path 'distance along a line' with Feedrate info to a Manufacturing
                |     Operation.
                | 
                |     Parameters:
                | 
                |         iFeedrateType
                |             Legal values: iFeedrateType can be
                | 
                |             "None"
                |             "Machining"
                |             "Approach"
                |             "Retract"
                |             "RAPID"
                |             "Local"
                | 
                |         iFeedrateValue
                |             feedrate Value in MKS units : m/s if linear feedrate, or m/turn if angular feedrate (take into account only if iFeedrateType = "Local") 
                | 
                |     Example:
                |         The following example add a path (distance along a line) on the
                |         approach group of path of the Linking macro of
                |         operation
                | 
                |          call Operation.AddDistanceAlongAlineMotionFeed("LinkingApproach",
                |          distance, iLine, iProduct, iFeedrateType,
                |          iFeedrateValue)

        :param str i_type:
        :param float i_distance:
        :param AnyObject i_line:
        :param Product i_product:
        :param str i_feedrate_type:
        :param float i_feedrate_value:
        :rtype: None
        """
        return self.manufacturing_operation.AddDistanceAlongAlineMotionFeed(
            i_type,
            i_distance,
            i_line.com_object,
            i_product.com_object,
            i_feedrate_type,
            i_feedrate_value
        )
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'add_distance_along_aline_motion_feed'
        # # vba_code = """
        # # Public Function add_distance_along_aline_motion_feed(manufacturing_operation)
        # #     Dim iType (2)
        # #     manufacturing_operation.AddDistanceAlongAlineMotionFeed iType
        # #     add_distance_along_aline_motion_feed = iType
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def add_distance_along_axis(self, i_type: str, i_distance: float) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub AddDistanceAlongAxis(CATBSTR iType,
                | double iDistance)
                | 
                |     Add a path 'distance along axis' to a Manufacturing
                |     Operation.
                | 
                |     Example:
                |         The following example add a path (distance along axis) on the approach
                |         group of path of the Linking macro of operation
                | 
                |          call Operation.AddDistanceAlongAxis("LinkingApproach",
                |          distance)

        :param str i_type:
        :param float i_distance:
        :rtype: None
        """
        return self.manufacturing_operation.AddDistanceAlongAxis(i_type, i_distance)

    def add_distance_along_axis_feed(
            self,
            i_type: str,
            i_distance: float,
            i_feedrate_type: str,
            i_feedrate_value: float
    ) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub AddDistanceAlongAxisFeed(CATBSTR iType,
                | double iDistance,
                | CATBSTR iFeedrateType,
                | double iFeedrateValue)
                | 
                |     Add a path 'distance along axis' with Feedrate info to a Manufacturing
                |     Operation.
                | 
                |     Parameters:
                | 
                |         iFeedrateType
                |             Legal values: iFeedrateType can be
                | 
                |             "None"
                |             "Machining"
                |             "Approach"
                |             "Retract"
                |             "RAPID"
                |             "Local"
                | 
                |         iFeedrateValue
                |             feedrate Value in MKS units : m/s if linear feedrate, or m/turn if
                |             angular feedrate (take into account only if iFeedrateType = "Local")
                | 
                |     Example:
                |         The following example add a path (distance along axis) on the approach
                |         group of path of the Linking macro of operation
                | 
                |          call Operation.AddDistanceAlongAxisFeed("LinkingApproach", distance,
                |          iFeedrateType, iFeedrateValue)

        :param str i_type:
        :param float i_distance:
        :param str i_feedrate_type:
        :param float i_feedrate_value:
        :rtype: None
        """
        return self.manufacturing_operation.AddDistanceAlongAxisFeed(
            i_type,
            i_distance,
            i_feedrate_type,
            i_feedrate_value
        )

    def add_goto_horizontal(self, i_type_macro: str, i_distance: float, i_angle1: float, i_angle2: float) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub AddGotoHorizontal(CATBSTR iTypeMacro,
                | double iDistance,
                | double iAngle1,
                | double iAngle2)
                | 
                |     Add a path 'goto horizontal' to a Manufacturing Operation.
                | 
                |     Example:
                |         The following example add a path (goto horizontal) on approach macro of
                |         operation
                | 
                |          call Operation.AddGotoHorizontal("Approach", distance, angle1,
                |          angle2)

        :param str i_type_macro:
        :param float i_distance:
        :param float i_angle1:
        :param float i_angle2:
        :rtype: None
        """
        return self.manufacturing_operation.AddGotoHorizontal(i_type_macro, i_distance, i_angle1, i_angle2)

    def add_motion_go_to_a_point(self, i_type_macro: str, i_point: AnyObject, i_product: Product) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub AddMotionGoToAPoint(CATBSTR iTypeMacro,
                | AnyObject iPoint,
                | Product iProduct)
                | 
                |     Add a path 'goto a point' to a Manufacturing Operation.
                | 
                |     Example:
                |         The following example add a path (goto a point ) on approach macro of
                |         operation
                | 
                |          call Operation.AddMotionGoToAPoint("Approach", iPoint, iProduct
                |          )

        :param str i_type_macro:
        :param AnyObject i_point:
        :param Product i_product:
        :rtype: None
        """
        return self.manufacturing_operation.AddMotionGoToAPoint(i_type_macro, i_point.com_object, i_product.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'add_motion_go_to_a_point'
        # # vba_code = """
        # # Public Function add_motion_go_to_a_point(manufacturing_operation)
        # #     Dim iTypeMacro (2)
        # #     manufacturing_operation.AddMotionGoToAPoint iTypeMacro
        # #     add_motion_go_to_a_point = iTypeMacro
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def add_motion_go_to_a_point_feed(
            self,
            i_type_macro: str,
            i_point: AnyObject,
            i_product: Product,
            i_feedrate_type: str,
            i_feedrate_value: float
    ) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub AddMotionGoToAPointFeed(CATBSTR iTypeMacro,
                | AnyObject iPoint,
                | Product iProduct,
                | CATBSTR iFeedrateType,
                | double iFeedrateValue)
                | 
                |     Add a path 'goto a point' with Feedrate info to a Manufacturing
                |     Operation.
                | 
                |     Parameters:
                | 
                |         iFeedrateType
                |             Legal values: iFeedrateType can be
                | 
                |             "None"
                |             "Machining"
                |             "Approach"
                |             "Retract"
                |             "RAPID"
                |             "Local"
                | 
                |         iFeedrateValue
                |             feedrate Value in MKS units : m/s if linear feedrate, or m/turn if
                |             angular feedrate (take into account only if iFeedrateType = "Local")
                | 
                |     Example:
                |         The following example add a path (goto a point ) on approach macro of
                |         operation
                | 
                |          call Operation.AddMotionGoToAPointFeed("Approach", iPoint, iProduct,
                |          iFeedrateType, iFeedrateValue)

        :param str i_type_macro:
        :param AnyObject i_point:
        :param Product i_product:
        :param str i_feedrate_type:
        :param float i_feedrate_value:
        :rtype: None
        """
        return self.manufacturing_operation.AddMotionGoToAPointFeed(
            i_type_macro,
            i_point.com_object,
            i_product.com_object,
            i_feedrate_type,
            i_feedrate_value
        )
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'add_motion_go_to_a_point_feed'
        # # vba_code = """
        # # Public Function add_motion_go_to_a_point_feed(manufacturing_operation)
        # #     Dim iTypeMacro (2)
        # #     manufacturing_operation.AddMotionGoToAPointFeed iTypeMacro
        # #     add_motion_go_to_a_point_feed = iTypeMacro
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def add_motion_to_a_plane(self, i_type_macro: str, i_mode: int, i_plane: AnyObject, i_product: Product) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub AddMotionToAPlane(CATBSTR iTypeMacro,
                | short iMode,
                | AnyObject iPlane,
                | Product iProduct)
                | 
                |     Add a path 'goto a plane with axial or perpendicular move' to a
                |     Manufacturing Operation.
                | 
                |     Example:
                |         The following example add a path (goto a plane with axial move ) on
                |         approach macro of operation
                | 
                |          call Operation.AddMotionToAPlane("Approach", 1, iPlane,
                |          iProduct)
                | 
                |     Example:
                |         The following example add a path (goto a plane with perpendicular move
                |         ) on approach macro of operation
                | 
                |          call Operation.AddMotionToAPlane("Approach", 0, iPlane,
                |          iProduct)

        :param str i_type_macro:
        :param int i_mode:
        :param AnyObject i_plane:
        :param Product i_product:
        :rtype: None
        """
        return self.manufacturing_operation.AddMotionToAPlane(
            i_type_macro,
            i_mode,
            i_plane.com_object,
            i_product.com_object
        )
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'add_motion_to_a_plane'
        # # vba_code = """
        # # Public Function add_motion_to_a_plane(manufacturing_operation)
        # #     Dim iTypeMacro (2)
        # #     manufacturing_operation.AddMotionToAPlane iTypeMacro
        # #     add_motion_to_a_plane = iTypeMacro
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def add_pp_words(self, i_type_macro: str, i_pp_words: str) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub AddPPWords(CATBSTR iTypeMacro,
                | CATBSTR iPPWords)
                | 
                |     Add a path 'PP Words' to a Manufacturing Operation.
                | 
                |     Example:
                |         The following example add a path (PP Words) on the retract group of
                |         path of the Linking macro of operation
                | 
                |          call Operation.AddPPWords("LinkingRetract", "PP Words
                |          example")

        :param str i_type_macro:
        :param str i_pp_words:
        :rtype: None
        """
        return self.manufacturing_operation.AddPPWords(i_type_macro, i_pp_words)

    def get_a_geometric_attribute(self, i_attribute: str) -> Parameter:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetAGeometricAttribute(CATBSTR iAttribut) As
                | Parameter
                | 
                |     Retrieve a Geometric Attribute of a Manufacturing
                |     Operation.
                | 
                |     Example:
                |         The following example retrieves in Offset the attribute OriginOffset of
                |         Manufacturing Operation firstOperation
                | 
                |          Set Offset = firstOperation.GetAttribute(OriginOffset)

        :param str i_attribute:
        :rtype: Parameter
        """
        return Parameter(self.manufacturing_operation.GetAGeometricAttribute(i_attribute))

    def get_an_attribute(self, i_attribute: str) -> Parameter:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetAnAttribute(CATBSTR iAttribut) As Parameter
                | 
                |     Retrieve the Attribute of a Manufacturing Operation.
                | 
                |     Example:
                |         The following example Retrieves in RapidFeed the attribute MfgRapidFeed
                |         of Manufacturing Operation firstOperation
                | 
                |          Set RapidFeed = firstOperation.GetAttribute(MfgRapidFeed)

        :param str i_attribute:
        :rtype: Parameter
        """
        return Parameter(self.manufacturing_operation.GetAnAttribute(i_attribute))

    def get_feature(self) -> AnyObject:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetFeature() As AnyObject
                | 
                |     Retrieve the Machinable Feature asociated to a Manufacturing
                |     Operation.
                | 
                |     Example:
                |         The following example Retrieves in firstOperation the machinable
                |         feature Feature
                | 
                |          call firstOperation.GetFeature(Feature)

        :rtype: AnyObject
        """
        return AnyObject(self.manufacturing_operation.GetFeature())

    def get_feed_speed_auto_update(self, i_type: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetFeedSpeedAutoUpdate(CATBSTR iType) As boolean
                | 
                |     Returns the Auto Update status for Feed Rate or Spindle
                |     Speed.
                | 
                |     Parameters:
                | 
                |         iType
                |             Determines if the method works on Feed Rate or Spindle Speed Legal
                |             values: iType can be
                | 
                |                 "FEEDRATE"
                |                 "SPINDLESPEED"
                | 
                |     Returns:
                |         oAutoUpdate Auto update status
                | 
                |             Example:
                |             The following example checks the status of AutoUpdate for Feed
                |             Rate
                |             Dim isAutoUpdateEnabled As Boolean
                |             isAutoUpdateEnabled = firstOperation.GetFeedSpeedAutoUpdate("FEEDRATE")

        :param str i_type:
        :rtype: bool
        """
        return self.manufacturing_operation.GetFeedSpeedAutoUpdate(i_type)

    def get_list_of_tool_motions(self) -> MFGToolMotions:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetListOfToolMotions() As MfgToolMotions
                | 
                |     Give a list of Manufacturing ToolMotion contained by a sequential
                |     operation.
                | 
                |     See interface CATIAMfgToolMotions for methods available on the
                |     list
                |         The following example extract the tool motions of operation SeqMO in
                |         the MfgToolMotions 
                |         list TMList2 .
                | 
                |          
                |         Example:
                |         Dim TMList2 As MfgToolMotions
                |         Set TMList2 = SeqMO.GetListOfToolMotions
                |         Dim Test2 As ManufacturingToolMotion
                |         Set Test2 = TMList2.GetElement(1)

        :return: MfgToolMotions
        :rtype: MFGToolMotions
        """
        return MFGToolMotions(self.manufacturing_operation.GetListOfToolMotions())

    def get_manufacturing_feature(self) -> ManufacturingFeature:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetManufacturingFeature() As ManufacturingFeature
                | 
                |     Retrieve the Manufacturing Feature asociated to a Manufacturing
                |     Operation.
                | 
                |     Example:
                |         The following example Retrieves in firstOperation the manufacturing
                |         feature Feature
                | 
                |          Set Feature = firstOperation.GetManufacturingFeature

        :rtype: ManufacturingFeature
        """
        return ManufacturingFeature(self.manufacturing_operation.GetManufacturingFeature())

    def get_mfg_aparam_top_pln(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetMfgAparamTopPln() As double
                | 
                |     Retrieve the Equation of the Top Plane of a Pocket
                |     Operation.
                | 
                |     Example:
                |         The following example Retrieves in A,B,C,D the equation Ax + By + Cz + D = 0
                |         of Manufacturing Pocket Operation firstOperation
                | 
                |          Dim A
                |          Set A = firstOperation.GetMfgBparamTopPln

        :rtype: float
        """
        return self.manufacturing_operation.GetMfgAparamTopPln()

    def get_mfg_axial_feature_diameter(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetMfgAxialFeatureDiameter() As double
                | 
                |     Retrieve the diameter of an axial manufacturing feature.
                | 
                |     Example:
                |         The following example Retrieves in Diam the diameter of the axial
                |         manufacturing feature linked to the operation
                |         firstOperation
                | 
                |          Dim Diam 
                |          Set Diam = firstOperation.GetMfgAxialFeatureDiameter

        :rtype: float
        """
        return self.manufacturing_operation.GetMfgAxialFeatureDiameter()

    def get_mfg_bparam_top_pln(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetMfgBparamTopPln() As double
                | 
                |     Retrieve the Equation of the Top Plane of a Pocket
                |     Operation.
                | 
                |     Example:
                |         The following example Retrieves in A,B,C,D the equation Ax + By + Cz + D = 0
                |         of Manufacturing Pocket Operation firstOperation
                | 
                |          Dim B
                |          Set B = firstOperation.GetMfgBparamTopPln

        :rtype: float
        """
        return self.manufacturing_operation.GetMfgBparamTopPln()

    def get_mfg_cparam_top_pln(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetMfgCparamTopPln() As double
                | 
                |     Retrieve the Equation of the Top Plane of a Pocket
                |     Operation.
                | 
                |     Example:
                |         The following example Retrieves in A,B,C,D the equation Ax + By + Cz + D = 0
                |         of Manufacturing Pocket Operation firstOperation
                | 
                |          Dim C
                |          Set C = firstOperation.GetMfgCparamTopPln

        :rtype: float
        """
        return self.manufacturing_operation.GetMfgCparamTopPln()

    def get_mfg_dparam_top_pln(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetMfgDparamTopPln() As double
                | 
                |     Retrieve the Equation of the Top Plane of a Pocket
                |     Operation.
                | 
                |     Example:
                |         The following example Retrieves in A,B,C,D the equation Ax + By + Cz + D = 0
                |         of Manufacturing Pocket Operation firstOperation
                | 
                |          Dim D
                |          Set D = firstOperation.GetMfgDparamTopPln

        :rtype: float
        """
        return self.manufacturing_operation.GetMfgDparamTopPln()

    def get_mfg_feature_position(self, io_position: tuple) -> tuple:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetMfgFeaturePosition(CATSafeArrayVariant ioPosition)
                | 
                |     Retrieve the Coordinate of the Reference Point of a Drill
                |     Operation.
                | 
                |     Example:
                |         The following example Retrieves in X,Y,Z the coordinate (X,Y,Z) of the
                |         Reference Point of the Drill Operation firstOperation
                | 
                |          Dim oPositionArray(3) As CATSafeArrayVariant
                |          Call
                |          firstOperation.GetMfgFeaturePosition(oPositionArray)
                |          Assume this array is oPositionArray. It contains: 
                |
                |         oPositionArray[0],oPositionArray[1],oPositionArray[2]
                |          
                |             The X, Y, and Z direction vector components
                |
                |         Example:
                |          
                |             The following example returns in oPositionArray
                |              the coordinates of the feature position
                |
                |              Call firstOperation.GetMfgFeaturePosition(oCoord)
                |              x = oPositionArray[0]
                |              y = oPositionArray[1]
                |              z = oPositionArray[2]

        :param tuple io_position:
        :rtype: tuple
        """
        return self.manufacturing_operation.GetMfgFeaturePosition(io_position)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_mfg_feature_position'
        # # vba_code = """
        # # Public Function get_mfg_feature_position(manufacturing_operation)
        # #     Dim ioPosition (2)
        # #     manufacturing_operation.GetMfgFeaturePosition ioPosition
        # #     get_mfg_feature_position = ioPosition
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_mfg_feature_x_position(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetMfgFeatureXPosition() As double
                | 
                |     Retrieve the Coordinate of the Reference Point of a Drill
                |     Operation.
                | 
                |     Example:
                |         The following example Retrieves in X,Y,Z the coordinate (X,Y,Z) of the
                |         Reference Point of the Drill Operation firstOperation
                | 
                |          Dim X
                |          X = firstOperation.GetMfgFeatureXPosition

        :rtype: float
        """
        return self.manufacturing_operation.GetMfgFeatureXPosition()

    def get_mfg_feature_y_position(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetMfgFeatureYPosition() As double
                | 
                |     Retrieve the Coordinate of the Reference Point of a Drill
                |     Operation.
                | 
                |     Example:
                |         The following example Retrieves in X,Y,Z the coordinate (X,Y,Z) of the
                |         Reference Point of the Drill Operation firstOperation
                | 
                |          Dim Y
                |          Y = firstOperation.GetMfgFeatureYPosition

        :rtype: float
        """
        return self.manufacturing_operation.GetMfgFeatureYPosition()

    def get_mfg_feature_z_position(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetMfgFeatureZPosition() As double
                | 
                |     Retrieve the Coordinate of the Reference Point of a Drill
                |     Operation.
                | 
                |     Example:
                |         The following example Retrieves in X,Y,Z the coordinate (X,Y,Z) of the
                |         Reference Point of the Drill Operation firstOperation
                | 
                |          Dim Z
                |          Z = firstOperation.GetMfgFeatureZPosition

        :rtype: float
        """
        return self.manufacturing_operation.GetMfgFeatureZPosition()

    def get_mfg_top_plane(self, o_a: float, o_b: float, o_c: float, o_d: float) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetMfgTopPlane(double oA,
                | double oB,
                | double oC,
                | double oD)
                | 
                |     Retrieve the Equation of the Top Plane of a Pocket
                |     Operation.
                | 
                |     Example:
                |         The following example Retrieves in A,B,C,D the equation Ax + By + Cz + D = 0
                |         of Manufacturing Pocket Operation firstOperation
                | 
                |          Call firstOperation.GetMfgTopPlane(A,B,C,D)

        :param float o_a:
        :param float o_b:
        :param float o_c:
        :param float o_d:
        :rtype: None
        """
        return self.manufacturing_operation.GetMfgTopPlane(o_a, o_b, o_c, o_d)

    def get_pattern(self) -> AnyObject:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetPattern() As AnyObject
                | 
                |     Retrieve the Machining Pattern asociated to a Manufacturing
                |     Operation.
                | 
                |     Example:
                |         The following example Retrieves in firstOperation the machining pattern
                |         Pattern
                | 
                |          Set Pattern = firstOperation.GetPattern

        :rtype: AnyObject
        """
        return AnyObject(self.manufacturing_operation.GetPattern())

    def get_radius_on_macro(self, i_macro_type: str) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetRadiusOnMacro(CATBSTR iMacroType) As double
                | 
                |     Retrieves radius attribute on the circular elementary macro motion on
                |     CIRCULAR MILLING or THREAD MILLING operations ONLY.
                | 
                |     Parameters:
                | 
                |         iMacroType
                |             Legal values: iMacroType can be:
                | 
                |             "Approach", to get the radius on the Approach
                |             Macro
                |             "Retract", to get the radius on the Retract Macro
                |             "ReturnInALevelApproach", to get the radius on the Return in a
                |             level Macro (Approach)
                |             "ReturnInALevelRetract", to get the radius on the Return in a level
                |             Macro (Retract)
                |             "ReturnBetweenLevelsApproach", to get the radius on the Return
                |             between levels Macro (Approach)
                |             "ReturnBetweenLevelsRetract", to get the radius on the Return
                |             between levels Macro (Approach)
                | 
                |         oRadius
                |             Radius value. (expressed in millimeters) 
                | 
                |     Example:
                |         The following example retrieves the radius on the circular motion of
                |         the retract macro on the Circular Milling operation
                |         CircularMilling1
                | 
                |          dim RadValue as double
                |          RadValue = CircularMilling1.GetRadiusOnMacro("Retract")

        :param str i_macro_type:
        :rtype: float
        """
        return self.manufacturing_operation.GetRadiusOnMacro(i_macro_type)

    def get_relimiting_geometry(
            self,
            i_geometry_type: str,
            o_reference: AnyObject,
            o_product: AnyObject,
            o_offset: float,
            o_position: str
    ) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetRelimitingGeometry(CATBSTR iGeometryType,
                | AnyObject oReference,
                | AnyObject oProduct,
                | double oOffset,
                | CATBSTR oPosition)
                | 
                |     Retrieves start / end element on PROFILE CONTOURING operation
                |     ONLY.
                | 
                |     Parameters:
                | 
                |         iGeometryType
                |             Legal values: iGeometryType can be:
                | 
                |             "StartElement", to get the Start element on Profile
                |             Contouring
                |             "EndElement", to get the End element on Profile
                |             Contouring
                | 
                |         oReference
                |             The relimiting geometry. 
                |         oProduct
                |             Product containing the relimiting geometry. 
                |         oOffset
                |             Offset set on the relimiting geometry. (expressed in millimeters)
                |             
                |         oPosition
                |             Tool position set on the relimiting geometry.
                |             Legal values: oPosition can be:
                | 
                |             "IN"
                |             "ON"
                |             "OUT"
                | 
                |     Example:
                |         The following example gets the End relimiting element of the Profile
                |         Contouring operation Contouring1
                | 
                |          Call Contouring1.GetRelimitingGeometry("EndElement",RelimitingElement,PartMachined,Offset,Position)

        :param str i_geometry_type:
        :param AnyObject o_reference:
        :param AnyObject o_product:
        :param float o_offset:
        :param str o_position:
        :rtype: None
        """
        return self.manufacturing_operation.GetRelimitingGeometry(
            i_geometry_type,
            o_reference.com_object,
            o_product.com_object,
            o_offset,
            o_position
        )

    def get_start_point_geometry(
            self,
            o_geometry_position: str,
            o_reference: AnyObject,
            o_product: AnyObject,
            o_offset: float
    ) -> tuple:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetStartPointGeometry(CATBSTR oGeometryPosition,
                | AnyObject oReference,
                | AnyObject oProduct,
                | double oOffset)
                | 
                |     Retrieves geometry and offset of a start point on POCKETING operation
                |     ONLY.
                | 
                |     Parameters:
                | 
                |         oGeometryPosition
                |             Legal values: oGeometryPosition can be:
                | 
                |             "Outside", if the start point is outside the pocket
                |             contour
                |             "Inside", if the start point is inside the pocket
                |             contour
                | 
                |         oReference
                |             The start point geometry. 
                |         oProduct
                |             Product containing the start point geometry. 
                |         oOffset
                |             Offset set on the start point. (expressed in
                |             millimeters)
                |             Offset has a meaning only if oGeometryPosition value is "Outside".
                |
                |     Example:
                |         The following example gets the Start point geometry on the Pocketing
                |         operation Pocketing1
                | 
                |          Call Pocketing1.GetStartPointGeometry(Position,Point1,Part,OffsetValue)

        :param str o_geometry_position:
        :param AnyObject o_reference:
        :param AnyObject o_product:
        :param float o_offset:
        :rtype: tuple
        """
        return self.manufacturing_operation.GetStartPointGeometry(
            o_geometry_position,
            o_reference.com_object,
            o_product.com_object,
            o_offset
        )

    def get_tool_gauge(self, o_min_tool_length: float, o_min_tool_gage: float) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetToolGage(double oMinToolLength,
                | double oMinToolGage)
                | 
                |     Retrieves the minimum tool cutting lentgh and the minimum tool gage
                |     length.
                | 
                |     Example:
                |         The following example Retrieves in MinToolLength and MinToolGage the
                |         values of tool of Manufacturing Operation Operation
                | 
                |          Call Operation.GetToolGage(MinToolLength,MinToolGage)

        :param float o_min_tool_length:
        :param float o_min_tool_gage:
        :rtype: None
        """
        return self.manufacturing_operation.GetToolGage(o_min_tool_length, o_min_tool_gage)

    def get_trajectory_end_point_coord(self) -> tuple:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetTrajectoryEndPointCoord(CATSafeArrayVariant
                | oEndPoint)
                | 
                |     Retrieve the Machining Operation's trajectory end point.
                | 
                |     Example:
                |         The following example Retrieves in oEndPoint the end point of the
                |         Machining Operation Operation
                | 
                |          Dim oEndPoint(2)
                |          call Operation.GetTrajectoryEndPointCoord(oEndPoint)
                |          x = oEndPoint(0)
                |          y = oEndPoint(1)
                |          z = oEndPoint(2)

        :rtype: tuple
        """
        return self.manufacturing_operation.GetTrajectoryEndPointCoord()
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_trajectory_end_point_coord'
        # # vba_code = """
        # # Public Function get_trajectory_end_point_coord(manufacturing_operation)
        # #     Dim oEndPoint (2)
        # #     manufacturing_operation.GetTrajectoryEndPointCoord oEndPoint
        # #     get_trajectory_end_point_coord = oEndPoint
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_trajectory_start_point_coord(self) -> tuple:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetTrajectoryStartPointCoord(CATSafeArrayVariant
                | oStartPoint)
                | 
                |     Retrieve the Machining Operation's trajectory start point.
                | 
                |     Example:
                |         The following example Retrieves in oStartPoint the start point of the
                |         Machining Operation Operation
                | 
                |          Dim oEndPoint(2)
                |          call
                |          Operation.GetTrajectoryStartPointCoord(oStartPoint)
                |          x = oStartPoint(0)
                |          y = oStartPoint(1)
                |          z = oStartPoint(2)

        :rtype: tuple
        """
        return self.manufacturing_operation.GetTrajectoryStartPointCoord()
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_trajectory_start_point_coord'
        # # vba_code = """
        # # Public Function get_trajectory_start_point_coord(manufacturing_operation)
        # #     Dim oStartPoint (2)
        # #     manufacturing_operation.GetTrajectoryStartPointCoord oStartPoint
        # #     get_trajectory_start_point_coord = oStartPoint
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def import_nc_output(self, i_type: str, i_nc_output_file: str, i_pp_name: str) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub ImportNCOutput(CATBSTR iType,
                | CATBSTR iNCOutputFile,
                | CATBSTR iPPName)
                | 
                |     Import an NC File.
                | 
                |     Example:
                |         The following example imports after an operation Operation an NC File
                |         of type TYPE available in the file path PATH using the PP PPNAME if
                |         required.
                | 
                |          Call
                |          Operation.ImportNCOutputOnProgram(TYPE,PATH,PPNAME)

        :param str i_type:
        :param str i_nc_output_file:
        :param str i_pp_name:
        :rtype: None
        """
        return self.manufacturing_operation.ImportNCOutput(i_type, i_nc_output_file, i_pp_name)

    def insert_tool_motion(self, i_type: str, i_position: int) -> ManufacturingToolMotion:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func InsertToolMotion(CATBSTR iType,
                | short iPosition) As ManufacturingToolMotion
                | 
                |     Create, given its type, a Manufacturing ToolMotion inside a sequential
                |     operation.
                | 
                |         The available type for lathe sequential operation are : 
                |         for GoStandard and GoGo tool motion iType = MfgSeqMotionLatheGoStd 
                |         for GoDelta tool motion, iType = MfgSeqMotionLatheDelta 
                |         for Indirv tool motion, iType = MfgSeqMotionLatheIndirv 
                |         for Follow tool motion, iType = MfgSeqMotionLatheFollow 
                |         for PPWord tool motion, iType = MfgSeqMotionPPWord 
                |         The available type for prismatic sequential operation are : 
                |         for Goto Point tool motion, iType = MfgSeqMotionPoint 
                |         for Goto Position tool motion, iType = MfgSeqMotionPosition 
                |         for Goto Delta tool motion, iType = MfgSeqMotionDelta 
                |         iType type of the ToolMotion to be created iPosition rank in the
                |         operation list where the ToolMotion will be created 
                |         iPosition=0 means creation at the end of the list of tool motions
                |         oToolMotion the created ManufacturingToolMotion 
                |         The following example creates in ManufacturingOperation SeqMO
                |         
                |         which is a Lathe Sequential operation 
                |         the ManufacturingToolMotion ThisToolMotion of type
                |         MfgSeqMotionLatheGoStd at the first rank
                | 
                |          
                |         Example:
                |         Set SeqMO = Program1.AppendOperation("MfgLatheMfgSequentialOperation",1)
                |         Set ThisToolMotion = SeqMO.InsertToolMotion("MfgSeqMotionLatheGoStd",1)
                | 
                |         The following example creates in ManufacturingOperation SeqMO
                |         
                |         which is an Axial Point to Point sequential operation 
                |         the ManufacturingToolMotion ThisToolMotion of type MfgSeqMotionPoint at
                |         the first rank
                | 
                |          
                |         Example:
                |         Set SeqMO = Program1.AppendOperation("PointToPoint",1)
                |         Set ThisToolMotion = SeqMO.InsertToolMotion("MfgSeqMotionPoint",1)

        :param str i_type:
        :param int i_position:
        :rtype: ManufacturingToolMotion
        """
        return ManufacturingToolMotion(self.manufacturing_operation.InsertToolMotion(i_type, i_position))

    def is_geometrically_accessible_on_setup(self, i_manufacturing_setup: AnyObject) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func IsGeometricallyAccessibleOnSetup(AnyObject iManufacturingSetup) As
                | boolean
                | 
                |     Returns True if the Manufacturing Axial Operation is geometrically
                |     accessible on the given Manufacturing Setup.The Axial Operation must have a
                |     valid tool axis and a machine must be assigned to the Manufacturing Setup. If
                |     this is not the case, the method returns False.
                | 
                |     Parameters:
                | 
                |         iSetup
                |             The Manufacturing Setup gives the accessibility checking context :
                |             the part,the machine and the relative orientation of the part on the machine.
                | 
                |             Example:
                |                 The following example checks the accessibility of
                |                 firstOperation on firstSetup.
                | 
                |                  Dim isAccessible As Boolean
                |                  isAccessible = firstOperation.IsGeometricallyAccessibleOnSetup(firstSetup)

        :param AnyObject i_manufacturing_setup:
        :rtype: bool
        """
        return self.manufacturing_operation.IsGeometricallyAccessibleOnSetup(i_manufacturing_setup.com_object)

    def lock_activity(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub LockActivty()
                | 
                |     Method is used for Locking and Unloking specific activity Call on
                |     ManufacturingOperation

        :rtype: None
        """
        return self.manufacturing_operation.LockActivty()

    def remove_relimiting_geometry(self, i_geometry_type: str) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub RemoveRelimitingGeometry(CATBSTR iGeometryType)
                | 
                |     Removes the geometry on relimiting element PROFILE CONTOURING operation
                |     ONLY.
                | 
                |     Parameters:
                | 
                |         iGeometryType
                |             Legal values: iGeometryType can be:
                | 
                |             "StartElement", to remove the Start element on Profile
                |             Contouring
                |             "EndElement", to remove the End element on Profile
                |             Contouring
                | 
                |     Example:
                |         The following example removes the End relimiting element of the Profile
                |         Contouring operation Contouring1
                | 
                |          Call
                |          Contouring1.RemoveRelimitingGeometry("EndElement")

        :param str i_geometry_type:
        :rtype: None
        """
        return self.manufacturing_operation.RemoveRelimitingGeometry(i_geometry_type)

    def remove_start_point_geometry(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub RemoveStartPointGeometry()
                | 
                |     Removes the start point element on POCKETING operation
                |     ONLY.
                | 
                |     Example:
                |         The following example removes the start point of the Pocketing
                |         operation Pocketing1
                | 
                |          Call Pocketing1.RemoveStartPointGeometry

        :rtype: None
        """
        return self.manufacturing_operation.RemoveStartPointGeometry()

    def set_feature(self, i_machinable_feature: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetFeature(AnyObject iMachinableFeature)
                | 
                |     Associate a Machinable Feature to a Manufacturing
                |     Operation.
                | 
                |     Example:
                |         The following example associates in firstOperation the machinable
                |         feature Feature
                | 
                |          call firstOperation.SetFeature(Feature)

        :param AnyObject i_machinable_feature:
        :rtype: None
        """
        return self.manufacturing_operation.SetFeature(i_machinable_feature.com_object)

    def set_feed_speed_auto_update(self, i_type: str, i_auto_update: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetFeedSpeedAutoUpdate(CATBSTR iType,
                | boolean iAutoUpdate)
                | 
                |     Set the Auto Update status for Feed Rate or Spindle Speed.
                | 
                |     Parameters:
                | 
                |         iType
                |             Determines if the method works on Feed Rate or Spindle Speed Legal
                |             values: iType can be
                | 
                |                 "FEEDRATE"
                |                 "SPINDLESPEED"
                | 
                |         iAutoUpdate
                |             Auto update status Legal values: iType can be
                | 
                |                 True
                |                 False
                | 
                |                     Example:
                |                     The following example enables AutoUpdate for Spindle
                |                     Speed
                |                     firstOperation.SetFeedSpeedAutoUpdate("SPINDLESPEED",
                |                     True)

        :param str i_type:
        :param bool i_auto_update:
        :rtype: None
        """
        return self.manufacturing_operation.SetFeedSpeedAutoUpdate(i_type, i_auto_update)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_feed_speed_auto_update'
        # # vba_code = """
        # # Public Function set_feed_speed_auto_update(manufacturing_operation)
        # #     Dim iType (2)
        # #     manufacturing_operation.SetFeedSpeedAutoUpdate iType
        # #     set_feed_speed_auto_update = iType
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_feedrate_magnitude(self, i_magnitude_name: str) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetFeedrateMagnitude(CATBSTR iMagnitudeName)
                | 
                |     Defines the magnitude of the feedrate values.
                | 
                |      
                | 
                |          
                |         The available types for Magnitude are: 
                |          
                |         for Linear Magnitude , iMagnitudeName = LINEARFEEDRATE
                |          
                |         for Angular Magnitude , iMagnitudeName = ANGULARFEEDRATE
                |          
                |     Example:
                |      Dim Operation1 As ManufacturingOperation
                |      Set Operation1 = Program1.AppendOperation ("Drilling",1)
                |      Operation1.SetFeedrateMagnitude("LINEARFEEDRATE")

        :param str i_magnitude_name:
        :rtype: None
        """
        return self.manufacturing_operation.SetFeedrateMagnitude(i_magnitude_name)

    def set_geometry(self, i_geometry_type: str, i_reference: AnyObject, i_product: AnyObject, i_position: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetGeometry(CATBSTR iGeometryType,
                | AnyObject iReference,
                | AnyObject iProduct,
                | short iPosition)
                | 
                |     Assigns geometry to a Manufacturing Operation.
                | 
                |     Parameters:
                | 
                |         iGeometryType
                |             Type of geometry to assign List of valid iGeometryType: - Parts -
                |             Drives - RoughStock - PartBottom - Checks - GuidingCurves - FirstGuideLine -
                |             SecondGuideLine - AuxGuidingCurves - RelimitingFace - RelimitingPlane -
                |             FirstRelimitingElement - SecondRelimitingElement - EndingPoint - StartingPoint
                |             - Island - SetupStocks - SetupDesigns 
                |         iReference
                |             Geometry to assign: it may be a feature (point, hole, ...) or a
                |             BREP feature. 
                |         iProduct
                |             Product containing the geometry to assign. It must be the occurence
                |             of the product which owns the part containing the geometry. Also see method
                |             GetProductInstance of CATIAManufacturingSetup interface.
                |             
                |         iPosition
                |             Position of the geometry in the list (0 to append at the end of the
                |             list). 
                |         Example:
                |             The following example assigns the plane Plane.1 as bottom of
                |             operation Pocketing1 of the Manufacturing Program Program1. The Product
                |             Product1 is associated to Manufacturing Setup Setup1. This example is valid
                |             only if the Product owning the part which contains the plane has been
                |             associated to the Manufacturing Setup (if the CATPart containing the plane has
                |             been associated to the Manufacturing Setup). In other cases, the product must
                |             be retrieved differently.
                | 
                |              Set Product1 = Setup1.GetProductInstance()
                |              Dim Pocketing1 As ManufacturingOperation
                |              Set Pocketing1 = Program1.AppendOperation ("Pocketing",1)
                |              Pocketing1
                |              .SetGeometry("PartBottom",Plane1,Product1,0)

        :param str i_geometry_type:
        :param AnyObject i_reference:
        :param AnyObject i_product:
        :param int i_position:
        :rtype: None
        """
        return self.manufacturing_operation.SetGeometry(
            i_geometry_type,
            i_reference.com_object,
            i_product.com_object,
            i_position
        )

    def set_pattern(self, i_pattern: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetPattern(AnyObject iPattern)
                | 
                |     Associate a Machining Pattern to a Manufacturing
                |     Operation.
                | 
                |     Example:
                |         The following example associates in firstOperation the machining
                |         pattern Pattern
                | 
                |          call firstOperation.SetPattern(Pattern)

        :param AnyObject i_pattern:
        :rtype: None
        """
        return self.manufacturing_operation.SetPattern(i_pattern.com_object)

    def set_radius_on_macro(self, i_macro_type: str, i_radius: float) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetRadiusOnMacro(CATBSTR iMacroType,
                | double iRadius)
                | 
                |     Defines radius attribute on the circular elementary macro motion on
                |     CIRCULAR MILLING or THREAD MILLING operations ONLY.
                | 
                |     Parameters:
                | 
                |         iMacroType
                |             Legal values: iMacroType can be:
                | 
                |             "Approach", to set the radius on the Approach
                |             Macro
                |             "Retract", to set the radius on the Retract Macro
                |             "ReturnInALevelApproach", to set the radius on the Return in a
                |             level Macro (Approach)
                |             "ReturnInALevelRetract", to set the radius on the Return in a level
                |             Macro (Retract)
                |             "ReturnBetweenLevelsApproach", to set the radius on the Return
                |             between levels Macro (Approach)
                |             "ReturnBetweenLevelsRetract", to set the radius on the Return
                |             between levels Macro (Approach)
                | 
                |         iRadius
                |             Radius value. (expressed in millimeters) 
                | 
                |     Example:
                |         The following example sets a radius 5mm on the circular motion of the
                |         retract macro on the Circular Milling operation
                |         CircularMilling1
                | 
                |          Dim CircularMilling1 As ManufacturingOperation
                |          Set CircularMilling1 = Program1.AppendOperation ("CircularMilling1",1)
                |          Call
                |          CircularMilling1.SetRadiusOnMacro("Retract",5.00)

        :param str i_macro_type:
        :param float i_radius:
        :rtype: None
        """
        return self.manufacturing_operation.SetRadiusOnMacro(i_macro_type, i_radius)

    def set_relimiting_geometry(
            self,
            i_geometry_type: str,
            i_reference: AnyObject,
            i_product: AnyObject,
            i_offset: float,
            i_position: str
    ) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetRelimitingGeometry(CATBSTR iGeometryType,
                | AnyObject iReference,
                | AnyObject iProduct,
                | double iOffset,
                | CATBSTR iPosition)
                | 
                |     Defines start / end element on PROFILE CONTOURING operation
                |     ONLY.
                |     Sets a geometry on relimiting element in profile contouring
                |     operation.
                | 
                |     Parameters:
                | 
                |         iGeometryType
                |             Legal values: iGeometryType can be:
                | 
                |             "StartElement", to set the Start element on Profile
                |             Contouring
                |             "EndElement", to set the End element on Profile
                |             Contouring
                | 
                |         iReference
                |             Geometries to be set. It can be a list of curves or a single point.
                |             The curves must be adjacent. 
                |         iProduct
                |             Product containing the geometry to be set. 
                |         iOffset
                |             Offset to set on the relimiting geometry. (expressed in
                |             millimeters) 
                |         iPosition
                |             Tool position to set on the relimiting geometry.
                |             Legal values: iPosition can be:
                | 
                |             "IN", to set the tool position IN
                |             "ON", to set the tool position ON
                |             "OUT", to set the tool position OUT
                | 
                |     Example:
                |         The following example sets the Start relimiting element Curve1 on the
                |         Profile Contouring operation Contouring1
                | 
                |          Call Contouring1.SetRelimitingGeometry("StartElement",Curve1,PartMachined,3.00,"ON")

        :param str i_geometry_type:
        :param AnyObject i_reference:
        :param AnyObject i_product:
        :param float i_offset:
        :param str i_position:
        :rtype: None
        """
        return self.manufacturing_operation.SetRelimitingGeometry(
            i_geometry_type,
            i_reference.com_object,
            i_product.com_object,
            i_offset,
            i_position
        )

    def set_spindle_magnitude(self, i_magnitude_name: str) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetSpindleMagnitude(CATBSTR iMagnitudeName)
                | 
                |     Defines the magnitude of the spindle values.
                |
                |         The available types for Magnitude are: 
                |          
                |         for Linear Magnitude , iMagnitudeName = LINEARSPINDLESPEED
                |          
                |         for Angular Magnitude , iMagnitudeName = ANGULARSPINDLESPEED
                |          
                |     Example:
                |      Dim Operation1 As ManufacturingOperation
                |      Set Operation1 = Program1.AppendOperation ("Drilling",1)
                |      Operation1.SetSpindleMagnitude("ANGULARSPINDLESPEED")

        :param str i_magnitude_name:
        :rtype: None
        """
        return self.manufacturing_operation.SetSpindleMagnitude(i_magnitude_name)

    def set_start_point_geometry(
            self,
            i_geometry_position: str,
            i_reference: AnyObject,
            i_product: AnyObject,
            i_offset: float
    ) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetStartPointGeometry(CATBSTR iGeometryPosition,
                | AnyObject iReference,
                | AnyObject iProduct,
                | double iOffset)
                | 
                |     Defines the geometry and the offset of a start point on POCKETING operation
                |     ONLY.
                | 
                |     Parameters:
                | 
                |         iGeometryPosition
                |             Legal values: iGeometryPosition can be:
                | 
                |             "Outside", to set the Start point outside the pocket
                |             contour
                |             "Inside", to set the Start point inside the pocket
                |             contour
                | 
                |         iReference
                |             Geometry to be set. It can be a point. 
                |         iProduct
                |             Product containing the geometry to be set. 
                |         iOffset
                |             Offset set on the start point. (expressed in
                |             millimeters)
                |             Offset is taken into account only if iGeometryPosition is set to
                |             "Outside". 
                | 
                |     Example:
                |         The following example sets Point1 as Start point on the Pocketing
                |         operation Pocketing1
                | 
                |          Call Pocketing1.SetStartPointGeometry("Inside",Point1,PartMachined,0.00)

        :param str i_geometry_position:
        :param AnyObject i_reference:
        :param AnyObject i_product:
        :param float i_offset:
        :rtype: None
        """
        return self.manufacturing_operation.SetStartPointGeometry(
            i_geometry_position,
            i_reference.com_object,
            i_product.com_object,
            i_offset
        )

    def set_tool(self, i_tool_name: str) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetTool(CATBSTR iToolName)
                | 
                |     Assign an already created tool to a Manufacturing
                |     Operation.
                |     If the tool is not already created, or if it is not authorized for this
                |     kind of Manufacturing Operation, a default tool is
                |     created.
                | 
                |     Example:
                |         The following example assign a drill tool named D-9.7 on the operation
                |         MO1 of the Manufacturing Program Program1 A tool change with tool D-9.7 has
                |         already been created in the Manufacturing Program.
                | 
                |          Dim Operation1 As ManufacturingOperation
                |          Set Operation1 = Program1.AppendOperation ("Drilling",1)
                |          Operation1.SetTool("D-9.7")

        :param str i_tool_name:
        :rtype: None
        """
        return self.manufacturing_operation.SetTool(i_tool_name)

    def unlock_activity(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub UnlockActivty()

        :rtype: None
        """
        return self.manufacturing_operation.UnlockActivty()

    def __repr__(self):
        return f'ManufacturingOperation(name="{self.name}")'
