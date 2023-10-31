#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.any_object import AnyObject


class SWKErgoPushPull(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SWKErgoPushPull
                | 
                | This interface deals the push/pull ergonomic analysis.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.swk_ergo_push_pull = com_object

    @property
    def distance_of_pull(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property DistanceOfPull() As CATBSTR
                | 
                |     Returns or sets the distance of pull.
                |     This distance must specified at least once.
                |     Failure to do so will result in invalid output values.

        :rtype: str
        """

        return self.swk_ergo_push_pull.DistanceOfPull

    @distance_of_pull.setter
    def distance_of_pull(self, value: str):
        """
        :param str value:
        """

        self.swk_ergo_push_pull.DistanceOfPull = value

    @property
    def distance_of_push(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property DistanceOfPush() As CATBSTR
                | 
                |     Returns or sets the distance of push.
                |     This distance must specified at least once.
                |     Failure to do so will result in invalid output values.

        :rtype: str
        """

        return self.swk_ergo_push_pull.DistanceOfPush

    @distance_of_push.setter
    def distance_of_push(self, value: str):
        """
        :param str value:
        """

        self.swk_ergo_push_pull.DistanceOfPush = value

    @property
    def frequency(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Frequency() As double
                | 
                |     Returns or sets the push/pull frequecy.
                |     This frequency must be expressed in pushes or pulls per second, and
                |     must be specified before attempting to retrive any output value from
                |     the study.
                |     Failure to do so will result in invalid output values.

        :rtype: float
        """

        return self.swk_ergo_push_pull.Frequency

    @frequency.setter
    def frequency(self, value: float):
        """
        :param float value:
        """

        self.swk_ergo_push_pull.Frequency = value

    @property
    def max_initial_pull_force(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property MaxInitialPullForce() As CATBSTR (Read Only)
                | 
                |     This field is the maximum initial pulling force, produced by the study,
                |     given the current input guidelines.

        :rtype: str
        """

        return self.swk_ergo_push_pull.MaxInitialPullForce

    @property
    def max_initial_push_force(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property MaxInitialPushForce() As CATBSTR (Read Only)
                | 
                |     This field is the maximum initial pushing force, produced by the study,
                |     given the current input guidelines.

        :rtype: str
        """

        return self.swk_ergo_push_pull.MaxInitialPushForce

    @property
    def max_sustained_pull_force(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property MaxSustainedPullForce() As CATBSTR (Read Only)
                | 
                |     This field is the maximum sustained pulling force, produced by the study,
                |     given the current input guidelines.

        :rtype: str
        """

        return self.swk_ergo_push_pull.MaxSustainedPullForce

    @property
    def max_sustained_push_force(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property MaxSustainedPushForce() As CATBSTR (Read Only)
                | 
                |     This field is the maximum sustained pushing force, produced by the study,
                |     given the current input guidelines.

        :rtype: str
        """

        return self.swk_ergo_push_pull.MaxSustainedPushForce

    @property
    def population(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Population() As double
                | 
                |     Returns or sets the percentage of the population that should be able to
                |     perform the push/pull task safely.
                |     This property can only take the values 50.0, 75.0 and 90.0, and must be
                |     specified at least once.
                |     Failure to do so will result in invalid output values.

        :rtype: float
        """

        return self.swk_ergo_push_pull.Population

    @population.setter
    def population(self, value: float):
        """
        :param float value:
        """

        self.swk_ergo_push_pull.Population = value

    def __repr__(self):
        return f'SWKErgoPushPull(name="{self.name}")'
