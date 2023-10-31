#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.any_object import AnyObject


class WIText(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     WIText

    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.wi_text = com_object

    @property
    def fixed_text(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property FixedText() As CATBSTR
                | 
                |     Returns or sets the value for 'Fixed Text'
                |     Role: Returns or sets the value of 'Fixed Text' to the Activity

        :rtype: str
        """

        return self.wi_text.FixedText

    @fixed_text.setter
    def fixed_text(self, value: str):
        """
        :param str value:
        """

        self.wi_text.FixedText = value

    @property
    def resolved_text(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ResolvedText() As CATBSTR
                | 
                |     Returns or sets the value for 'ResolvedText Text'
                |     Role: Returns or sets the value of 'ResolvedText Text' to the Activity

        :rtype: str
        """

        return self.wi_text.ResolvedText

    @resolved_text.setter
    def resolved_text(self, value: str):
        """
        :param str value:
        """

        self.wi_text.ResolvedText = value

    @property
    def unresolved_text(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property UnresolvedText() As CATBSTR
                | 
                |     Returns or sets the value for 'UnresolvedText Text'
                |     Role: Returns or sets the value of 'UnresolvedText Text' to the Activity

        :rtype: str
        """

        return self.wi_text.UnresolvedText

    @unresolved_text.setter
    def unresolved_text(self, value: str):
        """
        :param str value:
        """

        self.wi_text.UnresolvedText = value

    def get_attribute(self, i_attr_name: str) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetAttribute(CATBSTR iAttrName) As CATBSTR
                | 
                |     This gets the value of the Attribute.
                | 
                |     Parameters:
                | 
                |         iAttrName
                |             The Attribute Name whose value we need to get 
                |         iAttrValue
                |             CATUnicodeString value of the Attribute

        :param str i_attr_name:
        :rtype: str
        """
        return self.wi_text.GetAttribute(i_attr_name)

    def get_geom_associated_to_annotation(self, i_assignment_type: int, io_point_geom: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetGeomAssociatedToAnnotation(ItemAssignmentType
                | iAssignmentType,
                | CATBaseDispatch ioPointGeom)
                | 
                |     Gets the underlying geometry associated to FTA Text Annotation which is
                |     added as an item to operation of one WIText Activity or added as item to a
                |     WIText activity. This should be used in case when FTA Text Annotation is
                |     associated to single geometric entity.
                | 
                |     Parameters:
                | 
                |         iAssignmentType
                |             Point geometry associated to FTA text. 
                |         iAssignmentType
                |             Type of the Assignment (Item to the Process) 
                | 
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on failure

        :param int i_assignment_type: enum item_assignment_type
        :param AnyObject io_point_geom:
        :rtype: None
        """
        return self.wi_text.GetGeomAssociatedToAnnotation(i_assignment_type, io_point_geom.com_object)

    def get_hyper_links(self) -> tuple:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetHyperLinks() As CATSafeArrayVariant
                | 
                |     Retrieves the List of Hyperlinks associated to this
                |     activity
                |     Role: Retrieves the List of Hyperlinks associated to this
                |     activity
                | 
                |     Parameters:
                | 
                |         ioPath
                |             a CATSafeArrayVariant of CATBSTR that has the list of Hyperlinks
                |
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on failure

        :rtype: tuple
        """
        return self.wi_text.GetHyperLinks()

    def set_attribute(self, i_attr_name: str, i_attr_value: str) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetAttribute(CATBSTR iAttrName,
                | CATBSTR iAttrValue)
                | 
                |     This sets the value of the Attribute
                | 
                |     Parameters:
                | 
                |         iAttrName
                |             The Attribute Name whose value we need to get 
                |         iAttrValue
                |             CATUnicodeString value of the Attribute

        :param str i_attr_name:
        :param str i_attr_value:
        :rtype: None
        """
        return self.wi_text.SetAttribute(i_attr_name, i_attr_value)

    def set_hyper_links(self, i_hyperlinks: tuple) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetHyperLinks(CATSafeArrayVariant iHyperlinks)
                | 
                |     Sets a List of Hyperlinks to this activity
                |     Role: Sets the List of Hyperlinks to this activity
                | 
                |     Parameters:
                | 
                |         iPath
                |             a CATSafeArrayVariant of CATBSTR that has the list of Hyperlinks.
                |
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on failure

        :param tuple i_hyperlinks:
        :rtype: None
        """
        return self.wi_text.SetHyperLinks(i_hyperlinks)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_hyper_links'
        # # vba_code = """
        # # Public Function set_hyper_links(wi_text)
        # #     Dim iHyperlinks (2)
        # #     wi_text.SetHyperLinks iHyperlinks
        # #     set_hyper_links = iHyperlinks
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'WIText(name="{self.name}")'
