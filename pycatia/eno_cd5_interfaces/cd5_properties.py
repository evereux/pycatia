#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.eno_cd5_interfaces.cd5_property import CD5Property
from pycatia.system_interfaces.collection import Collection
from pycatia.types.general import cat_variant


class CD5Properties(Collection):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     CD5Properties
                | 
                | Represents a collection of all the properties of an ENOVIA V6
                | object.
                | 
                | Role: It represents all the properties of a given object/document already saved
                | into ENOVIA. The purpose of this interface is to get a collection of an ENOVIA
                | V6 object properties. The properties are accessible through Edit/Properties
                | menu item after user has clicked the ‘More…’ button It is managed by
                | CD5Engine.
                | 
                | Example:
                | 
                |       The following example indicates how to retrieve CD5Properties from ENOVIA
                |       V6 Integration Engine.
                |      
                | 
                |      Dim objCD5Properties As CD5Properties
                |      'To get properties of regular documents
                |      Set objCD5Properties = oCD5Engine.GetPropertiesOfDocument(objCATIADocument)
                |      'To get properties of Embedded Component
                |      Set objCD5Properties = oCD5Engine.GetPropertiesOfDocument(objCATIADocument, "Embedded_Component_Name")
                |
                | See also:
                |     CD5Engine, CD5Property
    
    """

    def __init__(self, com_object):
        super().__init__(com_object, child_object=CD5Property)
        self.cd5_properties = com_object

    def item(self, i_index: cat_variant) -> CD5Property:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func Item(CATVariant iIndex) As CD5Property
                | 
                |     Returns ENOVIA V6 object property specified by 1 based index. That is, 1th
                |     index is the first property ergo last property is (Total Count)th
                |     Index
                | 
                |     Throws:
                | 
                |         -1641847650 : Connection to ENOVIA V6 is necessary to intialize this option.
                | 
                |     Example:
                | 
                |           The following example shows how to retrieve a single property from
                |           the collection of all properties.
                |
                |          Dim objCD5Property As CD5Property
                |          Set objCD5Property = objCD5Properties.Item(1)

        :param cat_variant i_index:
        :rtype: CD5Property
        """
        return CD5Property(self.cd5_properties.Item(i_index))

    def __repr__(self):
        return f'CD5Properties(name="{self.name}")'
