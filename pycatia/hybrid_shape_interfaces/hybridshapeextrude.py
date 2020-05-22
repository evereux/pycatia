#! /usr/bin/python3.6
# module initially auto generated using V5Automation.chm from CATIA R25 on 2020-05-22 12:54:36.956119

from pycatia.mec_mod_interfaces.hybridshape import HybridShape


class HybridShapeExtrude(HybridShape):
    """
        .. note::
            CAA V5 Visual Basic help

                | The Extrude feature : an Extrude is made up of a face to process and
                | one Extrude parameter.Role: To access the data of the hybrid shape
                | extrude feature object.

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_extrude = com_object     

    @property
    def begin_offset(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | BeginOffset
                | o Property BeginOffset(    ) As   (Read Only)
                | 
                | Role: To get_BeginOffset on the object. For surface extrude,
                | if limit type is upto, this offset value is not used. In
                | case of Volume Extrude, if the up-to element is specified,
                | this will act as offset value from the upto element.

        :return:
        """
        return self.hybrid_shape_extrude.BeginOffset

    @property
    def context(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Context
                | o Property Context(    ) As
                | 
                | Returns or sets the context on Extrude feature. Legal
                | values: 0 This option creates surface of extrusion. 1 This
                | option creates volume of extrusion. Note: Setting volume
                | result requires GSO License. 
                |
                | Example:
                | This example retrieves
                | in oContext the context for the Extrude1 hybrid shape
                | feature. Dim oContext Set oContext = Extrude1.Context

        :return:
        """
        return self.hybrid_shape_extrude.Context

    @context.setter
    def context(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_extrude.Context = value 

    @property
    def direction(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Direction
                | o Property Direction(    ) As
                | 
                | Role: To get_Direction on the object.

        :return:
        """
        return self.hybrid_shape_extrude.Direction

    @property
    def end_offset(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | EndOffset
                | o Property EndOffset(    ) As   (Read Only)
                | 
                | Role: To get_EndOffset on the object. For surface extrude,
                | if limit type is upto, this offset value is not used. In
                | case of Volume Extrude, if the up-to element is specified,
                | this will act as offset value from the upto element.

        :return:
        """
        return self.hybrid_shape_extrude.EndOffset

    @property
    def extruded_object(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | ExtrudedObject
                | o Property ExtrudedObject(    ) As
                | 
                | Role: To get_ExtrudedObject on the object.

        :return:
        """
        return self.hybrid_shape_extrude.ExtrudedObject

    @property
    def first_limit_type(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | FirstLimitType
                | o Property FirstLimitType(    ) As
                | 
                | Returns or sets the First limit type. Legal values: 0
                | Unknown Limit type. 1 Limit type is Dimension. It implies
                | that limit is defined by length 2 Limit type is UptoElement.
                | It implies that limit is defined by a geometrical element

        :return:
        """
        return self.hybrid_shape_extrude.FirstLimitType

    @first_limit_type.setter
    def first_limit_type(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_extrude.FirstLimitType = value 

    @property
    def first_upto_element(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | FirstUptoElement
                | o Property FirstUptoElement(    ) As
                | 
                | Returns or sets the First up-to element used to limit
                | extrusion. 
                |
                | Example:
                | This example retrieves in Lim1Elem the
                | First up-to element for the Extrude hybrid shape feature.
                | Dim Lim1Elem As Reference Set Lim1Elem =
                | Extrude.FirstUptoElement

        :return:
        """
        return self.hybrid_shape_extrude.FirstUptoElement

    @first_upto_element.setter
    def first_upto_element(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_extrude.FirstUptoElement = value 

    @property
    def orientation(self, i_orientation):
        """
        .. note::
            CAA V5 Visual Basic help

                | Orientation
                | o Property Orientation(        iOrientation)
                | 
                | Gets or sets orientation of the extrude. Orientation = TRUE
                | : The natural orientation is taken. = FALSE : The opposite
                | orientation is taken This example retrieves in IsInverted
                | orientation of the extrude for the Extrude hybrid shape
                | feature. Dim IsInverted As boolean IsInverted =
                | Extrude.Orientation

        :param i_orientation:
        :return:
        """
        return self.hybrid_shape_extrude.Orientation

    @property
    def second_limit_type(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | SecondLimitType
                | o Property SecondLimitType(    ) As
                | 
                | Returns or sets the Second limit type. Legal values: 0
                | Unknown Limit type. 1 Limit type is Dimension. It implies
                | that limit is defined by length 2 Limit type is UptoElement.
                | It implies that limit is defined by a geometrical element

        :return:
        """
        return self.hybrid_shape_extrude.SecondLimitType

    @second_limit_type.setter
    def second_limit_type(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_extrude.SecondLimitType = value 

    @property
    def second_upto_element(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | SecondUptoElement
                | o Property SecondUptoElement(    ) As
                | 
                | Returns or sets the Second up-to element used to limit
                | extrusion. 
                |
                | Example:
                | This example retrieves in Lim2Elem the
                | Second up-to element for the Extrude hybrid shape feature.
                | Dim Lim2Elem As Reference Set Lim2Elem =
                | Extrude.SecondUptoElement

        :return:
        """
        return self.hybrid_shape_extrude.SecondUptoElement

    @second_upto_element.setter
    def second_upto_element(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_extrude.SecondUptoElement = value 

    @property
    def symmetrical_extension(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | SymmetricalExtension
                | o Property SymmetricalExtension(    ) As
                | 
                | Returns or Sets the Symmetrical Extension of Extrude (Limit
                | 2 = -Limit 1).

        :return:
        """
        return self.hybrid_shape_extrude.SymmetricalExtension

    def __repr__(self):
        return f'HybridShapeExtrude()'
