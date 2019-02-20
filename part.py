#! /usr/bin/python3.6

from .reference import create_reference

geometrical_feature_type = [
    'Unknown',
    'Point',
    'Curve',
    'Line',
    'Circle',
    'Surface',
    'Plane',
    'Solid, Volume'
]


class Part:
    """
    .. note::
        CAA V5 Visual Basic help

        The root level object inside a PartDocument object.
        Role: It aggregates all the objects making up the part document.
        It provides many factories and collections. The collections list only the direct children of the part.
        Selection.Search allows to get all objects of one type.

    :param part: CATIA Part COM object.
    """

    def __init__(self, part):

        self.part = part

    @property
    def name(self):
        """

        :return: part name
        """

        return self.part.Name

    @property
    def density(self):
        """
        Returns the density of the part in kg_m3.

        .. warning::
            This will only display the density of the main part body. If there are several bodies within the part with
            different densities you should not rely on this method!.


        .. note::
            CAA V5 Visual Basic help

            Returns the part density.
            | Example:
            | The following example displays the density of the part:
            |     Set partRoot = partDoc.Part
            |       MsgBox "The density is " & partRoot.Density

        :return float(): density
        """

        return self.part.Density

    def get_annotation_sets(self):
        """
        .. note::
            CAA V5 Visual Basic help

            Returns the collection object containing the annotation sets. All the annotation sets
            that are aggregated in the part might be accessed thru that collection.

            | Example:
            | The following example returns in annotationSets the annotation sets of the partRoot part
            | from the partDoc part document:
            |
            | Set partRoot = partDoc.Part
            | Dim annotationSets As AnnotationSets
            | Set annotationSets = partRoot.AnnotationSets

        :return: AnnotationSets COM object
        """

        return self.part.AnnotationSets

    def get_axes_names(self):
        """
        :return: list of axis names
        """

        names = list()

        for axis in self.get_axis_systems():
            name = axis.name
            names.append(name)

        return names

    def get_axis_systems(self):
        """
        This will not return axis systems inside geometrical sets.
        # todo implement selection search feature to get all axis systems inside parts.

        :return:
        """

        catia_axes = self.part.AxisSystems
        axes = list()

        for i in range(0, catia_axes.Count):
            axis = catia_axes.Item(i + 1)
            axes.append(axis)

        return axes

    def get_axis_by_name(self, name):
        """
        :return: Axis System COM object
        """

        for axis_name in self.get_axes_names():
            if name == axis_name:
                return self.part.AxisSystems.Item(name)
        return None

    def get_bodies(self):
        """
        :return: list()
        """

        catia_bodies = self.part.Bodies
        bodies = list()

        for i in range(0, catia_bodies.Count):
            body = catia_bodies.Item(i + 1)
            bodies.append(body)

        return bodies

    def get_bodies_names(self):
        """
        :return: list()
        """

        names = list()

        for body in self.get_bodies():
            name = body.name
            names.append(name)

        return names

    def get_body_by_name(self, name):
        """
        :return: Body COM object
        """

        for body_name in self.get_bodies_names():
            if name == body_name:
                return self.part.Bodies.Item(name)
        return None

    def get_geometric_elements(self):
        """

        .. note::
            CAA V5 Visual Basic help

            | Returns the collection object containing the part geometrical elements. Only 3D elements are concerned
            | here, 2D elements are managed in sketches. The origin elements are also accessible thru that collection.
            | Example:
            | The following example returns in geomElts the 3D elements of the partRoot part from the partDoc part
            | document:
            |       Set partRoot = partDoc.Part
            |       Set geomElts = partRoot.GeometricElements


        !!! WARNING !!! The items outputted from this don't return the correct geometrical_feature_type.
        As yet, not sure what impact that will have on measuring.

        elem = geometric_elements.Item(5)
        print(elem.name, part.get_geometrical_feature_type(elem))
        returns Point.1 Unknown

        :return: GeometricElements COM object.
        """

        return self.part.GeometricElements

    def get_geometrical_feature_type(self, geometrical_feature):
        """

        !!! WARNING !!! Use with care on items returned from self.get_geometric_elements()
        Reported types are incorrect with the version of CATIA tested with.

        :param geometrical_feature:
        :return:
        """

        reference_object = create_reference(self.part, geometrical_feature)
        feature_type = self.part.HybridShapeFactory.GetGeometricalFeatureType(reference_object)

        return geometrical_feature_type[feature_type]

    def get_hybrid_bodies(self):
        """

        :return: list()
        """

        hybrid_bodies = self.part.HybridBodies
        bodies = list()

        for i in range(0, hybrid_bodies.Count):
            body = hybrid_bodies.Item(i + 1)
            bodies.append(body)

        return bodies

    def get_hybrid_bodies_names(self):
        """

        :return: list
        """

        hybrid_bodies = self.get_hybrid_bodies()
        bodies = list()

        for hybrid_body in hybrid_bodies:
            body = hybrid_body.Name
            bodies.append(body)

        return bodies

    def get_hybrid_body_by_name(self, name):
        """

        :return: HybridBody COM object.
        """

        for hybrid_body_name in self.get_hybrid_bodies_names():
            if name == hybrid_body_name:
                return self.part.HybridBodies.Item(name)
        return None

    @staticmethod
    def get_hybrid_shapes_from_hybrid_body(hybrid_body):
        """

        :return: list()
        """

        shapes = list()
        for i in range(hybrid_body.HybridShapes.Count):
            shapes.append(hybrid_body.HybridShapes.Item(i + 1))

        return shapes

    def create_geometrical_set(self, name):
        """
        Creates a new geometrical set / HybridBody with name.
        :param name: str()
        :return:
        """

        new_geometrical_set = self.part.HybridBodies.Add()
        new_geometrical_set.Name = name

        return new_geometrical_set

    def is_upated(self, catia_object):
        """
        :Example:

            >>> with CATIADocHandler(cat_part) as handler:
            >>>    part = handler.document.part()
            >>>
            >>>    assert part.is_upated(part.part)

        .. note::
            CAA V5 Visual Basic help

            Func IsUpToDate( AnyObject  iObject) As boolean

            | Indicates whether an object needs to be updated. An object which is not up-to-date has not be calculated
            | with the last specifications.
            | Parameters:
            |   iObject
            | The object to examine
            |   Example:
            | The following example returns in isuptodate whether the pad1 pad is up-to-date:
            |   Set partRoot = partDoc.Part
            |   Set pad1 = partRoot.FindObjectByName("Pad.1")
            |   isuptodate = partRoot.IsUpToDate(pad1)

        :param catia_object:
        :return:
        """

        return self.part.IsUpToDate(catia_object)

    def update(self):
        """
        .. note::
            CAA V5 Visual Basic help

            Sub Update( )
            Updates of the part result with respect to its specifications. Any composing specification that hasn't its
            result up-to-date will recompute it, thus propagating changes to the whole part.

            | Example:
            | The following example update the part:
            | Set partRoot = partDoc.Part
            |   partRoot.Update


        :return:
        """

        self.part.Update()

    def __repr__(self):
        """
        :return: str()
        """
        return f'Part(name: {self.name})'
