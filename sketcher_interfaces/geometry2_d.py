#! usr/bin/python3.6
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-09 09:53:18.676780

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""




class Geometry2D(GeometricElement):

    """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SketcherInterfaces.GeometricElement
                |                         Geometry2D
                | 
                | 2D wireframe geometric element.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.geometry2_d = com_object

    @property
    def construction(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property Construction() As boolean
                | 
                |     Returns the construction mode of the 2D geometry

        :return: bool
        """

        return self.geometry2_d.Construction

    @construction.setter
    def construction(self, value):
        """
        :param bool value:
        """

        self.geometry2_d.Construction = value

    @property
    def report_name(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property ReportName() As long
                | 
                |     Returns the report name of the 2D geometry
                | 
                |     Parameters:
                | 
                |         oReportName
                |             The integer value of the report name

        :return: int
        """

        return self.geometry2_d.ReportName

    @report_name.setter
    def report_name(self, value):
        """
        :param int value:
        """

        self.geometry2_d.ReportName = value

    def __repr__(self):
        return f'Geometry2D(name="{ self.name }")'
