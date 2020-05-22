#! /usr/bin/python3.6
# module initially auto generated using V5Automation.chm from CATIA R25 on 2020-05-22 12:54:36.956119

from pycatia.mec_mod_interfaces.hybridshape import HybridShape


class HybridShapeRollingOffset(HybridShape):
    """
        .. note::
            CAA V5 Visual Basic help

                | The RollingOffset feature

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_rolling_offset = com_object     

    @property
    def offset(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Offset
                | o Property Offset(    ) As   (Read Only)
                | 
                | Role: To get_Offset on the object.

        :return:
        """
        return self.hybrid_shape_rolling_offset.Offset

    @property
    def support(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Support
                | o Property Support(    ) As
                | 
                | Role: To manage the support on the object.

        :return:
        """
        return self.hybrid_shape_rolling_offset.Support

    def get_curve(self, i_pos):
        """
        .. note::
            CAA V5 Visual Basic help

                | getCurve
                | o Func getCurve(        iPos) As
                | 
                | Role: To get_Curve on the object.
                |
                | Parameters:
                | iPos
                |     Position
                |    
                | 
                |  See also:
                |  long
                |      oCurve
                |    return value for CATScript applications, with (IDLRETVAL) function type
                |    
                |  See also:
                |  
                |  Returns:
                |   HRESULT    S_OK   if Ok 
                |    E_FAIL else 
                |    return error code for C++ Implementations
                |  
                |    See also:


        :param i_pos:
        :return:
        """
        return self.hybrid_shape_rolling_offset.getCurve(i_pos)

    def get_nb_curve(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | getNbCurve
                | o Func getNbCurve(    ) As
                | 
                | Role: To get_NbCurve on the object.
                |
                | Parameters:
                | CurvesNb
                |    Number of curves
                |    
                | 
                |  See also:
                |  long
                |    Returns:
                |   HRESULT    S_OK   if Ok 
                |    E_FAIL else 
                |    return error code for C++ Implementations
                |  
                |    See also:


        :return:
        """
        return self.hybrid_shape_rolling_offset.getNbCurve()

    def get_offset(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | getOffset
                | o Func getOffset(    ) As
                | 
                | Role: To getOffset on the object.
                |
                | Parameters:
                | oOffset
                |     offset value 
                |    
                | 
                |  See also:
                |  double
                |    Returns:
                |   HRESULT    S_OK   if Ok 
                |    E_FAIL else 
                |    return error code for C++ Implementations
                |  
                |    See also:


        :return:
        """
        return self.hybrid_shape_rolling_offset.getOffset()

    def put_curve(self, i_curve):
        """
        .. note::
            CAA V5 Visual Basic help

                | putCurve
                | o Sub putCurve(        iCurve)
                | 
                | Role: To add or remove a curve on the object.
                |
                | Parameters:
                | iCurve
                |    Curve to Add/Remove if not present in the list, or to remove.
                |  
                | 
                |  Returns:
                |   HRESULT    S_OK   if Ok 
                |    E_FAIL else 
                |    return error code for C++ Implementations
                |  
                |    See also:


        :param i_curve:
        :return:
        """
        return self.hybrid_shape_rolling_offset.putCurve(i_curve)

    def put_offset(self, i_offset):
        """
        .. note::
            CAA V5 Visual Basic help

                | putOffset
                | o Sub putOffset(        iOffset)
                | 
                | Role: To put_Offset on the object.
                |
                | Parameters:
                | iOffset
                |     offset value
                |    
                | 
                |  See also:
                |  double
                |    Returns:
                |   HRESULT    S_OK   if Ok 
                |    E_FAIL else 
                |    return error code for C++ Implementations
                |  
                |    See also:


        :param i_offset:
        :return:
        """
        return self.hybrid_shape_rolling_offset.putOffset(i_offset)

    def __repr__(self):
        return f'HybridShapeRollingOffset()'
