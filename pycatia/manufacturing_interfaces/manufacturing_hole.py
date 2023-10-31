#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.knowledge_interfaces.length import Length
from pycatia.system_interfaces.any_object import AnyObject


class ManufacturingHole(AnyObject):

    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     ManufacturingHole
                | 
                | Hole Feature in Machining domain.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.manufacturing_hole = com_object

    @property
    def depth(self) -> Length:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Depth() As Length (Read Only)
                | 
                |     Returns the hole depth.
                | 
                |     Returns:
                |         oDepth A CATIALength object controlling the hole depth (@see
                |         CATIALength for more information)
                | 
                |         Example:
                |             The following example returns in holeDepth the depth of hole
                |             firstHole:
                | 
                |              Set holeDepth = firstHole.Depth

        :rtype: Length
        """

        return Length(self.manufacturing_hole.Depth)

    @property
    def diameter(self) -> Length:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Diameter() As Length (Read Only)
                | 
                |     Returns the hole diameter.
                | 
                |     Returns:
                |         oDiameter A CATIALength object controlling the hole diameter (@see
                |         CATIALength for more information)
                | 
                |         Example:
                |             The following example returns in holeDiam the diameter of hole
                |             firstHole:
                | 
                |              Set holeDiam = firstHole.Diameter

        :rtype: Length
        """

        return Length(self.manufacturing_hole.Diameter)

    def get_direction(self, o_x: float, o_y: float, o_z: float) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetDirection(double oX,
                | double oY,
                | double oZ)
                | 
                |     Returns the hole direction with absolute coordinates.
                | 
                |     Returns:
                |         3 doubles: X, Y, Z - direction coordinates
                | 
                |         Example:
                |             The following example returns in X, Y, Z the direction coordinates
                |             of hole firstHole:
                | 
                |              call firstHole.GetDirection(X,Y,Z)

        :param float o_x:
        :param float o_y:
        :param float o_z:
        :rtype: None
        """
        return self.manufacturing_hole.GetDirection(o_x, o_y, o_z)

    def get_origin(self, o_x: float, o_y: float, o_z: float) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetOrigin(double oX,
                | double oY,
                | double oZ)
                | 
                |     Returns the origin point which the hole is anchored to.
                | 
                |     Returns:
                |         3 doubles: X, Y, Z - Hole origin point coordinates
                | 
                |         Example:
                |             The following example returns in X, Y, Z the origin coordinates of
                |             hole firstHole:
                | 
                |              call firstHole.GetOrigin(X,Y,Z)

        :param float o_x:
        :param float o_y:
        :param float o_z:
        :rtype: None
        """
        return self.manufacturing_hole.GetOrigin(o_x, o_y, o_z)

    def __repr__(self):
        return f'ManufacturingHole(name="{ self.name }")'
