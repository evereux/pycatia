#! usr/bin/python3.6
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-09 09:53:18.676780

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.in_interfaces.reference import Reference
from pycatia.knowledge_interfaces.length import Length
from pycatia.knowledge_interfaces.real_param import RealParam
from pycatia.mec_mod_interfaces.hybrid_shape import HybridShape


class HybridShapeBump(HybridShape):

    """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.HybridShape
                |                         HybridShapeBump
                | 
                | The Bump feature : an Bump is made up of a body to process and some Bump parameters.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_bump = com_object

    @property
    def body_to_bump(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property BodyToBump() As Reference
                | 
                |     Returns or sets the element to Bump.

        :return: Reference
        """

        return Reference(self.hybrid_shape_bump.BodyToBump)

    @body_to_bump.setter
    def body_to_bump(self, value):
        """
        :param Reference value:
        """

        self.hybrid_shape_bump.BodyToBump = value

    @property
    def center_tension(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property CenterTension() As RealParam
                | 
                |     Returns or sets the tension center parameter.

        :return: RealParam
        """

        return RealParam(self.hybrid_shape_bump.CenterTension)

    @center_tension.setter
    def center_tension(self, value):
        """
        :param RealParam value:
        """

        self.hybrid_shape_bump.CenterTension = value

    @property
    def continuity_type(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property ContinuityType() As long
                | 
                |     Returns or sets the continuity type ..
                |     Legal values: the continuity type is either
                | 
                |      PointContinuity      =0
                |      TangentContinuity    =1 
                |      CurvatureContinuity  =2

        :return: int
        """

        return self.hybrid_shape_bump.ContinuityType

    @continuity_type.setter
    def continuity_type(self, value):
        """
        :param int value:
        """

        self.hybrid_shape_bump.ContinuityType = value

    @property
    def deformation_center(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property DeformationCenter() As Reference
                | 
                |     Returns or sets the Deformation Center.

        :return: Reference
        """

        return Reference(self.hybrid_shape_bump.DeformationCenter)

    @deformation_center.setter
    def deformation_center(self, value):
        """
        :param Reference value:
        """

        self.hybrid_shape_bump.DeformationCenter = value

    @property
    def deformation_dir(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property DeformationDir() As Reference
                | 
                |     Returns or sets the Deformation Direction.

        :return: Reference
        """

        return Reference(self.hybrid_shape_bump.DeformationDir)

    @deformation_dir.setter
    def deformation_dir(self, value):
        """
        :param Reference value:
        """

        self.hybrid_shape_bump.DeformationDir = value

    @property
    def deformation_dist(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property DeformationDist() As Length
                | 
                |     Returns the translate distance (CATIA Parameter).
                |     Note: Distance value is set or retrieve trough a Literaql
                |     parameter
                |     Parameters are value are given in the Part Unit
                |     Example : if Part Unit for dimensions is mm: for 1 mmm, oDefDist.Value will return 1.000

        :return: Length
        """

        return Length(self.hybrid_shape_bump.DeformationDist)

    @deformation_dist.setter
    def deformation_dist(self, value):
        """
        :param Length value:
        """

        self.hybrid_shape_bump.DeformationDist = value

    @property
    def deformation_dist_value(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property DeformationDistValue() As double
                | 
                |     Returns or sets the Deformation distance (double) .
                |     Note: Distance value is expressed in MKS = Meters
                |     Example to set up 1mm , use .001

        :return: float
        """

        return self.hybrid_shape_bump.DeformationDistValue

    @deformation_dist_value.setter
    def deformation_dist_value(self, value):
        """
        :param float value:
        """

        self.hybrid_shape_bump.DeformationDistValue = value

    @property
    def limit_curve(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property LimitCurve() As Reference
                | 
                |     Returns or sets the limit curve.

        :return: Reference
        """

        return Reference(self.hybrid_shape_bump.LimitCurve)

    @limit_curve.setter
    def limit_curve(self, value):
        """
        :param Reference value:
        """

        self.hybrid_shape_bump.LimitCurve = value

    @property
    def projection_dir(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property ProjectionDir() As Reference
                | 
                |     Returns or sets the limit curve.

        :return: Reference
        """

        return Reference(self.hybrid_shape_bump.ProjectionDir)

    @projection_dir.setter
    def projection_dir(self, value):
        """
        :param Reference value:
        """

        self.hybrid_shape_bump.ProjectionDir = value

    def __repr__(self):
        return f'HybridShapeBump(name="{ self.name }")'
