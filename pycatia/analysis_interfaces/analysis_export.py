#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.analysis_interfaces.analysis_manager import AnalysisManager
from pycatia.system_interfaces.any_object import AnyObject


class AnalysisExport(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     AnalysisExport
                | 
                | The interface to access a CATIAAnalysisExport
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.analysis_export = com_object

    def export(self, i_full_path: str, i_type: str, i_occurrences: tuple, i_manager: AnalysisManager) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub Export(CATBSTR iFullPath,
                | CATBSTR iType,
                | CATSafeArrayVariant iOccurrences,
                | AnalysisManager iManager)
                | 
                |     Export computed loads/displacements as a CATAnalysisExport
                |     file.
                | 
                |     Parameters:
                | 
                |         iFullPath
                |             The full path of the file.
                |             (Example:
                |             “E:\tmp\ExportedLoads/CATAnalysisExport”).
                |         iType
                |             The type of data to be exported: "ComputedLoads" or
                |             "Displacements".
                |         iOccurrences
                |             The list of occurrences to be exported.
                |         iManager
                |             The analysis model for which the data will be
                |             exported.
                |             (Only revelant for assembly of analysis.
                |             )

        :param str i_full_path:
        :param str i_type:
        :param tuple i_occurrences:
        :param AnalysisManager i_manager:
        :return: None
        :rtype: None
        """
        return self.analysis_export.Export(i_full_path, i_type, i_occurrences, i_manager.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'export'
        # # vba_code = """
        # # Public Function export(analysis_export)
        # #     Dim iFullPath (2)
        # #     analysis_export.Export iFullPath
        # #     export = iFullPath
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'AnalysisExport(name="{self.name}")'