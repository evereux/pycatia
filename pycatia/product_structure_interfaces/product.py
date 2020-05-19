#! /usr/bin/python3.6

from pathlib import Path

from pycatia.system_interfaces.base_object import AnyObject
from pycatia.product_structure_interfaces.analyze import Analyze
from pycatia.base_interfaces.move import Move
from pycatia.in_interfaces.position import Position
from .enumeration_types import cat_file_types
from .enumeration_types import cat_work_mode_types
from .enumeration_types import cat_rep_types


class Product(AnyObject):

    def __init__(self, com_object):
        """

        .. note::
            CAA V5 Visual Basic help

            Represents the product.

            The product is the object that helps you model your real products by building a
            tree structure whose nodes are product objects. Each of them may contain other
            product objects gathered in a product collection. The terminal product objects in
            the tree structure have no aggregated product collection. Even if all products are
            located somewhere in the product tree structure, some of them can be used as reference
            products to create other products named components, which are instances of the
            reference product. For example, the left front wheel in a car can be used as reference
            to create the other wheels. Be careful: some properties and methods are dedicated to
            reference objects only, and some others are for components only. This is clearly stated
            for each property or method concerned.

        :param com_object: Product COM object
        """

        super().__init__(com_object)
        self.product = com_object

    @property
    def analyze(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Analyze
                | o Property Analyze(    ) As Analyze
                |
                | Returns the Analyze object associated to the current product.
                | Example:    This example retrieves in EngineAnalysis the Analyze
                | object of the Engine product.  Dim EngineAnalysis As Analyze Set
                | EngineAnalysis = Engine.Analyze


                | Parameters:

        :return: analyze object
        """

        return Analyze(self.product.Analyze)

    @property
    def definition(self):
        """

        .. note::
            CAA V5 Visual Basic help
            Property Definition( ) As CATBSTR

            Returns or sets the product's definition.
            Definition is valid for reference products only.
            | Example:
            | This example retrieves the definition of the Engine product in EngineDef.
            |     EngineDef = Engine.Definition


        :return: str()
        """

        return self.product.Definition

    @definition.setter
    def definition(self, definition):
        """
        :param str() definition:
        """

        self.product.Definition = definition

    @property
    def description_instance(self):
        """

        .. note::
            CAA V5 Visual Basic help

            Property DescriptionInst( ) As CATBSTR

            Returns or sets the product's description for a component product.
            DescriptionInst is valid for component products only.
            The description is a comment assigned to the component product to help describe or qualify it.
            | Example:
            | This example sets the description for the EngineComp product.
            |     Desc = "This is the Engine component product description"
            |     EngineComp.DescriptionInst(Desc)

        :return: str()
        """

        return self.product.DescriptionInst

    @description_instance.setter
    def description_instance(self, description_instance):
        """
        :param str() description_instance:
        """

        self.product.DescriptionInst = description_instance

    @property
    def description_reference(self):
        """

        .. note::
            CAA V5 Visual Basic help

            Property DescriptionRef( ) As CATBSTR

            Returns or sets the product's description for a reference product.
            DescriptionRef is valid for reference products only.
            The description is a comment assigned to the reference product to help describe or qualify it.
            | Example:
            | This example sets the description for the Engine product.
            |      Desc = "This is the Engine reference product description"
            |      Engine.DescriptionRef(Desc)


        :return: str()
        """

        return self.product.DescriptionRef

    @description_reference.setter
    def description_reference(self, description_reference):
        """
        :param str description_reference:
        """
        self.product.DescriptionRef = description_reference

    @property
    def move(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Move
                | o Property Move(    ) As Move
                |
                | Returns the product's move object. The move object is aggregated by
                | the product object and itself aggregates a movable object to which you
                | can apply a move transformation by means of an isometry matrix. It
                | moves your product master shape representation according to this
                | isometry.  Example:    This example retrieves the move object for the
                | Engine product.  Dim EngineMoveObject As Move Set EngineMoveObject =
                | Engine.Move


                | Parameters:


        """
        return Move(self.product)

    @property
    def file_name(self):
        """

        :return: str()
        """

        return self.product.ReferenceProduct.Parent.Name

    @property
    def full_name(self):
        """

        :return: str()
        """

        return self.product.ReferenceProduct.Parent.FullName

    def path(self):
        """
       
        Returns the pathlib.Path() object of the document fullname.

        example e:\\users\\psr\\Parts\\MyNiceProduct.CATProduct
        >>> Product.path().name
        MyNiceProduct.CATProduct
        >>> Product.path().parent
        e:\\users\\psr\\Parts\\
        >>> Product.path().suffix
        .CATProduct

        :return: Path()
        """

        return Path(self.full_name)

    @property
    def nomenclature(self):
        """

        .. note::
            CAA V5 Visual Basic help

            Property Nomenclature( ) As CATBSTR

            Returns or sets the product's nomenclature.
            Nomenclature is valid for reference products only.
            According to the STEP AP203, the nomenclature is
            "a name by which the part is commonly known within an organization".
            | Example:
            | This example retrieves the nomenclature the Engine product in EngineNom.
            | EngineNom = Engine.Nomenclature

        :return: str()
        """

        return self.product.nomenclature

    @nomenclature.setter
    def nomenclature(self, nomenclature):
        """
        :param str() nomenclature:
        """

        self.product.nomenclature = nomenclature

    @property
    def parameters(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Parameters
                | o Property Parameters(    ) As Parameters
                |
                | Returns the collection object containing the product parameters. All
                | the parameters that are aggregated in the different objects of the
                | product might be accessed through that collection.  Example:The
                | following example returns in params the parameters of the productRoot
                | product from the productDoc product document:  Set productRoot =
                | productDoc.Product Set params = productRoot.Parameters


                | Parameters:


        """
        # todo: not implemented yet.
        return self.product.Parameters

    @property
    def part_number(self):
        """

        .. note::
            CAA V5 Visual Basic help

            Property PartNumber( ) As CATBSTR

            Returns or sets the product's part number.
            PartNumber is valid for reference products only.
            | Example:
            | This example sets the Engine product's part number to A120-253X-7.
            |     Engine.PartNumber("A120-253X-7")


        :return: str()
        """

        return self.product.PartNumber

    @part_number.setter
    def part_number(self, part_number):
        """
        :param str() part_number:
        """

        self.product.PartNumber = part_number

    @property
    def position(self):
        """
         .. note::
             CAA V5 Visual Basic help

                 | Position
                 | o Property Position(    ) As Position
                 |
                 | Returns the product's position object. The position object is the
                 | object aggregated by the product object that holds the position of the
                 | master shape representation in the space.  Example:    This example
                 | retrieves the position object for the Engine product.  Dim
                 | EnginePositionObject As Position Set EnginePositionObject =
                 | Engine.Position


                 | Parameters:

         """

        return Position(self.product)

    @property
    def products(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Products
                | o Property Products(    ) As Products
                |
                | Returns the collection of products contained in the current product.
                | Example:    This example retrieves in EngineChildren the collection of
                | products contained in the Engine product.  Dim EngineChildren As
                | Products Set EngineChildren = Engine.Products


                | Parameters:


        """
        return self.product.Products

    @property
    def publications(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Publications
                | o Property Publications(    ) As Publications
                |
                | Returns the collection of publications managed by the product.


                | Parameters:


        """
        return self.product.Publications

    @property
    def reference_product(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | ReferenceProduct
                | o Property ReferenceProduct(    ) As Product
                |
                | Returns the Reference Product of this instance.


                | Parameters:


        """
        return self.product.ReferenceProduct

    @property
    def relations(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Relations
                | o Property Relations(    ) As Relations
                |
                | Returns the collection object containing the product relations. All
                | the relations that are used to valuate the parameters of the product
                | might be accessed thru that collection.  Example:The following example
                | returns in rels the relations of the productRoot product from the
                | productDoc product document:  Set productRoot = productDoc.Product Set
                | rels = productRoot.Relations


                | Parameters:


        """
        return self.product.Relations

    @property
    def revision(self):
        """

        .. note::
            CAA V5 Visual Basic help

            Property Revision( ) As CATBSTR

            Returns or sets the product's revision number.
            Revision is valid for reference products only.
            | Example:
            | This example sets the Engine product's revision number to 3A.
            |     Engine.Revision("3A")

        :return: str
        """

        return self.product.Revision

    @revision.setter
    def revision(self, revision):
        """
        :param str() revision:
        """

        self.product.Revision = revision

    @property
    def source(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Source
                | o Property Source(    ) As CatProductSource
                |
                | Returns or sets the product's source. Source is valid for reference
                | products only.  According to the STEP AP203, the source is the "design
                | organization's plan for obtaining the product". The source can take
                | the values catProductMade if the product is made internally,
                | catProductBought if it is purchased from a vendor, or
                | catProductUnknown if its origin is not determined.  Example:    This
                | example sets the source for the Engine product to catProductMade.
                | Engine.Source(catProductMade)


                | Parameters:


        """
        return self.product.Source

    @property
    def user_ref_properties(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | UserRefProperties
                | o Property UserRefProperties(    ) As Parameters
                |
                | Returns the collection object containing the product properties. All
                | the user defined properties that are created in the reference product
                | might be accessed through that collection.  Only available on
                | reference products.  Example:The following example returns in
                | UserProps the properties of the productRoot product from the
                | productDoc product document:  Set productRoot = productDoc.Product Set
                | UserProps = productRoot.UserRefProperties


                | Parameters:


        """
        return self.product.UserRefProperties

    def attributes(self):
        """
        Returns a string describing the products attributes.

        :return: str
        """

        return ('(Product) Attributes... \n'
                f'File Name:             {self.file_name}\n'
                f'Name:                  {self.name}\n'
                f'Part Number:           {self.part_number}\n'
                f'Revision:              {self.revision}\n'
                f'Definition:            {self.definition}\n'
                f'Nomenclature:          {self.nomenclature}\n'
                f'Description Instance:  {self.description_instance}\n'
                f'Description Reference: {self.description_reference}\n'
                f'Reference:             {self.reference_product}\n'
                f'Is CATProduct:         {self.is_catproduct()}\n'
                f'Is CATPart:            {self.is_catpart()}')

    def activate_default_shape(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | ActivateDefaultShape
                | o Sub ActivateDefaultShape(    )
                |
                | Activate default shape.


                | Parameters:


        """
        return self.product.ActivateDefaultShape()

    def activate_shape(self, shape_name):
        """
        .. note::
            CAA V5 Visual Basic help

                | ActivateShape
                | o Sub ActivateShape(    CATBSTR    ShapeName)
                |
                | Activate one shape.


                | Parameters:
                | ShapeName
                |            The name of the shape.


        """
        return self.product.ActivateShape(shape_name)

    @staticmethod
    def activate_terminal_node(products):
        """
        Method to 'Activate Terminal Node'.

        Loops through ALL products in product and activates_default_shape().

        :param products: self.get_products()
        """

        # noinspection PyShadowingNames
        def loop_d_loop(products):

            for product in products:
                if product.is_catpart():
                    product.activate_default_shape()
                elif product.is_catproduct():
                    loop_d_loop(product.get_products())

        loop_d_loop(products)

    def add_master_shape_representation(self, i_shape_path_name):
        """
        .. note::
            CAA V5 Visual Basic help

                | AddMasterShapeRepresentation
                | o Sub AddMasterShapeRepresentation(    CATBSTR    iShapePathName)
                |
                | Adds the master shape representation to the product. The master shape
                | representation is the object that gives a geometric shape and allows
                | the visualization of the product. It can be a CATIA V4 model, a VRML
                | file, or any other type of document that can be displayed. In a multi
                | representation  context, the master shape representation is the most
                | meaningful representation of the product according to the user. This
                | is the default shape for the multi representation. Note: This master
                | shape representation is optional.


                | Parameters:
                | iShapePathName
                |    The path name where the master shape representation can be found


                | Examples:
                |
                | This example adds the e:/Models/Engine.model as
                | the master shape representation to the Engine product.
                |
                | Engine.AddMasterShapeRepresentation("e:/Models/Engine.model")
                |
                |
                |
        """
        # todo: not yet implemented
        return self.product.AddMasterShapeRepresentation(i_shape_path_name)

    def add_shape_representation(self, i_shape_path_name, i_shape_name, i_rep_behavior, i_context):
        """
        .. note::
            CAA V5 Visual Basic help

                | AddShapeRepresentation
                | o Sub AddShapeRepresentation(    CATBSTR    iShapePathName,
                |                                  CATBSTR    iShapeName,
                |                                  CatRepType    iRepBehavior,
                |                                  boolean    iContext)
                |
                | Adds a representation to the product with a specific behavior. A
                | representation is the object that gives a geometric shape and allows
                | the visualization of the product. It can be  a CATIA V4 model, a VRML
                | file, or any other type of document that can be displayed. Note: The
                | possible behavior supported are : 3D, 2D and text. The representation
                | can also be added within a context or not. A representation on a
                | product is optional, but many representation with  different behavior
                | (or the same) is supported


                | Parameters:
                | iShapePathName
                |    The path name where the representation can be found
                |
                |  iShapeName
                |    The name that is given to the representation
                |    This name is a user free choice
                |
                |  iRepBehavior
                |    The behavior of the added representation.
                |    It can take the values catRep3D if the representation is a 3D one,
                |    catRep2D if the representation is a 2D one,
                |    or catRepText if the representation is a text one.
                |
                |  iContext
                |    A condition to specify if the added representation can be
                |    displayed with the representation of other products.


                | Examples:
                |
                | This example adds the e:/Models/Engine.model as
                | a 3D representation to the Engine product within an assembly context.
                |
                | Engine.AddShapeRepresentation("e:/Models/Engine.model","MyShape",catRep3D,TRUE)
                |

        """
        # todo: not yet implemented
        return self.product.AddShapeRepresentation(i_shape_path_name, i_shape_name, i_rep_behavior, i_context)

    def apply_work_mode(self, new_mode):
        """
        Applies the work mode defined by new_mode.

        new_mode must be a string that matches KEY value of cat_work_types

        .. note::
            CAA V5 Visual Basic help

                | ApplyWorkMode
                | o Sub ApplyWorkMode(    CatWorkModeType    newMode)
                |
                | Applies a new working mode.


                | Parameters:
                | newMode
                |            The new working mode.

        :param str new_mode:
        """
        return self.product.ApplyWorkMode(cat_work_mode_types[new_mode])

    def connections(self, i_connections_type):
        """
        .. note::
            CAA V5 Visual Basic help

                | Connections
                | o Func Connections(    CATBSTR    iConnectionsType) As Collection
                |
                | Returns the product's constraints. The constraint collection of a
                | product gathers the constraints this product should respect to be
                | positioned in the space.  Example:    This example retrieves the
                | constraint collection for the Engine product.  Dim EngineConstraints
                | As Collection Set EngineConstraints = Engine.Constraints


                | Parameters:


        """
        return self.product.Connections(i_connections_type)

    def create_reference_from_name(self, i_label):
        """
        .. note::
            CAA V5 Visual Basic help

                | CreateReferenceFromName
                | o Func CreateReferenceFromName(    CATBSTR    iLabel) As Reference
                |
                | Creates a reference from a name. A reference is an object that can
                | stand for any geometrical object. Creating references is necessary for
                | adding constraints between two components using Brep elements of the
                | representations of these components.


                | Parameters:
                | iLabel
                |    The path of the Brep element to use in the constraint.
                |    This path is passed as a character string comprising the component
                |    path from the root product to the component concerned, concatenated
                |    to the Brep element path in the product's representation.
                |    Components are separated using "/", and the product path is separated
                |    from the Brep using "/!". For separating parameter from product path use "/".
                |
                |
                |  Returns:
                |   The created reference


                | Examples:
                |
                | This example creates a reference from the path of a Brep element
                | in the Prod2 product located below the Root root
                | product. The face is located in the Pad.1 pad and limited by the
                | Circle.1 circle.
                |
                | Dim Ref As Reference
                | Ref = Prod2.CreateReferenceFromName("Root/Prod2/!Face:(Brp:(Pad.1:0(Brp:(Circle.1))):None())")
                |
                |
                |
        """
        return self.product.CreateReferenceFromName(i_label)

    def desactivate_default_shape(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | DesactivateDefaultShape
                | o Sub DesactivateDefaultShape(    )
                |
                | Deactivate default shape.


                | Parameters:


        """
        return self.product.DesactivateDefaultShape()

    def desactivate_shape(self, shape_name):
        """
        .. note::
            CAA V5 Visual Basic help

                | DesactivateShape
                | o Sub DesactivateShape(    CATBSTR    ShapeName)
                |
                | Deactivate one shape.


                | Parameters:
                | ShapeName
                |            The name of the shape.


        """
        return self.product.DesactivateShape(shape_name)

    def extract_bom(self, i_file_type, i_file):

        """

        i_file_type must be a string that matches KEY value of cat_file_types

        .. note::
            CAA V5 Visual Basic help

                | ExtractBOM
                | o Sub ExtractBOM(    CatFileType    iFileType,
                |                      CATBSTR    iFile)
                |
                | Extracts the product's contents as a bill of materials (BOM). The bill
                | of material displays, for every sub-assembly in the product, the one
                | level depth components and some of their properties.


                | Parameters:
                | iFileType
                |    Set this parameter to catFileTypeHTML to save to the html format.
                |
                |    Set this parameter to catFileTypeTXT to save to the text format.
                |
                |    The catFileTypeMotif should not be used.
                |
                |  iFile
                |    File where the bill of material will be saved


        """
        return self.product.ExtractBOM(cat_file_types[i_file_type], i_file)

    def get_active_shape_name(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetActiveShapeName
                | o Func GetActiveShapeName(    ) As CATBSTR
                |
                | Returns the name of the active shape.  Returns:  oShapeName
                | The name of the active shape.


                | Parameters:


        """
        return self.product.GetActiveShapeName()

    def get_all_shapes_names(self, olistshape):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetAllShapesNames
                | o Sub GetAllShapesNames(    CATSafeArrayVariant    olistshape)
                |
                | List the name of all shapes.  Returns:  olistshape           The list
                | of the names  The tab olistshape has to be allocated with a size given
                | by GetNumberOfShapes.


                | Parameters:


        """
        return self.product.GetAllShapesNames(olistshape)

    def count_children(self):
        """

       :return: int()
       """

        return self.product.Products.Count

    def get_child(self, index):
        """

        .. warning::

        The index MUST be it's python index (indexs in python start from 0) from the Documents.get_documents()
        collection. The COM interface index starts at 1.

        :return: Product()
        """
        return Product(self.product.Products.Item(index + 1))

    def get_children(self):
        """

        :return: list(Product())
        """

        children = list()

        if self.has_children():
            for i in range(self.product.Products.Count):
                child = Product(self.product.Products.Item(i + 1))
                children.append(child)

        return children

    def get_default_shape_name(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetDefaultShapeName
                | o Func GetDefaultShapeName(    ) As CATBSTR
                |
                | Returns the default shape.  Returns:  oShapeName           The name of
                | the default shape.


                | Parameters:


        """
        return self.product.GetDefaultShapeName()

    def get_master_shape_representation(self, i_load_if_necessary):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetMasterShapeRepresentation
                | o Func GetMasterShapeRepresentation(    boolean    iLoadIfNecessary) As CATBaseDispatch
                |
                | Retrieves the product's master shape representation.


                | Parameters:
                | iLoadIfNecessary
                |    Parameter to set to True if the master shape representation
                |    should be loaded to determine if it exists, or to False otherwise.


                | Examples:
                |
                | This example retrieves in MSRep the
                | Engine product's master shape representation.
                |
                | Dim MSRep As Object
                | Set MSRep = Engine.GetMasterShapeRepresentation(True)
                |
                |
                |
        """
        return self.product.GetMasterShapeRepresentation(i_load_if_necessary)

    def get_master_shape_representation_path_name(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetMasterShapeRepresentationPathName
                | o Func GetMasterShapeRepresentationPathName(    ) As CATBSTR
                |
                | Retrieves the product's master shape representation pathname.
                | Example:    This example retrieves in MSRep the  Engine product's
                | master shape representation.  Set MSRepPath =
                | Engine.GetMasterShapeRepresentationPathName


                | Parameters:


        """
        return self.product.GetMasterShapeRepresentationPathName()

    def get_number_of_shapes(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetNumberOfShapes
                | o Func GetNumberOfShapes(    ) As short
                |
                | Returns the number of Shapes  Returns:  oNbShapes           The number
                | of Shapes.


                | Parameters:


        """
        return self.product.GetNumberOfShapes()

    def get_products(self):
        """
        Returns a list of Products().

        :return: list(Prouct())
        """
        products = []

        for i in range(0, self.product.Products.Count):
            product = Product(self.product.Products.Item(i + 1))
            products.append(product)

        return products

    def get_shape_path_name(self, i_shape_name):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetShapePathName
                | o Func GetShapePathName(    CATBSTR    iShapeName) As CATBSTR
                |
                | Returns the path name of a shape for a given shape name.


                | Parameters:
                | iShapeName
                |    The name of the shape.
                |
                |
                |  Returns:
                |   oShapePathName           The path name of the shape.


        """
        return self.product.GetShapePathName(i_shape_name)

    def get_shape_representation(self, i_load_if_necessary, i_shape_name, i_rep_behavior, i_context):
        """

        i_rep_behaviour must be a string taken from KEY value of cat_rep_types
        .. note::
            CAA V5 Visual Basic help

                | GetShapeRepresentation
                | o Func GetShapeRepresentation(    boolean    iLoadIfNecessary,
                |                                   CATBSTR    iShapeName,
                |                                   CatRepType    iRepBehavior,
                |                                   boolean    iContext) As CATBaseDispatch
                |
                | Retrieves the product's  representation with the given parameters.


                | Parameters:
                | iLoadIfNecessary
                |    Parameter to set to True if the master shape representation
                |    should be loaded to determine if it exists, or to False otherwise.
                |
                |  iShapeName
                |    The name of the representation of the product.
                |
                |  iRepBehavior
                |    The behavior of the representation.
                |    It can take the values catRep3D if the representation is a 3D one,
                |    catRep2D if the representation is a 2D one,
                |    or catRepText if the representation is a text one.
                |
                |  iContext
                |    A condition to specify if the representation is
                |    displayed with the representation of other products.


                | Examples:
                |
                | This example retrieves in MSRep the
                | Engine product's  3D representation named "PART".
                |
                | Dim MSRep As Object
                | Set MSRep = Engine.GetMasterShapeRepresentation(True,"PART",catRep3D,TRUE)
                |
                |
                |
        """
        return self.product.GetShapeRepresentation(i_load_if_necessary, i_shape_name, cat_rep_types[i_rep_behavior],
                                                   i_context)

    def get_technological_object(self, i_application_type):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetTechnologicalObject
                | o Func GetTechnologicalObject(    CATBSTR    iApplicationType) As CATBaseDispatch
                |
                | Returns the product's applicative data which type is the given
                | parameter. The data returned can be either a collection or a simple
                | object.


                | Parameters:
                | iApplicationType
                |    The type of applicative data searched.


                | Examples:
                |
                | This example retrieves the constraints for the
                | Engine product.
                |
                | Dim EngineConstraints As Collection
                | Set EngineConstraints = Engine.GetTechnologicalObject("Constraints")
                |
                |
                |
        """
        return self.product.GetTechnologicalObject(i_application_type)

    def has_children(self):
        """

        :return: bool
        """

        if self.product.Products.Count > 0:
            return True

        return False

    def has_shape_representation(self, i_shape_name, i_rep_behavior, i_context):
        """
        .. note::
            CAA V5 Visual Basic help

                | HasShapeRepresentation
                | o Func HasShapeRepresentation(    CATBSTR    iShapeName,
                |                                   CatRepType    iRepBehavior,
                |                                   boolean    iContext) As boolean
                |
                | Returns whether the product has a representation of the given name
                | with a given behavior. True if the product has such a representation.


                | Parameters:
                | iShapeName
                |    The name of the representation of the product.
                |
                |  iRepBehavior
                |    The behavior of the representation.
                |    It can take the values catRep3D if the representation is a 3D one,
                |    catRep2D if the representation is a 2D one,
                |    or catRepText if the representation is a text one.
                |
                |  iContext
                |    A condition to specify if the representation is
                |    displayed with the representation of other products.


                | Examples:
                |
                | This example retrieves in HasRep whether the
                | Engine product has a master shape representation.
                |
                | HasRep = Engine.HasRepresentation("PART",catRep3D,TRUE)
                |
                |
                |
        """
        return self.product.HasShapeRepresentation(i_shape_name, cat_rep_types[i_rep_behavior], i_context)

    def is_catproduct(self):
        """

        :return: bool
        """

        if 'catproduct' == self.file_name.rsplit('.')[-1].lower():
            return True

        return False

    def is_catpart(self):
        """

        :return: bool
        """

        if 'catpart' == self.file_name.rsplit('.')[-1].lower():
            return True

        return False

    def remove_master_shape_representation(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | RemoveMasterShapeRepresentation
                | o Sub RemoveMasterShapeRepresentation(    )
                |
                | Removes the master shape representation from the product. The master
                | shape representation is the object that gives a geometric shape and
                | allows the visualization of the product. It can be a CATIA V4 model, a
                | VRML file, or any other type of document that can be displayed. In a
                | multi representation  context, the master shape representation is the
                | most  meaningful representation of the product according to the user.
                | This is the default shape for the multi representation. Note: This
                | master shape representation is optional.  Example:    This example
                | removes the master shape representation of the Engine product.
                | Engine.RemoveMasterShapeRepresentation()


                | Parameters:


        """
        return self.product.RemoveMasterShapeRepresentation()

    def remove_shape_representation(self, i_shape_name, i_rep_behavior, i_context):
        """
        .. note::
            CAA V5 Visual Basic help

                | RemoveShapeRepresentation
                | o Sub RemoveShapeRepresentation(    CATBSTR    iShapeName,
                |                                     CatRepType    iRepBehavior,
                |                                     boolean    iContext)
                |
                | Removes a specific representation from the product. A representation
                | is the object that gives a geometric shape and allows the
                | visualization of the product.. It can be a CATIA V4 model, a VRML
                | file, or any other type of document that can be displayed. Note: This
                | representation is optional.


                | Parameters:
                | iShapeName
                |    The name of the representation of the product.
                |
                |  iRepBehavior
                |    The behavior of the representation.
                |    It can take the values catRep3D if the representation is a 3D one,
                |    catRep2D if the representation is a 2D one,
                |    or catRepText if the representation is a text one.
                |
                |  iContext
                |    A condition to specify if the representation is
                |    displayed with the representation of other products.


                | Examples:
                |
                | This example removes the 3D representation named "PART" of the
                | Engine product.
                |
                | Engine.RemoveMasterShapeRepresentation
                | ("PART",catRep3D,TRUE)
                |
                |
                |
        """
        return self.product.RemoveShapeRepresentation(i_shape_name, cat_rep_types[i_rep_behavior], i_context)

    def update(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Update
                | o Sub Update(    )
                |
                | Updates the product. This update is performed with respect to the part
                | making the product or to the product's representation. It takes into
                | account the  components of the product at any level  Example:     The
                | following example updates the root product:  Dim RootProduct As
                | Product Set Rootproduct = productDoc.Product Rootproduct.Update


                | Parameters:


        """
        return self.product.Update()

    def __repr__(self):
        return f'Product(name="{self.name}")'
