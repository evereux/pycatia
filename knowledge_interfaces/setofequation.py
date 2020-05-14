#! /usr/bin/python3.6
# module initially auto generated using V5Automation.chm from CATIA V5 R25

from .relation import Relation


class SetOfEquation(Relation):
    """
        .. note::
            CAA V5 Visual Basic help

                | Represents the set of equations object.

    """

    def __init__(self, equation_set_com_object):
        super().__init__(equation_set_com_object)
        self.set_of_equation = equation_set_com_object

    def get_max_calculation_time(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetMaxCalculationTime
                | o Func GetMaxCalculationTime(    ) As long
                | 
                | Returns the maximum time of the model calculations.


                | Parameters:


        """
        return self.set_of_equation.GetMaxCalculationTime()

    def get_precision(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetPrecision
                | o Func GetPrecision(    ) As double
                | 
                | Returns the calculation precision.


                | Parameters:


        """
        return self.set_of_equation.GetPrecision()

    def get_symbolc_transformations(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetSymbolcTransformations
                | o Func GetSymbolcTransformations(    ) As boolean
                | 
                | Returns whether the Gauss method is used during the symbolic
                | transformation. TRUE if the Gauss method is used during the symbolic
                | transformation.


                | Parameters:


        """
        return self.set_of_equation.GetSymbolcTransformations()

    def is_stop_dialog(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | IsStopDialog
                | o Func IsStopDialog(    ) As boolean
                | 
                | Returns whether the "Stop Dialog" will be shown during calculations.
                | TRUE if the 'Stop Dialog' will be shown during calculations.


                | Parameters:


        """
        return self.set_of_equation.IsStopDialog()

    def set_max_calculation_time(self, i_max_time):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetMaxCalculationTime
                | o Sub SetMaxCalculationTime(    long    iMaxTime)
                | 
                | Sets a maximum time to the model calculations.


                | Parameters:


        """
        return self.set_of_equation.SetMaxCalculationTime(i_max_time)

    def set_parameter_as_input(self, i_parameter):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetParameterAsInput
                | o Sub SetParameterAsInput(    Parameter    iParameter)
                | 
                | Specifies that the parameter must be considered as input parameter.


                | Parameters:
                | iParameter
                |  The parameter to set up as input of the SetOfEquationObject


        """
        return self.set_of_equation.SetParameterAsInput(i_parameter)

    def set_parameter_as_output(self, i_parameter):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetParameterAsOutput
                | o Sub SetParameterAsOutput(    Parameter    iParameter)
                | 
                | Specifies that the parameter must be considered as an output
                | parameter.


                | Parameters:
                | iParameter
                |  The parameter to set up as output of the SetOfEquationObject


        """
        return self.set_of_equation.SetParameterAsOutput(i_parameter)

    def set_precision(self, i_eps):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetPrecision
                | o Sub SetPrecision(    double    iEps)
                | 
                | Sets the calculation precision.


                | Parameters:
                | iEps
                |  a precision Legal values: 1e-10 ≤ iEps ≤ 0.1


        """
        return self.set_of_equation.SetPrecision(i_eps)

    def use_stop_dialog(self, i_used):
        """
        .. note::
            CAA V5 Visual Basic help

                | UseStopDialog
                | o Sub UseStopDialog(    boolean    iUsed)
                | 
                | Specifies whether the 'Stop Dialog' should be shown during
                | calculations. TRUE to show the 'Stop Dialog' during calculations.


                | Parameters:


        """
        return self.set_of_equation.UseStopDialog(i_used)

    def use_symbolc_transformations(self, i_gauss):
        """
        .. note::
            CAA V5 Visual Basic help

                | UseSymbolcTransformations
                | o Sub UseSymbolcTransformations(    boolean    iGauss)
                | 
                | Specifies whether the Gauss method should be used during the symbolic
                | transformation. TRUE to use the Gauss method during the symbolic
                | transformation.


                | Parameters:


        """
        return self.set_of_equation.UseSymbolcTransformations(i_gauss)

    def __repr__(self):
        return f'SetOfEquation(name="{self.name}")'
