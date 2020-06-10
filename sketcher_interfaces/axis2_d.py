#! usr/bin/python3.6
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-09 09:53:18.676780

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""




class Axis2D(Geometry2D):

    """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SketcherInterfaces.GeometricElement
                |                         SketcherInterfaces.Geometry2D
                |                             Axis2D
                | 
                | Interface defining a coordinate system in the 2D Space.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.axis2_d = com_object

    @property
    def horizontal_reference(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property HorizontalReference() As Line2D (Read Only)
                | 
                |     Returns the 2D coordinate system horizontal axis.

        :return: Line2D
        """

        return Line2D(self.axis2_d.HorizontalReference)

    @property
    def origin(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property Origin() As Point2D (Read Only)
                | 
                |     Returns the 2D coordinate system origin.

        :return: Point2D
        """

        return Point2D(self.axis2_d.Origin)

    @property
    def vertical_reference(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property VerticalReference() As Line2D (Read Only)
                | 
                |     Returns the 2D coordinate system vertical axis.

        :return: Line2D
        """

        return Line2D(self.axis2_d.VerticalReference)

    def __repr__(self):
        return f'Axis2D(name="{ self.name }")'
