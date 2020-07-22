#! usr/bin/python3.6
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.any_object import AnyObject


class SystemConfiguration(AnyObject):
    """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SystemConfiguration
                | 
                | Provides abstractions to resources which depend on the platform or the current
                | configuration.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.system_configuration = com_object

    @property
    def operating_system(self) -> str:
        """
        .. note::
            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property OperatingSystem() As CATBSTR (Read Only)
                | 
                |     Returns a string which identifies the operating system on which the
                |     application is currently running. Examples of identifiers include: intel_a,
                |     solaris_a, aix_a, win_a and hpux_a.
                | 
                |     Parameters:
                | 
                |         oOperatingSystem
                |             The operating system identifier.

        :return: str
        :rtype: str
        """

        return self.system_configuration.OperatingSystem

    @property
    def product_count(self) -> int:
        """
        .. note::
            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property ProductCount() As long (Read Only)
                | 
                |     Returns the number of product names names currently known to the
                |     system.
                | 
                |     Parameters:
                | 
                |         oProductCount
                |             The number of product names currently known to the
                |             system.

        :return: int
        :rtype: int
        """

        return self.system_configuration.ProductCount

    @property
    def release(self) -> int:
        """
        .. note::
            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Release() As long (Read Only)
                | 
                |     Returns the CATIA release number.
                | 
                |     Parameters:
                | 
                |         oVersion
                |             The CATIA release number.

        :return: int
        :rtype: int
        """

        return self.system_configuration.Release

    @property
    def service_pack(self) -> int:
        """
        .. note::
            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property ServicePack() As long (Read Only)
                | 
                |     Returns the CATIA service pack number.
                | 
                |     Parameters:
                | 
                |         oServicePack
                |             The CATIA service pack number.

        :return: int
        :rtype: int
        """

        return self.system_configuration.ServicePack

    @property
    def version(self) -> int:
        """
        .. note::
            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Version() As long (Read Only)
                | 
                |     Returns the CATIA version number (usually version 5).
                | 
                |     Parameters:
                | 
                |         oVersion
                |             The CATIA version.

        :return: int
        :rtype: int
        """

        return self.system_configuration.Version

    def get_product_names(self, io_product_names: tuple) -> None:
        """
        .. note::
            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub GetProductNames(CATSafeArrayVariant ioProductNames)
                | 
                |     Returns the product names of all the licenses currently known to the
                |     system.
                | 
                |     Parameters:
                | 
                |         CATSafeArrayVariant
                |             An properly dimensioned array of strings in which the product names
                |             will be stored.
                | 
                |             Example:
                |                 This example determines if the first product in the list of
                |                 known product names is authorized.
                | 
                |                  Dim SystemConfiguration1 As
                |                  SystemConfiguration
                |                  Set SystemConfiguration1 = CATIA.SystemConfiguration
                |                  ReDim NameArray(SystemConfiguration1.ProductNamesCount)
                |                  SystemConfiguration1.GetProductNames
                |                  NameArray
                |                  MsgBox "IsProductAuthorized for product " & NameArray(0) & " 
                |                  returns " & SystemConfiguration1.IsProductAuthorized(NameArray(0))

        :param tuple io_product_names:
        :return: None
        :rtype: None
        """
        return self.system_configuration.GetProductNames(io_product_names)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_product_names'
        # # vba_code = """
        # # Public Function get_product_names(system_configuration)
        # #     Dim ioProductNames (2)
        # #     system_configuration.GetProductNames ioProductNames
        # #     get_product_names = ioProductNames
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def is_product_authorized(self, i_product_name: str) -> bool:
        """
        .. note::
            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func IsProductAuthorized(CATBSTR iProductName) As boolean
                | 
                |     Returns True if the specified product is authorized, False
                |     otherwise.
                | 
                |     Parameters:
                | 
                |         iProductName
                |             The name of the product to check. 
                |         oAuthorized
                |             A boolean which specifies if the product is
                |             authorized.

        :param str i_product_name:
        :return: bool
        :rtype: bool
        """
        return self.system_configuration.IsProductAuthorized(i_product_name)

    def __repr__(self):
        return f'SystemConfiguration(name="{self.name}")'
