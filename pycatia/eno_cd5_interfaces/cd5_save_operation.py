#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.eno_cd5_interfaces.cd5_save_items import CD5SaveItems
from pycatia.system_interfaces.any_object import AnyObject


class CD5SaveOperation(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     CD5SaveOperation
                | 
                | Represents a Save Operation Object.
                | 
                | Various properties which are applicable for the complete save operation can be
                | set using this.
                | Also, end-user may either run the Save operation as per customization done so
                | far or open the Advanced Save panel to finalize customization and run the Save
                | manually.
                | 
                | Example:
                | 
                |       The following example indicates how to create a ENOVIA V6 Save
                |       Operation.
                |      
                | 
                |      Dim oCD5Engine As CD5EngineV6R2014x
                |      Set oCD5Engine = CATIA.GetItem("CD5EngineV6R2014x")
                |      Dim oSaveOperation As CD5SaveOperation
                |      Set oSaveOperation = oCD5Engine.CreateSaveOperation(CD5SaveOperation_Session)
                |
                | See also:
                |     CD5SaveItems
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.cd5_save_operation = com_object

    @property
    def allow_disk_save(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property AllowDiskSave() As boolean
                | 
                |     Returns (gets) or sets the value of the Save option "Allow Disk
                |     Save".
                | 
                |     Example:
                | 
                |           The following example sets the Allow Disk Save option to
                |           True.
                |
                |          oSaveOperation.AllowDiskSave = True

        :rtype: bool
        """

        return self.cd5_save_operation.AllowDiskSave

    @allow_disk_save.setter
    def allow_disk_save(self, value: bool):
        """
        :param bool value:
        """

        self.cd5_save_operation.AllowDiskSave = value

    @property
    def comment(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Comment() As CATBSTR
                | 
                |     Returns (gets) or sets the value of the Save Comment.
                | 
                |     Example:
                | 
                |           The following example sets the Save Comment to
                |           "ABC".
                |
                |          oSaveOperation.Comment = "ABC"

        :rtype: str
        """

        return self.cd5_save_operation.Comment

    @comment.setter
    def comment(self, value: str):
        """
        :param str value:
        """

        self.cd5_save_operation.Comment = value

    @property
    def create_version(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property CreateVersion() As boolean
                | 
                |     Returns (gets) or sets the value of the Save option "Create Version". The
                |     default value is picked from the LCO/GCO.
                | 
                |     Example:
                | 
                |           The following example sets the Create Version option to
                |           True.
                |
                |          oSaveOperation.CreateVersion = True

        :rtype: bool
        """

        return self.cd5_save_operation.CreateVersion

    @create_version.setter
    def create_version(self, value: bool):
        """
        :param bool value:
        """

        self.cd5_save_operation.CreateVersion = value

    @property
    def items(self) -> CD5SaveItems:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Items() As CD5SaveItems (Read Only)
                | 
                |     Returns (gets) the collection of all the items in the scope of the
                |     Save.
                | 
                |     Example:
                | 
                |           The following example gets all the items in the scope of the
                |           Save.
                |          
                | 
                |          Dim oSaveItems As CD5SaveItems
                |          Set oSaveItems = oSaveOperation.Items

        :rtype: CD5SaveItems
        """

        return CD5SaveItems(self.cd5_save_operation.Items)

    @property
    def retain_lock(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property RetainLock() As boolean
                | 
                |     Returns (gets) or sets the value of the Save option "Retain Lock". The
                |     default value is picked from the LCO/GCO.
                | 
                |     Example:
                | 
                |           The following example sets the Retain Lock option to
                |           True.
                |
                |          oSaveOperation.RetainLock = True

        :rtype: bool
        """

        return self.cd5_save_operation.RetainLock

    @retain_lock.setter
    def retain_lock(self, value: bool):
        """
        :param bool value:
        """

        self.cd5_save_operation.RetainLock = value

    def run(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub Run()
                | 
                |     Runs the Save as per the cusomization done so far.
                | 
                |     Example:
                | 
                |           The following example executes the Save operation as per the
                |           customization done so far. 
                |
                |          oSaveOperation.Run

        :rtype: None
        """
        return self.cd5_save_operation.Run()

    def show_panel(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub ShowPanel()
                | 
                |     Shows the Save dialog as per the cusomization done so far.
                | 
                |     Example:
                | 
                |           The following example shows the Save panel as per the cusomization
                |           done so far.
                |
                |          oSaveOperation.ShowPanel

        :rtype: None
        """
        return self.cd5_save_operation.ShowPanel()

    def __repr__(self):
        return f'CD5SaveOperation(name="{self.name}")'
