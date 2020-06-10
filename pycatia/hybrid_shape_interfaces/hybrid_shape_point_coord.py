#! usr/bin/python3.6
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-09 09:53:18.676780

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.hybrid_shape_interfaces.point import Point
from pycatia.in_interfaces.reference import Reference
from pycatia.knowledge_interfaces.length import Length


class HybridShapePointCoord(Point):

    """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.HybridShape
                |                         CATGSMIDLItf.Point
                |                             HybridShapePointCoord
                | 
                | Point defined by coordinates.
                | Role: To access data of the point feature created with its cartesian
                | coordinates.
                | 
                | See also:
                |     Length 
                | See also:
                |     Reference 
                | See also:
                |     HybridShapeFactory
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_point_coord = com_object

    @property
    def pt_ref(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property PtRef() As Reference
                | 
                |     Returns or Sets the reference point for PointCoord
                |     feature.
                |     This data is not mandatory, if element is null, the origin point is
                |     taken.
                |     When an element is given, X, Y and Z are measured starting from this
                |     point.
                |     Sub-element(s) supported (see Boundary object): Vertex.
                | 
                |     Example
                |     :
                |         This example retrieves in oPtRef the reference point for PointCoord
                |         feature.
                | 
                |          Dim oPtRef As CATIAReference
                |          Set oPtRef  = PointCoord.PtRef

        :return: Reference
        """

        return Reference(self.hybrid_shape_point_coord.PtRef)

    @pt_ref.setter
    def pt_ref(self, value):
        """
        :param Reference value:
        """

        self.hybrid_shape_point_coord.PtRef = value

    @property
    def ref_axis_system(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property RefAxisSystem() As Reference
                | 
                |     Returns or Sets the reference Axis System for PointCoord
                |     feature.
                |     This data is not mandatory, if element is null, the absolute axis system is
                |     taken.
                |     When an element is given, X, Y and Z are considered in this Axis
                |     system.
                |     If reference point is not specified, X,Y and Z are measured from origin of
                |     this axis system. *
                | 
                |     Example
                |     :
                |         This example retrieves in oRefAxis the reference Axis System for
                |         PointCoord feature.
                | 
                |          Dim oRefAxis As CATIAReference
                |          Set oRefAxis  = PointCoord.RefAxisSystem

        :return: Reference
        """

        return Reference(self.hybrid_shape_point_coord.RefAxisSystem)

    @ref_axis_system.setter
    def ref_axis_system(self, value):
        """
        :param Reference value:
        """

        self.hybrid_shape_point_coord.RefAxisSystem = value

    @property
    def x(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property X() As Length (Read Only)
                | 
                |     Returns X coordinate of the point.
                | 
                |     Example
                |     :
                |         This example retrieves in oX the X coordinate for the PointCoord hybrid
                |         shape feature.
                | 
                |          Dim oX As CATIALength
                |          Set oX = PointCoord.X

        :return: Length
        """

        return Length(self.hybrid_shape_point_coord.X)

    @property
    def y(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property Y() As Length (Read Only)
                | 
                |     Returns Y coordinate of the point.
                | 
                |     Example
                |     :
                |         This example retrieves in oY the Y coordinate for the PointCoord hybrid
                |         shape feature.
                | 
                |          Dim oY As CATIALength
                |          Set oY = PointCoord.Y

        :return: Length
        """

        return Length(self.hybrid_shape_point_coord.Y)

    @property
    def z(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property Z() As Length (Read Only)
                | 
                |     Returns Z coordinate of the point.
                | 
                |     Example
                |     :
                |         This example retrieves in oZ the Z coordinate for the PointCoord hybrid
                |         shape feature.
                | 
                |          Dim oZ As CATIALength
                |          Set oZ = PointCoord.Z

        :return: Length
        """

        return Length(self.hybrid_shape_point_coord.Z)

    def __repr__(self):
        return f'HybridShapePointCoord(name="{ self.name }")'
