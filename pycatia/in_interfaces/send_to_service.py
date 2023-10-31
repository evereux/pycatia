#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.any_object import AnyObject


class SendToService(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SendToService
                | 
                | This interface allows to use 'Send To' functionalities through an
                | API.
                | Example: Set Send=CATIA.CreateSendTo()
                | This interface requires the installation of CATIA - PPR xPDM Gateway 1 Product
                | (PX1) or the installation of the CATIA-SmarTeam plugin. In case one of these
                | products is not granted, the first invocation to one of CATIASendToService
                | methods will fail.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.send_to_service = com_object

    def add_file(self, i_path: str) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub AddFile(CATBSTR iPath)
                | 
                |     Adds a file to the list of the files 'to be copied'. This method verifies
                |     that the given input file is valid (exists and is not a directory), it
                |     recursively adds pointed files.
                | 
                |     Parameters:
                | 
                |         iPath
                |             : The path of the file to be added to the list of the 'to be copied' files. 
                |         Example:
                |             Send.AddFile(iPath)

        :param str i_path:
        :rtype: None
        """
        return self.send_to_service.AddFile(i_path)

    def get_last_send_to_method_error(self, o_error_param: str, o_error_code: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub GetLastSendToMethodError(CATBSTR oErrorParam,
                | long oErrorCode)
                | 
                |     Retreives the diagnosis related to the last call to SendToService
                |     interface.
                | 
                |     Parameters:
                | 
                |         oErrorParam
                |             A parameter string given together with the error code.
                |             
                |         oErrorCode
                |             The last executed method error code:
                |             code diagnosisoErrorParam value
                |             0 action successfully performed :-)
                |             1 PX1 license not granted 
                |             2 internal error 
                |             5 file already in the list file name
                |             6 file is not in the list file name
                |             7 empty file list 
                |             8 missing target directory 
                |             9 no common root directory 
                |             10 file does not exist file name
                |             11 input is a directory directory name
                |             12 directory check failed directory name
                |             13 invalid file name given name
                |             14 file has no read permission given name
                |             36 allocation failed :-( 

        :param str o_error_param:
        :param int o_error_code:
        :rtype: None
        """
        return self.send_to_service.GetLastSendToMethodError(o_error_param, o_error_code)

    def get_list_of_dependant_file(self, o_dependant: tuple) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub GetListOfDependantFile(CATSafeArrayVariant oDependant)
                | 
                |     Retrieves the complete list of the files recursively pointed by the file given in argument to 
                |     SetInitialFile method. 
                |     Notice : in case AddFile has also been invoked, the files recursively pointed by the added file 
                |     also are retrieved.
                | 
                |     Parameters:
                | 
                |         oDependant
                |             : The table of dependant files. 
                |         Example:
                |             Send.GetListOfDependantFile(oDependant)

        :param tuple o_dependant:
        :rtype: None
        """
        return self.send_to_service.GetListOfDependantFile(o_dependant)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_list_of_dependant_file'
        # # vba_code = """
        # # Public Function get_list_of_dependant_file(send_to_service)
        # #     Dim oDependant (2)
        # #     send_to_service.GetListOfDependantFile oDependant
        # #     get_list_of_dependant_file = oDependant
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_list_of_to_be_copied_files(self, o_will_be_copied: tuple) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub GetListOfToBeCopiedFiles(CATSafeArrayVariant
                | oWillBeCopied)
                | 
                |     Retreives the complete list of the files that will be copied. This list
                |     matches the list of dependant files, but without the files for which RemoveFile
                |     has been invoked.
                | 
                |     Parameters:
                | 
                |         oWillBeCopied
                |             : The table of the files that will be copied. 
                |         Example:
                |             Send.GetListOfToBeCopiedFiles(oWillBeCopied)

        :param tuple o_will_be_copied:
        :rtype: None
        """
        return self.send_to_service.GetListOfToBeCopiedFiles(o_will_be_copied)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_list_of_to_be_copied_files'
        # # vba_code = """
        # # Public Function get_list_of_to_be_copied_files(send_to_service)
        # #     Dim oWillBeCopied (2)
        # #     send_to_service.GetListOfToBeCopiedFiles oWillBeCopied
        # #     get_list_of_to_be_copied_files = oWillBeCopied
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def keep_directory(self, i_keep: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub KeepDirectory(boolean iKeep)
                | 
                |     Controls the directory tree structure in the target
                |     directory.
                | 
                |     Parameters:
                | 
                |         iKeep
                |             =1: to preserve the relative tree structure of the
                |             files.
                |             This option will be effective only if there is a common root
                |             directory for all files. 
                |         iKeep
                |             =0: to copy the files directly in the destination directory
                |             
                |         Example:
                |             Send.KeepDirectory(ikeep)

        :param bool i_keep:
        :rtype: None
        """
        return self.send_to_service.KeepDirectory(i_keep)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'keep_directory'
        # # vba_code = """
        # # Public Function keep_directory(send_to_service)
        # #     Dim iKeep (2)
        # #     send_to_service.KeepDirectory iKeep
        # #     keep_directory = iKeep
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def remove_file(self, i_file: str) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub RemoveFile(CATBSTR iFile)
                | 
                |     Removes a file from the list of the files that will be
                |     copied.
                | 
                |     Parameters:
                | 
                |         iFile
                |             : The File (With extension) to be removed from the list of the 'to be copied' files. 
                |         Example:
                |             Send.RemoveFile(iFile)

        :param str i_file:
        :rtype: None
        """
        return self.send_to_service.RemoveFile(i_file)

    def run(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub Run()
                | 
                |     Executes the copy action, according to previously set files and
                |     options.
                |     A "report.txt" report file is generated in the specified destination
                |     directory.

        :rtype: None
        """
        return self.send_to_service.Run()

    def set_directory_file(self, i_directory: str) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetDirectoryFile(CATBSTR iDirectory)
                | 
                |     Positions the destination directory. This method verifies that the given
                |     directory exists. Be careful, if SetDirectoryOneFile method has been previously
                |     called, its action is overriden by this SetDirectoryFile
                |     call.
                | 
                |     Parameters:
                | 
                |         iDirectory
                |             : The destination directory where the files will be copied. 
                |         Example:
                |             Send.SetDirectoryFile(iDirectory)

        :param str i_directory:
        :rtype: None
        """
        return self.send_to_service.SetDirectoryFile(i_directory)

    def set_directory_one_file(self, i_file: str, i_directory: str) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetDirectoryOneFile(CATBSTR iFile,
                | CATBSTR iDirectory)
                | 
                |     Allows positioning the destination directory for one given file to be
                |     copied. The file will be copied in the specified target directory. Be careful
                |     that using this method implies that the 'KeepDirectory' variable will be
                |     automatically set to 0.
                | 
                |     Parameters:
                | 
                |         iFile
                |             : The name (Name With extension) of the given file. 
                |         iDirectory
                |             : The directory where this file will be copied. 
                |         Example:
                |             Send.SetDirectoryOneFile(iFile, iDirectory)

        :param str i_file:
        :param str i_directory:
        :rtype: None
        """
        return self.send_to_service.SetDirectoryOneFile(i_file, i_directory)

    def set_initial_file(self, i_path: str) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetInitialFile(CATBSTR iPath)
                | 
                |     Sets the initial file to be copied. This method verifies that the given
                |     input file is valid (exists and is not a directory)
                |     It generates a complete list of the recursively dependent files to be
                |     copied. 
                | Example:
                |     This example positions the file of path ipath in the list of 'to be copied'
                |     files. All its dependant files will also be added in the list of 'to be copied'
                |     files.
                | 
                |     Parameters:
                | 
                |         iPath
                |             : Full path of the file to be copied.
                | 
                |              Send.SetInitialFile(iPath)

        :param str i_path:
        :rtype: None
        """
        return self.send_to_service.SetInitialFile(i_path)

    def set_rename_file(self, i_oldname: str, i_new_name: str) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetRenameFile(CATBSTR iOldname,
                | CATBSTR iNewName)
                | 
                |     Renames one file to be copied. The new name may not have invalid
                |     characters
                | 
                |     Parameters:
                | 
                |         iOldname
                |             : The old file name (With extension). 
                |         iNewName
                |             : The new file name (Without extension). 
                |         Example:
                |             Send.SetRenameFile(iOldname, iNewName)

        :param str i_oldname:
        :param str i_new_name:
        :rtype: None
        """
        return self.send_to_service.SetRenameFile(i_oldname, i_new_name)

    def __repr__(self):
        return f'SendToService(name="{self.name}")'
