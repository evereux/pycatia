#! /usr/bin/python3.6
# module initially auto generated using V5Automation.chm from CATIA V5 R25

from pathlib import Path

from pycatia.hybrid_shape_interfaces.hybrid_shape_factory import HybridShapeFactory
from pycatia.in_interfaces.reference import Reference
from pycatia.knowledge_interfaces.parameters import Parameters
from pycatia.knowledge_interfaces.relations import Relations
from pycatia.part_interfaces.shape_factory import ShapeFactory
from pycatia.system_interfaces.any_object import AnyObject
from pycatia.system_interfaces.collection import Collection
from .axis_systems import AxisSystems
from .bodies import Bodies
from .body import Body
from .constraints import Constraints
from .factory import Factory
from .geometric_elements import GeometricElements
from .hybrid_bodies import HybridBodies
from .ordered_geometrical_sets import OrderedGeometricalSets
from .origin_ements import OriginElements


class Part(AnyObject):
    """
        .. note::
            CAA V5 Visual Basic help

                | The root level object inside a PartDocument object.Role: It aggregates
                | all the objects making up the part document.It provides many factories
                | and collections. The collections list only the direct children of the
                | part.activateLinkAnchor('Selection','Search','Selection.Search')allows
                | to get all objects of one type.

    """

    def __init__(self, com_part_object):
        super().__init__(com_part_object)
        self.part = com_part_object
        self.com_object = com_part_object

    @property
    def annotation_sets(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | AnnotationSets
                | o Property AnnotationSets() As Collection
                | 
                | Returns the collection object containing the annotation sets. All the
                | annotation sets that are aggregated in the part  might be accessed
                | thru that collection.  Example:The following example returns in
                | annotationSets the annotation sets of the partRoot part from the
                | partDoc part document:  Set partRoot = partDoc.Part Dim annotationSets
                | As AnnotationSets Set annotationSets = partRoot.AnnotationSets

        :return: Collection()
        """
        return Collection(self.part.AnnotationSets)

    @property
    def axis_systems(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | AxisSystems
                | o Property AxisSystems() As AxisSystems
                | 
                | Returns the collection object containing the coordinate systems. All
                | the coordinate systems that are aggregated in the part  might be
                | accessed thru that collection.  Example:The following example returns
                | in axisSystems the coordinate systems of the partRoot part from the
                | partDoc part document:  Set partRoot = partDoc.Part Dim axisSystems As
                | AxisSystems Set axisSystems = partRoot.AxisSystems

        :return: AxisSystems()
        """
        return AxisSystems(self.part.AxisSystems)

    @property
    def bodies(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Bodies
                | o Property Bodies() As Bodies
                | 
                | Returns the collection object containing the bodies that are direct
                | children of the part. It does not return all the bodies of the part,
                | particularly the bodies in a boolean operation.  Example:The following
                | example returns in bodiesColl the collection of the bodies of the
                | partRoot part from the partDoc part document:  Set partRoot =
                | partDoc.Part Set bodiesColl = partRoot.Bodies

        :return: Bodies()
        """
        return Bodies(self.part.Bodies)

    @property
    def constraints(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Constraints
                | o Property Constraints() As Constraints
                | 
                | Returns the collection object containing the part constraints. Only 3D
                | constraints are concerned here, 2D constraints are managed in
                | sketches.  Example:The following example returns in csts the
                | constraints of the partRoot part from the partDoc part document:  Set
                | partRoot = partDoc.Part Set csts = partRoot.Constraints

        :return: Constraints()
        """
        return Constraints(self.part.Constraints)

    @property
    def density(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Density
                | o Property Density() As double
                | 
                | Returns the part density.  Example:The following example displays the
                | density of the part:  Set partRoot = partDoc.Part MsgBox "The density
                | is " & partRoot.Density

        :return: float
        """
        return self.part.Density

    @property
    def file_name(self):
        """
        :return: str()
        """
        try:
            return self.part.ReferenceProduct.Parent.Name
        except AttributeError:
            return self.parent.Name

    @property
    def full_name(self):
        """
        :return: str()
        """
        try:
            return self.part.ReferenceProduct.Parent.FullName
        except AttributeError:
            return self.parent.FullName

    @property
    def geometric_elements(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | GeometricElements
                | o Property GeometricElements() As GeometricElements
                | 
                | Returns the collection object containing the part geometrical
                | elements. Only 3D elements are concerned here, 2D elements are managed
                | in sketches. The origin elements are also accessible thru that
                | collection.  Example:The following example returns in geomElts the 3D
                | elements of the partRoot part from the partDoc part document:  Set
                | partRoot = partDoc.Part Set geomElts = partRoot.GeometricElements

        :return: GeometricElements()
        """
        return GeometricElements(self.part.GeometricElements)

    @property
    def hybrid_bodies(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | HybridBodies
                | o Property HybridBodies() As HybridBodies
                | 
                | Returns the collection object containing the hybrid bodies that are
                | direct children of the part.  Example:The following example returns in
                | hybridBodiesColl the collection of hybrid bodies of the partRoot part
                | from the partDoc part document:  Set partRoot = partDoc.Part Set
                | hybridBodiesColl = partRoot.HybridBodies

        :return: HybridBodies()
        """
        return HybridBodies(self.part.HybridBodies)

    @property
    def hybrid_shape_factory(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | HybridShapeFactory
                | o Property HybridShapeFactory() As Factory
                | 
                | Returns the part hybrid shape factory. It allows the creation of
                | hybrid shapes in the part.
                |
                | Example:The following example returns in
                | hybridShapeFact the hybrid shape factory of the partRoot part from the
                | partDoc part document:
                | Set partRoot = partDoc.Part
                | Dim hybridShapeFact As Factory
                | Set hybridShapeFact = partRoot.HybridShapeFactory

        :return: HybridShapeFactory()
        """
        return HybridShapeFactory(self.part.HybridShapeFactory)

    @property
    def in_work_object(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property InWorkObject() As AnyObject
                |
                |     Returns or sets the in work object of the part. The in work object is the
                |     object after which a new object is added.
                |
                |     Example:
                |
                |      Set partRoot = partDoc.Part
                |      Set partRoot.InWorkObject = cylindricPad
                |      If ( partRoot.InWorkObject <> cylindricPad ) Then
                |           MsgBox "There is a big problem"
                |      End If

        :return: AnyObject
        """

        return AnyObject(self.part.InWorkObject)

    @in_work_object.setter
    def in_work_object(self, value):
        """
        :param AnyObject value:
        """

        self.part.InWorkObject = value.com_object

    @property
    def main_body(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property MainBody() As Body
                |
                |     Returns or sets the main body of the part.
                |
                |     Example:
                |         The following example returns the main body of the part of the current
                |         document.
                |
                |          Dim mainBody As Body
                |          Set mainBody=CATIA.ActiveDocument.Part.MainBody

        :return: Body
        """

        return Body(self.part.MainBody)

    @property
    def ordered_geometrical_sets(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | OrderedGeometricalSets
                | o Property OrderedGeometricalSets() As OrderedGeometricalSets
                | 
                | Returns the collection object containing the ordered geometrical sets
                | of the part.  Example:The following example returns in ogsColl the
                | collection of ordered geometrical sets of the partRoot part from the
                | partDoc part document:  Set partRoot = partDoc.Part Set ogsColl =
                | partRoot.OrderedGeometricalSets
        """
        return OrderedGeometricalSets(self.part.OrderedGeometricalSets)

    @property
    def origin_elements(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | OriginElements
                | o Property OriginElements() As OriginElements
                | 
                | Returns the object defining the part 3D reference axis system.
                |
                | Example:
                | The following example returns in originElts the origin of the
                | partRoot part from the partDoc part document:
                | Set partRoot = partDoc.Part
                | Set originElts = partRoot.OriginElements

        :return: OriginElements()
        """
        return OriginElements(self.part.OriginElements)

    @property
    def parameters(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Parameters
                | o Property Parameters() As Parameters
                |
                | Returns the collection object containing the part parameters. All the
                | parameters that are aggregated in the different objects of the part
                | might be accessed thru that collection.  Example:The following example
                | returns in params the parameters of the partRoot part from the partDoc
                | part document:  Set partRoot = partDoc.Part Dim params As Parameters
                | Set params = partRoot.Parameters

        :return: Parameters()
        """
        return Parameters(self.part.Parameters)

    @property
    def relations(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Relations
                | o Property Relations() As Relations
                |
                | Returns the collection object containing the part relations. All the
                | relations that are used to valuate  the parameters of the part might
                | be accessed thru that collection.  Example:The following example
                | returns in rels the relations of the partRoot part from the partDoc
                | part document:  Set partRoot = partDoc.Part Set rels =
                | partRoot.Relations

        :return: Relations()
        """
        return Relations(self.part.Relations)

    @property
    def shape_factory(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | ShapeFactory
                | o Property ShapeFactory() As Factory
                |
                | Returns the part shape factory. It allows the creation of shapes in
                | the part.  Example:The following example returns in shapeFact the
                | shape factory of the partRoot part from the partDoc part document:
                | Set partRoot = partDoc.Part Dim shapeFact As Factory   Set shapeFact =
                | partRoot.ShapeFactory

        :return: Factory()
        """
        return ShapeFactory(self.part.ShapeFactory)

    @property
    def sheet_metal_factory(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | SheetMetalFactory
                | o Property SheetMetalFactory() As Factory
                |
                | Returns the sheet metal factory of the part. It allows the creation of
                | sheet metal elements in the part.  Example:The following example
                | returns in sheetMetalFact the sheet metal factory of the partRoot part
                | from the partDoc part document:  Set partRoot = partDoc.Part Dim
                | sheetMetalFact As Factory Set sheetMetalFact =
                | partRoot.SheetMetalFactory

        """
        return Factory(self.part.SheetMetalFactory)

    @property
    def sheet_metal_parameters(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | SheetMetalParameters
                | o Property SheetMetalParameters() As AnyObject
                |
                | Returns the sheet metal parameters of the part.  Example:The following
                | example returns in sheetMetalParm the sheet metal parameters of the
                | partRoot part from the partDoc part document:  Set partRoot =
                | partDoc.Part Dim sheetMetalParm As SheetMetalParameters Set
                | sheetMetalFact = partRoot.SheetMetalParameters
        """
        return self.part.SheetMetalParameters

    @property
    def user_surfaces(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | UserSurfaces
                | o Property UserSurfaces() As Collection
                |
                | Returns the collection object containing the user surfaces. All the
                | user surfaces that are aggregated in the part  might be accessed thru
                | that collection.  Example:The following example returns in
                | userSurfaces the user surfaces of the partRoot part from the partDoc
                | part document:  Set partRoot = partDoc.Part Dim userSurfaces As
                | UserSurfaces Set userSurfaces = partRoot.UserSurfaces

        """
        return self.part.UserSurfaces

    def activate(self, i_object):
        """
        .. note::
            CAA V5 Visual Basic help

                | Activate
                | o Sub Activate(    AnyObject    iObject)
                |
                | Unsuppresses an object for the update process. A unsuppressed object
                | is again taken into account  for the calculation of the part.
                |
                | Parameters:
                | iObject
                |     The object to unsuppress for the update process
                | Examples:
                | The following example unsuppresses the pad1 pad:
                | Set partRoot = partDoc.Part
                | Set pad1 = partRoot.FindObjectByName("Pad.1")
                | partRoot.Activate(pad1)

        """
        self.part.Activate(i_object.com_object)

    def create_reference_from_b_rep_name(self, i_label, i_object_context):
        """
        .. note::
            CAA V5 Visual Basic help

                | CreateReferenceFromBRepName
                | o Func CreateReferenceFromBRepName(    CATBSTR    iLabel,
                |                                        AnyObject    iObjectContext) As Reference
                |
                | Creates a reference from a GenericNaming label. This allows
                | manipulation of B-Rep (Type Functinal and Relimited) that are not easy
                | to access.
                |
                | Parameters:
                | iLabel
                |    The GenericNaming identification for an object.
                |    This is a cryptic form for "the edge surrounded by the face extruded
                |    from line.12 of sketch.4 and the face...")
                |
                |  iObjectContext
                |    The Object Context of Resolution
                |    This is the feature used for label GenericNaming resolution
                |  Returns:
                |   The reference to a B-Rep sub-element such a face or an edge

        :param str i_label:
        :param AnyObject() i_object_context:
        :return: Reference()
        """
        return Reference(self.part.CreateReferenceFromBRepName(i_label, i_object_context.com_object))

    def create_reference_from_name(self, i_label):
        """
        .. note::
            CAA V5 Visual Basic help

                | CreateReferenceFromName
                | o Func CreateReferenceFromName(    CATBSTR    iLabel) As Reference
                |
                | Creates a reference from a GenericNaming label. This allows
                | manipulation of B-Rep (type Functional Only) that are not easy to
                | access.
                |
                | Parameters:
                | iLabel
                |    The GenericNaming identification for an object.
                |    This is a cryptic form for "the edge surrounded by the face extruded
                |    from line.12 of sketch.4 and the face...")
                |  Returns:
                |   The reference to a B-Rep sub-element such a face or an edge

        :param str i_label:
        :return: Reference()
        """
        return Reference(self.part.CreateReferenceFromName(i_label))

    def create_reference_from_object(self, i_object):
        """
        .. note::
            CAA V5 Visual Basic help

                | CreateReferenceFromObject
                | o Func CreateReferenceFromObject(    AnyObject    iObject) As Reference
                |
                | Creates a reference from a operator. Use of reference allows a uniform
                | handling of B-Rep and non B-Rep objects.
                |
                | Parameters:
                | iObject
                |    The geometric object to be referenced.
                |    It can be a plane, a line or a point.
                |
                |  Returns:
                |   The reference to the object. This way, a direction can be either an edge of a pad or a 3D line.

        :param AnyObject() i_object:
        :return: Reference()
        """
        return Reference(self.part.CreateReferenceFromObject(i_object.com_object))

    def deactivate(self, i_object):
        self.inactivate(i_object)

    def find_object_by_name(self, i_obj_name):
        """
        .. note::
            CAA V5 Visual Basic help

                | FindObjectByName
                | o Func FindObjectByName(    CATBSTR    iObjName) As AnyObject
                |
                | Finds an object that is not a collection by its name. Scan in depth
                | among all the direct and indirect children (expensive, but hard to
                | escape).
                |
                | Parameters:
                | iObjName
                |    The name to be searched
                |
                | Returns:
                |   The object, if found
                |
                | Examples:
                | The following example tests if the object was found:
                | Set partRoot = partDoc.Part
                | Set obj = partRoot.FindObjectByName("Wrong name")
                | If TypeName(obj)="Nothing" Then
                | MsgBox "Object not found"
                | End If

        :param str i_obj_name:
        :return: AnyObject()
        """
        if self.part.FindObjectByName(i_obj_name):
            return AnyObject(self.part.FindObjectByName(i_obj_name))

        return None

    def get_customer_factory(self, i_factory_iid):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetCustomerFactory
                | o Func GetCustomerFactory(    CATBSTR    iFactoryIID) As Factory
                |
                | Returns a customer factory from a code string defined by the customer.
                | It allows a customer to define its own factory to create its own
                | objects.


                | Parameters:
                | iFactoryIID
                | 	The code name of the factory

        :param str i_factory_iid:
        :return: Factory()
        """
        return Factory(self.part.GetCustomerFactory(i_factory_iid))

    def inactivate(self, i_object):
        """
        .. note::
            CAA V5 Visual Basic help

                | Inactivate
                | o Sub Inactivate(    AnyObject    iObject)
                |
                | Suppresses an object from being updated. A suppressed object is not
                | taken into account  for the calculation of the part.
                |
                | Parameters:
                | iObject
                |    The object to suppress from being updated
                |
                | Examples:
                | The following example suppresses the pad1 pad
                | from being updated:
                | Set partRoot = partDoc.Part
                | Set pad1 = partRoot.FindObjectByName("Pad.1")
                | partRoot.Inactivate(pad1)

        :param AnyObject() i_object:
        """
        self.part.Inactivate(i_object.com_object)

    def is_inactive(self, i_object):
        """
        .. note::
            CAA V5 Visual Basic help

                | IsInactive
                | o Func IsInactive(    AnyObject    iObject) As boolean
                |
                | Indicates whether an object is deactivated. A deactivated object is
                | not taken into account for the calculation of the part.


                | Parameters:
                | iObject
                |    The object to examine
                |
                | Examples:
                | The following example returns in isInactive
                | whether the pad1 pad is deactivated:
                | Set partRoot = partDoc.Part
                | Set pad1 = partRoot.FindObjectByName("Pad.1")
                | isInactive = partRoot.IsInactive(pad1)

        :param AnyObject() i_object:
        :return: bool
        """
        return self.part.IsInactive(i_object.com_object)

    def is_up_to_date(self, i_object):
        """
        .. note::
            CAA V5 Visual Basic help

                | IsUpToDate
                | o Func IsUpToDate(    AnyObject    iObject) As boolean
                |
                | Indicates whether an object needs to be updated. An object which is
                | not up-to-date has not be calculated  with the last specifications.
                |
                | Parameters:
                | iObject
                |    The object to examine
                |
                | Examples:
                | The following example returns in isuptodate whether
                | the pad1 pad is up-to-date:
                | Set partRoot = partDoc.Part
                | Set pad1 = partRoot.FindObjectByName("Pad.1")
                | isuptodate = partRoot.IsUpToDate(pad1)

        :param AnyObject() i_object:
        :return: bool
        """
        return self.part.IsUpToDate(i_object.com_object)

    def path(self):
        """

        Returns the pathlib.Path() object of the document fullname.
        example e://users//psr//Parts//MyNicePart.CATPart
        >>> Part.path().name
        MyNicePart.CATPart
        >>> Part.path().parent
        e://users//psr//Parts//
        >>> Part.path().suffix
        .CATPart

        :return: Path()
        """
        return Path(self.full_name)

    def update(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Update
                | o Sub Update()
                | 
                | Updates of the part result with respect to its specifications. Any
                | composing specification that hasn't its result up-to-date will
                | recompute it, thus propagating changes to the whole part.  Example:The
                | following example update the part:  Set partRoot = partDoc.Part
                | partRoot.Update

        """
        self.part.Update()

    def update_object(self, i_object):
        """
        .. note::
            CAA V5 Visual Basic help

                | UpdateObject
                | o Sub UpdateObject(    AnyObject    iObject)
                | 
                | Updates an object with respect to its specifications. Any composing
                | specification of the object that hasn't  its result up-to-date will
                | recompute it, thus propagating changes to the object.
                |
                | Parameters:
                | iObject
                |    The object to be updated
                |
                | Examples:
                | The following example updates Pad.1:
                | Set partRoot = partDoc.Part
                | Set pad1 = partRoot.FindObjectByName("Pad.1")
                | partRoot.UpdateObject(pad1)

        :param AnyObject() i_object:
        """
        return self.part.UpdateObject(i_object.com_object)

    def __repr__(self):
        return f'Part(name="{self.name}")'
