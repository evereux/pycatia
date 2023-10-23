#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.any_object import AnyObject


class CD5Template(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     CD5Template
                | 
                | Represents a Template.
                | 
                | Various properties on the object helps to perform operations on the
                | template.
                | 
                | Example:
                | 
                |       The following example indicates how to retrieve the
                |       template.
                |
                |      Dim oTemplate As ENOIACD5Template
                |      Set oTemplate = oTemplates.Item(1)
                |
                | See also:
                |     CD5Templates
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.cd5_template = com_object

    @property
    def template_name(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property TemplateName() As CATBSTR (Read Only)
                | 
                |     Returns (gets) the name of the Template.
                | 
                |     Example:
                | 
                |           The following example gets the name of the Template.
                |
                |          Dim oName As CATBSTR
                |          oName = oTemplate.TemplateName

        :rtype: str
        """

        return self.cd5_template.TemplateName

    @property
    def template_type(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property TemplateType() As CATBSTR (Read Only)
                | 
                |     Returns (gets) the type of the Template.
                | 
                |     Example:
                | 
                |           The following example gets the type of the Template.
                |
                |          Dim oType As CATBSTR
                |          oType = oTemplate.TemplateType

        :rtype: str
        """

        return self.cd5_template.TemplateType

    def download_file(self, i_target_folder: str) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func DownloadFile(CATBSTR iTargetFolder) As CATBSTR
                | 
                |     Downloads the template file to local disk.
                | 
                |     Parameters:
                | 
                |         iiTargetFolder
                |             The Folder Path on local disk where the template file will be
                |             downloaded. 
                | 
                |     Returns:
                |         Full path of the downloaded file. 
                |     Throws:
                | 
                |         -1782306828 : Template object is assigned more than one file.
                |         -1774688310 : Template object is not assigned any file.
                |         -1866082326 : File of same name as that of file assigned to Template object
                |                       is present on download directory.
                | 
                |     Example:
                | 
                |           The following example downloads the template file to local disk
                |           oTemplate:
                |
                |             iTargetFolder : "E:/New folder".
                |
                |          Dim DownloadedFilePath As CATBSTR
                |          DownloadedFilePath = oTemplate.DownloadFile("E:/New folder")

        :param str i_target_folder:
        :rtype: str
        """
        return self.cd5_template.DownloadFile(i_target_folder)

    def __repr__(self):
        return f'CD5Template(name="{self.name}")'
