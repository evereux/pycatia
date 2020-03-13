#! /usr/bin/python3.6
# module initially auto generated using V5Automation.chm from CATIA V5 R25


class Products:
    """
        .. note::
            CAA V5 Visual Basic help

                | The collection of the Product objects contained in a given Product
                | object of a ProductDocument object.A Product object can aggregate one
                | or zero Products collection.

    """

    def __init__(self, catia):
        self.products = catia.Products

    def add_component(self, i_reference_product):
        """
        .. note::
            CAA V5 Visual Basic help

                | AddComponent
                | o Func AddComponent(    Product    iReferenceProduct) As Product
                | 
                | Creates a component and adds it to the Products collection. A
                | component is a Product object created from another Product object used
                | as reference.


                | Parameters:
                | iReferenceProduct
                |    The product used as reference


                | Examples:
                | 
                | The following example creates the SpareWheel component from
                | the reference product FrontRightWheel and adds the component
                | to the ToolKits collection.
                | 
                | Dim SpareWheel As Product
                | Set SpareWheel = ToolKits.AddComponent(FrontRightWheel)
                | 
                | 
                | 
        """
        # todo: not yet implemented
        return self.products.AddComponent(i_reference_product)

    def add_components_from_files(self, i_files_list, i_method):
        """
        .. note::
            CAA V5 Visual Basic help

                | AddComponentsFromFiles
                | o Sub AddComponentsFromFiles(    CATSafeArrayVariant    iFilesList,
                |                                  CATBSTR    iMethod)
                | 
                | Creates a component for each file. The components are added to the
                | Products collection.


                | Parameters:
                | iFilesList
                |    The paths of the files used to retrieve the reference or the
                |    shape of th component
                |  
                |  iMethod
                |    A string describing the expected type of the files


        """
        # todo: not yet implemented
        return self.products.AddComponentsFromFiles(i_files_list, i_method)

    def add_external_component(self, i_product_document):
        """
        .. note::
            CAA V5 Visual Basic help

                | AddExternalComponent
                | o Func AddExternalComponent(    Document    iProductDocument) As Product
                | 
                | Creates a component from the root product of  another ProductDocument
                | object. This root product is used as a reference to create the
                | component. The component is added to the Products collection.


                | Parameters:
                | iProductDocument
                |    The product document whose root object is to be used as reference
                |    to create the component


                | Examples:
                | 
                | The following example creates the GearBox component by
                | referencing the GearBoxDocument and adds it
                | to the PowerTrains collection.
                | 
                | Dim GearBox As Product
                | Set GearBox = PowerTrains.AddExternalComponent(GearBoxDocument)
                | 
                | 
                | 
        """
        # todo: not yet implemented
        return self.products.AddExternalComponent(i_product_document)

    def add_new_component(self, i_documen_type, i_part_number):
        """
        .. note::
            CAA V5 Visual Basic help

                | AddNewComponent
                | o Func AddNewComponent(    CATBSTR    iDocumenType,
                |                            CATBSTR    iPartNumber) As Product
                | 
                | Creates a component from the root product of  a new ProductDocument
                | object. This root product is used as a reference to create the
                | component. The component is added to the Products collection.


                | Parameters:
                | iProductDocument
                |    The product document whose root object is to be used as reference
                |    to create the component


                | Examples:
                | 
                | The following example creates the GearBox component by
                | referencing the GearBoxDocument and adds it
                | to the PowerTrains collection.
                | 
                | Dim GearBox As Product
                | Set GearBox = PowerTrains.AddNewComponent(GearBoxDocument, "A120-253X-7")
                | 
                | 
                | 
        """
        # todo: not yet implemented
        return self.products.AddNewComponent(i_documen_type, i_part_number)

    def add_new_product(self, i_part_number):
        """
        .. note::
            CAA V5 Visual Basic help

                | AddNewProduct
                | o Func AddNewProduct(    CATBSTR    iPartNumber) As Product
                | 
                | Creates a Product reference object. This creates a Product reference
                | object and the associated component by specifying its type and adds it
                | to the Products collection.


                | Parameters:
                | iPartNumber
                |    The part number of the product to be created and added to the 
                |    to the collection


                | Examples:
                | 
                | The following example creates the Engine product
                | and adds the created component to the PowerTrains collection.
                | 
                | Dim Engine As Product
                | Set Engine = PowerTrains.AddNewProduct(V6Engine)
                | 
                | 
                | 
        """
        # todo: not yet implemented
        return self.products.AddNewProduct(i_part_number)

    def item(self, i_index):
        """
        .. note::
            CAA V5 Visual Basic help

                | Item
                | o Func Item(    CATVariant    iIndex) As Product
                | 
                | Returns a product from its index in the Products collection.


                | Parameters:
                | iIndex
                |    The index of the product to retrieve in the collection of products.
                |    This index can either be the rank of the product in the collection
                |    or the name you assign to the product.
                |    As a numerics, this index is the rank of the product 
                |    in the collection.
                |    The index of the first product in the collection is 1, and
                |    the index of the last product is Count.
                |    As a string, it is the name you assigned to the product using
                |    the 
                | 
                |  activateLinkAnchor('AnyObject','Name','AnyObject.Name')  property  
                |    Returns:
                |   The retrieved product


                | Examples:
                | 
                | The following example returns in ThisProduct the third product,
                | and in ThatProduct the product named
                | Wheel in the CarParts product collection.
                | 
                | Dim ThisProduct As Product
                | Set ThisProduct = CarParts.Item(3)
                | Dim ThatProduct As Product
                | Set ThatProduct = CarParts.Item("Wheel")
                | 
                | 
                | 
        """
        # todo: not yet implemented
        return self.products.Item(i_index)

    def remove(self, i_index):
        """
        .. note::
            CAA V5 Visual Basic help

                | Remove
                | o Sub Remove(    CATVariant    iIndex)
                | 
                | Removes a product from the Products collection.


                | Parameters:
                | iIndex
                |    The index of the product to remove.
                |    This index can either be the rank of the product in the collection
                |    or the name you assigned to the product.
                |    As a numerics, this index is the rank of the product 
                |    in the collection.
                |    The index of the first product in the collection is 1, and
                |    the index of the last product is Count.
                |    As a string, it is the name you assigned to the product using
                |    the 
                | 
                |  activateLinkAnchor('AnyObject','Name','AnyObject.Name')  property


                | Examples:
                | 
                | The following example removes the sixth product and the product named
                | LeftRearDisc from the Brakes product collection.
                | 
                | Brakes.Remove(6)
                | Brakes.Remove("LeftRearDisc")
                | 
                | 
                | 
        """
        # todo: not yet implemented
        return self.products.Remove(i_index)

    def replace_component(self, i_old_component, i_file_path, i_multi_instances):
        """
        .. note::
            CAA V5 Visual Basic help

                | ReplaceComponent
                | o Func ReplaceComponent(    Product    iOldComponent,
                |                             CATBSTR    iFilePath,
                |                             boolean    iMultiInstances) As Product
                | 
                | Creates a component which replace the given one.


                | Parameters:
                | iOldComponent
                |    The component which will be replaced
                |  
                |  iFilePath
                |    the document to replace with
                |  
                |   iMultiInstances
                |    Parameter to set to True if all instances are to be replaced, or to False otherwise. 
                |    Returns the component replacing iOldComponent
                |  Note:
                |    Part Number conflict will be resolved automatically.


        """
        # todo: not yet implemented
        return self.products.ReplaceComponent(i_old_component, i_file_path, i_multi_instances)

    def replace_product(self, i_old_component, i_new_reference, i_multi_instances):
        """
        .. note::
            CAA V5 Visual Basic help

                | ReplaceProduct
                | o Func ReplaceProduct(    Product    iOldComponent,
                |                           Product    iNewReference,
                |                           boolean    iMultiInstances) As Product
                | 
                | Creates a component which replace the given one.


                | Parameters:
                | iOldComponent
                |    The component which will be replaced
                |  
                |  iNewReference
                |    the reference whom the old copmponent will be reconnected
                |  
                |   iMultiInstances
                |    Parameter to set to True if all instances are to be replaced, or to False otherwise. 
                |    Returns the component replacing iOldComponent


        """
        # todo: not yet implemented
        return self.products.ReplaceProduct(i_old_component, i_new_reference, i_multi_instances)
