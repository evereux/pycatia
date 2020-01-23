class Analyse:
    """
    Yes, it's spelt correctly. I'm English.

        .. note::
            CAA V5 Visual Basic help

            Represents the analysis object associated with a product.
    """

    def __init__(self, product):
        """

        :param product: the product com object
        """
        self.analyse = product.Analyze

    @property
    def mass(self):
        """
            .. note::

            CAA V5 Visual Basic help

            Property Mass( ) As double (Read Only)

           Returns the product mass value.
            | Example:
            | This example retrieves MassValue from
            | the Analyze object associated with myProduct:
            |    MassValue = myProduct.Analyze.Mass

        :return:
        """
        return self.analyse.Mass

    @property
    def volume(self):
        """

            .. note::

                CAA V5 Visual Basic help

                Property Volume( ) As double (Read Only)

                Returns the product volume value.
                | Example:
                | This example retrieves VolumeValue from
                | the Analyze object associated with myProduct:
                |    VolumeValue = myProduct.Analyze.Volume

        :return:
        """
        return self.analyse.Volume

    @property
    def wet_area(self):
        """

            .. note::

                CAA V5 Visual Basic help

                Property WetArea( ) As double (Read Only) 

                Returns the product volume value.
                | Example:
                | This example retrieves VolumeValue from
                | the Analyze object associated with myProduct:
                |    VolumeValue = myProduct.Analyze.Volume

        :return:
        """
        pass

    def get_gravity_centere(self):
        """

        :return:
        """

        pass

    def get_inertia(self):
        """

        :return:
        """

        pass