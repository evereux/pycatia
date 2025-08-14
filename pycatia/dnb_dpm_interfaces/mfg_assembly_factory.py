#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.dmaps_interfaces.item import Item
from pycatia.system_interfaces.any_object import AnyObject
from pycatia.types.general import cat_variant


class MfgAssemblyFactory(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MfgAssemblyFactory
                | 
                | Represents the factory to creates a manufacturing assembly.
                | 
                | Role: It gives access to the C++ DNBIMfgAssemblyFactory interface methods Such
                | as
                | 
                |     Creates a manufacturing assembly
                | 
                | Example:
                |     This example fetches an instance of a Manufacturing Assembly factory in a a
                |     active document and then creates a manufactring assembly
                | 
                |      Dim objMAfact As MfgAssemblyFactory
                |      Set objMAfact =  CATIA.ActiveDocument.GetItem("MfgAssemblyFactory")
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.mfg_assembly_factory = com_object

    def create_mfg_assembly(self, i_name_bstr: str, i_part_number_bstr: str, i_type: int) -> Item:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func CreateMfgAssembly(CATBSTR iNameBSTR,
                | CATBSTR iPartNumberBSTR,
                | DNBIAMfgAssemblyType iType) As Item
                | 
                |     Creates a manufacturing assembly of given type "iType". This API cannot be
                |     used to create a Manufacturing Assembly of type AST(assemblySpecTree) or
                |     Manufacturing Output(manufacturingOutput)
                | 
                |     Parameters:
                | 
                |         iNameBSTR
                |             Name of the manufacturing assembly 
                |         iPartNumberBSTR
                |             Part-number of the manufacturing assembly 
                |         iType
                |             Type of the Manufacturing Assembly. If its value is "notSpecified"
                |             (or 4), the new assembly created will be of type "manufacturingAssembly"
                |             
                |         oMfgAssembly
                |             Handler of the Manufacturing Assembly created
                | 
                |             Example:
                |                 This example creates a Manufacturing Assembly of type
                |                 "manufacturingKit" having MAName as "MKit1" and part-number as
                |                 "Kit1"
                | 
                |                  Dim matype As DNBIAMfgAssemblyType
                |                  matype=manufacturingKit
                |                  Dim MA As MfgAssembly (Or Dim MA As item)
                |                  objMAfact.CreateMfgAssembly
                |                  "MKit1","Kit1",matype,MA
                |                 where objMAfact is a instance of Automation Interface for
                |                 Manufacturing Assembly as shown earlier

        :param str i_name_bstr:
        :param str i_part_number_bstr:
        :param int i_type: enum dnbia_mfg_assembly_type
        :rtype: Item
        """
        return Item(self.mfg_assembly_factory.CreateMfgAssembly(i_name_bstr, i_part_number_bstr, i_type))

    def get_number_of_mfg_assemblies(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetNumberOfMfgAssemblies() As long
                | 
                |     Get the number of Manufacturing Assemblies in MA Applicative
                |     Container
                | 
                |     Parameters:
                | 
                |         oNumOfMfgAssemblies
                |             number of Manufacturing Assemblies in MA Applicative
                |             Container
                | 
                |             Example:
                |                 For example getting the number of Manufacturing assemblies and
                |                 displaying them in the Message Box.
                | 
                |                  Dim nbMfgAssemblies 
                |                  Set nbMfgAssemblies =  objMAfact.GetNumberOfMfgAssemblies
                |                  MsgBox  nbMfgAssemblies

        :rtype: int
        """
        return self.mfg_assembly_factory.GetNumberOfMfgAssemblies()

    def get_number_of_all_mfg_assy(self, i_type: int, o_num_of_mfg_assemblies: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetNumberofALLMfgAssy(DNBIAMfgAssemblyType iType,
                | long oNumOfMfgAssemblies)
                | 
                |     Get the number of Manufacturing Assemblies(MA) of given type in MA
                |     Applicative Container
                | 
                |     Parameters:
                | 
                |         iType
                |             Type of MA to be considered. If its value is "notSpecified" (or 4),
                |             all the MAs will be considered 
                |         oNumOfMfgAssemblies
                |             Number of MAs found
                | 
                |             Example:
                |                 For example getting the number of MA of type "manufacturingKit"
                |                 and displaying them in the Message Box.
                | 
                |                  Dim matype As DNBIAMfgAssemblyType
                |                  matype=manufacturingKit
                |                  Dim nbMfgAssemblies 
                |                  objMAfact.GetNumberofALLMfgAssy
                |                  matype,nbMfgAssemblies
                |                  MsgBox  nbMfgAssemblies

        :param int i_type: enum dnbia_mfg_assembly_type
        :param int o_num_of_mfg_assemblies:
        :rtype: None
        """
        return self.mfg_assembly_factory.GetNumberofALLMfgAssy(i_type, o_num_of_mfg_assemblies)

    def remove_mfg_assembly(self, i_mfg_assembly: Item) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub RemoveMfgAssembly(Item iMfgAssembly)
                | 
                |     Removes a given Manufacturing Assembly from the MA Applicative Container.
                |     Please note that the AST MA cannot be removed
                | 
                |     Parameters:
                | 
                |         iMfgAssembly
                |             Manufacturing assembly to be removed or deleted
                | 
                |             Example:
                |                 For example deleting the first MA from the Applicative
                |                 Container
                | 
                |                  Dim mfgAssy As Item
                |                  Set mfgAssy =  objMAfact.RetrieveMfgAssemblyAtIndex(1)
                |                  objMAfact.RemoveMfgAssembly mfgAssy

        :param Item i_mfg_assembly:
        :rtype: None
        """
        return self.mfg_assembly_factory.RemoveMfgAssembly(i_mfg_assembly.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'remove_mfg_assembly'
        # # vba_code = """
        # # Public Function remove_mfg_assembly(mfg_assembly_factory)
        # #     Dim iMfgAssembly (2)
        # #     mfg_assembly_factory.RemoveMfgAssembly iMfgAssembly
        # #     remove_mfg_assembly = iMfgAssembly
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def retrieve_mfg_assembly(
            self,
            i_name_bstr: str,
            o_mfg_assemblies: tuple,
            o_num_of_mfg_assemblies: int
    ) -> AnyObject:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub RetrieveMfgAssembly(CATBSTR iNameBSTR,
                | CATSafeArrayVariant oMfgAssemblies,
                | long oNumOfMfgAssemblies)
                | 
                |     Retrieve all the Manufacturing Assemblies of a given name.
                | 
                |     Parameters:
                | 
                |         iNameBSTR
                |             Name of the manufacturing assembly 
                |         oMfgAssemblies
                |             Array of the Items of the type "MfgAssembly". Array need to be
                |             allocated before passing. In case, if the size allocated is found to be less
                |             than the actual number of Manufacturing Assemblies found, the number of MAs
                |             returned will be equal to size of array passed only
                |             
                |         oNumOfMfgAssemblies
                |             Number of MAs found with the given name. If the actual number of
                |             MAs found is greater than the size of the array passed, then value returned
                |             will be equal to the size of the array itself.
                | 
                |             Example:
                |                 For example retriving all the MAs with the name "MA_TYPE1" from
                |                 the MA Applicative Container
                | 
                |                  Dim nbMfgAssemblies 
                |                  Set nbMfgAssemblies =  objMAfact.GetNumberOfMfgAssemblies
                |                  Dim MAList() As AnyObject
                |                  ReDim MAList(nbMfgAssemblies-1)
                |                  Dim NbMA 
                |                  objMAfact.RetrieveMfgAssembly
                |                  "MA_TYPE1",MAList,NbMA
                |                  MsgBox  NbMA

        :param str i_name_bstr:
        :param tuple o_mfg_assemblies:
        :param int o_num_of_mfg_assemblies:
        :rtype: AnyObject
        """
        return AnyObject(
            self.mfg_assembly_factory.RetrieveMfgAssembly(
                i_name_bstr,
                o_mfg_assemblies,
                o_num_of_mfg_assemblies
            )
        )
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'retrieve_mfg_assembly'
        # # vba_code = """
        # # Public Function retrieve_mfg_assembly(mfg_assembly_factory)
        # #     Dim iNameBSTR (2)
        # #     mfg_assembly_factory.RetrieveMfgAssembly iNameBSTR
        # #     retrieve_mfg_assembly = iNameBSTR
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def retrieve_mfg_assembly_at_index(self, i_index: cat_variant) -> Item:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func RetrieveMfgAssemblyAtIndex(CATVariant iIndex) As Item
                | 
                |     Retrieves a Manufacturing Assembly at the given index from the MA
                |     Applicative Container.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             Index 
                |         oItem
                |             Manufacturing Assembly at the above Index
                | 
                |             Example:
                |                 For example retriving all the MAs from the Applicative
                |                 Container
                | 
                |                  Dim nbMfgAssemblies 
                |                  Set nbMfgAssemblies =  objMAfact.GetNumberOfMfgAssemblies
                |                  For II = 0 to MyNum-1
                |                    Dim mfgAssy As Item
                |                     Set mfgAssy =  objMAfact.RetrieveMfgAssemblyAtIndex(II)
                |                 Next

        :param cat_variant i_index:
        :rtype: Item
        """
        return Item(self.mfg_assembly_factory.RetrieveMfgAssemblyAtIndex(i_index))

    def retrive_all_mfg_assy(self, i_type: int, o_all_m_as: tuple, o_num_of_mfg_assemblies: int) -> AnyObject:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub RetriveALLMfgAssy(DNBIAMfgAssemblyType iType,
                | CATSafeArrayVariant oAllMAs,
                | long oNumOfMfgAssemblies)
                | 
                |     Retrieve all the Manufacturing Assemblies of a given type.
                | 
                |     Parameters:
                | 
                |         iType
                |             Type of manufacturing assemblies to be retrieved. If its value is
                |             "notSpecified" (or 4), all the manufacturing assemblies will be returned
                |             
                |         oMfgAssemblies
                |             Array of the Items of the type "MfgAssembly". Array need to be
                |             allocated before passing. In case, if the size allocated is found to be less
                |             than the actual number of Manufacturing Assemblies found, the number of MAs
                |             returned will be equal to size of array passed only
                |             
                |         oNumOfMfgAssemblies
                |             Number of MAs found. If the actual number of MAs found is greater
                |             than the size of the array passed, then value returned will be equal to the
                |             size of the array itself.
                | 
                |             Example:
                |                 For example: Code for retriving all the MAs of type
                |                 "manufacturingKit" from the MA Applicative
                |                 Container
                | 
                |                  Dim matype As DNBIAMfgAssemblyType
                |                  matype=manufacturingKit
                |                  Dim nbMfgAssemblies 
                |                  objMAfact.GetNumberofALLMfgAssy
                |                  matype,nbMfgAssemblies
                |                  Dim MAList() As AnyObject
                |                  ReDim MAList(nbMfgAssemblies)
                |                  Dim NbMA
                |                  objMAfact.RetriveALLMfgAssy
                |                  matype,MAList,NbMA

        :param int i_type: enum dnbia_mfg_assembly_type
        :param tuple o_all_m_as:
        :param int o_num_of_mfg_assemblies:
        :rtype: AnyObject
        """
        return AnyObject(self.mfg_assembly_factory.RetriveALLMfgAssy(i_type, o_all_m_as, o_num_of_mfg_assemblies))
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'retrive_all_mfg_assy'
        # # vba_code = """
        # # Public Function retrive_all_mfg_assy(mfg_assembly_factory)
        # #     Dim iType (2)
        # #     mfg_assembly_factory.RetriveALLMfgAssy iType
        # #     retrive_all_mfg_assy = iType
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'MfgAssemblyFactory(name="{self.name}")'
