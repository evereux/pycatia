#! /usr/bin/python3.9

from win32com.client import Dispatch
import pythoncom

from pycatia.in_interfaces.application import Application


def catia_application(co_initialise=False) -> Application:
    if co_initialise:
        return Application(Dispatch('CATIA.Application', pythoncom.CoInitialize()))
    return Application(Dispatch('CATIA.Application'))
