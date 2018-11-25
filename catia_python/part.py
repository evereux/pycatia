#! /usr/bin/python36


class Part:

    def __init__(self, document):
        """

        :param document:
        """

        self.part = document.Part

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
