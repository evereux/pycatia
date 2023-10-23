#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-07-06 14:02:20.222384

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.in_interfaces.reference import Reference
from pycatia.knowledge_interfaces.length import Length
from pycatia.mec_mod_interfaces.hybrid_shape import HybridShape


class HybridShapeRollingOffset(HybridShape):
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
                |                         HybridShapeRollingOffset
                | 
                | The RollingOffset feature
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_rolling_offset = com_object

    @property
    def offset(self) -> Length:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Offset() As Length (Read Only)
                | 
                |     Role: To get_Offset on the object.
                | 
                |     Parameters:
                | 
                |         oOffset
                |             offset value return value for CATScript applications, with
                |             (IDLRETVAL) function type 
                | 
                |     See also:
                |         Length 
                |     Returns:
                |         HRESULT S_OK if Ok E_FAIL else return error code for C++
                |         Implementations 
                |     See also:
                |         HybridShapeFactory

        :rtype: Length
        """

        return Length(self.hybrid_shape_rolling_offset.Offset)

    @property
    def support(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Support() As Reference
                | 
                |     Role: To manage the support on the object.
                | 
                |     Parameters:
                | 
                |         iSupport
                |             return value for CATScript applications, with (IDLRETVAL) function
                |             type 
                | 
                |     See also:
                |         Reference 
                |     Returns:
                |         HRESULT S_OK if Ok E_FAIL else return error code for C++
                |         Implementations 
                |     See also:
                |         HybridShapeFactory

        :rtype: Reference
        """

        return Reference(self.hybrid_shape_rolling_offset.Support)

    @support.setter
    def support(self, reference_support: Reference):
        """
        :param Reference reference_support:
        """

        self.hybrid_shape_rolling_offset.Support = reference_support.com_object

    def get_curve(self, i_pos: int) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func getCurve(long iPos) As Reference
                | 
                |     Role: To get_Curve on the object.
                | 
                |     Parameters:
                | 
                |         iPos
                |             Position 
                | 
                |     See also:
                |         long 
                |     oCurve
                |         return value for CATScript applications, with (IDLRETVAL) function type
                |         
                |     See also:
                |         Reference 
                |     Returns:
                |         HRESULT S_OK if Ok E_FAIL else return error code for C++
                |         Implementations 
                |     See also:
                |         HybridShapeFactory

        :param int i_pos:
        :rtype: Reference
        """
        return Reference(self.hybrid_shape_rolling_offset.getCurve(i_pos))

    def get_nb_curve(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func getNbCurve() As long
                | 
                |     Role: To get_NbCurve on the object.
                | 
                |     Parameters:
                | 
                |         CurvesNb
                |             Number of curves 
                | 
                |     See also:
                |         long 
                |     Returns:
                |         HRESULT S_OK if Ok E_FAIL else return error code for C++
                |         Implementations 
                |     See also:
                |         HybridShapeFactory

        :rtype: int
        """
        return self.hybrid_shape_rolling_offset.getNbCurve()

    def get_offset(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func getOffset() As double
                | 
                |     Role: To getOffset on the object.
                | 
                |     Parameters:
                | 
                |         oOffset
                |             offset value 
                | 
                |     See also:
                |         double 
                |     Returns:
                |         HRESULT S_OK if Ok E_FAIL else return error code for C++
                |         Implementations 
                |     See also:
                |         HybridShapeFactory

        :rtype: float
        """
        return self.hybrid_shape_rolling_offset.getOffset()

    def put_curve(self, i_curve: Reference) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub putCurve(Reference iCurve)
                | 
                |     Role: To add or remove a curve on the object.
                | 
                |     Parameters:
                | 
                |         iCurve
                |             Curve to Add/Remove if not present in the list, or to remove.
                |             
                | 
                |     Returns:
                |         HRESULT S_OK if Ok E_FAIL else return error code for C++
                |         Implementations 
                |     See also:
                |         HybridShapeFactory

        :param Reference i_curve:
        :rtype: None
        """
        return self.hybrid_shape_rolling_offset.putCurve(i_curve.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'put_curve'
        # # vba_code = """
        # # Public Function put_curve(hybrid_shape_rolling_offset)
        # #     Dim iCurve (2)
        # #     hybrid_shape_rolling_offset.putCurve iCurve
        # #     put_curve = iCurve
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def put_offset(self, i_offset: float) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub putOffset(double iOffset)
                | 
                |     Role: To put_Offset on the object.
                | 
                |     Parameters:
                | 
                |         iOffset
                |             offset value 
                | 
                |     See also:
                |         double 
                |     Returns:
                |         HRESULT S_OK if Ok E_FAIL else return error code for C++
                |         Implementations 
                |     See also:
                |         HybridShapeFactory

        :param float i_offset:
        :rtype: None
        """
        return self.hybrid_shape_rolling_offset.putOffset(i_offset)

    def __repr__(self):
        return f'HybridShapeRollingOffset(name="{self.name}")'
