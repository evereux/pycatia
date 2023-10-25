#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.

"""

from pycatia.in_interfaces.reference import Reference
from pycatia.knowledge_interfaces.dimension import Dimension
from pycatia.system_interfaces.any_object import AnyObject


class Constraint(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     Constraint
                |
                | A geometric constraint set for geometric elements of a part, a sketch, or a
                | product.

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.constraint = com_object

    @property
    def angle_sector(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property AngleSector() As CatConstraintAngleSector
                |
                |     Returns or sets the constraint angle (or angular) sector. The geometric elements of an angle
                |     constraint (e.g. : 2 lines or 2 planes) divide the sketch or the space in 4 regions which are
                |     called angle or angular sectors, numbered from 0 to 3. 1 / 0 ---/--- 2/ 3 By default, the
                |     constraint is created in the sector number 0. One angle sector corresponds exactly to particular
                |     values of the Dimension.Value, the Side and the Orientation. When changing the angle sector, the
                |     Dimension.Value, Side and Orientation are also modified.
                |
                |     Parameters:
                |
                |         AngleSector=0
                |             The default sector of a constraint.
                |             Dimension.Value
                |               = angle Orientation
                |               = catCstOrientSame Side
                |               = catCstSidePositive
                |         AngleSector=1
                |             Dimension.Value
                |               = angle-180 if angle>180 abs(angle)+180 otherwise Orientation
                |               = catCstOrientOpposite Side
                |               = catCstSidePositive
                |         AngleSector=2
                |             Dimension.Value
                |               = abs(540-angle) if angle>180 180-fabs(angle) otherwise Orientation
                |               = catCstOrientOpposite Side
                |               = catCstSideNegative
                |         AngleSector=3
                |             Dimension.Value
                |               = 360-abs(angle) Orientation
                |               = catCstOrientSame Side
                |               = catCstSideNegative
                |
                |             Example:
                |                 The following example retrieves in angleSector the angle sector
                |                 of the angleCst angle constraint and then changes the angle
                |                 sector
                |
                |                  angleSector = angleCst.AngleSector
                |                  angleCst.AngleSector = 2

        :return: enum cat_constraint_angle_sector
        :rtype: int
        """

        return self.constraint.AngleSector

    @angle_sector.setter
    def angle_sector(self, value: int):
        """
        :param int value: enum cat_constraint_angle_sector
        """

        self.constraint.AngleSector = value

    @property
    def dimension(self) -> Dimension:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property Dimension() As Dimension (Read Only)
                |
                |     Returns the constraint dimension. The dimension may be meaningless for some
                |     types of constraints such as tangency constraints, or if the constraint is not
                |     currently satisfied. Use the Status property to check whether the constraint is
                |     satisfied.
                |
                |     Example:
                |         The following example returns in cstDimension the dimension of the
                |         firstCst constraint:
                |
                |          Set cstDimension = firstCst.Dimension

        :rtype: Dimension
        """

        return Dimension(self.constraint.Dimension)

    @property
    def distance_config(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property DistanceConfig() As CatConstraintDistConfig
                |
                |     Returns or sets the distance constraint configuration. Distance constraints
                |     between lines and cylinders offer often more degrees of freedom to geometry
                |     than acually desired. This property allows to limit these degrees of freedom
                |     without having to redefine additional constraints. This property is useless for
                |     constraints whose type is not distance.
                |
                |     Example:
                |         The following example retrieves in distCstConfig the configuration of
                |         the distCst distance constraint:
                |
                |          distCstConfig = distCst.DistanceConfig

        :return: enum cat_constraint_dist_config
        :rtype: int
        """

        return self.constraint.DistanceConfig

    @distance_config.setter
    def distance_config(self, value: int):
        """
        :param int value: enum cat_constraint_dist_config
        """

        self.constraint.DistanceConfig = value

    @property
    def distance_direction(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property DistanceDirection() As CatConstraintDistDirection
                |
                |     Returns or sets the distance constraint direction. This property is useless for constraints whose
                |     type is not Distance (1). Distance constraints may be measured along a particular direction.
                |     Example:
                |         The following example retrieves in distCstDirection the configuration
                |         of the distCst distance constraint:
                | 
                |          distCstConfig = distCst.DistanceDirection

        :return: enum cat_constraint_dist_direction
        :rtype: int
        """

        return self.constraint.DistanceDirection

    @distance_direction.setter
    def distance_direction(self, value: int):
        """
        :param int value: enum cat_constraint_dist_direction
        """

        self.constraint.DistanceDirection = value

    @property
    def mode(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property Mode() As CatConstraintMode
                |
                |     Returns or sets the constraint driving mode. For constraint types
                |     supporting the concept of value, such as distance constraints, the driving mode
                |     tells whether the constraint value actually drives the geometry position, or,
                |     conversely, is driven by it.
                |
                |     Example:
                |         The following example retrieves in currentMode the driving mode for the
                |         distCst distance constraint:
                |
                |          currentMode = distCst.Mode

        :return: enum cat_constraint_mode
        :rtype: int
        """

        return self.constraint.Mode

    @mode.setter
    def mode(self, value: int):
        """
        :param int value:  enum cat_constraint_mode
        """

        self.constraint.Mode = value

    @property
    def orientation(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property Orientation() As CatConstraintOrientation
                |
                |     Returns or sets the constraint orientation. This is used for constraints
                |     that involve two geometric elements and specifies the orientation for the
                |     second geometric element with regard to the first one, when several possible
                |     orientations are all satisfying the constraint.
                |
                |     Example:
                |         The following example retrieves the in distCstOrient the orientation of
                |         the distCst distance constraint:
                |
                |          distCstOrient = distCst.Orientation

        :return: enum cat_constraint_orientation
        :rtype: int
        """

        return self.constraint.Orientation

    @orientation.setter
    def orientation(self, value: int):
        """
        :param int value: enum cat_constraint_orientation
        """

        self.constraint.Orientation = value

    @property
    def reference_axis(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property ReferenceAxis() As CatConstraintRefAxis
                |
                |     Returns or sets the constraint reference axis. AxisParallel or
                |     AxisPerpendicular constraint types define which axis they relate to through
                |     this property, which makes no sense for constraints of another
                |     type.
                |
                |     Example:
                |         The following example retrieves in refAxis the reference axis for the
                |         axisPerpCst AxisPerpendicular constraint:
                |
                |          refAxis = axisPerpCst.ReferenceAxis

        :return: enum cat_constraint_ref_axis
        :rtype: int
        """

        return self.constraint.ReferenceAxis

    @reference_axis.setter
    def reference_axis(self, value: int):
        """
        :param int value: enum cat_constraint_ref_axis
        """

        self.constraint.ReferenceAxis = value

    @property
    def reference_type(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property ReferenceType() As CatConstraintRefType
                |
                |     Returns or sets the constraint reference type. This property is used only
                |     for Reference constraints in the Assembly context.
                |
                |     Example:
                |         The following example applies to the reference constraint refCst2 the
                |         reference type of the constraint refCst1.
                |
                |          refCst2.ReferenceType = refCst1.ReferenceType

        :return: enum cat_constraint_ref_type
        :rtype: int
        """

        return self.constraint.ReferenceType

    @reference_type.setter
    def reference_type(self, value: int):
        """
        :param int value: enum cat_constraint_ref_type
        """

        self.constraint.ReferenceType = value

    @property
    def side(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property Side() As CatConstraintSide
                |
                |     Returns or sets the constraint side. Some constraint types need to
                |     relatively position the constrained geometries, when several possible
                |     configurations are all satisfying the constraint.
                |
                |     Example:
                |         The following example retrieves in distCstSide the side of the distCst
                |         distance constraint:
                |
                |          distCstSide = distCst.Side

        :return: enum cat_constraint_side
        :rtype: int
        """

        return self.constraint.Side

    @side.setter
    def side(self, value: int):
        """
        :param int value:
        """

        self.constraint.Side = value

    @property
    def status(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property Status() As CatConstraintStatus (Read Only)
                |
                |     Returns the constraint status. The constraint status is a diagnosis on
                |     whether the constraint is satisfied.
                |
                |     Example:
                |         The following example retrieves the status of the distCst distance
                |         constraint.
                |
                |          distCstSts = distCst.Status

        :return: enum cat_constraint_status
        :rtype: int
        """

        return self.constraint.Status

    @property
    def type(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property Type() As CatConstraintType (Read Only)
                |
                |     Returns the constraint type.
                |
                |     Example:
                |         The following example returns in cstType the type of the firstCst
                |         constraint:
                |
                |          cstType = firstCst.Type

        :return: enum cat_constraint_type
        :rtype: int
        """

        return self.constraint.Type

    def activate(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub Activate()
                |
                |     Unsuppresses a constraint for the update process. An activated constraint
                |     is again taken into account for the calculation of the part or product.
                |
                | Example:
                |     The following example es the pad1 pad:
                | Example:
                |     The following example activates the tangencyCst constraint
                |     :
                |
                |      tangencyCst.Activate

        :rtype: None
        """
        return self.constraint.Activate()

    def deactivate(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub Deactivate()
                |
                |     Suppresses the constraint from being updated. A deactivated constraint is
                |     not taken into account for the calculation of the part or of the product.
                |
                |
                | Example:
                |     The following example deactivates the tangencyCst constraint from being
                |     updated:
                |
                |      tangencyCst.Deactivate

        :rtype: None
        """
        return self.constraint.Deactivate()

    def get_constraint_element(self, i_element_number: int) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func GetConstraintElement(long iElementNumber) As
                | Reference
                |
                |     Reads an element of a constraint.
                |
                |     Parameters:
                |
                |         iElementNumber
                |             The number of the element of the constraint to be read. (1 for the first element,2 for
                |             the second, 3 for the third). Notice it must not exceed the total number of elements of
                |             the constraint. (eg : not allowed to read the third element of a tangency).
                |         oCurrentElement
                |             An element of the constraint.
                |
                |     Example:
                |         The following example reads the first element of a
                |         constraint
                |
                |          Dim reference1 As Reference
                |          reference1=tangencyCst.GetConstraintElement( 1 )

        :param int i_element_number:
        :rtype: Reference
        """
        return Reference(self.constraint.GetConstraintElement(i_element_number))

    def get_constraint_visu_location(self, o_anchor_point: tuple, o_anchor_vector: tuple) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub GetConstraintVisuLocation(CATSafeArrayVariant
                | oAnchorPoint,
                | CATSafeArrayVariant oAnchorVector)
                |
                |     Returns the constraint visualisation location. When displayed on screen,
                |     the constraint is visualized as a dimension positioned close to the constrained
                |     geometric element(s). This method retrieves the data used to position this
                |     representation within the 3D space.
                |
                |     Parameters:
                |
                |         oAnchorPoint
                |             A Safe Array made up of 3 doubles: X, Y, Z, representing the
                |             coordinates in model space of the point where the constraint value is
                |             displayed.
                |         oAnchorVector
                |             A Safe Array made up of 3 doubles : X, Y, Z, representing the vector normal to the plane
                |             onto which the constraint value is displayed.
                |
                |     Example:
                |         The following example retrieves in anchorPt the anchor point of the
                |         tangencyCst tangency constraint:
                |
                |          Dim anchorPoint(2)
                |          Dim anchorVector(2)
                |          tangencyCst.ConstraintVisuLocation
                |          anchorPoint,vectorPoint

        :param tuple o_anchor_point:
        :param tuple o_anchor_vector:
        :rtype: None
        """
        return self.constraint.GetConstraintVisuLocation(o_anchor_point, o_anchor_vector)
        # # # # Autogenerated comment:
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_constraint_visu_location'
        # # vba_code = """
        # # Public Function get_constraint_visu_location(constraint)
        # #     Dim oAnchorPoint (2)
        # #     constraint.GetConstraintVisuLocation oAnchorPoint
        # #     get_constraint_visu_location = oAnchorPoint
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def is_inactive(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func IsInactive() As boolean
                |
                |     Indicates whether a constraint is suppressed from the update process. A
                |     suppressed constraint is not taken into account for the calculation of part or
                |     the product. The method returns True if the constraint is not active, False if
                |     the constraint is active.
                | Example:
                |     The following example returns in isInactive whether the tangencyCst
                |     constraint is suppressed from the update process:
                |
                |      Set isInactive = tangencyCst.IsInactive

        :rtype: bool
        """
        return self.constraint.IsInactive()

    def set_constraint_element(self, i_element_number: int, i_new_element: Reference) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub SetConstraintElement(long iElementNumber,
                | Reference iNewElement)
                |
                |     Replaces an element of a constraint.
                |
                |     Parameters:
                |
                |         iElementNumber
                |             The number of the element of the constraint to replace. (1 for the
                |             first element,2 for the second, 3 for the third).
                |         iNewElement
                |             A new element of the constraint.
                |
                |     Example:
                |         The following example changes the second element of a
                |         constraint
                |
                |          Dim reference1 As Reference
                |          tangencyCst.SetConstraintElement ( 2, reference1)

        :param int i_element_number:
        :param Reference i_new_element:
        :rtype: None
        """
        return self.constraint.SetConstraintElement(i_element_number, i_new_element.com_object)
        # # # # Autogenerated comment:
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_constraint_element'
        # # vba_code = """
        # # Public Function set_constraint_element(constraint)
        # #     Dim iElementNumber (2)
        # #     constraint.SetConstraintElement iElementNumber
        # #     set_constraint_element = iElementNumber
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_constraint_visu_location(self, i_new_x: float, i_new_y: float, i_new_z: float) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub SetConstraintVisuLocation(double iNewX,
                | double iNewY,
                | double iNewZ)
                |
                |     Sets a new location for the constraint visualization.
                |
                |     Parameters:
                |
                |         iNewX
                |             The new value for the constraint anchor point X coordinate
                |
                |         iNewY
                |             The new value for the constraint anchor point Y coordinate
                |
                |         iNewZ
                |             The new value for the constraint anchor point Z coordinate
                |
                |
                |     Example:
                |         The following example changes the anchor point coordinates to
                |         10,0,0
                |
                |          tangencyCst.SetConstraintVisuLocation 10,0,0

        :param float i_new_x:
        :param float i_new_y:
        :param float i_new_z:
        :rtype: None
        """
        return self.constraint.SetConstraintVisuLocation(i_new_x, i_new_y, i_new_z)

    def __repr__(self):
        return f'Constraint(name="{self.name}")'
