from pycatia.knowledge_interfaces.parameter_set import ParameterSet
from pycatia.mec_mod_interfaces.body import Body
from pycatia.mec_mod_interfaces.hybrid_body import HybridBody

body_types = {
    'Body': Body,
    'HybridBody': HybridBody,
    'ParmsSet': ParameterSet,
}
