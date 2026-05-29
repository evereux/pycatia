#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.

"""

from pycatia.in_interfaces.document import Document
from pycatia.system_interfaces.any_object import AnyObject


class V4MasterModel(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     V4MasterModel
                |
                | Represents the V4 Master Model.
                | The Master is the root container of a V4 Model.

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.v4_master_model = com_object

    @property
    def v4_document_model(self) -> Document:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property V4DocumentModel() As Document (Read Only)
                |
                |     Returns the V4 Document that contains the Master's Model.

        :rtype: Document
        """

        return Document(self.v4_master_model.V4DocumentModel)

    def __repr__(self):
        return f'V4MasterModel(name="{self.name}")'
