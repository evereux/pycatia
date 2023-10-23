#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.analysis_interfaces.analysis_image import AnalysisImage
from pycatia.system_interfaces.collection import Collection
from pycatia.types.general import cat_variant


class AnalysisImages(Collection):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     AnalysisImages
                | 
                | The collection of analysis images.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object, child_object=AnalysisImage)
        self.analysis_images = com_object

    def add(
            self,
            i_image_name: str,
            i_hide_existing_images: cat_variant,
            i_show_mesh: cat_variant,
            i_duplicate: cat_variant) -> AnalysisImage:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func Add(CATBSTR iImageName,
                | CATVariant iHideExistingImages,
                | CATVariant iShowMesh,
                | CATVariant iDuplicate) As AnalysisImage
                | 
                |     Creates a new image and adds it to the analysis image
                |     collection.
                | 
                |     Parameters:
                | 
                |         iImageName
                |             The name of the image to create. 
                |         iHideExistingImages
                |             To deactivate or not all the activated images before create the new
                |             image. 
                |         iShowMesh
                |             To show or not the mesh image. 
                |         iDuplicate
                |             To duplicate or not the new image, if same image already exists in
                |             collection of images. 
                | 
                |     Returns:
                |         The created Analysis Image 
                |     Example:
                | 
                |           This example create ThisAnalysisImage in the analysisImagesanalysis
                |           
                | 
                |          images collection. The image to create is supposed to be a mesh
                |          deformed image. 
                | 
                |          
                | 
                |          Dim ThisAnalysisImage As AnalysisImage
                |          Set ThisAnalysisImage = analysisImages.Add("Mesh_Deformed", True, False, False)

        :param str i_image_name:
        :param cat_variant i_hide_existing_images:
        :param cat_variant i_show_mesh:
        :param cat_variant i_duplicate:
        :rtype: AnalysisImage
        """
        return AnalysisImage(
            self.analysis_images.Add(
                i_image_name,
                i_hide_existing_images,
                i_show_mesh,
                i_duplicate
            )
        )

    def item(self, i_index: cat_variant) -> AnalysisImage:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func Item(CATVariant iIndex) As AnalysisImage
                | 
                |     Returns an analysis image using its index or its name from the analysis
                |     images collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the analysis image to retrieve from the
                |             collection of analysis images. This index is the rank of the analysis image in
                |             the collection. The index of the first analysis image in the collection is 1,
                |             and the index of the last analysis image is Count.
                |             
                | 
                |     Returns:
                |         The retrieved analysis image 
                |     Example:
                | 
                |           This example retrieves in ThisAnalysisImage the third analysis
                |           image.
                |          
                | 
                |          Dim ThisAnalysisImage As AnalysisImage
                |          Set ThisAnalysisImage = analysisImages.Item(3)

        :param cat_variant i_index:
        :rtype: AnalysisImage
        """
        return AnalysisImage(self.analysis_images.Item(i_index))

    def remove_image(self, i_image_identifier: cat_variant) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub RemoveImage(CATVariant iImageIdentifier)
                | 
                |     Deletes the Analysis Image from the analysis images collection of the
                |     Analysis Set.
                | 
                |     Parameters:
                | 
                |         iImageIdentifier
                |             The index or the name of the analysis image to delete from the
                |             Analysis Set. Note: The index given is the position of the image in the
                |             Analysis Set. Note: The name given is the string got from analysisImage.Name If
                |             the index or the name specified is not present in the Analysis Set, this method
                |             FAILS. The index of the first analysis image in the collection is 1, and the
                |             index of the last analysis image is Count. 
                | 
                |     Example:
                | 
                |           Example 1
                |          In this example analysisImages1 is the Analysis Set and analysisImage1
                |          is the image present in it.
                |          imageName = analysisImage1.Name
                |          analysisImages1.RemoveImage(imageName)
                |          
                |          Example 2
                |          analysisImages1.RemoveImage(4)
                |          In this example 4 is the index of the Image to be deleted in Analysis
                |          Set: analysisImages1

        :param cat_variant i_image_identifier:
        :rtype: None
        """
        return self.analysis_images.RemoveImage(i_image_identifier)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'remove_image'
        # # vba_code = """
        # # Public Function remove_image(analysis_images)
        # #     Dim iImageIdentifier (2)
        # #     analysis_images.RemoveImage iImageIdentifier
        # #     remove_image = iImageIdentifier
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'AnalysisImages(name="{self.name}")'
