#! /usr/bin/python3.6
"""
    Enumerated Types Index

    The key values in this module are taken straight from the V5Automation handbook and are therefor not pythonic.

    When used the pycatia method will expect the key value.

"""

axis_system_axis_type = {
    # = 0 Specifies that the axis direction is defined by a point, line, or plane.
    # If the axis is defined by a point, the axis has the direction of the vector going from the origin of the
    # coordinate system to the point.
    # If defined by a line, the axis has the same direction as the line.
    # If defined by a plane, the axis has the same direction as the normal vector of the plane.
    # = 1 Specifies that the axis direction is defined by the three coordinates x,y,z of a vector.
    # = 2 Specifies that the axis direction is not specified or defined by a point, line, or plane.
    # If the axis is defined by a point, the axis has the direction of the vector going from the point to the origin
    # of the coordinate system.
    # If defined by a line, the axis has the opposite direction of the line.
    # If defined by a plane, the axis has the opposite direction of the normal vector of the plane.
    "catAxisSystemAxisSameDirection": 0,
    "catAxisSystemAxisByCoordinates": 1,
    "catAxisSystemAxisOppositeDirection": 2
}

axis_system_main_type = {
    # = 0 Specifies that the axis system is defined by an origin point and three axes
    # = 1 Specifies that the axis system is defined by an origin point, and a rotation around one axis
    # = 2 Specifies that the axis system is defined by an origin point, and the three Euler angles
    # = 3 Specifies that the axis system is a datum.
    "catAxisSystemStandard": 0,
    "catAxisSystemAxisRotation": 1,
    "catAxisSystemEulerAngles": 2,
    "catAxisSystemExplicit": 3,

}

axis_system_origin_type = {
    # = 0 Specifies that the origin point is put at the position defined by a geometric point.
    #   If no point si selected, the origin will be automatically put at the intersection of the lines or planes
    #   defining the axes.
    # = 1 Specifies that the origin point must stay at the position defined by three coordinates x,y,z.
    "catAxisSystemOriginByPoint": 0,
    "catAxisSystemOriginByCoordinates": 1,
}

constraint_angle_selector = {
    # AngleSector = 0
    #   The default sector of a constraint.
    #   Dimension.Value = angle Orientation = catCstOrientSame Side = catCstSidePositive
    # AngleSector = 1
    #   Dimension.Value = angle-180 if angle>180 abs(angle)+180
    #   otherwise
    #   Orientation = catCstOrientOpposite Side = catCstSidePositive
    # AngleSector = 2
    #   Dimension.Value = abs(540-angle) if angle>180 180-fabs(angle)
    #   otherwise
    #   Orientation = catCstOrientOpposite Side = catCstSideNegative
    # AngleSector = 3
    #   Dimension.Value = 360-abs(angle) Orientation = catCstOrientSame Side = catCstSideNegative
    "catCstAngleSector0": 0,
    "catCstAngleSector1": 1,
    "catCstAngleSector2": 2,
    "catCstAngleSector3": 3
}

constraint_dist_config = {
    # catCstDCUnspec
    #     No additional condition is set on the constraint.
    # catCstDCParallel
    #     In addition to being positioned at a given distance, constrained elements are required to be parallel.
    #     Their orientation can be the same or opposite.
    # catCstDCParallelSameOrient
    #     In addition to being positioned at a given distance, constrained elements are required to be parallel, and
    #     their orientations are required to be the same.
    # catCstDCParallelOppOrient
    #     In addition to being positioned at a given distance, constrained elements are required to be parallel, and
    #     their orientations are required to be opposite.
    "catCstDCUnspec": 0,
    "catCstDCParallel": 1,
    "catCstDCParallelSameOrient": 2,
    "catCstDCParallelOppOrient": 3
}

constraint_dist_direction = {
    # catCstDistDirectionNone
    #     No direction has been specified. The constraint is measured as usual.
    # catCstDistDirection1
    #     2D : The constraint is measured along the horizontal axis. 3D : The constraint is measured along the X axis.
    # catCstDistDirection2
    #     2D : The constraint is measured along the vertical axis. 3D : The constraint is measured along the Y axis.
    # catCstDistDirection3
    #     3D : The constraint is measured along the Z axis.
    "catCstDistDirectionNone": 0,
    "catCstDistDirection1": 1,
    "catCstDistDirection2": 2,
    "catCstDistDirection3": 3
}

constraint_mode = {
    "catCstModeDrivingDimension": 0,
    "catCstModeDrivenDimension": 1
}

constraint_orientation = {
    # catCstOrientSame
    #   specifies that characteristic vectors associated to constrained elements have same orientation.
    # catCstOrientOpposite
    #     specifies that characteristic vectors associated to constrained elements have opposite orientation.
    # catCstOrientUndefined
    #     specifies that the relative orientation of characteristic vectors associated to constrained elements is not
    #     specified.
    "catCstOrientSame": 0,
    "catCstOrientOpposite": 1,
    "catCstOrientUndefined": 2
}

