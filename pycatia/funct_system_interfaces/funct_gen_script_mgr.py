#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.funct_system_interfaces.funct_scripts import FunctScripts
from pycatia.funct_system_interfaces.functional_facet import FunctionalFacet


class FunctGenScriptMgr(FunctionalFacet):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     CATFunctSystemItf.FunctionalFacet
                |                         FunctGenScriptMgr
                | 
                | The interface to access a Functional GenerativeScripts
                | manager.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.funct_gen_script_mgr = com_object

    @property
    def current_script(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property CurrentScript() As long
                | 
                |     Get the CurrentScript.

        :rtype: int
        """

        return self.funct_gen_script_mgr.CurrentScript

    @current_script.setter
    def current_script(self, value: int):
        """
        :param int value:
        """

        self.funct_gen_script_mgr.CurrentScript = value

    @property
    def scripts(self) -> FunctScripts:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Scripts() As FunctScripts (Read Only)
                | 
                |     Get the Generative Scripts collection.

        :rtype: FunctScripts
        """

        return FunctScripts(self.funct_gen_script_mgr.Scripts)

    def __repr__(self):
        return f'FunctGenScriptMgr(name="{self.name}")'
