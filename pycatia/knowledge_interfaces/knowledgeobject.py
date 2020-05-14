#! /usr/bin/python3.6
# module initially auto generated using V5Automation.chm from CATIA V5 R25

from pycatia.system_interfaces.base_object import AnyObject


class KnowledgeObject(AnyObject):
    """
        .. note::
            CAA V5 Visual Basic help

                | Interface to access a CATIAKnowledgeObject.

    """

    def __init__(self, knowledge_com_object):
        super().__init__(knowledge_com_object)
        self.knowledge_com_object = knowledge_com_object

    @property
    def hidden(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Hidden
                | o Property Hidden(    ) As boolean
                | 
                | Returns or sets wether the relation is hidden or should be hidden. or
                | not.


                | Parameters:


        """
        return self.knowledge_com_object.Hidden

    @property
    def is_const(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | IsConst
                | o Property IsConst(    ) As boolean
                | 
                | Returns or sets wether the relation is Const or should be Const. or
                | not.


                | Parameters:


        """
        return self.knowledge_com_object.IsConst
