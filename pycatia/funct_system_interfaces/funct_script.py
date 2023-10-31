#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.any_object import AnyObject


class FunctScript(AnyObject):

    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     FunctScript
                | 
                | The interface to access a Functional Script.
                | 
                | It is managed on a Functional Element, thru the GenerativeKnowledge Facet
                | Manager (GKW).
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.funct_script = com_object

    @property
    def script_text(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ScriptText() As CATBSTR
                | 
                |     Get the ScriptText.

        :rtype: str
        """

        return self.funct_script.ScriptText

    @script_text.setter
    def script_text(self, value: str):
        """
        :param str value:
        """

        self.funct_script.ScriptText = value

    def __repr__(self):
        return f'FunctScript(name="{ self.name }")'
