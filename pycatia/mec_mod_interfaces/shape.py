#! /usr/bin/python3.6
# module initially auto generated using V5Automation.chm from CATIA R25

from pycatia.system_interfaces.base_object import AnyObject


class Shape(AnyObject):
    """
        .. note::
            CAA V5 Visual Basic help

                | Represents the Shape object.It is an abstract object which is not
                | intended to be created as such, from which all objects having a shape
                | representation derive.

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.shape = com_object

    def __repr__(self):
        return f'Shape(name={self.name})'
