#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.

"""

from pathlib import Path

from pycatia.exception_handling.exceptions import CATIAApplicationException
from pycatia.hybrid_shape_interfaces.hybrid_shape_factory import HybridShapeFactory
from pycatia.in_interfaces.reference import Reference
from pycatia.knowledge_interfaces.parameters import Parameters
from pycatia.knowledge_interfaces.relations import Relations
from pycatia.mec_mod_interfaces.axis_systems import AxisSystems
from pycatia.mec_mod_interfaces.bodies import Bodies
from pycatia.mec_mod_interfaces.body import Body
from pycatia.mec_mod_interfaces.constraints import Constraints
from pycatia.mec_mod_interfaces.factory import Factory
from pycatia.mec_mod_interfaces.geometric_elements import GeometricElements
from pycatia.mec_mod_interfaces.hybrid_bodies import HybridBodies
from pycatia.mec_mod_interfaces.ordered_geometrical_sets import OrderedGeometricalSets
from pycatia.mec_mod_interfaces.origin_elements import OriginElements
from pycatia.part_interfaces.shape_factory import ShapeFactory
from pycatia.system_interfaces.any_object import AnyObject
from pycatia.product_structure_interfaces.analyze import Analyze
from pycatia.system_interfaces.collection import Collection
from pycatia.cat_tps_interfaces.annotation_sets import AnnotationSets


class Part(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     Part
                |
                | The root level object inside a PartDocument object.
                | Role: It aggregates all the objects making up the part
                | document.
                | It provides many factories and collections. The collections list only the
                | direct children of the part. Selection.Search allows to get all objects of one
                | type.
                |
                | See also:
                |     PartDocument

    """

    def __init__(self, com_part_object):
        super().__init__(com_part_object)
        self.part = com_part_object
        self.com_object = com_part_object

    @property
    def analyze(self) -> Analyze:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property Analyze() As Analyze (Read Only)
                |
                |     Returns the Analyze object associated to the current
                |     product.
                |
                |     Example:
                |
                |           This example retrieves in EngineAnalysis the Analyze object
                |           of
                |          the Engine product.
                |
                |
                |          Dim EngineAnalysis As Analyze
                |          Set EngineAnalysis = Engine.Analyze

        :rtype: Analyze
        """

        return Analyze(self.part.Analyze)

    @property
    def annotation_sets(self) -> AnnotationSets:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property AnnotationSets() As Collection (Read Only)
                | 
                |     Returns the collection object containing the annotation sets. All the
                |     annotation sets that are aggregated in the part might be accessed thru that
                |     collection.
                |
                |     Example:
                |         The following example returns in annotationSets the annotation sets of
                |         the partRoot part from the partDoc part document:
                |
                |          Set partRoot = partDoc.Part
                |          Dim annotationSets As AnnotationSets
                |          Set annotationSets = partRoot.AnnotationSets

        :return: Collection
        """

        return AnnotationSets(self.part.AnnotationSets)

    @property
    def axis_systems(self) -> AxisSystems:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property AxisSystems() As AxisSystems (Read Only)
                |
                |     Returns the collection object containing the coordinate systems. All the
                |     coordinate systems that are aggregated in the part might be accessed thru that
                |     collection.
                |
                |     Example:
                |         The following example returns in axisSystems the coordinate systems of
                |         the partRoot part from the partDoc part document:
                | 
                |          Set partRoot = partDoc.Part
                |          Dim axisSystems As AxisSystems
                |          Set axisSystems = partRoot.AxisSystems

        :return: AxisSystems

        This will only return axis systems under the Axis Systems node. Axis systems within a Geometrical Set will not
        be returned.
        """

        return AxisSystems(self.part.AxisSystems)

    @property
    def bodies(self) -> Bodies:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property Bodies() As Bodies (Read Only)
                | 
                |     Returns the collection object containing the bodies that are direct
                |     children of the part.
                |     It does not return all the bodies of the part, particularly the bodies in a
                |     boolean operation.
                |
                |     Example:
                |         The following example returns in bodiesColl the collection of the
                |         bodies of the partRoot part from the partDoc part
                |         document:
                |
                |          Set partRoot = partDoc.Part
                |          Set bodiesColl = partRoot.Bodies

        :rtype: Bodies
        """

        return Bodies(self.part.Bodies)

    @property
    def constraints(self) -> Constraints:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property Constraints() As Constraints (Read Only)
                | 
                |     Returns the collection object containing the part constraints. Only 3D
                |     constraints are concerned here, 2D constraints are managed in
                |     sketches.
                |
                |     Example:
                |         The following example returns in csts the constraints of the partRoot
                |         part from the partDoc part document:
                |
                |          Set partRoot = partDoc.Part
                |          Set csts = partRoot.Constraints

        :rtype: Constraints
        """

        return Constraints(self.part.Constraints)

    @property
    def density(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property Density() As double (Read Only)
                |
                |     Returns the part density.
                | 
                |     Example:
                |         The following example displays the density of the
                |         part:
                |
                |          Set partRoot = partDoc.Part
                |          MsgBox "The density is " & partRoot.Density

        :rtype: float
        """

        return self.part.Density

    @property
    def file_name(self) -> str:
        """
        :rtype: str
        """
        try:
            return self.part.ReferenceProduct.Parent.Name
        except AttributeError:
            return self.part.Name

    @property
    def full_name(self) -> str:
        """
        :rtype: str
        """
        try:
            return self.part.ReferenceProduct.Parent.FullName
        except AttributeError:
            return self.part.FullName

    @property
    def geometric_elements(self) -> GeometricElements:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property GeometricElements() As GeometricElements (Read
                | Only)
                |
                |     Returns the collection object containing the part geometrical elements.
                |     Only 3D elements are concerned here, 2D elements are managed in sketches. The
                |     origin elements are also accessible thru that collection.
                |
                |     Example:
                |         The following example returns in geomElts the 3D elements of the
                |         partRoot part from the partDoc part document:
                | 
                |          Set partRoot = partDoc.Part
                |          Set geomElts = partRoot.GeometricElements

        :rtype: GeometricElements
        """

        return GeometricElements(self.part.GeometricElements)

    @property
    def hybrid_bodies(self) -> HybridBodies:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property HybridBodies() As HybridBodies (Read Only)
                |
                |     Returns the collection object containing the hybrid bodies that are direct
                |     children of the part.
                |
                |     Example:
                |         The following example returns in hybridBodiesColl the collection of
                |         hybrid bodies of the partRoot part from the partDoc part
                |         document:
                | 
                |          Set partRoot = partDoc.Part
                |          Set hybridBodiesColl = partRoot.HybridBodies

        :rtype: HybridBodies
        """

        return HybridBodies(self.part.HybridBodies)

    @property
    def hybrid_shape_factory(self) -> HybridShapeFactory:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property HybridShapeFactory() As Factory (Read Only)
                | 
                |     Returns the part hybrid shape factory. It allows the creation of hybrid
                |     shapes in the part.
                |
                |     Example:
                |         The following example returns in hybridShapeFact the hybrid shape
                |         factory of the partRoot part from the partDoc part
                |         document:
                |
                |          Set partRoot = partDoc.Part
                |          Dim hybridShapeFact As Factory
                |          Set hybridShapeFact = partRoot.HybridShapeFactory

        :rtype: HybridShapeFactory
        """

        return HybridShapeFactory(self.part.HybridShapeFactory)

    @property
    def in_work_object(self) -> AnyObject:
        """
        .. note::
            :class: toggle

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

        :rtype: AnyObject
        """

        return AnyObject(self.part.InWorkObject)

    @in_work_object.setter
    def in_work_object(self, any_object: AnyObject):
        """
        :param AnyObject any_object:
        """

        self.part.InWorkObject = any_object.com_object

    @property
    def main_body(self) -> Body:
        """
        .. note::
            :class: toggle

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

        :rtype: Body
        """

        return Body(self.part.MainBody)

    @main_body.setter
    def main_body(self, body: Body):
        """
        :param Body body:
        """

        self.part.MainBody = body.com_object

    @property
    def ordered_geometrical_sets(self) -> OrderedGeometricalSets:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property OrderedGeometricalSets() As OrderedGeometricalSets (Read
                | Only)
                |
                |     Returns the collection object containing the ordered geometrical sets of
                |     the part.
                |
                |     Example:
                |         The following example returns in ogsColl the collection of ordered
                |         geometrical sets of the partRoot part from the partDoc part
                |         document:
                |
                |          Set partRoot = partDoc.Part
                |          Set ogsColl = partRoot.OrderedGeometricalSets

        :rtype: OrderedGeometricalSets
        """

        return OrderedGeometricalSets(self.part.OrderedGeometricalSets)

    @property
    def origin_elements(self) -> OriginElements:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property OriginElements() As OriginElements (Read Only)
                | 
                |     Returns the object defining the part 3D reference axis
                |     system.
                |
                |     Example:
                |         The following example returns in originElts the origin of the partRoot
                |         part from the partDoc part document:
                |
                |          Set partRoot = partDoc.Part
                |          Set originElts = partRoot.OriginElements

        :rtype: OriginElements
        """

        return OriginElements(self.part.OriginElements)

    @property
    def parameters(self) -> Parameters:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property Parameters() As Parameters (Read Only)
                |
                |     Returns the collection object containing the part parameters. All the
                |     parameters that are aggregated in the different objects of the part might be
                |     accessed thru that collection.
                |
                |     Example:
                |         The following example returns in params the parameters of the partRoot
                |         part from the partDoc part document:
                |
                |          Set partRoot = partDoc.Part
                |          Dim params As Parameters
                |          Set params = partRoot.Parameters

        :rtype: Parameters
        """

        return Parameters(self.part.Parameters)

    @property
    def relations(self) -> Relations:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property Relations() As Relations (Read Only)
                |
                |     Returns the collection object containing the part relations. All the
                |     relations that are used to valuate the parameters of the part might be accessed
                |     thru that collection.
                |
                |     Example:
                |         The following example returns in rels the relations of the partRoot
                |         part from the partDoc part document:
                |
                |          Set partRoot = partDoc.Part
                |          Set rels = partRoot.Relations

        :rtype: Relations
        """

        return Relations(self.part.Relations)

    @property
    def shape_factory(self) -> ShapeFactory:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property ShapeFactory() As Factory (Read Only)
                |
                |     Returns the part shape factory. It allows the creation of shapes in the
                |     part.
                |
                |     Example:
                |         The following example returns in shapeFact the shape factory of the
                |         partRoot part from the partDoc part document:
                |
                |          Set partRoot = partDoc.Part
                |          Dim shapeFact As Factory
                |          Set shapeFact = partRoot.ShapeFactory

        :rtype: ShapeFactory
        """

        return ShapeFactory(self.part.ShapeFactory)

    @property
    def sheet_metal_factory(self) -> Factory:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property SheetMetalFactory() As Factory (Read Only)
                |
                |     Returns the sheet metal factory of the part. It allows the creation of
                |     sheet metal elements in the part.
                |
                |     Example:
                |         The following example returns in sheetMetalFact the sheet metal factory
                |         of the partRoot part from the partDoc part document:
                |
                |          Set partRoot = partDoc.Part
                |          Dim sheetMetalFact As Factory
                |          Set sheetMetalFact = partRoot.SheetMetalFactory

        :return: Factory
        :return: Factory
        """

        return Factory(self.part.SheetMetalFactory)

    @property
    def sheet_metal_parameters(self) -> AnyObject:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property SheetMetalParameters() As AnyObject (Read Only)
                |
                |     Returns the sheet metal parameters of the part.
                |
                |     Example:
                |         The following example returns in sheetMetalParm the sheet metal
                |         parameters of the partRoot part from the partDoc part
                |         document:
                |
                |          Set partRoot = partDoc.Part
                |          Dim sheetMetalParm As SheetMetalParameters
                |          Set sheetMetalFact = partRoot.SheetMetalParameters

        :rtype: AnyObject
        """

        return AnyObject(self.part.SheetMetalParameters)

    @property
    def user_surfaces(self) -> Collection:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property UserSurfaces() As Collection (Read Only)
                |
                |     Returns the collection object containing the user surfaces. All the user
                |     surfaces that are aggregated in the part might be accessed thru that
                |     collection.
                |
                |     Example:
                |         The following example returns in userSurfaces the user surfaces of the
                |         partRoot part from the partDoc part document:
                |
                |          Set partRoot = partDoc.Part
                |          Dim userSurfaces As UserSurfaces
                |          Set userSurfaces = partRoot.UserSurfaces

        :rtype: Collection
        """

        return Collection(self.part.UserSurfaces)

    def activate(self, i_object: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub Activate(AnyObject iObject)
                |
                |     Unsuppresses an object for the update process. A unsuppressed object is
                |     again taken into account for the calculation of the part.
                |
                |     Parameters:
                |
                |         iObject
                |             The object to unsuppress for the update process
                |
                |     Example:
                |         The following example unsuppresses the pad1 pad:
                |
                |          Set partRoot = partDoc.Part
                |          Set pad1 = partRoot.FindObjectByName("Pad.1")
                |          partRoot.Activate(pad1)

        :param AnyObject i_object:
        :rtype: None
        """
        return self.part.Activate(i_object.com_object)

    def create_reference_from_b_rep_name(self, i_label: str, i_object_context: AnyObject):
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func CreateReferenceFromBRepName(CATBSTR iLabel,
                | AnyObject iObjectContext) As Reference
                |
                |     Creates a reference from a GenericNaming label. This allows manipulation of
                |     B-Rep (Type Functinal and Relimited) that are not easy to
                |     access.
                |
                |     Parameters:
                |
                |         iLabel
                |             The GenericNaming identification for an object. This is a cryptic
                |             form for "the edge surrounded by the face extruded from line.12 of sketch.4 and
                |             the face...")
                |         iObjectContext
                |             The Object Context of Resolution This is the feature used for label
                |             GenericNaming resolution
                |
                |     Returns:
                |         The reference to a B-Rep sub-element such a face or an edge

        :param str i_label:
        :param AnyObject i_object_context:
        :rtype: Reference
        """
        return Reference(self.part.CreateReferenceFromBRepName(i_label, i_object_context.com_object))

    def create_reference_from_geometry(self, i_object: AnyObject) -> Reference:
        """
        .. note::
            :class: toggle

            Microsoft Visual Basic Object Browser
                | Function CreateReferenceFromGeometry(iObject As AnyObject) As Reference
                |     Member of MECMOD.Part

        :param AnyObject i_object:
        :rtype: Reference
        """

        return Reference(self.part.CreateReferenceFromGeometry(i_object.com_object))

    def create_reference_from_name(self, i_label: str):
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func CreateReferenceFromName(CATBSTR iLabel) As Reference
                |
                |     Creates a reference from a GenericNaming label. This allows manipulation of
                |     B-Rep (type Functional Only) that are not easy to access.
                |
                |     Parameters:
                |
                |         iLabel
                |             The GenericNaming identification for an object. This is a cryptic
                |             form for "the edge surrounded by the face extruded from line.12 of sketch.4 and
                |             the face...")
                |
                |     Returns:
                |         The reference to a B-Rep sub-element such a face or an edge

        :param str i_label:
        :rtype: Reference
        """
        return Reference(self.part.CreateReferenceFromName(i_label))

    def create_reference_from_object(self, i_object: AnyObject):
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func CreateReferenceFromObject(AnyObject iObject) As
                | Reference
                |
                |     Creates a reference from a operator. Use of reference allows a uniform
                |     handling of B-Rep and non B-Rep objects.
                |
                |     Parameters:
                |
                |         iObject
                |             The geometric object to be referenced. It can be a plane, a line or
                |             a point.
                |
                |     Returns:
                |         The reference to the object. This way, a direction can be either an
                |         edge of a pad or a 3D line.

        :param AnyObject i_object:
        :rtype: Reference
        """
        return Reference(self.part.CreateReferenceFromObject(i_object.com_object))

    def deactivate(self, i_object: AnyObject) -> None:
        """
        See inactivate
        :param i_object:
        :rtype: None
        """
        return self.part.Inactivate(i_object.com_object)

    def find_object_by_name(self, i_obj_name: str) -> AnyObject:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func FindObjectByName(CATBSTR iObjName) As AnyObject
                |
                |     Finds an object that is not a collection by its name. Scan in depth among
                |     all the direct and indirect children (expensive, but hard to
                |     escape).
                |
                |     Parameters:
                |
                |         iObjName
                |             The name to be searched
                |
                |     Returns:
                |         The object, if found
                |     Example:
                |         The following example tests if the object was found:
                |
                |          Set partRoot = partDoc.Part
                |          Set obj = partRoot.FindObjectByName("Wrong name")
                |          If TypeName(obj)="Nothing" Then
                |               MsgBox "Object not found"
                |          End If

        :param str i_obj_name:
        :rtype: AnyObject
        """

        if self.part.FindObjectByName(i_obj_name):
            return AnyObject(self.part.FindObjectByName(i_obj_name))
        else:
            raise CATIAApplicationException('Could not find object.')

    def get_customer_factory(self, i_factory_iid: str) -> Factory:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func GetCustomerFactory(CATBSTR iFactoryIID) As Factory
                |
                |     Returns a customer factory from a code string defined by the customer. It
                |     allows a customer to define its own factory to create its own
                |     objects.
                |
                |     Parameters:
                |
                |         iFactoryIID
                |             The code name of the factory

        :param str i_factory_iid:
        :rtype: Factory
        """
        return Factory(self.part.GetCustomerFactory(i_factory_iid))

    def inactivate(self, i_object: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub Inactivate(AnyObject iObject)
                |
                |     Suppresses an object from being updated. A suppressed object is not taken
                |     into account for the calculation of the part.
                |
                |     Parameters:
                |
                |         iObject
                |             The object to suppress from being updated
                |
                |     Example:
                |         The following example suppresses the pad1 pad from being
                |         updated:
                |
                |          Set partRoot = partDoc.Part
                |          Set pad1 = partRoot.FindObjectByName("Pad.1")
                |          partRoot.Inactivate(pad1)

        :param AnyObject i_object:
        :rtype: None
        """
        return self.part.Inactivate(i_object.com_object)

    def is_inactive(self, i_object: AnyObject) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func IsInactive(AnyObject iObject) As boolean
                |
                |     Indicates whether an object is deactivated. A deactivated object is not
                |     taken into account for the calculation of the part.
                |
                |     Parameters:
                |
                |         iObject
                |             The object to examine
                |
                |     Example:
                |         The following example returns in isInactive whether the pad1 pad is
                |         deactivated:
                |
                |          Set partRoot = partDoc.Part
                |          Set pad1 = partRoot.FindObjectByName("Pad.1")
                |          isInactive = partRoot.IsInactive(pad1)

        :param AnyObject i_object:
        :rtype: bool
        """
        return self.part.IsInactive(i_object.com_object)

    def is_up_to_date(self, i_object: AnyObject) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func IsUpToDate(AnyObject iObject) As boolean
                |
                |     Indicates whether an object needs to be updated. An object which is not
                |     up-to-date has not be calculated with the last
                |     specifications.
                |
                |     Parameters:
                |
                |         iObject
                |             The object to examine
                |
                |     Example:
                |         The following example returns in isuptodate whether the pad1 pad is
                |         up-to-date:
                |
                |          Set partRoot = partDoc.Part
                |          Set pad1 = partRoot.FindObjectByName("Pad.1")
                |          isuptodate = partRoot.IsUpToDate(pad1)

        :param AnyObject i_object:
        :rtype: bool
        """
        return self.part.IsUpToDate(i_object.com_object)

    def path(self) -> Path:
        """

        Returns the pathlib.Path() object of the document fullname.
        example e://users//psr//Parts//MyNicePart.CATPart
        >>> Part.path().name
        MyNicePart.CATPart
        >>> Part.path().parent
        e://users//psr//Parts//
        >>> Part.path().suffix
        .CATPart

        :rtype: Path()
        """
        return Path(self.full_name)

    def update(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub Update()
                | 
                |     Updates of the part result with respect to its specifications. Any
                |     composing specification that hasn't its result up-to-date will recompute it,
                |     thus propagating changes to the whole part.
                |
                |     Example:
                |         The following example update the part:
                |
                |          Set partRoot = partDoc.Part
                |          partRoot.Update

        :rtype: None
        """
        return self.part.Update()

    def update_object(self, i_object: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub UpdateObject(AnyObject iObject)
                | 
                |     Updates an object with respect to its specifications. Any composing
                |     specification of the object that hasn't its result up-to-date will recompute
                |     it, thus propagating changes to the object.
                |
                |     Parameters:
                |
                |         iObject
                |             The object to be updated
                |
                |     Example:
                |         The following example updates Pad.1:
                |
                |          Set partRoot = partDoc.Part
                |          Set pad1 = partRoot.FindObjectByName("Pad.1")
                |          partRoot.UpdateObject(pad1)

        :param AnyObject i_object:
        :rtype: None
        """
        return self.part.UpdateObject(i_object.com_object)

    def __repr__(self):
        return f'Part(name="{self.name}")'
