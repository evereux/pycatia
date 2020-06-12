#! /usr/bin/python3.6
# module initially auto generated using V5Automation.chm from CATIA R25

from pycatia.system_interfaces.any_object import AnyObject


class Factory(AnyObject):
    """
        .. note::
            CAA V5 Visual Basic help

                | Abstract object gathering behaviours of all objects being a factory.

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.factory = com_object

    def __repr__(self):
        return f'Factory()'
