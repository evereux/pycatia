#! /usr/bin/python3.6
# module initially auto generated using V5Automation.chm from CATIA V5 R25

from pycatia.system_interfaces.any_object import AnyObject
from pycatia.knowledge_interfaces.dimension import Dimension
from pycatia.in_interfaces.reference import Reference


class Constraint(AnyObject):
    """
        .. note::
            CAA V5 Visual Basic help

                | A geometric constraint set for geometric elements of a part, a sketch,
                | or a product.

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.constraint = com_object

    @property
    def angle_sector(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | AngleSector
                | o Property AngleSector() As CatConstraintAngleSector
                | 
                | Returns or sets the constraint angle (or angular) sector. The
                | geometric elements of an angle constraint         (e.g. : 2 lines or 2
                | planes) divide the sketch or the space in 4 regions which are called
                | angle or angular sectors, numbered from 0 to 3.        1  / 0 ---/---
                | 2/   3 By default, the constraint is created in the sector number 0.
                | One angle sector corresponds exactly to particular values  of the
                | Dimension.Value, the Side and the Orientation. When changing the angle
                | sector, the Dimension.Value,  Side and Orientation are also modified.


                | Parameters:
                | AngleSector=0
                |     The default sector of a constraint.      
                |         Dimension.Value = angle 
                |         Orientation     = catCstOrientSame
                |         Side            = catCstSidePositive
                |  
                |  AngleSector=1
                |         Dimension.Value = angle-180 if angle>180
                |                          abs(angle)+180 otherwise
                |         Orientation     = catCstOrientOpposite
                |         Side            = catCstSidePositive
                |  
                |  AngleSector=2
                |         Dimension.Value = abs(540-angle) if angle>180
                |                          180-fabs(angle) otherwise
                |         Orientation     = catCstOrientOpposite
                |         Side            = catCstSideNegative
                |  
                |  AngleSector=3
                |         Dimension.Value = 360-abs(angle)
                |         Orientation     = catCstOrientSame
                |         Side            = catCstSideNegative


                | Examples:
                | 
                | The following example retrieves in angleSector
                | the angle sector of the angleCst angle constraint
                | and then changes the angle sector
                | 
                | angleSector = angleCst.AngleSector
                | angleCst.AngleSector = 2

        :return: int
        """
        return self.constraint.AngleSector

    @property
    def dimension(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Dimension
                | o Property Dimension() As Dimension
                | 
                | Returns the constraint dimension. The dimension may be meaningless for
                | some types of constraints  such as tangency constraints,  or if the
                | constraint is not currently satisfied. Use the
                | activateLinkAnchor('','Status','Status')  property to check whether
                | the constraint is  satisfied.  Example:The following example returns
                | in cstDimension the dimension  of the firstCst constraint:  Set
                | cstDimension = firstCst.Dimension


                | Parameters:


        """
        return Dimension(self.constraint.Dimension)

    @property
    def distance_config(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | DistanceConfig
                | o Property DistanceConfig() As CatConstraintDistConfig
                | 
                | Returns or sets the distance constraint configuration. Distance
                | constraints between lines and cylinders offer  often more degrees of
                | freedom to geometry than acually desired. This property allows to
                | limit these degrees of freedom without  having to redefine additional
                | constraints. This property is useless for constraints whose type is
                | not distance.   Example:The following example retrieves in
                | distCstConfig the configuration of the distCst distance constraint:
                | distCstConfig = distCst.DistanceConfig


                | Parameters:

        :return: int
        """
        return self.constraint.DistanceConfig

    @property
    def distance_direction(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | DistanceDirection
                | o Property DistanceDirection() As CatConstraintDistDirection
                | 
                | Returns or sets the distance constraint direction. This property is
                | useless for constraints whose type is not Distance (1). Distance
                | constraints may be measured along a particular direction. This
                | property will be  used if the direction is a reference axis : In 2D, 1
                | means the horizontal axis, 2 the vertical axis.   In 3D, 1 stands for
                | the X axis, 2 for the Y axis, 3 for the Z axis. 0 means that no
                | direction is specified and the distance is measured as usual.
                | Example:The following example retrieves in distCstDirection the
                | configuration of the distCst distance constraint:  distCstConfig =
                | distCst.DistanceDirection


                | Parameters:

        :return: int
        """
        return self.constraint.DistanceDirection

    @property
    def mode(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Mode
                | o Property Mode() As CatConstraintMode
                | 
                | Returns or sets the constraint driving  mode.  For constraint types
                | supporting the concept of value, such as distance  constraints, the
                | driving mode tells whether the constraint value actually drives the
                | geometry position, or, conversely, is driven  by it.  Example:The
                | following example retrieves in currentMode the driving mode for the
                | distCst distance constraint:   currentMode = distCst.Mode


                | Parameters:

        :return: int
        """
        return self.constraint.Mode

    @property
    def orientation(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Orientation
                | o Property Orientation() As CatConstraintOrientation
                | 
                | Returns or sets the constraint orientation. This is used for
                | constraints that involve  two  geometric elements and specifies the
                | orientation for the second geometric element with regard to the first
                | one, when several  possible orientations are all satisfying the
                | constraint.    Example:The following example retrieves the in
                | distCstOrient the orientation of the distCst distance constraint:
                | distCstOrient = distCst.Orientation


                | Parameters:

        :return: int
        """
        return self.constraint.Orientation

    @property
    def reference_axis(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | ReferenceAxis
                | o Property ReferenceAxis() As CatConstraintRefAxis
                | 
                | Returns or sets the constraint reference axis. AxisParallel or
                | AxisPerpendicular constraint types define which axis they relate to
                | through this property,  which makes no sense for constraints of
                | another type.  Example:The following example retrieves in refAxis the
                | reference axis for the axisPerpCst AxisPerpendicular constraint:
                | refAxis = axisPerpCst.ReferenceAxis


                | Parameters:

        :return: int
        """
        return self.constraint.ReferenceAxis

    @property
    def reference_type(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | ReferenceType
                | o Property ReferenceType() As CatConstraintRefType
                | 
                | Returns or sets the constraint reference type. This property is used
                | only for Reference constraints in the Assembly context.  Example:The
                | following example applies to the reference constraint refCst2 the
                | reference type of the constraint refCst1.   refCst2.ReferenceType =
                | refCst1.ReferenceType


                | Parameters:

        :return: int
        """
        return self.constraint.ReferenceType

    @property
    def side(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Side
                | o Property Side() As CatConstraintSide
                | 
                | Returns or sets the constraint side.  Some constraint types need to
                | relatively position the constrained geometries, when several possible
                | configurations are all satisfying the constraint.   Example:The
                | following example retrieves in distCstSide the side of the distCst
                | distance constraint:   distCstSide = distCst.Side


                | Parameters:

        :return: int
        """
        return self.constraint.Side

    @property
    def status(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Status
                | o Property Status() As CatConstraintStatus
                | 
                | Returns the constraint status. The constraint status is a diagnosis on
                | whether the constraint is satisfied.  Example:The following example
                | retrieves the status of the distCst distance constraint.   distCstSts
                | = distCst.Status


                | Parameters:

        :return: int
        """
        return self.constraint.Status

    @property
    def type(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Type
                | o Property Type() As CatConstraintType
                | 
                | Returns the  constraint type.  Example:The following example returns
                | in cstType the type  of the firstCst constraint:  cstType =
                | firstCst.Type


                | Parameters:

        :return: int
        """
        return self.constraint.Type

    def activate(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Activate
                | o Sub Activate()
                | 
                | Unsuppresses a constraint for the update process. An activated
                | constraint is again taken into account  for the calculation of the
                | part or product. Example:The following example es the pad1 pad:
                | Example:The following example activates the tangencyCst constraint :
                | tangencyCst.Activate

        """
        self.constraint.Activate()

    def deactivate(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Deactivate
                | o Sub Deactivate()
                | 
                | Suppresses the constraint from being updated. A deactivated constraint
                | is not taken into account  for the calculation of the part or of the
                | product.

        """
        self.constraint.Deactivate()

    def get_constraint_element(self, i_element_number):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetConstraintElement
                | o Func GetConstraintElement(    long    iElementNumber) As Reference
                | 
                | Reads an element of a constraint.


                | Parameters:
                | iElementNumber
                |    The number of the element of the constraint to be read.
                |    (1 for the first element,2 for the second, 3 for the third).
                |    Notice it must not exceed the total number of elements of the constraint.
                |    (eg : not allowed to read the third element of a tangency).
                |   
                |  
                |   oCurrentElement
                |    An element of the constraint.


                | Examples:
                | 
                | The following example reads the first element of a constraint
                | 
                | Dim reference1 As Reference
                | reference1=tangencyCst.GetConstraintElement( 1 )
                | 
                | 
                | 
        """
        return Reference(self.constraint.GetConstraintElement(i_element_number))

    def get_constraint_visu_location(self, o_anchor_point, o_anchor_vector):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetConstraintVisuLocation
                | o Sub GetConstraintVisuLocation(    CATSafeArrayVariant    oAnchorPoint,
                |                                     CATSafeArrayVariant    oAnchorVector)
                | 
                | Returns the constraint visualisation location. When displayed on
                | screen, the constraint is visualized as  a dimension positioned close
                | to the constrained geometric element(s). This method retrieves the
                | data used to position this representation within the 3D space.


                | Parameters:
                | oAnchorPoint
                |    A Safe Array made up of 3 doubles: X, Y, Z, representing the 
                |    coordinates in model space of the point where the constraint value 
                |    is displayed.
                |  
                |  oAnchorVector
                |      A Safe Array made up of 3 doubles : X, Y, Z, representing the 
                |    vector normal to the plane onto which the constraint value 
                |    is displayed.


                | Examples:
                | 
                | The following example retrieves in anchorPt the anchor point
                | of the tangencyCst tangency constraint:
                | 
                | Dim anchorPoint(2)
                | Dim anchorVector(2)
                | tangencyCst.ConstraintVisuLocation anchorPoint,vectorPoint

        :return: tuple
        """
        return self.constraint.GetConstraintVisuLocation(o_anchor_point, o_anchor_vector)

    def is_inactive(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | IsInactive
                | o Func IsInactive() As boolean
                | 
                | Indicates whether a constraint is suppressed from the update process.
                | A suppressed constraint is not taken into account for the calculation
                | of part or  the product. The method returns True if the constraint is
                | not active,  False if the constraint is active. Example:The following
                | example returns in isInactive whether the tangencyCst constraint is
                | suppressed from the update process:  Set isInactive =
                | tangencyCst.IsInactive

        :return: bool
        """
        return self.constraint.IsInactive()

    def set_constraint_element(self, i_element_number, i_new_element):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetConstraintElement
                | o Sub SetConstraintElement(    long    iElementNumber,
                |                                Reference    iNewElement)
                | 
                | Replaces an element of a constraint.


                | Parameters:
                | iElementNumber
                |    The number of the element of the constraint to replace.
                |    (1 for the first element,2 for the second, 3 for the third).
                |   
                |  
                |   iNewElement
                |    A new element of the constraint.


                | Examples:
                | 
                | The following example changes the second element of a constraint
                | 
                | Dim reference1 As Reference
                | tangencyCst.SetConstraintElement ( 2, reference1)

        :param int i_element_number:
        :param Reference() i_new_element:
        """
        return self.constraint.SetConstraintElement(i_element_number, i_new_element.com_object)

    def set_constraint_visu_location(self, i_new_x, i_new_y, i_new_z):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetConstraintVisuLocation
                | o Sub SetConstraintVisuLocation(    double    iNewX,
                |                                     double    iNewY,
                |                                     double    iNewZ)
                | 
                | Sets a new location for the constraint visualization.


                | Parameters:
                | iNewX
                |    The new value for the constraint anchor point X coordinate
                |  
                |   iNewY
                |    The new value for the constraint anchor point Y coordinate
                |  
                |   iNewZ
                |    The new value for the constraint anchor point Z coordinate


                | Examples:
                | 
                | The following example changes the anchor point coordinates to 10,0,0
                | 
                | tangencyCst.SetConstraintVisuLocation 10,0,0

        :param float i_new_x:
        :param float i_new_y:
        :param float i_new_z:
        """
        return self.constraint.SetConstraintVisuLocation(i_new_x, i_new_y, i_new_z)

    def __repr__(self):
        return f'Constraint()'
