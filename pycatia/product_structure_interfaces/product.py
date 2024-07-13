#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.

"""

from pathlib import Path
from typing import TYPE_CHECKING
import warnings

from pywintypes import com_error

from pycatia.exception_handling.exceptions import CATIAApplicationException
from pycatia.in_interfaces.move import Move
from pycatia.in_interfaces.position import Position
from pycatia.in_interfaces.reference import Reference
from pycatia.knowledge_interfaces.parameters import Parameters
from pycatia.knowledge_interfaces.relations import Relations
from pycatia.mec_mod_interfaces.constraints import Constraints
from pycatia.product_structure_interfaces.analyze import Analyze
from pycatia.product_structure_interfaces.publications import Publications
from pycatia.system_interfaces.any_object import AnyObject

if TYPE_CHECKING:
    from pycatia.product_structure_interfaces.products import Products
    from pycatia.in_interfaces.document import Document


class Product(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     Product
                |
                | Represents the product.
                | The product is the object that helps you model your real products by building a
                | tree structure whose nodes are product objects. Each of them may contain other
                | product objects gathered in a product collection. The terminal product objects
                | in the tree structure have no aggregated product collection. Even if all
                | products are located somewhere in the product tree structure, some of them can
                | be used as reference products to create other products named components, which
                | are instances of the reference product. For example, the left front wheel in a
                | car can be used as reference to create the other wheels. Be careful: some
                | properties and methods are dedicated to reference objects only, and some others
                | are for components only. This is clearly stated for each property or method
                | concerned.

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.product = com_object

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

        return Analyze(self.product.Analyze)

    @property
    def definition(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property Definition() As CATBSTR
                |
                |     Returns or sets the product's definition.
                |     Definition is valid for reference products only.
                |
                |     Example:
                |
                |           This example retrieves the definition of the
                |          Engine product in EngineDef.
                |
                |
                |          EngineDef = Engine.Definition

        :rtype: str
        """

        return self.product.Definition

    @definition.setter
    def definition(self, value: str):
        """
        :param str value:
        """

        self.product.Definition = value

    @property
    def description_instance(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property DescriptionInst() As CATBSTR
                |
                |     Returns or sets the product's description for a component
                |     product.
                |     DescriptionInst is valid for component products only.
                |     The description is a comment assigned to the component product to help
                |     describe or qualify it.
                |
                |     Example:
                |
                |           This example sets the description for the
                |          EngineComp product.
                |
                |
                |          Desc = "This is the Engine component product description"
                |          EngineComp.DescriptionInst(Desc)

        :rtype: str
        """

        return self.product.DescriptionInst

    @description_instance.setter
    def description_instance(self, value: str):
        """
        :param str value:
        """

        self.product.DescriptionInst = value

    @property
    def description_reference(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property DescriptionRef() As CATBSTR
                |
                |     Returns or sets the product's description for a reference
                |     product.
                |     DescriptionRef is valid for reference products only.
                |     The description is a comment assigned to the reference product to help
                |     describe or qualify it.
                |
                |     Example:
                |
                |           This example sets the description for the
                |          Engine product.
                |
                |
                |          Desc = "This is the Engine reference product description"
                |          Engine.DescriptionRef(Desc)

        :rtype: str
        """

        return self.product.DescriptionRef

    @description_reference.setter
    def description_reference(self, value: str):
        """
        :param str value:
        """

        self.product.DescriptionRef = value

    @property
    def file_name(self) -> str:
        """
        :return: str()
        """

        return self.reference_product.parent.name

    @property
    def full_name(self) -> str:
        """
        :return: str()
        """

        return self.reference_product.parent.com_object.FullName

    @property
    def move(self) -> Move:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property Move() As Move (Read Only)
                |
                |     Returns the product's move object. The move object is aggregated by the
                |     product object and itself aggregates a movable object to which you can apply a
                |     move transformation by means of an isometry matrix. It moves your product
                |     master shape representation according to this isometry.
                |
                |     Example:
                |
                |           This example retrieves the move object for the
                |          Engine product.
                |
                |
                |          Dim EngineMoveObject As Move
                |          Set EngineMoveObject = Engine.Move

        :return: Move
        """

        return Move(self.product.Move)

    @property
    def nomenclature(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property Nomenclature() As CATBSTR
                |
                |     Returns or sets the product's nomenclature.
                |     Nomenclature is valid for reference products only.
                |     According to the STEP AP203, the nomenclature is "a name by which the part
                |     is commonly known within an organization".
                |
                |     Example:
                |
                |           This example retrieves the nomenclature the
                |          Engine product in EngineNom.
                |
                |
                |          EngineNom = Engine.Nomenclature

        :rtype: str
        """

        return self.product.Nomenclature

    @nomenclature.setter
    def nomenclature(self, value: str):
        """
        :param str value:
        """

        self.product.Nomenclature = value

    @property
    def parameters(self) -> Parameters:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property Parameters() As Parameters (Read Only)
                |
                |     Returns the collection object containing the product parameters. All the
                |     parameters that are aggregated in the different objects of the product might be
                |     accessed through that collection.
                |
                |     Example:
                |         The following example returns in params the parameters of the
                |         productRoot product from the productDoc product
                |         document:
                |
                |          Set productRoot = productDoc.Product
                |          Set params = productRoot.Parameters

        :rtype: Parameters
        """

        return Parameters(self.product.Parameters)

    @property
    def part_number(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property PartNumber() As CATBSTR
                |
                |     Returns or sets the product's part number.
                |     PartNumber is valid for reference products only.
                |
                |     Example:
                |
                |           This example sets the
                |          Engine product's part number to A120-253X-7.
                |
                |
                |          Engine.PartNumber("A120-253X-7")

        :rtype: str
        """
        try:
            return self.product.PartNumber
        except com_error:
            raise CATIAApplicationException(
                f'Prodcut "{self.name}" could not do get Product.PartNumber. Check Product for broken links.')

    @part_number.setter
    def part_number(self, value: str):
        """
        :param str value:
        """

        try:
            self.product.PartNumber = value
        except com_error:
            raise CATIAApplicationException(
                f'Prodcut "{self.name}" could not do set Product.PartNumber. Check Product for broken links.')

    @property
    def position(self) -> Position:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property Position() As Position (Read Only)
                |
                |     Returns the product's position object. The position object is the object
                |     aggregated by the product object that holds the position of the master shape
                |     representation in the space.
                |
                |     Example:
                |
                |           This example retrieves the position object for the
                |          Engine product.
                |
                |
                |          Dim EnginePositionObject As Position
                |          Set EnginePositionObject = Engine.Position

        :rtype: Position
        """

        return Position(self.product.Position)

    @property
    def products(self) -> 'Products':
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property Products() As Products (Read Only)
                |
                |     Returns the collection of products contained in the current
                |     product.
                |
                |     Example:
                |
                |           This example retrieves in EngineChildren the collection
                |           of
                |          products contained in the Engine product.
                |
                |
                |          Dim EngineChildren As Products
                |          Set EngineChildren = Engine.Products

        :rtype: Products
        """
        from pycatia.product_structure_interfaces.products import Products
        return Products(self.product.Products)

    @property
    def publications(self) -> Publications:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property Publications() As Publications (Read Only)
                |
                |     Returns the collection of publications managed by the product.

        :rtype: Publications
        """

        return Publications(self.product.Publications)

    @property
    def reference_product(self) -> 'Product':
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property ReferenceProduct() As Product (Read Only)
                |
                |     Returns the Reference Product of this instance.

        :rtype: Product
        """
        try:
            return Product(self.product.ReferenceProduct)
        except com_error:
            raise CATIAApplicationException(
                f'Product "{self.name}" could not do get Reference Product. Check Product for broken links.')

    @property
    def relations(self) -> Relations:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property Relations() As Relations (Read Only)
                |
                |     Returns the collection object containing the product relations. All the
                |     relations that are used to valuate the parameters of the product might be
                |     accessed thru that collection.
                |
                |     Example:
                |         The following example returns in rels the relations of the productRoot
                |         product from the productDoc product document:
                |
                |          Set productRoot = productDoc.Product
                |          Set rels = productRoot.Relations

        :rtype: Relations
        """

        return Relations(self.product.Relations)

    @property
    def revision(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property Revision() As CATBSTR
                |
                |     Returns or sets the product's revision number.
                |     Revision is valid for reference products only.
                |
                |     Example:
                |
                |           This example sets the
                |          Engine product's revision number to 3A.
                |
                |
                |          Engine.Revision("3A")

        :rtype: str
        """

        return self.product.Revision

    @revision.setter
    def revision(self, value: str):
        """
        :param str value:
        """

        self.product.Revision = value

    @property
    def source(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property Source() As CatProductSource
                |
                |     Returns or sets the product's source.
                |     Source is valid for reference products only.
                |     According to the STEP AP203, the source is the "design organization's plan
                |     for obtaining the product". The source can take the values catProductMade if
                |     the product is made internally, catProductBought if it is purchased from a
                |     vendor, or catProductUnknown if its origin is not
                |     determined.
                |
                |     Example:
                |
                |           This example sets the source for the
                |          Engine product to catProductMade.
                |
                |
                |          Engine.Source(catProductMade)

        :return: enum cat_product_source
        :rtype: int
        """

        try:
            return self.product.Source
        except com_error:
            raise CATIAApplicationException(
                f'Prodcut "{self.name}" could not do get Product.Source. Check Product for broken links.')

    @source.setter
    def source(self, value: int):
        """
        :param int value: enum cat_product_source
        """

        try:
            self.product.Source = value
        except com_error:
            raise CATIAApplicationException(
                f'Prodcut "{self.name}" could not do set Product.Source. Check Product for broken links.')

    @property
    def type(self) -> str:
        """
        Returns the type of product (CATProduct, CATPart or Component).

        :rtype: str
        """

        root_product_name = self.reference_product.com_object.Parent.Product.Name
        self_product_name = self.reference_product.name
        if root_product_name == self_product_name:
            return self.reference_product.com_object.Parent.Name.split('.')[-1]
        else:
            return "Component"

    @property
    def user_ref_properties(self) -> Parameters:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property UserRefProperties() As Parameters (Read Only)
                |
                |     Returns the collection object containing the product properties. All the
                |     user defined properties that are created in the reference product might be
                |     accessed through that collection.
                |     Only available on reference products.
                |
                |     Example:
                |         The following example returns in UserProps the properties of the
                |         productRoot product from the productDoc product
                |         document:
                |
                |          Set productRoot = productDoc.Product
                |          Set UserProps = productRoot.UserRefProperties

        :rtype: Parameters
        """

        return Parameters(self.product.UserRefProperties)

    def activate_default_shape(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub ActivateDefaultShape()
                |
                |     Activate default shape.

        :rtype: None
        """
        return self.product.ActivateDefaultShape()

    def activate_shape(self, shape_name: str) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub ActivateShape(CATBSTR ShapeName)
                |
                |     Activate one shape.
                |
                |     Parameters:
                |
                |         ShapeName
                |             The name of the shape.

        :param str shape_name:
        :rtype: None
        """
        return self.product.ActivateShape(shape_name)

    @staticmethod
    def activate_terminal_node(products: 'Products') -> None:
        """
        Method to 'Activate Terminal Node'.
        Loops through ALL products in product and activates_default_shape().
        :param list(Product) products:
        """

        def product_looper(_products: 'Products'):
            for current_product in _products:
                try:
                    current_product.activate_default_shape()
                except CATIAApplicationException:
                    current_product.logger.info(f'Could not activate default shape for {current_product.name}.')

                product_looper(current_product.products)

        product_looper(products)

    def add_master_shape_representation(self, i_shape_path_name=None) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub AddMasterShapeRepresentation(CATBSTR iShapePathName)
                |
                |     Adds the master shape representation to the product. The master shape
                |     representation is the object that gives a geometric shape and allows the
                |     visualization of the product. It can be a CATIA V4 model, a VRML file, or any
                |     other type of document that can be displayed. In a multi representation
                |     context, the master shape representation is the most meaningful representation
                |     of the product according to the user. This is the default shape for the multi
                |     representation.
                |
                |     Note: This master shape representation is optional.
                |
                |     Parameters:
                |
                |         iShapePathName
                |             The path name where the master shape representation can be found
                |
                |
                |     Example:
                |
                |           This example adds the e:\\Models\\Engine.model as
                |          the master shape representation to the Engine
                |          product.
                |
                |
                |      Engine.AddMasterShapeRepresentation("e:\\Models\\Engine.model")

        :param str i_shape_path_name:
        :return: None
        """
        return self.product.AddMasterShapeRepresentation(i_shape_path_name)

    def add_shape_representation(
            self,
            i_shape_path_name: str,
            i_shape_name: str,
            i_rep_behavior: int,
            i_context: bool
    ) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub AddShapeRepresentation(CATBSTR iShapePathName,
                | CATBSTR iShapeName,
                | CatRepType iRepBehavior,
                | boolean iContext)
                |
                |     Adds a representation to the product with a specific behavior. A
                |     representation is the object that gives a geometric shape and allows the
                |     visualization of the product. It can be a CATIA V4 model, a VRML file, or any
                |     other type of document that can be displayed.
                |
                |     Note: The possible behavior supported are : 3D, 2D and text.
                |     The representation can also be added within a context or not.
                |     A representation on a product is optional, but many representation
                |     with different behavior (or the same) is supported
                |
                |     Parameters:
                |
                |         iShapePathName
                |             The path name where the representation can be found
                |
                |         iShapeName
                |             The name that is given to the representation This name is a user
                |             free choice
                |         iRepBehavior
                |             The behavior of the added representation. It can take the values
                |             catRep3D if the representation is a 3D one, catRep2D if the representation is a
                |             2D one, or catRepText if the representation is a text one.
                |
                |         iContext
                |             A condition to specify if the added representation can be displayed
                |             with the representation of other products.
                |
                |     Example:
                |
                |           This example adds the e:\\Models\\Engine.model as
                |          a 3D representation to the Engine product within an assembly
                |          context.
                |
                |
                |     Engine.AddShapeRepresentation("e:\\Models\\Engine.model","MyShape",catRep3D,TRUE)

        :param str i_shape_path_name:
        :param str i_shape_name:
        :param int i_rep_behavior: enum cat_rep_type
        :param bool i_context:
        :rtype: None
        """
        return self.product.AddShapeRepresentation(
            i_shape_path_name,
            i_shape_name,
            i_rep_behavior,
            i_context
        )
        # # # # Autogenerated comment:
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'add_shape_representation'
        # # vba_code = """
        # # Public Function add_shape_representation(product)
        # #     Dim iShapePathName (2)
        # #     product.AddShapeRepresentation iShapePathName
        # #     add_shape_representation = iShapePathName
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def apply_work_mode(self, new_mode: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub ApplyWorkMode(CatWorkModeType newMode)
                |
                |     Applies a new working mode.
                |
                |     Parameters:
                |
                |         newMode
                |             The new working mode.

        :param int new_mode: enum cat_work_mode_type
        :rtype: None
        """
        return self.product.ApplyWorkMode(new_mode)

    def attributes(self) -> str:
        """
        Returns a string describing the products attributes.
        :return: str
        """

        return (
            "(Product) Attributes... \n"
            f"File Name:             {self.file_name}\n"
            f"Name:                  {self.name}\n"
            f"Part Number:           {self.part_number}\n"
            f"Revision:              {self.revision}\n"
            f"Definition:            {self.definition}\n"
            f"Nomenclature:          {self.nomenclature}\n"
            f"Description Instance:  {self.description_instance}\n"
            f"Description Reference: {self.description_reference}\n"
            f"Reference:             {self.reference_product}\n"
            f"Is CATProduct:         {self.is_catproduct()}\n"
            f"Is CATPart:            {self.is_catpart()}"
        )

    def constraints(self) -> Constraints:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func Connections(CATBSTR iConnectionsType) As Collection
                |
                |     Returns the product's constraints. The constraint collection of a product
                |     gathers the constraints this product should respect to be positioned in the
                |     space.
                |
                |     Example:
                |
                |           This example retrieves the constraint collection for
                |           the
                |          Engine product.
                |
                |
                |          Dim EngineConstraints As Collection
                |          Set EngineConstraints = Engine.Constraints

        :param str i_connections_type:
        :return: Collection
        """
        return Constraints(self.product.Connections("CATIAConstraints"))

    def create_reference_from_name(self, i_label: str) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func CreateReferenceFromName(CATBSTR iLabel) As Reference
                |
                |     Creates a reference from a name. A reference is an object that can stand
                |     for any geometrical object. Creating references is necessary for adding
                |     constraints between two components using Brep elements of the representations
                |     of these components.
                |
                |     Parameters:
                |
                |         iLabel
                |             The path of the Brep element to use in the constraint. This path is
                |             passed as a character string comprising the component path from the root
                |             product to the component concerned, concatenated to the Brep element path in
                |             the product's representation. Components are separated using "/", and the
                |             product path is separated from the Brep using "/!". For separating parameter
                |             from product path use "\".
                |
                |     Returns:
                |         The created reference
                |     Example:
                |
                |           This example creates a reference from the path of a Brep element
                |
                |          in the Prod2 product located below the Root root
                |          product. The face is located in the Pad.1 pad and limited by
                |          the
                |          Circle.1 circle.
                |
                |
                |          Dim Ref As Reference
                |          Ref = Prod2.CreateReferenceFromName(
                |              "Root/Prod2/!Face:(Brp:(Pad.1:0(Brp:(Circle.1))):None())"
                |          )

        :param str i_label:
        :rtype: Reference
        """
        return Reference(self.product.CreateReferenceFromName(i_label))

    def desactivate_default_shape(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub DesactivateDefaultShape()
                |
                |     Deactivate default shape.

        :rtype: None
        """
        return self.product.DesactivateDefaultShape()

    def desactivate_shape(self, shape_name: str) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub DesactivateShape(CATBSTR ShapeName)
                |
                |     Deactivate one shape.
                |
                |     Parameters:
                |
                |         ShapeName
                |             The name of the shape.

        :param str shape_name:
        :rtype: None
        """
        return self.product.DesactivateShape(shape_name)

    def extract_bom(self, i_file_type: int, i_file: str) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub ExtractBOM(CatFileType iFileType,
                | CATBSTR iFile)
                |
                |     Extracts the product's contents as a bill of materials (BOM). The bill of
                |     material displays, for every sub-assembly in the product, the one level depth
                |     components and some of their properties.
                |
                |     Parameters:
                |
                |         iFileType
                |             Set this parameter to catFileTypeHTML to save to the html
                |             format.
                |             Set this parameter to catFileTypeTXT to save to the text
                |             format.
                |             The catFileTypeMotif should not be used.
                |         iFile
                |             File where the bill of material will be saved

        :param int i_file_type: enum cat_file_type
        :param str i_file:
        :rtype: None
        """
        return self.product.ExtractBOM(i_file_type, i_file)
        # # # # Autogenerated comment:
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'extract_bom'
        # # vba_code = """
        # # Public Function extract_bom(product)
        # #     Dim iFileType (2)
        # #     product.ExtractBOM iFileType
        # #     extract_bom = iFileType
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def count_children(self):
        """
       :return: int()
       """

        return self.product.Products.Count

    @staticmethod
    def generate_ALLCATPart(product: 'Product') -> 'Document':
        """

        Generate an ALLCATPart (CATPart) from CATProduct.

        :param Product product:
        :rtype: Document
        """

        from pycatia.in_interfaces.document import Document

        part = product.com_object.GetItem("DECProductToPart")
        part.Run()
        part = part.GetResult()

        return Document(part)

    def get_active_shape_name(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func GetActiveShapeName() As CATBSTR
                |
                |     Returns the name of the active shape.
                |
                |     Returns:
                |         oShapeName The name of the active shape.

        :return: str
        """
        return self.product.GetActiveShapeName()

    def get_all_shapes_names(self, olistshape: tuple) -> list:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub GetAllShapesNames(CATSafeArrayVariant olistshape)
                |
                |     List the name of all shapes.
                |
                |     Returns:
                |         olistshape The list of the names The tab olistshape has to be allocated
                |         with a size given by GetNumberOfShapes.

        :param tuple olistshape:
        :rtype: None
        """
        return self.product.GetAllShapesNames(olistshape)
        # # # # Autogenerated comment:
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_all_shapes_names'
        # # vba_code = """
        # # Public Function get_all_shapes_names(product)
        # #     Dim olistshape (2)
        # #     product.GetAllShapesNames olistshape
        # #     get_all_shapes_names = olistshape
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_child(self, index) -> 'Product':
        """
        :return: Product()
        """
        return Product(self.product.Products.Item(index + 1))

    def get_children(self) -> list:
        """
        :return: list(Product())
        """

        children = list()

        if self.has_children():
            for i in range(self.product.Products.Count):
                child = Product(self.product.Products.Item(i + 1))
                children.append(child)

        return children

    def get_default_shape_name(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func GetDefaultShapeName() As CATBSTR
                |
                |     Returns the default shape.
                |
                |     Returns:
                |         oShapeName The name of the default shape.

        :return: str
        """
        return self.product.GetDefaultShapeName()

    def get_master_shape_representation(self, i_load_if_necessary: bool) -> AnyObject:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func GetMasterShapeRepresentation(boolean iLoadIfNecessary) As
                | CATBaseDispatch
                |
                |     Retrieves the product's master shape representation.
                |
                |     Parameters:
                |
                |         iLoadIfNecessary
                |             Parameter to set to True if the master shape representation should
                |             be loaded to determine if it exists, or to False otherwise.
                |
                |     Example:
                |
                |           This example retrieves in MSRep the
                |          Engine product's master shape representation.
                |
                |
                |          Dim MSRep As Object
                |          Set MSRep = Engine.GetMasterShapeRepresentation(True)

        :param bool i_load_if_necessary:
        :rtype: AnyObject
        """
        return self.product.GetMasterShapeRepresentation(i_load_if_necessary)

    def get_master_shape_representation_path_name(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func GetMasterShapeRepresentationPathName() As CATBSTR
                |
                |     Retrieves the product's master shape representation
                |     pathname.
                |
                |     Example:
                |
                |          This example retrieves in MSRep the
                |          Engine product's master shape representation.
                |
                |          Set MSRepPath = Engine.GetMasterShapeRepresentationPathName

        :rtype: str
        """
        return self.product.GetMasterShapeRepresentationPathName()

    def get_number_of_shapes(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func GetNumberOfShapes() As short
                |
                |     Returns the number of Shapes
                |
                |     Returns:
                |         oNbShapes The number of Shapes.

        :rtype: int
        """
        return self.product.GetNumberOfShapes()

    def get_shape_path_name(self, i_shape_name=None) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func GetShapePathName(CATBSTR iShapeName) As CATBSTR
                |
                |     Returns the path name of a shape for a given shape name.
                |
                |     Parameters:
                |
                |         iShapeName
                |             The name of the shape.
                |
                |     Returns:
                |         oShapePathName The path name of the shape.

        :param str i_shape_name:
        :return: str
        """
        return self.product.GetShapePathName(i_shape_name)

    def get_shape_representation(
            self,
            i_load_if_necessary: bool,
            i_shape_name: str,
            i_rep_behavior: int,
            i_context: bool
    ) -> AnyObject:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func GetShapeRepresentation(boolean iLoadIfNecessary,
                | CATBSTR iShapeName,
                | CatRepType iRepBehavior,
                | boolean iContext) As CATBaseDispatch
                |
                |     Retrieves the product's representation with the given
                |     parameters.
                |
                |     Parameters:
                |
                |         iLoadIfNecessary
                |             Parameter to set to True if the master shape representation should
                |             be loaded to determine if it exists, or to False otherwise.
                |
                |         iShapeName
                |             The name of the representation of the product.
                |         iRepBehavior
                |             The behavior of the representation. It can take the values catRep3D
                |             if the representation is a 3D one, catRep2D if the representation is a 2D one,
                |             or catRepText if the representation is a text one.
                |
                |         iContext
                |             A condition to specify if the representation is displayed with the
                |             representation of other products.
                |
                |     Example:
                |
                |          This example retrieves in MSRep the
                |          Engine product's  3D representation named "PART".
                |
                |          Dim MSRep As Object
                |          Set MSRep = Engine.GetMasterShapeRepresentation(True,"PART",catRep3D,TRUE)

        :param bool i_load_if_necessary:
        :param str i_shape_name:
        :param int i_rep_behavior: enum cat_rep_type
        :param bool i_context:
        :return: AnyObject
        """
        return self.product.GetShapeRepresentation(
            i_load_if_necessary,
            i_shape_name,
            i_rep_behavior,
            i_context
        )

    def get_technological_object(self, i_application_type: str) -> AnyObject:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func GetTechnologicalObject(CATBSTR iApplicationType) As
                | CATBaseDispatch
                |
                |     Returns the product's applicative data which type is the given parameter.
                |     The data returned can be either a collection or a simple
                |     object.
                |
                |     Parameters:
                |
                |         iApplicationType
                |             The type of applicative data searched.
                |
                |     Example:
                |
                |           This example retrieves the constraints for the
                |          Engine product.
                |
                |
                |          Dim EngineConstraints As Collection
                |          Set EngineConstraints = Engine.GetTechnologicalObject("Constraints")

        :param str i_application_type:
        :rtype: AnyObject
        """
        return self.product.GetTechnologicalObject(i_application_type)

    def has_a_master_shape_representation(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func HasAMasterShapeRepresentation() As boolean
                |
                |     Returns whether the product has a master shape
                |     representation.
                |     True if the product has a master shape representation.
                |
                |     Example:
                |
                |          This example retrieves in HasMSRep whether the
                |          Engine product has a master shape representation.
                |
                |          HasMSRep = Engine.HasAMasterShapeRepresentation()

        :rtype: bool
        """
        return self.product.HasAMasterShapeRepresentation()

    def has_children(self) -> bool:
        """
        :return: bool
        """

        if self.product.Products.Count > 0:
            return True

        return False

    def has_shape_representation(self, i_shape_name: str, i_rep_behavior: int, i_context: bool) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func HasShapeRepresentation(CATBSTR iShapeName,
                | CatRepType iRepBehavior,
                | boolean iContext) As boolean
                |
                |     Returns whether the product has a representation of the given name with a
                |     given behavior.
                |     True if the product has such a representation.
                |
                |     Parameters:
                |
                |         iShapeName
                |             The name of the representation of the product.
                |         iRepBehavior
                |             The behavior of the representation. It can take the values catRep3D
                |             if the representation is a 3D one, catRep2D if the representation is a 2D one,
                |             or catRepText if the representation is a text one.
                |
                |         iContext
                |             A condition to specify if the representation is displayed with the
                |             representation of other products.
                |
                |     Example:
                |
                |          This example retrieves in HasRep whether the
                |          Engine product has a master shape representation.
                |
                |          HasRep = Engine.HasRepresentation("PART",catRep3D,TRUE)

        :param str i_shape_name:
        :param int i_rep_behavior: enum cat_rep_type
        :param bool i_context:
        :rtype: bool
        """
        return self.product.HasShapeRepresentation(i_shape_name, i_rep_behavior, i_context)

    def is_catproduct(self) -> bool:
        """
        :rtype: bool
        """

        if "catproduct" == self.file_name.rsplit(".")[-1].lower():
            return True

        return False

    def is_catpart(self) -> bool:
        """
        :rtype: bool
        """

        if "catpart" == self.file_name.rsplit(".")[-1].lower():
            return True

        return False

    def path(self) -> Path:
        """

        Returns the pathlib.Path() object of the document fullname.
        example e://users//psr//Parts//MyNiceProduct.CATProduct
        >>> Product.path().name
        >>> # MyNiceProduct.CATProduct
        >>> Product.path().parent
        >>> # e://users//psr//Parts//
        >>> Product.path().suffix
        >>> # .CATProduct
        :rtype: Path
        """

        return Path(self.full_name)

    def remove_master_shape_representation(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub RemoveMasterShapeRepresentation()
                |
                |     Removes the master shape representation from the product. The master shape
                |     representation is the object that gives a geometric shape and allows the
                |     visualization of the product. It can be a CATIA V4 model, a VRML file, or any
                |     other type of document that can be displayed. In a multi representation
                |     context, the master shape representation is the most meaningful representation
                |     of the product according to the user. This is the default shape for the multi
                |     representation.
                |
                |     Note: This master shape representation is optional.
                |
                |     Example:
                |
                |           This example removes the master shape representation of
                |           the
                |          Engine product.
                |
                |
                |          Engine.RemoveMasterShapeRepresentation()

        :rtype: None
        """
        return self.product.RemoveMasterShapeRepresentation()

    def remove_shape_representation(self, i_shape_name: str, i_rep_behavior: int, i_context: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub RemoveShapeRepresentation(CATBSTR iShapeName,
                | CatRepType iRepBehavior,
                | boolean iContext)
                |
                |     Removes a specific representation from the product. A representation is the
                |     object that gives a geometric shape and allows the visualization of the
                |     product.. It can be a CATIA V4 model, a VRML file, or any other type of
                |     document that can be displayed.
                |
                |     Note: This representation is optional.
                |
                |     Parameters:
                |
                |         iShapeName
                |             The name of the representation of the product.
                |         iRepBehavior
                |             The behavior of the representation. It can take the values catRep3D
                |             if the representation is a 3D one, catRep2D if the representation is a 2D one,
                |             or catRepText if the representation is a text one.
                |
                |         iContext
                |             A condition to specify if the representation is displayed with the
                |             representation of other products.
                |
                |     Example:
                |
                |          This example removes the 3D representation named "PART" of the
                |          Engine product.
                |
                |          Engine.RemoveMasterShapeRepresentation
                |         ("PART",catRep3D,TRUE)

        :param str i_shape_name:
        :param int i_rep_behavior: enum cat_rep_type
        :param bool i_context:
        :rtype: None
        """
        return self.product.RemoveShapeRepresentation(i_shape_name, i_rep_behavior, i_context)
        # # # # Autogenerated comment:
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'remove_shape_representation'
        # # vba_code = """
        # # Public Function remove_shape_representation(product)
        # #     Dim iShapeName (2)
        # #     product.RemoveShapeRepresentation iShapeName
        # #     remove_shape_representation = iShapeName
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def update(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub Update()
                |
                |     Updates the product. This update is performed with respect to the part
                |     making the product or to the product's representation. It takes into account
                |     the components of the product at any level
                |
                |     Example:
                |
                |            The following example updates the root product:
                |
                |
                |          Dim RootProduct As Product
                |          Set Rootproduct = productDoc.Product
                |          Rootproduct.Update

        :rtype: None
        """
        return self.product.Update()

    def __repr__(self):
        return f'Product(name="{self.name}")'
