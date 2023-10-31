#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-07-06 14:02:20.222384

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.in_interfaces.reference import Reference
from pycatia.mec_mod_interfaces.hybrid_shape import HybridShape


class HybridShapeExtract(HybridShape):

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
                |                         HybridShapeExtract
                | 
                | Represents the hybrid shape extract feature object.
                | Role: To access the data of the hybrid shape extract feature
                | object.
                | 
                | Use the CATIAHybridShapeFactory to create a HybridShapeExtract
                | object.
                | 
                | See also:
                |     HybridShapeFactory.AddNewExtract
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_extract = com_object

    @property
    def angular_threshold(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property AngularThreshold() As double
                | 
                |     Returns or sets the AngularThreshold.
                | 
                |     Example: This example retrieves the AngularThreshold of the hybShpExtract
                |     in AngularThH.
                | 
                |      Dim AngularThH as double
                |      AngularThH = hybShpExtract.AngularThreshold

        :rtype: float
        """

        return self.hybrid_shape_extract.AngularThreshold

    @angular_threshold.setter
    def angular_threshold(self, value: float):
        """
        :param float value:
        """

        self.hybrid_shape_extract.AngularThreshold = value

    @property
    def angular_threshold_activity(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property AngularThresholdActivity() As boolean
                | 
                |     Returns or sets the AngularThresholdActivity.
                | 
                |     Example: This example retrieves the AngularThresholdActivity of the
                |     hybShpExtract in AngularActivity .
                | 
                |      Dim AngularActivity as boolean 
                |      AngularActivity = hybShpExtract.AngularThresholdActivity

        :rtype: bool
        """

        return self.hybrid_shape_extract.AngularThresholdActivity

    @angular_threshold_activity.setter
    def angular_threshold_activity(self, value: bool):
        """
        :param bool value:
        """

        self.hybrid_shape_extract.AngularThresholdActivity = value

    @property
    def complementary_extract(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property ComplementaryExtract() As boolean
                | 
                |     Returns or sets the ComplementaryExtract checked/unchecked for the extract.

        :rtype: bool
        """

        return self.hybrid_shape_extract.ComplementaryExtract

    @complementary_extract.setter
    def complementary_extract(self, value: bool):
        """
        :param bool value:
        """

        self.hybrid_shape_extract.ComplementaryExtract = value

    @property
    def curvature_threshold(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property CurvatureThreshold() As double
                | 
                |     Returns or sets the CurvatureThreshold.
                | 
                |     Example: This example retrieves the CurvatureThreshold of the hybShpExtract
                |     in CurvatureThH.
                | 
                |      Dim CurvatureThH as double
                |      CurvatureThH = hybShpExtract.CurvatureThreshold

        :rtype: float
        """

        return self.hybrid_shape_extract.CurvatureThreshold

    @curvature_threshold.setter
    def curvature_threshold(self, value: float):
        """
        :param float value:
        """

        self.hybrid_shape_extract.CurvatureThreshold = value

    @property
    def curvature_threshold_activity(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property CurvatureThresholdActivity() As boolean
                | 
                |     Returns or sets the CurvatureThresholdActivity.
                | 
                |     Example: This example retrieves the CurvatureThresholdActivity of the
                |     hybShpExtract in CurvatureActivity .
                | 
                |      Dim CurvatureActivity as boolean 
                |      CurvatureActivity = hybShpExtract.CurvatureThresholdActivity

        :rtype: bool
        """

        return self.hybrid_shape_extract.CurvatureThresholdActivity

    @curvature_threshold_activity.setter
    def curvature_threshold_activity(self, value: bool):
        """
        :param bool value:
        """

        self.hybrid_shape_extract.CurvatureThresholdActivity = value

    @property
    def distance_threshold(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property DistanceThreshold() As double
                | 
                |     Returns or sets the DistanceThreshold.
                | 
                |     Example: This example retrieves the DistanceThreshold of the hybShpExtract
                |     in DistanceThH.
                | 
                |      Dim DistanceThH as double
                |      DistanceThH = hybShpExtract.DistanceThreshold

        :rtype: float
        """

        return self.hybrid_shape_extract.DistanceThreshold

    @distance_threshold.setter
    def distance_threshold(self, value: float):
        """
        :param float value:
        """

        self.hybrid_shape_extract.DistanceThreshold = value

    @property
    def distance_threshold_activity(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property DistanceThresholdActivity() As boolean
                | 
                |     Returns or sets the DistanceThresholdActivity.
                | 
                |     Example: This example retrieves the DistanceThresholdActivity of the
                |     hybShpExtract in DistanceActivity .
                | 
                |      Dim DistanceActivity as boolean 
                |      DistanceActivity = hybShpExtract.DistanceThresholdActivity

        :rtype: bool
        """

        return self.hybrid_shape_extract.DistanceThresholdActivity

    @distance_threshold_activity.setter
    def distance_threshold_activity(self, value: bool):
        """
        :param bool value:
        """

        self.hybrid_shape_extract.DistanceThresholdActivity = value

    @property
    def elem(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Elem() As Reference
                | 
                |     Returns or sets the sub element used as init for the
                |     propagation.
                | 
                |     See also:
                |         HybridShapeFactory

        :rtype: Reference
        """

        return Reference(self.hybrid_shape_extract.Elem)

    @elem.setter
    def elem(self, reference_element: Reference):
        """
        :param Reference reference_element:
        """

        self.hybrid_shape_extract.Elem = reference_element.com_object

    @property
    def is_federated(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property IsFederated() As boolean
                | 
                |     Returns or sets the IsFederated flag checked/unchecked for the extract.

        :rtype: bool
        """

        return self.hybrid_shape_extract.IsFederated

    @is_federated.setter
    def is_federated(self, value: bool):
        """
        :param bool value:
        """

        self.hybrid_shape_extract.IsFederated = value

    @property
    def propagation_type(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property PropagationType() As long
                | 
                |     Returns or sets the type of propagation for the extract.
                |     The propagation types for the extract can have the following
                |     values:
                | 
                |         1 for extraction propagation in point continuity
                |         2 for extraction propagation in tangent continuity
                |         3 for extraction without propagation

        :rtype: int
        """

        return self.hybrid_shape_extract.PropagationType

    @propagation_type.setter
    def propagation_type(self, value: int):
        """
        :param int value:
        """

        self.hybrid_shape_extract.PropagationType = value

    @property
    def support(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Support() As Reference
                | 
                |     Returns or sets the support for the extract.

        :rtype: Reference
        """

        return Reference(self.hybrid_shape_extract.Support)

    @support.setter
    def support(self, reference_support: Reference):
        """
        :param Reference reference_support:
        """

        self.hybrid_shape_extract.Support = reference_support.com_object

    def __repr__(self):
        return f'HybridShapeExtract(name="{ self.name }")'
