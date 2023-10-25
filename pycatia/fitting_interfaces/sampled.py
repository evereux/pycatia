#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.fitting_interfaces.shots import Shots
from pycatia.system_interfaces.any_object import AnyObject


class Sampled(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     Sampled
                | 
                | The interface to access a CATIASampled based object.
                | The Sampled class defines characteristics for simulatable tasks within DMU
                | Fitting. CATIASampled is the parent class for tracks. Key samples are recorded
                | (as shots or CATIAShots) for an object and then during simulation the object is
                | interpolated with these shots over time.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.sampled = com_object

    @property
    def interpolater(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Interpolater() As CATBSTR
                | 
                |     Retrieves/sets the sampled's interpolater. Role: Retrieves/sets the
                |     interpolator used by the sampled during simulation. Note that the name of the
                |     interpolater is used (which is a string).

        :rtype: str
        """

        return self.sampled.Interpolater

    @interpolater.setter
    def interpolater(self, value: str):
        """
        :param str value:
        """

        self.sampled.Interpolater = value

    @property
    def object(self) -> AnyObject:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Object() As CATBaseDispatch
                | 
                |     Returns or sets the Sampled object. Role:/b> Retrieves/stores the object
                |     that will be used in the sampled based simulation. Please note that the object
                |     will move to the shots defined in the sampled.

        :rtype: AnyObject
        """

        return AnyObject(self.sampled.Object)

    @object.setter
    def object(self, value: AnyObject):
        """
        :param AnyObject value:
        """

        self.sampled.Object = value

    @property
    def scaling(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Scaling() As double
                | 
                |     Returns or sets the Sampled object.

        :rtype: float
        """

        return self.sampled.Scaling

    @scaling.setter
    def scaling(self, value: float):
        """
        :param float value:
        """

        self.sampled.Scaling = value

    @property
    def shots(self) -> Shots:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Shots() As Shots (Read Only)
                | 
                |     Returns or sets the Sampled object.

        :rtype: Shots
        """

        return Shots(self.sampled.Shots)

    @property
    def time(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Time() As double
                | 
                |     Retrieves/sets the sampled's time. Role: Retrieves/sets the internal time
                |     associated to the current sampled object. Note that the time is handled as a
                |     double.

        :rtype: float
        """

        return self.sampled.Time

    @time.setter
    def time(self, value: float):
        """
        :param float value:
        """

        self.sampled.Time = value

    def append(self, i_tracks: tuple) -> 'Sampled':
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func Append(CATSafeArrayVariant iTracks) As Sampled
                | 
                |     Returns or sets the Sampled object.

        :param tuple i_tracks:
        :rtype: Sampled
        """
        return Sampled(self.sampled.Append(i_tracks))

    def bind_analysis(self, i_object: AnyObject, i_analysis_mode: int, i_monitor_mode: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub BindAnalysis(CATBaseDispatch iObject,
                | CatSampledAnalysisMode iAnalysisMode,
                | boolean iMonitorMode)
                | 
                |     Add (bind) an analysis object to a Track.
                | 
                |     Parameters:
                | 
                |         iObject
                |             The analysis to add (bind) to the Track 
                |         iAnalysisMode
                |             Indicates the analysis status for iAnalysis CatSampledAnalysisOff
                |             CatSampledAnalysisOn, CatSampledAnalysisStop CatSampledAnalysisVerbose
                |             
                |         iMonitorMode
                |             Indicates the monitor status for iAnalysis - Off (0) or On
                |             (1)

        :param AnyObject i_object:
        :param int i_analysis_mode: enum cat_sampled_analysis_mode
        :param bool i_monitor_mode:
        :rtype: None
        """
        return self.sampled.BindAnalysis(i_object.com_object, i_analysis_mode, i_monitor_mode)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'bind_analysis'
        # # vba_code = """
        # # Public Function bind_analysis(sampled)
        # #     Dim iObject (2)
        # #     sampled.BindAnalysis iObject
        # #     bind_analysis = iObject
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def break_inheritance(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub BreakInheritance()
                | 
                |     Returns or sets the Sampled object.

        :rtype: None
        """
        return self.sampled.BreakInheritance()

    def get_known_interpolaters(self, o_interpolaters: tuple) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetKnownInterpolaters(CATSafeArrayVariant
                | oInterpolaters)
                | 
                |     Returns or sets the Sampled object.

        :param tuple o_interpolaters:
        :rtype: None
        """
        return self.sampled.GetKnownInterpolaters(o_interpolaters)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_known_interpolaters'
        # # vba_code = """
        # # Public Function get_known_interpolaters(sampled)
        # #     Dim oInterpolaters (2)
        # #     sampled.GetKnownInterpolaters oInterpolaters
        # #     get_known_interpolaters = oInterpolaters
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_total_duration(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetTotalDuration() As double
                | 
                |     Returns the total duration

        :rtype: float
        """
        return self.sampled.GetTotalDuration()

    def remove_analyses(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub RemoveAnalyses()
                | 
                |     Returns or sets the Sampled object.

        :rtype: None
        """
        return self.sampled.RemoveAnalyses()

    def reverse_time(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub ReverseTime()
                | 
                |     Returns or sets the Sampled object.

        :rtype: None
        """
        return self.sampled.ReverseTime()

    def set_object_keeping_position(self, i_object: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetObjectKeepingPosition(CATBaseDispatch iObject)
                | 
                |     Sets the object in the sampled. Role: Stores the object that will be used
                |     in the sampled based simulation. The object will not move and the sample's
                |     shots will be repositioned relative to the object position.

        :param AnyObject i_object:
        :rtype: None
        """
        return self.sampled.SetObjectKeepingPosition(i_object.com_object)

    def split(self, i_type: int, i_indice: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub Split(CatSampledSplitType iType,
                | short iIndice)
                | 
                |     Returns or sets the Sampled object.

        :param int i_type: enum cat_sampled_split_type
        :param int i_indice:
        :rtype: None
        """
        return self.sampled.Split(i_type, i_indice)

    def __repr__(self):
        return f'Sampled(name="{self.name}")'
