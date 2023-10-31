#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.cat_sch_platform_interfaces.sch_list_of_objects import SchListOfObjects
from pycatia.product_structure_interfaces.product import Product


class ElectricalSchematicObject(Product):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     ProductStructureInterfaces.Product
                |                         ElecSchematicObject
                | 
                | Represents the electrical schematic objects.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.elec_schematic_object = com_object

    @property
    def connected_elec_sch_objects(self) -> SchListOfObjects:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ConnectedElecSchObjects() As SchListOfObjects (Read
                | Only)
                | 
                |     This method returns the collection of Electrical Schematic Connected
                |     Objects.

        :rtype: SchListOfObjects
        """

        return SchListOfObjects(self.elec_schematic_object.ConnectedElecSchObjects)

    @property
    def elec_schematic_children(self) -> SchListOfObjects:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ElecSchematicChildren() As SchListOfObjects (Read
                | Only)
                | 
                |     This method returns the collection of Electrical Schematic Object's
                |     Children (component in Pipe Line, Assembly).

        :rtype: SchListOfObjects
        """

        return SchListOfObjects(self.elec_schematic_object.ElecSchematicChildren)

    @property
    def elec_schematic_parent(self) -> 'ElectricalSchematicObject':
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ElecSchematicParent() As ElecSchematicObject (Read
                | Only)
                | 
                |     This method returns the electrical schematic parent.

        :rtype: ElecSchematicObject
        """

        return ElectricalSchematicObject(self.elec_schematic_object.ElecSchematicParent)

    @property
    def is_space_reserved(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property IsSpaceReserved() As boolean (Read Only)
                | 
                |     Defines if the electrical schematic object has a reservation box in 3D
                |     world

        :rtype: bool
        """

        return self.elec_schematic_object.IsSpaceReserved

    @property
    def root_type(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property RootType() As CATBSTR (Read Only)
                | 
                |     Returns the Electrical Schematic Object's Root Type (Equipment, Signal,
                |     Bundle, Wire).

        :rtype: str
        """

        return self.elec_schematic_object.RootType

    @property
    def type(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Type() As CATBSTR (Read Only)
                | 
                |     Returns the Electrical Schematic Object's Type (Alternator, Signal, Bundle,
                |     Wire, ...).

        :rtype: str
        """

        return self.elec_schematic_object.Type

    def get_pin_attribute(self, i_connected_object: 'ElectricalSchematicObject', i_attr_name: str) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetPinAttribute(ElecSchematicObject iConnectedObject,
                | CATBSTR iAttrName) As CATBSTR
                | 
                |     Get the value of an attribute of the pin which connects this and the
                |     specified object.

        :param ElecSchematicObject i_connected_object:
        :param str i_attr_name:
        :rtype: str
        """
        return self.elec_schematic_object.GetPinAttribute(i_connected_object.com_object, i_attr_name)

    def __repr__(self):
        return f'ElectricalSchematicObject(name="{self.name}")'