constraint_ref_axis = {
    # catCstRefAxisX
    #     The constraint applies to the X axis.
    # catCstRefAxisY
    #     The constraint applies to the Y axis.
    # catCstRefAxisZ
    #     The constraint applies to the Z axis.
    "catCstRefAxisX": 0,
    "catCstRefAxisY": 1,
    "catCstRefAxisZ": 2
}

constraint_ref_type = {
    # catCstRefTypeRelative
    #     The element will not move during the update (the default mode).
    # catCstRefTypeFixInSpace
    #     The element will move to its former position (Assembly context only).
    "catCstRefTypeRelative": 0,
    "catCstRefTypeFixInSpace": 1
}

constraint_side = {
    # catCstSidePositive
    #     First constrained element characteristic vector points towards second constrained element.
    #     Arithmetic sign of constraint value is ignored, only its absolute value is taken into account.
    # catCstSideNegative
    #     First constrained element characteristic vector points opposite to second constrained element.
    #     Arithmetic sign of constraint value is ignored, only its absolute value is taken into account.
    # catCstSideSameAsValue
    #     Arithmetic sign of constraint value specifies where second element lies with regard to first one: a positive
    #     value means in the direction of first constrained element characteristic vector, a negative value in the
    #     opposite direction.
    # catCstSideOppositeToValue
    #     Arithmetic sign of constraint value specifies where second element lies with regard to first one: a negative
    #     value means in the direction of first constrained element characteristic vector, a positive value in the
    #     opposite direction.
    # catCstSideUndefined
    #     Relative positioning of constrained elements is not defined.
    "catCstSidePositive": 0,
    "catCstSideNegative": 1,
    "catCstSideSameAsValue": 2,
    "catCstSideOppositeToValue": 3,
    "catCstSideUndefined": 4,
}

constraint_status = {
    "catCstStatusOK": 0,
    "catCstStatusKOStronglyNotSatisfied": 1,
    "catCstStatusKOWrongOrientOrSide": 2,
    "catCstStatusKOWrongValue": 3,
    "catCstStatusKOWrongGeomEltType": 4,
    "catCstStatusKOBroken": 5
}

constraint_type = {
    "catCstTypeReference": 0,
    "catCstTypeDistance": 1,
    "catCstTypeOn": 2,
    "catCstTypeConcentricity": 3,
    "catCstTypeTangency": 4,
    "catCstTypeLength": 5,
    "catCstTypeAngle": 6,
    "catCstTypePlanarAngle": 7,
    "catCstTypeParallelism": 8,
    "catCstTypeAxisParallelism": 9,
    "catCstTypeHorizontality": 10,
    "catCstTypePerpendicularity": 11,
    "catCstTypeAxisPerpendicularity": 12,
    "catCstTypeVerticality": 13,
    "catCstTypeRadius": 14,
    "catCstTypeSymmetry": 15,
    "catCstTypeMidPoint": 16,
    "catCstTypeEquidistance": 17,
    "catCstTypeMajorRadius": 18,
    "catCstTypeMinorRadius": 19,
    "catCstTypeSurfContact": 20,
    "catCstTypeLinContact": 21,
    "catCstTypePoncContact": 22,
    "catCstTypeChamfer": 23,
    "catCstTypeChamferPerpend": 24,
    "catCstTypeAnnulContact": 25,
    "catCstTypeCylinderRadius": 26,
    "catCstTypeStContinuity": 27,
    "catCstTypeStDistance": 28,
    "catCstTypeSdContinuity": 29,
    "catCstTypeSdShape": 30
}

part_elements_naming_mode = {
    # catNoCheck
    #     Naming is rule-free,
    # catNamingCheckUnderSameNode
    #     Two elements cannot have the same name under the same node,
    # catNamingCheckWithinUIActiveObject
    #     Two elements cannot have the same name within a defined UIActiveObject.
    "catNoNamingCheck": 0,
    "catNamingCheckUnderSameNode": 1,
    "catNamingCheckWithinUIActiveObject": 2,
}

part_surface_elements_location = {
    # catPartBodyLocation
    #     Wireframe and surface elements are created within a PartBody
    # catXGSLocation
    #     Wireframe and surface elements are created within a G.S. or an O.G.S..
    "catPartBodyLocation": 0,
    "catXGSLocation": 1,
}

part_update_mode = {
    # catManualUpdate
    #     User has to manually launch update tasks.
    # catAutomaticUpdate
    #     Update is automatically launched
    "catManualUpdate": 0,
    "catAutomaticUpdate": 1
}
