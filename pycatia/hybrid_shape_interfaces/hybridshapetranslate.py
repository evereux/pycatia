#! /usr/bin/python3.6
# module initially auto generated using V5Automation.chm from CATIA R25 on 2020-05-22 12:54:36.956119

from pycatia.mec_mod_interfaces.hybridshape import HybridShape


class HybridShapeTranslate(HybridShape):
    """
        .. note::
            CAA V5 Visual Basic help

                | Represents the hybrid shape translate feature object.Role: To access
                | the data of the hybrid shape translate feature object. This data
                | includes:Use the CATIAHybridShapeFactory to create HybridShapeFeature
                | object.

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_translate = com_object     

    @property
    def coord_x_value(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | CoordXValue
                | o Property CoordXValue(    ) As
                | 
                | Returns or sets the translate X coordinate value.

        :return:
        """
        return self.hybrid_shape_translate.CoordXValue

    @coord_x_value.setter
    def coord_x_value(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_translate.CoordXValue = value 

    @property
    def coord_y_value(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | CoordYValue
                | o Property CoordYValue(    ) As
                | 
                | Returns or sets the translate Y coordinate value.

        :return:
        """
        return self.hybrid_shape_translate.CoordYValue

    @coord_y_value.setter
    def coord_y_value(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_translate.CoordYValue = value 

    @property
    def coord_z_value(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | CoordZValue
                | o Property CoordZValue(    ) As
                | 
                | Returns or sets the translate Z coordinate value.

        :return:
        """
        return self.hybrid_shape_translate.CoordZValue

    @coord_z_value.setter
    def coord_z_value(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_translate.CoordZValue = value 

    @property
    def direction(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Direction
                | o Property Direction(    ) As
                | 
                | Returns or sets the translate direction. Example This
                | example retrieves in Dir the translation direction for the
                | Translate hybrid shape feature. Dim Dir As
                | CATIAHybridShapeDirection Set Dir=Translate.Direction

        :return:
        """
        return self.hybrid_shape_translate.Direction

    @direction.setter
    def direction(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_translate.Direction = value 

    @property
    def distance(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Distance
                | o Property Distance(    ) As   (Read Only)
                | 
                | Returns the translate distance.

        :return:
        """
        return self.hybrid_shape_translate.Distance

    @property
    def distance_value(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | DistanceValue
                | o Property DistanceValue(    ) As
                | 
                | Returns or sets the translate distance value. Example This
                | example retrieves in DistVal the translation distance value
                | for the Translate hybrid shape feature. Dim DistVal As
                | double Set DistVal =Translate.DistanceValue

        :return:
        """
        return self.hybrid_shape_translate.DistanceValue

    @distance_value.setter
    def distance_value(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_translate.DistanceValue = value 

    @property
    def elem_to_translate(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | ElemToTranslate
                | o Property ElemToTranslate(    ) As
                | 
                | Returns or sets the element to translate. Example This
                | example retrieves in Element the element to be translated
                | for the Translate hybrid shape feature. Dim Element As
                | Reference Set Element=Translate.ElemToTranslate

        :return:
        """
        return self.hybrid_shape_translate.ElemToTranslate

    @elem_to_translate.setter
    def elem_to_translate(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_translate.ElemToTranslate = value 

    @property
    def first_point(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | FirstPoint
                | o Property FirstPoint(    ) As
                | 
                | Returns or sets the first point defining the translation.

        :return:
        """
        return self.hybrid_shape_translate.FirstPoint

    @first_point.setter
    def first_point(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_translate.FirstPoint = value 

    @property
    def ref_axis_system(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | RefAxisSystem
                | o Property RefAxisSystem(    ) As
                | 
                | Returns or Sets the reference Axis System for Translate
                | feature. This data is not mandatory, if element is null, the
                | absolute axis system is taken. When an element is given, X,
                | Y and Z are considered in this Axis system. 
                |
                | Example:
                | This
                | example retrieves in oRefAxis the reference Axis System for
                | Translate feature. Dim oRefAxis As CATIAReference Set
                | oRefAxis = Translate.RefAxisSystem

        :return:
        """
        return self.hybrid_shape_translate.RefAxisSystem

    @property
    def second_point(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | SecondPoint
                | o Property SecondPoint(    ) As
                | 
                | Returns or sets the second point defining the translation.

        :return:
        """
        return self.hybrid_shape_translate.SecondPoint

    @second_point.setter
    def second_point(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_translate.SecondPoint = value 

    @property
    def vector_type(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | VectorType
                | o Property VectorType(    ) As
                | 
                | Returns or sets the way the translation vector is defined.
                | 0= Direction + distance 1= point + points 2= coordinates 3=
                | Unknown type

        :return:
        """
        return self.hybrid_shape_translate.VectorType

    @vector_type.setter
    def vector_type(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_translate.VectorType = value 

    @property
    def volume_result(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | VolumeResult
                | o Property VolumeResult(    ) As
                | 
                | Returns or sets the volume result. Legal values: True if the
                | result of translation is required as volume (option is
                | effective only in case of volumes,requires GSO License) and
                | False if it is needed as surface . 
                |
                | Example:
                | This example
                | sets that the result of the hybShpTranslate hybrid shape
                | translate is volume. hybShpTranslate.VolumeResult = True

        :return:
        """
        return self.hybrid_shape_translate.VolumeResult

    @volume_result.setter
    def volume_result(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_translate.VolumeResult = value 

    def get_creation_mode(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetCreationMode
                | o Func GetCreationMode(    ) As
                | 
                | Gets the creation mode. Legal values: 0
                | CATGSMTransfoModeUnset. Default behavior: creation mode by
                | default for all features, modification mode for axis system
                | 1 CATGSMTransfoModeCreation. Creation mode. 2
                | CATGSMTransfoModeModification. Modification mode.
                |
                | Parameters:


        :return:
        """
        return self.hybrid_shape_translate.GetCreationMode()

    def set_creation_mode(self, i_creation):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetCreationMode
                | o Sub SetCreationMode(        iCreation)
                | 
                | Sets the creation mode(creation or modification). Legal
                | values: True if the result is a creation feature and False
                | if the result is a modification feature. 
                |
                | Example:
                | This
                | example sets that the mode of the hybShpTranslate hybrid
                | shape translate to creation hybShpTranslate.SetCreationMode
                | True
                |
                | Parameters:


        :param i_creation:
        :return:
        """
        return self.hybrid_shape_translate.SetCreationMode(i_creation)

    def __repr__(self):
        return f'HybridShapeTranslate()'
