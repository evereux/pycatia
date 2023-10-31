#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.eno_cd5_interfaces.cd5_template_type import CD5TemplateType
from pycatia.system_interfaces.collection import Collection
from pycatia.types.general import cat_variant


class CD5TemplateTypes(Collection):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     CD5TemplateTypes
                | 
                | Represents a List of all Template types.
                | 
                | Example:
                | 
                |       The following example indicates how to retrieve List of all Template
                |       types.
                |
                |      Dim oCD5Engine As CD5EngineV6R2015
                |      Set oCD5Engine = CATIA.GetItem("CD5EngineV6R2015")
                |      Dim oTemplateTypes As ENOIACD5TemplateTypes
                |      Set oTemplateTypes = oCD5Engine.TemplateTypes
                |
                | See also:
                |     CD5EngineV6R2015
    
    """

    def __init__(self, com_object):
        super().__init__(com_object, child_object=CD5TemplateType)
        self.cd5_template_types = com_object

    def item(self, i_index: cat_variant) -> CD5TemplateType:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func Item(CATVariant iIndex) As CD5TemplateType
                | 
                |     Returns (gets) an item from the list of items.
                | 
                |     Example:
                | 
                |           The following example gets a Template Type at index
                |           1.
                |
                |          Dim oTemplateType As ENOIACD5TemplateType
                |          Set oTemplateType = oTemplateTypes.Item(1)

        :param cat_variant i_index:
        :rtype: CD5TemplateType
        """
        return CD5TemplateType(self.cd5_template_types.Item(i_index))

    def __repr__(self):
        return f'CD5TemplateTypes(name="{self.name}")'
