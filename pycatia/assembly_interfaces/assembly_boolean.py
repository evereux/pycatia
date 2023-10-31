#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.assembly_interfaces.assembly_feature import AssemblyFeature
from pycatia.mec_mod_interfaces.body import Body
from pycatia.product_structure_interfaces.product import Product


class AssemblyBoolean(AssemblyFeature):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     CATAssemblyInterfaces.AssemblyFeature
                |                         AssemblyBoolean
                | 
                | Represents the AssemblyBoolean object.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.assembly_boolean = com_object

    @property
    def body(self) -> Body:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Body() As Body (Read Only)
                | 
                |     Returns the operating body.
                | 
                |     Example:
                |         The following example retrieves in opBody the operating body of the
                |         assembly boolean assemblyBool.
                | 
                |          Dim opBody As Body
                |          Set opBody = assemblyBool.Body

        :rtype: Body
        """

        return Body(self.assembly_boolean.Body)

    @property
    def body_component(self) -> Product:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property BodyComponent() As Product (Read Only)
                | 
                |     Returns the component containing the operating body.
                | 
                |     Example:
                |         The following example retrieves in opBodyComp the component that
                |         contains the operating body of the assembly boolean
                |         assemblyBool.
                | 
                |          Dim opBodyComp As Product
                |          Set opBodyComp = assemblyBool.BodyComponent

        :rtype: Product
        """

        return Product(self.assembly_boolean.BodyComponent)

    def __repr__(self):
        return f'AssemblyBoolean(name="{self.name}")'
