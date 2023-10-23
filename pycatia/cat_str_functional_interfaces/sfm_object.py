#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.any_object import AnyObject


class SFMObject(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SfmObject
                | 
                | Interface to manage the category of a SfmObject.
                | Role: To manage SfmObject's category.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.sfm_object = com_object

    @property
    def category(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Category() As CATBSTR
                | 
                |     Returns or sets the category.
                | 
                |     Example:
                |         This example retrieves in Category the supporting curve for the
                |         SfmObject feature.
                | 
                |          Category = SfmObject.Category

        :rtype: str
        """

        return self.sfm_object.Category

    @category.setter
    def category(self, value: str):
        """
        :param str value:
        """

        self.sfm_object.Category = value

    @property
    def grade(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Grade() As CATBSTR
                | 
                |     Returns or sets the grade.
                | 
                |     Example:
                |         This example retrieves in Grade the informations for the
                |         SfmMaterialProperties feature.
                | 
                |          SfmMaterialProperties.Grade Grade

        :rtype: str
        """

        return self.sfm_object.Grade

    @grade.setter
    def grade(self, value: str):
        """
        :param str value:
        """

        self.sfm_object.Grade = value

    @property
    def material(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Material() As CATBSTR
                | 
                |     Returns or sets the material.
                | 
                |     Example:
                |         This example retrieves in Material the informations for the
                |         SfmMaterialProperties feature.
                | 
                |          SfmMaterialProperties.Material Material

        :rtype: str
        """

        return self.sfm_object.Material

    @material.setter
    def material(self, value: str):
        """
        :param str value:
        """

        self.sfm_object.Material = value

    def __repr__(self):
        return f'SFMObject(name="{self.name}")'
