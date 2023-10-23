#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.any_object import AnyObject


class SWKErgoCarry(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SWKErgoCarry
                | 
                | This interface deals the carry ergonomic analysis.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.swk_ergo_carry = com_object

    @property
    def distance_of_carry(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property DistanceOfCarry() As CATBSTR
                | 
                |     Returns or sets the distance of carry.
                |     This distance must specified at least once.
                |     Failure to do so will result in invalid output values.

        :rtype: str
        """

        return self.swk_ergo_carry.DistanceOfCarry

    @distance_of_carry.setter
    def distance_of_carry(self, value: str):
        """
        :param str value:
        """

        self.swk_ergo_carry.DistanceOfCarry = value

    @property
    def frequency(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Frequency() As double
                | 
                |     Returns or sets the carry frequency.
                |     This frequency must be expressed in carries per second, and must
                |     be specified before attempting to retrieve any output value from the
                |     study. Failure to do so will result in invalid output values.

        :rtype: float
        """

        return self.swk_ergo_carry.Frequency

    @frequency.setter
    def frequency(self, value: float):
        """
        :param float value:
        """

        self.swk_ergo_carry.Frequency = value

    @property
    def maximum_weight(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property MaximumWeight() As CATBSTR (Read Only)
                | 
                |     This field is the maximum weight that can be carried force, given the
                |     current input guidelines.

        :rtype: str
        """

        return self.swk_ergo_carry.MaximumWeight

    @property
    def population(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Population() As double
                | 
                |     Returns or sets the percentage of the population that should be able to
                |     perform the carry task safely.
                |     This property can only take the values 50.0, 75.0 and 90.0, and must be
                |     specified at least once.
                |     Failure to do so will result in invalid output values.

        :rtype: float
        """

        return self.swk_ergo_carry.Population

    @population.setter
    def population(self, value: float):
        """
        :param float value:
        """

        self.swk_ergo_carry.Population = value

    def __repr__(self):
        return f'SWKErgoCarry(name="{self.name}")'
