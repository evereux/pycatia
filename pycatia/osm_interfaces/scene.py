#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.in_interfaces.move import Move
from pycatia.in_interfaces.position import Position
from pycatia.osm_interfaces.product_scene import ProductScene
from pycatia.product_structure_interfaces.product import Product
from pycatia.system_interfaces.any_object import AnyObject


class Scene(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     Scene
                | 
                | Represent the scene.
                | A scene stores a state of a product in a given
                | ProductDocument.
                | 
                | This state is composed of product properties, graphical attibutes, activation
                | status and position for each component of the product.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.scene = com_object

    def get_definition(self, i_product: Product) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetDefinition(Product iProduct) As CATBSTR
                | 
                |     Returns the product's definition.
                | 
                |     Parameters:
                | 
                |         iProduct
                |             The product. 
                | 
                |     Returns:
                |         The product's definition. 
                |     Example:
                | 
                |              This example retrieves the Engine product's
                |              definition
                |             in the Configuration1 scene.
                |             
                | 
                |             Dim Definition As String
                |             Definition = Configuration1.GetDefinition(Engine)

        :param Product i_product:
        :rtype: str
        """
        return self.scene.GetDefinition(i_product.com_object)

    def get_description(self, i_product: Product) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetDescription(Product iProduct) As CATBSTR
                | 
                |     Returns the product's description.
                | 
                |     Parameters:
                | 
                |         iProduct
                |             The product. 
                | 
                |     Returns:
                |         The product's description. 
                |     Example:
                | 
                |              This example retrieves the Engine product's
                |              description
                |             in the Configuration1 scene.
                |
                |             Dim Description As String
                |             Description = Configuration1.GetDescription(Engine)

        :param Product i_product:
        :rtype: str
        """
        return self.scene.GetDescription(i_product.com_object)

    def get_master_shape_representation(self, i_product: Product, i_load_if_necessary: bool) -> AnyObject:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetMasterShapeRepresentation(Product iProduct,
                | boolean iLoadIfNecessary) As CATBaseDispatch
                | 
                |     Retrieves the product's master shape representation.
                | 
                |     Parameters:
                | 
                |         iProduct.
                |             The product 
                |         iLoadIfNecessary
                |             Parameter to set to True if the master shape representation should
                |             be loaded to determine if it exists, or to False otherwise.
                |
                |     Returns:
                |         The product's master shape representation. 
                |     Example:
                | 
                |              This example retrieves the Engine product's master shape
                |              representation
                |             in the Configuration1 scene.
                |
                |             Dim MSRep As Object
                |             Set MSRep = Configuration1.GetMasterShapeRepresentation(Engine)

        :param Product i_product:
        :param bool i_load_if_necessary:
        :rtype: AnyObject
        """
        return self.scene.GetMasterShapeRepresentation(i_product.com_object, i_load_if_necessary)

    def get_move(self, i_product: Product) -> Move:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetMove(Product iProduct) As Move
                | 
                |     Returns the product's move object. The move object is aggregated by the
                |     product object and itself aggregates a movable object to which you can apply a
                |     move transformation by means of an isometry matrix. It moves your product
                |     master shape representation according to this isometry.
                | 
                |     Parameters:
                | 
                |         iProduct
                |             The product 
                | 
                |     Returns:
                |         The move. 
                |     Example:
                | 
                |              This example retrieves the EngineMove move from the Engine
                |              product
                |             in the Configuration1 scene.
                |
                |             Dim EngineMove As Move
                |             Set EngineMove = Configuration1.GetMove(Engine)

        :param Product i_product:
        :rtype: Move
        """
        return Move(self.scene.GetMove(i_product.com_object))

    def get_nomenclature(self, i_product: Product) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetNomenclature(Product iProduct) As CATBSTR
                | 
                |     Returns the product's nomenclature.
                | 
                |     Parameters:
                | 
                |         iProduct
                |             The product. 
                | 
                |     Returns:
                |         The product's nomenclature. 
                |     Example:
                | 
                |              This example retrieves the Engine product's
                |              nomenclature
                |             in the Configuration1 scene.
                |
                |             Dim Nomenclature As String
                |             Nomenclature = Configuration1.GetNomenclature(Engine)

        :param Product i_product:
        :rtype: str
        """
        return self.scene.GetNomenclature(i_product.com_object)

    def get_part_number(self, i_product: Product) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetPartNumber(Product iProduct) As CATBSTR
                | 
                |     Returns the product's part number.
                | 
                |     Parameters:
                | 
                |         iProduct
                |             The product. 
                | 
                |     Returns:
                |         The product's part number. 
                |     Example:
                | 
                |              This example retrieves the Engine product's part
                |              number
                |             in the Configuration1 scene.
                |
                |             Dim PartNumber As String
                |             PartNumber = Configuration1.GetPartNumber(Engine)

        :param Product i_product:
        :rtype: str
        """
        return self.scene.GetPartNumber(i_product.com_object)

    def get_position(self, i_product: Product) -> Position:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetPosition(Product iProduct) As Position
                | 
                |     Returns the product's position object in the scene. The position object is
                |     the object aggregated by the product object that holds the position of the
                |     master shape representation in the space.
                | 
                |     Parameters:
                | 
                |         iProduct
                |             The product 
                | 
                |     Returns:
                |         The position. 
                |     Example:
                | 
                |              This example retrieves the EnginePosition position from the Engine
                |              product
                |             in the Configuration1 scene.
                |
                |             Dim EnginePosition As Position
                |             Set EnginePosition = Configuration1.GetPosition(Engine)

        :param Product i_product:
        :rtype: Position
        """
        return Position(self.scene.GetPosition(i_product.com_object))

    def get_revision(self, i_product: Product) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetRevision(Product iProduct) As CATBSTR
                | 
                |     Returns the product's revision number.
                | 
                |     Parameters:
                | 
                |         iProduct
                |             The product. 
                | 
                |     Returns:
                |         The product's revision number. 
                |     Example:
                | 
                |              This example retrieves the Engine product's revision
                |              number
                |             in the Configuration1 scene.
                |
                |             Dim Revision As String
                |             Revision = Configuration1.GetRevision(Engine)

        :param Product i_product:
        :rtype: str
        """
        return self.scene.GetRevision(i_product.com_object)

    def get_source(self, i_product: Product) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetSource(Product iProduct) As CatProductSource
                | 
                |     Returns the product's source.
                | 
                |     Parameters:
                | 
                |         iProduct
                |             The product. 
                | 
                |     Returns:
                |         The product's source. 
                |     Example:
                | 
                |              This example retrieves the Engine product's
                |              source
                |             in the Configuration1 scene.
                |
                |             Dim Source
                |             Source = Configuration1.GetSource(Engine)

        :param Product i_product:
        :rtype: enum cat_product_source
        :rtype: int
        """
        return self.scene.GetSource(i_product.com_object)

    def has_a_master_shape_representation(self, i_product: Product) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func HasAMasterShapeRepresentation(Product iProduct) As
                | boolean
                | 
                |     Returns whether the product has a master shape representation in the
                |     scene.
                | 
                |     Parameters:
                | 
                |         iProduct
                |             The product 
                | 
                |     Returns:
                |         True if the product has a master shape representation.
                |         
                |     Example:
                | 
                |              This example returns whether the Engine product has a master shape
                |              representation
                |             in the Configuration1 scene.
                |
                |             HasMSRep = Configuration1.HasAMasterShapeRepresentation(Engine)

        :param Product i_product:
        :rtype: bool
        """
        return self.scene.HasAMasterShapeRepresentation(i_product.com_object)

    def upgrade_to_full(self) -> ProductScene:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func UpgradeToFull() As ProductScene
                | 
                |     Create a ProductScene in Full mode from the current Scene.
                | 
                |     Returns:
                |         The new ProductScene. 
                |     Example:
                | 
                |              This example creates the FullScene ProductScene from the
                |              Configuration1 scene.
                |
                |             Dim FullScene As ProductScene
                |             Set FullScene = Configuration1.UpgradeToFull

        :rtype: ProductScene
        """
        return ProductScene(self.scene.UpgradeToFull())

    def upgrade_to_partial(self) -> ProductScene:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func UpgradeToPartial() As ProductScene
                | 
                |     Create a ProductScene in Partial mode from the current
                |     Scene.
                | 
                |     Returns:
                |         The new ProductScene. 
                |     Example:
                | 
                |              This example creates the PartialScene ProductScene from the
                |              Configuration1 scene.
                |
                |             Dim PartialScene As ProductScene
                |             Set PartialScene = Configuration1.UpgradeToPartial

        :rtype: ProductScene
        """
        return ProductScene(self.scene.UpgradeToPartial())

    def __repr__(self):
        return f'Scene(name="{self.name}")'
