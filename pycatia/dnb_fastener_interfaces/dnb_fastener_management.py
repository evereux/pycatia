#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.dnb_fastener_interfaces.curve_fastener import CurveFastener
from pycatia.dnb_fastener_interfaces.fastener_group import FastenerGroup
from pycatia.dnb_fastener_interfaces.point_fastener import PointFastener
from pycatia.system_interfaces.any_object import AnyObject


class DnbFastenerManagement(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     DNBFastenerManagement
                | 
                | Valid fastener process types and its fastening context *
                | The valid known values for process types for fasteners and value for its
                | fastening context
                | 
                |     Point fasteners fastening context
                |     sealant point
                |     1
                |     spot weld
                |     2
                |     stud weld
                |     2
                |     Glue Drop
                |     1
                |     Rivet
                |     2
                |     Screw
                |     2
                |     clinch
                |     2
                |     Drill
                |     2
                |     adhesive point
                |     1
                |     stud
                |     2 Curve fasteners
                |     adhesive Curve
                |     1
                |     arc weld
                |     2
                |     sealant curve
                |     1
                |     glue bead
                |     1
                |     adhesive
                |     1
                |     sealant
                |     1
                |     spot glue
                |     1
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.dnb_fastener_management = com_object

    def create_curve_fastener(
            self,
            i_name: str,
            i_parent_group_body: FastenerGroup,
            i_list_of_joining_parts: tuple,
            i_process_type: str,
            i_fastening_context: int,
            i_design_points_positions: tuple,
            i_feature_cgr_path: str,
            o_curve_fastener: CurveFastener
    ) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub CreateCurveFastener(CATBSTR iName,
                | FastenerGroup iParentGroupBody,
                | CATSafeArrayVariant iListOfJoiningParts,
                | CATBSTR iProcessType,
                | short iFasteningContext,
                | CATSafeArrayVariant iDesignPointsPositions,
                | CATBSTR iFeatureCGRPath,
                | CurveFastener oCurveFastener)
                | 
                |     Creates a curve fastener in the V5 .. only for flat file
                |     scenario.
                | 
                |     Parameters:
                | 
                |         in
                |             CATBSTR iName Name of the feature to be created.. a unique value
                |             has to be provided. 
                |         inout
                |             DELMIAFastenerGroup iParentGroupBody Parent under which fastener to
                |             be created In case of no parent provided, fastener would be created under top
                |             fastener group(assembly joint(s)) automatically. 
                |         in
                |             CATSafeArrayVariant iListOfJoiningParts List of joining parts for
                |             fastener In case, the parent assembly joint already has joining part
                |             information empty list can be provided, 
                |         in
                |             CATBSTR iProcessType Process type for fastener : refer known values on top section of
                |             file. any custom value other than known values can be provided
                |         in
                |             short iFasteningContext fastening contex : refer known values on top section of file for
                |             a process type For custom fastener type.. value can be 1 or greater. if any other value
                |             provided default would be set to 2.
                |         in
                |             CATSafeArrayVariant iDesignPointsPositions Design position for
                |             curve fastener Multiple support points can be provided in a sequence in the
                |             array in the order of "XYZYPR" for each point .. YPR values should be in
                |             Degree. if fastener has n points , then size of array should be exactly of 6n
                |             now assign values for first point's poisition in XYZYPR format at location 0-5
                |             .. next point's 6-11... next 12-17... 18-23... 6(n-1)-(6n-1)
                |             
                |         in
                |             CATBSTR iFeatureCGRPath Representation for curve fastener Value
                |             should be complete file path 
                |         out
                |             DELMIACurveFastener oCurveFastener Created curve fastener *
                |             
                | 
                |     Example:
                |         Set myObject = CATIA.GetItem("DNBFastenerManagement")
                |         myObject.CreateCurveFastener "Curve Fastener.1", ParentGroupObj,JoinPartArray,"arc weld",2, DesignPos, FeatureRepPath, oCurveFast

        :param str i_name:
        :param FastenerGroup i_parent_group_body:
        :param tuple i_list_of_joining_parts:
        :param str i_process_type:
        :param int i_fastening_context:
        :param tuple i_design_points_positions:
        :param str i_feature_cgr_path:
        :param CurveFastener o_curve_fastener:
        :rtype: None
        """
        return self.dnb_fastener_management.CreateCurveFastener(
            i_name,
            i_parent_group_body.com_object,
            i_list_of_joining_parts,
            i_process_type,
            i_fastening_context,
            i_design_points_positions,
            i_feature_cgr_path,
            o_curve_fastener.com_object
        )
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'create_curve_fastener'
        # # vba_code = """
        # # Public Function create_curve_fastener(dnb_fastener_management)
        # #     Dim iName (2)
        # #     dnb_fastener_management.CreateCurveFastener iName
        # #     create_curve_fastener = iName
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def create_fastener_group(
            self,
            i_name: str,
            i_parent_group_body: FastenerGroup,
            i_list_of_joining_parts: tuple,
            o_fastener_group: FastenerGroup
    ) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub CreateFastenerGroup(CATBSTR iName,
                | FastenerGroup iParentGroupBody,
                | CATSafeArrayVariant iListOfJoiningParts,
                | FastenerGroup oFastenerGroup)
                | 
                |     Creates a fastener group in the V5 .. only for flat file
                |     scenario.
                | 
                |     Parameters:
                | 
                |         in
                |             CATBSTR iName Name of the feature to be created.. a unique value
                |             has to be provided. 
                |         inout
                |             DELMIAFastenerGroup iParentGroupBody Parent under which fastener
                |             group to be created In case of no parent provided, fastener group would be
                |             created under top fastener group(assembly joint(s)) automatically.
                |             
                |         in
                |             CATSafeArrayVariant iListOfJoiningParts List of joining parts for
                |             fastener If the List has joining parts .. an assembly joint is created If list
                |             has no part .. a normal fastener group is created 
                |         out
                |             DELMIAFastenerGroup oFastenerGroup Created fastener group *
                |             
                | 
                |     Example:
                |         Set myObject = CATIA.GetItem("DNBFastenerManagement")
                |         myObject.CreateFastenerGroup "Assembly Joint.1", ParentGroupObj,JoinPartArray,oFastenerGroup

        :param str i_name:
        :param FastenerGroup i_parent_group_body:
        :param tuple i_list_of_joining_parts:
        :param FastenerGroup o_fastener_group:
        :rtype: None
        """
        return self.dnb_fastener_management.CreateFastenerGroup(
            i_name,
            i_parent_group_body.com_object,
            i_list_of_joining_parts,
            o_fastener_group.com_object
        )
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'create_fastener_group'
        # # vba_code = """
        # # Public Function create_fastener_group(dnb_fastener_management)
        # #     Dim iName (2)
        # #     dnb_fastener_management.CreateFastenerGroup iName
        # #     create_fastener_group = iName
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def create_point_fastener(
            self,
            i_name: str,
            i_parent_group_body: FastenerGroup,
            i_list_of_joining_parts: tuple,
            i_process_type: str,
            i_fastening_context: int,
            i_design_position: tuple,
            o_point_fastener: PointFastener
    ) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub CreatePointFastener(CATBSTR iName,
                | FastenerGroup iParentGroupBody,
                | CATSafeArrayVariant iListOfJoiningParts,
                | CATBSTR iProcessType,
                | short iFasteningContext,
                | CATSafeArrayVariant iDesignPosition,
                | PointFastener oPointFastener)
                | 
                |     Creates a point fastener in the V5 .. only for flat file
                |     scenario.
                | 
                |     Parameters:
                | 
                |         in
                |             CATBSTR iName Name of the feature to be created.. a unique value
                |             has to be provided. 
                |         inout
                |             DELMIAFastenerGroup iParentGroupBody Parent under which fastener to
                |             be created In case of no parent provided, fastener would be created under top
                |             fastener group(assembly joint(s)) automatically. 
                |         in
                |             CATSafeArrayVariant iListOfJoiningParts List of joining parts for
                |             fastener In case, the parent assembly joint already has joining part
                |             information empty list can be provided, 
                |         in
                |             CATBSTR iProcessType Process type for fastener : refer known values on top section of
                |             file. any custom value other than known values can be provided
                |         in
                |             short iFasteningContext fastening contex : refer known values on top section of file
                |             for a process type For custom fastener type.. value can be 1 or greater. if any other
                |             value provided default would be set to 2.
                |         in
                |             CATSafeArrayVariant iDesignPointsPositions Design position for
                |             point fastener in XYZYPR format .... YPR values should be in Degree. array
                |             should be exactly of size of six array should contains values on index from 0-5
                |             in a sequence order of XYZYPR format. 
                |         out
                |             DELMIAPointFastener oPointFastener Created point fastener *
                |             
                | 
                |     Example:
                |         Set myObject = CATIA.GetItem("DNBFastenerManagement")
                |         myObject.CreatePointFastener "Point Fastener.1", ParentGroupObj,JoinPartArray,"spot weld",2, DesignPos, oPointFastener

        :param str i_name:
        :param FastenerGroup i_parent_group_body:
        :param tuple i_list_of_joining_parts:
        :param str i_process_type:
        :param int i_fastening_context:
        :param tuple i_design_position:
        :param PointFastener o_point_fastener:
        :rtype: None
        """
        return self.dnb_fastener_management.CreatePointFastener(
            i_name,
            i_parent_group_body.com_object,
            i_list_of_joining_parts,
            i_process_type,
            i_fastening_context,
            i_design_position,
            o_point_fastener.com_object
        )
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'create_point_fastener'
        # # vba_code = """
        # # Public Function create_point_fastener(dnb_fastener_management)
        # #     Dim iName (2)
        # #     dnb_fastener_management.CreatePointFastener iName
        # #     create_point_fastener = iName
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'DnbFastenerManagement(name="{self.name}")'
