#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.dnb_human_modeling_interfaces.swk_line_of_sight import SWKLineOfSight
from pycatia.dnb_human_modeling_interfaces.swk_manikin_part import SWKManikinPart


class SWKVision(SWKManikinPart):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     DNBHumanModelingInterfaces.SWKManikinPart
                |                         SWKVision
                | 
                | This interface manages the vision of the manikin.
                | It provides
                | access to the vision data (lines of sight, focal point...)
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.swk_vision = com_object

    @property
    def active_line_of_sight(self) -> SWKLineOfSight:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ActiveLineOfSight() As SWKLineOfSight (Read Only)
                | 
                |     Returns the active line of sight, according to the vision type.

        :rtype: SWKLineOfSight
        """

        return SWKLineOfSight(self.swk_vision.ActiveLineOfSight)

    @property
    def active_side(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ActiveSide() As long (Read Only)
                | 
                |     Returns the vision active side.
                |     The active line of sight is the one able to
                |     control the two others. That is, when the active line of
                |     sight moves, the two others update accordingly.
                |     When setting the type, the value given must be 0, 1 or 2.
                |     The value 0 activates the left line of sight, the value 1
                |     activates the central line of sight, the value 2 activates
                |     the right line of sight.
                |     If other values are given, an error will occur.

        :rtype: int
        """

        return self.swk_vision.ActiveSide

    @property
    def ambinocular_angle(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property AmbinocularAngle() As double
                | 
                |     Returns or sets the vision Ambinocular angle.
                |     This angle is always in degrees.

        :rtype: float
        """

        return self.swk_vision.AmbinocularAngle

    @ambinocular_angle.setter
    def ambinocular_angle(self, value: float):
        """
        :param float value:
        """

        self.swk_vision.AmbinocularAngle = value

    @property
    def binocular_angle(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property BinocularAngle() As double
                | 
                |     Returns or sets the vision Binocular angle.
                |     This angle is always in degrees.

        :rtype: float
        """

        return self.swk_vision.BinocularAngle

    @binocular_angle.setter
    def binocular_angle(self, value: float):
        """
        :param float value:
        """

        self.swk_vision.BinocularAngle = value

    @property
    def central_cone_angle(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property CentralConeAngle() As double
                | 
                |     Returns or sets the vision Central cone angle.
                |     This angle is always in degrees.

        :rtype: float
        """

        return self.swk_vision.CentralConeAngle

    @central_cone_angle.setter
    def central_cone_angle(self, value: float):
        """
        :param float value:
        """

        self.swk_vision.CentralConeAngle = value

    @property
    def focal_distance(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property FocalDistance() As double
                | 
                |     Returns or sets the focal distance, in centimeters.
                |     N.B.: if the value is -1.0,
                |     then the focal distance is set to infinite.

        :rtype: float
        """

        return self.swk_vision.FocalDistance

    @focal_distance.setter
    def focal_distance(self, value: float):
        """
        :param float value:
        """

        self.swk_vision.FocalDistance = value

    @property
    def focal_point_x(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property FocalPointX() As double (Read Only)
                | 
                |     Returns the x coordinate (in millimeters) of the focal point.

        :rtype: float
        """

        return self.swk_vision.FocalPointX

    @property
    def focal_point_y(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property FocalPointY() As double (Read Only)
                | 
                |     Returns the y coordinate (in millimeters) of the focal point.

        :rtype: float
        """

        return self.swk_vision.FocalPointY

    @property
    def focal_point_z(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property FocalPointZ() As double (Read Only)
                | 
                |     Returns the z coordinate (in millimeters) of the focal point.

        :rtype: float
        """

        return self.swk_vision.FocalPointZ

    @property
    def monocular_angle(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property MonocularAngle() As double
                | 
                |     Returns or sets the vision Monocular angle.
                |     This angle is always in degrees.

        :rtype: float
        """

        return self.swk_vision.MonocularAngle

    @monocular_angle.setter
    def monocular_angle(self, value: float):
        """
        :param float value:
        """

        self.swk_vision.MonocularAngle = value

    @property
    def ponctum_proximum(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property PonctumProximum() As double
                | 
                |     Returns or sets the ponctum proximum, in centimeters. The ponctum proximum
                |     is the minimum value the focal distance can take.

        :rtype: float
        """

        return self.swk_vision.PonctumProximum

    @ponctum_proximum.setter
    def ponctum_proximum(self, value: float):
        """
        :param float value:
        """

        self.swk_vision.PonctumProximum = value

    @property
    def ponctum_remotum(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property PonctumRemotum() As double
                | 
                |     Returns or sets the ponctum remotum, in centimeters. The ponctum remotum is
                |     the largest value that the focal distance can take. N.B.: if the value is -1.0,
                |     then the ponctum remotum is set to infinite.

        :rtype: float
        """

        return self.swk_vision.PonctumRemotum

    @ponctum_remotum.setter
    def ponctum_remotum(self, value: float):
        """
        :param float value:
        """

        self.swk_vision.PonctumRemotum = value

    @property
    def type(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Type() As long
                | 
                |     Returns or sets the vision type. (binocular, ambinocular, monocular left,
                |     monocular right or stereo.
                |     When setting the type, the value given must be 0, 1, 2, 3, or 4
                |     The value 0 activates the Binocular type, 1 is Ambinocular, 2 is
                |     MonocularRight, 3 is MonocularLeft, and 4 is Stereo. If other values are given,
                |     an error will occur.

        :rtype: int
        """

        return self.swk_vision.Type

    @type.setter
    def type(self, value: int):
        """
        :param int value:
        """

        self.swk_vision.Type = value

    @property
    def vertical_bottom_angle(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property VerticalBottomAngle() As double
                | 
                |     Returns or sets the vision Vertical Bottom angle.
                |     This angle is always in degrees.

        :rtype: float
        """

        return self.swk_vision.VerticalBottomAngle

    @vertical_bottom_angle.setter
    def vertical_bottom_angle(self, value: float):
        """
        :param float value:
        """

        self.swk_vision.VerticalBottomAngle = value

    @property
    def vertical_top_angle(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property VerticalTopAngle() As double
                | 
                |     Returns or sets the vision Vertical Top angle.
                |     This angle is always in degrees.

        :rtype: float
        """

        return self.swk_vision.VerticalTopAngle

    @vertical_top_angle.setter
    def vertical_top_angle(self, value: float):
        """
        :param float value:
        """

        self.swk_vision.VerticalTopAngle = value

    def close_vision_windows(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub CloseVisionWindows()
                | 
                |     Closes all open vision windows relating to the manikin on which the
                |     function is called.

        :rtype: None
        """
        return self.swk_vision.CloseVisionWindows()

    def look_at(self, pi_focal_distance: float, pi_v_angle: float, pi_h_angle: float) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub LookAt(double piFocalDistance,
                | double piVAngle,
                | double piHAngle)
                | 
                |     Make the manikin look at the specified position in space.
                |     This position is given by the focal distance, and two
                |     deviation angles.
                | 
                |     Parameters:
                | 
                |         piFocalDistance
                |             The focal distance (measured from the active eye), which is a
                |             horizontal straight distance, measured in centimeters.
                |             
                |         piVAngle
                |             The vertical angle (in radians) between the focal point
                |             and
                |             the active eye (positive angle deviates up, negative angle deviates
                |             down). 
                |         piHAngle
                |             The horizontal angle (in radians) between the
                |             focal
                |             point and the active eye (positive angle deviates left, negative
                |             angle deviates right). N.B.: the manikin's eyes will move only if it is
                |             able
                |             to reach the specified point.

        :param float pi_focal_distance:
        :param float pi_v_angle:
        :param float pi_h_angle:
        :rtype: None
        """
        return self.swk_vision.LookAt(pi_focal_distance, pi_v_angle, pi_h_angle)

    def look_at_point(self, pi_x: float, pi_y: float, pi_z: float) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub LookAtPoint(double piX,
                | double piY,
                | double piZ)
                | 
                |     Make the manikin look at the specified position in space.
                |     This position is given by three coordinates (expressed in
                |     millimeters)
                |     passed to the method.
                | 
                |     N.B.: the manikin's eyes will move only if it is able
                |     to reach the specified point.

        :param float pi_x:
        :param float pi_y:
        :param float pi_z:
        :rtype: None
        """
        return self.swk_vision.LookAtPoint(pi_x, pi_y, pi_z)

    def reset(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub Reset()
                | 
                |     Resets all attributes of the vision to their default values. This method
                |     resets the focal distance, the active line of sight, the ponctum proximum, the
                |     ponctum remotum, the field of view angles, the convergence mode, and restores
                |     the default DOF values on the three lines of sight.

        :rtype: None
        """
        return self.swk_vision.Reset()

    def __repr__(self):
        return f'SWKVision(name="{self.name}")'
