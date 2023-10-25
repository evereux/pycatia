#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.eno_cd5_interfaces.cd5_id import CD5ID
from pycatia.system_interfaces.any_object import AnyObject


class CD5SaveItem(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     CD5SaveItem
                | 
                | Represents a save object which user is trying to save.
                | 
                | Various properties on the object help the end-user to customize each object
                | individually.
                | 
                | Example:
                | 
                |       The following example indicates how to retrieve an item in the scope of a
                |       Save Operation.
                |
                |      Dim oCD5Engine As CD5EngineV6R2014x
                |      Set oCD5Engine = CATIA.GetItem("CD5EngineV6R2014x")
                |      Dim oSaveOperation As CD5SaveOperation
                |      Set oSaveOperation = oCD5Engine.CreateSaveOperation(CD5SaveOperation_Session)
                |      Dim oSaveItems As CD5SaveItems
                |      Set oSaveItems = oSaveOperation.Items()
                |      Dim oSaveItem As CD5SaveItem
                |      Set oSaveItem = oSaveItems.Item(1)
                |
                | See also:
                |     CD5SaveItems
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.cd5_save_item = com_object

    @property
    def cd5_id(self) -> CD5ID:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property CD5ID() As CD5ID (Read Only)
                | 
                |     Returns (gets) the CD5ID for a save item.
                | 
                |     Example:
                | 
                |           The following example gets CD5ID from a save item.
                |
                |          Dim myID As CD5ID
                |          Set myID = oSaveItem.CD5ID

        :rtype: CD5ID
        """

        return CD5ID(self.cd5_save_item.CD5ID)

    @property
    def derived_outputs(self) -> tuple:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property DerivedOutputs(CATSafeArrayVariant
                | DerivedOutputs)
                | 
                |     Returns (gets) or sets the Derived Outputs for a save
                |     item.
                | 
                |     Example:
                | 
                |           The following example sets Derived Outputs from a save
                |           item.
                |
                |          Dim iDerivedOutputs(1) As CATBSTR
                |          iDerivedOutputs(0) = "cgrOutput"
                |          oSaveItem.DerivedOutputs = iDerivedOutputs

        :rtype: tuple
        """

        return self.cd5_save_item.DerivedOutputs

    @derived_outputs.setter
    def derived_outputs(self, value: tuple):
        """
        :param tuple value:
        """

        self.cd5_save_item.DerivedOutputs = value

    @property
    def included(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Included() As boolean
                | 
                |     Returns (gets) or sets whether item should be included in the Save
                |     Operation. The default value is determined by the status of the item. Objects
                |     with status "Exists" are not selected by default.
                | 
                |     Example:
                | 
                |           The following example includes the item for the Save
                |           operation.
                |
                |          oSaveItem.Included = True

        :rtype: bool
        """

        return self.cd5_save_item.Included

    @included.setter
    def included(self, value: bool):
        """
        :param bool value:
        """

        self.cd5_save_item.Included = value

    @property
    def next_revision(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property NextRevision() As CATBSTR (Read Only)
                | 
                |     Returns the next combined revision and version string for this
                |     CD5SaveItem.
                |     If next revision of the item is to be created, then CD5SaveItem.Revision
                |     may be set to this value.
                | 
                |     Example:
                | 
                |           The following example gets the NextRevision of the
                |           item.
                |
                |          CD5SaveItem.Revision = CD5SaveItem.NextRevision

        :rtype: str
        """

        return self.cd5_save_item.NextRevision

    @property
    def object_name(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ObjectName() As CATBSTR
                | 
                |     Returns (gets) or sets the value of the ENOVIA Object
                |     Name.
                | 
                |     Example:
                | 
                |           The following example sets the Object Name.
                |
                |          oSaveItem.ObjectName = "MyPart"

        :rtype: str
        """

        return self.cd5_save_item.ObjectName

    @object_name.setter
    def object_name(self, value: str):
        """
        :param str value:
        """

        self.cd5_save_item.ObjectName = value

    @property
    def possible_derived_outputs(self) -> tuple:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property PossibleDerivedOutputs() As CATSafeArrayVariant (Read
                | Only)
                | 
                |     Returns (gets) the possible Derived Outputs for a save
                |     item.
                | 
                |     Example:
                | 
                |           The following example gets Possible DerivedOutputs from a save
                |           item.
                |
                |          Dim oPossibleDerivedOutputs As CATSafeArrayVariant
                |          oPossibleDerivedOutputs = oSaveItem.PossibleDerivedOutputs

        :rtype: tuple
        """

        return self.cd5_save_item.PossibleDerivedOutputs

    @property
    def possible_types(self) -> tuple:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property PossibleTypes() As CATSafeArrayVariant (Read Only)
                | 
                |     Returns (gets) the possible Types for a save item.
                | 
                |     Example:
                | 
                |           The following example gets PossibleTypes from a save
                |           item.
                |
                |          Dim oPossibleTypes As CATSafeArrayVariant
                |          oPossibleTypes = oSaveItem.PossibleTypes

        :rtype: tuple
        """

        return self.cd5_save_item.PossibleTypes

    @property
    def revision(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Revision() As CATBSTR
                | 
                |     Returns or sets the target revision of the CD5SaveItem for the Save
                |     Operation. Default value is current CD5SaveItem target
                |     revision.
                |     Get: will return string combining revision and version (ex:
                |     "B.3").
                |     Set: will keep the revision string only (e.g. "A", "BB"), even if combining
                |     revision and version is passed.
                | 
                |     Note:
                |         As revision part of the string cannot contain ‘.’ character, given
                |         string may be truncated up to the first ‘.’ character’ before being appended
                |         with appropriate version number.
                |         (ex: MyItem.Revision = "AA.BB" => property is set to "AA.0")
                |         It is advised to read the Revision property after it has been set as
                |         the current value may not match what has been set. 
                |         Changing the CD5SaveOperation.CreateVersion value may affect the
                |         version part of this property.
                | 
                |         Example:
                | 
                |               The following example gets the targeted Revision for the
                |               item.
                |
                |              Dim oRevision As CATBSTR
                |              oRevision = CD5SaveItem.Revision

        :rtype: str
        """

        return self.cd5_save_item.Revision

    @revision.setter
    def revision(self, value: str):
        """
        :param str value:
        """

        self.cd5_save_item.Revision = value

    @property
    def status(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Status() As CD5SaveItem_Status (Read Only)
                | 
                |     Returns (gets) the Save status of the item.
                | 
                |     Example:
                | 
                |           The following example gets item Status.
                |
                |          Dim itemStatus As CD5SaveItem_Status
                |          itemStatus = oSaveItem.Status

        :return: enum cd5_save_item_status
        :rtype: int
        """

        return self.cd5_save_item.Status

    @property
    def type(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Type() As CATBSTR
                | 
                |     Returns (gets) or sets the Type of the item. The default value is picked
                |     from the GCO. To set a type user can get the list of Possible Types from
                |     PossibleTypes property
                | 
                |     Example:
                | 
                |           The following example gets the type of the item.
                |
                |          Dim oType As CATBSTR
                |          oType = oSaveItem.Type

        :rtype: str
        """

        return self.cd5_save_item.Type

    @type.setter
    def type(self, value: str):
        """
        :param str value:
        """

        self.cd5_save_item.Type = value

    def __repr__(self):
        return f'CD5SaveItem(name="{self.name}")'
