#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.any_object import AnyObject


class SelectionSets(AnyObject):

    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SelectionSets
                | 
                | Interface to manage the Selection Sets in a document.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.selection_sets = com_object

    def add_cso_into_selection_set(self, i_sel_set_name: str) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub AddCSOIntoSelectionSet(CATBSTR iSelSetName)
                | 
                |     Adds CSO's content in a Selection Set.
                | 
                |     Parameters:
                | 
                |         iSelSetName
                |             The name of the Selection Set in wich the CSO has to be added.
                |             
                | 
                |     Returns:
                |         The error code of function :
                | 
                |             S_OK if the content of the CSO is added
                |             E_FAIL if the content of the CSO is not added

        :param str i_sel_set_name:
        :rtype: None
        """
        return self.selection_sets.AddCSOIntoSelectionSet(i_sel_set_name)

    def create_selection_set(self, i_sel_set_name: str) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub CreateSelectionSet(CATBSTR iSelSetName)
                | 
                |     Creates a new Selection Set.
                |     Role: This method creates a new Selection Set.
                | 
                |     Parameters:
                | 
                |         iSelSetName
                |             The name of Selection Set to create. 
                | 
                |     Returns:
                |         The error code of function :
                | 
                |             S_OK if the Selection Set is created
                |             E_FAIL if a problem occurred

        :param str i_sel_set_name:
        :rtype: None
        """
        return self.selection_sets.CreateSelectionSet(i_sel_set_name)

    def delete_selection_set(self, i_sel_set_name: str) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub DeleteSelectionSet(CATBSTR iSelSetName)
                | 
                |     Deletes a Selection Set.
                |     Role: This method removes a Selection Set and all its
                |     content.
                | 
                |     Parameters:
                | 
                |         iSelSetName
                |             The Selection Set to delete. 
                | 
                |     Returns:
                |         The error code of function :
                | 
                |             S_OK if the method succeeded
                |             E_FAIL if a problem occurred

        :param str i_sel_set_name:
        :rtype: None
        """
        return self.selection_sets.DeleteSelectionSet(i_sel_set_name)

    def get_list_of_selection_set(self, o_list_of_selection_set: tuple) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub GetListOfSelectionSet(CATSafeArrayVariant
                | oListOfSelectionSet)
                | 
                |     Retrieves the list of Selection Sets in the document.
                | 
                |     Parameters:
                | 
                |         oListOfSelectionSet
                |             The list of Selection Sets in the document 
                | 
                |     Returns:
                |         The error code of function :
                | 
                |             S_OK if the method succeeded
                |             E_FAIL if an error occurred

        :param tuple o_list_of_selection_set:
        :rtype: None
        """
        return self.selection_sets.GetListOfSelectionSet(o_list_of_selection_set)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_list_of_selection_set'
        # # vba_code = """
        # # Public Function get_list_of_selection_set(selection_sets)
        # #     Dim oListOfSelectionSet (2)
        # #     selection_sets.GetListOfSelectionSet oListOfSelectionSet
        # #     get_list_of_selection_set = oListOfSelectionSet
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def put_selection_set_into_cso(self, i_sel_set_name: str) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub PutSelectionSetIntoCSO(CATBSTR iSelSetName)
                | 
                |     Puts Selection Set's content in the CSO.
                | 
                |     Parameters:
                | 
                |         iSelSetName
                |             The name of the Selection Set to put in the CSO. 
                | 
                |     Returns:
                |         The error code of function :
                | 
                |             S_OK if the content of the Selection Set is added in the
                |             CSO
                |             E_FAIL if the content of the Selection Set is added in the
                |             CSO

        :param str i_sel_set_name:
        :rtype: None
        """
        return self.selection_sets.PutSelectionSetIntoCSO(i_sel_set_name)

    def rename_selection_set(self, i_old_sel_set_name: str, i_new_sel_set_name: str) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub RenameSelectionSet(CATBSTR iOldSelSetName,
                | CATBSTR iNewSelSetName)
                | 
                |     Renames a Selection Set.
                | 
                |     Parameters:
                | 
                |         iOldSelSetName
                |             The original name of the Selection Set. 
                |         iNewSelSetName
                |             The new name of the Selection Set. 
                | 
                |     Returns:
                |         The error code of function :
                | 
                |             S_OK if the name is changed
                |             E_FAIL if the name is not changed

        :param str i_old_sel_set_name:
        :param str i_new_sel_set_name:
        :rtype: None
        """
        return self.selection_sets.RenameSelectionSet(i_old_sel_set_name, i_new_sel_set_name)

    def __repr__(self):
        return f'SelectionSets(name="{ self.name }")'
