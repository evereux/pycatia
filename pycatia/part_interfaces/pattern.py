#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.knowledge_interfaces.angle import Angle
from pycatia.part_interfaces.transformation_shape import TransformationShape
from pycatia.system_interfaces.any_object import AnyObject


class Pattern(TransformationShape):

    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.Shape
                |                         PartInterfaces.TransformationShape
                |                             Pattern
                | 
                | Represents the pattern shape.
                | It is the base object for rectangular and circular patterns. A pattern shape is
                | a set of copies of the same shape. The copy is done according to linear and
                | angular repartitions.
                | 
                | See also:
                |     CircPattern, RectPattern, Repartition, LinearRepartition,
                |     AngularRepartition
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.pattern = com_object

    @property
    def item_to_copy(self) -> AnyObject:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property ItemToCopy() As AnyObject
                | 
                |     Returns or sets the shape to be copied.
                | 
                |     Example:
                |         The following example returns in shape the copied shape of the pattern
                |         firstPattern, and then sets it to pad1:
                | 
                |          Set shape = firstPattern.ItemToCopy
                |          firstPattern.ItemToCopy = pad1

        :rtype: AnyObject
        """

        return AnyObject(self.pattern.ItemToCopy)

    @item_to_copy.setter
    def item_to_copy(self, value: AnyObject):
        """
        :param AnyObject value:
        """

        self.pattern.ItemToCopy = value

    @property
    def rotation_angle(self) -> Angle:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property RotationAngle() As Angle (Read Only)
                | 
                |     Returns the pattern global rotation angle. The rotation is applied to the
                |     whole pattern, but not to the shapes themselves. The shape to be copied is used
                |     as the rotation center.
                | 
                |     Example:
                |         The following example returns in globAng the rotation of pattern
                |         firstPattern:
                | 
                |          Set globAng = firstPattern.RotationAngle

        :rtype: Angle
        """

        return Angle(self.pattern.RotationAngle)

    def activate_position(self, i_pos_u: int, i_pos_v: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub ActivatePosition(long iPosU,
                | long iPosV)
                | 
                |     Allows user to activate an instance of the pattern.
                | 
                |     Parameters:
                | 
                |         iPosU
                |             The position of the instance in the U direction 
                |         iPosV
                |             The position of the instance in the V direction

        :param int i_pos_u:
        :param int i_pos_v:
        :rtype: None
        """
        return self.pattern.ActivatePosition(i_pos_u, i_pos_v)

    def desactivate_position(self, i_pos_u: int, i_pos_v: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub DesactivatePosition(long iPosU,
                | long iPosV)
                | 
                |     Allows user to desactivate an instance of the pattern.
                | 
                |     Parameters:
                | 
                |         iPosU
                |             The position of the instance in the U direction 
                |         iPosV
                |             The position of the instance in the V direction

        :param int i_pos_u:
        :param int i_pos_v:
        :rtype: None
        """
        return self.pattern.DesactivatePosition(i_pos_u, i_pos_v)

    def __repr__(self):
        return f'Pattern(name="{ self.name }")'
