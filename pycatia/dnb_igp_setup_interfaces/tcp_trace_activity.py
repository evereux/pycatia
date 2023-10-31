#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.dmaps_interfaces.activity import Activity


class TCPTraceActivity(Activity):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     DMAPSInterfaces.Activity
                |                         TCPTraceActivity
                | 
                | Interface representing TCPTraceActivity.
                | 
                | Role: This interface is used to work with TCPTraceActivity which consists of a
                | various attributes.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.tcp_trace_activity = com_object

    def get_line_colour(self, o_r: int, o_g: int, o_b: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetLineColor(long oR,
                | long oG,
                | long oB)
                | 
                |     Indicates the line Color property of trace.
                | 
                |     Parameters:
                | 
                |         oR,oG,oB
                |             long. Get the line Color property defined in the trace
                |             activity(R,G,B values).

        :param int o_r:
        :param int o_g:
        :param int o_b:
        :rtype: None
        """
        return self.tcp_trace_activity.GetLineColor(o_r, o_g, o_b)

    def get_line_thickness(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetLineThickness() As long
                | 
                |     Indicates the line thickness property of trace.
                | 
                |     Parameters:
                | 
                |         oThickness
                |             long. Get the line thickness property defined in the trace
                |             activity.

        :rtype: int
        """
        return self.tcp_trace_activity.GetLineThickness()

    def get_line_type(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetLineType() As long
                | 
                |     Indicates the line type property of trace.
                | 
                |     Parameters:
                | 
                |         oType
                |             long. Get the line type property defined in the trace
                |             activity.

        :rtype: int
        """
        return self.tcp_trace_activity.GetLineType()

    def get_tcp_trace_mode(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetTCPTraceMode() As boolean
                | 
                |     Indicates if the tracing capability is active or not.
                | 
                |         True: tracing capability activated
                |         False: tracing capability deactivated
                | 
                |     Parameters:
                | 
                |         oTCPTraceMode
                |             Boolean. Indicates if the tracing capability is active or
                |             not.

        :rtype: bool
        """
        return self.tcp_trace_activity.GetTCPTraceMode()

    def set_line_colour(self, i_r: int, i_g: int, i_b: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetLineColor(long iR,
                | long iG,
                | long iB)
                | 
                |     Indicates the line Color property of trace.
                | 
                |     Parameters:
                | 
                |         iR,iG,iB
                |             long. Set the line Color property for the trace activity(R,G,B
                |             values).

        :param int i_r:
        :param int i_g:
        :param int i_b:
        :rtype: None
        """
        return self.tcp_trace_activity.SetLineColor(i_r, i_g, i_b)

    def set_line_thickness(self, i_thickness: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetLineThickness(long iThickness)
                | 
                |     Indicates the line thickness property of trace.
                | 
                |     Parameters:
                | 
                |         iThickness
                |             long. Set the line thickness property for the trace
                |             activity.

        :param int i_thickness:
        :rtype: None
        """
        return self.tcp_trace_activity.SetLineThickness(i_thickness)

    def set_line_type(self, i_type: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetLineType(long iType)
                | 
                |     Indicates the line type property of trace.
                | 
                |     Parameters:
                | 
                |         iType
                |             long. Set the line type property for the trace.

        :param int i_type:
        :rtype: None
        """
        return self.tcp_trace_activity.SetLineType(i_type)

    def set_tcp_trace_mode(self, i_tcp_trace_mode: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetTCPTraceMode(boolean iTCPTraceMode)
                | 
                |     Set the tracing capability as active or not.
                | 
                |         True: tracing capability activated
                |         False: tracing capability deactivated
                | 
                |     Parameters:
                | 
                |         iTCPTraceMode
                |             Boolean. Value to set.

        :param bool i_tcp_trace_mode:
        :rtype: None
        """
        return self.tcp_trace_activity.SetTCPTraceMode(i_tcp_trace_mode)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_tcp_trace_mode'
        # # vba_code = """
        # # Public Function set_tcp_trace_mode(tcp_trace_activity)
        # #     Dim iTCPTraceMode (2)
        # #     tcp_trace_activity.SetTCPTraceMode iTCPTraceMode
        # #     set_tcp_trace_mode = iTCPTraceMode
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'TCPTraceActivity(name="{self.name}")'
