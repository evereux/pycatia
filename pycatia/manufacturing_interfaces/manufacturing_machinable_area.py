#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.manufacturing_interfaces.manufacturing_machinable_feature import ManufacturingMachinableFeature
from pycatia.types.general import cat_variant


class ManufacturingMachinableArea(ManufacturingMachinableFeature):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                    ManufacturingInterfaces.ManufacturingFeature
                |                        ManufacturingInterfaces.ManufacturingMachinableFeature
                |                             ManufacturingMachinableArea
                | 
                | Machinable Area in Manufacturing.
                | It is a manufacturing feature pointing design features through one or several
                | machinable geometry. This manufacturing feature could be a target for a
                | manufacturing activity.
                | 
                | See also:
                |     ManufacturingMachinableGeometry, ManufacturingActivity
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.manufacturing_machinable_area = com_object

    @property
    def frozen(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Freezed() As boolean
                | 
                |     Returns the manufacturing machinable area freezed state.
                | 
                |     Returns:
                |         oFreezed The manufacturing machinable area freezed state
                |         
                |     Example:
                |         The following example returns in bFreezed the freezed state of
                |         manufacturing machinable area firstMachArea:
                | 
                |          Dim firstMachArea As ManufacturingMachinableArea
                |          Set firstMachArea = ...
                |          Dim bFreezed As boolean
                |          Set bFreezed = firstMachArea.Freezed

        :rtype: bool
        """

        return self.manufacturing_machinable_area.Freezed

    @frozen.setter
    def frozen(self, value: bool):
        """
        :param bool value:
        """

        self.manufacturing_machinable_area.Freezed = value

    @property
    def visible_in_mfg_view(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property VisibleInMfgView() As boolean
                | 
                |     Returns the manufacturing machinable area visibility
                |     state.
                | 
                |     Returns:
                |         oVisibleInMfgView The manufacturing machinable area visibility state
                |         
                |     Example:
                |         The following example returns in bVisibleInMfgView the visible state in
                |         the Manufacturing View of manufacturing machinable area
                |         firstMachArea:
                | 
                |          Dim firstMachArea As ManufacturingMachinableArea
                |          Set firstMachArea = ...
                |          Dim bVisibleInMfgView As boolean
                |          Set bVisibleInMfgView = firstMachArea.VisibleInMfgView

        :rtype: bool
        """

        return self.manufacturing_machinable_area.VisibleInMfgView

    @visible_in_mfg_view.setter
    def visible_in_mfg_view(self, value: bool):
        """
        :param bool value:
        """

        self.manufacturing_machinable_area.VisibleInMfgView = value

    def add_machinable_geometry(self, i_machinable_geometry: ManufacturingMachinableFeature) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub AddMachinableGeometry(ManufacturingMachinableFeature
                | iMachinableGeometry)
                | 
                |     Adds a machinable geometry to the list.
                | 
                |     Parameters:
                | 
                |         iMachinableGeometry
                |             The machinable geometry to affect 
                | 
                |     Example:
                |         The following example adds the machinable geometry MachGeomToAdd to the
                |         manufacturing machinable area firstMachArea.
                | 
                |          Dim firstMachArea As ManufacturingMachinableArea
                |          Set firstMachArea = ...
                |          Dim MachGeomToAdd As ManufacturingMachinableGeometry
                |          Set MachGeomToAdd = ...
                |          Call firstMachArea.AddMachinableGeometry( MachGeomToAdd
                |          )

        :param ManufacturingMachinableFeature i_machinable_geometry:
        :rtype: None
        """
        return self.manufacturing_machinable_area.AddMachinableGeometry(i_machinable_geometry.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'add_machinable_geometry'
        # # vba_code = """
        # # Public Function add_machinable_geometry(manufacturing_machinable_area)
        # #     Dim iMachinableGeometry (2)
        # #     manufacturing_machinable_area.AddMachinableGeometry iMachinableGeometry
        # #     add_machinable_geometry = iMachinableGeometry
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def list_machinable_geometry(self, o_list_of_machinable_geometry: tuple) -> cat_variant:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub ListMachinableGeometry(CATSafeArrayVariant
                | oListOfMachinableGeometry)
                | 
                |     Retrieves the machinable geometry list.
                | 
                |     Parameters:
                | 
                |         oListOfMachinableGeometry
                |             The retrieved list.
                |             The array must be previously initialized using the
                |             
                | 
                |         MachinableGeometryCount method. 
                | 
                | Example:
                |     The following example retrieves the machinable geometry list of the
                |     manufacturing machinable area firstMachArea in
                |     MachinableGeometryList.
                | 
                |      Dim firstMachArea As ManufacturingMachinableArea
                |      Set firstMachArea = ...
                |      Dim MachinableGeometryListSize As Long
                |      Set MachinableGeometryListSize = firstMachArea.MachinableGeometryCount
                |      If MachinableGeometryListSize > 0 Then
                |        Dim MachinableGeometryList() As Variant
                |        Redim
                |        MachinableGeometryList(MachinableGeometryListSize-1)
                |        Call firstMachArea.ListMachinableGeometry(MachinableGeometryList)
                |      End If

        :param tuple o_list_of_machinable_geometry:
        :rtype: cat_variant
        """
        return self.manufacturing_machinable_area.ListMachinableGeometry(o_list_of_machinable_geometry)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'list_machinable_geometry'
        # # vba_code = """
        # # Public Function list_machinable_geometry(manufacturing_machinable_area)
        # #     Dim oListOfMachinableGeometry (2)
        # #     manufacturing_machinable_area.ListMachinableGeometry oListOfMachinableGeometry
        # #     list_machinable_geometry = oListOfMachinableGeometry
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def list_manufacturing_activity_connected(self, o_list_of_manufacturing_activity_connected: tuple) -> cat_variant:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub ListManufacturingActivityConnected(CATSafeArrayVariant
                | oListOfManufacturingActivityConnected)
                | 
                |     Retrieves the manufacturing activity connected list.
                | 
                |     Parameters:
                | 
                |         oListOfManufacturingActivityConnected
                |             The retrieved list.
                |             The array must be previously initialized using the
                |             
                | 
                |         ManufacturingActivityConnectedCount method. 
                | 
                | Example:
                |     The following example retrieves the manufacturing activity connected list
                |     of the manufacturing machinable area firstMachArea in
                |     ManufacturingActivityConnectedList.
                | 
                |      Dim firstMachArea As ManufacturingMachinableArea
                |      Set firstMachArea = ...
                |      Dim ManufacturingActivityConnectedListSize As Long
                |      Set ManufacturingActivityConnectedListSize = firstMachArea.ManufacturingActivityConnectedCount
                |      If ManufacturingActivityConnectedListSize > 0 Then
                |        Dim ManufacturingActivityConnectedList() As Variant
                |        Redim ManufacturingActivityConnectedList(ManufacturingActivityConnectedListSize-1)
                |        Call firstMachArea.ListManufacturingActivityConnected(ManufacturingActivityConnectedList)
                |      End If

        :param tuple o_list_of_manufacturing_activity_connected:
        :rtype: cat_variant
        """
        return self.manufacturing_machinable_area.ListManufacturingActivityConnected(
            o_list_of_manufacturing_activity_connected)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'list_manufacturing_activity_connected'
        # # vba_code = """
        # # Public Function list_manufacturing_activity_connected(manufacturing_machinable_area)
        # #     Dim oListOfManufacturingActivityConnected (2)
        # #     manufacturing_machinable_area.ListManufacturingActivityConnected oListOfManufacturingActivityConnected
        # #     list_manufacturing_activity_connected = oListOfManufacturingActivityConnected
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def machinable_geometry_count(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func MachinableGeometryCount() As long
                | 
                |     Returns the machinable geometry list count.
                | 
                |     Parameters:
                | 
                |         oMachinableGeometryCount
                |             The number of machinable geometry connected to this feature
                |
                |     Example:
                |         The following example retrieves the machinable geometry list count of
                |         the manufacturing machinable area firstMachArea in
                |         MachinableGeometryListSize.
                | 
                |          Dim firstMachArea As ManufacturingMachinableArea
                |          Set firstMachArea = ...
                |          Dim MachinableGeometryListSize As Long
                |          Set MachinableGeometryListSize = firstMachArea.MachinableGeometryCount

        :rtype: int
        """
        return self.manufacturing_machinable_area.MachinableGeometryCount()

    def manufacturing_activity_connected_count(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func ManufacturingActivityConnectedCount() As long
                | 
                |     Returns the manufacturing activity connected list count.
                | 
                |     Parameters:
                | 
                |         oManufacturingActivityConnectedCount
                |             The number of manufacturing activity pointing this feature
                |
                |     Example:
                |         The following example retrieves the manufacturing activity connected
                |         list count of the manufacturing machinable area firstMachArea in
                |         ManufacturingActivityConnectedListSize.
                | 
                |          Dim firstMachArea As ManufacturingMachinableArea
                |          Set firstMachArea = ...
                |          Dim ManufacturingActivityConnectedListSize As Long
                |          Set ManufacturingActivityConnectedListSize = firstMachArea.ManufacturingActivityConnectedCount

        :rtype: int
        """
        return self.manufacturing_machinable_area.ManufacturingActivityConnectedCount()

    def remove_machinable_geometry(self, i_machinable_geometry: ManufacturingMachinableFeature) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub RemoveMachinableGeometry(ManufacturingMachinableFeature
                | iMachinableGeometry)
                | 
                |     Removes a machinable geometry from the list.
                | 
                |     Parameters:
                | 
                |         iMachinableGeometry
                |             The machinable geometry to remove 
                | 
                |     Example:
                |         The following example removes the machinable geometry MachGeomToRemove
                |         to the manufacturing machinable area firstMachArea.
                | 
                |          Dim firstMachArea As ManufacturingMachinableArea
                |          Set firstMachArea = ...
                |          Dim MachGeomToRemove As
                |          ManufacturingMachinableGeometry
                |          Set MachGeomToRemove = ...
                |          Call firstMachArea.RemoveMachinableGeometry( MachGeomToRemove
                |          )

        :param ManufacturingMachinableFeature i_machinable_geometry:
        :rtype: None
        """
        return self.manufacturing_machinable_area.RemoveMachinableGeometry(i_machinable_geometry.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'remove_machinable_geometry'
        # # vba_code = """
        # # Public Function remove_machinable_geometry(manufacturing_machinable_area)
        # #     Dim iMachinableGeometry (2)
        # #     manufacturing_machinable_area.RemoveMachinableGeometry iMachinableGeometry
        # #     remove_machinable_geometry = iMachinableGeometry
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'ManufacturingMachinableArea(name="{self.name}")'
