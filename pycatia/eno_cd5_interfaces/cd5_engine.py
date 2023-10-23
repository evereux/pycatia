#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.eno_cd5_interfaces.cd5_id import CD5ID
from pycatia.eno_cd5_interfaces.cd5_structure import CD5Structure
from pycatia.in_interfaces.document import Document
from pycatia.system_interfaces.any_object import AnyObject


class CD5Engine(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     CD5Engine
                | 
                | Represents the ENOVIA V6 Integration Engine, that is to say the entry point to
                | the CATIA/ENOVIA V6 Integration.
                | 
                | It allows end user to realize the following operations : connection and disconnection to
                | ENOVIA V6 Integration, creation of ENOVIA V6 Integration IDs (CD5ID) and Structures (CD5Strcture),
                | and opening of the corresponding objects in different modes.
                | Note that all operations performed from this interface are the same as
                | operations available in the ENOVIA V6 menu in CATIA, unless most of them are
                | executed without panel.
                | 
                | Example:
                | 
                |       The following example indicates how to retrieve the ENOVIA V6 Integration
                |       Engine.
                |
                |      Dim oCD5Engine As CD5Engine
                |      Set oCD5Engine = CATIA.GetItem("CD5Engine")
                |
                | See also:
                |     CD5ID, CD5Structure
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.cd5_engine = com_object

    @property
    def expand_mode(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ExpandMode() As CATBSTR
                | 
                |     Returns (gets) or sets the value of the Open option "Expand Mode". The
                |     default value is set in the user's Preferences.
                | 
                |     Throws:
                | 
                |         -1641847650 : Connection to ENOVIA V6 is necessary to intialize this option.
                | 
                |     Example:
                | 
                |           The following example sets Expand Mode to LatestVersion, then
                |           displays it.
                |
                |          oCD5Engine.ExpandMode = "LatestVersion"
                |          MsgBox oCD5Engine.ExpandMode

        :rtype: str
        """

        return self.cd5_engine.ExpandMode

    @expand_mode.setter
    def expand_mode(self, value: str):
        """
        :param str value:
        """

        self.cd5_engine.ExpandMode = value

    @property
    def include_all_children(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property IncludeAllChildren() As boolean
                | 
                |     Returns (gets) or sets the value of the Open option "Open With". The
                |     default value is False, means Required Children.
                | 
                |     Example:
                | 
                |           The following example sets Open With to All
                |           Children.
                |
                |          oCD5Engine.IncludeAllChildren = True

        :rtype: bool
        """

        return self.cd5_engine.IncludeAllChildren

    @include_all_children.setter
    def include_all_children(self, value: bool):
        """
        :param bool value:
        """

        self.cd5_engine.IncludeAllChildren = value

    @property
    def related_designs(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property RelatedDesigns() As CATBSTR
                | 
                |     Returns (gets) or sets the value of the Open option "Related Designs". The
                |     default value is set in the user's Preferences.
                | 
                |     Throws:
                | 
                |         -1641847650 : Connection to ENOVIA V6 is necessary to intialize this option.
                | 
                |     Example:
                | 
                |           The following example sets Related Designs to Associated Drawings,
                |           then displays it.
                |
                |          oCD5Engine.RelatedDesigns = "Associated Drawings"
                |          MsgBox oCD5Engine.RelatedDesigns

        :rtype: str
        """

        return self.cd5_engine.RelatedDesigns

    @related_designs.setter
    def related_designs(self, value: str):
        """
        :param str value:
        """

        self.cd5_engine.RelatedDesigns = value

    def connect(self, i_user_name: str, i_user_password: str, i_security_context: str) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub Connect(CATBSTR iUserName,
                | CATBSTR iUserPassword,
                | CATBSTR iSecurityContext)
                | 
                |     Connects to ENOVIA V6. It is equivalent to launch in CATIA the command
                |     ENOVIA V6/Connect and enter the User Name/Password/Security
                |     Context.
                | 
                |     Parameters:
                | 
                |         iUserName
                |             The Login name of the end user, who wants to connect to ENOVIA V6.
                |             
                |         iUserPassword
                |             The associated Password of this end user. 
                |         iSecurityContext
                |             The security context the end user wants to use (if empty, the API
                |             will first try to connect without security context then try again with the
                |             default one). 
                | 
                |     Throws:
                | 
                |         -1867244384 : The Document Location setting is incorrect.
                |         -1878815075 : Invalid Password.
                |         -1803748693 : Another user is already logged in.
                | 
                |     Example:
                | 
                |           The following example connects end user to ENOVIA V6 on CD5Engine
                |           oCD5Engine.
                |          The User Login is "xxx" and his associated Password
                |          "yyy".
                |
                |          Dim iUserName As CATBSTR
                |          iUserName = "xxx"
                |          Dim iUserPassword As CATBSTR
                |          iUserPassword = "yyy"
                |          oCD5Engine.Connect iUserName,iUserPassword,""

        :param str i_user_name:
        :param str i_user_password:
        :param str i_security_context:
        :rtype: None
        """
        return self.cd5_engine.Connect(i_user_name, i_user_password, i_security_context)

    def disconnect(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub Disconnect()
                | 
                |     Disconnects from ENOVIA V6. It is equivalent to launch in CATIA the command
                |     ENOVIA V6/Disconnect.
                | 
                |     Example:
                | 
                |           The following example disconnects end user from ENOVIA V6 Integration
                |           on CD5Engine oCD5Engine.
                |
                |          oCD5Engine.Disconnect

        :rtype: None
        """
        return self.cd5_engine.Disconnect()

    def get_id_from_tnr(self, i_type: str, i_name: str, i_revision: str) -> CD5ID:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetIDFromTNR(CATBSTR iType,
                | CATBSTR iName,
                | CATBSTR iRevision) As CD5ID
                | 
                |     Creates a ENOVIA V6 Integration ID (CD5ID) from a Major Object thanks to
                |     its Type, Name and Revision.
                | 
                |     Parameters:
                | 
                |         iType
                |             The type of the ENOVIA V6 Object. 
                |         iName
                |             The name of the ENOVIA V6 Object. 
                |         iRevision
                |             The revision of the ENOVIA V6 Object. 
                | 
                |     Returns:
                |         The created CD5ID. 
                |     Example:
                | 
                |           The following example creates a CD5ID from the major object
                |           "MyProduct" of Type "CATProduct For Team" and Revision "---" on CD5Engine
                |           oCD5Engine.
                |
                |          Dim oCD5ID As CD5ID
                |          Set oCD5ID = oCD5Engine.GetIDFromTNR("CATProduct For Team", "MyProduct", "---")

        :param str i_type:
        :param str i_name:
        :param str i_revision:
        :rtype: CD5ID
        """
        return CD5ID(self.cd5_engine.GetIDFromTNR(i_type, i_name, i_revision))

    def get_id_from_tnrv(self, i_type: str, i_name: str, i_revision: str, i_version: str) -> CD5ID:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetIDFromTNRV(CATBSTR iType,
                | CATBSTR iName,
                | CATBSTR iRevision,
                | CATBSTR iVersion) As CD5ID
                | 
                |     Creates a ENOVIA V6 Integration ID (CD5ID) from a Minor Object thanks to
                |     its Type, Name, Revision and Version.
                | 
                |     Parameters:
                | 
                |         iType
                |             The type of the ENOVIA V6 Object. 
                |         iName
                |             The name of the ENOVIA V6 Object. 
                |         iRevision
                |             The revision of the ENOVIA V6 Object. 
                |         iVersion
                |             The version of the ENOVIA V6 Object. 
                | 
                |     Returns:
                |         The created CD5ID. 
                |     Example:
                | 
                |           The following example creates a CD5ID from the minor object
                |           "MyProduct" of Type "CATProduct For Team", Revision "---" and Version "0" on
                |           CD5Engine oCD5Engine.
                |
                |          Dim oCD5ID As CD5ID
                |          Set oCD5ID = oCD5Engine.GetIDFromTNRV("CATProduct For Team", "MyProduct", "---", "0")

        :param str i_type:
        :param str i_name:
        :param str i_revision:
        :param str i_version:
        :rtype: CD5ID
        """
        return CD5ID(self.cd5_engine.GetIDFromTNRV(i_type, i_name, i_revision, i_version))

    def get_structure(self, i_cd5_id: CD5ID) -> CD5Structure:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetStructure(CD5ID iCD5ID) As CD5Structure
                | 
                |     Creates a Structure from a ENOVIA V6 Object identified by its CD5ID, in the
                |     purpose of a future Partial Open.
                | 
                |     Parameters:
                | 
                |         iCD5ID
                |             The CD5ID of the ENOVIA V6 Object, candidate for a partial open.
                |
                |     Returns:
                |         The created CD5Structure. 
                |     Example:
                | 
                |           The following example creates a CD5Structure from the CD5ID of an
                |           object on CD5Engine oCD5Engine.
                |
                |          Dim iCD5ID As CD5ID
                |          Set iCD5ID = oCD5Engine.GetIDFromTNR("CATProduct For Team", "MyProduct", "---")
                |          Dim oCD5Structure As CD5Structure
                |          Set oCD5Structure = oCD5Engine.GetStructure(iCD5ID)

        :param CD5ID i_cd5_id:
        :rtype: CD5Structure
        """
        return CD5Structure(self.cd5_engine.GetStructure(i_cd5_id.com_object))

    def interactive_open(self, i_cd5_id: CD5ID) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub InteractiveOpen(CD5ID iCD5ID)
                | 
                |     Launches the Interactive ENOVIA V6 Open Command and performs the search
                |     with the input CD5ID.
                | 
                |     Parameters:
                | 
                |         iCD5ID
                |             The ENOVIA V6 ID of the Object to open in CATIA. 
                | 
                |     Throws:
                | 
                |         -1697450280 : CATIA is not connected to ENOVIA V6.
                | 
                |     Example:
                | 
                |           The following example launches the interactive ENOVIA V6 Open Command
                |           on CD5Engine oCD5Engine, with the following search
                |           criteria:
                |
                |             Type : "CATProduct For Team".
                |             Name : "MyProduct".
                |             Revision : "---".
                |
                |          Dim myCD5ID As CD5ID
                |          Set myCD5ID = oCD5Engine.GetIDFromTNR("CATProduct For Team", "MyProduct", "---")
                |          oCD5Engine.InteractiveOpen(myCD5ID)

        :param CD5ID i_cd5_id:
        :rtype: None
        """
        return self.cd5_engine.InteractiveOpen(i_cd5_id.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'interactive_open'
        # # vba_code = """
        # # Public Function interactive_open(cd5_engine)
        # #     Dim iCD5ID (2)
        # #     cd5_engine.InteractiveOpen iCD5ID
        # #     interactive_open = iCD5ID
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def is_connected(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func IsConnected() As boolean
                | 
                |     Returns if end user is connected to ENOVIA V6 (True) or not
                |     (False).
                | 
                |     Example:
                | 
                |           The following example tests if end user is connected to ENOVIA V6
                |           Integration on CD5Engine oCD5Engine.
                |          A MsgBox with the connection status will appear to the end
                |          user.
                |          If end user is connected, the MsgBox will contain "Connected", else it
                |          will contain "Not Connected".
                |
                |          If oCD5Engine.IsConnected Then
                |            MsgBox "Connected"
                |          Else
                |            MsgBox "Not Connected"
                |          End If

        :rtype: bool
        """
        return self.cd5_engine.IsConnected()

    def open(self, i_cd5_id: CD5ID) -> Document:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func Open(CD5ID iCD5ID) As Document
                | 
                |     Opens a ENOVIA V6 Object in CATIA thanks to its previously created CD5ID,
                |     and returns the created Document.
                | 
                |     Parameters:
                | 
                |         iCD5ID
                |             The ENOVIA V6 ID of the Object to open in CATIA. 
                | 
                |     Returns:
                |         The created Document. 
                |     Throws:
                | 
                |         -1697450280 : CATIA is not connected to ENOVIA V6.
                |         -1871171370 : Failed to get details of design objects.
                | 
                |     Example:
                | 
                |           The following example opens an ENOVIA V6 Object in CATIA from its
                |           CD5ID on CD5Engine oCD5Engine.
                |
                |          Dim myCD5ID As CD5ID
                |          Set myCD5ID = oCD5Engine.GetIDFromTNRV("CATProduct For Team", "MyProduct", "---", "0")
                |          Dim oDocument As Document
                |          Set oDocument = oCD5Engine.Open(myCD5ID)

        :param CD5ID i_cd5_id:
        :rtype: Document
        """
        return Document(self.cd5_engine.Open(i_cd5_id.com_object))

    def partial_open(self, i_cd5_structure: CD5Structure) -> Document:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func PartialOpen(CD5Structure iCD5Structure) As Document
                | 
                |     Opens partially a ENOVIA V6 Object in CATIA thanks to its previously
                |     created CD5Structure, and returns the created Document.
                | 
                |     Parameters:
                | 
                |         iCD5Structure
                |             The Structure of the Object to open in CATIA. 
                | 
                |     Returns:
                |         The created Document. 
                |     Throws:
                | 
                |         -1697450280 : CATIA is not connected to ENOVIA V6.
                |         -1871171370 : Failed to get details of design objects.
                | 
                |     Example:
                | 
                |           The following example opens partially the ENOVIA V6 Object
                |           "RootProduct" and its subproduct "DummyProduct" in CATIA on CD5Engine
                |           oCD5Engine.
                |
                |          Dim iRootCD5ID As CD5ID
                |          Set iRootCD5ID = oCD5Engine.GetIDFromTNR("CATProduct For Team", "RootProduct", "---")
                |          Dim iSubCD5ID As CD5ID
                |          Set iSubCD5ID = oCD5Engine.GetIDFromTNR("CATProduct For Team", "SubProduct", "---")
                |          Dim iCD5Structure As CD5Structure
                |          Set iCD5Structure = oCD5Engine.GetStructure(iRootCD5ID)
                |          iCD5Structure.Include(iDummyCD5ID)
                |          Dim oDocument As Document
                |          Set oDocument = oCD5Engine.PartialOpen(iCD5Structure)

        :param CD5Structure i_cd5_structure:
        :rtype: Document
        """
        return Document(self.cd5_engine.PartialOpen(i_cd5_structure.com_object))

    def __repr__(self):
        return f'CD5Engine(name="{self.name}")'
