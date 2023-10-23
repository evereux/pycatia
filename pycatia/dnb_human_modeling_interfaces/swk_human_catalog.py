from pathlib import Path

from pycatia.in_interfaces.reference import Reference
from pycatia.system_interfaces.any_object import AnyObject
from pycatia.types.general import cat_variant


class SWKHumanCatalog(AnyObject):
    """
    This class is not documented in the CAA V5 Visual Basic Help file.

    This class was created by referring to the Microsoft Visual Basic object explorer.
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def active_family(self) -> str:
        """
        .. note::
            :class: toggle

            Microsoft Visual Basic Object Browser
                | Property ActiveFamily As String
                |     Member of SWKHumanModelingItf.SWKHumanCatalog

        :rtype: str
        """

        return self.com_object.ActiveFamily

    @property
    def is_dirty(self) -> bool:
        """
        .. note::
            :class: toggle

            Microsoft Visual Basic Object Browser
                | Property IsDirty As Boolean
                |     read-only
                |     Member of SWKHumanModelingItf.SWKHumanCatalog

        :rtype: bool
        """

        return self.com_object.IsDirty

    @property
    def nb_items(self) -> int:
        """
        .. note::
            :class: toggle

            Microsoft Visual Basic Object Browser
                | Property NbItems As Long
                |     read-only
                |     Member of SWKHumanModelingItf.SWKHumanCatalog

        :rtype: int
        """

        return self.com_object.NbItems

    @property
    def number_of_families(self) -> int:
        """
        .. note::
            :class: toggle

            Microsoft Visual Basic Object Browser
                | Property NumberOfFamilies As Long
                |     read-only
                |     Member of SWKHumanModelingItf.SWKHumanCatalog

        :rtype: int
        """

        return self.com_object.NumberOfFamilies

    def add_item_from_hso(self, pi_description: str) -> None:
        """
        .. note::
            :class: toggle

            Microsoft Visual Basic Object Browser
                | Sub AddItemFromHSO(piDescription As String)
                |     Member of SWKHumanModelingItf.SWKHumanCatalog

        :param str pi_description:
        :rtype: None
        """

        return self.com_object.AddItemFromHSO(pi_description)

    def add_items_from_swl_file(self, pi_file_path: Path) -> None:
        """
        .. note::
            :class: toggle

            Microsoft Visual Basic Object Browser
                | Sub AddItemsFromSwlFile(piFilePath As String)
                |     Member of SWKHumanModelingItf.SWKHumanCatalog

        :param Path pi_file_path:
        :rtype: None
        """

        return self.com_object.AddItemsFromSwlFile(pi_file_path)

    def apply_item(self, pi_index: int) -> None:
        """
        .. note::
            :class: toggle

            Microsoft Visual Basic Object Browser
                | Sub ApplyItem(piIndex As Long)
                |     Member of SWKHumanModelingItf.SWKHumanCatalog

        :param int pi_index:
        :rtype: None
        """

        return self.com_object.ApplyItem(pi_index)

    def empty(self) -> None:
        """
        .. note::
            :class: toggle

            Microsoft Visual Basic Object Browser
                | Sub Empty()
                |     Member of SWKHumanModelingItf.SWKHumanCatalog

        :rtype: None
        """

        return self.com_object.Empty()

    def get_attach_and_cst_infos(self) -> cat_variant:
        """
        .. note::
            :class: toggle

            Microsoft Visual Basic Object Browser
                | Sub GetAttachAndCstInfos(piIndex As Long, piNbInfos As Long, poInfos() As Variant)
                |     Member of SWKHumanModelingItf.SWKHumanCatalog

        :rtype: cat_variant
        """

        return self.com_object.GetAttachAndCstInfos()

    def get_family_name(self, pi_index: int) -> str:
        """
        .. note::
            :class: toggle

            Microsoft Visual Basic Object Browser
                | Function GetFamilyName(piIndex As Long) As String
                |     Member of SWKHumanModelingItf.SWKHumanCatalog

        :param int pi_index:
        :rtype: cat_variant
        """

        return self.com_object.GetFamilyName(pi_index)

    def get_item_date(self, pi_index: int) -> str:
        """
        .. note::
            :class: toggle

            Microsoft Visual Basic Object Browser
                | Function GetItemDate(piIndex As Long) As String
                |     Member of SWKHumanModelingItf.SWKHumanCatalog

        :param int pi_index:
        :rtype: str
        """

        return self.com_object.GetItemDate(pi_index)

    def get_item_description(self, pi_index: int) -> str:
        """
        .. note::
            :class: toggle

            Microsoft Visual Basic Object Browser
                | Function GetItemDescription(piIndex As Long) As String
                |     Member of SWKHumanModelingItf.SWKHumanCatalog

        :param int pi_index:
        :rtype: str
        """

        return self.com_object.GetItemDescription(pi_index)

    def get_item_type(self, pi_index: int) -> str:
        """
        .. note::
            :class: toggle

            Microsoft Visual Basic Object Browser
                | Function GetItemType(piIndex As Long) As String
                |     Member of SWKHumanModelingItf.SWKHumanCatalog

        :param int pi_index:
        :rtype: str
        """

        return self.com_object.GetItemType(pi_index)

    def get_nb_attach_and_cst(self, pi_index: int) -> int:
        """
        .. note::
            :class: toggle

            Microsoft Visual Basic Object Browser
                | Function GetNbAttachAndCst(piIndex As Long) As Long
                |     Member of SWKHumanModelingItf.SWKHumanCatalog

        :param int pi_index:
        :rtype: int
        """

        return self.com_object.GetNbAttachAndCst(pi_index)

    def reload(self) -> None:
        """
        .. note::
            :class: toggle

            Microsoft Visual Basic Object Browser
                | Sub Reload()
                |     Member of SWKHumanModelingItf.SWKHumanCatalog

        :rtype: None
        """

        return self.com_object.Reload()

    def remove_item(self, pi_index: int) -> None:
        """
        .. note::
            :class: toggle

            Microsoft Visual Basic Object Browser
                | Sub RemoveItem(piIndex As Long)
                |     Member of SWKHumanModelingItf.SWKHumanCatalog

        :param int pi_index:
        :rtype: None
        """

        return self.com_object.RemoveItem(pi_index)

    def save(self) -> None:
        """
        .. note::
            :class: toggle

            Microsoft Visual Basic Object Browser
                | Sub Save()
                |     Member of SWKHumanModelingItf.SWKHumanCatalog

        :rtype: None
        """

        return self.com_object.Save()

    def set_attach_or_cst_object(self, pi_description_index: int, pi_item_index: int, pi_reference: Reference) -> None:
        """
        .. note::
            :class: toggle

            Microsoft Visual Basic Object Browser
                | Sub SetAttachOrCstObject(piDescriptionIndex As Long, piItemIndex As Long, piReference As Reference)
                |     Member of SWKHumanModelingItf.SWKHumanCatalog

        :param int pi_description_index:
        :param int pi_item_index:
        :param int pi_reference:
        :rtype: None
        """

        return self.com_object.SetAttachOrCstObject(pi_description_index, pi_item_index, pi_reference)
