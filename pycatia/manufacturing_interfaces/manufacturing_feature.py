#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.knowledge_interfaces.parameter import Parameter
from pycatia.system_interfaces.any_object import AnyObject


class ManufacturingFeature(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     ManufacturingFeature
                | 
                | ManufacturingFeature defines a set of methods to access a Manufacturing
                | Feature.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.manufacturing_feature = com_object

    def get_a_geometric_attribute(self, i_attribute: str) -> Parameter:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetAGeometricAttribute(CATBSTR iAttribut) As
                | Parameter
                | 
                |     Retrieve a geometry attribute of a Manufacturing Feature from its
                |     name.
                | 
                |     Parameters:
                | 
                |         iAttribute
                |             The identifier of the attribute to be read 
                |         Example:
                |             The following example retrieves the attribute 'MfgHoleExtension' of
                |             the manufacturing feature mfgFeature:
                | 
                |              call mfgFeature.GetAGeometricAttribute('MfgHoleExtension'
                |              ,ExtentParm)

        :param str i_attribute:
        :rtype: Parameter
        """
        return Parameter(self.manufacturing_feature.GetAGeometricAttribute(i_attribute))

    def __repr__(self):
        return f'ManufacturingFeature(name="{self.name}")'
