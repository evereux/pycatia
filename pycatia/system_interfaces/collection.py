#! /usr/bin/python3.6
# module initially auto generated using V5Automation.chm from CATIA V5 R25

from pycatia.system_interfaces.base_object import AnyObject


class Collection:
    """
        .. note::
            CAA V5 Visual Basic help

                | Represents the base object for collections.As a base object, it
                | provides properties and methods shared by any other object.

    """

    def __init__(self, com_collection_object, child_object=AnyObject):
        self.com_object = com_collection_object
        self.child_object = child_object

    @property
    def application(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Application
                | o Property Application(    ) As Application
                |
                | Returns the application. The application is the root object in the
                | object structure and can be retrieved from any object in the object
                | structure using the Application property. The Application property is
                | the way to jump from any object up to the root of the object data
                | structure, allowing then to navigate downwards. For in-process
                | scripting, the application is always referred to as CATIA. Note that
                | the Application property of the Application object returns the
                | Application object itself.  Example: This example retrieves in
                | CurrentApplication the application object, root of the object
                | structure, from a given object of this structure: a document refered
                | to using the MyDocCollecion variable.  Dim CurrentApplication As
                | Application Set CurrentApplication = MyDocCollecion.Application


                | Parameters:

        """
        return self.com_object.Application

    @property
    def count(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Count
                | o Property Count(    ) As long
                |
                | Returns the number of objects in the collection. This is handy to scan
                | all the objects in a collection.  Example: This example retrieves in
                | ObjectNumber the number of objects currently gathered in MyCollection.
                | ObjectNumber = MyCollection.Count


                | Parameters:

        :return: int
        """
        return self.com_object.Count

    def items(self):
        """
        :return: [self.child_object()]
        """
        items_list = []

        for i in range(self.com_object.Count):
            item = self.child_object(self.com_object.Item(i + 1))
            items_list.append(item)

        return items_list

    def get_item_by_index(self, index):
        """

        .. warning::

            The index when not a string must be it's python index (indexes in python start from 0).
            collection. The COM interface index starts at 1.


        :param str/int index: relation name or index
        :return: item
        """

        if isinstance(index, int):
            index += 1

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

    @property
    def name(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Name
                | o Property Name(    ) As CATBSTR
                |
                | Returns or sets the name of the object. The name is a character string
                | you can assign to any object to handle it easier. In the case of an
                | object part of a collection, the name can often be used in place of
                | the object rank to retrieve or remove the object, providing the Item
                | and Remove methods of the collection feature an argument with the
                | Variant type. If the object has no name set, the name returned is the
                | one of its parent.  Example: This example sets to MyObject the name
                | Nice and Handy Object Name.  MyObject.Name("Nice and Handy Object
                | Name")


                | Parameters:

            :return: str
        """
        return self.com_object.Name

    @property
    def parent(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Parent
                | o Property Parent(    ) As CATBaseDispatch
                |
                | Returns the parent object. The parent object of a given object is the
                | object that created this object, usually the object just above in the
                | object tree structure and that aggregates it. In the case of an object
                | part of a collection, the parent object is not the collection object
                | itself, but the object that aggregates the collection object. The
                | Parent property is the way to step upwards in the object data
                | structure. Note that the Parent property of the Application object
                | returns the Application object itself.  Example: This example
                | retrieves in ParentObject the parent object of the GivenObject object.
                | Dim ParentObject As AnyObject Set ParentObject = GivenObject.Parent


                | Parameters:


        """
        return self.com_object.Parent

    def get_item(self, id_name):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetItem
                | o Func GetItem(    CATBSTR    IDName) As CATBaseDispatch
                |
                | Returns an object from its name. Role: To retrieve an object when only
                | its name is available. You should not use this method, but you can
                | find it in the macros generated by the Tools->Macro command.
                |
                | Parameters:
                | IDName
                |    The searched obect name
                |  Returns:
                |     The searched object

            :param int|str id_name:
            :return:
        """
        return self.com_object.GetItem(id_name)
