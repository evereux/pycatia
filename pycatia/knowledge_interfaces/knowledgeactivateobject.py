#! /usr/bin/python3.6
# module initially auto generated using V5Automation.chm from CATIA V5 R25

from .knowledgeobject import KnowledgeObject


class KnowledgeActivateObject(KnowledgeObject):
    """
        .. note::
            CAA V5 Visual Basic help

                | Interface to access a CATIAKnowledgeActivableObject.

    """

    def __init__(self, knowledge_com_object):
        super().__init__(knowledge_com_object)
        self.knowledge_com_object = knowledge_com_object

    @property
    def activated(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Activated
                | o Property Activated(    ) As boolean
                | 
                | Returns whether the relation is activated. True if the relation is
                | activated. An activated relation is processed whenever the value of
                | one of its input parameter is modified.   Example: This example
                | retrieves whether the maximummass relation is activated, and if true,
                | displays the result in a message box:  If ( maximummass.Activated )
                | Then      MsgBox "maximummass is activated" End If


                | Parameters:


        """
        return self.knowledge_com_object.Activated

    def activate(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Activate
                | o Sub Activate(    )
                | 
                | Activates the relation. The relation will be processed whenever the
                | value of one of its input parameter is modified.  Example: This
                | example activates the maximummass relation:  maximummass.Activate()


                | Parameters:


        """
        return self.knowledge_com_object.Activate()

    def deactivate(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Deactivate
                | o Sub Deactivate(    )
                | 
                | Deactivates the relation. The relation will no longer be processed
                | when the value of one of its input parameter is modified.  Example:
                | This example deactivates the maximummass relation:
                | maximummass.Deactivate()


                | Parameters:


        """
        return self.knowledge_com_object.Deactivate()
