#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.in_interfaces.document import Document
from pycatia.system_interfaces.any_object import AnyObject


class ProcessDocument(Document):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     InfInterfaces.Document
                |                         ProcessDocument
                | 
                | This interface is used to access the PPRDocument and to add a new
                | library.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.process_document = com_object

    @property
    def dnb_3d_state_position_management(self) -> AnyObject:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property DNB3DStatePositionManagement() As CATBaseDispatch (Read
                | Only)
                | 
                |     Retrieves the interface which manages the 3D state
                |     positions.
                | 
                |     Returns:
                |         The DNBIA3DStatePositionManagement corresponding to the current Process
                |         document.

        :rtype: AnyObject
        """

        return AnyObject(self.process_document.DNB3DStatePositionManagement)

    @property
    def ppr_document(self) -> AnyObject:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property PPRDocument() As CATBaseDispatch (Read Only)
                | 
                |     Retrieves the interface which manages the PPRDocument.
                | 
                |     Returns:
                |         The PPRDocument corresponding to the current Process document.

        :rtype: AnyObject
        """

        return AnyObject(self.process_document.PPRDocument)

    def add_library(self, i_file_name: str) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub AddLibrary(CATBSTR iFileName)
                | 
                |     Adds a new library to the current Process document.
                | 
                |     Parameters:
                | 
                |         iFileName
                |             The name of the library to be added.

        :param str i_file_name:
        :rtype: None
        """
        return self.process_document.AddLibrary(i_file_name)

    def __repr__(self):
        return f'ProcessDocument(name="{self.name}")'
