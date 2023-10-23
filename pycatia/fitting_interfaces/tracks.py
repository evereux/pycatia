#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.fitting_interfaces.sampleds import Sampleds


class Tracks(Sampleds):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     FittingInterfaces.Sampleds
                |                         Tracks
                | 
                | A collection of all the track objects contained in the current
                | document.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.tracks = com_object

    def add_from_file(self, i_file_name: str) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub AddFromFile(CATBSTR iFileName)
                | 
                |     Creates a track in the collection, from information from an external
                |     file.
                | 
                |     Parameters:
                | 
                |         iFileName
                |             The path to a valid xml file. 
                |         Example:
                |             The following example reads a file called exmple.xml and creates a
                |             track in the tracks collection.
                | 
                |              myTracks.AddFromFile ("example.xml")

        :param str i_file_name:
        :rtype: None
        """
        return self.tracks.AddFromFile(i_file_name)

    def __repr__(self):
        return f'Tracks(name="{self.name}")'
