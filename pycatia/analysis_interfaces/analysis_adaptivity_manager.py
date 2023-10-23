#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.analysis_interfaces.analysis_set import AnalysisSet


class AnalysisAdaptivityManager(AnalysisSet):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     CATAnalysisInterfaces.AnalysisSet
                |                         AnalysisAdaptivityManager
                | 
                | The interface to access a CATIAAnalysisAdaptivityManager.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.analysis_adaptivity_manager = com_object

    def run(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub Run()
                | 
                |     Run the adaptivity process.

        :rtype: None
        """
        return self.analysis_adaptivity_manager.Run()

    def __repr__(self):
        return f'AnalysisAdaptivityManager(name="{self.name}")'
