#! /usr/bin/python3.6
# module initially auto generated using V5Automation.chm from CATIA V5 R25

from .relation import Relation


class Law(Relation):
    """
        .. note::
            CAA V5 Visual Basic help

                | Represents the Law object.

    """

    def __init__(self, law_com_object):
        super().__init__(law_com_object)
        self.law = law_com_object

    def add_formal_parameter(self, i_name, i_magnitude):
        """
        .. note::
            CAA V5 Visual Basic help

                | AddFormalParameter
                | o Sub AddFormalParameter(    CATBSTR    iName,
                |                              CATBSTR    iMagnitude)
                | 
                | Creates a formal parameter for the law.


                | Parameters:
                | iName
                |     The name of the formal parameter.
                |  
                |  iType
                |     The type name of the formal parameter.


        """
        return self.law.AddFormalParameter(i_name, i_magnitude)

    def remove_formal_parameter(self, i_name):
        """
        .. note::
            CAA V5 Visual Basic help

                | RemoveFormalParameter
                | o Sub RemoveFormalParameter(    CATBSTR    iName)
                | 
                | Removes a formal parameter of the law.


                | Parameters:
                | iName
                |     The name of the formal parameter.


        """
        return self.law.RemoveFormalParameter(i_name)

    def __repr__(self):
        return f'Law(name="{self.name}")'
