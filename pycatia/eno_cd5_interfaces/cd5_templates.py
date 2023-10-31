#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.eno_cd5_interfaces.cd5_template import CD5Template
from pycatia.system_interfaces.collection import Collection
from pycatia.types.general import cat_variant


class CD5Templates(Collection):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     CD5Templates
                | 
                | Represents a List of all Templates from a Template type.
                | 
                | Example:
                | 
                |       The following example indicates how to retrieve the List of all
                |       Templates.
                |
                |      Dim oTemplates As ENOIACD5Templates
                |      Set oTemplates = oTemplateType.Templates
                |
                | See also:
                |     CD5TemplateType
    
    """

    def __init__(self, com_object):
        super().__init__(com_object, child_object=CD5Template)
        self.cd5_templates = com_object

    def item(self, i_index: cat_variant) -> CD5Template:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func Item(CATVariant iIndex) As CD5Template
                | 
                |     Returns (gets) an item from the list of items.
                | 
                |     Example:
                | 
                |           The following example gets a Template at index 1.
                |
                |          Dim oTemplate As ENOIACD5Template
                |          Set oTemplate = oTemplates.Item(1)

        :param cat_variant i_index:
        :rtype: CD5Template
        """
        return CD5Template(self.cd5_templates.Item(i_index))

    def __repr__(self):
        return f'CD5Templates(name="{self.name}")'
