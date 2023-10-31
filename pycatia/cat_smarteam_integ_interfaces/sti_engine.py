#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.cat_smarteam_integ_interfaces.sti_db_item import StiDBItem
from pycatia.system_interfaces.any_object import AnyObject


class StiEngine(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     StiEngine
                | 
                | Represents the SmarTeam Integration Engine, that is to say the entry point to
                | the CATIA/SmarTeam Integration.
                | 
                | It allows end user to realize the following operations (also called StiEngine
                | methods): connection and disconnection to SmarTeam Integration, creation of
                | SmarTeam Integration Objects (StiDBItem) and management of their lifecycle
                | (Save, Check In, Check Out, Release, New Release, ...).
                | Note that all operations performed from this interface are the same as
                | operations available and launched from the SmarTeam menu in
                | CATIA.
                | Warning: By Default, these operations launched from this interface are executed
                | Without Panel.
                | 
                | Example:
                | 
                |       The following example indicates how to retrieve the SmarTeam Integration
                |       Engine.
                | 
                |      Dim oStiEngine As StiEngine
                |      Set oStiEngine = CATIA.GetItem("CAIEngine")
                | 
                | See also:
                |     StiDBItem
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.sti_engine = com_object

    @property
    def integration_type(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property IntegrationType() As CATBSTR (Read Only)
                | 
                |     Returns the Engine Integration Type.
                |     Warning: Do Not use this method. It is Not implemented.

        :rtype: str
        """

        return self.sti_engine.IntegrationType

    @property
    def use_graphical_ui(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property UseGraphicalUI() As boolean
                | 
                |     Returns (gets) or sets the use of Graphical User Interface (GUI) in order
                |     to display or not panels. This method allows programmer to define if methods of
                |     this Interface Definition Language (IDL) will be executed With or Without user
                |     interactions.
                |     Warning: By Default, operations launched from this interface are executed
                |     Without GUI, that is to say 'UseGraphicalUI' is set to 'False'. In practice, No
                |     GUI means that treatments are executed With Default Values because additional
                |     parameters or options can not be set, as there is no user interaction. If GUI
                |     are allowed, panels will be displayed. These panels correspond to the usual
                |     ones displayed when the corresponding functionnalities are launched from the
                |     SmarTeam Intagration menu. The behaviour is so the same as in Interactive
                |     Mode.
                |     Note that the Connection to SmarTeam Integration is totally Independent of
                |     the Value of UseGraphicalUI.
                | 
                |     Example:
                | 
                |           The following example returns in the boolean bIsActive the current
                |           value of this option -that is to say 
                |          if we use or not GUI for StiEngine methods- and then sets it -if
                |          needed- to 'True' -that corresponds to GUI operating
                |          mode.
                |
                |          Dim oStiEngine As StiEngine
                |          Set oStiEngine = CATIA.GetItem("CAIEngine")
                |          Dim bIsActive As boolean
                |          bIsActive = oStiEngine.UseGraphicalUI
                |          If Not bIsActive Then
                |              oStiEngine.UseGraphicalUI = True
                |          End If

        :rtype: bool
        """

        return self.sti_engine.UseGraphicalUI

    @use_graphical_ui.setter
    def use_graphical_ui(self, value: bool):
        """
        :param bool value:
        """

        self.sti_engine.UseGraphicalUI = value

    def build_doc_db_item_from_smar_team_id(self, iobject_id: int, iclass_id: int) -> StiDBItem:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func BuildDocDBItemFromSmarTeamID(long iobjectId,
                | short iclassId) As StiDBItem
                | 
                |     Copys the SmarTeam object -and its children- to default Work directory,
                |     opens it into CATIA session and returns the corresponding
                |     CATIAStiDBItem.
                |     Note that this method is always executed Without any GUI and is so totally
                |     independent of the value returned by 'UseGraphicalUI'.
                | 
                |     Parameters:
                | 
                |         iobjectId
                |             This input corresponds to the Object ID of the required SmarTeam
                |             object. 
                |         iclassId
                |             This input corresponds to the Class ID of the required SmarTeam
                |             object. 
                | 
                |     Returns:
                |         This output corresponds to the retrieved CATIAStiDBItem.
                |         
                |     Example:
                | 
                |           The following example retrieves a loaded document corresponding to a
                |           SmarTeam ID {Object ID, Class ID}.
                |          
                | 
                |          Dim oStiEngine As StiEngine
                |          Set oStiEngine = CATIA.GetItem("CAIEngine")
                |          Dim iobjectId As long
                |          iobjectId = 963
                |          Dim iclassId As short
                |          iclassId = 57
                |          Dim oStiDBItem As StiDBItem
                |          Set oStiDBItem = oStiEngine.BuildDocDBItemFromSmarTeamID iobjectId, iclassId

        :param int iobject_id:
        :param int iclass_id:
        :rtype: StiDBItem
        """
        return StiDBItem(self.sti_engine.BuildDocDBItemFromSmarTeamID(iobject_id, iclass_id))

    def build_file_db_item_from_smar_team_id(self, iobject_id: int, iclass_id: int) -> StiDBItem:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func BuildFileDBItemFromSmarTeamID(long iobjectId,
                | short iclassId) As StiDBItem
                | 
                |     Copys the SmarTeam object -and its children- to default Work directory and
                |     returns the corresponding CATIAStiDBItem, Without opening the file into CATIA
                |     session.
                |     Note that this method is always executed Without any GUI and is so totally
                |     independent of the value returned by 'UseGraphicalUI'.
                | 
                |     Parameters:
                | 
                |         iobjectId
                |             This input corresponds to the Object ID of the required SmarTeam
                |             object. 
                |         iclassId
                |             This input corresponds to the Class ID of the required SmarTeam
                |             object. 
                | 
                |     Returns:
                |         This output corresponds to the retrieved CATIAStiDBItem.
                |         
                |     Example:
                | 
                |           The following example retrieves a loaded document corresponding to a
                |           SmarTeam ID {Object ID, Class ID}.
                |
                |          Dim oStiEngine As StiEngine
                |          Set oStiEngine = CATIA.GetItem("CAIEngine")
                |          Dim iobjectId As long
                |          iobjectId = 963
                |          Dim iclassId As short
                |          iclassId = 57
                |          Dim oStiDBItem As StiDBItem
                |          Set oStiDBItem = oStiEngine.BuildFileDBItemFromSmarTeamID iobjectId, iclassId

        :param int iobject_id:
        :param int iclass_id:
        :rtype: StiDBItem
        """
        return StiDBItem(self.sti_engine.BuildFileDBItemFromSmarTeamID(iobject_id, iclass_id))

    def connect(self, i_user_login: str, i_user_password: str) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub Connect(CATBSTR iUserLogin,
                | CATBSTR iUserPassword)
                | 
                |     Connects to SmarTeam Integration.
                |     This connection to SmarTeam Integration is equivalent to launch in CATIA
                |     the command SmarTeam/Connect.
                |     Note that this method is totally independent of the value returned by
                |     'UseGraphicalUI' and that the 'SmarTeam User Login' panel (dedicated connection
                |     panel) may be displayed.
                | 
                |     Parameters:
                | 
                |         iUserLogin
                |             This input corresponds to the Login name of the end user, who wants
                |             to connect to SmarTeam Integration. 
                |         iUserPassword
                |             This input corresponds to the associated Password of this end
                |             user.
                | 
                |             Note that when 'iUserLogin' is EMPTY, the 'SmarTeam User Login'
                |             panel is displayed and the end user has to login himself. Note that
                |             'iUserPassword' is taken into account if and only if 'iUserLogin' is NOT empty.
                |
                |     Example:
                | 
                |           ********** Connection With 'iUserLogin' & 'iUserPassword'
                |           **********
                |          
                |         The following example connects end user to SmarTeam database on
                |         StiEngine oStiEngine Without displaying
                |          'SmarTeam User Login' panel. The User Login is "xxx" and his
                |          associated Password "yyy".
                |          Note that User Login and Password should NOT be EMPTY. Otherwise the
                |          'SmarTeam User Login' panel will be displayed.
                |          If User Login or Password are NOT correct, the connection
                |          failed.
                |          
                |          Dim oStiEngine As StiEngine
                |          Set oStiEngine = CATIA.GetItem("CAIEngine")
                |          Dim iUserLogin As CATBSTR
                |          iUserLogin = "xxx"
                |          Dim iUserPassword As CATBSTR
                |          iUserPassword = "yyy"
                |          oStiEngine.Connect iUserLogin,iUserPassword
                |
                |          ********** Connection Without 'iUserLogin' & 'iUserPassword'
                |          **********
                |          
                |         The following example connects end user to SmarTeam database on
                |         stiEngine oStiEngine With 'SmarTeam User Login' panel.
                |          The end user will have to type his Login and his Password in the
                |          dedicated panel.
                |          Note that if the User Login and his Password are specified, the
                |          'SmarTeam User Login' panel will NOT be displayed.
                |          If the end user only specifies his Login or if User Login and/or
                |          Password are NOT correct, the connection failed. 
                |          In these cases, the 'SmarTeam User Login' panel will NOT be
                |          displayed.
                |
                |          Dim oStiEngine As StiEngine
                |          Set oStiEngine = CATIA.GetItem("CAIEngine")
                |          oStiEngine.Connect "",""

        :param str i_user_login:
        :param str i_user_password:
        :rtype: None
        """
        return self.sti_engine.Connect(i_user_login, i_user_password)

    def disconnect(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub Disconnect()
                | 
                |     Disconnects to SmarTeam Integration.
                |     This disconnection to SmarTeam Integration is equivalent to launch in CATIA
                |     the command SmarTeam/Disconnect.
                |     Note that this method is always executed Without any GUI and is so totally
                |     independent of the value returned by 'UseGraphicalUI'.
                | 
                |     Example:
                | 
                |           The following example disconnects end user to SmarTeam database on
                |           StiEngine oStiEngine.
                |          
                | 
                |          Dim oStiEngine As StiEngine
                |          Set oStiEngine = CATIA.GetItem("CAIEngine")
                |          oStiEngine.Connect "",""
                |          (...)
                |          oStiEngine.Disconnect

        :rtype: None
        """
        return self.sti_engine.Disconnect()

    def get_smarteam_class_id(self, i_sti_db_item: StiDBItem) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetSMARTEAMClassID(StiDBItem iStiDBItem) As short
                | 
                |     Returns the Class Identifier of a SmarTeam Integration Object
                |     CATIAStiDBItem -at least saved in SmarTeam.
                |     Note that the Class Identifier is unique for each Class defined in SmarTeam
                |     Data Model. This data is so linked to the current DataBase, that is to say With
                |     the SmarTeam Release (RXX).
                |     Note that this method is always executed Without any GUI and is so totally
                |     independent of the value returned by 'UseGraphicalUI'.
                | 
                |     Parameters:
                | 
                |         iStiDBItem
                |             This input corresponds to the CATIAStiDBItem. 
                | 
                |     Returns:
                |         This output corresponds to the retrieved Class Identifier of the
                |         CATIAStiDBItem. 
                |     Example:
                | 
                |           The following example returns in oClassId the Class Identifier of the
                |           CATIAStiDBItem oStiDBItem.
                |
                |          Dim oStiEngine As StiEngine
                |          Set oStiEngine = CATIA.GetItem("CAIEngine")
                |          ' Retrieve the Current Activated Product Document
                |          Dim productDocument01 As Document
                |          Set productDocument01 = CATIA.ActiveDocument
                |          ' Retrieve the StiDBItem from the Document
                |          Dim iStiDBItem As StiDBItem
                |          Set iStiDBItem = oStiEngine.GetStiDBItemFromAnyObject(productDocument01)
                |          Dim oClassId As short
                |          oClassId = oStiEngine.GetSMARTEAMClassID(iStiDBItem)

        :param StiDBItem i_sti_db_item:
        :rtype: int
        """
        return self.sti_engine.GetSMARTEAMClassID(i_sti_db_item.com_object)

    def get_smarteam_object_id(self, i_sti_db_item: StiDBItem) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetSMARTEAMObjectID(StiDBItem iStiDBItem) As long
                | 
                |     Returns the Object Identifier of a SmarTeam Integration Object
                |     CATIAStiDBItem -at least saved in SmarTeam.
                |     This data is linked to the current DataBase, that is to say to the SmarTeam
                |     Release (RXX).
                |     Note that this method is always executed Without any GUI and is so totally
                |     independent of the value returned by 'UseGraphicalUI'.
                | 
                |     Parameters:
                | 
                |         iStiDBItem
                |             This input corresponds to the CATIAStiDBItem. 
                | 
                |     Returns:
                |         This output corresponds to the retrieved Object Identifier of the
                |         CATIAStiDBItem.
                |
                |     Example:
                | 
                |           The following example returns in oObjectId the Object Identifier of
                |           the CATIAStiDBItem oStiDBItem.
                |
                |          Dim oStiEngine As StiEngine
                |          Set oStiEngine = CATIA.GetItem("CAIEngine")
                |          ' Retrieve the Current Activated Product Document
                |          Dim productDocument01 As Document
                |          Set productDocument01 = CATIA.ActiveDocument
                |          ' Retrieve the StiDBItem from the Document
                |          Dim iStiDBItem As StiDBItem
                |          Set iStiDBItem = oStiEngine.GetStiDBItemFromAnyObject(productDocument01)
                |          Dim oObjectId As long
                |          oObjectId = oStiEngine.GetSMARTEAMObjectID(iStiDBItem)

        :param StiDBItem i_sti_db_item:
        :rtype: int
        """
        return self.sti_engine.GetSMARTEAMObjectID(i_sti_db_item.com_object)

    def get_sti_db_item_from_any_object(self, i_any_object: AnyObject) -> StiDBItem:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetStiDBItemFromAnyObject(AnyObject iAnyObject) As
                | StiDBItem
                | 
                |     Returns the SmarTeam Integration Object CATIAStiDBItem from an AnyObject
                |     object.
                |     This method is useful to convert whatever CATIA V5 Object to a
                |     CATIAStiDBItem.
                |     Note that this method is always executed Without any GUI and is so totally
                |     independent of the value returned by 'UseGraphicalUI'.
                | 
                |     Parameters:
                | 
                |         iAnyObject
                |             This input corresponds to a CATIA V5 Object. It must be a Document,
                |             a Product, a Part or a DrawingSheet. 
                | 
                |     Returns:
                |         This output corresponds to the retrieved CATIAStiDBItem.
                |         
                |     Example:
                | 
                |           The following example returns in oStiDBItem the CATIAStiDBItem
                |           corresponding to the Document iDocument.
                |
                |          Dim oStiEngine As StiEngine
                |          Set oStiEngine = CATIA.GetItem("CAIEngine")
                |          ' Retrieve the Current Activated Product Document
                |          Dim productDocument01 As Document
                |          Set productDocument01 = CATIA.ActiveDocument
                |          ' Retrieve the StiDBItem from the Document
                |          Dim oStiDBItem As StiDBItem
                |          Set oStiDBItem = oStiEngine.GetStiDBItemFromAnyObject(productDocument01)

        :param AnyObject i_any_object:
        :rtype: StiDBItem
        """
        return StiDBItem(self.sti_engine.GetStiDBItemFromAnyObject(i_any_object.com_object))

    def get_sti_db_item_from_catbstr(self, i_full_path: str) -> StiDBItem:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetStiDBItemFromCATBSTR(CATBSTR iFullPath) As
                | StiDBItem
                | 
                |     Returns the SmarTeam Integration Object CATIAStiDBItem from a Full
                |     Path.
                |     This method is useful to convert a path to a CATIAStiDBItem, that is to say
                |     to create a SmarTeam Integration object. The programmer is then able to manage
                |     its lifecycle (that is to say to Save, Check In, Check Out, Release, New
                |     Release, ... it).
                |     Note that this method is always executed Without any GUI and is so totally
                |     independent of the value returned by 'UseGraphicalUI'.
                | 
                |     See also:
                |         CATIAStiDBItem 
                |     Parameters:
                | 
                |         iFullPath
                |             This input corresponds to the Full Path of the object to retrieve.
                |             
                | 
                |     Returns:
                |         This output corresponds to the retrieved CATIAStiDBItem.
                |         
                |     Example:
                | 
                |           The following example returns in oStiDBItem the CATIAStiDBItem
                |           corresponding to the full path.
                |
                |          Dim oStiEngine As StiEngine
                |          Set oStiEngine = CATIA.GetItem("CAIEngine")
                |          Dim iFullPath As CATBSTR
                |          iFullPath = "E:/CATIAFiles/Engine.CATProduct"
                |          Dim oStiDBItem As StiDBItem
                |          Set oStiDBItem = oStiEngine.GetStiDBItemFromCATBSTR(iFullPath)

        :param str i_full_path:
        :rtype: StiDBItem
        """
        return StiDBItem(self.sti_engine.GetStiDBItemFromCATBSTR(i_full_path))

    def get_team_pdmurl(self, i_sti_db_item: StiDBItem) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetTeamPDMURL(StiDBItem iStiDBItem) As CATBSTR
                | 
                |     Returns the Team PDM URL of a CATIAStiDBItem.
                |     Note that the Team PDM URL has the following syntax:
                |     "TeamPDM://DBExtractor?CLASSID.EQ.www.
                |     AND.OBJECTID.EQ.zzz.AND.Vers.EQ.1"
                |     The only values which are modified from a SmarTeam object to an other are
                |     the numbers corresponding to the document "Class ID" (www) and "Object ID"
                |     (zzz).
                |     Note that this method is always executed With GUI. Indeed it returns a
                |     SmarTeam panel displaying the TEAM PDM URL. It is so totally independent of the
                |     value returned by 'UseGraphicalUI'.
                | 
                |     Parameters:
                | 
                |         iStiDBItem
                |             This input corresponds to the CATIAStiDBItem. 
                | 
                |     Returns:
                |         This output corresponds to the retrieved Team PDM URL of the
                |         CATIAStiDBItem.
                |
                |     Example:
                | 
                |           The following example returns the Team PDM URL from a
                |           CATIAStiDBItem.
                |
                |          Dim oStiEngine As StiEngine
                |          Set oStiEngine = CATIA.GetItem("CAIEngine")
                |          Dim iobjectId As long
                |          iobjectId = 963
                |          Dim iclassId As short
                |          iclassId = 57
                |          Dim iStiDBItem As StiDBItem
                |          Set iStiDBItem = oStiEngine.BuildFileDBItemFromSmarTeamID iobjectId, iclassId
                |          Dim oTeamPDMURL As CATBSTR
                |          oTeamPDMURL = oStiEngine.GetTeamPDMURL iStiDBItem

        :param StiDBItem i_sti_db_item:
        :rtype: str
        """
        return self.sti_engine.GetTeamPDMURL(i_sti_db_item.com_object)

    def is_connected(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func IsConnected() As boolean
                | 
                |     Returns if end user Is Connected to SmarTeam Integration (True) or not
                |     (False).
                |     Note that this method is always executed Without any GUI and is so totally
                |     independent of the value returned by 'UseGraphicalUI'.
                | 
                |     Example:
                | 
                |           The following example tests if end user is connected to SmarTeam
                |           Integration on StiEngine oStiEngine.
                |          If end user is not connected, this code sample allows her/him to
                |          connect to SmarTeam Integration by displaying the 'SmarTeam User Login'
                |          panel.
                |          
                | 
                |          Dim oStiEngine As StiEngine
                |          Set oStiEngine = CATIA.GetItem("CAIEngine")
                |          Dim oIsConnected As boolean
                |          oIsConnected = oStiEngine.IsConnected
                |          If Not oStiEngine.IsConnected() Then
                |            oStiEngine.Connect
                |          End If

        :rtype: bool
        """
        return self.sti_engine.IsConnected()

    def life_cycle_check_in(self, i_sti_db_item: StiDBItem) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub LifeCycleCheckIn(StiDBItem iStiDBItem)
                | 
                |     Checks the CATIAStiDBItem Into SmarTeam Check-In Vault.
                |     This LifeCycleCheckIn operation is equivalent to launch in CATIA the
                |     command SmarTeam/LifeCycle/CheckIn.
                |     2 cases: either the document is NEW (that is to say already saved in
                |     SmarTeam) or the document is being Modified (Checked-Out) and is removed back
                |     into the vault.
                |     Note that this method should be executed With GUI and is so totally
                |     dependent of the value returned by 'UseGraphicalUI'.
                | 
                |     Parameters:
                | 
                |         iStiDBItem
                |             This input corresponds to the CATIAStiDBItem to Check-In.
                |
                |     Example:
                | 
                |           ********** LifeCycleCheckIn With GUI **********
                |          
                |         The following example checks the current activated document -associated
                |         to the CATIAStiDBItem oStiDBItem and
                |          already saved in SmarTeam -into the vault.
                |          
                |         Note that in the dedicated panel, the end user should choose to
                |         activate the following options 'Keep Local File' or 'Keep
                |         Checked-Out'.
                |
                |          Dim oStiEngine As StiEngine
                |          Set oStiEngine = CATIA.GetItem("CAIEngine")
                |          Dim bIsActive As boolean
                |          bIsActive = oStiEngine.UseGraphicalUI
                |          If Not bIsActive Then
                |            oStiEngine.UseGraphicalUI = True
                |          End If
                |          ' Retrieve the Current Activated Product
                |          Dim productDocument01 As Document
                |          Set productDocument01 = CATIA.ActiveDocument
                |          ' Retrieve the StiDBItem from the Document
                |          Dim iStiDBItem As StiDBItem
                |          Set iStiDBItem = oStiEngine.GetStiDBItemFromAnyObject( productDocument01 )
                |          oStiEngine.LifeCycleCheckIn iStiDBItem
                |
                |          ********** LifeCycleCheckIn Without GUI **********
                |          
                |         The following example checks the current activated document -associated
                |         to the CATIAStiDBItem oStiDBItem and
                |          already saved in SmarTeam- into the vault.
                |
                |          Dim oStiEngine As StiEngine
                |          Set oStiEngine = CATIA.GetItem("CAIEngine")
                |          Dim bIsActive As boolean
                |          bIsActive = oStiEngine.UseGraphicalUI
                |          If bIsActive Then
                |            oStiEngine.UseGraphicalUI = False 
                |          End If
                |          ' Retrieve the Current Activated Product
                |          Dim productDocument01 As Document
                |          Set productDocument01 = CATIA.ActiveDocument
                |          ' Retrieve the StiDBItem from the Document
                |          Dim iStiDBItem As StiDBItem
                |          Set iStiDBItem = oStiEngine.GetStiDBItemFromAnyObject( productDocument01 )
                |          oStiEngine.LifeCycleCheckIn iStiDBItem

        :param StiDBItem i_sti_db_item:
        :rtype: None
        """
        return self.sti_engine.LifeCycleCheckIn(i_sti_db_item.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'life_cycle_check_in'
        # # vba_code = """
        # # Public Function life_cycle_check_in(sti_engine)
        # #     Dim iStiDBItem (2)
        # #     sti_engine.LifeCycleCheckIn iStiDBItem
        # #     life_cycle_check_in = iStiDBItem
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def life_cycle_check_out(self, i_sti_db_item: StiDBItem) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub LifeCycleCheckOut(StiDBItem iStiDBItem)
                | 
                |     Checks Out Without Propagation the CATIAStiDBItem in
                |     SmarTeam.
                |     This LifeCycleCheckOut operation is equivalent to launch in CATIA the
                |     command SmarTeam/LifeCycle/CheckOut.
                |     Note that this method should be executed With GUI and is so totally
                |     dependent of the value returned by 'UseGraphicalUI'.
                | 
                |     Parameters:
                | 
                |         iStiDBItem
                |             This input corresponds to the CATIAStiDBItem to Check-Out.
                |
                |     Example:
                | 
                |           ********** LifeCycleCheckOut With GUI **********
                |          
                |         The following example checks out from the vault the current activated
                |         document -associated to the CATIAStiDBItem oStiDBItem.
                |          Note that in the dedicated panel, the end user is able to realize the
                |          following action 'Propagate Operation' to select which children she/he also
                |          wants to Check-Out.
                |          She/he has also access to the SmarTeam panel option 'Do not get the
                |          file from vault'.
                |
                |          Dim oStiEngine As StiEngine
                |          Set oStiEngine = CATIA.GetItem("CAIEngine")
                |          Dim bIsActive As boolean
                |          bIsActive = oStiEngine.UseGraphicalUI
                |          If Not bIsActive Then
                |            oStiEngine.UseGraphicalUI = True
                |          End If
                |          ' Retrieve the Current Activated Product
                |          Dim productDocument01 As Document
                |          Set productDocument01 = CATIA.ActiveDocument
                |          ' Retrieve the StiDBItem from the Document
                |          Dim iStiDBItem As StiDBItem
                |          Set iStiDBItem = oStiEngine.GetStiDBItemFromAnyObject( productDocument01 )
                |          oStiEngine.LifeCycleCheckOut iStiDBItem
                |
                |          **********  LifeCycleCheckOut Without GUI **********
                |          
                |         The following example Checks Out from the vault the current activated
                |         document -associated to the StiDBItem oStiDBItem.
                |
                |          Dim oStiEngine As StiEngine
                |          Set oStiEngine = CATIA.GetItem("CAIEngine")
                |          Dim bIsActive As boolean
                |          bIsActive = oStiEngine.UseGraphicalUI
                |          If bIsActive Then
                |            oStiEngine.UseGraphicalUI = False 
                |          End If
                |          ' Retrieve the Current Activated Product
                |          Dim productDocument01 As Document
                |          Set productDocument01 = CATIA.ActiveDocument
                |          ' Retrieve the StiDBItem from the Document
                |          Dim iStiDBItem As StiDBItem
                |          Set iStiDBItem = oStiEngine.GetStiDBItemFromAnyObject( productDocument01 )
                |          oStiEngine.LifeCycleCheckOut iStiDBItem

        :param StiDBItem i_sti_db_item:
        :rtype: None
        """
        return self.sti_engine.LifeCycleCheckOut(i_sti_db_item.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'life_cycle_check_out'
        # # vba_code = """
        # # Public Function life_cycle_check_out(sti_engine)
        # #     Dim iStiDBItem (2)
        # #     sti_engine.LifeCycleCheckOut iStiDBItem
        # #     life_cycle_check_out = iStiDBItem
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def life_cycle_check_out_propagated(self, i_sti_db_item: StiDBItem) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub LifeCycleCheckOutPropagated(StiDBItem iStiDBItem)
                | 
                |     Checks Out With Propagation the CATIAStiDBItem in
                |     SMARTEAM.
                |     This LifeCycleCheckOutPropagated operation is equivalent to launch in CATIA
                |     the command SmarTeam/LifeCycle/CheckOut and then to specify in the associated
                |     SmarTeam panel 'Actions/Propagate Operation'.
                |     Note that this method should be executed With GUI and is so totally
                |     dependent of the value returned by 'UseGraphicalUI'.
                | 
                |     Parameters:
                | 
                |         iStiDBItem
                |             This input corresponds to the CATIAStiDBItem to be Checked-Out.
                |
                |     Example:
                | 
                |           **********  LifeCycleCheckOutPropagated With GUI
                |           **********
                |          
                |         The following example Checks Out from the vault the current activated
                |         document -associated to the CATIAStiDBItem oStiDBItem
                |          AND its children.
                |          She/he has also access to the SmarTeam panel option 'Do not get the
                |          file from vault'.
                |
                |          Dim oStiEngine As StiEngine
                |          Set oStiEngine = CATIA.GetItem("CAIEngine")
                |          Dim bIsActive As boolean
                |          bIsActive = oStiEngine.UseGraphicalUI
                |          If Not bIsActive Then
                |            oStiEngine.UseGraphicalUI = True
                |          End If
                |          ' Retrieve the Current Activated Product
                |          Dim productDocument01 As Document
                |          Set productDocument01 = CATIA.ActiveDocument
                |          ' Retrieve the StiDBItem from the Document
                |          Dim iStiDBItem As StiDBItem
                |          Set iStiDBItem = oStiEngine.GetStiDBItemFromAnyObject( productDocument01 )
                |          oStiEngine.LifeCycleCheckOutPropagated iStiDBItem
                |
                |          **********  LifeCycleCheckOutPropagated Without GUI
                |          **********
                |          
                |         The following example Checks Out from the vault the current activated
                |         document -associated to the StiDBItem oStiDBItem
                |          AND its children.
                |
                |          Dim oStiEngine As StiEngine
                |          Set oStiEngine = CATIA.GetItem("CAIEngine")
                |          Dim bIsActive As boolean
                |          bIsActive = oStiEngine.UseGraphicalUI
                |          If bIsActive Then
                |            oStiEngine.UseGraphicalUI = False 
                |          End If
                |          ' Retrieve the Current Activated Product
                |          Dim productDocument01 As Document
                |          Set productDocument01 = CATIA.ActiveDocument
                |          ' Retrieve the StiDBItem from the Document
                |          Dim iStiDBItem As StiDBItem
                |          Set iStiDBItem = oStiEngine.GetStiDBItemFromAnyObject( productDocument01 )
                |          oStiEngine.LifeCycleCheckOutPropagated iStiDBItem

        :param StiDBItem i_sti_db_item:
        :rtype: None
        """
        return self.sti_engine.LifeCycleCheckOutPropagated(i_sti_db_item.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'life_cycle_check_out_propagated'
        # # vba_code = """
        # # Public Function life_cycle_check_out_propagated(sti_engine)
        # #     Dim iStiDBItem (2)
        # #     sti_engine.LifeCycleCheckOutPropagated iStiDBItem
        # #     life_cycle_check_out_propagated = iStiDBItem
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def life_cycle_new_release(self, i_sti_db_item: StiDBItem) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub LifeCycleNewRelease(StiDBItem iStiDBItem)
                | 
                |     Enables a New Release Without Propagation for the CATIAStiDBItem in
                |     SmarTeam.
                |     This LifeCycleNewRelease operation to SmarTeam Integration is equivalent to
                |     launch in CATIA the command SmarTeam/LifeCycle/NewRelease.
                |     Note that this method should be executed With GUI and is so totally
                |     dependent of the value returned by 'UseGraphicalUI'.
                | 
                |     Parameters:
                | 
                |         iStiDBItem
                |             This input corresponds to the CATIAStiDBItem to New Release.
                |
                |     Example:
                | 
                |           **********  LifeCycleNewRelease With GUI **********
                |          
                |         The following example makes a new copy of a Released document
                |         associated to the CATIAStiDBItem oStiDBItem
                |          that was moved into the Released vault. The resulting document is a
                |          new revision of the source document. 
                |          Note that in the dedicated panel,the end user is also able to realize
                |          the following action 'Propagate Operation' to select which
                |          children
                |          she/he also wants to Check-Out. She/he has also access to the SmarTeam
                |          panel option 'Do not get the file from vault'.
                |
                |          Dim oStiEngine As StiEngine
                |          Set oStiEngine = CATIA.GetItem("CAIEngine")
                |          Dim bIsActive As boolean
                |          bIsActive = oStiEngine.UseGraphicalUI
                |          If Not bIsActive Then
                |            oStiEngine.UseGraphicalUI = True
                |          End If
                |          ' Retrieve the Current Activated Product
                |          Dim productDocument01 As Document
                |          Set productDocument01 = CATIA.ActiveDocument
                |          ' Retrieve the StiDBItem from the Document
                |          Dim iStiDBItem As StiDBItem
                |          Set iStiDBItem = oStiEngine.GetStiDBItemFromAnyObject( productDocument01 )
                |          oStiEngine.LifeCycleNewRelease iStiDBItem
                |
                |          **********  LifeCycleNewRelease Without GUI
                |          **********
                |          
                |         The following example makes a new copy of a Released document
                |         associated to the CATIAStiDBItem oStiDBItem
                |          that was moved into the Released vault. The resulting document is a
                |          new revision of the source document. 
                |
                |          Dim oStiEngine As StiEngine
                |          Set oStiEngine = CATIA.GetItem("CAIEngine")
                |          Dim bIsActive As boolean
                |          bIsActive = oStiEngine.UseGraphicalUI
                |          If bIsActive Then
                |            oStiEngine.UseGraphicalUI = False 
                |          End If
                |          ' Retrieve the Current Activated Product
                |          Dim productDocument01 As Document
                |          Set productDocument01 = CATIA.ActiveDocument
                |          ' Retrieve the StiDBItem from the Document
                |          Dim iStiDBItem As StiDBItem
                |          Set iStiDBItem = oStiEngine.GetStiDBItemFromAnyObject( productDocument01 )
                |          oStiEngine.LifeCycleNewRelease iStiDBItem

        :param StiDBItem i_sti_db_item:
        :rtype: None
        """
        return self.sti_engine.LifeCycleNewRelease(i_sti_db_item.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'life_cycle_new_release'
        # # vba_code = """
        # # Public Function life_cycle_new_release(sti_engine)
        # #     Dim iStiDBItem (2)
        # #     sti_engine.LifeCycleNewRelease iStiDBItem
        # #     life_cycle_new_release = iStiDBItem
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def life_cycle_new_release_propagated(self, i_sti_db_item: StiDBItem) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub LifeCycleNewReleasePropagated(StiDBItem iStiDBItem)
                | 
                |     Enables a NewRelease action With Propagation for the CATIAStiDBItem in
                |     SmarTeam.
                |     This LifeCycleNewReleasePropagated operation is equivalent to launch in
                |     CATIA the command SmarTeam/LifeCycle/NewRelease and then to specify in the
                |     associated SmarTeam panel 'Propagate Operation'.
                |     Note that this method should be executed With GUI and is so totally
                |     dependent of the value returned by 'UseGraphicalUI'.
                | 
                |     Parameters:
                | 
                |         iStiDBItem
                |             This input corresponds to the CATIAStiDBItem to be New Released.
                |
                |     Example:
                | 
                |            ********** LifeCycleNewReleasePropagated With GUI
                |            **********
                |          
                |         The following example makes a new copy of the Released document
                |         associated to the CATIAStiDBItem oStiDBItem and of its
                |         children.
                |          This document was previously saved into the Released vault. The
                |          resulting document is a new revision of the source document.
                |          
                |          She/he has also access to the SmarTeam panel option 'Do not get the
                |          file from vault'.
                |
                |          Dim bIsActive As boolean
                |          bIsActive = oStiEngine.UseGraphicalUI
                |          If Not bIsActive Then
                |            oStiEngine.UseGraphicalUI = True
                |          End If
                |          ' Retrieve the Current Activated Product
                |          Dim productDocument01 As Document
                |          Set productDocument01 = CATIA.ActiveDocument
                |          ' Retrieve the StiDBItem from the Document
                |          Dim iStiDBItem As StiDBItem
                |          Set iStiDBItem = oStiEngine.GetStiDBItemFromAnyObject( productDocument01 )
                |          oStiEngine.LifeCycleNewReleasePropagated iStiDBItem
                |
                |          ********** LifeCycleNewReleasePropagated Without GUI
                |          **********
                |          
                |         The following example makes a new copy of a Released document
                |         associated to the CATIAStiDBItem oStiDBItem and of its
                |         children.
                |          This document was previously saved into the Released vault. The
                |          resulting document is a new revision of the source document.
                |
                |          Dim bIsActive As boolean
                |          bIsActive = oStiEngine.UseGraphicalUI
                |          If bIsActive Then
                |            oStiEngine.UseGraphicalUI = False 
                |          End If
                |          ' Retrieve the Current Activated Product
                |          Dim productDocument01 As Document
                |          Set productDocument01 = CATIA.ActiveDocument
                |          ' Retrieve the StiDBItem from the Document
                |          Dim iStiDBItem As StiDBItem
                |          Set iStiDBItem = oStiEngine.GetStiDBItemFromAnyObject( productDocument01 )
                |          oStiEngine.LifeCycleNewReleasePropagated iStiDBItem

        :param StiDBItem i_sti_db_item:
        :rtype: None
        """
        return self.sti_engine.LifeCycleNewReleasePropagated(i_sti_db_item.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'life_cycle_new_release_propagated'
        # # vba_code = """
        # # Public Function life_cycle_new_release_propagated(sti_engine)
        # #     Dim iStiDBItem (2)
        # #     sti_engine.LifeCycleNewReleasePropagated iStiDBItem
        # #     life_cycle_new_release_propagated = iStiDBItem
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def life_cycle_release(self, i_sti_db_item: StiDBItem) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub LifeCycleRelease(StiDBItem iStiDBItem)
                | 
                |     Releases the CATIAStiDBItem in SmarTeam Release Vault.
                |     This LifeCycleRelease operation is equivalent to launch in CATIA the
                |     command SmarTeam/LifeCycle/Release.
                |     3 cases: either the document is New (that is to say already saved in
                |     SmarTeam) or it is being Modified (Checked-Out or New Released) and is removed
                |     back into the vault or it is Checked-In and is moved from the Check-In vault to
                |     the Release one.
                |     Note that this method should be executed With GUI and is so totally
                |     dependent of the value returned by 'UseGraphicalUI'.
                | 
                |     Parameters:
                | 
                |         iStiDBItem
                |             This input corresponds to the CATIAStiDBItem to Released.
                |
                |     Example:
                | 
                |           ********** LifeCycleRelease With GUI ********** 
                |          
                |         The following example releases the current activated document
                |         -associated to the CATIAStiDBItem oStiDBItem and
                |          already saved in SmarTeam- into the vault.
                |          
                |         Note that in the dedicated panel, the end user should choose to
                |         activate the following options 'Keep Local File' or 'Keep
                |         Checked-Out'.
                |
                |          Dim oStiEngine As StiEngine
                |          Set oStiEngine = CATIA.GetItem("CAIEngine")
                |          Dim bIsActive As boolean
                |          bIsActive = oStiEngine.UseGraphicalUI
                |          If Not bIsActive Then
                |            oStiEngine.UseGraphicalUI = True
                |          End If
                |          ' Retrieve the Current activated document
                |          Dim productDocument01 As Document
                |          Set productDocument01 = CATIA.ActiveDocument
                |          ' Retrieve the StiDBItem from the Document
                |          Dim iStiDBItem As StiDBItem
                |          Set iStiDBItem = oStiEngine.GetStiDBItemFromAnyObject( productDocument01 )
                |          oStiEngine.LifeCycleRelease iStiDBItem
                |
                |          ********** LifeCycleRelease Without GUI **********
                |          
                |         The following example moves the current activated document -associated
                |         to the CATIAStiDBItem oStiDBItem and
                |          already saved in SmarTeam -into the Released vault.
                |
                |          Dim oStiEngine As StiEngine
                |          Set oStiEngine = CATIA.GetItem("CAIEngine")
                |          Dim bIsActive As boolean
                |          bIsActive = oStiEngine.UseGraphicalUI
                |          If bIsActive Then
                |            oStiEngine.UseGraphicalUI = False 
                |          End If
                |          ' Retrieve the Current activated document
                |          Dim productDocument01 As Document
                |          Set productDocument01 = CATIA.ActiveDocument
                |          ' Retrieve the StiDBItem from the Document
                |          Dim iStiDBItem As StiDBItem
                |          Set iStiDBItem = oStiEngine.GetStiDBItemFromAnyObject( productDocument01 )
                |          oStiEngine.LifeCycleRelease iStiDBItem

        :param StiDBItem i_sti_db_item:
        :rtype: None
        """
        return self.sti_engine.LifeCycleRelease(i_sti_db_item.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'life_cycle_release'
        # # vba_code = """
        # # Public Function life_cycle_release(sti_engine)
        # #     Dim iStiDBItem (2)
        # #     sti_engine.LifeCycleRelease iStiDBItem
        # #     life_cycle_release = iStiDBItem
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def life_cycle_undo_check_out(self, i_sti_db_item: StiDBItem) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub LifeCycleUndoCheckOut(StiDBItem iStiDBItem)
                | 
                |     Cancels Check-Out operation on the CATIAStiDBItem in SmarTeam. So the
                |     programmer is able to retrieve the previous latest state (Checked-In or
                |     Released) of the CATIAStiDBItem.
                |     This LifeCycleUndoCheckOut operation is equivalent to launch in CATIA the
                |     command SmarTeam/LifeCycle/UndoCheckOut.
                |     Note that this method should be executed With GUI and is so totally
                |     dependent of the value returned by 'UseGraphicalUI'.
                | 
                |     Parameters:
                | 
                |         iStiDBItem
                |             This input corresponds to the CATIAStiDBItem to be Undo
                |             Checked-Out. 
                | 
                |     Example:
                | 
                |           **********  LifeCycleUndoCheckOut With GUI
                |           **********
                |          
                |         The following example retrieves a copy of a document associated to the
                |         CATIAStiDBItem oStiDBItem
                |          in the previous latest state (Checked-In or
                |          Released).
                |          
                |         A CATIA panel is firstly displayed to warn the end user that it is
                |         strongly recommanded to confirm the file deletion when
                |         asked.
                |          If, the end user clicks "OK", a SmarTeam panel is then displayed "File
                |          '(...)/Work/CATPRD-XXXX.CATProduct' is referenced only by
                |          
                |          Object 'CATPRD-XXXX RevX.X', and will be deleted. Do you want to
                |          delete this file?" The end user had better accept.
                |          
                | 
                |          Dim oStiEngine As StiEngine
                |          Set oStiEngine = CATIA.GetItem("CAIEngine")
                |          Dim bIsActive As boolean
                |          bIsActive = oStiEngine.UseGraphicalUI
                |          If Not bIsActive Then
                |            oStiEngine.UseGraphicalUI = True 
                |          End If
                |          ' Retrieve the Current Activated Product
                |          Dim productDocument01 As Document
                |          Set productDocument01 = CATIA.ActiveDocument
                |          ' Retrieve the StiDBItem from the Document
                |          Dim iStiDBItem As StiDBItem
                |          Set iStiDBItem = oStiEngine.GetStiDBItemFromAnyObject( productDocument01 )
                |          oStiEngine.LifeCycleUndoCheckOut iStiDBItem
                |
                |          **********  LifeCycleUndoCheckOut Without GUI
                |          **********
                |          
                |         The following example cancels the Check-Out of the document associated
                |         to the CATIAStiDBItem oStiDBItem 
                |          in the previous latest state (Checked-In or
                |          Released).
                |          
                |         By default, the Undo Check-Out operation is not propagated, i.e.
                |         available only for the current CATIAStiDBItem.
                |          
                | 
                |          Dim bIsActive As boolean
                |          bIsActive = oStiEngine.UseGraphicalUI
                |          If bIsActive Then
                |            oStiEngine.UseGraphicalUI = False 
                |          End If
                |          ' Retrieve the Current Activated Product
                |          Dim productDocument01 As Document
                |          Set productDocument01 = CATIA.ActiveDocument
                |          ' Retrieve the StiDBItem from the Document
                |          Dim iStiDBItem As StiDBItem
                |          Set iStiDBItem = oStiEngine.GetStiDBItemFromAnyObject( productDocument01 )
                |          oStiEngine.LifeCycleUndoCheckOut iStiDBItem

        :param StiDBItem i_sti_db_item:
        :rtype: None
        """
        return self.sti_engine.LifeCycleUndoCheckOut(i_sti_db_item.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'life_cycle_undo_check_out'
        # # vba_code = """
        # # Public Function life_cycle_undo_check_out(sti_engine)
        # #     Dim iStiDBItem (2)
        # #     sti_engine.LifeCycleUndoCheckOut iStiDBItem
        # #     life_cycle_undo_check_out = iStiDBItem
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def refresh_info(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub RefreshInfo()
                | 
                |     Refreshes Information concerning all CATIA Documents in
                |     session.
                |     This RefreshInfo operation is equivalent to launch in CATIA the command
                |     SmarTeam/Tools/Refresh.
                |     Note that this method is always executed Without any GUI and is so totally
                |     independent of the value returned by 'UseGraphicalUI'.
                | 
                |     During this RefreshInfo operation, the following steps are
                |     executed:
                |         - Checking the document synchronization on disk, 
                |         - Updating internal info, 
                |         - Updating Read/Write status for valid documents, 
                |         - Updating icons, 
                |         - Sending error or warning message for not synchronized or removed
                |         documents if GUIs are activated. 
                | 
                |     Example:
                | 
                |           The following example refreshs the CATIA session:
                |
                |          Dim oStiEngine As StiEngine
                |          Set oStiEngine = CATIA.GetItem("CAIEngine")
                |          oStiEngine.RefreshInfo

        :rtype: None
        """
        return self.sti_engine.RefreshInfo()

    def save(self, i_sti_db_item: StiDBItem) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub Save(StiDBItem iStiDBItem)
                | 
                |     Saves the CATIAStiDBItem in SmarTeam.
                |     This Save operation is equivalent to launch in CATIA the command
                |     SmarTeam/Save.
                |     Note that this method should be executed With GUI and is so totally
                |     dependent of the value returned by 'UseGraphicalUI'. The SmarTeam Integration
                |     Object (and its children) is(are) saved in the current Work -if NOT already
                |     saved on disc.
                | 
                |     Parameters:
                | 
                |         iStiDBItem
                |             This input corresponds to the CATIAStiDBItem to save.
                |
                |     Example:
                | 
                |           ********** Save With GUI **********
                |          
                |         Note that in the 'Projects Manager' panel, the end user should select
                |         the 'Project' in which she/he wants to save the corresponding
                |         file.
                |          If she/he selects one, then she/he can activate the option 'Link To
                |          Projects' and then 'Secured By' and to finish 'Propagate
                |          security'.
                |          She/he is also able to choose to activate the following option 'Add To
                |          Desktop'. 
                |          
                |         The following example saves in SmarTeam the CATIAStiDBItem oStiDBItem
                |         With GUI.
                |
                |          Dim oStiEngine As StiEngine
                |          Set oStiEngine = CATIA.GetItem("CAIEngine")
                |          Dim bIsActive As boolean
                |          bIsActive = oStiEngine.UseGraphicalUI
                |          If Not bIsActive Then
                |            oStiEngine.UseGraphicalUI = True
                |          End If
                |          ' Retrieve the Current Activated Product
                |          Dim productDocument01 As Document
                |          Set productDocument01 = CATIA.ActiveDocument
                |          ' Retrieve the StiDBItem from the Document
                |          Dim iStiDBItem As StiDBItem
                |          Set iStiDBItem = oStiEngine.GetStiDBItemFromAnyObject(productDocument01)
                |          oStiEngine.Save iStiDBItem 
                |
                |          ********** Save Without GUI **********
                |          
                |         By Default, the SmarTeam Integration Object (and its children) is(are)
                |         saved in the current Work -if NOT already saved on disc,
                |         
                |          NOT linked With any Project and NOT Added to Desktop.
                |          
                |         The following example saves in SmarTeam the CATIAStiDBItem oStiDBItem
                |         Without GUI.
                |
                |          Dim oStiEngine As StiEngine
                |          Set oStiEngine = CATIA.GetItem("CAIEngine")
                |          Dim bIsActive As boolean
                |          bIsActive = oStiEngine.UseGraphicalUI
                |          If bIsActive Then
                |            oStiEngine.UseGraphicalUI = False 
                |          End If
                |          ' Retrieve the Current Activated Product
                |          Dim productDocument01 As Document
                |          Set productDocument01 = CATIA.ActiveDocument
                |          ' Retrieve the StiDBItem from the Document
                |          Dim iStiDBItem As StiDBItem
                |          Set iStiDBItem = oStiEngine.GetStiDBItemFromAnyObject( productDocument01 )
                |          ' Save the Product
                |          oStiEngine.Save iStiDBItem

        :param StiDBItem i_sti_db_item:
        :rtype: None
        """
        return self.sti_engine.Save(i_sti_db_item.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'save'
        # # vba_code = """
        # # Public Function save(sti_engine)
        # #     Dim iStiDBItem (2)
        # #     sti_engine.Save iStiDBItem
        # #     save = iStiDBItem
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'StiEngine(name="{self.name}")'
