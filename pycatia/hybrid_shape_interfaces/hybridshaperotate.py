#! /usr/bin/python3.6
# module initially auto generated using V5Automation.chm from CATIA R25 on 2020-05-22 12:54:36.956119

from pycatia.mec_mod_interfaces.hybridshape import HybridShape


class HybridShapeRotate(HybridShape):
    """
        .. note::
            CAA V5 Visual Basic help

                | Represents the hybrid shape rotate feature object.Role: To access the
                | data of the hybrid shape rotate feature object. This data includes:

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_rotate = com_object     

    @property
    def angle(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Angle
                | o Property Angle(    ) As   (Read Only)
                | 
                | Returns the rotation angle.

        :return:
        """
        return self.hybrid_shape_rotate.Angle

    @property
    def angle_value(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | AngleValue
                | o Property AngleValue(    ) As
                | 
                | Returns or sets the rotation angle value. 
                |
                | Example:
                | This
                | example retrieves in AngleValue the angle value for the
                | Rotate hybrid shape feature. Dim AngleValue As double Set
                | AngleValue = Rotate.AngleValue

        :return:
        """
        return self.hybrid_shape_rotate.AngleValue

    @angle_value.setter
    def angle_value(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_rotate.AngleValue = value 

    @property
    def axis(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Axis
                | o Property Axis(    ) As
                | 
                | Returns or sets the rotation axis. Sub-element(s) supported
                | (see object): . 
                |
                | Example:
                | This example retrieves in
                | RotationAxis the rotation axis for the Rotate hybrid shape
                | feature. Dim RotationAxis As Reference Set RotationAxis =
                | Rotate.Axis

        :return:
        """
        return self.hybrid_shape_rotate.Axis

    @axis.setter
    def axis(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_rotate.Axis = value 

    @property
    def elem_to_rotate(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | ElemToRotate
                | o Property ElemToRotate(    ) As
                | 
                | Retuns or sets the element to be rotated. 
                |
                | Example:
                | This
                | example retrieves in Elem the element to be rotated for the
                | Rotate hybrid shape feature. Dim Elem As Reference Set Elem
                | = Rotate.ElemToRotate

        :return:
        """
        return self.hybrid_shape_rotate.ElemToRotate

    @property
    def first_element(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | FirstElement
                | o Property FirstElement(    ) As
                | 
                | Returns or sets the first element defining the rotation
                | angle.

        :return:
        """
        return self.hybrid_shape_rotate.FirstElement

    @first_element.setter
    def first_element(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_rotate.FirstElement = value 

    @property
    def first_point(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | FirstPoint
                | o Property FirstPoint(    ) As
                | 
                | Returns or sets the first point defining the rotation.

        :return:
        """
        return self.hybrid_shape_rotate.FirstPoint

    @first_point.setter
    def first_point(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_rotate.FirstPoint = value 

    @property
    def orientation_of_first_element(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | OrientationOfFirstElement
                | o Property OrientationOfFirstElement(    ) As
                | 
                | Returns or sets the orientation of the first element
                | defining the rotation angle. This applies in case of line or
                | plane element.

        :return:
        """
        return self.hybrid_shape_rotate.OrientationOfFirstElement

    @orientation_of_first_element.setter
    def orientation_of_first_element(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_rotate.OrientationOfFirstElement = value 

    @property
    def orientation_of_second_element(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | OrientationOfSecondElement
                | o Property OrientationOfSecondElement(    ) As
                | 
                | Returns or sets the orientation of the second element
                | defining the rotation angle. This applies in case of line or
                | plane element.

        :return:
        """
        return self.hybrid_shape_rotate.OrientationOfSecondElement

    @orientation_of_second_element.setter
    def orientation_of_second_element(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_rotate.OrientationOfSecondElement = value 

    @property
    def rotation_type(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | RotationType
                | o Property RotationType(    ) As
                | 
                | Returns or sets the type of the rotation definition. 0= Axis
                | + angle 1= Axis + two elements 2= Three Points 3= Unknown
                | type

        :return:
        """
        return self.hybrid_shape_rotate.RotationType

    @rotation_type.setter
    def rotation_type(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_rotate.RotationType = value 

    @property
    def second_element(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | SecondElement
                | o Property SecondElement(    ) As
                | 
                | Returns or sets the second element defining the rotation
                | angle.

        :return:
        """
        return self.hybrid_shape_rotate.SecondElement

    @second_element.setter
    def second_element(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_rotate.SecondElement = value 

    @property
    def second_point(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | SecondPoint
                | o Property SecondPoint(    ) As
                | 
                | Returns or sets the second point defining the rotation.

        :return:
        """
        return self.hybrid_shape_rotate.SecondPoint

    @second_point.setter
    def second_point(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_rotate.SecondPoint = value 

    @property
    def third_point(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | ThirdPoint
                | o Property ThirdPoint(    ) As
                | 
                | Returns or sets the third point defining the rotation.

        :return:
        """
        return self.hybrid_shape_rotate.ThirdPoint

    @third_point.setter
    def third_point(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_rotate.ThirdPoint = value 

    @property
    def volume_result(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | VolumeResult
                | o Property VolumeResult(    ) As
                | 
                | Returns or sets the volume result. Legal values: True if the
                | result of Rotate is required as volume (option is effective
                | only in case of volumes,requires GSO License) and False if
                | it is needed as surface . 
                |
                | Example:
                | This example sets that
                | the result of the hybShpRotate hybrid shape rotate is
                | volume. hybShpRotate.VolumeResult = True

        :return:
        """
        return self.hybrid_shape_rotate.VolumeResult

    @volume_result.setter
    def volume_result(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_rotate.VolumeResult = value 

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
        return self.hybrid_shape_rotate.GetCreationMode()

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
                | example sets that the mode of the hybShpRotate hybrid shape
                | rotate to creation hybShpRotate.SetCreationMode True
                |
                | Parameters:


        :param i_creation:
        :return:
        """
        return self.hybrid_shape_rotate.SetCreationMode(i_creation)

    def __repr__(self):
        return f'HybridShapeRotate()'
