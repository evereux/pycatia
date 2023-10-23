#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.any_object import AnyObject


class DeviceSim(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     DeviceSim
                | 
                | Interface allowing simulation of a Device.
                | 
                | Role: This interface is used to simulate the devices that are available in the
                | Device Building workbench. This includes devices created in both V5 and
                | D5.
                | The following code snippet can be used to obtain a device in a CATProduct
                | document.
                | 
                |    Dim objDeviceSim As DeviceSim
                |    Set objDeviceSim = CATIA.ActiveDocument.Product.GetTechnologicalObject("DeviceSim")
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.device_sim = com_object

    def finalize(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub Finalize()
                | 
                |     Cleans the WDM world. Please note that no reference counting will be
                |     maintained. Cleanup should be done on each device before another device is
                |     Initialized
                | 
                |     Returns:
                |         an HRESULT value.
                |
                |     Example:
                |
                |            Dim objDeviceSim As DeviceSim
                |            Set objDeviceSim = CATIA.ActiveDocument.Product.GetTechnologicalObject("DeviceSim")
                |            objDeviceSim.Initialize
                |            ...
                |            objDevice.Finalize

        :rtype: None
        """
        return self.device_sim.Finalize()

    def get_dof_values(self, i_mechanism: AnyObject) -> tuple:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetDOFValues(CATBaseDispatch iMechanism) As
                | CATSafeArrayVariant
                | 
                |     Get the DOF values for the device.
                | 
                |     Parameters:
                | 
                |         iMechanism
                |             This inner parameter contains a handle to the mechanism
                |             
                |         oValues
                |             This outer parameter contains a list of the current DOF values.
                |             Please note that distances are measured in meters and angles in radians.
                |             
                | 
                |     Returns:
                |         an HRESULT value.
                |
                |     Example:
                |
                |            Dim  ListMechanisms  As Mechanisms
                |            Set  ListMechanisms  =  CATIA.ActiveDocument.Product.GetTechnologicalObject("Mechanisms")
                |            On Error Resume Next
                |            Dim mech
                |            Set mech = ListMechanisms.Item(1)
                |            If Err.Number <> 0 Then
                |               'If there are no mechanisms (i.e. D5 devices), use the device sim
                |               handle instead
                |               Set mech = CATIA.ActiveDocument.Product.GetTechnologicalObject("DeviceSim")
                |            End If    
                |            On Error GoTo 0
                | 
                |            Dim objDeviceSim As DeviceSim
                |            Set objDeviceSim = CATIA.ActiveDocument.Product.GetTechnologicalObject("DeviceSim")
                |            objDeviceSim.Initialize
                |            
                |            Dim ListOfDOFValues
                |            ListOfDOFValues = objDevice.GetDOFValues (mech)
                |            ...

        :param AnyObject i_mechanism:
        :rtype: tuple
        """
        return self.device_sim.GetDOFValues(i_mechanism.com_object)

    def initialize(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub Initialize()
                | 
                |     Initializes the WDM world. Required for calls to
                |     Get/SetDOFValues
                | 
                |     Returns:
                |         an HRESULT value.
                |
                |     Example:
                |
                |            Dim objDeviceSim As DeviceSim
                |            Set objDeviceSim = CATIA.ActiveDocument.Product.GetTechnologicalObject("DeviceSim")
                |            objDeviceSim.Initialize

        :rtype: None
        """
        return self.device_sim.Initialize()

    def set_dof_values(self, i_mechanism: AnyObject, i_values: tuple, i_is_relative: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetDOFValues(CATBaseDispatch iMechanism,
                | CATSafeArrayVariant iValues,
                | boolean iIsRelative)
                | 
                |     Set the DOF values for the device.
                | 
                |     Parameters:
                | 
                |         iValues
                |             This inner parameter contains a list of the DOF values to be
                |             applied. Size of iValues should be equal to the number of DOFs. Please note
                |             that distances are measured in meters and angles in radians.
                |             
                |         iMechanism
                |             This inner parameter contains a handle to the mechanism. For D5
                |             devices the device itself should be used as the mechanism (sample below)
                |             
                |         iIsRelative
                |             This inner parameter indicates if iValues is relative to the
                |             existing DOF values. If set to TRUE, iValues will be added to the existing
                |             values 
                | 
                |     Returns:
                |         an HRESULT value.
                |
                |     Example:
                |
                |            Dim  ListMechanisms  As Mechanisms
                |            Set  ListMechanisms  =  CATIA.ActiveDocument.Product.GetTechnologicalObject("Mechanisms")
                |            On Error Resume Next
                |            Dim mech
                |            Set mech = ListMechanisms.Item(1)
                |            If Err.Number <> 0 Then
                |               'If there are no mechanisms (i.e. D5 devices), use the device
                |               handle instead
                |               Set mech = CATIA.ActiveDocument.Product.GetTechnologicalObject("DeviceSim")
                |            End If    
                |            On Error GoTo 0
                | 
                |            Dim objDeviceSim As DeviceSim
                |            Set objDeviceSim = CATIA.ActiveDocument.Product.GetTechnologicalObject("DeviceSim")
                |            objDeviceSim.Initialize
                |            Dim ListOfDOFValues (5) 
                |            'Populate ListOfDOFValues with some values
                |            ...
                |            objDevice.SetDOFValues mech, ListOfDOFValues, TRUE
                |            ...

        :param AnyObject i_mechanism:
        :param tuple i_values:
        :param bool i_is_relative:
        :rtype: None
        """
        return self.device_sim.SetDOFValues(i_mechanism.com_object, i_values, i_is_relative)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_dof_values'
        # # vba_code = """
        # # Public Function set_dof_values(device_sim)
        # #     Dim iMechanism (2)
        # #     device_sim.SetDOFValues iMechanism
        # #     set_dof_values = iMechanism
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'DeviceSim(name="{self.name}")'
