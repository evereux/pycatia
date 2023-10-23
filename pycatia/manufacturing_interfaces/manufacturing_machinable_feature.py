#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.manufacturing_interfaces.manufacturing_feature import ManufacturingFeature


class ManufacturingMachinableFeature(ManufacturingFeature):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                    ManufacturingInterfaces.ManufacturingFeature
                |                         ManufacturingMachinableFeature
                | 
                | Machinable Feature in Manufacturing.
                | It is the base object for machinable geometry and machinable
                | area
                | 
                | See also:
                |     ManufacturingMachinableArea, ManufacturingMachinableGeometry
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.manufacturing_machinable_feature = com_object

    @property
    def feat_remark(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property FeatRemark() As CATBSTR
                | 
                |     Returns the manufacturing machinable feature remark.
                | 
                |     Returns:
                |         oFeatRemark The manufacturing machinable feature remark
                |         
                |     Example:
                |         The following example returns in tFeatRemark the remark of
                |         manufacturing machinable feature firstMachFeat:
                | 
                |          Dim firstMachFeat As ManufacturingMachinableFeature
                |          Set firstMachFeat = ...
                |          Dim tFeatRemark As CATBSTR
                |          Set tFeatRemark = firstMachFeat.FeatRemark

        :rtype: str
        """

        return self.manufacturing_machinable_feature.FeatRemark

    @feat_remark.setter
    def feat_remark(self, value: str):
        """
        :param str value:
        """

        self.manufacturing_machinable_feature.FeatRemark = value

    @property
    def feat_type(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property FeatType() As CATBSTR
                | 
                |     Returns the manufacturing machinable feature type.
                | 
                |     Returns:
                |         oFeatType The manufacturing machinable feature type 
                |     Example:
                |         The following example returns in tFeatType the type of manufacturing
                |         machinable feature firstMachFeat:
                | 
                |          Dim firstMachFeat As ManufacturingMachinableFeature
                |          Set firstMachFeat = ...
                |          Dim tFeatType As CATBSTR
                |          Set tFeatType = firstMachFeat.FeatType

        :rtype: str
        """

        return self.manufacturing_machinable_feature.FeatType

    @feat_type.setter
    def feat_type(self, value: str):
        """
        :param str value:
        """

        self.manufacturing_machinable_feature.FeatType = value

    def __repr__(self):
        return f'ManufacturingMachinableFeature(name="{self.name}")'
