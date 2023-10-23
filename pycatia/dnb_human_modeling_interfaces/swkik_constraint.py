#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.dnb_human_modeling_interfaces.swk_body_element import SWKBodyElement
from pycatia.dnb_human_modeling_interfaces.swk_manikin import SWKManikin
from pycatia.dnb_human_modeling_interfaces.swk_manikin_part import SWKManikinPart
from pycatia.dnb_human_modeling_interfaces.swk_segment import SWKSegment
from pycatia.in_interfaces.reference import Reference
from pycatia.system_interfaces.any_object import AnyObject


class SWKIKConstraint(SWKManikinPart):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     DNBHumanModelingInterfaces.SWKManikinPart
                |                         SWKIKConstraint
                | 
                | This interface manages the constraint of the manikin.
                | It provides access to the constraints data (ID, EndEffector,
                | StartSegment,...)
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.swkik_constraint = com_object

    @property
    def active(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Active() As boolean
                | 
                |     Returns or sets the constraint activity.
                |     A constraint being active means that the constraint is taken
                |     into account during the resolution.
                | 
                |     If the constraint is not active,then it is ignored during the resolution.

        :rtype: bool
        """

        return self.swkik_constraint.Active

    @active.setter
    def active(self, value: bool):
        """
        :param bool value:
        """

        self.swkik_constraint.Active = value

    @property
    def angle_criteria(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property AngleCriteria() As double
                | 
                |     Returns or sets the angle criteria that will be used to evaluate success or
                |     failure of the constraint resolution. If, after resolution, the agle between
                |     the constraint and the target is lower than the criteria, then the constraint
                |     will be considered resolved. This criteria must be specified in radians.

        :rtype: float
        """

        return self.swkik_constraint.AngleCriteria

    @angle_criteria.setter
    def angle_criteria(self, value: float):
        """
        :param float value:
        """

        self.swkik_constraint.AngleCriteria = value

    @property
    def angle_to_target(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property AngleToTarget() As double (Read Only)
                | 
                |     Returns the angle (in radians) from the constraint end effector to the
                |     target.

        :rtype: float
        """

        return self.swkik_constraint.AngleToTarget

    @property
    def distance_criteria(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property DistanceCriteria() As double
                | 
                |     Returns or sets the distance criteria that will be used to evaluate success
                |     or failure of the constraint resolution. If, after resolution, the distance
                |     between the constraint and the target is lower than the criteria, then the
                |     constraint will be considered resolved. This criteria must be specified in
                |     millimeters.

        :rtype: float
        """

        return self.swkik_constraint.DistanceCriteria

    @distance_criteria.setter
    def distance_criteria(self, value: float):
        """
        :param float value:
        """

        self.swkik_constraint.DistanceCriteria = value

    @property
    def distance_to_target(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property DistanceToTarget() As double (Read Only)
                | 
                |     Returns the distance (in mm) from the constraint end effector to the
                |     target.

        :rtype: float
        """

        return self.swkik_constraint.DistanceToTarget

    @property
    def end_effector(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property EndEffector() As CATBSTR
                | 
                |     Returns or sets the end effector of the IK chain of the constraint. The
                |     string in this property is the short name of the last segment (or line of
                |     sight) to be driven by this constraint

        :rtype: str
        """

        return self.swkik_constraint.EndEffector

    @end_effector.setter
    def end_effector(self, value: str):
        """
        :param str value:
        """

        self.swkik_constraint.EndEffector = value

    @property
    def identifier(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Identifier() As CATBSTR (Read Only)
                | 
                |     Returns the identifier(ID) of the constraint.

        :rtype: str
        """

        return self.swkik_constraint.Identifier

    @property
    def is_success(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property IsSuccess() As boolean (Read Only)
                | 
                |     Returns whether the resolution of this constraint is a success or a
                |     failure, given the current criteria.

        :rtype: bool
        """

        return self.swkik_constraint.IsSuccess

    @property
    def manikin(self) -> SWKManikin:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Manikin() As SWKManikin (Read Only)
                | 
                |     Returns the manikin which owns this IK constraint.

        :rtype: SWKManikin
        """

        return SWKManikin(self.swkik_constraint.Manikin)

    @property
    def priority(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Priority() As long
                | 
                |     Returns or sets the priority of the constraint.
                |     When using that property, the number returned or set
                |     is an integer and must be between 1 and 4 inclusive.
                |     The lower the priority, the more prioritary the constraint becomes.

        :rtype: int
        """

        return self.swkik_constraint.Priority

    @priority.setter
    def priority(self, value: int):
        """
        :param int value:
        """

        self.swkik_constraint.Priority = value

    @property
    def rotation_offset_angle(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property RotationOffsetAngle() As double
                | 
                |     Returns or sets the rotation offset angle for the 3D plane
                |     constraint.
                |     This rotation offset angle(rad) is used to adjust 3D plane
                |     constraint.
                |     When using that property, the number returned or set
                |     must be between -PI and PI inclusive.

        :rtype: float
        """

        return self.swkik_constraint.RotationOffsetAngle

    @rotation_offset_angle.setter
    def rotation_offset_angle(self, value: float):
        """
        :param float value:
        """

        self.swkik_constraint.RotationOffsetAngle = value

    @property
    def start_segment(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property StartSegment() As CATBSTR
                | 
                |     Returns or sets the first segment of the body to be driven
                |     by this constraint.

        :rtype: str
        """

        return self.swkik_constraint.StartSegment

    @start_segment.setter
    def start_segment(self, value: str):
        """
        :param str value:
        """

        self.swkik_constraint.StartSegment = value

    @property
    def transfer_with_target(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property TransferWithTarget() As boolean
                | 
                |     Returns or sets the Transfer With Target property.

        :rtype: bool
        """

        return self.swkik_constraint.TransferWithTarget

    @transfer_with_target.setter
    def transfer_with_target(self, value: bool):
        """
        :param bool value:
        """

        self.swkik_constraint.TransferWithTarget = value

    @property
    def user_type(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property UserType() As CATBSTR (Read Only)
                | 
                |     Returns the user type of the constraint. The user type returned will be one
                |     of the following: ("Contact", "Coincidence", "Fix", or "FixOn"),

        :rtype: str
        """

        return self.swkik_constraint.UserType

    def get_constraint_element(self) -> AnyObject:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetConstraintElement() As CATBaseDispatch
                | 
                |     Returns a reference to the target object of the constraint (if any).

        :rtype: AnyObject
        """
        return self.swkik_constraint.GetConstraintElement()

    def get_end_effector(self) -> SWKBodyElement:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetEndEffector() As SWKBodyElement
                | 
                |     Returns the end effector of the IK chain of the constraint.

        :rtype: SWKBodyElement
        """
        return SWKBodyElement(self.swkik_constraint.GetEndEffector())

    def get_start_segment(self) -> SWKSegment:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetStartSegment() As SWKSegment
                | 
                |     Returns the start segment of the IK chain of the constraint.

        :rtype: SWKSegment
        """
        return SWKSegment(self.swkik_constraint.GetStartSegment())

    def get_target_line(self, po_target_line_coord: tuple) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetTargetLine(CATSafeArrayVariant poTargetLineCoord)
                | 
                |     Get the target points coordinates of a line This method
                |     retrieves the origin point coordinates as (x, y, z) data
                |     and the direction value of a line.
                | 
                |     Parameters:
                | 
                |         poTargetLineCoord
                |             The array of 6 data containing target point coordinates as x, y, z
                |             respectively and the x, y, z direction values for the target line.

        :param tuple po_target_line_coord:
        :rtype: None
        """
        return self.swkik_constraint.GetTargetLine(po_target_line_coord)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_target_line'
        # # vba_code = """
        # # Public Function get_target_line(swkik_constraint)
        # #     Dim poTargetLineCoord (2)
        # #     swkik_constraint.GetTargetLine poTargetLineCoord
        # #     get_target_line = poTargetLineCoord
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_target_plane(self, po_target_plane_coord: tuple) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetTargetPlane(CATSafeArrayVariant poTargetPlaneCoord)
                | 
                |     Get the target points coordinates of a line This method retrieves the
                |     origin point coordinates as (x, y, z) data and the direction value of a
                |     line.
                | 
                |     Parameters:
                | 
                |         poTargetLineCoord
                |             The array of 9 data containing origin point coordinates as x, y, z,
                |             the first normalized direction as x, y, z coordinates and the x, y, z
                |             ortho-normalized direction values for the target plane.

        :param tuple po_target_plane_coord:
        :rtype: None
        """
        return self.swkik_constraint.GetTargetPlane(po_target_plane_coord)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_target_plane'
        # # vba_code = """
        # # Public Function get_target_plane(swkik_constraint)
        # #     Dim poTargetPlaneCoord (2)
        # #     swkik_constraint.GetTargetPlane poTargetPlaneCoord
        # #     get_target_plane = poTargetPlaneCoord
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_target_point(self, po_target_pt_coord: tuple) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetTargetPoint(CATSafeArrayVariant poTargetPtCoord)
                | 
                |     Get the target point coordinates. This method retrieves the target point
                |     coordinates as (x, y, z) data under an array form.
                | 
                |     Parameters:
                | 
                |         poTargetPtCoord
                |             The array containing target point coordinates as x, y, z
                |             respectively, the x coordinate being the first data in the array.

        :param tuple po_target_pt_coord:
        :rtype: None
        """
        return self.swkik_constraint.GetTargetPoint(po_target_pt_coord)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_target_point'
        # # vba_code = """
        # # Public Function get_target_point(swkik_constraint)
        # #     Dim poTargetPtCoord (2)
        # #     swkik_constraint.GetTargetPoint poTargetPtCoord
        # #     get_target_point = poTargetPtCoord
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def reset_target(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub ResetTarget()
                | 
                |     Reset the offset of the target object (i.e. set the offset
                |     to the end effector's current position).

        :rtype: None
        """
        return self.swkik_constraint.ResetTarget()

    def set_constraint_element(self, pi_constraint_element: AnyObject, pi_constraint_type: str) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetConstraintElement(CATBaseDispatch
                | piConstraintElement,
                | CATBSTR piConstraintType)
                | 
                |     Set the target object to follow. This method establishes a part relation
                |     between the end effector and an object to follow.
                | 
                |     Parameters:
                | 
                |         piConstraintElement
                |             A reference to the target object
                |             This target object can be either a wireframe 
                | 
                |         GeometricElement object such as a plane or a line, or a boundary
                |         representation object such as a face, a vertex or an edge. In the case of a
                |         'Fix on' constraint, the target object must be the product ( CATIAProduct)
                |         associated with the constraint. 
                |     piConstraintType
                |         The type of the constraint.
                |         This parameter can take the following values: "Coincidence", "Contact",
                |         "Contact2D", "Contact3D", "FixPositon", "FixOrientation",
                |         "FixPositonAndOrientation", "FixOnPositon", "FixOnOrientation" and
                |         "FixOnPositonAndOrientation".

        :param AnyObject pi_constraint_element:
        :param str pi_constraint_type:
        :rtype: None
        """
        return self.swkik_constraint.SetConstraintElement(pi_constraint_element.com_object, pi_constraint_type)

    def set_target_line(
            self,
            pi_object: Reference,
            pi_start_point_x: float,
            pi_start_point_y: float,
            pi_start_point_z: float,
            pi_end_point_x: float,
            pi_end_point_y: float,
            pi_end_point_z: float,
            pi_constraint_type: str
    ) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetTargetLine(Reference piObject,
                | double piStartPointX,
                | double piStartPointY,
                | double piStartPointZ,
                | double piEndPointX,
                | double piEndPointY,
                | double piEndPointZ,
                | CATBSTR piConstraintType)
                | 
                |     Set the target line to follow. This method establishes a contact or
                |     coincidence constraint between the end effector and the
                |     line.
                | 
                |     Parameters:
                | 
                |         piConstraintElement
                |             A reference to the target object
                |             This target object must be the product (
                | 
                |         CATIAProduct) associated with the constraint. 
                |     piStartPointX
                |         The x coordinate of the start point of the line, relatively to the
                |         father object. 
                |     piStartPointY
                |         The y coordinate of the start point of the line, relatively to the
                |         father object. 
                |     piStartPointZ
                |         The z coordinate of the start point of the line, relatively to the
                |         father object. 
                |     piEndPointX
                |         The x coordinate of the end point of the line, relatively to the father
                |         object. 
                |     piEndPointY
                |         The y coordinate of the end point of the line, relatively to the father
                |         object. 
                |     piEndPointZ
                |         The z coordinate of the end point of the line, relatively to the father
                |         object. 
                |     piConstraintType
                |         The type of the constraint.
                |         This parameter can take the values "Contact", "Contact2D", "Contact3D"
                |         or "Coincidence".

        :param Reference pi_object:
        :param float pi_start_point_x:
        :param float pi_start_point_y:
        :param float pi_start_point_z:
        :param float pi_end_point_x:
        :param float pi_end_point_y:
        :param float pi_end_point_z:
        :param str pi_constraint_type:
        :rtype: None
        """
        return self.swkik_constraint.SetTargetLine(
            pi_object.com_object,
            pi_start_point_x,
            pi_start_point_y,
            pi_start_point_z,
            pi_end_point_x,
            pi_end_point_y,
            pi_end_point_z,
            pi_constraint_type)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_target_line'
        # # vba_code = """
        # # Public Function set_target_line(swkik_constraint)
        # #     Dim piObject (2)
        # #     swkik_constraint.SetTargetLine piObject
        # #     set_target_line = piObject
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_target_plane(
            self,
            pi_object: Reference,
            pi_origin_x: float,
            pi_origin_y: float,
            pi_origin_z: float,
            pi_normal_x: float,
            pi_normal_y: float,
            pi_normal_z: float,
            pi_constraint_type: str
    ) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetTargetPlane(Reference piObject,
                | double piOriginX,
                | double piOriginY,
                | double piOriginZ,
                | double piNormalX,
                | double piNormalY,
                | double piNormalZ,
                | CATBSTR piConstraintType)
                | 
                |     Set the target plane to follow. This method establishes a contact or
                |     coincidence constraint between the end effector and the
                |     plane.
                | 
                |     Parameters:
                | 
                |         piConstraintElement
                |             A reference to the target object
                |             This target object must be the product (
                | 
                |         CATIAProduct) associated with the constraint. 
                |     piOriginX
                |         The x coordinate of the origin of the plane, relatively to the father
                |         object. 
                |     piOriginY
                |         The y coordinate of the origin of the plane, relatively to the father
                |         object. 
                |     piOriginZ
                |         The z coordinate of the origin of the plane, relatively to the father
                |         object. 
                |     piNormalX
                |         The x coordinate of the normal vector of the plane, relatively to the
                |         father object. 
                |     piNormalY
                |         The y coordinate of the normal vector of the plane, relatively to the
                |         father object. 
                |     piNormalZ
                |         The z coordinate of the normal vector of the plane, relatively to the
                |         father object. 
                |     piConstraintType
                |         The type of the constraint.
                |         This parameter can take the values "Contact", "Contact2D", "Contact3D"
                |         or "Coincidence".

        :param Reference pi_object:
        :param float pi_origin_x:
        :param float pi_origin_y:
        :param float pi_origin_z:
        :param float pi_normal_x:
        :param float pi_normal_y:
        :param float pi_normal_z:
        :param str pi_constraint_type:
        :rtype: None
        """
        return self.swkik_constraint.SetTargetPlane(
            pi_object.com_object,
            pi_origin_x,
            pi_origin_y,
            pi_origin_z,
            pi_normal_x,
            pi_normal_y,
            pi_normal_z,
            pi_constraint_type
        )
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_target_plane'
        # # vba_code = """
        # # Public Function set_target_plane(swkik_constraint)
        # #     Dim piObject (2)
        # #     swkik_constraint.SetTargetPlane piObject
        # #     set_target_plane = piObject
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_target_point(self, pi_object: Reference, pi_coord_x: float, pi_coord_y: float, pi_coord_z: float) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetTargetPoint(Reference piObject,
                | double piCoordX,
                | double piCoordY,
                | double piCoordZ)
                | 
                |     Set the target point to follow. This method establishes a contact
                |     constraint between the end effector and the point.
                | 
                |     Parameters:
                | 
                |         piConstraintElement
                |             A reference to the target object
                |             This target object must be the product (
                | 
                |         CATIAProduct) associated with the constraint. 
                |     piCoordX
                |         The x coordinate of the point, relatively to the father object.
                |         
                |     piCoordY
                |         The y coordinate of the point, relatively to the father object.
                |         
                |     piCoordZ
                |         The z coordinate of the point, relatively to the father object.

        :param Reference pi_object:
        :param float pi_coord_x:
        :param float pi_coord_y:
        :param float pi_coord_z:
        :rtype: None
        """
        return self.swkik_constraint.SetTargetPoint(pi_object.com_object, pi_coord_x, pi_coord_y, pi_coord_z)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_target_point'
        # # vba_code = """
        # # Public Function set_target_point(swkik_constraint)
        # #     Dim piObject (2)
        # #     swkik_constraint.SetTargetPoint piObject
        # #     set_target_point = piObject
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'SWKikConstraint(name="{self.name}")'
