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
from pycatia.product_structure_interfaces.product import Product
from pycatia.system_interfaces.any_object import AnyObject


class MachiningProcess(ManufacturingActivity):
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
                |                             MachiningProcess
                | 
                | MachiningProcess defines a set of properties and methods to apply a Machining
                | Process to a geometrical feature (design or manufacturing).
                | It refers to a Machining Process which has been defined in the Machining
                | Process view of a CATProcess file In the VB macro, be sure that the active
                | document is the target document where are located the insertion level and where
                | the instantiated activities will be created
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.machining_process = com_object

    @property
    def insertion_level(self) -> ManufacturingActivity:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property InsertionLevel() As ManufacturingActivity
                | 
                |     This property defines the insertion level in the program receiving the
                |     resulting operations. It can be set to either the Manufacturing Program or one
                |     the Manufacturing Activities of the Manufacturing Program.
                | 
                |     Example:
                |         The following example sets the InsertionLevel property to the first
                |         Manufacturing Program as ManufacturingActivity Activity for the mpReference
                |         MachiningProcess which will be used for the Machining Process
                |         application:
                | 
                |          ...
                |          Dim programReference As ManufacturingActivity
                |          Set programReference = ... 
                |          Dim mpReference As MachiningProcess
                |          Set mpReference = ...
                |          mpReference.InsertionLevel = programReference

        :rtype: ManufacturingActivity
        """

        return ManufacturingActivity(self.machining_process.InsertionLevel)

    @insertion_level.setter
    def insertion_level(self, value: ManufacturingActivity):
        """
        :param ManufacturingActivity value:
        """

        self.machining_process.InsertionLevel = value

    def get_activities(self) -> ManufacturingActivities:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetActivities() As MfgActivities
                | 
                |     This method gets the Manufacturing Activities referenced by the Machining
                |     Process.
                | 
                |     Parameters:
                | 
                |         oMfgActivities
                |             The Manufacturing Activities list

        :rtype: MfgActivities
        """
        return ManufacturingActivities(self.machining_process.GetActivities())

    def insert_activity(self, i_activity_type: str,
                        i_referenced_activity: ManufacturingActivity) -> ManufacturingActivity:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func InsertActivity(CATBSTR iActivityType,
                | ManufacturingActivity iReferencedActivity) As
                | ManufacturingActivity
                | 
                |     This method creates and inserts a Manufacturing Activity in the Machining
                |     Process.
                | 
                |     Parameters:
                | 
                |         iActivityType
                |             The activity to be created type 
                |         iReferencedActivity
                |             The insertion level in the machining process: the machining process
                |             itself to insert at the beginning of the Machining Process
                |             
                |         oManufacturingActivity
                |             The inserted activity
                | 
                |             Example:
                |                 The following example executes the InsertActivity method to add
                |                 a drilling operation to the mpReference
                |                 MachiningProcess
                | 
                |                  ...
                |                  Dim mpReference As MachiningProcess
                |                  Set mpReference = ...
                |                  ...
                |                  Dim iActivityType As CATBSTR
                |                  Set iActivityType = Drilling
                |                  Dim iReferencedActivity As
                |                  CATIAManufacturingActivity
                |                  Set iReferencedActivity = MachiningProcess
                |                  Dim oManufacturingActivity As
                |                  CATIAManufacturingActivity
                |                  mpReference.InsertActivity(iActivityType,iReferencedActivity,oManufacturingActivity)

        :param str i_activity_type:
        :param ManufacturingActivity i_referenced_activity:
        :rtype: ManufacturingActivity
        """
        return ManufacturingActivity(
            self.machining_process.InsertActivity(i_activity_type, i_referenced_activity.com_object))

    def instantiate(self, i_feature: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub Instantiate(AnyObject iFeature)
                | 
                |     This method enables to apply a Machining Process to an any feature. This
                |     one has to be available for all Manufacturing Activities inside the Machining
                |     Process. At the end of the Machining Process application, the InsertionLevel
                |     property is set to the last created Manufacturing Activity in the Manufacturing
                |     program
                | 
                |     Example:
                |         The following example executes the Instantiate method to apply the
                |         mpReference MachiningProcess to a DesignFeature selected
                |         feature
                | 
                |          ...
                |          Dim mpReference As MachiningProcess
                |          Set mpReference = ...
                |          ...
                |          Dim DesignFeature As AnyObject
                |          Set DesignFeature = ...
                |          ...
                |          mpReference.Instantiate(DesignFeature)

        :param AnyObject i_feature:
        :rtype: None
        """
        return self.machining_process.Instantiate(i_feature.com_object)

    def instantiate_in_product_context(self, i_feature: AnyObject, i_product: Product) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub InstantiateInProductContext(AnyObject iFeature,
                | Product iProduct)
                | 
                |     This method enables to apply a Machining Process to a given feature by
                |     taking into account the product from which it belongs to. This one has to be
                |     available for all Manufacturing Activities inside the Machining Process. At the
                |     end of the Machining Process application, the InsertionLevel property is set to
                |     the last created Manufacturing Activity in the Manufacturing
                |     program
                | 
                |     Parameters:
                | 
                |         iFeature
                |             The feature on which the Machining Process is instantiated
                |             
                |         iProduct
                |             The product containing the feature.
                | 
                |             Example:
                |                 The following example executes the Instantiate method to apply
                |                 the mpReference MachiningProcess to a iDesignFeature selected
                |                 feature
                | 
                |                  ...
                |                  Dim mpReference As MachiningProcess
                |                  Set mpReference = ...
                |                  ...
                |                  Dim iDesignFeature As AnyObject
                |                  Set iDesignFeature = ...
                |                  ...
                |                  Dim iProduct As Product
                |                  Set iProduct = ...
                |                  ...
                |                 mpReference.Instantiate(iDesignFeature,iProduct)

        :param AnyObject i_feature:
        :param Product i_product:
        :rtype: None
        """
        return self.machining_process.InstantiateInProductContext(i_feature.com_object, i_product.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'instantiate_in_product_context'
        # # vba_code = """
        # # Public Function instantiate_in_product_context(machining_process)
        # #     Dim iFeature (2)
        # #     machining_process.InstantiateInProductContext iFeature
        # #     instantiate_in_product_context = iFeature
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'MachiningProcess(name="{self.name}")'
