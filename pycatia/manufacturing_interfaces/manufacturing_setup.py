#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.manufacturing_interfaces.manufacturing_activities import ManufacturingActivities
from pycatia.manufacturing_interfaces.manufacturing_activity import ManufacturingActivity
from pycatia.manufacturing_interfaces.manufacturing_machine import ManufacturingMachine
from pycatia.manufacturing_interfaces.manufacturing_machining_axis import ManufacturingMachiningAxis
from pycatia.manufacturing_interfaces.manufacturing_view import ManufacturingView
from pycatia.product_structure_interfaces.product import Product
from pycatia.system_interfaces.any_object import AnyObject
from pycatia.types.general import cat_variant


class ManufacturingSetup(ManufacturingActivity):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     DMAPSInterfaces.Activity
                |                        ManufacturingInterfaces.ManufacturingActivity
                |                             ManufacturingSetup
                | 
                | A ManufacturingSetup for a Manufacturing Document.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.manufacturing_setup = com_object

    @property
    def comment(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Comment() As CATBSTR
                | 
                |     Return the Default Comment of a Manufacturing Setup.
                | 
                |     Example:
                |         The following example return the comment SetupComment of to the
                |         manufacturing setup CurrentSetup
                | 
                |          Set CurrentSetup.Comment

        :rtype: str
        """

        return self.manufacturing_setup.Comment

    @comment.setter
    def comment(self, value: str):
        """
        :param str value:
        """

        self.manufacturing_setup.Comment = value

    @property
    def machine(self) -> ManufacturingMachine:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Machine() As ManufacturingMachine
                | 
                |     Give the Machine linked to a Manufacturing Setup.
                | 
                |     Example:
                |         The following example returns the Machine linked to the manufacturing
                |         setup CurrentSetup
                | 
                |          Set Machine = CurrentSetup.Machine

        :rtype: ManufacturingMachine
        """

        return ManufacturingMachine(self.manufacturing_setup.Machine)

    @machine.setter
    def machine(self, value: ManufacturingMachine):
        """
        :param ManufacturingMachine value:
        """

        self.manufacturing_setup.Machine = value

    @property
    def machining_axis_system(self) -> ManufacturingMachiningAxis:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property MachiningAxisSystem() As
                | ManufacturingMachiningAxis
                | 
                |     Retrieves the Machining Axis system from a Manufacturing
                |     Setup.
                | 
                |     Example:
                |         The following example retrieves the Machining Axis system
                |         oMachiningAxis from the manufacturing setup
                |         CurrentSetup
                | 
                |          Set oMachiningAxis = CurrentSetup.MachiningAxisSystem

        :rtype: ManufacturingMachiningAxis
        """

        return ManufacturingMachiningAxis(self.manufacturing_setup.MachiningAxisSystem)

    @machining_axis_system.setter
    def machining_axis_system(self, value: ManufacturingMachiningAxis):
        """
        :param ManufacturingMachiningAxis value:
        """

        self.manufacturing_setup.MachiningAxisSystem = value

    @property
    def product(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Product(Product iProduct)
                | 
                |     Associate the Product to a Manufacturing Setup.
                | 
                |     Example:
                |         The following example associates the Product iProduct to the
                |         manufacturing setup CurrentSetup
                | 
                |          CurrentSetup.Product = iProduct

        :rtype: None
        """

        return self.manufacturing_setup.Product

    @product.setter
    def product(self, value: Product):
        """
        :param False value:
        """

        self.manufacturing_setup.Product = value.com_object

    @property
    def programs(self) -> ManufacturingActivities:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Programs() As MfgActivities (Read Only)
                | 
                |     Give the List of Programs linked to a Manufacturing Setup.
                | 
                |     Example:
                |         The following example returns the list of Programs ProgramsList linked
                |         to the manufacturing Setup CurrentSetup
                | 
                |          Set ProgramsList = CurrentSetup.Programs

        :rtype: ManufacturingActivities
        """

        return ManufacturingActivities(self.manufacturing_setup.Programs)

    def create_machine(self, i_type_machine: str) -> ManufacturingMachine:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func CreateMachine(CATBSTR iTypeMachine) As
                | ManufacturingMachine
                | 
                |     Initialise the Manufacturing Machine linked to a Manufacturing
                |     Setup.
                | 
                |     Example:
                |         The following example initialise the machine
                |         Mfg3AxisWithTableRotationMachine as Manufacturing Machine in the manufacturing
                |         setup CurrentSetup
                | 
                |          call CurrentSetup.CreateMachine(Mfg3AxisWithTableRotationMachine)

        :param str i_type_machine:
        :rtype: ManufacturingMachine
        """
        return ManufacturingMachine(self.manufacturing_setup.CreateMachine(i_type_machine))

    def design_geometries_count(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func DesignGeometriesCount() As long
                | 
                |     Returns the number of design geometries from a Manufacturing
                |     Setup.
                | 
                |     Parameters:
                | 
                |         oDesignGeometriesListSize
                |             The number of design geometries of this setup 
                | 
                |     Example:
                |         The following example retrieves the number of design geometries of the
                |         setup CurrentSetup in DesignGeometriesListSize.
                | 
                |          Dim CurrentSetup As ManufacturingSetup
                |          Set CurrentSetup = ...
                |          Dim DesignGeometriesListSize As Long
                |          DesignGeometriesListSize = CurrentSetup.DesignGeometriesCount

        :rtype: int
        """
        return self.manufacturing_setup.DesignGeometriesCount()

    def export_cat_setting(self, dir_path: str) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub ExportCATSetting(CATBSTR dirPath)
                | 
                |     ExportCATSetting. Export All Machining CATSetting file to a location in xml format.
                |     dirPath = Absolute path to the location where all settings should be exported.
                |     eg, "D:/dir/" Call on Current Manufacturngsetup

        :param str dir_path:
        :rtype: None
        """
        return self.manufacturing_setup.ExportCATSetting(dir_path)

    def fixture_geometries_count(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func FixtureGeometriesCount() As long
                | 
                |     Returns the number of fixture geometries from a Manufacturing
                |     Setup.
                | 
                |     Parameters:
                | 
                |         oFixtureGeometriesListSize
                |             The number of fixture geometries of this setup 
                | 
                |     Example:
                |         The following example retrieves the number of fixture geometries of the
                |         setup CurrentSetup in FixtureGeometriesListSize.
                | 
                |          Dim CurrentSetup As ManufacturingSetup
                |          Set CurrentSetup = ...
                |          Dim FixtureGeometriesListSize As Long
                |          FixtureGeometriesListSize = CurrentSetup.FixtureGeometriesCount

        :rtype: int
        """
        return self.manufacturing_setup.FixtureGeometriesCount()

    def get_machining_axis_system_name(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetMachiningAxisSystemName() As CATBSTR
                | 
                |     Retrieves the Name of the Machining Axis system from a Manufacturing
                |     Setup.
                | 
                |     Example:
                |         The following example retrieves the Name of the Machining Axis
                |         systemoMachiningAxisSystemName from the manufacturing setup
                |         CurrentSetup
                | 
                |          Set oMachiningAxisSystemName = CurrentSetup.GetMachiningAxisSystemName

        :rtype: str
        """
        return self.manufacturing_setup.GetMachiningAxisSystemName()

    def get_manufacturing_view(self) -> ManufacturingView:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetManufacturingView() As ManufacturingView
                | 
                |     Retrieves the Manufacturing View from a Manufacturing
                |     Setup.
                | 
                |     Example:
                |         The following example retrievec the Manufacturing View MfgView from the
                |         manufacturing setup CurrentSetup
                | 
                |          Set MfgView = CurrentSetup.GetManufacturingView

        :rtype: ManufacturingView
        """
        return ManufacturingView(self.manufacturing_setup.GetManufacturingView())

    def get_part_name(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetPartName() As CATBSTR
                | 
                |     Retrieves the Name of the Design Part from a Manufacturing
                |     Setup.
                | 
                |     Example:
                |         The following example retrieves the Name of the Design PartoPartName
                |         from the manufacturing setup CurrentSetup
                | 
                |          Set oPartName = CurrentSetup.GetPartName

        :rtype: str
        """
        return self.manufacturing_setup.GetPartName()

    def get_product_instance(self) -> Product:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetProductInstance() As Product
                | 
                |     Give the Product of the ProductList linked to a Manufacturing
                |     Setup.
                | 
                |     Example:
                |         The following example returns the Product linked to the manufacturing
                |         setup CurrentSetup
                | 
                |          Set Product = CurrentSetup.GetProductInstance

        :rtype: Product
        """
        return Product(self.manufacturing_setup.GetProductInstance())

    def get_safety_plane(self) -> tuple:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetSafetyPlane() As CATSafeArrayVariant
                | 
                |     Retrieves the Safety Plane from a Manufacturing Setup.
                | 
                |     Example:
                |         The following example retrieves the Safety Plane oMathPLane from the
                |         manufacturing setup CurrentSetup The size of oMathPlane is 9 (origin, first
                |         direction, second direction)
                | 
                |          Set oMathPlane= CurrentSetup.GetSafetyPlane

        :rtype: tuple
        """
        return self.manufacturing_setup.GetSafetyPlane()

    def get_stock_from_setup(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetStockFromSetup(CATBSTR oStockPath)
                | 
                |     Retrieves the path of the Stock file from a Manufacturing
                |     Setup.
                | 
                |     Example:
                |         The following example retrieves the the path of the Stock
                |         fileoStockPath from the manufacturing setup
                |         CurrentSetup
                | 
                |          call CurrentSetup.GetStockFromSetup(oStockPath)

        :rtype: str
        """
        return self.manufacturing_setup.GetStockFromSetup()

    def get_tool_change_point(self) -> tuple:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetToolChangePoint(double oX,
                | double oY,
                | double oZ)
                | 
                |     Get the ToolChange point of the machine linked to a Manufacturing
                |     Setup.
                | 
                |     Example:
                |         The following example gets the point with coordinates X,Y,Z as
                |         ToolChangePoint in the manufacturing setup
                |         CurrentSetup
                | 
                |          call CurrentSetup.GetToolChangePoint(X,Y,Z)

        :rtype: tuple
        """
        return self.manufacturing_setup.GetToolChangePoint()

    def import_cat_setting(self, xml_file_path: str) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub ImportCATSetting(CATBSTR XMLFilePath)
                | 
                |     ImportCATSetting. Import the CATSetting in xml format from a specified location.
                |     XMLFilePath = Path to the xml file.
                |     eg, "D:/dirs/settings.xml" Call on Current Manufacturngsetup

        :param str xml_file_path:
        :rtype: None
        """
        return self.manufacturing_setup.ImportCATSetting(xml_file_path)

    def in_process_model_bodies_count(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func InProcessModelBodiesCount() As long
                | 
                |     Returns the number of In Process Model Bodies from a Manufacturing
                |     Setup.
                | 
                |     Parameters:
                | 
                |         oIPMBodiesListSize
                |             The number of In Process Model Bodies of this setup
                |             
                | 
                |     Example:
                |         The following example retrieves the number of In Process Model Bodies
                |         of the setup CurrentSetup in IPMBodiesListSize.
                | 
                |          Dim CurrentSetup As ManufacturingSetup
                |          Set CurrentSetup = ...
                |          Dim IPMBodiesListSize As Long
                |          IPMBodiesListSize = CurrentSetup.InProcessModelBodiesCount

        :rtype: int
        """
        return self.manufacturing_setup.InProcessModelBodiesCount()

    def list_design_geometries(self, o_list_of_design_geometries: tuple) -> cat_variant:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub ListDesignGeometries(CATSafeArrayVariant
                | oListOfDesignGeometries)
                | 
                |     Retrieves the design geometries list from a Manufacturing Setup. Each of
                |     these geometries may be either a Product or a Body.
                | 
                |     Parameters:
                | 
                |         oListOfDesignGeometries
                |             The retrieved list.
                |             The array must be previously initialized using the
                |             
                | 
                |         DesignGeometriesCount method. 
                | 
                | Example:
                |     The following example retrieves the design geometries list of the
                |     manufacturing setup CurrentSetup in
                |     ListOfDesignGeometries.
                | 
                |      Dim CurrentSetup As ManufacturingSetup
                |      Set CurrentSetup = ...
                |      Dim DesignGeometriesListSize As Long
                |      DesignGeometriesListSize = CurrentSetup.DesignGeometriesCount
                |      If DesignGeometriesListSize > 0 Then
                |        Dim ListOfDesignGeometries() As Variant
                |        Redim
                |        ListOfDesignGeometries(DesignGeometriesListSize-1)
                |       CurrentSetup.ListDesignGeometries(ListOfDesignGeometries)
                |      End If

        :param tuple o_list_of_design_geometries:
        :rtype: cat_variant
        """
        return self.manufacturing_setup.ListDesignGeometries(o_list_of_design_geometries)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'list_design_geometries'
        # # vba_code = """
        # # Public Function list_design_geometries(manufacturing_setup)
        # #     Dim oListOfDesignGeometries (2)
        # #     manufacturing_setup.ListDesignGeometries oListOfDesignGeometries
        # #     list_design_geometries = oListOfDesignGeometries
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def list_design_geometries_products(self, o_list_of_design_geometries_products: tuple) -> cat_variant:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub ListDesignGeometriesProducts(CATSafeArrayVariant
                | oListOfDesignGeometriesProducts)
                | 
                |     Retrieves the design geometries products list from a Manufacturing Setup.
                |     Each of these geometries may be either a Product or a
                |     Body.
                | 
                |     Parameters:
                | 
                |         oListOfDesignGeometriesProducts
                |             The retrieved list.
                |             The array must be previously initialized using the
                |             
                |         DesignGeometriesCount method.
                | 
                | Example:
                |     The following example retrieves the design geometries list of the
                |     manufacturing setup CurrentSetup in
                |     ListOfDesignGeometriesProducts.
                | 
                |      Dim CurrentSetup As ManufacturingSetup
                |      Set CurrentSetup = ...
                |      Dim DesignGeometriesListSize As Long
                |      DesignGeometriesListSize = CurrentSetup.DesignGeometriesCount
                |      If DesignGeometriesListSize > 0 Then
                |        Dim ListOfDesignGeometries() As Variant
                |        Redim
                |        ListOfDesignGeometries(DesignGeometriesListSize-1)
                |       CurrentSetup.ListDesignGeometriesProducts(ListOfDesignGeometriesProducts)
                |      End If

        :param tuple o_list_of_design_geometries_products:
        :rtype: cat_variant
        """
        return self.manufacturing_setup.ListDesignGeometriesProducts(o_list_of_design_geometries_products)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'list_design_geometries_products'
        # # vba_code = """
        # # Public Function list_design_geometries_products(manufacturing_setup)
        # #     Dim oListOfDesignGeometriesProducts (2)
        # #     manufacturing_setup.ListDesignGeometriesProducts oListOfDesignGeometriesProducts
        # #     list_design_geometries_products = oListOfDesignGeometriesProducts
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def list_fixture_geometries(self, o_list_of_fixture_geometries: tuple) -> cat_variant:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub ListFixtureGeometries(CATSafeArrayVariant
                | oListOfFixtureGeometries)
                | 
                |     Retrieves the fixture geometries list from a Manufacturing Setup. Each of
                |     these geometries may be either a Product or a Body.
                | 
                |     Parameters:
                | 
                |         oListOfFixtureGeometries
                |             The retrieved list.
                |             The array must be previously initialized using the
                |             
                | 
                |         FixtureGeometriesCount method. 
                | 
                | Example:
                |     The following example retrieves the fixture geometries list of the
                |     manufacturing setup CurrentSetup in
                |     ListOfFixtureGeometries.
                | 
                |      Dim CurrentSetup As ManufacturingSetup
                |      Set CurrentSetup = ...
                |      Dim FixtureGeometriesListSize As Long
                |      FixtureGeometriesListSize = CurrentSetup.FixtureGeometriesCount
                |      If FixtureGeometriesListSize > 0 Then
                |        Dim ListOfFixtureGeometries() As Variant
                |        Redim
                |        ListOfFixtureGeometries(FixtureGeometriesListSize-1)
                |       CurrentSetup.ListFixtureGeometries(ListOfFixtureGeometries)
                |      End If

        :param tuple o_list_of_fixture_geometries:
        :rtype: cat_variant
        """
        return self.manufacturing_setup.ListFixtureGeometries(o_list_of_fixture_geometries)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'list_fixture_geometries'
        # # vba_code = """
        # # Public Function list_fixture_geometries(manufacturing_setup)
        # #     Dim oListOfFixtureGeometries (2)
        # #     manufacturing_setup.ListFixtureGeometries oListOfFixtureGeometries
        # #     list_fixture_geometries = oListOfFixtureGeometries
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def list_fixture_geometries_products(self, o_list_of_fixture_geometries_products: tuple) -> cat_variant:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub ListFixtureGeometriesProducts(CATSafeArrayVariant
                | oListOfFixtureGeometriesProducts)
                | 
                |     Retrieves the Fixture geometries products list from a Manufacturing Setup.
                |     Each of these geometries may be either a Product or a
                |     Body.
                | 
                |     Parameters:
                | 
                |         oListOfFixtureGeometriesProducts
                |             The retrieved list.
                |             The array must be previously initialized using the
                |
                |         FixtureGeometriesCount method. 
                | 
                | Example:
                |     The following example retrieves the Fixture geometries list of the
                |     manufacturing setup CurrentSetup in
                |     ListOfFixtureGeometriesProducts.
                | 
                |      Dim CurrentSetup As ManufacturingSetup
                |      Set CurrentSetup = ...
                |      Dim FixtureGeometriesListSize As Long
                |      FixtureGeometriesListSize = CurrentSetup.FixtureGeometriesCount
                |      If FixtureGeometriesListSize > 0 Then
                |        Dim ListOfFixtureGeometries() As Variant
                |        Redim
                |        ListOfFixtureGeometries(FixtureGeometriesListSize-1)
                |       CurrentSetup.ListFixtureGeometriesProducts(ListOfFixtureGeometriesProducts)
                |      End If

        :param tuple o_list_of_fixture_geometries_products:
        :rtype: cat_variant
        """
        return self.manufacturing_setup.ListFixtureGeometriesProducts(o_list_of_fixture_geometries_products)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'list_fixture_geometries_products'
        # # vba_code = """
        # # Public Function list_fixture_geometries_products(manufacturing_setup)
        # #     Dim oListOfFixtureGeometriesProducts (2)
        # #     manufacturing_setup.ListFixtureGeometriesProducts oListOfFixtureGeometriesProducts
        # #     list_fixture_geometries_products = oListOfFixtureGeometriesProducts
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def list_in_process_model_bodies(self, o_list_of_ipm_bodies: tuple) -> cat_variant:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub ListInProcessModelBodies(CATSafeArrayVariant
                | oListOfIPMBodies)
                | 
                |     Retrieves the In Process Model Bodies list from a Manufacturing
                |     Setup.
                | 
                |     Parameters:
                | 
                |         oListOfIPMBodies
                |             The retrieved list.
                |             The array must be previously initialized using the
                |
                |         InProcessModelBodiesCount method. 
                | 
                | Example:
                |     The following example retrieves the In Process Model Bodies list of the
                |     manufacturing setup CurrentSetup in ListOfIPMBodies.
                | 
                |      Dim CurrentSetup As ManufacturingSetup
                |      Set CurrentSetup = ...
                |      Dim IPMBodiesListSize As Long
                |      IPMBodiesListSize = CurrentSetup.InProcessModelBodiesCount
                |      If IPMBodiesListSize > 0 Then
                |        Dim ListOfIPMBodies() As Variant
                |        Redim ListOfIPMBodies(IPMBodiesListSize-1)
                |        CurrentSetup.ListInProcessModelBodies(ListOfIPMBodies)
                |      End If

        :param tuple o_list_of_ipm_bodies:
        :rtype: cat_variant
        """
        return self.manufacturing_setup.ListInProcessModelBodies(o_list_of_ipm_bodies)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'list_in_process_model_bodies'
        # # vba_code = """
        # # Public Function list_in_process_model_bodies(manufacturing_setup)
        # #     Dim oListOfIPMBodies (2)
        # #     manufacturing_setup.ListInProcessModelBodies oListOfIPMBodies
        # #     list_in_process_model_bodies = oListOfIPMBodies
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def list_stock_geometries(self, o_list_of_stock_geometries: tuple) -> cat_variant:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub ListStockGeometries(CATSafeArrayVariant
                | oListOfStockGeometries)
                | 
                |     Retrieves the stock geometries list from a Manufacturing Setup. Each of
                |     these geometries may be either a Product or a Body.
                | 
                |     Parameters:
                | 
                |         oListOfStockGeometries
                |             The retrieved list.
                |             The array must be previously initialized using the
                |             
                | 
                |         StockGeometriesCount method. 
                | 
                | Example:
                |     The following example retrieves the stock geometries list of the
                |     manufacturing setup CurrentSetup in ListOfStockGeometries.
                | 
                |      Dim CurrentSetup As ManufacturingSetup
                |      Set CurrentSetup = ...
                |      Dim StockGeometriesListSize As Long
                |      StockGeometriesListSize = CurrentSetup.StockGeometriesCount
                |      If StockGeometriesListSize > 0 Then
                |        Dim ListOfStockGeometries() As Variant
                |        Redim ListOfStockGeometries(StockGeometriesListSize-1)
                |        CurrentSetup.ListStockGeometries(ListOfStockGeometries)
                |      End If

        :param tuple o_list_of_stock_geometries:
        :rtype: cat_variant
        """
        return self.manufacturing_setup.ListStockGeometries(o_list_of_stock_geometries)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'list_stock_geometries'
        # # vba_code = """
        # # Public Function list_stock_geometries(manufacturing_setup)
        # #     Dim oListOfStockGeometries (2)
        # #     manufacturing_setup.ListStockGeometries oListOfStockGeometries
        # #     list_stock_geometries = oListOfStockGeometries
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def list_stock_geometries_products(self, o_list_of_stock_geometries_products: tuple) -> cat_variant:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub ListStockGeometriesProducts(CATSafeArrayVariant
                | oListOfStockGeometriesProducts)
                | 
                |     Retrieves the Stock geometries products list from a Manufacturing Setup.
                |     Each of these geometries may be either a Product or a
                |     Body.
                | 
                |     Parameters:
                | 
                |         oListOfStockGeometriesProducts
                |             The retrieved list.
                |             The array must be previously initialized using the
                |
                |         StockGeometriesCount method. 
                | 
                | Example:
                |     The following example retrieves the Stock geometries list of the
                |     manufacturing setup CurrentSetup in
                |     ListOfStockGeometriesProducts.
                | 
                |      Dim CurrentSetup As ManufacturingSetup
                |      Set CurrentSetup = ...
                |      Dim StockGeometriesListSize As Long
                |      StockGeometriesListSize = CurrentSetup.StockGeometriesCount
                |      If StockGeometriesListSize > 0 Then
                |        Dim ListOfStockGeometries() As Variant
                |        Redim ListOfStockGeometries(StockGeometriesListSize-1)
                |       CurrentSetup.ListStockGeometriesProducts(ListOfStockGeometriesProducts)
                |      End If

        :param tuple o_list_of_stock_geometries_products:
        :rtype: cat_variant
        """
        return self.manufacturing_setup.ListStockGeometriesProducts(o_list_of_stock_geometries_products)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'list_stock_geometries_products'
        # # vba_code = """
        # # Public Function list_stock_geometries_products(manufacturing_setup)
        # #     Dim oListOfStockGeometriesProducts (2)
        # #     manufacturing_setup.ListStockGeometriesProducts oListOfStockGeometriesProducts
        # #     list_stock_geometries_products = oListOfStockGeometriesProducts
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def read_mfg_data(self, i_file_name: str, i_ncmillset: tuple) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub ReadMfgData(CATBSTR iFileName,
                | CATSafeArrayVariant iNCMILLSET)
                | 
                |     ReadMfgData. Read Manufacturing V4 data.
                |     iFileName = Path for V4 product
                |     iNCMILLSET = NC sets Acts Same as command "Read Manufacturing data from V4 model"
                 |    in NC Manufacturing Review workbench Call on Current Manufacturngsetup


        :param str i_file_name:
        :param tuple i_ncmillset:
        :rtype: None
        """
        return self.manufacturing_setup.ReadMfgData(i_file_name, i_ncmillset)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'read_mfg_data'
        # # vba_code = """
        # # Public Function read_mfg_data(manufacturing_setup)
        # #     Dim iFileName (2)
        # #     manufacturing_setup.ReadMfgData iFileName
        # #     read_mfg_data = iFileName
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_design_part(self, i_part: AnyObject, i_product: Product) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetDesignPart(AnyObject iPart,
                | Product iProduct)
                | 
                |     Associates the design part to a Manufacturing Setup.
                |     The part must be a Body feature (Geometrical Set, Ordered Geometrical Set,
                |     PartBody, Body.n)
                | 
                |     Example:
                |         The following example associates the part iPart belonging to the
                |         Product iProduct to the manufacturing setup
                |         CurrentSetup
                | 
                |          call CurrentSetup.SetPart(iPart,iProduct)

        :param AnyObject i_part:
        :param Product i_product:
        :rtype: None
        """
        return self.manufacturing_setup.SetDesignPart(i_part.com_object, i_product.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_design_part'
        # # vba_code = """
        # # Public Function set_design_part(manufacturing_setup)
        # #     Dim iPart (2)
        # #     manufacturing_setup.SetDesignPart iPart
        # #     set_design_part = iPart
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_product_and_reconciliate(self, i_product: Product) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetProductAndReconciliate(Product iProduct)
                | 
                |     Associate the Product to a Manufacturing Setup and reconciliate
                |     links.
                | 
                |     Example:
                |         The following example associates the Product iProduct to the
                |         manufacturing setup CurrentSetup
                | 
                |          call CurrentSetup.SetProductAndReconciliate(iProduct)

        :param Product i_product:
        :rtype: None
        """
        return self.manufacturing_setup.SetProductAndReconciliate(i_product.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_product_and_reconciliate'
        # # vba_code = """
        # # Public Function set_product_and_reconciliate(manufacturing_setup)
        # #     Dim iProduct (2)
        # #     manufacturing_setup.SetProductAndReconciliate iProduct
        # #     set_product_and_reconciliate = iProduct
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_safety_plane(self, i_safety_plane: AnyObject, i_product: Product) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetSafetyPlane(AnyObject iSafetyPlane,
                | Product iProduct)
                | 
                |     Associates a Safety Plane to a Manufacturing Setup.
                | 
                |     Example:
                |         The following example associates the Safety Plane iSafetyPlane
                |         belonging to the Product iProduct to the manufacturing setup
                |         CurrentSetup
                | 
                |          call
                |          CurrentSetup.SetSafetyPlane(iSafetyPlane,iProduct)

        :param AnyObject i_safety_plane:
        :param Product i_product:
        :rtype: None
        """
        return self.manufacturing_setup.SetSafetyPlane(i_safety_plane.com_object, i_product.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_safety_plane'
        # # vba_code = """
        # # Public Function set_safety_plane(manufacturing_setup)
        # #     Dim iSafetyPlane (2)
        # #     manufacturing_setup.SetSafetyPlane iSafetyPlane
        # #     set_safety_plane = iSafetyPlane
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_stock(self, i_stock: AnyObject, i_product: Product) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetStock(AnyObject iStock,
                | Product iProduct)
                | 
                |     Associates a stock to a Manufacturing Setup.
                |     The stock must be either a Body feature (Geometrical Set, Ordered
                |     Geometrical Set, PartBody, Body.n) either a CGR product.
                | 
                |     Example:
                |         The following example associates the stock iStock belonging to the
                |         Product iProduct to the manufacturing setup
                |         CurrentSetup
                | 
                |          call CurrentSetup.SetStock(iStock,iProduct)

        :param AnyObject i_stock:
        :param Product i_product:
        :rtype: None
        """
        return self.manufacturing_setup.SetStock(i_stock.com_object, i_product.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_stock'
        # # vba_code = """
        # # Public Function set_stock(manufacturing_setup)
        # #     Dim iStock (2)
        # #     manufacturing_setup.SetStock iStock
        # #     set_stock = iStock
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_tool_change_point(self, i_x: float, i_y: float, i_z: float) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetToolChangePoint(double iX,
                | double iY,
                | double iZ)
                | 
                |     Initialise the ToolChange point of the machine linked to a Manufacturing
                |     Setup.
                | 
                |     Example:
                |         The following example initialise the point with coordinates X,Y,Z as
                |         ToolChangePoint in the manufacturing setup
                |         CurrentSetup
                | 
                |          call CurrentSetup.SetToolChangePoint(X,Y,Z)

        :param float i_x:
        :param float i_y:
        :param float i_z:
        :rtype: None
        """
        return self.manufacturing_setup.SetToolChangePoint(i_x, i_y, i_z)

    def set_tool_change_point_by_name(self, i_point_name: str) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetToolChangePointByName(CATBSTR iPointName)
                | 
                |     Initialise the ToolChange point of the machine linked to a Manufacturing
                |     Setup.
                | 
                |     Example:
                |         The following example initialise the point PT23 as ToolChangePoint in
                |         the manufacturing setup CurrentSetup
                | 
                |          call CurrentSetup.SetToolChangePointByName(PT23)

        :param str i_point_name:
        :rtype: None
        """
        return self.manufacturing_setup.SetToolChangePointByName(i_point_name)

    def stock_geometries_count(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func StockGeometriesCount() As long
                | 
                |     Returns the number of stock geometries from a Manufacturing
                |     Setup.
                | 
                |     Parameters:
                | 
                |         oStockGeometriesListSize
                |             The number of stock geometries of this setup 
                | 
                |     Example:
                |         The following example retrieves the number of stock geometries of the
                |         setup CurrentSetup in StockGeometriesListSize.
                | 
                |          Dim CurrentSetup As ManufacturingSetup
                |          Set CurrentSetup = ...
                |          Dim StockGeometriesListSize As Long
                |          StockGeometriesListSize = CurrentSetup.StockGeometriesCount

        :rtype: int
        """
        return self.manufacturing_setup.StockGeometriesCount()

    def __repr__(self):
        return f'ManufacturingSetup(name="{self.name}")'
