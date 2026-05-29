#! usr/bin/python3.9
"""Wrapper for the CATIA V4 Master Model automation object."""

from pycatia.in_interfaces.document import Document
from pycatia.system_interfaces.any_object import AnyObject


class V4MasterModel(AnyObject):
    """Represents the root container of a V4 model."""

    def __init__(self, com_object):
        super().__init__(com_object)
        self.v4_master_model = com_object

    @property
    def v4_document_model(self) -> Document:
        """
        Returns the V4 document containing the master model.

        :rtype: Document
        """

        return Document(self.v4_master_model.V4DocumentModel)

    def __repr__(self):
        return f'V4MasterModel(name="{self.name}")'
