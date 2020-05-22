#! /usr/bin/python3.6
# module initially auto generated using V5Automation.chm from CATIA R25 on 2020-05-22 12:54:36.956119

from pycatia.mec_mod_interfaces.hybridshape import HybridShape


class HybridShapeConnect(HybridShape):
    """
        .. note::
            CAA V5 Visual Basic help

                | Represents the hybrid shape connect curve object.Role: To access the
                | data of the hybrid shape connect curve object. This data includes:

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_connect = com_object     

    @property
    def base_curve(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | BaseCurve
                | o Property BaseCurve(    ) As
                | 
                | Returns or sets the base curve. Do not use this property

        :return:
        """
        return self.hybrid_shape_connect.BaseCurve

    @base_curve.setter
    def base_curve(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_connect.BaseCurve = value 

    @property
    def connect_type(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | ConnectType
                | o Property ConnectType(    ) As
                | 
                | Returns or sets whether the connect curve is or should be
                | created as a"Normal Connect" or with a "Base Curve". Legal
                | values: 0 for the normal solution and 1 for base curve
                | solution. 
                |
                | Example:
                | This example sets the mode to create the
                | connect curve hybConnectCurve with a base curve.
                | hybConnectCurve.Base Curve = 1

        :return:
        """
        return self.hybrid_shape_connect.ConnectType

    @connect_type.setter
    def connect_type(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_connect.ConnectType = value 

    @property
    def first_continuity(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | FirstContinuity
                | o Property FirstContinuity(    ) As
                | 
                | Gets or Sets the continuity on first curve. FirstContinuity
                | = 0 : Point continuity = 1 : Tangency continuity = 2 :
                | Curvature continuity

        :return:
        """
        return self.hybrid_shape_connect.FirstContinuity

    @property
    def first_curve(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | FirstCurve
                | o Property FirstCurve(    ) As
                | 
                | Gets or Sets the first reference curve. new first reference
                | curve

        :return:
        """
        return self.hybrid_shape_connect.FirstCurve

    @property
    def first_orientation(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | FirstOrientation
                | o Property FirstOrientation(    ) As
                | 
                | Gets or Sets the orientation of first curve FirstOrientation
                | = 1 : SameOrientation. = -1 : InvertOrientation. = 2 :
                | KoOrientation

        :return:
        """
        return self.hybrid_shape_connect.FirstOrientation

    @property
    def first_point(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | FirstPoint
                | o Property FirstPoint(    ) As
                | 
                | Gets or Sets the first reference point. new first reference
                | point

        :return:
        """
        return self.hybrid_shape_connect.FirstPoint

    @property
    def first_tension(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | FirstTension
                | o Property FirstTension(    ) As   (Read Only)
                | 
                | Returns the tension on the first curve making up the connect
                | curve. 
                |
                | Example:
                | This example retrieves the tension of the
                | first curve that makes up the connect curve hybConnect. Dim
                | firstCurveTension As CATIARealParam firstCurveTension =
                | hybConnect.FirstTension

        :return:
        """
        return self.hybrid_shape_connect.FirstTension

    @property
    def second_continuity(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | SecondContinuity
                | o Property SecondContinuity(    ) As
                | 
                | Gets or Sets the continuity on second curve.
                | SecondContinuity = 0 : Point continuity = 1 : Tangency
                | continuity = 2 : Curvature continuity

        :return:
        """
        return self.hybrid_shape_connect.SecondContinuity

    @property
    def second_curve(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | SecondCurve
                | o Property SecondCurve(    ) As
                | 
                | Gets or Sets the second reference curve. new second
                | reference curve

        :return:
        """
        return self.hybrid_shape_connect.SecondCurve

    @property
    def second_orientation(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | SecondOrientation
                | o Property SecondOrientation(    ) As
                | 
                | Gets or Sets the orientation of second curve
                | SecondOrientation = 1 : SameOrientation. = -1 :
                | InvertOrientation. = 2 : KoOrientation

        :return:
        """
        return self.hybrid_shape_connect.SecondOrientation

    @property
    def second_point(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | SecondPoint
                | o Property SecondPoint(    ) As
                | 
                | Gets or Sets the second reference point. new second
                | reference point

        :return:
        """
        return self.hybrid_shape_connect.SecondPoint

    @property
    def second_tension(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | SecondTension
                | o Property SecondTension(    ) As   (Read Only)
                | 
                | Returns the tension on the second curve making up the
                | connect curve. 
                |
                | Example:
                | This example retrieves the tension
                | of the second curve that makes up the connect curve
                | hybConnect. Dim secondCurveTension As CATIARealParam
                | secondCurveTension = hybConnect.SecondTension

        :return:
        """
        return self.hybrid_shape_connect.SecondTension

    @property
    def trim(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Trim
                | o Property Trim(    ) As
                | 
                | Gets or Sets the trim mode. Trim = FALSE : Connected curves
                | are not trimmed. = TRUE : Connected curves are trimmed.

        :return:
        """
        return self.hybrid_shape_connect.Trim

    def __repr__(self):
        return f'HybridShapeConnect()'
