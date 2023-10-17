#! /usr/bin/python3.8

from .caa import caa


def resize_active_view():
    active_window = caa.active_window
    active_viewer = active_window.active_viewer
    active_viewer.reframe()
