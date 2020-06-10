#! usr/bin/python3.6
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-09 09:53:18.676780

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.in_interfaces.reference import Reference
from pycatia.knowledge_interfaces.real_param import RealParam
from pycatia.mec_mod_interfaces.hybrid_shape import HybridShape


class HybridShapeConnect(HybridShape):

    """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.HybridShape
                |                         HybridShapeConnect
                | 
                | Represents the hybrid shape connect curve object.
                | Role: To access the data of the hybrid shape connect curve object. This data
                | includes:
                | 
                |     The face to process
                |     The connection parameter.
                | 
                | Use the HybridShapeFactory to create a HybridShapeConnect
                | object.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_connect = com_object

    @property
    def base_curve(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property BaseCurve() As Reference
                | 
                |     Returns or sets the base curve.
                |     Do not use this property

        :return: Reference
        """

        return Reference(self.hybrid_shape_connect.BaseCurve)

    @base_curve.setter
    def base_curve(self, value):
        """
        :param Reference value:
        """

        self.hybrid_shape_connect.BaseCurve = value

    @property
    def connect_type(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property ConnectType() As long
                | 
                |     Returns or sets whether the connect curve is or should be created as
                |     a"Normal Connect" or with a "Base Curve".
                |     Legal values: 0 for the normal solution and 1 for base curve
                |     solution.
                | 
                |     Example:
                | 
                |           This example sets the mode to create the connect
                |           curve
                |          hybConnectCurve with a base curve.
                |          
                | 
                |          hybConnectCurve.Base Curve = 1

        :return: int
        """

        return self.hybrid_shape_connect.ConnectType

    @connect_type.setter
    def connect_type(self, value):
        """
        :param int value:
        """

        self.hybrid_shape_connect.ConnectType = value

    @property
    def first_continuity(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property FirstContinuity() As long
                | 
                |     Gets or Sets the continuity on first curve. FirstContinuity = 0 : Point continuity = 1 : Tangency continuity = 2 : Curvature continuity

        :return: int
        """

        return self.hybrid_shape_connect.FirstContinuity

    @first_continuity.setter
    def first_continuity(self, value):
        """
        :param int value:
        """

        self.hybrid_shape_connect.FirstContinuity = value

    @property
    def first_curve(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property FirstCurve() As Reference
                | 
                |     Gets or Sets the first reference curve. new first reference curve

        :return: Reference
        """

        return Reference(self.hybrid_shape_connect.FirstCurve)

    @first_curve.setter
    def first_curve(self, value):
        """
        :param Reference value:
        """

        self.hybrid_shape_connect.FirstCurve = value

    @property
    def first_orientation(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property FirstOrientation() As long
                | 
                |     Gets or Sets the orientation of first curve FirstOrientation = 1 : SameOrientation. = -1 : InvertOrientation. = 2 : KoOrientation

        :return: int
        """

        return self.hybrid_shape_connect.FirstOrientation

    @first_orientation.setter
    def first_orientation(self, value):
        """
        :param int value:
        """

        self.hybrid_shape_connect.FirstOrientation = value

    @property
    def first_point(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property FirstPoint() As Reference
                | 
                |     Gets or Sets the first reference point. new first reference point

        :return: Reference
        """

        return Reference(self.hybrid_shape_connect.FirstPoint)

    @first_point.setter
    def first_point(self, value):
        """
        :param Reference value:
        """

        self.hybrid_shape_connect.FirstPoint = value

    @property
    def first_tension(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property FirstTension() As RealParam (Read Only)
                | 
                |     Returns the tension on the first curve making up the connect
                |     curve.
                | 
                |     Example:
                | 
                |           This example retrieves the tension of the first curve that makes
                |           up
                |          the connect curve hybConnect.
                |          
                | 
                |          Dim firstCurveTension As CATIARealParam
                |          firstCurveTension = hybConnect.FirstTension

        :return: RealParam
        """

        return RealParam(self.hybrid_shape_connect.FirstTension)

    @property
    def second_continuity(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property SecondContinuity() As long
                | 
                |     Gets or Sets the continuity on second curve. SecondContinuity = 0 : Point continuity = 1 : Tangency continuity = 2 : Curvature continuity

        :return: int
        """

        return self.hybrid_shape_connect.SecondContinuity

    @second_continuity.setter
    def second_continuity(self, value):
        """
        :param int value:
        """

        self.hybrid_shape_connect.SecondContinuity = value

    @property
    def second_curve(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property SecondCurve() As Reference
                | 
                |     Gets or Sets the second reference curve. new second reference curve

        :return: Reference
        """

        return Reference(self.hybrid_shape_connect.SecondCurve)

    @second_curve.setter
    def second_curve(self, value):
        """
        :param Reference value:
        """

        self.hybrid_shape_connect.SecondCurve = value

    @property
    def second_orientation(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property SecondOrientation() As long
                | 
                |     Gets or Sets the orientation of second curve SecondOrientation = 1 : SameOrientation. = -1 : InvertOrientation. = 2 : KoOrientation

        :return: int
        """

        return self.hybrid_shape_connect.SecondOrientation

    @second_orientation.setter
    def second_orientation(self, value):
        """
        :param int value:
        """

        self.hybrid_shape_connect.SecondOrientation = value

    @property
    def second_point(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property SecondPoint() As Reference
                | 
                |     Gets or Sets the second reference point. new second reference point

        :return: Reference
        """

        return Reference(self.hybrid_shape_connect.SecondPoint)

    @second_point.setter
    def second_point(self, value):
        """
        :param Reference value:
        """

        self.hybrid_shape_connect.SecondPoint = value

    @property
    def second_tension(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property SecondTension() As RealParam (Read Only)
                | 
                |     Returns the tension on the second curve making up the connect
                |     curve.
                | 
                |     Example:
                | 
                |           This example retrieves the tension of the second curve that makes
                |           up
                |          the connect curve hybConnect.
                |          
                | 
                |          Dim secondCurveTension As CATIARealParam
                |          secondCurveTension = hybConnect.SecondTension

        :return: RealParam
        """

        return RealParam(self.hybrid_shape_connect.SecondTension)

    @property
    def trim(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property Trim() As boolean
                | 
                |     Gets or Sets the trim mode. Trim = FALSE : Connected curves are not trimmed. = TRUE : Connected curves are trimmed.

        :return: bool
        """

        return self.hybrid_shape_connect.Trim

    @trim.setter
    def trim(self, value):
        """
        :param bool value:
        """

        self.hybrid_shape_connect.Trim = value

    def __repr__(self):
        return f'HybridShapeConnect(name="{ self.name }")'
