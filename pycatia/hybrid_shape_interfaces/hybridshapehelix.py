#! /usr/bin/python3.6
# module initially auto generated using V5Automation.chm from CATIA R25 on 2020-05-22 12:54:36.956119

from pycatia.mec_mod_interfaces.hybridshape import HybridShape


class HybridShapeHelix(HybridShape):
    """
        .. note::
            CAA V5 Visual Basic help

                | Represents the hybrid shape helix feature object.Role: Allows to
                | access data of the Helix feature.   This data includes:

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_helix = com_object     

    @property
    def axis(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Axis
                | o Property Axis(    ) As
                | 
                | Reads / Changes the Helix axis.

        :return:
        """
        return self.hybrid_shape_helix.Axis

    @property
    def clockwise_revolution(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | ClockwiseRevolution
                | o Property ClockwiseRevolution(    ) As
                | 
                | Reads / Modifies the sense of revolutions .

        :return:
        """
        return self.hybrid_shape_helix.ClockwiseRevolution

    @property
    def height(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Height
                | o Property Height(    ) As   (Read Only)
                | 
                | Reads the height of the Helix.

        :return:
        """
        return self.hybrid_shape_helix.Height

    @property
    def invert_axis(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | InvertAxis
                | o Property InvertAxis(    ) As
                | 
                | Reads / Modifies the orientation .

        :return:
        """
        return self.hybrid_shape_helix.InvertAxis

    @property
    def pitch(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Pitch
                | o Property Pitch(    ) As   (Read Only)
                | 
                | Reads the pitch of the Helix.

        :return:
        """
        return self.hybrid_shape_helix.Pitch

    @property
    def pitch2(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Pitch2
                | o Property Pitch2(    ) As   (Read Only)
                | 
                | Reads the Helix pitch2.

        :return:
        """
        return self.hybrid_shape_helix.Pitch2

    @property
    def pitch_law_type(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | PitchLawType
                | o Property PitchLawType(    ) As
                | 
                | Reads / Changes the Helix pitch law type.

        :return:
        """
        return self.hybrid_shape_helix.PitchLawType

    @property
    def profile(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Profile
                | o Property Profile(    ) As
                | 
                | Reads / Changes the Helix profile.

        :return:
        """
        return self.hybrid_shape_helix.Profile

    @property
    def revol_number(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | RevolNumber
                | o Property RevolNumber(    ) As   (Read Only)
                | 
                | Reads the revolution number of the Helix.

        :return:
        """
        return self.hybrid_shape_helix.RevolNumber

    @property
    def starting_angle(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | StartingAngle
                | o Property StartingAngle(    ) As   (Read Only)
                | 
                | Reads the helix starting angle.

        :return:
        """
        return self.hybrid_shape_helix.StartingAngle

    @property
    def starting_point(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | StartingPoint
                | o Property StartingPoint(    ) As
                | 
                | Reads / Changes the starting point of the Helix. The
                | starting point must not be on the Helix axis.

        :return:
        """
        return self.hybrid_shape_helix.StartingPoint

    @property
    def taper_angle(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | TaperAngle
                | o Property TaperAngle(    ) As   (Read Only)
                | 
                | Reads the helix taper angle.

        :return:
        """
        return self.hybrid_shape_helix.TaperAngle

    @property
    def taper_outward(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | TaperOutward
                | o Property TaperOutward(    ) As
                | 
                | Reads / Modifies the taper angle sense of variation.

        :return:
        """
        return self.hybrid_shape_helix.TaperOutward

    def set_height(self, i_height):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetHeight
                | o Sub SetHeight(        iHeight)
                | 
                | Sets the helix height.
                |
                | Parameters:
                | iHeight
                |       Height.


        :param i_height:
        :return:
        """
        return self.hybrid_shape_helix.SetHeight(i_height)

    def set_pitch(self, i_pitch):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetPitch
                | o Sub SetPitch(        iPitch)
                | 
                | Sets the helix pitch.
                |
                | Parameters:
                | iPitch
                |       Pitch.


        :param i_pitch:
        :return:
        """
        return self.hybrid_shape_helix.SetPitch(i_pitch)

    def set_pitch2(self, i_pitch_2):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetPitch2
                | o Sub SetPitch2(        iPitch2)
                | 
                | Changes the Helix pitch2 .
                |
                | Parameters:
                | Pitch2
                |       Pitch2 for Helix.


        :param i_pitch_2:
        :return:
        """
        return self.hybrid_shape_helix.SetPitch2(i_pitch_2)

    def set_revolution_number(self, i_nb_revol):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetRevolutionNumber
                | o Sub SetRevolutionNumber(        iNbRevol)
                | 
                | Changes the Revolution Numbers.
                |
                | Parameters:
                | NbRevol
                |       Number of revolutions for Helix.


        :param i_nb_revol:
        :return:
        """
        return self.hybrid_shape_helix.SetRevolutionNumber(i_nb_revol)

    def set_starting_angle(self, i_starting_angle):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetStartingAngle
                | o Sub SetStartingAngle(        iStartingAngle)
                | 
                | Sets the helix starting angle.
                |
                | Parameters:
                | oTaperAngle
                |       Starting angle.


        :param i_starting_angle:
        :return:
        """
        return self.hybrid_shape_helix.SetStartingAngle(i_starting_angle)

    def set_taper_angle(self, i_taper_angle):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetTaperAngle
                | o Sub SetTaperAngle(        iTaperAngle)
                | 
                | Sets the helix taper angle.
                |
                | Parameters:
                | iTaperAngle
                |       Taper angle.


        :param i_taper_angle:
        :return:
        """
        return self.hybrid_shape_helix.SetTaperAngle(i_taper_angle)

    def __repr__(self):
        return f'HybridShapeHelix()'
