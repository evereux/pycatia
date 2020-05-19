#! /usr/bin/python3.6
# module initially auto generated using V5Automation.chm from CATIA V5 R25

from pycatia.system_interfaces.base_object import AnyObject


class Reference(AnyObject):
    """
        .. note::
            CAA V5 Visual Basic help

                | Represents an object pointing to another object.This other object can
                | be either a wireframeactivateLinkAnchor('GeometricElement','','Geometr
                | icElement')object such as a plane or a line, or a boundary
                | representation object such as a face, a vertex or an edge. It may be,
                | in particular, aactivateLinkAnchor('Boundary','','Boundary')object.
                | References are created using appropriate methods for parts. They are
                | then passed to an object to enable associativity with the referenced
                | object.

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.reference = com_object

    @property
    def display_name(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | DisplayName
                | o Property DisplayName(    ) As CATBSTR
                | 
                | Returns the name of the referenced object. The name of the referenced
                | object is either the name displayed in the specification tree for a
                | activateLinkAnchor('GeometricElement','','GeometricElement')  object
                | or a character string defining the reference for a boundary object.
                | Example:The following example returns in StrName the displayable name
                | of reference FirstRef:  StrName = FirstRef.DisplayName

        """
        return self.reference.DisplayName

    def compose_with(self, i_reference):
        """
        .. note::
            CAA V5 Visual Basic help

                | ComposeWith
                | o Func ComposeWith(    Reference    iReference) As Reference
                | 
                | Composes a reference with another reference thus creating a new
                | composite reference.


                | Parameters:
                | iReference
                |    The reference to be composed with the current reference.


                | Examples:
                | 
                | The following example returns in CompositeRef
                | the reference resulting
                | from the composition of the FirstRef
                | and SecondRef references.
                | 
                | Dim CompositeRef As Reference
                | Set CompositeRef = FirstRef.ComposeWith(SecondRef)

        """
        return Reference(self.reference.ComposeWith(i_reference))

    def __repr__(self):
        return f'Reference(name="{self.name}")'
