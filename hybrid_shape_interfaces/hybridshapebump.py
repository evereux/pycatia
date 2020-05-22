#! /usr/bin/python3.6
# module initially auto generated using V5Automation.chm from CATIA R25 on 2020-05-22 12:54:36.956119

from pycatia.mec_mod_interfaces.hybridshape import HybridShape


class HybridShapeBump(HybridShape):
    """
        .. note::
            CAA V5 Visual Basic help

                | The Bump feature : an Bump is made up of a body to process and some
                | Bump parameters.

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_bump = com_object

    @property
    def body_to_bump(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | BodyToBump
                | o Property BodyToBump(    ) As
                | 
                | Returns or sets the element to Bump.

        :return:
        """
        return self.hybrid_shape_bump.BodyToBump

    @body_to_bump.setter
    def body_to_bump(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_bump.BodyToBump = value

    @property
    def center_tension(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | CenterTension
                | o Property CenterTension(    ) As
                | 
                | Returns or sets the tensuion center parameter.

        :return:
        """
        return self.hybrid_shape_bump.CenterTension

    @center_tension.setter
    def center_tension(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_bump.CenterTension = value

    @property
    def continuity_type(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | ContinuityType
                | o Property ContinuityType(    ) As
                | 
                | Returns or sets the continuity type .. Legal values: the
                | continuity type is either PointContinuity =0
                | TangentContinuity =1 CurvatureContinuity =2

        :return:
        """
        return self.hybrid_shape_bump.ContinuityType

    @continuity_type.setter
    def continuity_type(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_bump.ContinuityType = value

    @property
    def deformation_center(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | DeformationCenter
                | o Property DeformationCenter(    ) As
                | 
                | Returns or sets the Deformation Center.

        :return:
        """
        return self.hybrid_shape_bump.DeformationCenter

    @deformation_center.setter
    def deformation_center(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_bump.DeformationCenter = value

    @property
    def deformation_dir(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | DeformationDir
                | o Property DeformationDir(    ) As
                | 
                | Returns or sets the Deformation Direction.

        :return:
        """
        return self.hybrid_shape_bump.DeformationDir

    @deformation_dir.setter
    def deformation_dir(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_bump.DeformationDir = value

    @property
    def deformation_dist(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | DeformationDist
                | o Property DeformationDist(    ) As
                | 
                | Returns the translate distance (CATIA Parameter). Note:
                | Distance value is seted or retrieve trough a Literaql
                | parameter Parameters are value are given in the Part Unit
                | Example : if Part Unit for dimensions is mm: for 1 mmm,
                | oDefDist.Value will return 1.000

        :return:
        """
        return self.hybrid_shape_bump.DeformationDist

    @property
    def deformation_dist_value(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | DeformationDistValue
                | o Property DeformationDistValue(    ) As
                | 
                | Returns or sets the Deformation distance (double) . Note:
                | Distance value is expressed in MKS = Meters Example to set
                | up 1mm , use .001

        :return:
        """
        return self.hybrid_shape_bump.DeformationDistValue

    @deformation_dist_value.setter
    def deformation_dist_value(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_bump.DeformationDistValue = value

    @property
    def limit_curve(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | LimitCurve
                | o Property LimitCurve(    ) As
                | 
                | Returns or sets the limit curve.

        :return:
        """
        return self.hybrid_shape_bump.LimitCurve

    @limit_curve.setter
    def limit_curve(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_bump.LimitCurve = value

    @property
    def projection_dir(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | ProjectionDir
                | o Property ProjectionDir(    ) As
                | 
                | Returns or sets the limit curve.

        :return:
        """
        return self.hybrid_shape_bump.ProjectionDir

    @projection_dir.setter
    def projection_dir(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_bump.ProjectionDir = value

    def __repr__(self):
        return f'HybridShapeBump()'
