#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.any_object import AnyObject


class ABQGlobalElementAssignment(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     ABQGlobalElementAssignment
                | 
                | Represents an Abaqus Global Element assignment (ABQGlobalElementAssignment)
                | object.
                | Role:Access an Abaqus Global Element assignment property object or determine
                | its properties.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.abq_global_element_assignment = com_object

    def get_element_properties(
            self,
            i_elem_id: int,
            o_elem_behav: int,
            o_mff_lag: bool,
            o_hf_flag: bool,
            o_ri_flag: bool,
            o_im_flag: bool,
            o_in_flag: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetElementProperties(elemIDEnum iElemID,
                | elemBehavEnum oElemBehav,
                | boolean oMFFLag,
                | boolean oHFFlag,
                | boolean oRIFlag,
                | boolean oIMFlag,
                | boolean oINFlag)
                | 
                |     Gets the behavior and the modifier to given element type.
                | 
                |     Parameters:
                | 
                |         iElemID
                |             The element type ID for which behavior and modifier is
                |             requested.
                |
                |             Legal values:
                |             TET_LINEAR
                |             TET_PARABOLIC
                |             HEX_LINEAR
                |             HEX_PARABOLIC
                |             WEDG_LINEAR
                |             WEDG_PARABOLIC
                |             TRI_LINEAR
                |             TRI_PARABOLIC
                |             QUAD_LINEAR
                |             QUAD_PARABOLIC
                |             LINE_LINEAR
                |             LINE_PARABOLIC
                | 
                |         oElemBehav
                |             The element behavior set to given element type.
                |
                |             Legal values:
                |             SHELL
                |             MEMBRANE
                |             SOLID3D
                |             CONTINUUM_SHELL
                |             BEAM
                |             GASKET
                | 
                |         oMFFLag
                |             The modified formulation flag.
                |
                |             Legal values:
                |             true
                |             false
                | 
                |         oHFFlag
                |             The hybrid formulation flag.
                |
                |             Legal values:
                |             true
                |             false
                | 
                |         oRIFlag
                |             The reduced integration flag.
                |
                |             Legal values:
                |             true
                |             false
                | 
                |         oIMFlag
                |             The incompatible modes flag.
                |
                |             Legal values:
                |             true
                |             false
                | 
                |         oINFlag
                |             The Gasket thickness behavior flag.
                |
                |             Legal values:
                |             true
                |             false

        :param int i_elem_id: enum elem_id_enum
        :param int o_elem_behav: enum elem_behav_enum
        :param bool o_mff_lag:
        :param bool o_hf_flag:
        :param bool o_ri_flag:
        :param bool o_im_flag:
        :param bool o_in_flag:
        :rtype: None
        """
        return self.abq_global_element_assignment.GetElementProperties(
            i_elem_id,
            o_elem_behav,
            o_mff_lag,
            o_hf_flag,
            o_ri_flag,
            o_im_flag,
            o_in_flag)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_element_properties'
        # # vba_code = """
        # # Public Function get_element_properties(abq_global_element_assignment)
        # #     Dim iElemID (2)
        # #     abq_global_element_assignment.GetElementProperties iElemID
        # #     get_element_properties = iElemID
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_element_properties(
            self,
            i_elem_id: int,
            i_elem_behav: int,
            i_mff_lag: bool,
            i_hf_flag: bool,
            i_ri_flag: bool,
            i_im_flag: bool,
            i_in_flag: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetElementProperties(elemIDEnum iElemID,
                | elemBehavEnum iElemBehav,
                | boolean iMFFLag,
                | boolean iHFFlag,
                | boolean iRIFlag,
                | boolean iIMFlag,
                | boolean iINFlag)
                | 
                |     Sets the behavior and the modifier to given element type.
                | 
                |     Parameters:
                | 
                |         iElemID
                |             The element type ID for which behavior and modifier is to be
                |             set.
                |
                |             Legal values:
                |             TET_LINEAR
                |             TET_PARABOLIC
                |             HEX_LINEAR
                |             HEX_PARABOLIC
                |             WEDG_LINEAR
                |             WEDG_PARABOLIC
                |             TRI_LINEAR
                |             TRI_PARABOLIC
                |             QUAD_LINEAR
                |             QUAD_PARABOLIC
                |             LINE_LINEAR
                |             LINE_PARABOLIC
                | 
                |         iElemBehav
                |             The element behavior to be set to given element
                |             type.
                |
                |             Legal values:
                |             SHELL
                |             MEMBRANE
                |             SOLID3D
                |             CONTINUUM_SHELL
                |             BEAM
                |             GASKET
                | 
                |         iMFFLag
                |             The modified formulation flag.
                | 
                |             Legal values:
                |             true
                |             false
                | 
                |         iHFFlag
                |             The hybrid formulation flag.
                |
                |             Legal values:
                |             true
                |             false
                | 
                |         iRIFlag
                |             The reduced integration flag.
                |
                |             Legal values:
                |             true
                |             false
                | 
                |         iIMFlag
                |             The incompatible modes flag.
                | 
                |             Legal values:
                |             true
                |             false
                | 
                |         iINFlag
                |             The Gasket thickness behavior flag.
                | 
                |             Legal values:
                |             true
                |             false
                |
                |             Example: To specify element type 'C3D10MH' user can use this method
                |             as shown below.
                |             SetElementValues TET_PARABOLI SOLID3D true true false false false
                |             false.

        :param int i_elem_id: enum elem_id_enum
        :param int i_elem_behav: enum elem_behav_enum
        :param bool i_mff_lag:
        :param bool i_hf_flag:
        :param bool i_ri_flag:
        :param bool i_im_flag:
        :param bool i_in_flag:
        :rtype: None
        """
        return self.abq_global_element_assignment.SetElementProperties(
            i_elem_id,
            i_elem_behav,
            i_mff_lag,
            i_hf_flag,
            i_ri_flag,
            i_im_flag,
            i_in_flag)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_element_properties'
        # # vba_code = """
        # # Public Function set_element_properties(abq_global_element_assignment)
        # #     Dim iElemID (2)
        # #     abq_global_element_assignment.SetElementProperties iElemID
        # #     set_element_properties = iElemID
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'ABQGlobalElementAssignment(name="{self.name}")'
