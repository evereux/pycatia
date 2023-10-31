#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.setting_controller import SettingController


class ColourStdObjectSettingAtt(SettingController):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     System.SettingController
                |                         ColorSTDObjectSettingAtt
                | 
                | The interface to access a CATIAColorSTDObjectSettingAtt.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.colour_std_object_setting_att = com_object

    def get_plate_colour(self, o_plate_colour_r: int, o_plate_colour_g: int, o_plate_colour_b: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetPlateColor(long oPlateColorR,
                | long oPlateColorG,
                | long oPlateColorB)
                | 
                |     Returns or sets the PlateColor parameter.
                | 
                |     Ensure consistency with the C++ interface to which the work is delegated.

        :param int o_plate_colour_r:
        :param int o_plate_colour_g:
        :param int o_plate_colour_b:
        :rtype: None
        """
        return self.colour_std_object_setting_att.GetPlateColor(o_plate_colour_r, o_plate_colour_g, o_plate_colour_b)

    def get_plate_colour_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetPlateColorInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the PlateColor
                |     parameter.
                |     Role:Retrieves the state of the PlateColor parameter in the current
                |     environment.
                | 
                |     Parameters:
                | 
                |         ioAdminLevel
                | 
                |             If the parameter is locked, AdminLevel gives the administration
                |             level that imposes the value of the parameter.
                |             If the parameter is not locked, AdminLevel gives the administration
                |             level that will give the value of the parameter after a reset.
                |             
                |         ioLocked
                |             Indicates if the parameter has been locked. 
                | 
                |     Returns:
                |         Indicates if the parameter has been explicitly modified or remain to
                |         the administrated value.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.colour_std_object_setting_att.GetPlateColorInfo(io_admin_level, io_locked)

    def get_shape_colour(self, o_shape_colour_r: int, o_shape_colour_g: int, o_shape_colour_b: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetShapeColor(long oShapeColorR,
                | long oShapeColorG,
                | long oShapeColorB)
                | 
                |     Returns or sets the ShapeColor parameter.
                | 
                |     Ensure consistency with the C++ interface to which the work is delegated.

        :param int o_shape_colour_r:
        :param int o_shape_colour_g:
        :param int o_shape_colour_b:
        :rtype: None
        """
        return self.colour_std_object_setting_att.GetShapeColor(o_shape_colour_r, o_shape_colour_g, o_shape_colour_b)

    def get_shape_colour_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetShapeColorInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the ShapeColor
                |     parameter.
                |     Role:Retrieves the state of the ShapeColor parameter in the current
                |     environment.
                | 
                |     Parameters:
                | 
                |         ioAdminLevel
                | 
                |             If the parameter is locked, AdminLevel gives the administration
                |             level that imposes the value of the parameter.
                |             If the parameter is not locked, AdminLevel gives the administration
                |             level that will give the value of the parameter after a reset.
                |             
                |         ioLocked
                |             Indicates if the parameter has been locked. 
                | 
                |     Returns:
                |         Indicates if the parameter has been explicitly modified or remain to
                |         the administrated value.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.colour_std_object_setting_att.GetShapeColorInfo(io_admin_level, io_locked)

    def set_plate_colour(self, i_plate_colour_r: int, i_plate_colour_g: int, i_plate_colour_b: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetPlateColor(long iPlateColorR,
                | long iPlateColorG,
                | long iPlateColorB)

        :param int i_plate_colour_r:
        :param int i_plate_colour_g:
        :param int i_plate_colour_b:
        :rtype: None
        """
        return self.colour_std_object_setting_att.SetPlateColor(i_plate_colour_r, i_plate_colour_g, i_plate_colour_b)

    def set_plate_colour_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetPlateColorLock(boolean iLocked)
                | 
                |     Locks or unlocks the PlateColor parameter.
                |     Role:Locks or unlocks the PlateColor parameter if it is possible in the
                |     current administrative context. In user mode this method will always return
                |     E_FAIL.
                | 
                |     Parameters:
                | 
                |         iLocked
                |             the locking operation to be performed Legal
                |             values:
                |             TRUE : to lock the parameter.
                |             FALSE: to unlock the parameter.

        :param bool i_locked:
        :rtype: None
        """
        return self.colour_std_object_setting_att.SetPlateColorLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_plate_color_lock'
        # # vba_code = """
        # # Public Function set_plate_color_lock(color_std_object_setting_att)
        # #     Dim iLocked (2)
        # #     color_std_object_setting_att.SetPlateColorLock iLocked
        # #     set_plate_color_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_shape_colour(self, i_shape_colour_r: int, i_shape_colour_g: int, i_shape_colour_b: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetShapeColor(long iShapeColorR,
                | long iShapeColorG,
                | long iShapeColorB)

        :param int i_shape_colour_r:
        :param int i_shape_colour_g:
        :param int i_shape_colour_b:
        :rtype: None
        """
        return self.colour_std_object_setting_att.SetShapeColor(i_shape_colour_r, i_shape_colour_g, i_shape_colour_b)

    def set_shape_colour_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetShapeColorLock(boolean iLocked)
                | 
                |     Locks or unlocks the ShapeColor parameter.
                |     Role:Locks or unlocks the ShapeColor parameter if it is possible in the
                |     current administrative context. In user mode this method will always return
                |     E_FAIL.
                | 
                |     Parameters:
                | 
                |         iLocked
                |             the locking operation to be performed Legal
                |             values:
                |             TRUE : to lock the parameter.
                |             FALSE: to unlock the parameter.

        :param bool i_locked:
        :rtype: None
        """
        return self.colour_std_object_setting_att.SetShapeColorLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_shape_color_lock'
        # # vba_code = """
        # # Public Function set_shape_color_lock(color_std_object_setting_att)
        # #     Dim iLocked (2)
        # #     color_std_object_setting_att.SetShapeColorLock iLocked
        # #     set_shape_color_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'ColourStdObjectSettingAtt(name="{self.name}")'
