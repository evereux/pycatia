class Product:

    def __init__(self, product):
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

        :param product: Product COM object
        """

        self.product = product

    @property
    def name(self):
        """

        :return:
        """

        return self.product.Name

    @property
    def file_name(self):
        """

        :return:
        """

        return self.product.ReferenceProduct.Parent.Name

    @property
    def part_number(self):
        """

        .. note::
            CAA V5 Visual Basic help

            Property PartNumber( ) As CATBSTR

            Returns or sets the product's part number.
            PartNumber is valid for reference products only.
            Example:
            This example sets the Engine product's part number to A120-253X-7.
                  Engine.PartNumber("A120-253X-7")


        :return:
        """

        return self.product.PartNumber

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

        :return:
        """

        return self.product.revision

    @property
    def definition(self):
        """

        .. note::
            CAA V5 Visual Basic help
            Property Definition( ) As CATBSTR

            Returns or sets the product's definition.
            Definition is valid for reference products only.
            Example:
            This example retrieves the definition of the Engine product in EngineDef.
                  EngineDef = Engine.Definition


        :return: str()
        """

        return self.product.Definition

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

        :return:
        """

        return self.product.DescriptionInst

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

        :return:
        """

        return self.product.DescriptionRef

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

        :return:
        """

        return self.product.Nomenclature

    @property
    def reference_product(self):
        """

        .. note::
            CAA V5 Visual Basic help

            Property ReferenceProduct( ) As Product (Read Only)

            Returns the Reference Product of this instance.

        :return:
        """

        return self.product.ReferenceProduct

    def is_catproduct(self):

        if 'catproduct' == self.file_name.rsplit('.')[1].lower():
            return True

        return False

    def is_catpart(self):

        if 'catpart' == self.file_name.rsplit('.')[1].lower():
            return True

        return False

    def has_children(self):

        if self.product.Products.Count > 0:
            return True

        return False

    def get_children(self):
        """

        :return: list(Product)
        """

        children = list()

        if self.has_children():
            for i in range(self.product.Products.Count):
                child = Product(self.product.Products.Item(i + 1))
                children.append(child)

        return children

    def get_products(self):
        """

        :return: list()
        """
        products = list()

        for i in range(0, self.product.Products.Count):
            product = Product(self.product.Products.Item(i + 1))
            products.append(product)

        return products

    def attributes(self):
        """
        Returns a string describing the products attributes.

        :return:
        """

        return ('<Product> Attributes... \n'
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
                f'Is CATPart:            {self.is_catpart()}\n')

    def __repr__(self):
        return f'<Product  part_number: {self.part_number}, file_name: {self.file_name})'
