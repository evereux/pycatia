#! /usr/bin/python3.6

"""

    Example 24:

    Determine if a license for DF1 has been requested.

"""

from pycatia import catia
from pycatia.enumeration.enumeration_types import cat_constraint_type

from pycatia import catia
from pycatia.system_interfaces.license_setting_att import LicenseSettingAtt
from pycatia.in_interfaces.setting_controllers import SettingControllers

license = "AL3.prd"

caa = catia()
settings_controller = SettingControllers(caa)
setting_controller = settings_controller.item("CATSysLicenseSettingCtrl")
license_settings = LicenseSettingAtt(setting_controller)

status = license_settings.get_license(license)

if status == "Requested":
    print(f'License "{license}" has been requested.')
elif status == "NotRequested":
    print(f'License "{license}" has not been requested.')
