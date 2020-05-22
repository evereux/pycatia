#! /usr/bin/python3.6
# module initially auto generated using V5Automation.chm from CATIA R25 on 2020-05-22 12:54:36.956119

from pycatia.mec_mod_interfaces.hybridshape import HybridShape


class HybridShapeExtract(HybridShape):
    """
        .. note::
            CAA V5 Visual Basic help

                | Represents the hybrid shape extract feature object.Role: To access the
                | data of the hybrid shape extract feature object.Use the
                | CATIAHybridShapeFactory to create a HybridShapeExtract object.

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_extract = com_object     

    @property
    def angular_threshold(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | AngularThreshold
                | o Property AngularThreshold(    ) As
                | 
                | Returns or sets the AngularThreshold. 
                |
                | Example:
                | This example
                | retrieves the AngularThreshold of the hybShpExtract in
                | AngularThH. Dim AngularThH as double AngularThH =
                | hybShpExtract.AngularThreshold o Property
                | AngularThresholdActivity() As Returns or sets the
                | AngularThresholdActivity. 
                |
                | Example:
                | This example retrieves
                | the AngularThresholdActivity of the hybShpExtract in
                | AngularActivity . Dim AngularActivity as boolean
                | AngularActivity = hybShpExtract.AngularThresholdActivity o
                | Property ComplementaryExtract() As Returns or sets the
                | ComplementaryExtract checked/unchecked for the extract. o
                | Property CurvatureThreshold() As Returns or sets the
                | CurvatureThreshold. 
                |
                | Example:
                | This example retrieves the
                | CurvatureThreshold of the hybShpExtract in CurvatureThH. Dim
                | CurvatureThH as double CurvatureThH =
                | hybShpExtract.CurvatureThreshold o Property
                | CurvatureThresholdActivity() As Returns or sets the
                | CurvatureThresholdActivity. 
                |
                | Example:
                | This example retrieves
                | the CurvatureThresholdActivity of the hybShpExtract in
                | CurvatureActivity . Dim CurvatureActivity as boolean
                | CurvatureActivity = hybShpExtract.CurvatureThresholdActivity
                | o Property DistanceThreshold() As Returns or sets the
                | DistanceThreshold. 
                |
                | Example:
                | This example retrieves the
                | DistanceThreshold of the hybShpExtract in DistanceThH. Dim
                | DistanceThH as double DistanceThH =
                | hybShpExtract.DistanceThreshold o Property
                | DistanceThresholdActivity() As Returns or sets the
                | DistanceThresholdActivity. 
                |
                | Example:
                | This example retrieves
                | the DistanceThresholdActivity of the hybShpExtract in
                | DistanceActivity . Dim DistanceActivity as boolean
                | DistanceActivity = hybShpExtract.DistanceThresholdActivity o
                | Property Elem() As Returns or sets the sub element used as
                | init for the propagation. See also: o Property IsFederated()
                | As Returns or sets the IsFederated flag checked/unchecked
                | for the extract. o Property PropagationType() As Returns or
                | sets the type of propagation for the extract. The
                | propagation types for the extract can have the following
                | values: 1 for extraction propagation in point continuity 2
                | for extraction propagation in tangent continuity 3 for
                | extraction without propagation o Property Support() As
                | Returns or sets the support for the extract. Copyright ©
                | 1999-2011, Dassault Systèmes. All rights reserved.

        :return:
        """
        return self.hybrid_shape_extract.AngularThreshold

    @angular_threshold.setter
    def angular_threshold(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_extract.AngularThreshold = value 

    @property
    def angular_threshold_activity(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | AngularThresholdActivity
                | o Property AngularThresholdActivity(    ) As
                | 
                | Returns or sets the AngularThresholdActivity. 
                |
                | Example:
                | This
                | example retrieves the AngularThresholdActivity of the
                | hybShpExtract in AngularActivity . Dim AngularActivity as
                | boolean AngularActivity =
                | hybShpExtract.AngularThresholdActivity o Property
                | ComplementaryExtract() As Returns or sets the
                | ComplementaryExtract checked/unchecked for the extract. o
                | Property CurvatureThreshold() As Returns or sets the
                | CurvatureThreshold. 
                |
                | Example:
                | This example retrieves the
                | CurvatureThreshold of the hybShpExtract in CurvatureThH. Dim
                | CurvatureThH as double CurvatureThH =
                | hybShpExtract.CurvatureThreshold o Property
                | CurvatureThresholdActivity() As Returns or sets the
                | CurvatureThresholdActivity. 
                |
                | Example:
                | This example retrieves
                | the CurvatureThresholdActivity of the hybShpExtract in
                | CurvatureActivity . Dim CurvatureActivity as boolean
                | CurvatureActivity = hybShpExtract.CurvatureThresholdActivity
                | o Property DistanceThreshold() As Returns or sets the
                | DistanceThreshold. 
                |
                | Example:
                | This example retrieves the
                | DistanceThreshold of the hybShpExtract in DistanceThH. Dim
                | DistanceThH as double DistanceThH =
                | hybShpExtract.DistanceThreshold o Property
                | DistanceThresholdActivity() As Returns or sets the
                | DistanceThresholdActivity. 
                |
                | Example:
                | This example retrieves
                | the DistanceThresholdActivity of the hybShpExtract in
                | DistanceActivity . Dim DistanceActivity as boolean
                | DistanceActivity = hybShpExtract.DistanceThresholdActivity o
                | Property Elem() As Returns or sets the sub element used as
                | init for the propagation. See also: o Property IsFederated()
                | As Returns or sets the IsFederated flag checked/unchecked
                | for the extract. o Property PropagationType() As Returns or
                | sets the type of propagation for the extract. The
                | propagation types for the extract can have the following
                | values: 1 for extraction propagation in point continuity 2
                | for extraction propagation in tangent continuity 3 for
                | extraction without propagation o Property Support() As
                | Returns or sets the support for the extract. Copyright ©
                | 1999-2011, Dassault Systèmes. All rights reserved.

        :return:
        """
        return self.hybrid_shape_extract.AngularThresholdActivity

    @angular_threshold_activity.setter
    def angular_threshold_activity(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_extract.AngularThresholdActivity = value 

    @property
    def complementary_extract(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | ComplementaryExtract
                | o Property ComplementaryExtract(    ) As
                | 
                | Returns or sets the ComplementaryExtract checked/unchecked
                | for the extract.

        :return:
        """
        return self.hybrid_shape_extract.ComplementaryExtract

    @complementary_extract.setter
    def complementary_extract(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_extract.ComplementaryExtract = value 

    @property
    def curvature_threshold(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | CurvatureThreshold
                | o Property CurvatureThreshold(    ) As
                | 
                | Returns or sets the CurvatureThreshold. 
                |
                | Example:
                | This
                | example retrieves the CurvatureThreshold of the
                | hybShpExtract in CurvatureThH. Dim CurvatureThH as double
                | CurvatureThH = hybShpExtract.CurvatureThreshold o Property
                | CurvatureThresholdActivity() As Returns or sets the
                | CurvatureThresholdActivity. 
                |
                | Example:
                | This example retrieves
                | the CurvatureThresholdActivity of the hybShpExtract in
                | CurvatureActivity . Dim CurvatureActivity as boolean
                | CurvatureActivity = hybShpExtract.CurvatureThresholdActivity
                | o Property DistanceThreshold() As Returns or sets the
                | DistanceThreshold. 
                |
                | Example:
                | This example retrieves the
                | DistanceThreshold of the hybShpExtract in DistanceThH. Dim
                | DistanceThH as double DistanceThH =
                | hybShpExtract.DistanceThreshold o Property
                | DistanceThresholdActivity() As Returns or sets the
                | DistanceThresholdActivity. 
                |
                | Example:
                | This example retrieves
                | the DistanceThresholdActivity of the hybShpExtract in
                | DistanceActivity . Dim DistanceActivity as boolean
                | DistanceActivity = hybShpExtract.DistanceThresholdActivity o
                | Property Elem() As Returns or sets the sub element used as
                | init for the propagation. See also: o Property IsFederated()
                | As Returns or sets the IsFederated flag checked/unchecked
                | for the extract. o Property PropagationType() As Returns or
                | sets the type of propagation for the extract. The
                | propagation types for the extract can have the following
                | values: 1 for extraction propagation in point continuity 2
                | for extraction propagation in tangent continuity 3 for
                | extraction without propagation o Property Support() As
                | Returns or sets the support for the extract. Copyright ©
                | 1999-2011, Dassault Systèmes. All rights reserved.

        :return:
        """
        return self.hybrid_shape_extract.CurvatureThreshold

    @curvature_threshold.setter
    def curvature_threshold(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_extract.CurvatureThreshold = value 

    @property
    def curvature_threshold_activity(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | CurvatureThresholdActivity
                | o Property CurvatureThresholdActivity(    ) As
                | 
                | Returns or sets the CurvatureThresholdActivity. Example:
                | This example retrieves the CurvatureThresholdActivity of the
                | hybShpExtract in CurvatureActivity . Dim CurvatureActivity
                | as boolean CurvatureActivity =
                | hybShpExtract.CurvatureThresholdActivity o Property
                | DistanceThreshold() As Returns or sets the
                | DistanceThreshold. 
                |
                | Example:
                | This example retrieves the
                | DistanceThreshold of the hybShpExtract in DistanceThH. Dim
                | DistanceThH as double DistanceThH =
                | hybShpExtract.DistanceThreshold o Property
                | DistanceThresholdActivity() As Returns or sets the
                | DistanceThresholdActivity. 
                |
                | Example:
                | This example retrieves
                | the DistanceThresholdActivity of the hybShpExtract in
                | DistanceActivity . Dim DistanceActivity as boolean
                | DistanceActivity = hybShpExtract.DistanceThresholdActivity o
                | Property Elem() As Returns or sets the sub element used as
                | init for the propagation. See also: o Property IsFederated()
                | As Returns or sets the IsFederated flag checked/unchecked
                | for the extract. o Property PropagationType() As Returns or
                | sets the type of propagation for the extract. The
                | propagation types for the extract can have the following
                | values: 1 for extraction propagation in point continuity 2
                | for extraction propagation in tangent continuity 3 for
                | extraction without propagation o Property Support() As
                | Returns or sets the support for the extract. Copyright ©
                | 1999-2011, Dassault Systèmes. All rights reserved.

        :return:
        """
        return self.hybrid_shape_extract.CurvatureThresholdActivity

    @curvature_threshold_activity.setter
    def curvature_threshold_activity(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_extract.CurvatureThresholdActivity = value 

    @property
    def distance_threshold(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | DistanceThreshold
                | o Property DistanceThreshold(    ) As
                | 
                | Returns or sets the DistanceThreshold. 
                |
                | Example:
                | This example
                | retrieves the DistanceThreshold of the hybShpExtract in
                | DistanceThH. Dim DistanceThH as double DistanceThH =
                | hybShpExtract.DistanceThreshold o Property
                | DistanceThresholdActivity() As Returns or sets the
                | DistanceThresholdActivity. 
                |
                | Example:
                | This example retrieves
                | the DistanceThresholdActivity of the hybShpExtract in
                | DistanceActivity . Dim DistanceActivity as boolean
                | DistanceActivity = hybShpExtract.DistanceThresholdActivity o
                | Property Elem() As Returns or sets the sub element used as
                | init for the propagation. See also: o Property IsFederated()
                | As Returns or sets the IsFederated flag checked/unchecked
                | for the extract. o Property PropagationType() As Returns or
                | sets the type of propagation for the extract. The
                | propagation types for the extract can have the following
                | values: 1 for extraction propagation in point continuity 2
                | for extraction propagation in tangent continuity 3 for
                | extraction without propagation o Property Support() As
                | Returns or sets the support for the extract. Copyright ©
                | 1999-2011, Dassault Systèmes. All rights reserved.

        :return:
        """
        return self.hybrid_shape_extract.DistanceThreshold

    @distance_threshold.setter
    def distance_threshold(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_extract.DistanceThreshold = value 

    @property
    def distance_threshold_activity(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | DistanceThresholdActivity
                | o Property DistanceThresholdActivity(    ) As
                | 
                | Returns or sets the DistanceThresholdActivity. 
                |
                | Example:
                | This
                | example retrieves the DistanceThresholdActivity of the
                | hybShpExtract in DistanceActivity . Dim DistanceActivity as
                | boolean DistanceActivity =
                | hybShpExtract.DistanceThresholdActivity o Property Elem() As
                | Returns or sets the sub element used as init for the
                | propagation. See also: o Property IsFederated() As Returns
                | or sets the IsFederated flag checked/unchecked for the
                | extract. o Property PropagationType() As Returns or sets the
                | type of propagation for the extract. The propagation types
                | for the extract can have the following values: 1 for
                | extraction propagation in point continuity 2 for extraction
                | propagation in tangent continuity 3 for extraction without
                | propagation o Property Support() As Returns or sets the
                | support for the extract. Copyright © 1999-2011, Dassault
                | Systèmes. All rights reserved.

        :return:
        """
        return self.hybrid_shape_extract.DistanceThresholdActivity

    @distance_threshold_activity.setter
    def distance_threshold_activity(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_extract.DistanceThresholdActivity = value 

    @property
    def elem(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Elem
                | o Property Elem(    ) As
                | 
                | Returns or sets the sub element used as init for the
                | propagation. See also:

        :return:
        """
        return self.hybrid_shape_extract.Elem

    @elem.setter
    def elem(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_extract.Elem = value 

    @property
    def is_federated(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | IsFederated
                | o Property IsFederated(    ) As
                | 
                | Returns or sets the IsFederated flag checked/unchecked for
                | the extract.

        :return:
        """
        return self.hybrid_shape_extract.IsFederated

    @is_federated.setter
    def is_federated(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_extract.IsFederated = value 

    @property
    def propagation_type(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | PropagationType
                | o Property PropagationType(    ) As
                | 
                | Returns or sets the type of propagation for the extract. The
                | propagation types for the extract can have the following
                | values: 1 for extraction propagation in point continuity 2
                | for extraction propagation in tangent continuity 3 for
                | extraction without propagation

        :return:
        """
        return self.hybrid_shape_extract.PropagationType

    @propagation_type.setter
    def propagation_type(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_extract.PropagationType = value 

    @property
    def support(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Support
                | o Property Support(    ) As
                | 
                | Returns or sets the support for the extract.

        :return:
        """
        return self.hybrid_shape_extract.Support

    @support.setter
    def support(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_extract.Support = value 

    def __repr__(self):
        return f'HybridShapeExtract()'
