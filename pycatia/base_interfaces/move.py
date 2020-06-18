#! /usr/bin/python3.6
# module initially auto generated using V5Automation.chm from CATIA V5 R25

from pycatia.system_interfaces.any_object import AnyObject


class Move(AnyObject):
    """
        .. note::
            CAA V5 Visual Basic help

                | Represents an object associated with any kind of objects which
                | retrieves the corresponding movable object.An object can be moved only
                | if it is independent from other objects. For example, a pad can be
                | moved, and is as such a movable object, while an edge cannot be moved
                | individually. It should be moved with all the objects making up the
                | pad to which it belongs as a whole. In this case, the underlying
                | edge's movable object is the pad.

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.move = com_object
        self.com_object = com_object

    @property
    def movable_object(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | MovableObject
                | o Property MovableObject() As Move
                |
                | Returns the movable object associated with the used object. Example:
                | This example retrieves the myMovableObject from  Move object
                | associated with MyObject.  Dim myMovableObject As Move Set
                | myMovableObject = MyObject.Move.MovableObject


                | Parameters:


        """
        return self.move.MovableObject

    def apply(self, i_transformation_array):
        """
        .. note::
            CAA V5 Visual Basic help

                | Apply
                | o Sub Apply(    CATSafeArrayVariant    iTransformationArray)
                |
                | Applies a move transformation to a movable object.


                | Parameters:
                | TransformationArray
                |    The linear transformation array initialized successively by the
                |    four columns of the transformation matrix.
                |    The first nine components represent the rotation matrix.
                |    The last three components represent the translation vector.


                | Examples:
                |
                | This example applies the transformation (45 degrees-rotation around
                | the x axis and a translation) stored in TransformationArray
                | to the Move object associated with myMovableObject:
                |
                | Dim TransformationArray( 11 )
                | 'Rotation( 45 degrees around the x axis) components
                | TransformationArray( 0 )  = 1.000
                | TransformationArray( 1 )  = 0
                | TransformationArray( 2 )  = 0
                | TransformationArray( 3 )  = 0
                | TransformationArray( 4 )  = 0.707
                | TransformationArray( 5 )  = 0.707
                | TransformationArray( 6 )  = 0
                | TransformationArray( 7 )  = -0.707
                | TransformationArray( 8 )  = 0.707
                | 'Translation Vector (10,20,30)
                | TransformationArray( 9 )  = 10.000
                | TransformationArray( 10 ) = 20.000
                | TransformationArray( 11 ) = 30.000
                | MyMovableObject.Move.Apply TransformationArray
                |
        """

        return self.move.Apply(i_transformation_array)
