#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.space_analyses_interfaces.conflicts import Conflicts
from pycatia.system_interfaces.any_object import AnyObject


class ClashResult(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     ClashResult
                | 
                | Represents the ClashResult object.
                | The ClashResult object is a set of conflicts resulting from a clash
                | detection.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.clash_result = com_object

    @property
    def conflicts(self) -> Conflicts:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Conflicts() As Conflicts (Read Only)
                | 
                |     Returns the collection of computed Conflicts.
                | 
                |     Example:
                | 
                |              This example retrieves the conflicts of NewClashResult
                |              ClashResult.
                |
                |             Dim NewConflicts As Conflicts
                |             Set NewConflicts = NewClashResult.Conflicts

        :rtype: Conflicts
        """

        return Conflicts(self.clash_result.Conflicts)

    def export(self, i_type: int, i_path: str) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub Export(CatClashExportType iType,
                | CATBSTR iPath)
                | 
                |     Exports the results in a XML file.
                | 
                |     Parameters:
                | 
                |         iType
                |             The type of export. 
                |         iPath
                |             The path of the file. 
                | 
                |     Example:
                | 
                |              This example exports the results of NewClashResult
                |              ClashResult.
                |
                |             Dim ThePath As String
                |             NewClashResult.Export CatClashExportTypeXMLResultOnly,
                |             "c:\\tmp\\sample.xml"

        :param int i_type: enum cat_clash_export_type
        :param str i_path:
        :rtype: None
        """
        return self.clash_result.Export(i_type, i_path)

    def __repr__(self):
        return f'ClashResult(name="{self.name}")'
