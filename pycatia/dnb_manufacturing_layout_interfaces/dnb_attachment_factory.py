#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.any_object import AnyObject


class DnbAttachmentFactory(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     DNBAttachmentFactory
                | 
                | Interface representing xxx.
                | 
                | Role: Components that implement DNBIABasicDevice are ...
                | 
                | Do not use the DNBIAMRLAttachmentFactory interface for such and such
                | ClassReference, Class#MethodReference, #InternalMethod...
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.dnb_attachment_factory = com_object

    def attach(self, i_parent: AnyObject, i_child: AnyObject, o_attachment: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub Attach(CATBaseDispatch iParent,
                | CATBaseDispatch iChild,
                | CATBaseDispatch oAttachment)
                | 
                |     Attach a Product/MA with another Product/MA
                | 
                |     Parameters:
                | 
                |         iParent
                |             This input parameter contains the Parent product/MA of the
                |             attachment to be created 
                |         iChild
                |             This input parameter contains the Child product/MA of the
                |             attachment to be created 
                |         oAttachment
                |             This output parameter contains the attachment that is created.
                |
                |     Returns:
                |         An HRESULT

        :param AnyObject i_parent:
        :param AnyObject i_child:
        :param AnyObject o_attachment:
        :rtype: None
        """
        return self.dnb_attachment_factory.Attach(i_parent.com_object, i_child.com_object, o_attachment.com_object)

    def remove(self, i_attachment: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub Remove(CATBaseDispatch iAttachment)
                | 
                |     Remove an attachment.
                | 
                |     Parameters:
                | 
                |         iAttachment
                |             This input parameter contains the Attachment to be deleted.
                |
                |     Returns:
                |         An HRESULT

        :param AnyObject i_attachment:
        :rtype: None
        """
        return self.dnb_attachment_factory.Remove(i_attachment.com_object)

    def __repr__(self):
        return f'DnbAttachmentFactory(name="{self.name}")'
