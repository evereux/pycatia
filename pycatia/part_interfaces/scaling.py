#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.in_interfaces.reference import Reference
from pycatia.knowledge_interfaces.real_param import RealParam
from pycatia.part_interfaces.dress_up_shape import DressUpShape


class Scaling(DressUpShape):

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
                |                         PartInterfaces.DressUpShape
                |                             Scaling
                | 
                | Represents the scaling shape.
                | The scaling shape is made up of a scaling reference element, such as a point,
                | and a scaling factor.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.scaling = com_object

    @property
    def factor(self) -> RealParam:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Factor() As RealParam (Read Only)
                | 
                |     Returns the scaling factor.
                | 
                |     Example:
                |         The following example returns in factor the scaling factor of the
                |         scaling firstScaling:
                | 
                |          Set factor = firstScaling.Factor

        :rtype: RealParam
        """

        return RealParam(self.scaling.Factor)

    @property
    def scaling_reference(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property ScalingReference() As Reference
                | 
                |     Returns or sets the scaling reference element. It can be a
                |     point.
                |     To set the property, you can use one of the following Boundary objects:
                |     PlanarFace or Vertex.
                | 
                |     Example:
                |         The following example returns in ref the scaling reference element of
                |         the scaling firstScaling, and then sets it to the created
                |         MyRef:
                | 
                |          Set ref = firstScaling.ScalingSupport
                |          Set MyRef = part.CreateReferenceFromGeometry (Point)
                |          firstScaling.ScalingSupport = MyRef

        :rtype: Reference
        """

        return Reference(self.scaling.ScalingReference)

    @scaling_reference.setter
    def scaling_reference(self, value: Reference):
        """
        :param Reference value:
        """

        self.scaling.ScalingReference = value.com_object

    def __repr__(self):
        return f'Scaling(name="{ self.name }")'
