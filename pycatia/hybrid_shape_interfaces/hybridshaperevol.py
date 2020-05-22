#! /usr/bin/python3.6
# module initially auto generated using V5Automation.chm from CATIA R25 on 2020-05-22 12:54:36.956119

from pycatia.mec_mod_interfaces.hybridshape import HybridShape


class HybridShapeRevol(HybridShape):
    """
        .. note::
            CAA V5 Visual Basic help

                | The Revol feature : an Revol is made up of a face to process  and one
                | Revol parameter.Role: To access the data of the hybrid shape revol
                | feature object.

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_revol = com_object     

    @property
    def axis(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Axis
                | o Property Axis(    ) As
                | 
                | Role: To get_Axis on the object.

        :return:
        """
        return self.hybrid_shape_revol.Axis

    @property
    def begin_angle(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | BeginAngle
                | o Property BeginAngle(    ) As   (Read Only)
                | 
                | Role: To get_BeginAngle on the object.

        :return:
        """
        return self.hybrid_shape_revol.BeginAngle

    @property
    def context(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Context
                | o Property Context(    ) As
                | 
                | Returns or sets the context on Revolve feature. Legal
                | values: 0 This option creates surface of revolution. 1 This
                | option creates volume of revolution. Note: Setting volume
                | result requires GSO License. 
                |
                | Example:
                | This example retrieves
                | in oContext the context for the Revol hybrid shape feature.
                | Dim oContext Set oContext = Revol.Context

        :return:
        """
        return self.hybrid_shape_revol.Context

    @context.setter
    def context(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_revol.Context = value 

    @property
    def end_angle(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | EndAngle
                | o Property EndAngle(    ) As   (Read Only)
                | 
                | Role: To get_EndAngle on the object.

        :return:
        """
        return self.hybrid_shape_revol.EndAngle

    @property
    def orientation(self, i_orientation):
        """
        .. note::
            CAA V5 Visual Basic help

                | Orientation
                | o Property Orientation(        iOrientation)
                | 
                | Gets or sets orientation of the revolution. Orientation =
                | TRUE : The natural orientation of the axis is taken. = FALSE
                | : The opposite orientation is taken This example retrieves
                | in IsInverted orientation of the revolution for the Revol
                | hybrid shape feature. Dim IsInverted As boolean IsInverted =
                | Revol.Orientation

        :param i_orientation:
        :return:
        """
        return self.hybrid_shape_revol.Orientation

    @property
    def profil(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Profil
                | o Property Profil(    ) As
                | 
                | Role: To get_Profil on the object.

        :return:
        """
        return self.hybrid_shape_revol.Profil

    def __repr__(self):
        return f'HybridShapeRevol()'
