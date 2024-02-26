#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.abq_automation_interfaces.abq_step import ABQStep
from pycatia.system_interfaces.any_object import AnyObject


class ABQJob(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     ABQJob
                | 
                | Represents an Abaqus job (ABQJob) object.
                | Role: Access an Abaqus job object or determine its properties.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.abq_job = com_object

    @property
    def computation_dir(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ComputationDir() As CATBSTR
                | 
                |     Sets or returns the computation directory.
                | 
                |     Returns:
                |         The computation directory.
                | 
                |         Example:
                |             This example sets the computation directory for the myJob job to
                |             "D:\\CompDir".
                | 
                |              myJob.ComputationDir = "D:\\CompDir"

        :rtype: str
        """

        return self.abq_job.ComputationDir

    @computation_dir.setter
    def computation_dir(self, value: str):
        """
        :param str value:
        """

        self.abq_job.ComputationDir = value

    @property
    def contact_print(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ContactPrint() As boolean
                | 
                |     Returns or sets whether contact constraint data are
                |     printed.
                | 
                |     Returns:
                |         A boolean specifying whether contact constraint data will be
                |         printed.
                | 
                |         Example:
                |             This example sets the printing of contact constraint data for the
                |             myJob job to False.
                | 
                |              myJob.ContactPrint = False

        :rtype: bool
        """

        return self.abq_job.ContactPrint

    @contact_print.setter
    def contact_print(self, value: bool):
        """
        :param bool value:
        """

        self.abq_job.ContactPrint = value

    @property
    def description(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Description() As CATBSTR
                | 
                |     Returns or sets the job description.
                | 
                |     Example:
                |         This example sets the job description for the myJob job to
                |         "AutomatedJob".
                | 
                |          myJob.Description = "AutomatedJob"

        :rtype: str
        """

        return self.abq_job.Description

    @description.setter
    def description(self, value: str):
        """
        :param str value:
        """

        self.abq_job.Description = value

    @property
    def echo_print(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property EchoPrint() As boolean
                | 
                |     Sets or returns whether an echo of the input data is
                |     printed.
                | 
                |     Returns:
                |         A boolen specifying whether the input data will be
                |         printed.
                | 
                |         Example:
                |             This example sets the printing of echo of the input data for the
                |             myJob job to True.
                | 
                |              myJob.EchoPrint = True

        :rtype: bool
        """

        return self.abq_job.EchoPrint

    @echo_print.setter
    def echo_print(self, value: bool):
        """
        :param bool value:
        """

        self.abq_job.EchoPrint = value

    @property
    def history_print(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property HistoryPrint() As boolean
                | 
                |     Sets or returns whether history data are printed.
                | 
                |     Returns:
                |         A boolean specifying whether the the history data will be
                |         printed.
                | 
                |         Example:
                |             This example sets the printing of history data for the myJob job to
                |             True.
                | 
                |              myJob.HistoryPrint = True

        :rtype: bool
        """

        return self.abq_job.HistoryPrint

    @history_print.setter
    def history_print(self, value: bool):
        """
        :param bool value:
        """

        self.abq_job.HistoryPrint = value

    @property
    def input_file_format(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property InputFileFormat() As boolean
                | 
                |     Sets or returns the format of the input file generated by the
                |     job.
                | 
                |     Returns:
                |         The input file format.
                | 
                |           
                |         Legal values:
                |          False (an assembly of separate parts)
                |          True  (a single part)
                |          
                | 
                |         Example:
                |             This example sets the input file format for the myJob job to a
                |             single part.
                | 
                |              myJob.InputFileFormat = True

        :rtype: bool
        """

        return self.abq_job.InputFileFormat

    @input_file_format.setter
    def input_file_format(self, value: bool):
        """
        :param bool value:
        """

        self.abq_job.InputFileFormat = value

    @property
    def max_memory(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property MaxMemory() As double
                | 
                |     Sets or returns the amount of memory (in percent or MB) available to the
                |     solver
                | 
                |     Returns:
                |         The amount of memory.
                | 
                |         Example:
                |             This example sets the amount of memory available to the solver for
                |             myJob job to 60.
                | 
                |              myJob.MaxMemory = 60

        :rtype: float
        """

        return self.abq_job.MaxMemory

    @max_memory.setter
    def max_memory(self, value: float):
        """
        :param float value:
        """

        self.abq_job.MaxMemory = value

    @property
    def memory_unit(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property MemoryUnit() As MemoryUnit_Type
                | 
                |     Sets or returns the units to be used for specifying the maximum memory to
                |     be used by the solver.
                | 
                |     Returns:
                |         The unit.
                |
                |         Legal values:
                |          PERCENT
                |          MEGABYTES
                |
                |         Example:
                |             This example sets the unit for the myJob job to
                |             PERCENT.
                | 
                |              myJob.MemoryUnit = PERCENT

        :return: enum memory_unit_type
        :rtype: int
        """

        return self.abq_job.MemoryUnit

    @memory_unit.setter
    def memory_unit(self, value: int):
        """
        :param int value: enum memory_unit_type
        """

        self.abq_job.MemoryUnit = value

    @property
    def model_consistency_check(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ModelConsistencyCheck() As boolean
                | 
                |     Sets or returns whether a model consistency check should be
                |     performed.
                | 
                |     Returns:
                |         A boolean specifying whether a consistency check will be
                |         performed.
                | 
                |         Example:
                |             This example sets the Model consistency check for the myJob job to
                |             False.
                | 
                |              myJob.ModelConsistencyCheck = False

        :rtype: bool
        """

        return self.abq_job.ModelConsistencyCheck

    @model_consistency_check.setter
    def model_consistency_check(self, value: bool):
        """
        :param bool value:
        """

        self.abq_job.ModelConsistencyCheck = value

    @property
    def model_print(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ModelPrint() As boolean
                | 
                |     Sets or returns or sets whether model definition data is
                |     printed.
                | 
                |     Returns:
                |         A boolean specifying whether the model definition data will be
                |         printed.
                | 
                |         Example:
                |             This example sets the printing of model definition data for the
                |             myJob job to False.
                | 
                |              myJob.ModelPrint = False

        :rtype: bool
        """

        return self.abq_job.ModelPrint

    @model_print.setter
    def model_print(self, value: bool):
        """
        :param bool value:
        """

        self.abq_job.ModelPrint = value

    @property
    def num_cpus(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property NumCpus() As short
                | 
                |     Sets or returns the number of CPUs to use for this
                |     analysis.
                | 
                |     Returns:
                |         The number of CPUs.
                | 
                |         Example:
                |             This example sets the number of CPUs to use myJob job to
                |             3.
                | 
                |              myJob.NumCpus = 3

        :rtype: int
        """

        return self.abq_job.NumCpus

    @num_cpus.setter
    def num_cpus(self, value: int):
        """
        :param int value:
        """

        self.abq_job.NumCpus = value

    @property
    def parallelization_method_standard(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ParallelizationMethodStandard() As
                | ParallelMethodStd_Type
                | 
                |     Sets or returns the parallelization method for the Abaqus/Standard direct
                |     solver.
                | 
                |     Returns:
                |         The parallelization method.
                | 
                |           
                |         Legal values:
                |          TREE 
                |          SUPERNODE
                |          
                | 
                |         Example:
                |             This example sets the parallelization method for the myJob job to
                |             TREE.
                | 
                |              myJob.ParallelizationMethodStandard = TREE

        :return: enum parallel_method_std_type
        :rtype: int
        """

        return self.abq_job.ParallelizationMethodStandard

    @parallelization_method_standard.setter
    def parallelization_method_standard(self, value: int):
        """
        :param int value: enum parallel_method_std_type
        """

        self.abq_job.ParallelizationMethodStandard = value

    @property
    def restart_read_interval(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property RestartReadInterval() As short
                | 
                |     Sets or returns the interval of restart read requests. This is only valid
                |     if RestartReadOption is RESTART_INTERVAL The value must be greater than
                |     0.
                | 
                |     Returns:
                |         The interval of restart read requests.
                | 
                |         Example:
                |             This example sets the restart read request interval for myJob job
                |             to 10.
                | 
                |              myJob.RestartReadInterval = 10

        :rtype: int
        """

        return self.abq_job.RestartReadInterval

    @restart_read_interval.setter
    def restart_read_interval(self, value: int):
        """
        :param int value:
        """

        self.abq_job.RestartReadInterval = value

    @property
    def restart_read_job(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property RestartReadJob() As CATBSTR
                | 
                |     Sets or returns or the path to the original job (\\*.odb)
                |     file.
                | 
                |     Returns:
                |         The path to the original job (\\*.odb) file.
                |
                |         Example:
                |             This example sets the original job for the myJob job to
                |             "D:\\myoriginaljob.odb".
                | 
                |              myJob.RestartReadJob = "D:\\myoriginaljob.odb"

        :rtype: str
        """

        return self.abq_job.RestartReadJob

    @restart_read_job.setter
    def restart_read_job(self, value: str):
        """
        :param str value:
        """

        self.abq_job.RestartReadJob = value

    @property
    def restart_read_option(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property RestartReadOption() As short
                | 
                |     Sets or returns the restart read option. This is only valid if
                |     RestartReadOption is ABQ_STEP_OBJECT
                | 
                |     Returns:
                |         The option of restart read requests.
                | 
                |           
                |         Legal values:
                |          ABQ_RESTART_END_OF_STEP - The current step is terminated from which
                |          restart  
                |          is being made and restarts from end of that
                |         step.
                |          ABQ_RESTART_INTERVAL- Analysis will restart from the specified
                |          interval
                |                             number within the specified step.
                |          
                | 
                |         Example:
                |             This example sets the restart read option for myJob job to end of
                |             step.
                | 
                |              myJob.RestartReadOption = ABQ_RESTART_END_OF_STEP

        :return: enum abq_restart_read_option
        :rtype: int
        """

        return self.abq_job.RestartReadOption

    @restart_read_option.setter
    def restart_read_option(self, value: int):
        """
        :param int value: enum abq_restart_read_option
        """

        self.abq_job.RestartReadOption = value

    @property
    def restart_read_step(self) -> ABQStep:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property RestartReadStep() As ABQStep
                | 
                |     Sets or returns the Step.
                | 
                |     Returns:
                |         The Step of restart read requests.
                | 
                |         Example:
                |             This example sets the step for myJob job to 2.
                | 
                |              myJob.RestartReadStep = 2

        :rtype: ABQStep
        """

        return ABQStep(self.abq_job.RestartReadStep)

    @restart_read_step.setter
    def restart_read_step(self, value: ABQStep):
        """
        :param ABQStep value:
        """

        self.abq_job.RestartReadStep = value

    @property
    def restart_read_step_number(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property RestartReadStepNumber() As short
                | 
                |     Sets or returns the step number of restart read requests. This is only
                |     valid if RestartReadOption is ABQ_STEP_NUMBER The value must be greater than or
                |     equal to 1 and less than total number of steps.
                | 
                |     Returns:
                |         The step number of restart read requests.
                | 
                |         Example:
                |             This example sets the step number for myJob job to
                |             2.
                | 
                |              myJob.RestartReadStepNumber = 2

        :rtype: int
        """

        return self.abq_job.RestartReadStepNumber

    @restart_read_step_number.setter
    def restart_read_step_number(self, value: int):
        """
        :param int value:
        """

        self.abq_job.RestartReadStepNumber = value

    @property
    def restart_read_step_selection_option(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property RestartReadStepSelectionOption() As short
                | 
                |     Sets or returns the step selection option for restart
                |     read.
                | 
                |     Returns:
                |         The step selection option of restart read requests.
                | 
                |           
                |         Legal values:
                |          ABQ_STEP_OBJECT - Selects step object
                |          ABQ_STEP_NUMBER- Selects step by step number
                |          
                | 
                |         Example:
                |             This example sets the step selection option for myJob job to end of
                |             step.
                | 
                |              myJob.RestartReadStepSelectionOption = ABQ_STEP_OBJECT

        :return: enum abq_restart_read_step_sel_option
        :rtype: int
        """

        return self.abq_job.RestartReadStepSelectionOption

    @restart_read_step_selection_option.setter
    def restart_read_step_selection_option(self, value: int):
        """
        :param int value: enum abq_restart_read_step_sel_option
        """

        self.abq_job.RestartReadStepSelectionOption = value

    @property
    def restart_request_frequency(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property RestartRequestFrequency() As short
                | 
                |     DEPRECATED - please use RestartRequestOption instead. Sets or returns the
                |     frequency of restart requests.
                | 
                |     Returns:
                |         The frequency of restart requests.
                | 
                |           
                |         Legal values:
                |          0 (None)
                |          1 (After each increment)
                |          999 (After the last increment in each step and after the last
                |          increment of the analysis)
                |          
                | 
                |         Example:
                |             This example sets the restart request frequency for myJob job to
                |             999.
                | 
                |              myJob.RestartRequestFrequency = 999

        :rtype: int
        """

        return self.abq_job.RestartRequestFrequency

    @restart_request_frequency.setter
    def restart_request_frequency(self, value: int):
        """
        :param int value:
        """

        self.abq_job.RestartRequestFrequency = value

    @property
    def restart_request_frequency_value(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property RestartRequestFrequencyValue() As short
                | 
                |     Sets or returns the frequencey value of restart requests. This is only
                |     valid if RestartRequestOption is ABQ_RESTART_SPECINT. The value must be greater
                |     than 0.
                | 
                |     Returns:
                |         The frequency value of restart requests.
                | 
                |         Example:
                |             This example sets the restart request frequency value for myJob job
                |             to 10.
                | 
                |              myJob.RestartRequestFrequencyValue = 10

        :rtype: int
        """

        return self.abq_job.RestartRequestFrequencyValue

    @restart_request_frequency_value.setter
    def restart_request_frequency_value(self, value: int):
        """
        :param int value:
        """

        self.abq_job.RestartRequestFrequencyValue = value

    @property
    def restart_request_interval_value(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property RestartRequestIntervalValue() As short
                | 
                |     Sets or returns the interval of restart requests. This is only valid if
                |     RestartRequestOption is ABQ_RESTART_NUMINT The value must be greater than
                |     0.
                | 
                |     Returns:
                |         The interval of restart requests.
                | 
                |         Example:
                |             This example sets the restart request interval for myJob job to
                |             10.
                | 
                |              myJob.RestartRequestIntervalValue = 10

        :rtype: int
        """

        return self.abq_job.RestartRequestIntervalValue

    @restart_request_interval_value.setter
    def restart_request_interval_value(self, value: int):
        """
        :param int value:
        """

        self.abq_job.RestartRequestIntervalValue = value

    @property
    def restart_request_option(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property RestartRequestOption() As short
                | 
                |     Sets or returns the restart request option.
                | 
                |     Returns:
                |         The option of restart requests.
                |
                |         Legal values:
                |          ABQ_RESTART_NONE - No restart data.
                |          ABQ_RESTART_EVERYINC- Collect on every increment.
                |          ABQ_RESTART_SPECINC  - Used to define the frequency to collect the
                |          data.  
                |                             Used in conjunction with
                |                             RestartRequestFrequencyValue.
                |          ABQ_RESTART_NUMINT   - Used to define the interval to collect the
                |          data.
                |                             Used in conjunction with
                |                             RestartRequestIntervalValue.
                |          ABQ_RESTART_LASTINC  - Collect after the last increment in each step
                |          and 
                |                             after the last increment of the
                |                             analysis.
                |
                |         Example:
                |             This example sets the restart option for myJob job to every
                |             increment.
                | 
                |              myJob.RestartRequestOption = RESTART_EVERYINC

        :return: enum ABQ_RESTART_NONE
        :rtype: int
        """

        return self.abq_job.RestartRequestOption

    @restart_request_option.setter
    def restart_request_option(self, value: int):
        """
        :param int value: enum ABQ_RESTART_NONE
        """

        self.abq_job.RestartRequestOption = value

    @property
    def restart_request_overlay(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property RestartRequestOverlay() As boolean
                | 
                |     Sets or returns the overlay option for the restart
                |     request.
                | 
                |     Returns:
                |         A boolean specifying whether the to use the overlay
                |         option.
                | 
                |         Example:
                |             This example sets the overlay option for the restart request for
                |             myJob job to True.
                | 
                |              myJob.RestartRequestOverlay = True

        :rtype: bool
        """

        return self.abq_job.RestartRequestOverlay

    @restart_request_overlay.setter
    def restart_request_overlay(self, value: bool):
        """
        :param bool value:
        """

        self.abq_job.RestartRequestOverlay = value

    @property
    def restart_request_time_marks(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property RestartRequestTimeMarks() As boolean
                | 
                |     Sets or returns the time marks flag for restart requests. This is only
                |     valid if the RestartRequestOption is ABQ_RESTART_NUMINT.
                | 
                |     Returns:
                |         The time marks flag for restart requests.
                | 
                |         Example:
                |             This example sets the time marks flag for myJob job to
                |             10.
                | 
                |              myJob.RestartRequestTimeMarks = True

        :rtype: bool
        """

        return self.abq_job.RestartRequestTimeMarks

    @restart_request_time_marks.setter
    def restart_request_time_marks(self, value: bool):
        """
        :param bool value:
        """

        self.abq_job.RestartRequestTimeMarks = value

    @property
    def scratch(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Scratch() As CATBSTR
                | 
                |     Sets or returns or the path to the scratch directory.
                | 
                |     Returns:
                |         The path to the scratch directory.
                | 
                |         Example:
                |             This example sets the scratch directory for the myJob job to
                |             "D:\\Scratch".
                | 
                |              myJob.Scratch = "D:\\Scratch"

        :rtype: str
        """

        return self.abq_job.Scratch

    @scratch.setter
    def scratch(self, value: str):
        """
        :param str value:
        """

        self.abq_job.Scratch = value

    @property
    def source(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Source() As boolean
                | 
                |     Sets or returns the source for analysis.
                | 
                |     Returns:
                |         The source (model or input file).
                | 
                |         Example:
                |             This example sets the time marks flag for myJob job to From
                |             Model.
                | 
                |              myJob.Source = True

        :rtype: bool
        """

        return self.abq_job.Source

    @source.setter
    def source(self, value: bool):
        """
        :param bool value:
        """

        self.abq_job.Source = value

    @property
    def type(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Type() As Job_Type
                | 
                |     Returns or sets the job type.
                | 
                |     Returns:
                |         The job type.
                | 
                |           
                |         Legal values:
                |           ANALYSIS
                |           DATACHECK
                |           CONTINUE
                |           SYNTAXCHECK
                |           RESTART
                |          
                | 
                |         Example:
                |             This example sets the job type for the myJob job to
                |             ANALYSIS.
                | 
                |              myJob.Type = ANALYSIS

        :return: enum job_type
        :rtype: int
        """

        return self.abq_job.Type

    @type.setter
    def type(self, value: int):
        """
        :param int value: enum job_type
        """

        self.abq_job.Type = value

    @property
    def user_subroutine(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property UserSubroutine() As CATBSTR
                | 
                |     Sets or returns the user subroutine file path.
                | 
                |     Returns:
                |         The user subroutine file path.
                | 
                |         Example:
                |             This example sets the user subroutine path for the myJob job to
                |             "D:/UserSub".
                | 
                |              myJob.UserSubroutine = "D:/UserSub"

        :rtype: str
        """

        return self.abq_job.UserSubroutine

    @user_subroutine.setter
    def user_subroutine(self, value: str):
        """
        :param str value:
        """

        self.abq_job.UserSubroutine = value

    def submit_job(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SubmitJob()
                | 
                |     Submits the job.

        :rtype: None
        """
        return self.abq_job.SubmitJob()

    def write_input_file(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub WriteInputFile()
                | 
                |     Writes the input file for the job.

        :rtype: None
        """
        return self.abq_job.WriteInputFile()

    def __repr__(self):
        return f'ABQJob(name="{self.name}")'
