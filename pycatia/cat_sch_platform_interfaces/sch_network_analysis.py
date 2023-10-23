#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.cat_sch_platform_interfaces.sch_app_connectable import SchAppConnectable
from pycatia.cat_sch_platform_interfaces.sch_list_of_objects import SchListOfObjects
from pycatia.system_interfaces.any_object import AnyObject


class SchNetworkAnalysis(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SchNetworkAnalysis
                | 
                | Represents a schematic network.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.sch_network_analysis = com_object

    def find_paths(self, i_from_object: SchAppConnectable, i_to_object: SchAppConnectable) -> SchListOfObjects:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func FindPaths(SchAppConnectable iFromObject,
                | SchAppConnectable iToObject) As SchListOfObjects
                | 
                |     Given a start and end object in the network, this method returns a list of
                |     network objects each representing a path connecting the the 2 input
                |     objects.
                | 
                |     Parameters:
                | 
                |         iFromObject
                |             The connectable to start from. 
                |         iToObject
                |             The connectable to finish at. 
                |         oLNetworks
                |             Pointer to a list of networks. (Members are CATISchNetworkAnalysis
                |             interface pointers). 
                | 
                |     Example:
                |
                |          Dim objThisIntf As SchNetworkAnalysis
                |          Dim objArg1 As SchAppConnectable
                |          Dim objArg2 As SchAppConnectable
                |          Dim objArg3 As SchListOfObjects
                |           ...
                |          Set objArg3 = objThisIntf.FindPaths(objArg1,objArg2)

        :param SchAppConnectable i_from_object:
        :param SchAppConnectable i_to_object:
        :rtype: SchListOfObjects
        """
        return SchListOfObjects(self.sch_network_analysis.FindPaths(i_from_object.com_object, i_to_object.com_object))

    def list_extremity_objects(self) -> SchListOfObjects:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func ListExtremityObjects() As SchListOfObjects
                | 
                |     List the extremity objects of the network.
                | 
                |     Parameters:
                | 
                |         oLExtremityObjs
                |             Pointer to a list of extremity objects of the network (Members are
                |             CATISchAppConnectable interface pointers). 
                | 
                |     Example:
                |
                |          Dim objThisIntf As SchNetworkAnalysis
                |          Dim objArg1 As SchListOfObjects
                |           ...
                |          Set objArg1 = objThisIntf.ListExtremityObjects

        :rtype: SchListOfObjects
        """
        return SchListOfObjects(self.sch_network_analysis.ListExtremityObjects())

    def list_network_objects(self) -> SchListOfObjects:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func ListNetworkObjects() As SchListOfObjects
                | 
                |     List the connected objects in the network.
                | 
                |     Parameters:
                | 
                |         oLNetworkObjs
                |             Pointer to a list of all connected objects in the network. (Members
                |             are CATISchAppConnectable interface pointers) 
                | 
                |     Example:
                |
                |          Dim objThisIntf As SchNetworkAnalysis
                |          Dim objArg1 As SchListOfObjects
                |           ...
                |          Set objArg1 = objThisIntf.ListNetworkObjects

        :rtype: SchListOfObjects
        """
        return SchListOfObjects(self.sch_network_analysis.ListNetworkObjects())

    def __repr__(self):
        return f'SchNetworkAnalysis(name="{self.name}")'
