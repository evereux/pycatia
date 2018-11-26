#! /usr/bin/python36

from catia_python import Application
from catia_python import Document


class Part:

    def __init__(self, document):
        """

        ### FROM CAA V5 Visual Basic help ###
        # The root level object inside a PartDocument object.
        # Role: It aggregates all the objects making up the part document.
        # It provides many factories and collections. The collections list only the direct children of the part.
        # Selection.Search allows to get all objects of one type.

        The CATIA Part object is accessible using either self.part.Part of self.catia_part.

        :param document: CATIA Document COM object.
        """

        self.part = document.Part

    @property
    def catia_part(self):
        """
        Returns the CATIA Part object. Same as self.part.Part.
        :return:
        """

        return self.part.part

    @property
    def name(self):
        """

        :return:
        """

        return self.part.Name

    def get_axis_systems(self):
        """
        This will not return axis systems inside geometrical sets.
        #todo implement selection search feature to get all axis systems
            inside parts.
        :return:
        """

        catia_axes = self.part.AxisSystems
        axes = list()

        for i in range(0, catia_axes.Count):
            axis = catia_axes.Item(i + 1)
            axes.append(axis)

        return axes

    def get_axes_names(self):
        """

        :return:
        """

        names = list()

        for axis in self.get_axis_systems():
            name = axis.name
            names.append(name)

        return names

    def get_axis_by_name(self, name):
        """

        :return:
        """

        for axis_name in self.get_axes_names():
            if name == axis_name:
                return self.part.AxesSystems.Item(name)
        return None

    def get_bodies(self):
        """

        :return:
        """

        catia_bodies = self.part.Bodies
        bodies = list()

        for i in range(0, catia_bodies.Count):
            body = catia_bodies.Item(i + 1)
            bodies.append(body)

        return bodies

    def get_bodies_names(self):
        """

        :return:
        """

        names = list()

        for body in self.get_bodies():
            name = body.name
            names.append(name)

        return names

    def get_body_by_name(self, name):
        """

        :return:
        """

        for body_name in self.get_bodies_names():
            if name == body_name:
                return self.part.Bodies.Item(name)
        return None

    def get_hybrid_bodies(self):
        """

        :return:
        """

        hybrid_bodies = self.part.HybridBodies
        bodies = list()

        for i in range(0, hybrid_bodies.Count):
            body = hybrid_bodies.Item(i + 1)
            bodies.append(body)

        return bodies

    def get_hybrid_bodies_names(self):
        """

        :return:
        """

        hybrid_bodies = self.get_hybrid_bodies()
        bodies = list()

        for hybrid_body in hybrid_bodies:
            body = hybrid_body.Name
            bodies.append(body)

        return bodies

    def get_hybrid_body_by_name(self, name):
        """

        :return:
        """

        for hybrid_body_name in self.get_hybrid_bodies_names():
            if name == hybrid_body_name:
                return self.part.HybridBodies.Item(name)
        return None

    def __repr__(self):
        """

        :return:
        """
        return f'Part object (name: {self.name})'


def get_document_part_object():
    """

    :return: Part(), Document()
    """

    catia = Application()
    document = Document(catia.catia).document
    part = Part(document)

    return document, part
