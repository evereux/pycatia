#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.eno_cd5_interfaces.cd5_engine import CD5Engine
from pycatia.eno_cd5_interfaces.cd5_save_operation import CD5SaveOperation


class CD5EngineV6R2014x(CD5Engine):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     ENOCD5Interfaces.CD5Engine
                |                         CD5EngineV6R2014x
                | 
                | Represents the ENOVIA V6 Integration Engine, that is to say the entry point to
                | the CATIA/ENOVIA V6 Integration.
                | 
                | It allows end user to realize ENOVIA V6 Integration operations such as
                | Connection, Disconnection, Open, Save...
                | Note that all operations performed from this interface are the same as
                | operations available in the ENOVIA V6 menu in CATIA, unless most of them are
                | executed without panel.
                | 
                | Example:
                | 
                |       The following example indicates how to retrieve the ENOVIA V6 Integration
                |       Engine.
                |
                |      Dim oCD5Engine As CD5EngineV6R2014x
                |      Set oCD5Engine = CATIA.GetItem("CD5EngineV6R2014x")
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.cd5_engine_v6_r2014x = com_object

    def create_save_operation(self, i_scope: int) -> CD5SaveOperation:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func CreateSaveOperation(CD5SaveOperation_Scope iScope) As
                | CD5SaveOperation
                |
                |     Creates the basic Save Operation object. It requires ENOVIA V6
                |     connection.
                |
                |     Parameters:
                |
                |         iScope
                |             The scope of the Save Operation.
                |
                |     Returns:
                |         The created Save Operation.
                |     Throws:
                |
                |         -1697450280 : CATIA is not connected to ENOVIA V6.
                |
                |     Example:
                |
                |           The following example creates a Save Operation with the whole session
                |           as scope on CD5Engine oCD5Engine:
                |
                |          Dim SaveOperation As CD5SaveOperation
                |          Set SaveOperation = oCD5Engine.CreateSaveOperation(CD5SaveOperation_Session)

        :param int i_scope: enum cd5_save_operation_scope
        :rtype: CD5SaveOperation
        """
        return CD5SaveOperation(self.cd5_engine_v6_r2014x.CreateSaveOperation(i_scope).com_object)

    def generate_autoname(self, i_autoname_series: str, i_count: int) -> tuple:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GenerateAutoname(CATBSTR iAutonameSeries,
                | short iCount) As CATSafeArrayVariant
                |
                |     Generates and gets the Autonames for the given series. It requires ENOVIA
                |     V6 connection.
                |
                |     Parameters:
                |
                |         iAutonameSeries
                |             The Autoname Series for which we want to generate Autonames.
                |
                |         iCount
                |             The number of Autonames to be generated.
                |
                |     Returns:
                |         The array of generated Autonames.
                |     Throws:
                |
                |         -1697450280 : CATIA is not connected to ENOVIA V6.
                |
                |     Example:
                |
                |           The following example generates and gets 1 Autoname for series "A
                |           Size":
                |
                |          Dim Autoname As CATBSTR
                |          Autoname = oCD5Engine.GenerateAutoname("A Size", 1)(0)

        :param str i_autoname_series:
        :param int i_count:
        :rtype: tuple
        """
        return self.cd5_engine_v6_r2014x.GenerateAutoname(i_autoname_series, i_count)

    def get_autoname_series(self, i_type: str) -> tuple:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetAutonameSeries(CATBSTR iType) As
                | CATSafeArrayVariant
                |
                |     Gets the Autoname Series for an input type. It requires ENOVIA V6
                |     connection.
                |
                |     Parameters:
                |
                |         iType
                |             The ENOVIA type of the Object ("CATIA Embedded Component"...).
                |
                |
                |     Returns:
                |         The array of Autoname Series.
                |     Throws:
                |
                |         -1697450280 : CATIA is not connected to ENOVIA V6.
                |
                |     Example:
                |
                |           The following example gets autoname series for CATIA Embedded
                |           Component:
                |
                |          Dim AutonameSeries As CATSafeArrayVariant
                |          AutonameSeries = oCD5Engine.GetAutonameSeries("CATIA Embedded Component")

        :param str i_type:
        :rtype: tuple
        """
        return self.cd5_engine_v6_r2014x.GetAutonameSeries(i_type)

    def __repr__(self):
        return f'CD5EngineV6R2014x(name="{self.name}")'
