#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-07-06 14:02:20.222384

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.in_interfaces.reference import Reference
from pycatia.mec_mod_interfaces.hybrid_shape import HybridShape


class Line(HybridShape):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.HybridShape
                |                         Line
                | 
                | Represents the hybrid shape Line feature object.
                | Role: Declare hybrid shape Line root feature object. All interfaces for
                | different type of Line derives HybridShapeLine.
                | 
                | Use the CATIAHybridShapeFactory to create a HybridShapeLine
                | objects.
                | 
                | See also:
                |     HybridShapeFactory
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.line = com_object

    @property
    def first_upto_elem(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property FirstUptoElem() As Reference
                | 
                |     Role: Gets the First upto element of the line.
                | 
                |     Parameters:
                | 
                |         oFirstUpto
                | 
                |     Returns:
                |         HRESULT S_OK if Ok E_FAIL else

        :rtype: Reference
        """

        return Reference(self.line.FirstUptoElem)

    @first_upto_elem.setter
    def first_upto_elem(self, reference_element: Reference):
        """
        :param Reference reference_element:
        """

        self.line.FirstUptoElem = reference_element.com_object

    @property
    def second_upto_elem(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property SecondUptoElem() As Reference
                | 
                |     Role: Gets the Second upto element of the line.
                | 
                |     Parameters:
                | 
                |         oSecondUpto
                | 
                |     Returns:
                |         HRESULT S_OK if Ok E_FAIL else

        :rtype: Reference
        """

        return Reference(self.line.SecondUptoElem)

    @second_upto_elem.setter
    def second_upto_elem(self, reference_element: Reference):
        """
        :param Reference reference_element:
        """

        self.line.SecondUptoElem = reference_element.com_object

    def get_direction(self) -> tuple:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub GetDirection(CATSafeArrayVariant oDirection)
                | 
                |     Role: Returns the unit-vector pointing in the direction of the
                |     line.
                | 
                |     Parameters:
                | 
                |         oDirection
                |         oDirection[0]
                |             The X Coordinate of the unit vector pointing in the direction of
                |             the line 
                |         oDirection[1]
                |             The Y Coordinate of the unit vector pointing in the direction of
                |             the line 
                |         oDirection[2]
                |             The Z Coordinate of the unit vector pointing in the direction of
                |             the line 
                | 
                |     Returns:
                |         HRESULT S_OK if Ok E_FAIL else return error code for C++
                |         Implementations 
                |     See also:
                |         HybridShapeFactory

        :rtype: None
        """
        vba_function_name = "get_direction"
        vba_code = """
        Public Function get_direction(line)
            Dim oDirection (2)
            line.GetDirection oDirection
            get_direction = oDirection
        End Function
        """

        system_service = self.application.system_service
        return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_origin(self, o_origin: tuple) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub GetOrigin(CATSafeArrayVariant oOrigin)
                | 
                |     Role: Returns the origin of the line.
                | 
                |     Parameters:
                | 
                |         oOrigin
                |         oOrigin[0]
                |             The X Coordinate of a point lying on the line 
                |         oOrigin[1]
                |             The Y Coordinate of a point lying on the line 
                |         oOrigin[2]
                |             The Z Coordinate of a point lying on the line The Origin is
                |             evaluated from the geometry of the line. 
                | 
                |     Returns:
                |         HRESULT S_OK if Ok E_FAIL else return error code for C++
                |         Implementations 
                |     See also:
                |         HybridShapeFactory

        :param tuple o_origin:
        :rtype: None
        """
        return self.line.GetOrigin(o_origin)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_origin'
        # # vba_code = """
        # # Public Function get_origin(line)
        # #     Dim oOrigin (2)
        # #     line.GetOrigin oOrigin
        # #     get_origin = oOrigin
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def put_direction(self, i_direction: tuple) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub PutDirection(CATSafeArrayVariant iDirection)
                | 
                |     Role: Sets the unit-vector pointing in the direction of the
                |     line.
                | 
                |     Parameters:
                | 
                |         iDirection
                |         iDirection[0]
                |             The X Coordinate of the unit vector pointing in the direction of
                |             the line 
                |         iDirection[1]
                |             The Y Coordinate of the unit vector pointing in the direction of
                |             the line 
                |         iDirection[2]
                |             The Z Coordinate of the unit vector pointing in the direction of
                |             the line 
                | 
                |     Returns:
                |         HRESULT S_OK if Ok E_FAIL else return error code for C++
                |         Implementations 
                |     See also:
                |         HybridShapeFactory

        :param tuple i_direction:
        :rtype: None
        """
        return self.line.PutDirection(i_direction)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'put_direction'
        # # vba_code = """
        # # Public Function put_direction(line)
        # #     Dim iDirection (2)
        # #     line.PutDirection iDirection
        # #     put_direction = iDirection
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'Line(name="{self.name}")'
