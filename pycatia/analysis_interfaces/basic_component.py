#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from typing import TYPE_CHECKING

from pycatia.analysis_interfaces.analysis_entities import AnalysisEntities
from pycatia.analysis_interfaces.analysis_supports import AnalysisSupports
from pycatia.in_interfaces.reference import Reference
from pycatia.product_structure_interfaces.product import Product
from pycatia.product_structure_interfaces.publication import Publication
from pycatia.system_interfaces.any_object import AnyObject
from pycatia.types.general import cat_variant

if TYPE_CHECKING:
    from pycatia.analysis_interfaces.basic_components import BasicComponents


class BasicComponent(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     BasicComponent
                | 
                | Interface designed to manage Analysis Basic Components.
                | 
                | A Basic Component is the low level of physical descriptive data. It is a
                | "brick" dedicated to build the Analysis Entity or an Analysis Set
                | .
                | 
                | A Basic Components can contain several Blocks. A Block is identified by a
                | label. It contains entity data of the same type, organized in superimposed
                | tables.
                | 
                | To create Analysis Entities with a complex structure, we have also created a
                | particular Basic Component dedicated to encapsulate other Basic
                | Components.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.basic_component = com_object

    @property
    def analysis_supports(self) -> AnalysisSupports:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property AnalysisSupports() As AnalysisSupports (Read Only)
                | 
                |     Returns the list of Analysis Supports. The support defines the area on
                |     which the analysis is applied on.

        :rtype: AnalysisSupports
        """

        return AnalysisSupports(self.basic_component.AnalysisSupports)

    @property
    def basic_components(self) -> 'BasicComponents':
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property BasicComponents() As BasicComponents (Read Only)
                | 
                |     Returns the collection of Basic Components agregated by the basic
                |     component. It can be (scalar value, vector, tensor,...). Depending on the type
                |     of the Basic component, the collection can be empty.
                | 
                |     Example:
                | 
                |           This example retrieves Basic components collection 
                | 
                |          
                | 
                |          Dim MyBasicComp As BasicComponent
                |          Dim myBasicComponents As BasicComponents
                |          Set myBasicComponents = MyBasicComp.BasicComponents

        :rtype: BasicComponents
        """
        from pycatia.analysis_interfaces.basic_components import BasicComponents
        return BasicComponents(self.basic_component.BasicComponents)

    @property
    def entities(self) -> AnalysisEntities:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Entities() As AnalysisEntities (Read Only)
                | 
                |     Returns the collection of Entities agregated by the basic component.
                |     Depending on the type of the Basic component,the collection can be
                |     empty.
                | 
                |     Example:
                | 
                |           This example retrieves Basic components collection 
                | 
                |          
                | 
                |          Dim MyBasicComp As BasicComponent
                |          Dim myEntities AnalysisEntities
                |          Set myEntities = MyBasicComp.AnalysisEntities

        :rtype: AnalysisEntities
        """

        return AnalysisEntities(self.basic_component.Entities)

    @property
    def type(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Type() As CATBSTR (Read Only)
                | 
                |     Returns the type of the Basic Component.
                | 
                |     Returns:
                |         The string that represent the Basic Component type.

        :rtype: str
        """

        return self.basic_component.Type

    def add_support_from_product(self, i_product: Product, i_support: Reference) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub AddSupportFromProduct(Product iProduct,
                | Reference iSupport)
                | 
                |     Creates a new support and add it to the description of the basic
                |     component.
                | 
                |     Parameters:
                | 
                |         iProduct
                |             the CATIA Product that represent the object to
                |             linked.
                |         iSupport
                |             the CATIA Reference that represent the object to
                |             linked.
                | 
                |     See also:
                |         Reference, Product

        :param Product i_product:
        :param Reference i_support:
        :rtype: None
        """
        return self.basic_component.AddSupportFromProduct(i_product.com_object, i_support.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'add_support_from_product'
        # # vba_code = """
        # # Public Function add_support_from_product(basic_component)
        # #     Dim iProduct (2)
        # #     basic_component.AddSupportFromProduct iProduct
        # #     add_support_from_product = iProduct
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def add_support_from_publication(self, i_product: Product, i_publication: Publication) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub AddSupportFromPublication(Product iProduct,
                | Publication iPublication)
                | 
                |     Creates a new support and add it to the description of the Basic
                |     Component.
                | 
                |     Parameters:
                | 
                |         iProduct
                |             the CATIA Product that represent the object to
                |             linked.
                |         iPublication
                |             the CATIA Publication that represent the object to
                |             linked.
                | 
                |     See also:
                |         Publication, Product

        :param Product i_product:
        :param Publication i_publication:
        :rtype: None
        """
        return self.basic_component.AddSupportFromPublication(i_product.com_object, i_publication.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'add_support_from_publication'
        # # vba_code = """
        # # Public Function add_support_from_publication(basic_component)
        # #     Dim iProduct (2)
        # #     basic_component.AddSupportFromPublication iProduct
        # #     add_support_from_publication = iProduct
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def add_support_from_reference(self, i_reference: Reference, i_support: Reference) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub AddSupportFromReference(Reference iReference,
                | Reference iSupport)
                | 
                |     Creates a new support and add it to the description of the basic
                |     component.
                | 
                |     Parameters:
                | 
                |         iReference
                |             the CATIA Reference that represent the object to
                |             linked.
                |         iSupport
                |             the CATIA Reference that represent the object to
                |             linked.
                | 
                |     See also:
                |         Reference, Product

        :param Reference i_reference:
        :param Reference i_support:
        :rtype: None
        """
        return self.basic_component.AddSupportFromReference(i_reference.com_object, i_support.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'add_support_from_reference'
        # # vba_code = """
        # # Public Function add_support_from_reference(basic_component)
        # #     Dim iReference (2)
        # #     basic_component.AddSupportFromReference iReference
        # #     add_support_from_reference = iReference
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_columns_number(self, i_label: str) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetColumnsNumber(CATBSTR iLabel) As long
                | 
                |     Return one of the dimensions information of the Basic Component
                |     structure.
                | 
                |     Parameters:
                | 
                |         oColumnsNumber
                |             = Number of Columns.

        :param str i_label:
        :rtype: int
        """
        return self.basic_component.GetColumnsNumber(i_label)

    def get_layers_number(self, i_label: str) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetLayersNumber(CATBSTR iLabel) As long
                | 
                |     Return one of the dimensions information of the Basic Component
                |     structure.
                | 
                |     Parameters:
                | 
                |         oLayersNumber
                |             = Number of Layers.

        :param str i_label:
        :rtype: int
        """
        return self.basic_component.GetLayersNumber(i_label)

    def get_lines_number(self, i_label: str) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetLinesNumber(CATBSTR iLabel) As long
                | 
                |     Return one of the dimensions information of the Basic Component
                |     structure.
                | 
                |     Parameters:
                | 
                |         oLinesNumber
                |             = Number of lines.

        :param str i_label:
        :rtype: int
        """
        return self.basic_component.GetLinesNumber(i_label)

    def get_value(self, i_label: str, i_line_index: int, i_column_index: int, i_layer_index: int) -> cat_variant:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetValue(CATBSTR iLabel,
                | long iLineIndex,
                | long iColumnIndex,
                | long iLayerIndex) As CATVariant
                | 
                |     Return the value corresponding to the given coordinates.
                | 
                |     Parameters:
                | 
                |         iLabel
                |             = Label of the block containing the value.
                |         iLineIndex
                |             = line index of the value.
                |         iColumnIndex
                |             = column index of the value.
                |         iLayerIndex
                |             = layer index of the value.
                |             If the the component has a single value, set these 3 parameters to
                |             0.

        :param str i_label:
        :param int i_line_index:
        :param int i_column_index:
        :param int i_layer_index:
        :rtype: cat_variant
        """
        return self.basic_component.GetValue(i_label, i_line_index, i_column_index, i_layer_index)

    def set_dimensions(self, i_line_count: int, i_column_count: int, i_layer_count: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetDimensions(long iLineCount,
                | long iColumnCount,
                | long iLayerCount)
                | 
                |     Sets the dimensions of the basic component.
                | 
                |     Parameters:
                | 
                |         iLineCount
                |             Number of lines.
                |         iColumnCount
                |             Number of columns.
                |         iLayerCount
                |             Number of layers.

        :param int i_line_count:
        :param int i_column_count:
        :param int i_layer_count:
        :rtype: None
        """
        return self.basic_component.SetDimensions(i_line_count, i_column_count, i_layer_count)

    def set_reference(
            self,
            i_label: str,
            i_line_index: int,
            i_column_index: int,
            i_layer_index: int,
            i_value: Reference) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetReference(CATBSTR iLabel,
                | long iLineIndex,
                | long iColumnIndex,
                | long iLayerIndex,
                | Reference iValue)
                | 
                |     Sets the reference corresponding to the given component.
                | 
                |     Parameters:
                | 
                |         iLabel
                |             The label of the block containing the value.
                |         iLineIndex
                |             The line index of the value.
                |         iColumnIndex
                |             The column index of the value.
                |         iLayerIndex
                |             The layer index of the value.
                |             If the the component has a single value, assign 0 to the 3
                |             parameters.

        :param str i_label:
        :param int i_line_index:
        :param int i_column_index:
        :param int i_layer_index:
        :param Reference i_value:
        :rtype: None
        """
        return self.basic_component.SetReference(
            i_label,
            i_line_index,
            i_column_index,
            i_layer_index,
            i_value.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_reference'
        # # vba_code = """
        # # Public Function set_reference(basic_component)
        # #     Dim iLabel (2)
        # #     basic_component.SetReference iLabel
        # #     set_reference = iLabel
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_value(
            self,
            i_label: str,
            i_line_index: int,
            i_column_index: int,
            i_layer_index: int,
            i_value: cat_variant) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetValue(CATBSTR iLabel,
                | long iLineIndex,
                | long iColumnIndex,
                | long iLayerIndex,
                | CATVariant iValue)
                | 
                |     Set the value corresponding to the given coordinates.
                | 
                |     Parameters:
                | 
                |         iLabel
                |             = Label of the block containing the value.
                |         iLineIndex
                |             = line index of the value.
                |         iColumnIndex
                |             = column index of the value.
                |         iLayerIndex
                |             = layer index of the value.
                |             If the the component has a single value, set these 3 parameters to
                |             0.

        :param str i_label:
        :param int i_line_index:
        :param int i_column_index:
        :param int i_layer_index:
        :param cat_variant i_value:
        :rtype: None
        """
        return self.basic_component.SetValue(
            i_label,
            i_line_index,
            i_column_index,
            i_layer_index,
            i_value
        )
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_value'
        # # vba_code = """
        # # Public Function set_value(basic_component)
        # #     Dim iLabel (2)
        # #     basic_component.SetValue iLabel
        # #     set_value = iLabel
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'BasicComponent(name="{self.name}")'
