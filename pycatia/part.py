#! /usr/bin/python3.6

import warnings

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

        :return: str - part name
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

        :return: float
        """

        return self.part.Density

    @property
    def in_work_object(self):
        """

        .. note::
            CAA V5 Visual Basic help

            Property InWorkObject( ) As AnyObject

            | Returns or sets the in work object of the part. The in work object is the object after which a new object
            | is added.
            | Example:
            |   Set partRoot = partDoc.Part
            |   Set partRoot.InWorkObject = cylindricPad
            |   If ( partRoot.InWorkObject <> cylindricPad ) Then
            |       MsgBox "There is a big problem"
            |   End If

        :return: the in work COM object.
        """

        return self.part.InWorkObject

    @in_work_object.setter
    def in_work_object(self, in_work_object):

        self.part.InWorkObject = in_work_object

    def activate(self, item):
        """
        .. note::
            CAA V5 Visual Basic help

            Sub Activate( AnyObject  iObject)

            | Unsuppresses an object for the update process. A unsuppressed object is again taken into account for the
            | calculation of the part.
            | Parameters:
            |   iObject
            |       The object to unsuppress for the update process
            | Example:
            |   The following example unsuppresses the pad1 pad:
            |       Set partRoot = partDoc.Part
            |       Set pad1 = partRoot.FindObjectByName("Pad.1")
            |       partRoot.Activate(pad1)

        :param item:
        :return:
        """

        self.part.Activate(item)

    def create_geometrical_set(self, name):
        """

        :param str name: new geometrical set name.
        :return: geometrical_set
        """

        new_geometrical_set = self.part.HybridBodies.Add()
        new_geometrical_set.Name = name

        return new_geometrical_set

    def create_reference(self, catia_object):
        """
        .. note::
            CAA V5 Visual Basic help

            Func CreateReferenceFromObject( AnyObject  iObject) As Reference

            | Creates a reference from a operator. Use of reference allows a uniform handling of B-Rep and non B-Rep
            | objects.
            | Parameters:
            |   iObject
            |       The geometric object to be referenced. It can be a plane, a line or a point.
            |   Returns:
            |       The reference to the object. This way, a direction can be either an edge of a pad or a 3D line.

        :return:
        """

        return self.part.CreateReferenceFromObject(catia_object)

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
        :return: list(str) - axis names
        """

        names = list()

        for axis in self.get_axis_systems():
            name = axis.name
            names.append(name)

        return names

    def get_axis_systems(self):
        """
        .. warning::
            This will not return axis systems inside geometrical sets.


        # todo: implement selection search feature to get all axis systems inside parts.

        :return: list(axis) - com objects
        """

        catia_axes = self.part.AxisSystems
        axes = list()

        for i in range(0, catia_axes.Count):
            axis = catia_axes.Item(i + 1)
            axes.append(axis)

        warning_text = ('Axis systems contained with geometrical sets are not currently returned.'
                        'Axis systems must be contained within the annotation set `Axis Systems`')

        warnings.warn(warning_text)

        return axes

    def get_axis_by_name(self, name):
        """
        :return: Axis System COM object if found otherwise None.
        """

        for axis_name in self.get_axes_names():
            if name == axis_name:
                return self.part.AxisSystems.Item(name)
        return None

    def get_bodies(self):
        """
        :return: list
        """

        catia_bodies = self.part.Bodies
        bodies = list()

        for i in range(0, catia_bodies.Count):
            body = catia_bodies.Item(i + 1)
            bodies.append(body)

        return bodies

    def get_bodies_names(self):
        """
        :return: list
        """

        names = list()

        for body in self.get_bodies():
            name = body.name
            names.append(name)

        return names

    def get_body_by_name(self, name):
        """
        :return: Body COM object if found otherwise None.
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
                    elem = geometric_elements.Item(5)


        .. warning::
            The items outputted from this don't return the correct geometrical_feature_type.
            As yet, not sure what impact that will have on measuring.

            print(elem.name, part.get_geometrical_feature_type(elem))
            returns Point.1 Unknown


        :return: GeometricElements COM object.
        """

        return self.part.GeometricElements

    def get_geometrical_feature_type(self, reference_object):
        """

        .. warning::
            Use with care on items returned from self.get_geometric_elements()
            Reported types are incorrect with the version of CATIA tested with.


        :param reference_object:
        :return:
        """

        feature_type = self.part.HybridShapeFactory.GetGeometricalFeatureType(reference_object)

        warning_text = ('Use with care on items returned from self.get_geometric_elements()'
                        'Reported types are incorrect with the version of CATIA tested with.')
        warnings.warn(warning_text)

        return geometrical_feature_type[feature_type]

    def get_hybrid_bodies(self):
        """

        :return: list
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

        :return: HybridBody COM object if found otherwise None.
        """

        for hybrid_body_name in self.get_hybrid_bodies_names():
            if name == hybrid_body_name:
                return self.part.HybridBodies.Item(name)
        return None

    @staticmethod
    def get_hybrid_shapes_from_hybrid_body(hybrid_body):
        """

        :return: list
        """

        shapes = list()
        for i in range(hybrid_body.HybridShapes.Count):
            shapes.append(hybrid_body.HybridShapes.Item(i + 1))

        return shapes

    def find_object_by_name(self, name):
        """
        .. note::
            CAA V5 Visual Basic help
            Func FindObjectByName( CATBSTR  iObjName) As AnyObject

            | Finds an object that is not a collection by its name. Scan in depth among all the direct and indirect
            | children (expensive, but hard to escape).
            | Parameters:
            |   iObjName
            |       The name to be searched
            | Returns:
            |   The object, if found
            | Example:
            |   The following example tests if the object was found:
            |       Set partRoot = partDoc.Part
            |       Set obj = partRoot.FindObjectByName("Wrong name")
            |       If TypeName(obj)="Nothing" Then
            |           MsgBox "Object not found"
            |       End If

        :param str name:
        :return:
        """

        return self.part.FindObjectByName(name)

    def deactivate(self, item):
        """
        .. note::
            CAA V5 Visual Basic help

            Sub Inactivate( AnyObject  iObject)

            | Suppresses an object from being updated. A suppressed object is not taken into account for the
            | calculation of the part.
            | Parameters:
            |   iObject
            |       The object to suppress from being updated
            | Example:
            |   The following example suppresses the pad1 pad from being updated:
            |       Set partRoot = partDoc.Part
            |       Set pad1 = partRoot.FindObjectByName("Pad.1")
            |       partRoot.Inactivate(pad1)

        :return:
        """

        self.part.Inactivate(item)

    def is_inactive(self, item):
        """
        .. note::
            CAA V5 Visual Basic help

            Func IsInactive( AnyObject  iObject) As boolean

            | Indicates whether an object is deactivated. A deactivated object is not taken into account for the
            | calculation of the part.
            | Parameters:
            |   iObject
            |       The object to examine
            | Example:
            |   The following example returns in isInactive whether the pad1 pad is deactivated:
            |       Set partRoot = partDoc.Part
            |       Set pad1 = partRoot.FindObjectByName("Pad.1")
            |       isInactive = partRoot.IsInactive(pad1)


        :param item:
        :return: bool
        """

        return self.part.IsInactive(item)

    def is_upated(self, catia_object):
        """
        :Example:

            >>> from pycatia import CATIADocHandler
            >>> cat_part = r'my_part.CATPart'
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
        :return: bool
        """

        return self.part.IsUpToDate(catia_object)

    def update(self):
        """
        Update the document.

        .. note::
            CAA V5 Visual Basic help

            Sub Update( )
            Updates of the part result with respect to its specifications. Any composing specification that hasn't its
            result up-to-date will recompute it, thus propagating changes to the whole part.

            | Example:
            | The following example update the part:
            | Set partRoot = partDoc.Part
            |   partRoot.Update

        """

        self.part.Update()

    def __repr__(self):
        """
        :return: str
        """
        return f'Part(name: {self.name})'
