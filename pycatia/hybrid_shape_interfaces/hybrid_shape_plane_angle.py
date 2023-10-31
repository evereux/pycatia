#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-07-06 14:02:20.222384

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.hybrid_shape_interfaces.plane import Plane
from pycatia.in_interfaces.reference import Reference
from pycatia.knowledge_interfaces.angle import Angle


class HybridShapePlaneAngle(Plane):
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
                |                         CATGSMIDLItf.Plane
                |                             HybridShapePlaneAngle
                | 
                | Represents the hybrid shape plane angle feature object.
                | Role: To access the data of the hybrid shape plane angle feature object,
                | created with an angle to another plane. This data includes:
                | 
                |     The rotation axis
                |     The rotation angle
                |     The reference plane
                | 
                | Use the CATIAHybridShapeFactory to create a HybridShapePlaneAngle
                | object.
                | 
                | See also:
                |     HybridShapeFactory
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_plane_angle = com_object

    @property
    def angle(self) -> Angle:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Angle() As Angle (Read Only)
                | 
                |     Returns the rotation angle.

        :rtype: Angle
        """

        return Angle(self.hybrid_shape_plane_angle.Angle)

    @property
    def orientation(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Orientation() As long
                | 
                |     Returns or sets the plane orientation.
                |     Role: The orientation allows you to invert the plane from the reference
                |     plane.
                |     Legal values: the orientation is 1 if the plane orientation is not
                |     inverted, and -1 otherwise.

        :rtype: int
        """

        return self.hybrid_shape_plane_angle.Orientation

    @orientation.setter
    def orientation(self, value: int):
        """
        :param int value:
        """

        self.hybrid_shape_plane_angle.Orientation = value

    @property
    def ref_plane(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Plane() As Reference
                | 
                |     Returns or sets the reference plane.
                |     Sub-element(s) supported (see Boundary object): PlanarFace.

        :rtype: Reference
        """

        return Reference(self.hybrid_shape_plane_angle.Plane)

    @ref_plane.setter
    def ref_plane(self, reference_plane: Reference):
        """
        :param Reference reference_plane:
        """

        self.hybrid_shape_plane_angle.Plane = reference_plane.com_object

    @property
    def projection_mode(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property ProjectionMode() As boolean
                | 
                |     Gets or sets the projection mode status.
                |     ProjectionMode = TRUE : Rotation axis will be projected on to reference plane.
                |     FALSE(default) : Rotation axis will be as it is. This example retrieves in ProjMode the projection
                 |                     mode status for the PlaneAngle hybrid shape feature.
                | 
                |      Dim ProjMode As boolean
                |      ProjMode = PlaneAngle.ProjectionMode

        :rtype: bool
        """

        return self.hybrid_shape_plane_angle.ProjectionMode

    @projection_mode.setter
    def projection_mode(self, value: bool):
        """
        :param bool value:
        """

        self.hybrid_shape_plane_angle.ProjectionMode = value

    @property
    def revol_axis(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property RevolAxis() As Reference
                | 
                |     Returns or sets the rotation axis.
                |     Sub-element(s) supported (see Boundary object): RectilinearTriDimFeatEdge,
                |     RectilinearBiDimFeatEdge or RectilinearMonoDimFeatEdge.

        :rtype: Reference
        """

        return Reference(self.hybrid_shape_plane_angle.RevolAxis)

    @revol_axis.setter
    def revol_axis(self, reference_axis: Reference):
        """
        :param Reference reference_axis:
        """

        self.hybrid_shape_plane_angle.RevolAxis = reference_axis.com_object

    def __repr__(self):
        return f'HybridShapePlaneAngle(name="{self.name}")'
