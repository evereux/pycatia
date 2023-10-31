#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-07-06 14:02:20.222384

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.in_interfaces.reference import Reference
from pycatia.knowledge_interfaces.angle import Angle
from pycatia.knowledge_interfaces.length import Length
from pycatia.knowledge_interfaces.real_param import RealParam
from pycatia.mec_mod_interfaces.hybrid_shape import HybridShape


class HybridShapeHelix(HybridShape):

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
                |                         HybridShapeHelix
                | 
                | Represents the hybrid shape helix feature object.
                | Role: Allows to access data of the Helix feature. This data
                | includes:
                | 
                |     axis
                |     a starting point
                |     a pitch
                |     a height
                |     2 angle values
                | 
                | See also:
                |     HybridShapeFactory
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_helix = com_object

    @property
    def axis(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Axis() As Reference
                | 
                |     Reads / Changes the Helix axis.
                | 
                |     Parameters:
                | 
                |         Axis
                |             Helix axis.
                |             Sub-element(s) supported (see 
                | 
                |         Boundary object): CATIARectlinearTriDimFeatEdge or
                |         RectilinearBiDimFeatEdge.

        :rtype: Reference
        """

        return Reference(self.hybrid_shape_helix.Axis)

    @axis.setter
    def axis(self, reference_axis: Reference):
        """
        :param Reference reference_axis:
        """

        self.hybrid_shape_helix.Axis = reference_axis.com_object

    @property
    def clockwise_revolution(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property ClockwiseRevolution() As boolean
                | 
                |     Reads / Modifies the sense of revolutions .
                | 
                |     Parameters:
                | 
                |         Clockwise
                |             FALSE means that revolutions are counter-clockwise. TRUE means that
                |             revolutions are clockwise.

        :rtype: bool
        """

        return self.hybrid_shape_helix.ClockwiseRevolution

    @clockwise_revolution.setter
    def clockwise_revolution(self, value: bool):
        """
        :param bool value:
        """

        self.hybrid_shape_helix.ClockwiseRevolution = value

    @property
    def height(self) -> Length:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Height() As Length (Read Only)
                | 
                |     Reads the height of the Helix.
                | 
                |     Parameters:
                | 
                |         oHeight
                |             Height.

        :rtype: Length
        """

        return Length(self.hybrid_shape_helix.Height)

    @property
    def invert_axis(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property InvertAxis() As boolean
                | 
                |     Reads / Modifies the orientation .
                | 
                |     Parameters:
                | 
                |         Invert
                |             FALSE means that there is no invertion (natural orientation). TRUE
                |             to invert this orientation.

        :rtype: bool
        """

        return self.hybrid_shape_helix.InvertAxis

    @invert_axis.setter
    def invert_axis(self, value: bool):
        """
        :param bool value:
        """

        self.hybrid_shape_helix.InvertAxis = value

    @property
    def pitch(self) -> Length:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Pitch() As Length (Read Only)
                | 
                |     Reads the pitch of the Helix.
                | 
                |     Parameters:
                | 
                |         oPitch
                |             Pitch.

        :rtype: Length
        """

        return Length(self.hybrid_shape_helix.Pitch)

    @property
    def pitch2(self) -> Length:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Pitch2() As Length (Read Only)
                | 
                |     Reads the Helix pitch2.
                | 
                |     Parameters:
                | 
                |         Pitch2
                |             Pitch2 for Helix.

        :rtype: Length
        """

        return Length(self.hybrid_shape_helix.Pitch2)

    @property
    def pitch_law_type(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property PitchLawType() As long
                | 
                |     Reads / Changes the Helix pitch law type.
                | 
                |     Parameters:
                | 
                |         LawType
                |             LawType for Helix.

        :rtype: int
        """

        return self.hybrid_shape_helix.PitchLawType

    @pitch_law_type.setter
    def pitch_law_type(self, value: int):
        """
        :param int value:
        """

        self.hybrid_shape_helix.PitchLawType = value

    @property
    def profile(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Profile() As Reference
                | 
                |     Reads / Changes the Helix profile.
                | 
                |     Parameters:
                | 
                |         Profile
                |             Profile for Helix.

        :rtype: Reference
        """

        return Reference(self.hybrid_shape_helix.Profile)

    @profile.setter
    def profile(self, reference_profile: Reference):
        """
        :param Reference reference_profile:
        """

        self.hybrid_shape_helix.Profile = reference_profile.com_object

    @property
    def revol_number(self) -> RealParam:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property RevolNumber() As RealParam (Read Only)
                | 
                |     Reads the revolution number of the Helix.
                | 
                |     Parameters:
                | 
                |         oNbRevol
                |             Revolutions.

        :rtype: RealParam
        """

        return RealParam(self.hybrid_shape_helix.RevolNumber)

    @property
    def starting_angle(self) -> Angle:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property StartingAngle() As Angle (Read Only)
                | 
                |     Reads the helix starting angle.
                | 
                |     Parameters:
                | 
                |         oStartingAngle
                |             Starting angle.

        :rtype: Angle
        """

        return Angle(self.hybrid_shape_helix.StartingAngle)

    @property
    def starting_point(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property StartingPoint() As Reference
                | 
                |     Reads / Changes the starting point of the Helix. The starting point must
                |     not be on the Helix axis.
                | 
                |     Parameters:
                | 
                |         StartingPoint
                |             Starting point.
                |             Sub-element(s) supported (see 
                | 
                |         Boundary object): Vertex.

        :rtype: Reference
        """

        return Reference(self.hybrid_shape_helix.StartingPoint)

    @starting_point.setter
    def starting_point(self, reference_point: Reference):
        """
        :param Reference reference_point:
        """

        self.hybrid_shape_helix.StartingPoint = reference_point.com_object

    @property
    def taper_angle(self) -> Angle:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property TaperAngle() As Angle (Read Only)
                | 
                |     Reads the helix taper angle.
                | 
                |     Parameters:
                | 
                |         oTaperAngle
                |             Taper angle.

        :rtype: Angle
        """

        return Angle(self.hybrid_shape_helix.TaperAngle)

    @property
    def taper_outward(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property TaperOutward() As boolean
                | 
                |     Reads / Modifies the taper angle sense of variation.
                | 
                |     Parameters:
                | 
                |         TaperOutward
                |             FALSE means that helix radius decreases. TRUE means that helix
                |             radius increases.

        :rtype: bool
        """

        return self.hybrid_shape_helix.TaperOutward

    @taper_outward.setter
    def taper_outward(self, value: bool):
        """
        :param bool value:
        """

        self.hybrid_shape_helix.TaperOutward = value

    def set_height(self, i_height: float) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetHeight(double iHeight)
                | 
                |     Sets the helix height.
                | 
                |     Parameters:
                | 
                |         iHeight
                |             Height.

        :param float i_height:
        :rtype: None
        """
        return self.hybrid_shape_helix.SetHeight(i_height)

    def set_pitch(self, i_pitch: float) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetPitch(double iPitch)
                | 
                |     Sets the helix pitch.
                | 
                |     Parameters:
                | 
                |         iPitch
                |             Pitch.

        :param float i_pitch:
        :rtype: None
        """
        return self.hybrid_shape_helix.SetPitch(i_pitch)

    def set_pitch2(self, i_pitch2: float) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetPitch2(double iPitch2)
                | 
                |     Changes the Helix pitch2 .
                | 
                |     Parameters:
                | 
                |         Pitch2
                |             Pitch2 for Helix.

        :param float i_pitch2:
        :rtype: None
        """
        return self.hybrid_shape_helix.SetPitch2(i_pitch2)

    def set_revolution_number(self, i_nb_revol: float) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetRevolutionNumber(double iNbRevol)
                | 
                |     Changes the Revolution Numbers.
                | 
                |     Parameters:
                | 
                |         NbRevol
                |             Number of revolutions for Helix.

        :param float i_nb_revol:
        :rtype: None
        """
        return self.hybrid_shape_helix.SetRevolutionNumber(i_nb_revol)

    def set_starting_angle(self, i_starting_angle: float) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetStartingAngle(double iStartingAngle)
                | 
                |     Sets the helix starting angle.
                | 
                |     Parameters:
                | 
                |         oTaperAngle
                |             Starting angle.

        :param float i_starting_angle:
        :rtype: None
        """
        return self.hybrid_shape_helix.SetStartingAngle(i_starting_angle)

    def set_taper_angle(self, i_taper_angle: float) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetTaperAngle(double iTaperAngle)
                | 
                |     Sets the helix taper angle.
                | 
                |     Parameters:
                | 
                |         iTaperAngle
                |             Taper angle.

        :param float i_taper_angle:
        :rtype: None
        """
        return self.hybrid_shape_helix.SetTaperAngle(i_taper_angle)

    def __repr__(self):
        return f'HybridShapeHelix(name="{ self.name }")'
