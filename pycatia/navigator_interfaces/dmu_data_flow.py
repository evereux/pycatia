#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.any_object import AnyObject


class DMUDataFlow(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     DMUDataFlow
                | 
                | Allows the DMU Data Flow Management within the DMU Navigator
                | environment.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.dmu_data_flow = com_object

    def cache_export(self, i_directory: str, i_prefix: str, i_data: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub CacheExport(CATBSTR iDirectory,
                | CATBSTR iPrefix,
                | long iData)
                | 
                |     Exports all documents related to the product in a
                |     directory.
                | 
                |     Parameters:
                | 
                |         iDirectory
                |             The directory that will contain documents. 
                |         iPrefix
                |             The prefix used to save product documents. 
                |         iData
                |             To save geometries.
                | 
                |                 0: no save.
                |                 1: save.

        :param str i_directory:
        :param str i_prefix:
        :param int i_data:
        :rtype: None
        """
        return self.dmu_data_flow.CacheExport(i_directory, i_prefix, i_data)

    def cache_import(self, i_directory: str) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub CacheImport(CATBSTR iDirectory)
                | 
                |     Imports in the cache of marked documents in a directory.
                | 
                |     Parameters:
                | 
                |         iDirectory
                |             The directory that contains marked documents.

        :param str i_directory:
        :rtype: None
        """
        return self.dmu_data_flow.CacheImport(i_directory)

    def collapse(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub Collapse()
                | 
                |     Collapse the product by replacing all sub-product by corresponding
                |     components.

        :rtype: None
        """
        return self.dmu_data_flow.Collapse()

    def replace_by_cgr(self, i_directory: str, i_prefix: str) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub ReplaceByCGR(CATBSTR iDirectory,
                | CATBSTR iPrefix)
                | 
                |     Replaces all components of the product by the corresponding CGR located in
                |     a directory.
                | 
                |     Parameters:
                | 
                |         iDirectory
                |             The directory that will contain documents. 
                |         iPrefix
                |             The prefix used to save product documents.

        :param str i_directory:
        :param str i_prefix:
        :rtype: None
        """
        return self.dmu_data_flow.ReplaceByCGR(i_directory, i_prefix)

    def save_as_frozen(self, i_directory: str, i_prefix: str, i_data: int, i_cache: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SaveAsFrozen(CATBSTR iDirectory,
                | CATBSTR iPrefix,
                | long iData,
                | long iCache)
                | 
                |     Saves all documents related to the product in a directory.
                | 
                |     Parameters:
                | 
                |         iDirectory
                |             The directory that will contain documents. 
                |         iPrefix
                |             The prefix used to save product documents. 
                |         iData
                |             To save geometries.
                | 
                |                 0: no save.
                |                 1: save. 
                | 
                |         iCache
                |             To cache data.
                | 
                |                 0: no save.
                |                 1: save.

        :param str i_directory:
        :param str i_prefix:
        :param int i_data:
        :param int i_cache:
        :rtype: None
        """
        return self.dmu_data_flow.SaveAsFrozen(i_directory, i_prefix, i_data, i_cache)

    def __repr__(self):
        return f'DmuDataFlow(name="{self.name}")'
