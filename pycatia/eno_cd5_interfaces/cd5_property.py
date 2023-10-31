#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.any_object import AnyObject


class CD5Property(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     CD5Property
                | 
                | Represents a single property of an ENOVIA V6 object.
                | 
                | Role: It represents a single property tuple of a given object/document already
                | saved into ENOVIA. The purpose of this interface is to get the information of a
                | given property of an ENOVIA V6 object. The properties are accessible through
                | Edit/Properties menu item after user has clicked the ‘More…’
                | button
                | 
                | Example:
                | 
                |       The following example indicates how to retrieve a single CD5Property from
                |       a collection CD5Properties.
                |      
                | 
                |      Dim objCD5Property As CD5Property
                |      Set objCD5Property = objCD5Properties.Item("0")
                |
                | See also:
                |     CD5Properties
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.cd5_property = com_object

    @property
    def property_name(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property PropertyName() As CATBSTR (Read Only)
                | 
                |     Returns (gets) the name of the ENOVIA V6 object property.
                |     This is a readonly property.
                | 
                |     Throws:
                | 
                |         -1641847650 : Connection to ENOVIA V6 is necessary to intialize this option.
                | 
                |     Example:
                | 
                |           The following example retrieves Property Name
                |
                |          oCD5Property.PropertyName

        :rtype: str
        """

        return self.cd5_property.PropertyName

    @property
    def property_value(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property PropertyValue() As CATBSTR (Read Only)
                | 
                |     Returns (gets) the value of the ENOVIA V6 object property.
                |     This is a readonly property.
                | 
                |     Throws:
                | 
                |         -1641847650 : Connection to ENOVIA V6 is necessary to intialize this option.
                | 
                |     Example:
                | 
                |           The following example retrieves Property Value
                |
                |          oCD5Property.PropertyValue

        :rtype: str
        """

        return self.cd5_property.PropertyValue

    def __repr__(self):
        return f'CD5Property(name="{self.name}")'
