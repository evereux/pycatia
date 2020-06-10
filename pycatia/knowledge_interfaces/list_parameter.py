#! /usr/bin/python3.6
# module initially auto generated using V5Automation.chm from CATIA V5 R25

from .parameter import Parameter
from .list import List


class ListParameter(Parameter):
    """
        .. note::
            CAA V5 Visual Basic help

                | Represents a CATIAListParameter.

    """

    def __init__(self, com_parameter_object):
        super().__init__(com_parameter_object)
        self.listparameter = com_parameter_object

    @property
    def value_list(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | ValueList
                | o Property ValueList() As List
                | 
                | Returns or sets the value of the List object.


                | Parameters:


        """
        return List(self.listparameter.ValueList)
