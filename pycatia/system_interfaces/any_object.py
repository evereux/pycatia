#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-09 09:53:18.676780

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.

"""
from typing import TYPE_CHECKING

from pycatia.base_interfaces.pycatia import PyCATIA

if TYPE_CHECKING:
    from pycatia.in_interfaces.application import Application


class AnyObject(PyCATIA):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 AnyObject
                |
                | Represents the base object for all other objects except collection and
                | reference objects.
                | As a base object, it provides properties shared by any other
                | object.

    """

    def __init__(self, com_object):
        super().__init__()
        self.com_object = com_object

    @property
    def application(self) -> 'Application':
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property Application() As Application (Read Only)
                |
                |     Returns the application. The application is the root object of the object
                |     structure and can be retrieved from any object in this object structure using
                |     the Application property. The root object, also called top-level object, is the
                |     object located at the top of the application's object structure. It is used by
                |     clients to retrieve and navigate across all the application's subordinate
                |     objects. If the client runs in-process, it retrieves the object at the top of
                |     the object structure. If the client runs out-process, it should call the
                |     GetApplication method to retrieve the object at the top of the object
                |     structure, which is the only object accessible from outside. The Application
                |     property is thus the way to jump from any object up to the root of the object
                |     structure, allowing then to navigate downwards. For in-process scripting, the
                |     application is always referred to as CATIA. Note that the Application property
                |     of the Application object returns the Application object
                |     itself.
                |
                |     Example:
                |         This example retrieves in CurrentApplication the application object,
                |         root of the object structure, from a given object of this structure: a document
                |         refered to using the MyDoc variable.
                |
                |          Dim CurrentApplication As Application
                |          Set CurrentApplication = MyDoc.Application

        :rtype: com_object
        """
        from pycatia.in_interfaces.application import Application
        return Application(self.com_object.Application)

    @property
    def name(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property Name() As CATBSTR
                |
                |     Returns or sets the name of the object. The name is a character string
                |     automatically assigned to any object to handle it easier. Even if the Name
                |     property allows you to reassign an object name, this is not advised. Many
                |     objects, such as the application and the collections, have names that you must
                |     not change, and it's safer to use Name as a read only property. When an object
                |     is part of a collection, the object name can often be used in place of the
                |     object rank to retrieve or remove the object, providing the Item and Remove
                |     methods of the collection feature an argument with the Variant type. A name
                |     must start with a letter. It can include numbers, but it can't include spaces.
                |     If the object has no name set, the default name returned is the object type.
                |     For example, the Name property of a Viewer3D object with no name set returns
                |     Viewer3D.
                |
                |     Example:
                |         This example retrieves in MyObjectName the name of the MyObject
                |         object.
                |
                |          MyObjectName = MyObject.Name

        :rtype: str
        """

        return self.com_object.Name

    @name.setter
    def name(self, value: str):
        """
        :param str value:
        """

        self.com_object.Name = value

    @property
    def parent(self) -> 'AnyObject':
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property Parent() As CATBaseDispatch (Read Only)
                |
                |     Returns the parent object. The parent object of a given object is the
                |     object just above in the object structure, usually the object that created this
                |     object and that aggregates it. In the case of an object part of a collection,
                |     the parent object can be the collection object itself or the object that
                |     aggregates the collection object. The Parent property is the way to step
                |     upwards in the object structure. Note that the Parent property of the
                |     Application object returns the Application object itself.
                |
                |     Example:
                |         This example retrieves in ParentObject the parent object of the
                |         GivenObject object.
                |
                |          Dim ParentObject As AnyObject
                |          Set ParentObject = GivenObject.Parent

        :rtype: AnyObject
        """

        return AnyObject(self.com_object.Parent)

    def get_item(self, id_name: str) -> 'AnyObject':
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Func GetItem(CATBSTR IDName) As CATBaseDispatch
                |
                |     Returns an object from its name.
                |     Role: To retrieve an object when only its name is
                |     available.
                |
                |     Parameters:
                |
                |         IDName
                |             The searched object name
                |
                |     Returns:
                |         The searched object

        :param str id_name:
        :rtype: AnyObject
        """
        return AnyObject(self.com_object.GetItem(id_name))

    def __repr__(self):
        return f'AnyObject(name="{self.name}")'
