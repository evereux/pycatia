#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-10 10:58:07.270911

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.

"""
from typing import Iterator
from typing import TYPE_CHECKING

from pycatia.base_interfaces.pycatia import PyCATIA
from pycatia.system_interfaces.any_object import AnyObject

# from pycatia.system_interfaces.cat_base_dispatch import CATBaseDispatch

if TYPE_CHECKING:
    from pycatia.in_interfaces.application import Application


class Collection(PyCATIA):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-10 10:58:07.270911)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 Collection
                |
                | Represents the base object for collections.
                | As a base object, it provides properties and methods shared by any other
                | object.

    """

    def __init__(self, com_object, child_object=AnyObject):
        super().__init__()
        self.com_object = com_object
        self.child_object = child_object

    @property
    def application(self) -> 'Application':
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-10 10:58:07.270911)
                | o Property Application() As Application (Read Only)
                |
                |     Returns the application. The application is the root object in the object
                |     structure and can be retrieved from any object in the object structure using
                |     the Application property. The Application property is the way to jump from any
                |     object up to the root of the object data structure, allowing then to navigate
                |     downwards. For in-process scripting, the application is always referred to as
                |     CATIA. Note that the Application property of the Application object returns the
                |     Application object itself.
                |
                |     Example:
                |         This example retrieves in CurrentApplication the application object,
                |         root of the object structure, from a given object of this structure: a document
                |         refered to using the MyDocCollecion variable.
                |
                |          Dim CurrentApplication As Application
                |          Set CurrentApplication = MyDocCollecion.Application

        :rtype: Application
        """
        from pycatia.in_interfaces.application import Application
        return Application(self.com_object.Application)

    @property
    def count(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-10 10:58:07.270911)
                | o Property Count() As long (Read Only)
                |
                |     Returns the number of objects in the collection. This is handy to scan all
                |     the objects in a collection.
                |
                |     Example:
                |         This example retrieves in ObjectNumber the number of objects currently
                |         gathered in MyCollection.
                |
                |          ObjectNumber = MyCollection.Count

        :rtype: int
        """

        return self.com_object.Count

    @property
    def name(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-10 10:58:07.270911)
                | o Property Name() As CATBSTR (Read Only)
                |
                |     Returns or sets the name of the object. The name is a character string you
                |     can assign to any object to handle it easier. In the case of an object part of
                |     a collection, the name can often be used in place of the object rank to
                |     retrieve or remove the object, providing the Item and Remove methods of the
                |     collection feature an argument with the Variant type. If the object has no name
                |     set, the name returned is the one of its parent.
                |
                |     Example:
                |         This example sets to MyObject the name Nice and Handy Object
                |         Name.
                |
                |          MyObject.Name("Nice and Handy Object Name")

        :rtype: str
        """

        return self.com_object.Name

    @property
    def parent(self) -> AnyObject:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-10 10:58:07.270911)
                | o Property Parent() As CATBaseDispatch (Read Only)
                |
                |     Returns the parent object. The parent object of a given object is the
                |     object that created this object, usually the object just above in the object
                |     tree structure and that aggregates it. In the case of an object part of a
                |     collection, the parent object is not the collection object itself, but the
                |     object that aggregates the collection object. The Parent property is the way to
                |     step upwards in the object data structure. Note that the Parent property of the
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

    def get_item(self, id_name: str) -> AnyObject:
        """

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-10 10:58:07.270911))
                | o Func GetItem(CATBSTR IDName) As CATBaseDispatch
                |
                |     Returns an object from its name.
                |     Role: To retrieve an object when only its name is available. You should not
                |     use this method, but you can find it in the macros generated by the
                |     Tools->Macro command.
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

        return self.child_object(self.com_object.GetItem(id_name))

    def get_item_by_index(self, index):
        """
        :param str/int index: relation name or index
        :return: child_object
        """

        return self.child_object(self.com_object.Item(index))

    def get_item_names(self):
        names = []
        for i in range(self.com_object.Count):
            name = self.com_object.Item(i + 1).Name
            names.append(name)

        return names

    def get_item_by_name(self, name):
        for i in range(self.com_object.Count):
            if self.com_object.Item(i + 1).Name == name:
                return self.child_object(self.com_object.Item(i + 1))

        return None

    def items(self):
        """
        :return: [self.child_object()]
        """
        items_list = []

        for i in range(self.com_object.Count):
            item = self.child_object(self.com_object.Item(i + 1))
            items_list.append(item)

        return items_list

    def __len__(self):

        return self.count

    def __getitem__(self, n: int) -> AnyObject:
        if (n + 1) > self.count:
            raise StopIteration

        return AnyObject(self.com_object.Item(n + 1))

    def __iter__(self) -> Iterator[AnyObject]:
        for i in range(self.count):
            yield self.child_object(self.com_object.Item(i + 1))

    def __repr__(self):
        return f'Collection(name="{self.name}")'
