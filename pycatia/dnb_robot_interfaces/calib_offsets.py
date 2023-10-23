#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.any_object import AnyObject


class CalibOffsets(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     CalibOffsets
                | 
                | Interface to set Robot base/Tool offsets based on Calibration.
                | 
                | Role: This interface provides methods to get/set calibration offsets related to
                | Robot base and Robot tool position.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.calib_offsets = com_object

    def apply_corrected_base_offset(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub ApplyCorrectedBaseOffset()
                | 
                |     Applies corrected base offset.
                | 
                |     Returns:
                |         an HRESULT value.
                |         Legal values:
                | 
                |             S_OK if the operation succeeds
                |             E_FAIL otherwise

        :rtype: None
        """
        return self.calib_offsets.ApplyCorrectedBaseOffset()

    def apply_corrected_tool_offset(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub ApplyCorrectedToolOffset()
                | 
                |     Applies corrected tool offset.
                | 
                |     Returns:
                |         an HRESULT value.
                |         Legal values:
                | 
                |             S_OK if the operation succeeds
                |             E_FAIL otherwise

        :rtype: None
        """
        return self.calib_offsets.ApplyCorrectedToolOffset()

    def apply_nominal_base_offset(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub ApplyNominalBaseOffset()
                | 
                |     Applies the nominal base offset.
                | 
                |     Returns:
                |         an HRESULT value.
                |         Legal values:
                | 
                |             S_OK if the operation succeeds
                |             E_FAIL otherwise

        :rtype: None
        """
        return self.calib_offsets.ApplyNominalBaseOffset()

    def apply_nominal_tool_offset(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub ApplyNominalToolOffset()
                | 
                |     Applies nominal tool offset.
                | 
                |     Returns:
                |         an HRESULT value.
                |         Legal values:
                | 
                |             S_OK if the operation succeeds
                |             E_FAIL otherwise

        :rtype: None
        """
        return self.calib_offsets.ApplyNominalToolOffset()

    def get_calib_reference_file(self, o_calib_reference_file: str) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetCalibReferenceFile(CATBSTR oCalibReferenceFile)
                | 
                |     Retrieve the reference calibration file.
                | 
                |     Parameters:
                | 
                |         iCalibReferenceFile
                |             Full path of reference calibration file. 
                | 
                |     Returns:
                |         an HRESULT value.
                |         Legal values:
                | 
                |             S_OK if the operation succeeds
                |             E_FAIL otherwise

        :param str o_calib_reference_file:
        :rtype: None
        """
        return self.calib_offsets.GetCalibReferenceFile(o_calib_reference_file)

    def get_corrected_base_offset(
            self,
            x: float,
            y: float,
            z: float,
            roll: float,
            pitch: float,
            yaw: float
    ) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetCorrectedBaseOffset(double x,
                | double y,
                | double z,
                | double roll,
                | double pitch,
                | double yaw)
                | 
                |     Retrieve corrected base offset for the robot base wrt robot base reference
                |     position.
                | 
                |     Parameters:
                | 
                |         x
                |             X coordinate of the Corrected robot base offset(in m).
                |             
                |         y
                |             Y coordinate of the Corrected robot base offset(in m).
                |             
                |         z
                |             Z coordinate of the Corrected robot base offset(in m).
                |             
                |         roll
                |             Roll angle of the Corrected robot base offset(in deg).
                |             
                |         pitch
                |             Pitch angle of the Corrected robot base offset(in deg).
                |             
                |         yaw
                |             Pitch angle of the Corrected robot base offset(in deg).
                |             
                | 
                |     Returns:
                |         an HRESULT value.
                |         Legal values:
                | 
                |             S_OK if the operation succeeds
                |             E_FAIL otherwise

        :param float x:
        :param float y:
        :param float z:
        :param float roll:
        :param float pitch:
        :param float yaw:
        :rtype: None
        """
        return self.calib_offsets.GetCorrectedBaseOffset(x, y, z, roll, pitch, yaw)

    def get_corrected_tool_offset(self, x: float, y: float, z: float, roll: float, pitch: float, yaw: float) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetCorrectedToolOffset(double x,
                | double y,
                | double z,
                | double roll,
                | double pitch,
                | double yaw)
                | 
                |     Retrieve corrected tool offset for the robot wrt robot mount
                |     position.
                | 
                |     Parameters:
                | 
                |         x
                |             X coordinate of the Corrected tool offset(in m). 
                |         y
                |             Y coordinate of the Corrected tool offset(in m). 
                |         z
                |             Z coordinate of the Corrected tool offset(in m). 
                |         roll
                |             Roll angle of the Corrected tool offset(in deg). 
                |         pitch
                |             Pitch angle of the Corrected tool offset(in deg). 
                |         yaw
                |             Pitch angle of the Corrected tool offset(in deg). 
                | 
                |     Returns:
                |         an HRESULT value.
                |         Legal values:
                | 
                |             S_OK if the operation succeeds
                |             E_FAIL otherwise

        :param float x:
        :param float y:
        :param float z:
        :param float roll:
        :param float pitch:
        :param float yaw:
        :rtype: None
        """
        return self.calib_offsets.GetCorrectedToolOffset(x, y, z, roll, pitch, yaw)

    def get_nominal_base_offset(self, x: float, y: float, z: float, roll: float, pitch: float, yaw: float) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetNominalBaseOffset(double x,
                | double y,
                | double z,
                | double roll,
                | double pitch,
                | double yaw)
                | 
                |     Retrieve nominal base offset for the robot base wrt robot base reference
                |     position.
                | 
                |     Parameters:
                | 
                |         x
                |             X coordinate of the Nominal robot base offset(in m).
                |             
                |         y
                |             Y coordinate of the Nominal robot base offset(in m).
                |             
                |         z
                |             Z coordinate of the Nominal robot base offset(in m).
                |             
                |         roll
                |             Roll angle of the Nominal robot base offset(in deg).
                |             
                |         pitch
                |             Pitch angle of the Nominal robot base offset(in deg).
                |             
                |         yaw
                |             Pitch angle of the Nominal robot base offset(in deg).
                |             
                | 
                |     Returns:
                |         an HRESULT value.
                |         Legal values:
                | 
                |             S_OK if the operation succeeds
                |             E_FAIL otherwise

        :param float x:
        :param float y:
        :param float z:
        :param float roll:
        :param float pitch:
        :param float yaw:
        :rtype: None
        """
        return self.calib_offsets.GetNominalBaseOffset(x, y, z, roll, pitch, yaw)

    def get_nominal_tool_offset(self, x: float, y: float, z: float, roll: float, pitch: float, yaw: float) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetNominalToolOffset(double x,
                | double y,
                | double z,
                | double roll,
                | double pitch,
                | double yaw)
                | 
                |     Retrieve nominal tool offset for the robot wrt robot mount
                |     position.
                | 
                |     Parameters:
                | 
                |         x
                |             X coordinate of the Nominal tool offset(in m). 
                |         y
                |             Y coordinate of the Nominal tool offset(in m). 
                |         z
                |             Z coordinate of the Nominal tool offset(in m). 
                |         roll
                |             Roll angle of the Nominal tool offset(in deg). 
                |         pitch
                |             Pitch angle of the Nominal tool offset(in deg). 
                |         yaw
                |             Pitch angle of the Nominal tool offset(in deg). 
                | 
                |     Returns:
                |         an HRESULT value.
                |         Legal values:
                | 
                |             S_OK if the operation succeeds
                |             E_FAIL otherwise

        :param float x:
        :param float y:
        :param float z:
        :param float roll:
        :param float pitch:
        :param float yaw:
        :rtype: None
        """
        return self.calib_offsets.GetNominalToolOffset(x, y, z, roll, pitch, yaw)

    def get_reference_base_position(self, x: float, y: float, z: float, roll: float, pitch: float, yaw: float) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetReferenceBasePosition(double x,
                | double y,
                | double z,
                | double roll,
                | double pitch,
                | double yaw)
                | 
                |     Retrieve current reference base position of robot.
                | 
                |     Parameters:
                | 
                |         x
                |             X coordinate of the reference base position(in m).
                |             
                |         y
                |             Y coordinate of the reference base position(in m).
                |             
                |         z
                |             Z coordinate of the reference base position(in m).
                |             
                |         roll
                |             Roll angle of the reference base position(in deg).
                |             
                |         pitch
                |             Pitch angle of the reference base position(in deg).
                |             
                |         yaw
                |             Yaw angle of the reference base position(in deg). 
                | 
                |     Returns:
                |         an HRESULT value.
                |         Legal values:
                | 
                |             S_OK if the operation succeeds
                |             E_FAIL otherwise

        :param float x:
        :param float y:
        :param float z:
        :param float roll:
        :param float pitch:
        :param float yaw:
        :rtype: None
        """
        return self.calib_offsets.GetReferenceBasePosition(x, y, z, roll, pitch, yaw)

    def set_calib_reference_file(self, i_calib_reference_file: str) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetCalibReferenceFile(CATBSTR iCalibReferenceFile)
                | 
                |     Set the reference calibration file.
                | 
                |     Parameters:
                | 
                |         iCalibReferenceFile
                |             Full path of reference calibration file. 
                | 
                |     Returns:
                |         an HRESULT value.
                |         Legal values:
                | 
                |             S_OK if the operation succeeds
                |             E_FAIL otherwise

        :param str i_calib_reference_file:
        :rtype: None
        """
        return self.calib_offsets.SetCalibReferenceFile(i_calib_reference_file)

    def set_corrected_base_offset(self, x: float, y: float, z: float, roll: float, pitch: float, yaw: float) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetCorrectedBaseOffset(double x,
                | double y,
                | double z,
                | double roll,
                | double pitch,
                | double yaw)
                | 
                |     Set corrected base offset for the robot base wrt robot base reference
                |     position.
                | 
                |     Parameters:
                | 
                |         x
                |             X coordinate of the Corrected robot base offset(in m).
                |             
                |         y
                |             Y coordinate of the Corrected robot base offset(in m).
                |             
                |         z
                |             Z coordinate of the Corrected robot base offset(in m).
                |             
                |         roll
                |             Roll angle of the Corrected robot base offset(in deg).
                |             
                |         pitch
                |             Pitch angle of the Corrected robot base offset(in deg).
                |             
                |         yaw
                |             Pitch angle of the Corrected robot base offset(in deg).
                |             
                | 
                |     Returns:
                |         an HRESULT value.
                |         Legal values:
                | 
                |             S_OK if the operation succeeds
                |             E_FAIL otherwise

        :param float x:
        :param float y:
        :param float z:
        :param float roll:
        :param float pitch:
        :param float yaw:
        :rtype: None
        """
        return self.calib_offsets.SetCorrectedBaseOffset(x, y, z, roll, pitch, yaw)

    def set_corrected_tool_offset(self, x: float, y: float, z: float, roll: float, pitch: float, yaw: float) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetCorrectedToolOffset(double x,
                | double y,
                | double z,
                | double roll,
                | double pitch,
                | double yaw)
                | 
                |     Set corrected tool offset for the robot wrt robot mount
                |     position.
                | 
                |     Parameters:
                | 
                |         x
                |             X coordinate of the Corrected tool offset(in m). 
                |         y
                |             Y coordinate of the Corrected tool offset(in m). 
                |         z
                |             Z coordinate of the Corrected tool offset(in m). 
                |         roll
                |             Roll angle of the Corrected tool offset(in deg). 
                |         pitch
                |             Pitch angle of the Corrected tool offset(in deg). 
                |         yaw
                |             Pitch angle of the Corrected tool offset(in deg). 
                | 
                |     Returns:
                |         an HRESULT value.
                |         Legal values:
                | 
                |             S_OK if the operation succeeds
                |             E_FAIL otherwise

        :param float x:
        :param float y:
        :param float z:
        :param float roll:
        :param float pitch:
        :param float yaw:
        :rtype: None
        """
        return self.calib_offsets.SetCorrectedToolOffset(x, y, z, roll, pitch, yaw)

    def set_nominal_base_offset(self, x: float, y: float, z: float, roll: float, pitch: float, yaw: float) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetNominalBaseOffset(double x,
                | double y,
                | double z,
                | double roll,
                | double pitch,
                | double yaw)
                | 
                |     Set nominal base offset for the robot base wrt robot base reference
                |     position.
                | 
                |     Parameters:
                | 
                |         x
                |             X coordinate of the Nominal robot base offset(in m).
                |             
                |         y
                |             Y coordinate of the Nominal robot base offset(in m).
                |             
                |         z
                |             Z coordinate of the Nominal robot base offset(in m).
                |             
                |         roll
                |             Roll angle of the Nominal robot base offset(in deg).
                |             
                |         pitch
                |             Pitch angle of the Nominal robot base offset(in deg).
                |             
                |         yaw
                |             Pitch angle of the Nominal robot base offset(in deg).
                |             
                | 
                |     Returns:
                |         an HRESULT value.
                |         Legal values:
                | 
                |             S_OK if the operation succeeds
                |             E_FAIL otherwise

        :param float x:
        :param float y:
        :param float z:
        :param float roll:
        :param float pitch:
        :param float yaw:
        :rtype: None
        """
        return self.calib_offsets.SetNominalBaseOffset(x, y, z, roll, pitch, yaw)

    def set_nominal_tool_offset(self, x: float, y: float, z: float, roll: float, pitch: float, yaw: float) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetNominalToolOffset(double x,
                | double y,
                | double z,
                | double roll,
                | double pitch,
                | double yaw)
                | 
                |     Set nominal tool offset for the robot wrt robot mount
                |     position.
                | 
                |     Parameters:
                | 
                |         x
                |             X coordinate of the Nominal tool offset(in m). 
                |         y
                |             Y coordinate of the Nominal tool offset(in m). 
                |         z
                |             Z coordinate of the Nominal tool offset(in m). 
                |         roll
                |             Roll angle of the Nominal tool offset(in deg). 
                |         pitch
                |             Pitch angle of the Nominal tool offset(in deg). 
                |         yaw
                |             Pitch angle of the Nominal tool offset(in deg). 
                | 
                |     Returns:
                |         an HRESULT value.
                |         Legal values:
                | 
                |             S_OK if the operation succeeds
                |             E_FAIL otherwise

        :param float x:
        :param float y:
        :param float z:
        :param float roll:
        :param float pitch:
        :param float yaw:
        :rtype: None
        """
        return self.calib_offsets.SetNominalToolOffset(x, y, z, roll, pitch, yaw)

    def set_reference_base_position(self, x: float, y: float, z: float, roll: float, pitch: float, yaw: float) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetReferenceBasePosition(double x,
                | double y,
                | double z,
                | double roll,
                | double pitch,
                | double yaw)
                | 
                |     Set reference base position of robot.
                | 
                |     Parameters:
                | 
                |         x
                |             X coordinate of the Robot base position(in m). 
                |         y
                |             Y coordinate of the Robot base position(in m). 
                |         z
                |             Z coordinate of the Robot base position(in m). 
                |         roll
                |             Roll angle of the Robot Base position(in deg). 
                |         pitch
                |             Pitch angle of the Robot Base position(in deg). 
                |         yaw
                |             Pitch angle of the Robot Base position(in deg). 
                | 
                |     Returns:
                |         an HRESULT value.
                |         Legal values:
                | 
                |             S_OK if the operation succeeds
                |             E_FAIL otherwise

        :param float x:
        :param float y:
        :param float z:
        :param float roll:
        :param float pitch:
        :param float yaw:
        :rtype: None
        """
        return self.calib_offsets.SetReferenceBasePosition(x, y, z, roll, pitch, yaw)

    def __repr__(self):
        return f'CalibOffsets(name="{self.name}")'
