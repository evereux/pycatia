#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.osm_interfaces.product_scene import ProductScene
from pycatia.system_interfaces.collection import Collection
from pycatia.types.general import cat_variant


class ProductScenes(Collection):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     ProductScenes
                | 
                | A collection of ProductScenes contained in a given
                | ProductDocument.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object, child_object=ProductScene)
        self.product_scenes = com_object

    def add_product_scene_full(self, i_name: str, i_reference_products: tuple) -> ProductScene:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func AddProductSceneFull(CATBSTR iName,
                | CATSafeArrayVariant iReferenceProducts) As ProductScene
                | 
                |     Creates a new FULL scene from a set of products and adds it to the
                |     ProductScenes collection.
                | 
                |     Parameters:
                | 
                |         iName
                |             The name of the new scene 
                |         iReferenceProducts
                |             Products used as root nodes of the new scene 
                | 
                |     Returns:
                |         The created new full scene 
                |     Example:
                | 
                |              This example creates the SpareWheel new scene from the reference
                |              product
                |             FrontRightWheel and adds the scene to the ToolKits
                |             collection.
                |
                |             Dim SpareWheel As ProductScene
                |             Set SpareWheel = ToolKits.AddProductSceneFull("SpareWheel", FrontRightWheel)

        :param str i_name:
        :param tuple i_reference_products:
        :rtype: ProductScene
        """
        return ProductScene(self.product_scenes.AddProductSceneFull(i_name, i_reference_products))

    def add_product_scene_partial(self, i_name: str, i_reference_products: tuple) -> ProductScene:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func AddProductScenePartial(CATBSTR iName,
                | CATSafeArrayVariant iReferenceProducts) As ProductScene
                | 
                |     Creates a new DELTA scene from a set of products and adds it to the
                |     ProductScenes collection.
                | 
                |     Parameters:
                | 
                |         iName
                |             The name of the new scene 
                |         iReferenceProducts
                |             Products used as root nodes of the new scene 
                | 
                |     Returns:
                |         The created new delta scene 
                |     Example:
                | 
                |              This example creates the SpareWheel new scene from the reference
                |              product
                |             FrontRightWheel and adds the scene to the ToolKits
                |             collection.
                |
                |             Dim SpareWheel As ProductScene
                |             Set SpareWheel = ToolKits.AddProductScenePartial("SpareWheel", FrontRightWheel)

        :param str i_name:
        :param tuple i_reference_products:
        :rtype: ProductScene
        """
        return ProductScene(self.product_scenes.AddProductScenePartial(i_name, i_reference_products))

    def item(self, i_index: cat_variant) -> ProductScene:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func Item(CATVariant iIndex) As ProductScene
                | 
                |     Returns a scene using its index or its name from the ProductScenes
                |     collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the ProductScene to retrieve from the
                |             collection of ProductScenes. As a numerics, this index is the rank of the
                |             ProductScene in the collection. The index of the first ProductScene in the
                |             collection is 1, and the index of the last ProductScene is Count. As a string,
                |             it is the name you assigned to the ProductScene. 
                | 
                |     Returns:
                |         The retrieved ProductScene. 
                |     Example:
                | 
                |              This example retrieves in ThisProductScene the ninth
                |              ProductScene,
                |             and in ThatProductScene the ProductScene named
                |             ProductScene3 from the TheProductScenes collection.
                |
                |             Dim ThisProductScene As ProductScene
                |             Set ThisProductScene = TheProductScenes.Item(9)
                |             Dim ThatProductScene As ProductScene
                |             Set ThatProductScene = TheProductScenes.Item("ProductScene3")

        :param cat_variant i_index:
        :rtype: ProductScene
        """
        return ProductScene(self.product_scenes.Item(i_index))

    def remove(self, i_product_scene: ProductScene) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub Remove(ProductScene iProductScene)
                | 
                |     Removes a product-scene from the ProductScenes collection.
                | 
                |     Parameters:
                | 
                |         iScene
                |             The scene to remove. 
                | 
                |     Example:
                | 
                |              This example removes the Engine product-scene from the ToolKits
                |              collection.
                |
                |             ToolKits.Remove Engine

        :param ProductScene i_product_scene:
        :rtype: None
        """
        return self.product_scenes.Remove(i_product_scene.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'remove'
        # # vba_code = """
        # # Public Function remove(product_scenes)
        # #     Dim iProductScene (2)
        # #     product_scenes.Remove iProductScene
        # #     remove = iProductScene
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'ProductScenes(name="{self.name}")'
