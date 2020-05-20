#! /usr/bin/python3.6

from win32com.client import Dispatch

from pycatia.in_interfaces.application import Application


def catia_application():
    return Application(Dispatch('CATIA.Application'))
