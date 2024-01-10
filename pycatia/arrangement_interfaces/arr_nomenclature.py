#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from typing import TYPE_CHECKING

from pycatia.system_interfaces.any_object import AnyObject

if TYPE_CHECKING:
    from pycatia.arrangement_interfaces.arr_nomenclatures import ArrNomenclatures


class ArrNomenclature(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     ArrNomenclature
                | 
                | Represents the UserNomenclature object.
                | The UserNomenclature object is used in the CATIAArrNomenclatureTree object to
                | maintain the hierarchy of user type names and associated icons.
                | CATIAArrNomenclatureTree
                |
                | _______ Area - (I_ArrArea)
                |
                | _______ Building -
                | (I_ArrBuilding)
                |
                | _______ Safety Zone - (I_ArrSafetyZone)
                |
                | -------- Run -
                | (I_ArrRun)
                |
                | _______ Conduit Run
                | _______ Raceway Run In the diagram shown
                | above, Area (along with its subtypes) and Run (also along with it's
                | subtypes) are all UserNomenclature objects. Entries such as the Area and Run
                | are called System or SuperClass objects that have to be defined first before
                | the subclasses such as Building and Safety Zone are defined. SuperClasses will
                | not have a supertype. Each Nomenclature holds the following information... (1)
                | NLSName - So as to support names in different languages (2) IconName - So as to
                | allow user's to define their own icons (3) SuperType - For subtypes to fetch
                | their parent names (4) SubTypes - SubTypes defined under this User
                | Nomenclature
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.arr_nomenclature = com_object

    @property
    def icon_name(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property IconName() As CATBSTR
                | 
                |     Gets/Sets the Icon Name associated to the Type Name. The IconName is the
                |     file name, without the extension, of the Icon bitmap representing this user
                |     type. The icon definition file must be in one of the icon directories defined
                |     in the search paths used by CATIA.

        :rtype: str
        """

        return self.arr_nomenclature.IconName

    @icon_name.setter
    def icon_name(self, value: str):
        """
        :param str value:
        """

        self.arr_nomenclature.IconName = value

    @property
    def int_sys_class_name(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property IntSysClassName() As CATBSTR
                | 
                |     Gets/Sets the internal class names for System nomenclatures. This value is
                |     set only for System nomenclatures

        :rtype: str
        """

        return self.arr_nomenclature.IntSysClassName

    @int_sys_class_name.setter
    def int_sys_class_name(self, value: str):
        """
        :param str value:
        """

        self.arr_nomenclature.IntSysClassName = value

    @property
    def nls_instance_name(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property NLSInstanceName() As CATBSTR
                | 
                |     Gets/Sets the InstanceName

        :rtype: str
        """

        return self.arr_nomenclature.NLSInstanceName

    @nls_instance_name.setter
    def nls_instance_name(self, value: str):
        """
        :param str value:
        """

        self.arr_nomenclature.NLSInstanceName = value

    @property
    def sub_types(self) -> 'ArrNomenclatures':
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property SubTypes() As ArrNomenclatures (Read Only)
                | 
                |     Returns the collection of subtype UserNomenclatures within this
                |     UserNomenclature.

        :rtype: ArrNomenclatures
        """
        from pycatia.arrangement_interfaces.arr_nomenclatures import ArrNomenclatures
        return ArrNomenclatures(self.arr_nomenclature.SubTypes)

    @property
    def super_type_name(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property SuperTypeName() As CATBSTR
                | 
                |     Get/Set the Supertype Information This property is used to set the subtypes
                |     for system classes

        :rtype: str
        """

        return self.arr_nomenclature.SuperTypeName

    @super_type_name.setter
    def super_type_name(self, value: str):
        """
        :param str value:
        """

        self.arr_nomenclature.SuperTypeName = value

    def is_system_nomenclature(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func IsSystemNomenclature() As boolean
                | 
                |     Returns TRUE if the nomenclature happens to be a system nomenclature.
                |     Returns FALSE if it is a user specified nomenclature.

        :rtype: bool
        """
        return self.arr_nomenclature.IsSystemNomenclature()

    def __repr__(self):
        return f'ArrNomenclature(name="{self.name}")'
