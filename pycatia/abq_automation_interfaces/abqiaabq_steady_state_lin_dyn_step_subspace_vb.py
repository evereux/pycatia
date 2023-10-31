#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.abq_automation_interfaces.abqiaabq_steady_state_lin_dyn_step_basic_vb import \
    ABQIAABQSteadyStateLinDynStepBasicVB


class ABQIAABQSteadyStateLinDynStepSubspaceVB(ABQIAABQSteadyStateLinDynStepBasicVB):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     ABQAutomationItf.ABQStep
                |                        ABQAutomationItf.ABQIAABQSteadyStateLinDynStepBasicVB
                |                            ABQIAABQSteadyStateLinDynStepSubspaceVB
                | 
                | Interface representing xxx.
                | 
                | Role: Components that implement ABQIAABQSteadyStateLinDynStepSubspace are
                | ...
                | 
                | Do not use the ABQIAABQSteadyStateLinDynStepSubspace interface for such and
                | such ClassReference, Class#MethodReference, #InternalMethod...
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.abqiaabq_steady_state_lin_dyn_step_subspace_vb = com_object

    @property
    def max_damping_change(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property MaxDampingChange() As double
                | 
                |     Returns or sets Maximum Damping Change.
                | 
                |     Returns:
                |         The Maximum Damping Change. Applicable only for Projection Type = As a function of property changes.

        :rtype: float
        """

        return self.abqiaabq_steady_state_lin_dyn_step_subspace_vb.MaxDampingChange

    @max_damping_change.setter
    def max_damping_change(self, value: float):
        """
        :param float value:
        """

        self.abqiaabq_steady_state_lin_dyn_step_subspace_vb.MaxDampingChange = value

    @property
    def max_stiffness_change(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property MaxStiffnessChange() As double
                | 
                |     Returns or sets Maximum Stiffness Change.
                | 
                |     Returns:
                |         The Maximum Stiffness Change. Applicable only for Projection Type = As a function of property changes.

        :rtype: float
        """

        return self.abqiaabq_steady_state_lin_dyn_step_subspace_vb.MaxStiffnessChange

    @max_stiffness_change.setter
    def max_stiffness_change(self, value: float):
        """
        :param float value:
        """

        self.abqiaabq_steady_state_lin_dyn_step_subspace_vb.MaxStiffnessChange = value

    @property
    def subspace_friction_damping(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property SubspaceFrictionDamping() As boolean
                | 
                |     Sets or returns if the Subspace Response.
                | 
                |     Returns:
                |         A boolean specifying whether the Subspace Response is used.

        :rtype: bool
        """

        return self.abqiaabq_steady_state_lin_dyn_step_subspace_vb.SubspaceFrictionDamping

    @subspace_friction_damping.setter
    def subspace_friction_damping(self, value: bool):
        """
        :param bool value:
        """

        self.abqiaabq_steady_state_lin_dyn_step_subspace_vb.SubspaceFrictionDamping = value

    @property
    def subspace_projection_type(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property SubspaceProjectionType() As short
                | 
                |     Returns or sets Subspace Projection Type.
                | 
                |     Returns:
                |         The Subspace Projection Type.
                |
                |         Legal values:
                |          1 - Evaluate at each frequency.
                |          2 - Constant.
                |          3 - Interpolate at eigen frequency.
                |          4 - As a function of property changes.
                |          5 - Interpolate at upper and lower frequency limits.
                |
                |         Example:
                |             This example sets the Subspace Projection Type as Evaluate at each
                |             frequency for abqSSDStep
                | 
                |              abqSSDStep.SubspaceProjectionType = 1

        :rtype: int
        """

        return self.abqiaabq_steady_state_lin_dyn_step_subspace_vb.SubspaceProjectionType

    @subspace_projection_type.setter
    def subspace_projection_type(self, value: int):
        """
        :param int value:
        """

        self.abqiaabq_steady_state_lin_dyn_step_subspace_vb.SubspaceProjectionType = value

    @property
    def subspace_response(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property SubspaceResponase() As short
                | 
                |     Returns or sets Subspace Responase.
                | 
                |     Returns:
                |         The Subspace Responase.
                | 
                |           
                |         Legal values:
                |          1 - Real.
                |          2 - Complex.
                |          
                | 
                |         Example:
                |             This example sets the Subspace Responase as Real for
                |             abqSSDStep
                | 
                |              abqSSDStep.SubspaceResponase = 1

        :rtype: int
        """

        return self.abqiaabq_steady_state_lin_dyn_step_subspace_vb.SubspaceResponase

    @subspace_response.setter
    def subspace_response(self, value: int):
        """
        :param int value:
        """

        self.abqiaabq_steady_state_lin_dyn_step_subspace_vb.SubspaceResponase = value

    def __repr__(self):
        return f'ABQIAABQSteadyStateLinDynStepSubspaceVB(name="{self.name}")'
