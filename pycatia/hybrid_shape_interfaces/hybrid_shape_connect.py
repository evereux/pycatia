#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-07-06 14:02:20.222384

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
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)

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
    def base_curve(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property BaseCurve() As Reference
                | 
                |     Returns or sets the base curve.
                |     Do not use this property

        :rtype: Reference
        """

        return Reference(self.hybrid_shape_connect.BaseCurve)

    @base_curve.setter
    def base_curve(self, refernce_curve: Reference):
        """
        :param Reference refernce_curve:
        """

        self.hybrid_shape_connect.BaseCurve = refernce_curve.com_object

    @property
    def connect_type(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
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

        :rtype: int
        """

        return self.hybrid_shape_connect.ConnectType

    @connect_type.setter
    def connect_type(self, value: int):
        """
        :param int value:
        """

        self.hybrid_shape_connect.ConnectType = value

    @property
    def first_continuity(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property FirstContinuity() As long
                | 
                |     Gets or Sets the continuity on first curve.
                |     FirstContinuity = 0 : Point continuity = 1 : Tangency continuity = 2 : Curvature continuity

        :rtype: int
        """

        return self.hybrid_shape_connect.FirstContinuity

    @first_continuity.setter
    def first_continuity(self, value: int):
        """
        :param int value:
        """

        self.hybrid_shape_connect.FirstContinuity = value

    @property
    def first_curve(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property FirstCurve() As Reference
                | 
                |     Gets or Sets the first reference curve. new first reference curve

        :rtype: Reference
        """

        return Reference(self.hybrid_shape_connect.FirstCurve)

    @first_curve.setter
    def first_curve(self, refernce_curve: Reference):
        """
        :param Reference refernce_curve:
        """

        self.hybrid_shape_connect.FirstCurve = refernce_curve.com_object

    @property
    def first_orientation(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property FirstOrientation() As long
                | 
                |     Gets or Sets the orientation of first curve
                |     FirstOrientation = 1 : SameOrientation. = -1 : InvertOrientation. = 2 : KoOrientation

        :rtype: int
        """

        return self.hybrid_shape_connect.FirstOrientation

    @first_orientation.setter
    def first_orientation(self, value: int):
        """
        :param int value:
        """

        self.hybrid_shape_connect.FirstOrientation = value

    @property
    def first_point(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property FirstPoint() As Reference
                | 
                |     Gets or Sets the first reference point. new first reference point

        :rtype: Reference
        """

        return Reference(self.hybrid_shape_connect.FirstPoint)

    @first_point.setter
    def first_point(self, refernce_curve: Reference):
        """
        :param Reference refernce_curve:
        """

        self.hybrid_shape_connect.FirstPoint = refernce_curve.com_object

    @property
    def first_tension(self) -> RealParam:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
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

        :rtype: RealParam
        """

        return RealParam(self.hybrid_shape_connect.FirstTension)

    @property
    def second_continuity(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property SecondContinuity() As long
                | 
                |     Gets or Sets the continuity on second curve. SecondContinuity = 0 : Point continuity = 1 :
                |     Tangency continuity = 2 : Curvature continuity

        :rtype: int
        """

        return self.hybrid_shape_connect.SecondContinuity

    @second_continuity.setter
    def second_continuity(self, value: int):
        """
        :param int value:
        """

        self.hybrid_shape_connect.SecondContinuity = value

    @property
    def second_curve(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property SecondCurve() As Reference
                | 
                |     Gets or Sets the second reference curve. new second reference curve

        :rtype: Reference
        """

        return Reference(self.hybrid_shape_connect.SecondCurve)

    @second_curve.setter
    def second_curve(self, refernce_curve: Reference):
        """
        :param Reference refernce_curve:
        """

        self.hybrid_shape_connect.SecondCurve = refernce_curve.com_object

    @property
    def second_orientation(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property SecondOrientation() As long
                | 
                |     Gets or Sets the orientation of second curve SecondOrientation = 1 : SameOrientation. = -1 :
                |     InvertOrientation. = 2 : KoOrientation

        :rtype: int
        """

        return self.hybrid_shape_connect.SecondOrientation

    @second_orientation.setter
    def second_orientation(self, value: int):
        """
        :param int value:
        """

        self.hybrid_shape_connect.SecondOrientation = value

    @property
    def second_point(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property SecondPoint() As Reference
                | 
                |     Gets or Sets the second reference point. new second reference point

        :rtype: Reference
        """

        return Reference(self.hybrid_shape_connect.SecondPoint)

    @second_point.setter
    def second_point(self, reference_point: Reference):
        """
        :param Reference reference_point:
        """

        self.hybrid_shape_connect.SecondPoint = reference_point.com_object

    @property
    def second_tension(self) -> RealParam:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
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

        :rtype: RealParam
        """

        return RealParam(self.hybrid_shape_connect.SecondTension)

    @property
    def trim(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property Trim() As boolean
                | 
                |     Gets or Sets the trim mode. Trim = FALSE : Connected curves are not trimmed. = TRUE :
                |     Connected curves are trimmed.

        :rtype: bool
        """

        return self.hybrid_shape_connect.Trim

    @trim.setter
    def trim(self, value: bool):
        """
        :param bool value:
        """

        self.hybrid_shape_connect.Trim = value

    def __repr__(self):
        return f'HybridShapeConnect(name="{self.name}")'
