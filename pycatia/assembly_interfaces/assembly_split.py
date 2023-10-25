#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.assembly_interfaces.assembly_feature import AssemblyFeature
from pycatia.in_interfaces.reference import Reference
from pycatia.product_structure_interfaces.product import Product


class AssemblySplit(AssemblyFeature):
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
                |                         AssemblySplit
                | 
                | Represents the AssemblySplit object.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.assembly_split = com_object

    @property
    def splitting_component(self) -> Product:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property SplittingComponent() As Product (Read Only)
                | 
                |     Returns the component containing the splitting element.
                | 
                |     Example:
                |         The following example retrieves in sptComponent the splitting component
                |         containing the splitting element of the assembly split
                |         assemblySplit:
                | 
                |          Dim sptComponent As Product
                |          Set sptComponent = assemblySplit.SplittingComponent

        :rtype: Product
        """

        return Product(self.assembly_split.SplittingComponent)

    @property
    def splitting_element(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property SplittingElement() As Reference (Read Only)
                | 
                |     Returns the splitting element.
                | 
                |     Example:
                |         The following example retrieves in sptElement the splitting element of
                |         the assembly split assemblySplit:
                | 
                |          Dim sptElement As Reference
                |          Set sptElement = assemblySplit.SplittingElement

        :rtype: Reference
        """

        return Reference(self.assembly_split.SplittingElement)

    @property
    def splitting_side(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property SplittingSide() As CatSplitSide
                | 
                |     Returns or sets the splitting side. The splitting side is the side of the
                |     split object kept after the split, with respect to the splitting element. A
                |     positive side refers to the split object side shown by the splitting element
                |     normal vector.
                | 
                |     Example:
                |         The following example returns in sptSide the splitting side of the
                |         assembly split assemblySplit, and then sets it to
                |         catPositiveSide:
                | 
                |          Set sptSide = assemblySplit.SplittingSide
                |          assemblySplit.SplittingSide = catPositiveSide

        :return: enum cat_split_side
        :rtype: int
        """

        return self.assembly_split.SplittingSide

    @splitting_side.setter
    def splitting_side(self, value: int):
        """
        :param int value: enum cat_split_side
        """

        self.assembly_split.SplittingSide = value

    def modify_splitting_element(self, i_splitting_element: Reference, i_splitting_elem_comp: Product) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub ModifySplittingElement(Reference iSplittingElement,
                | Product iSplittingElemComp)
                | 
                |     Replaces the splitting element by a new one.
                | 
                |     Parameters:
                | 
                |         iSplittingElement
                |             The new face or plane that will split the current body
                |             
                |         iSplittingElemComp
                |             The component that contains the new splitting element
                |             
                | 
                |     Example:
                |         The following example replaces the existing splitting element of the
                |         assembly split assemblySplit by sptElem contained in the sptComponent splitting
                |         component
                | 
                |          assemblySplit.ModifySplittingElement(sptElem, _
                |                                               sptComponent)

        :param Reference i_splitting_element:
        :param Product i_splitting_elem_comp:
        :rtype: None
        """
        return self.assembly_split.ModifySplittingElement(
            i_splitting_element.com_object,
            i_splitting_elem_comp.com_object
        )
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'modify_splitting_element'
        # # vba_code = """
        # # Public Function modify_splitting_element(assembly_split)
        # #     Dim iSplittingElement (2)
        # #     assembly_split.ModifySplittingElement iSplittingElement
        # #     modify_splitting_element = iSplittingElement
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'AssemblySplit(name="{self.name}")'
