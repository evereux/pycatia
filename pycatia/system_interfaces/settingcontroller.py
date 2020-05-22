#! /usr/bin/python3.6
# module initially auto generated using V5Automation.chm from CATIA R25 on 2020-05-18 10:56:40.651039

from pycatia.system_interfaces.base_object import AnyObject


class SettingController(AnyObject):
    """
        .. note::
            CAA V5 Visual Basic help

                | Represents the base object for setting controllers.Role: A setting
                | controller manages all or only a part of the parameters available in a
                | property page of the dialog displayed using the Options command of the
                | Tools menu. Each setting parameter may be represented by one or
                | several setting attribute  in the underlying setting repository.All
                | setting controllers share the five methods of the SettingController
                | object to deal with the whole set, or a subset of the setting
                | attributes:In addition, each setting controller exposes four methods
                | per setting parameter: two methods to access the setting attribute
                | values, that usually make up a  read/write property if the setting
                | parameter is represented by a single setting attribute, a method to
                | manage the setting parameter lock, and a method to  retrieve the state
                | of the setting parameter. The first two methods are  parameter-
                | specific and are fully described in the setting controller object
                | that managing the setting parameter.  The last two methods have always
                | the same signature and the same behavior  whatever the setting
                | parameter. They are described below. PARAMETER is used in place of the
                | actual setting parameter name.

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.setting_controller = com_object.SettingController

    def commit(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Commit
                | o Sub Commit(    )
                | 
                | Makes a memory copy of the setting attribute values. Role:
                | Commit saves the current values of the setting attributes
                | managed by the setting controller in a specific memory area.
                | Successive calls to Commit overwrite the memory area. The
                | values saved by the last call to Commit can be restored from
                | that memory area using the method.

        :return:
        """
        return self.setting_controller.Commit()

    def reset_to_admin_values(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | ResetToAdminValues
                | o Sub ResetToAdminValues(    )
                | 
                | Restores the administrated values of the all attributes.
                | Role: ResetToAdminValues restores all the values of the
                | setting attributes managed by the setting controller to
                | either the values set by the setting administrator, or to
                | their default values if the setting administrator did not
                | change them.

        :return:
        """
        return self.setting_controller.ResetToAdminValues()

    def reset_to_admin_values_by_name(self, i_att_list):
        """
        .. note::
            CAA V5 Visual Basic help

                | ResetToAdminValuesByName
                | o Sub ResetToAdminValuesByName(        iAttList)
                | 
                | Restores the administrated values of a subset of the
                | attributes. Role: ResetToAdminValuesByName restores the
                | values of a subset of the setting attributes managed by the
                | setting controller to either the values set by the setting
                | administrator, or to their default values if the setting
                | administrator did not change them.

        :param i_att_list:
        :return:
        """
        return self.setting_controller.ResetToAdminValuesByName(i_att_list)

    def rollback(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Rollback
                | o Sub Rollback(    )
                | 
                | Restores the last memory copy of the setting attribute
                | values. Role: Rollback restores the values of the setting
                | attributes managed by the setting controller from the memory
                | area. All values of the setting attributes managed by the
                | setting controller modified since the last call to are
                | restored to the values they had when this last was called.

        :return:
        """
        return self.setting_controller.Rollback()

    def save_repository(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | SaveRepository
                | o Sub SaveRepository(    )
                | 
                | Makes a persistent copy of the setting attribute values on
                | file. Role: SaveRepository saves the current values of the
                | setting attributes managed by the setting controller in a
                | setting repository file. To avoid inconsistencies,
                | SaveRepository first saves the values in the memory area
                | used by the method by calling before writing the values in
                | the setting repository file.

        :return:
        """
        return self.setting_controller.SaveRepository()

    def __repr__(self):
        return f'SettingController(name="{self.name}")'
