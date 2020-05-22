#! /usr/bin/python3.6
# module initially auto generated using V5Automation.chm from CATIA R25 on 2020-05-22 12:54:36.956119

from pycatia.mec_mod_interfaces.hybridshape import HybridShape


class HybridShapeAffinity(HybridShape):
    """
        .. note::
            CAA V5 Visual Basic help

                | Represents the hybrid shape affinity feature object.Role: To access
                | the data of the hybrid shape affinity feature object. This data
                | includes:The reference coordinate system is always a direct one.Use
                | the  CATIAHybridShapeFactory to create a HybridShapeAffinity object.

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_affinity = com_object

    @property
    def axis_first_direction(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | AxisFirstDirection
                | o Property AxisFirstDirection(    ) As
                | 
                | Returns or sets the first direction of the reference
                | coordinate system. Sub-element(s) supported (see object): ,
                | or . 
                |
                | Example:
                | This example retrieves in FirstDir the first
                | direction of the reference coordinate system used by the
                | Affinity hybrid shape feature. Dim FirstDir As Reference Set
                | FirstDir = Affinity.AxisFirstDirection

        :return:
        """
        return self.hybrid_shape_affinity.AxisFirstDirection

    @axis_first_direction.setter
    def axis_first_direction(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_affinity.AxisFirstDirection = value

    @property
    def axis_origin(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | AxisOrigin
                | o Property AxisOrigin(    ) As
                | 
                | Returns or sets the origin of the reference coordinate
                | system. Sub-element(s) supported (see object): . Example:
                | This example retrieves in Origin the origin of the reference
                | coordinate system used by the Affinity hybrid shape feature.
                | Dim Origin As Reference Set Origin = Affinity.AxisOrigin

        :return:
        """
        return self.hybrid_shape_affinity.AxisOrigin

    @axis_origin.setter
    def axis_origin(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_affinity.AxisOrigin = value

    @property
    def axis_plane(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | AxisPlane
                | o Property AxisPlane(    ) As
                | 
                | Returns or sets the reference plane of the reference
                | coordinate system. Sub-element(s) supported (see object): .
                | 
                |
                | Example:
                | This example retrieves in RefPlane the reference
                | plane of the reference coordinate system used by the
                | Affinity hybrid shape feature. Dim RefPlane As Reference Set
                | RefPlane = Affinity.AxisPlane

        :return:
        """
        return self.hybrid_shape_affinity.AxisPlane

    @axis_plane.setter
    def axis_plane(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_affinity.AxisPlane = value

    @property
    def creation_mode(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | CreationMode
                | o Property CreationMode(    ) As
                | 
                | Returns or sets the creation mode(creation or modification).
                | Legal values: True if the result is a creation feature and
                | False if the result is a modification feature. 
                |
                | Example:
                | This
                | example sets that the mode of the hybShpAffinity hybrid
                | shape affinity to creation hybShpAffinity.CreationMode =
                | True

        :return:
        """
        return self.hybrid_shape_affinity.CreationMode

    @creation_mode.setter
    def creation_mode(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_affinity.CreationMode = value

    @property
    def elem_to_transform(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | ElemToTransform
                | o Property ElemToTransform(    ) As
                | 
                | Returns or sets the element to transform using the affinity.
                | 
                |
                | Example:
                | This example retrieves in ElementToTransform the
                | element to transform for the Affinity hybrid shape feature.
                | Dim ElementToTransform As Reference Set ElementToTransform =
                | Affinity.ElemToTransform

        :return:
        """
        return self.hybrid_shape_affinity.ElemToTransform

    @elem_to_transform.setter
    def elem_to_transform(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_affinity.ElemToTransform = value

    @property
    def volume_result(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | VolumeResult
                | o Property VolumeResult(    ) As
                | 
                | Returns or sets the volume result. Legal values: True if the
                | result of affinity is required as volume (option is
                | effective only in case of volumes,requires GSO License) and
                | False if it is needed as surface . 
                |
                | Example:
                | This example
                | sets that the result of the hybShpAffinity hybrid shape
                | affinity is volume. hybShpAffinity.VolumeResult = True

        :return:
        """
        return self.hybrid_shape_affinity.VolumeResult

    @volume_result.setter
    def volume_result(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_affinity.VolumeResult = value

    @property
    def x_ratios(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | XRatios
                | o Property XRatios(    ) As   (Read Only)
                | 
                | Returns the affinity ratio along the X Direction of the
                | reference coordinate system. 
                |
                | Example:
                | This example retrieves
                | in X the ratio of the affinity along the X Direction of the
                | reference coordinate system used by the Affinity hybrid
                | shape feature. Dim X As RealParam Set X = Affinity.XRatios

        :return:
        """
        return self.hybrid_shape_affinity.XRatios

    @property
    def y_ratios(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | YRatios
                | o Property YRatios(    ) As   (Read Only)
                | 
                | Returns the affinity ratio along the Y Direction of the
                | reference coordinate system. 
                |
                | Example:
                | This example retrieves
                | in Y the ratio of the affinity along the Y Direction of the
                | reference coordinate system used by the Affinity hybrid
                | shape feature. Dim Y As RealParam Set Y = Affinity.YRatios

        :return:
        """
        return self.hybrid_shape_affinity.YRatios

    @property
    def z_ratios(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | ZRatios
                | o Property ZRatios(    ) As   (Read Only)
                | 
                | Returns the affinity ratio along the Z Direction of the
                | reference coordinate system. 
                |
                | Example:
                | This example retrieves
                | in Z the ratio of the affinity along the Z Direction of the
                | reference coordinate system used by the Affinity hybrid
                | shape feature. Dim Z As RealParam Set Z = Affinity.ZRatios

        :return:
        """
        return self.hybrid_shape_affinity.ZRatios

    def __repr__(self):
        return f'HybridShapeAffinity()'
