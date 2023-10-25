#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.osm_interfaces.scene_product_data import SceneProductData
from pycatia.product_structure_interfaces.product import Product
from pycatia.system_interfaces.any_object import AnyObject


class ProductScene(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     ProductScene
                | 
                | Represent the Product-Scene.
                | A Product-Scene stores a state of a product in a given
                | ProductDocument.
                | 
                | This state is composed of product properties, graphical attibutes, activation
                | status and position for each component of the product.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.product_scene = com_object

    @property
    def type(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Type() As CatSceneType (Read Only)
                | 
                |     Returns the type of the Product-Scene.
                | 
                |     Example:
                | 
                |              This example reads the type of NewSceneDelta
                |              Product-Scene.
                |
                |             Dim type As CatSceneType
                |             type = NewSceneDelta.Type

        :return: enum cat_scene_type
        :rtype: int
        """

        return self.product_scene.Type

    def copy(self, i_type: int) -> 'ProductScene':
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func Copy(CatSceneType iType) As ProductScene
                | 
                |     Creates another Product-Scene from the current one with the possibility to
                |     have a different mode.
                | 
                |     Parameters:
                | 
                |         iType
                |             The Product-Scene type 
                | 
                |     Returns:
                |         The Product-Scene created from the current one. 
                |     Example:
                | 
                |              This example returns whether the CopyScene Product-Scene created
                |              from 
                |             the Configuration1 Product-Scene, with the DELTA
                |             mode.
                |
                |             Dim type As CatSceneType
                |             type = CatSceneTypeDelta
                |             Dim CopyScene As ProductScene
                |             CopyScene = Configuration1.Copy(type)

        :param int i_type: enum cat_scene_type
        :rtype: ProductScene
        """
        return ProductScene(self.product_scene.Copy(i_type))

    def exists_in_scene(self, i_product: Product) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func ExistsInScene(Product iProduct) As boolean
                | 
                |     Returns whether the product has overloaded attributes in the
                |     Product-Scene.
                | 
                |     Parameters:
                | 
                |         iProduct
                |             The product 
                | 
                |     Returns:
                |         True if the Product-Scene overloads some of the product attributes.
                |         
                |     Example:
                | 
                |              This example returns whether the Engine product exists
                |              in
                |             the Configuration1 Product-Scene.
                |             
                | 
                |             ExistsInSc = Configuration1.ExistsInScene(Engine)

        :param Product i_product:
        :rtype: bool
        """
        return self.product_scene.ExistsInScene(i_product.com_object)

    def get_scene_product_data(self, i_product: Product) -> SceneProductData:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetSceneProductData(Product iProduct) As
                | SceneProductData
                | 
                |     Returns the SceneProductData associated to the given product in the
                |     Product-Scene. If it does not exist yet, it is created.
                | 
                |     Parameters:
                | 
                |         iProduct
                |             The product 
                | 
                |     Returns:
                |         The SceneProductData associated to the given product. 
                |     Example:
                | 
                |              This example returns SceneProductData associated to Engine
                |              in
                |             the NewSceneDelta Product-Scene.
                |             
                | 
                |             Dim scenePrd As SceneProductData
                |             type = NewSceneDelta.GetSceneProductData(Engine)

        :param Product i_product:
        :rtype: SceneProductData
        """
        return SceneProductData(self.product_scene.GetSceneProductData(i_product.com_object))

    def __repr__(self):
        return f'ProductScene(name="{self.name}")'
