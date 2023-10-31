#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.drafting_interfaces.drawing_component import DrawingComponent
from pycatia.system_interfaces.any_object import AnyObject
from pycatia.cat_tps_interfaces.tps_parallel_on_screen import TPSParallelOnScreen
from pycatia.types.general import cat_variant


class Noa(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     Noa
                | 
                | Interface for the TPS Noa object.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.noa = com_object

    @property
    def flag_text(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property FlagText() As CATBSTR
                | 
                |     Retrieves or sets Flag Text.
                | 
                |     Parameters:
                | 
                |         oText
                |             Returned text for NOA hidden text.

        :rtype: str
        """

        return self.noa.FlagText

    @flag_text.setter
    def flag_text(self, value: str):
        """
        :param str value:
        """

        self.noa.FlagText = value

    @property
    def text(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Text() As CATBSTR
                | 
                |     Retrieves or sets Text Representation.
                | 
                |     Parameters:
                | 
                |         oText
                |             Returned text for graphical representation.

        :rtype: str
        """

        return self.noa.Text

    @text.setter
    def text(self, value: str):
        """
        :param str value:
        """

        self.noa.Text = value

    def add_url(self, i_url: str) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub AddURL(CATBSTR iUrl)
                | 
                |     Sets an URL.
                | 
                |     Parameters:
                | 
                |         iUrl
                |             URL to Set

        :param str i_url:
        :rtype: None
        """
        return self.noa.AddURL(i_url)

    def get_ditto(self) -> DrawingComponent:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetDitto() As DrawingComponent
                | 
                |     Gets the ditto as a DrawingComponent of the Noa entity.

        :rtype: DrawingComponent
        """
        return DrawingComponent(self.noa.GetDitto())

    def get_modifiable_text(self, i_index: cat_variant) -> AnyObject:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetModifiableText(CATVariant iIndex) As AnyObject
                | 
                |     Gets by index a modifiable Text included in the ditto which represents this
                |     NOA.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             Index of the modifiable text. 
                |         oText
                |             returns a CATIADrawingText

        :param cat_variant i_index:
        :rtype: AnyObject
        """
        return AnyObject(self.noa.GetModifiableText(i_index))

    def get_modifiable_texts_count(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetModifiableTextsCount() As long
                | 
                |     Gets the number of modifiable texts included in the ditto which represents
                |     this NOA.
                | 
                |     Parameters:
                | 
                |         oCount
                |             returns the number of modifiable text included into the ditto which
                |             represents this NOA.

        :rtype: int
        """
        return self.noa.GetModifiableTextsCount()

    def get_nbr_url(self, o_number_of_url: cat_variant) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetNbrURL(CATVariant oNumberOfURL)
                | 
                |     Deprecated:
                |         V5-6R2017 This method is replaced by Noa.GetNbrURL2

        :param cat_variant o_number_of_url:
        :rtype: None
        """
        return self.noa.GetNbrURL(o_number_of_url)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_nbr_url'
        # # vba_code = """
        # # Public Function get_nbr_url(noa)
        # #     Dim oNumberOfURL (2)
        # #     noa.GetNbrURL oNumberOfURL
        # #     get_nbr_url = oNumberOfURL
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_nbr_url_2(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetNbrURL2() As long
                | 
                |     Gets the number of URL.
                | 
                |     Parameters:
                | 
                |         oNumberOfURL
                |             returns param oNumberOfURL.

        :rtype: int
        """
        return self.noa.GetNbrURL2()

    def modify_url(self, i_url: str, i_index: cat_variant) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub ModifyURL(CATBSTR iUrl,
                | CATVariant iIndex)
                | 
                |     Modifies an URL.
                | 
                |     Parameters:
                | 
                |         iUrl
                |             URL to Set. 
                |         iIndex
                |             index of the URL to modify.

        :param str i_url:
        :param cat_variant i_index:
        :rtype: None
        """
        return self.noa.ModifyURL(i_url, i_index)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'modify_url'
        # # vba_code = """
        # # Public Function modify_url(noa)
        # #     Dim iUrl (2)
        # #     noa.ModifyURL iUrl
        # #     modify_url = iUrl
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def remove_url(self, i_index: cat_variant) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub RemoveURL(CATVariant iIndex)
                | 
                |     Removes an URL.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             position of the URL to remove.

        :param cat_variant i_index:
        :rtype: None
        """
        return self.noa.RemoveURL(i_index)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'remove_url'
        # # vba_code = """
        # # Public Function remove_url(noa)
        # #     Dim iIndex (2)
        # #     noa.RemoveURL iIndex
        # #     remove_url = iIndex
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def tps_parallel_on_screen(self) -> TPSParallelOnScreen:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func TPSParallelOnScreen() As TPSParallelOnScreen
                | 
                |     Gets the annotation on TPSParallelOnScreen interface.

        :rtype: TPSParallelOnScreen
        """

        return TPSParallelOnScreen(self.noa.TPSParallelOnScreen())

    def url(self, i_index: cat_variant) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func URL(CATVariant iIndex) As CATBSTR
                | 
                |     Retrieves URL.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             Index of URL. 
                |         oUrl
                |             URL

        :param cat_variant i_index:
        :rtype: str
        """
        return self.noa.URL(i_index)

    def __repr__(self):
        return f'Noa(name="{self.name}")'
