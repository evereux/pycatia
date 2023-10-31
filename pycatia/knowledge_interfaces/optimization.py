#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.knowledge_interfaces.free_parameters import FreeParameters
from pycatia.knowledge_interfaces.knowledge_object import KnowledgeObject
from pycatia.knowledge_interfaces.optimization_constraints import OptimizationConstraints
from pycatia.knowledge_interfaces.real_param import RealParam


class Optimization(KnowledgeObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     KnowledgeInterfaces.KnowledgeObject
                |                         Optimization
                | 
                | Represents an Optimization object.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.optimization = com_object

    @property
    def algorithm_type(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property AlgorithmType() As CatAlgorithmType
                | 
                |     Returns or sets the algorithm type. Currently available algorithms are
                |     gradient and simulatedAnnealing
                | 
                |     See also:
                |         CatAlgorithmType

        :return: enum cat_algorithm_type
        :rtype: int
        """

        return self.optimization.AlgorithmType

    @algorithm_type.setter
    def algorithm_type(self, value: int):
        """
        :param int value: enum cat_algorithm_type
        """

        self.optimization.AlgorithmType = value

    @property
    def constraints(self) -> OptimizationConstraints:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property Constraints() As OptimizationConstraints (Read
                | Only)
                | 
                |     Returns the collection of optimization constraints.

        :rtype: OptimizationConstraints
        """

        return OptimizationConstraints(self.optimization.Constraints)

    @property
    def conv_speed(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property ConvSpeed() As long
                | 
                |     Returns or sets the convergence speed for some gradients and the simulated
                |     annealing.

        :rtype: int
        """

        return self.optimization.ConvSpeed

    @conv_speed.setter
    def conv_speed(self, value: int):
        """
        :param int value:
        """

        self.optimization.ConvSpeed = value

    @property
    def free_parameters(self) -> FreeParameters:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property FreeParameters() As FreeParameters (Read Only)
                | 
                |     Returns the collection of the free parameters.

        :rtype: FreeParameters
        """

        return FreeParameters(self.optimization.FreeParameters)

    @property
    def max_evals_nb(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property MaxEvalsNb() As long
                | 
                |     Returns or sets the maximum number of model updates allowed during one run
                |     of the optimization.

        :rtype: int
        """

        return self.optimization.MaxEvalsNb

    @max_evals_nb.setter
    def max_evals_nb(self, value: int):
        """
        :param int value:
        """

        self.optimization.MaxEvalsNb = value

    @property
    def max_evals_wo_improvement(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property MaxEvalsWoImprovement() As long
                | 
                |     Returns or sets the maximum number of model updates without improvement of
                |     the problem solution during one run of the optimization.

        :rtype: int
        """

        return self.optimization.MaxEvalsWoImprovement

    @max_evals_wo_improvement.setter
    def max_evals_wo_improvement(self, value: int):
        """
        :param int value:
        """

        self.optimization.MaxEvalsWoImprovement = value

    @property
    def max_time(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property MaxTime() As long
                | 
                |     Returns or sets the maximum time allowed for one run of the optimization
                |     (in minutes).

        :rtype: int
        """

        return self.optimization.MaxTime

    @max_time.setter
    def max_time(self, value: int):
        """
        :param int value:
        """

        self.optimization.MaxTime = value

    @property
    def objective_parameter(self) -> RealParam:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property ObjectiveParameter() As RealParam
                | 
                |     Returns or sets the objective parameter of the optimization. This parameter
                |     can not exist (in this case the get method returns E_FAIL) when the
                |     optimization contains only constraints and uses Simulated Annealing, or if the
                |     optimization feature doesn't contain all information necessary to be run.

        :rtype: RealParam
        """

        return RealParam(self.optimization.ObjectiveParameter)

    @objective_parameter.setter
    def objective_parameter(self, value: RealParam):
        """
        :param RealParam value:
        """

        self.optimization.ObjectiveParameter = value

    @property
    def optimization_type(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property OptimizationType() As CatOptimizationType
                | 
                |     Returns or sets the type of the optimization: minimum, maximum or target
                |     value searched on the objective parameter.
                | 
                |     See also:
                |         CatOptimizationType

        :return: enum cat_optimization_type
        :rtype: int
        """

        return self.optimization.OptimizationType

    @optimization_type.setter
    def optimization_type(self, value: int):
        """
        :param int value: enum cat_optimization_type
        """

        self.optimization.OptimizationType = value

    @property
    def target_value(self) -> RealParam:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property TargetValue() As RealParam (Read Only)
                | 
                |     Returns the objective parameter target value. (used only if the
                |     optimization type is a target value search)

        :rtype: RealParam
        """

        return RealParam(self.optimization.TargetValue)

    @property
    def use_max_evals_wo_improvement(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property UseMaxEvalsWoImprovement() As boolean
                | 
                |     Returns or sets if the number of updates without improvement of the
                |     solution has to be used as a termination criterion.

        :rtype: bool
        """

        return self.optimization.UseMaxEvalsWoImprovement

    @use_max_evals_wo_improvement.setter
    def use_max_evals_wo_improvement(self, value: bool):
        """
        :param bool value:
        """

        self.optimization.UseMaxEvalsWoImprovement = value

    @property
    def use_max_time(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property UseMaxTime() As boolean
                | 
                |     Returns or sets if max time has to be used as a termination criterion.

        :rtype: bool
        """

        return self.optimization.UseMaxTime

    @use_max_time.setter
    def use_max_time(self, value: bool):
        """
        :param bool value:
        """

        self.optimization.UseMaxTime = value

    def run(self, i_with_stop_dialog: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub Run(boolean iWithStopDialog)
                | 
                |     Runs the optimization as it is defined. The stop dialog appears if argument
                |     is TRUE
                |     Before running, a check is made to ensure that the optimization feature
                |     contains enough information to run the optimization. In the case where some
                |     information is missing, this method returns E_FAIL
                |     WARNING : if argument is TRUE, the optimization is launched asynchronously, and you can not run
                |               several optimizations in this mode.

        :param bool i_with_stop_dialog:
        :rtype: None
        """
        return self.optimization.Run(i_with_stop_dialog)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'run'
        # # vba_code = """
        # # Public Function run(optimization)
        # #     Dim iWithStopDialog (2)
        # #     optimization.Run iWithStopDialog
        # #     run = iWithStopDialog
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'Optimization(name="{self.name}")'
