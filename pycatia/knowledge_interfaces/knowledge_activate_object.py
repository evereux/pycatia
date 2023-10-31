#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.knowledge_interfaces.knowledge_object import KnowledgeObject


class KnowledgeActivateObject(KnowledgeObject):

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
                |                         KnowledgeActivateObject
                | 
                | Interface to access a CATIAKnowledgeActivableObject.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.knowledge_activate_object = com_object

    @property
    def activated(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property Activated() As boolean (Read Only)
                | 
                |     Returns whether the relation is activated.
                |     True if the relation is activated. An activated relation is processed
                |     whenever the value of one of its input parameter is
                |     modified.
                | 
                |     Example:
                |         This example retrieves whether the maximummass relation is activated,
                |         and if true, displays the result in a message box:
                | 
                |          If ( maximummass.Activated ) Then
                |               MsgBox "maximummass is activated"
                |          End If

        :rtype: bool
        """

        return self.knowledge_activate_object.Activated

    def activate(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub Activate()
                | 
                |     Activates the relation. The relation will be processed whenever the value
                |     of one of its input parameter is modified.
                | 
                |     Example:
                |         This example activates the maximummass relation:
                | 
                |          maximummass.Activate()

        :rtype: None
        """
        return self.knowledge_activate_object.Activate()

    def deactivate(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub Deactivate()
                | 
                |     Deactivates the relation. The relation will no longer be processed when the
                |     value of one of its input parameter is modified.
                | 
                |     Example:
                |         This example deactivates the maximummass relation:
                | 
                |          maximummass.Deactivate()

        :rtype: None
        """
        return self.knowledge_activate_object.Deactivate()

    def __repr__(self):
        return f'KnowledgeActivateObject(name="{ self.name }")'
