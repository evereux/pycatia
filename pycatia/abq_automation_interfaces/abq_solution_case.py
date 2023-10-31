#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.abq_automation_interfaces.abq_solution_case_images import ABQSolutionCaseImages
from pycatia.abq_automation_interfaces.abq_solution_steps import ABQSolutionSteps
from pycatia.analysis_interfaces.analysis_image import AnalysisImage
from pycatia.system_interfaces.any_object import AnyObject
from pycatia.types.general import cat_variant


class ABQSolutionCase(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     ABQSolutionCase
                | 
                | Represents an Abaqus solution case (ABQSolutionCase) object.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.abq_solution_case = com_object

    @property
    def analysis_images(self) -> ABQSolutionCaseImages:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property AnalysisImages() As ABQSolutionCaseImages (Read
                | Only)
                | 
                |     Returns the analysis images associated with this solution
                |     case.
                | 
                |     Returns:
                |         The collection of analysis images. 
                |     Example:
                |         The following example retrieves the analysis images collection
                |         AnalysisImages in ListSolutionCaseImages.
                | 
                |          Dim MySolutionCase As ABQSolutionCase
                |          Dim ListSolutionCaseImages As ABQSolutionCaseImages
                |          Set ListSolutionCaseImages = MySolutionCase.AnalysisImages

        :rtype: ABQSolutionCaseImages
        """

        return ABQSolutionCaseImages(self.abq_solution_case.AnalysisImages)

    @property
    def solution_steps(self) -> ABQSolutionSteps:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property SolutionSteps() As ABQSolutionSteps (Read Only)
                | 
                |     Returns the Abaqus solution steps associated with this solution
                |     case.
                | 
                |     Returns:
                |         The collection of solution steps. 
                |     Example:
                |         The following example retrieves the Abaqus solution steps collection
                |         SolutionSteps in ListSolutionSteps.
                | 
                |          Dim MySolutionCase As ABQSolutionCase
                |          Dim ListSolutionSteps As ABQSolutionSteps
                |          Set ListSolutionSteps = MySolutionCase.SolutionSteps

        :rtype: ABQSolutionSteps
        """

        return ABQSolutionSteps(self.abq_solution_case.SolutionSteps)

    def create_image(
            self,
            i_image_name: str,
            i_hide_existing_images: cat_variant,
            i_step_number: cat_variant,
            i_increment_number: cat_variant) -> AnalysisImage:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func CreateImage(CATBSTR iImageName,
                | CATVariant iHideExistingImages,
                | CATVariant iStepNumber,
                | CATVariant iIncrementNumber) As AnalysisImage
                | 
                |     Creates a new image under this solution case.
                | 
                |     Parameters:
                | 
                |         iImageName
                |             The name of the image to create. 
                |         iHideExistingImages
                |             To deactivate or not all the activated images before create the new
                |             image. 
                |         iStepNumber
                |             Step number to be set in created image. 
                |         iIncrementNumber
                |             Increment number to be set in created image. 
                | 
                |     Returns:
                |         The created Analysis Image 
                |     Example:
                | 
                |           This example create ThisAnalysisImage in the MySolutionCase.
                |           
                |          The image to create is supposed to be a mesh deformed image for first
                |          increment of first step. 
                | 
                |          Dim MySolutionCase As ABQSolutionCase
                |          Dim ThisAnalysisImage As AnalysisImage
                |          Set ThisAnalysisImage = MySolutionCase.CreateImage("Mesh_Deformed", True, 1, 1)

        :param str i_image_name:
        :param cat_variant i_hide_existing_images:
        :param cat_variant i_step_number:
        :param cat_variant i_increment_number:
        :rtype: AnalysisImage
        """
        return AnalysisImage(
            self.abq_solution_case.CreateImage(
                i_image_name,
                i_hide_existing_images,
                i_step_number,
                i_increment_number
            )
        )

    def set_step_increment_number(
            self,
            i_step_number: cat_variant,
            i_increment_number: cat_variant,
            i_image: AnalysisImage) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetStepIncrementNumber(CATVariant iStepNumber,
                | CATVariant iIncrementNumber,
                | AnalysisImage iImage)
                | 
                |     Sets step and increment number for an image.
                |     This is done related to an existing image
                | 
                |     Parameters:
                | 
                |         iStepNumber
                |             The step number to select 
                |         iIncrementNumber
                |             The increment number to select

        :param cat_variant i_step_number:
        :param cat_variant i_increment_number:
        :param AnalysisImage i_image:
        :rtype: None
        """
        return self.abq_solution_case.SetStepIncrementNumber(
            i_step_number,
            i_increment_number,
            i_image.com_object
        )
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_step_increment_number'
        # # vba_code = """
        # # Public Function set_step_increment_number(abq_solution_case)
        # #     Dim iStepNumber (2)
        # #     abq_solution_case.SetStepIncrementNumber iStepNumber
        # #     set_step_increment_number = iStepNumber
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'ABQSolutionCase(name="{self.name}")'
