from .caa import caa


def resize_active_view():
    active_window = caa.active_window
    active_viewer = active_window.active_viewer
    active_viewer.reframe()
