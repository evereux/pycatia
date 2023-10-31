#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.eno_cd5_interfaces.cd5_templates import CD5Templates
from pycatia.system_interfaces.any_object import AnyObject


class CD5TemplateType(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     CD5TemplateType
                | 
                | Represents a Template Type.
                | 
                | Properties on the object helps the users to get various templates and there
                | possible ENOVIA Types.
                | 
                | Example:
                | 
                |       The following example indicates how to retrieve the template
                |       type.
                |
                |      Dim oTemplateType As ENOIACD5TemplateType
                |      Set oTemplateType = oTemplateTypes.Item(1)
                |
                | See also:
                |     CD5TemplateTypes
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.cd5_template_type = com_object

    @property
    def possible_types(self) -> tuple:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property PossibleTypes() As CATSafeArrayVariant (Read Only)
                | 
                |     Returns (gets) the possible Types from a Template type.
                | 
                |     Example:
                | 
                |           The following example gets Possible ENOVIA Types from a Template
                |           type.
                |
                |          Dim oPossibleTypes As Array
                |          oPossibleTypes = oTemplateType.PossibleTypes

        :rtype: tuple
        """

        return self.cd5_template_type.PossibleTypes

    @property
    def template_type_name(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property TemplateTypeName() As CATBSTR (Read Only)
                | 
                |     Returns (gets) the name of the Template Type.
                | 
                |     Example:
                | 
                |           The following example gets the name of the Template
                |           Type.
                |
                |          Dim oName As CATBSTR
                |          oName = oTemplateType.TemplateTypeName

        :rtype: str
        """

        return self.cd5_template_type.TemplateTypeName

    @property
    def templates(self) -> CD5Templates:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Templates() As CD5Templates (Read Only)
                | 
                |     Returns (gets) the list of Templates from a Template type.
                | 
                |     Example:
                | 
                |           The following example gets Templates.
                |
                |          Dim oTemplates As ENOIACD5Templates
                |          Set oTemplates = oTemplateType.Templates

        :rtype: CD5Templates
        """

        return CD5Templates(self.cd5_template_type.Templates)

    def __repr__(self):
        return f'CD5TemplateType(name="{self.name}")'
