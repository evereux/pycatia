#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.abq_automation_interfaces.abq_solution_step_images import ABQSolutionStepImages
from pycatia.analysis_interfaces.analysis_image import AnalysisImage
from pycatia.system_interfaces.any_object import AnyObject
from pycatia.types.general import cat_variant


class ABQSolutionStep(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     ABQSolutionStep
                | 
                | Represents an Abaqus solution step (ABQSolutionStep) object.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.abq_solution_step = com_object

    @property
    def analysis_images(self) -> ABQSolutionStepImages:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property AnalysisImages() As ABQSolutionStepImages (Read
                | Only)
                | 
                |     Returns the analysis images associated with this solution
                |     step.
                | 
                |     Returns:
                |         The collection of analysis images. 
                |     Example:
                |         The following example retrieves the analysis images collection
                |         AnalysisImages in ListSolutionStepImages.
                | 
                |          Dim MySolutionStep As ABQSolutionStep
                |          Dim ListSolutionStepImages As ABQSolutionStepImages
                |          Set ListSolutionStepImages = MySolutionStep.AnalysisImages

        :rtype: ABQSolutionStepImages
        """

        return ABQSolutionStepImages(self.abq_solution_step.AnalysisImages)

    def create_image(
            self,
            i_image_name: str,
            i_hide_existing_images: cat_variant,
            i_incr_or_mode_number: cat_variant) -> AnalysisImage:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func CreateImage(CATBSTR iImageName,
                | CATVariant iHideExistingImages,
                | CATVariant iIncrOrModeNumber) As AnalysisImage
                | 
                |     Creates a new image under this solution step.
                | 
                |     Parameters:
                | 
                |         iImageName
                |             The name of the image to create. 
                |         iHideExistingImages
                |             To deactivate or not all the activated images before create the new
                |             image. 
                |         iIncrOrModeNumber
                |             Increment or mode (for frequency step) number to be set in created
                |             image. 
                | 
                |     Returns:
                |         The created Analysis Image 
                |     Example:
                | 
                |           This example create ThisAnalysisImage in the MySolutionStep.
                |           
                | 
                |          The image to create is supposed to be a mesh deformed image for first
                |          increment. 
                | 
                |          
                | 
                |          Dim MySolutionStep As ABQSolutionStep
                |          Dim ThisAnalysisImage As AnalysisImage
                |          Set ThisAnalysisImage = MySolutionStep.CreateImage("Mesh_Deformed", True, 1)

        :param str i_image_name:
        :param cat_variant i_hide_existing_images:
        :param cat_variant i_incr_or_mode_number:
        :rtype: AnalysisImage
        """
        return AnalysisImage(
            self.abq_solution_step.CreateImage(
                i_image_name,
                i_hide_existing_images,
                i_incr_or_mode_number
            )
        )

    def set_increment_or_mode_number(
            self,
            i_incr_or_mode_number: cat_variant,
            i_image: AnalysisImage) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetIncrementOrModeNumber(CATVariant iIncrOrModeNumber,
                | AnalysisImage iImage)
                | 
                |     Sets increment number for an image.
                |     This is done related to an existing image
                | 
                |     Parameters:
                | 
                |         iIncrOrModeNumber
                |             The increment or mode (for frequency step) number to
                |             select

        :param cat_variant i_incr_or_mode_number:
        :param AnalysisImage i_image:
        :rtype: None
        """
        return self.abq_solution_step.SetIncrementOrModeNumber(
            i_incr_or_mode_number,
            i_image.com_object
        )
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_increment_or_mode_number'
        # # vba_code = """
        # # Public Function set_increment_or_mode_number(abq_solution_step)
        # #     Dim iIncrOrModeNumber (2)
        # #     abq_solution_step.SetIncrementOrModeNumber iIncrOrModeNumber
        # #     set_increment_or_mode_number = iIncrOrModeNumber
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'ABQSolutionStep(name="{self.name}")'
