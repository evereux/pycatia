#! /usr/bin/python3.6

"""

    Example - License Settings - 001:

    Determine if a license for DF1 has been requested.

"""

##########################################################
# insert syspath to project folder so examples can be run.
# for development purposes.
import os
import sys

sys.path.insert(0, os.path.abspath('..\\pycatia'))
##########################################################

from pycatia import catia
from pycatia.system_interfaces.license_setting_att import LicenseSettingAtt
from pycatia.in_interfaces.setting_controllers import SettingControllers

cat_lic = "AL3.prd"

caa = catia()
settings_controller = SettingControllers(caa)
setting_controller = settings_controller.item("CATSysLicenseSettingCtrl")
license_settings = LicenseSettingAtt(setting_controller)

status = license_settings.get_license(cat_lic)

if status == "Requested":
    print(f'License "{cat_lic}" has been requested.')
elif status == "NotRequested":
    print(f'License "{cat_lic}" has not been requested.')
