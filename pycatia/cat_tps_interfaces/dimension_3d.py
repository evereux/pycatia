#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
import inspect

from pycatia.drafting_interfaces.drawing_dimension import DrawingDimension
from pycatia.system_interfaces.any_object import AnyObject
from pycatia.cat_tps_interfaces.controlled_radius import ControlledRadius
from pycatia.cat_tps_interfaces.dimension_limit import DimensionLimit
from pycatia.cat_tps_interfaces.dimension_pattern import DimensionPattern
from pycatia.cat_tps_interfaces.envelope_condition import EnvelopeCondition


class Dimension3D(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     Dimension3D
                | 
                | Interface Managing Semantic Dimension.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.dimension_3d = com_object

    def controled_radius(self) -> ControlledRadius:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func ControledRadius() As ControledRadius
                | 
                |     Get the Dimension on the Controled Radius interface.
                | 
                |     Parameters:
                | 
                |         oContRadius
                |             The Controled Radius.

        :rtype: ControledRadius
        """
        return ControlledRadius(self.dimension_3d.ControlledRadius())

    def dimension_limit(self) -> DimensionLimit:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func DimensionLimit() As DimensionLimit
                | 
                |     Gets the Dimension on the DimensionLimit interface.
                | 
                |     Parameters:
                | 
                |         oDimLim
                |             The Dimension Limits.

        :rtype: DimensionLimit
        """
        return DimensionLimit(self.dimension_3d.DimensionLimit())

    def dimension_pattern(self) -> DimensionPattern:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func DimensionPattern() As DimensionPattern
                | 
                |     Gets the Dimension on the DimensionPattern interface.
                | 
                |     Parameters:
                | 
                |         oDimPatt
                |             The Dimension Pattern.

        :rtype: DimensionPattern
        """
        return DimensionPattern(self.dimension_3d.DimensionPattern())

    def envelope_condition(self) -> EnvelopeCondition:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func EnvelopCondition() As EnvelopCondition
                | 
                |     Gets the Dimension on the EnvelopCondition interface.
                | 
                |     Parameters:
                | 
                |         oEnvCond
                |             The Envelop Condition.

        :rtype: EnvelopCondition
        """
        return EnvelopeCondition(self.dimension_3d.EnvelopeCondition())

    def get_2d_annot(self) -> DrawingDimension:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func Get2dAnnot() As DrawingDimension
                | 
                |     Retrieves Drafting Dimension.
                | 
                |     Parameters:
                | 
                |         oDim
                |             The Drafting Dimension.

        :rtype: DrawingDimension
        """
        return DrawingDimension(self.dimension_3d.Get2dAnnot())

    def has_a_controlled_radius(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func HasAControledRadius() As boolean
                | 
                |     Checks if the Dimension has a Controled Radius.
                | 
                |     Parameters:
                | 
                |         oHasConRad
                | 
                |                 TRUE: The dimension has a Controled Radius
                |                 FALSE: The dimension has not a Controled
                |                 Radius

        :rtype: bool
        """
        return self.dimension_3d.HasAControledRadius()

    def has_an_envelope_condition(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func HasAnEnvelopCondition() As boolean
                | 
                |     Checks if the Annotation has an Envelop Condition.
                | 
                |     Parameters:
                | 
                |         oHasEnvCond
                | 
                |                 TRUE: The dimension has an Envelop Condition
                |                 FALSE: The dimension has not an Envelop
                |                 Condition

        :rtype: bool
        """
        return self.dimension_3d.HasAnEnvelopCondition()

    def has_dimension_limit(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func HasDimensionLimit() As boolean
                | 
                |     Checks if the Dimension has a Dimension Limit.
                | 
                |     Parameters:
                | 
                |         oHasDimLim
                | 
                |                 TRUE: Dimension Limit exists
                |                 FALSE: Dimension Limit does not exist

        :rtype: bool
        """
        return self.dimension_3d.HasDimensionLimit()

    def is_a_continuous_feature_applied(self) -> bool:
        """

        Introduced in V5-6R2019.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2024-08-20 16:04:57.203445)
                | Func IsAContinuousFeatureApplied() As boolean
                |     Checks if the Semantic Dimension is a applied on a Continuous Feature. CF
                |     suffix size modifier is only valid for ASME Standard.
                |
                |     Parameters:
                |
                |         oIsACFDim
                |
                |                 TRUE: The dimension is a applied onto a Continuous
                |                 Feature
                |                 FALSE: The dimension is not applied onto a Continuous
                |                 Feature

        :rtype: bool
        """

        self.release_check(
            self.application.system_configuration.release,
            29,
            f'{self.__class__.__name__}.{inspect.stack()[0][3]}',
        )

        return self.dimension3_d.IsAContinuousFeatureApplied()

    def is_a_dimension_pattern(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func IsADimensionPattern() As boolean
                | 
                |     Checks if the Semantic Dimension is a Dimension Pattern.
                | 
                |     Parameters:
                | 
                |         oIsADimPatt
                | 
                |                 TRUE: The dimension is a Dimension Pattern
                |                 FALSE: The dimension is not a Dimension
                |                 Pattern

        :rtype: bool
        """
        return self.dimension_3d.IsADimensionPattern()

    def move_value(self, x: float, y: float, sub_part: int, dim_angle_behavior: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub MoveValue(double X,
                | double Y,
                | long SubPart,
                | long DimAngleBehavior)
                | 
                |     Moves the dimension value at a given point.
                | 
                |     Returns:
                |         HRESULT error returned code If the modification of the vertical offset value can not be performed because the parameter is locked in the current standard, the method return HRESULT = S_READ_ONLY. 
                |     Parameters:
                | 
                |         X
                |             Point abscissa on which the dimension value will be positionned.
                |             
                |         Y
                |             Point ordinate on which the dimension value will be positionned.
                |             
                |         SubPart
                |             Defines which part of the dimension should be
                |             moved
                |             -1 = Value (vertical move is take account according ptPos coordinates)
                |             0 = Both dimension line and value
                |             1 = Value
                |             2 = Dimension line
                |             3 = Secondary part
                |             4 = Secondary part and value
                |             5 = Secondary part and dimension line
                |             6 = Secondary part, dimension line and value
                |             7 = Value leader (for dimension line with leader one part or two parts) 
                |         DimAngleBehavior
                |             Defines angle dimension line behavior.
                |             0 = Sector angle is switched when ptPos is in opposite sector (Default)
                |             1 = Sector angle is kept what ever ptPos placement 
                |         Example:
                |             This example move dimension value MyDimension
                |             path.
                | 
                |              MyDimension.MoveValue(X, Y, SubPart,
                |              DimAngleBehavior)

        :param float x:
        :param float y:
        :param int sub_part:
        :param int dim_angle_behavior:
        :rtype: None
        """
        return self.dimension_3d.MoveValue(x, y, sub_part, dim_angle_behavior)

    def __repr__(self):
        return f'Dimension3D(name="{self.name}")'
