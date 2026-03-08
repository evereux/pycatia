#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R34 on 2026-03-08 14:35:32.197861

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
import inspect

from pycatia.manufacturing_interfaces.manufacturing_feature import ManufacturingFeature


class ManufacturingPattern2(ManufacturingFeature):
    """

    Introduced in V5-6R2024.

            .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2026-03-08 14:35:32.197861)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                    ManufacturingInterfaces.ManufacturingFeature
                |                         ManufacturingPattern2
                | 
                | The Manufacturing Pattern is a specialized feature used to machine the same
                | item several times at several positions.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)

        self.release_check(
            self.application.system_configuration.release,
            34,
            f'{self.__class__.__name__}.{inspect.stack()[0][3]}',
        )

        self.com_object = com_object

    def set_pp_words_for_positions(self, i_point_number: int, i_list_pp_words: tuple) -> None:
        """

        Introduced in V5-6R2024.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2026-03-08 14:35:32.197861))
                | Sub SetPPWordsForPositions(short iPointNumber,CATSafeArrayVariant
                | ilistPPWords)
                |     Set all the PPWord lines of the record .
                | 
                |     Parameters:
                | 
                |         iPointNumber
                |             The number of the point 
                |         ilistPPWords
                |             The PPWords list of string 
                | 
                |     Example:
                |
                |          Dim Pattern
                |          Set Pattern = Operation.GetPattern()
                |          Dim textPPWord(2)
                |          textPPWord(0) = "PPWord1"
                |          textPPWord(1) = "PPWord2"
                |          Pattern.SetPPWordsForPositions 1, textPPWord

        :param int i_point_number:
        :param tuple i_list_pp_words:
        :rtype: None
        """
        return self.com_object.SetPPWordsForPositions(i_point_number, i_list_pp_words)

    def __repr__(self):
        return f'ManufacturingPattern2(name="{self.name}")'
