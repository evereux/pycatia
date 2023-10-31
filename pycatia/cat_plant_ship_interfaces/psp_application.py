#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.any_object import AnyObject


class PSPApplication(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     PspApplication
                | 
                | Represents an application.
                | Role: To activate and query a Distributive System application.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.psp_application = com_object

    def initialization(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub Initialization()
                | 
                |     Initializes the application environment (load feature start up objects,
                |     activate the application..).
                | 
                |     Example:
                |
                |          Dim objPrdRoot        As Product
                |          Dim objPspWorkbench   As PspWorkbench
                |          Dim objPspApplnPip       As PspApplication
                |          Dim objPspApplnTub    As PspApplication
                | 
                |          Set objPrdRoot = CATIA.ActiveDocument.Product
                |          Set objPspWorkbench = objPrdRoot.GetTechnologicalObject ("PspWorkbench")
                |          
                |          Set objPspApplnPip = objPspWorkbench.GetApplication(catPspIDLCATPiping)
                |          ...
                |          objPspApplnPip.Initialization
                |          ....
                |          Set objPspApplnTub = objPspWorkbench.GetApplication(catPspIDLCATTubing)

        :rtype: None
        """
        return self.psp_application.Initialization()

    def __repr__(self):
        return f'PSPApplication(name="{self.name}")'
