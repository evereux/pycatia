from pycatia.part_interfaces.add import Add
from pycatia.part_interfaces.assemble import Assemble
from pycatia.part_interfaces.auto_draft import AutoDraft
from pycatia.part_interfaces.auto_fillet import AutoFillet
from pycatia.part_interfaces.chamfer import Chamfer
from pycatia.part_interfaces.circ_pattern import CircPattern
from pycatia.part_interfaces.close_surface import CloseSurface
from pycatia.part_interfaces.const_rad_edge_fillet import ConstRadEdgeFillet
from pycatia.part_interfaces.defeaturing import Defeaturing
from pycatia.part_interfaces.draft import Draft
from pycatia.part_interfaces.face_fillet import FaceFillet
from pycatia.part_interfaces.groove import Groove
from pycatia.part_interfaces.hole import Hole
from pycatia.part_interfaces.intersect import Intersect
from pycatia.part_interfaces.loft import Loft
from pycatia.part_interfaces.mirror import Mirror
from pycatia.part_interfaces.pad import Pad
from pycatia.part_interfaces.pocket import Pocket
from pycatia.part_interfaces.rect_pattern import RectPattern
from pycatia.part_interfaces.remove import Remove
from pycatia.part_interfaces.remove_face import RemoveFace
from pycatia.part_interfaces.replace_face import ReplaceFace
from pycatia.part_interfaces.rib import Rib
from pycatia.part_interfaces.scaling import Scaling
from pycatia.part_interfaces.sew_surface import SewSurface
from pycatia.part_interfaces.shaft import Shaft
from pycatia.part_interfaces.shell import Shell
from pycatia.part_interfaces.slot import Slot
from pycatia.part_interfaces.solid_combine import SolidCombine
from pycatia.part_interfaces.split import Split
from pycatia.part_interfaces.stiffener import Stiffener
from pycatia.part_interfaces.thick_surface import ThickSurface
from pycatia.part_interfaces.thickness import Thickness
from pycatia.part_interfaces.thread import Thread
from pycatia.part_interfaces.trim import Trim
from pycatia.part_interfaces.tritangent_fillet import TritangentFillet
from pycatia.part_interfaces.user_pattern import UserPattern
from pycatia.part_interfaces.var_rad_edge_fillet import VarRadEdgeFillet

shape_types = {
    'Add': Add,
    'Assemble': Assemble,
    'AutoDraft': AutoDraft,
    'AutoFillet': AutoFillet,
    'Chamfer': Chamfer,
    'CircPattern': CircPattern,
    'CloseSurface': CloseSurface,
    'ConstRadEdgeFillet': ConstRadEdgeFillet,
    'Defeaturing': Defeaturing,
    'Draft': Draft,
    'FaceFillet': FaceFillet,
    'Groove': Groove,
    'Hole': Hole,
    'Intersect': Intersect,
    'Loft': Loft,
    'Mirror': Mirror,
    'Pad': Pad,
    'Pocket': Pocket,
    'RectPattern': RectPattern,
    'Remove': Remove,
    'RemoveFace': RemoveFace,
    'ReplaceFace': ReplaceFace,
    'Rib': Rib,
    'Scaling': Scaling,
    'SewSurface': SewSurface,
    'Shaft': Shaft,
    'Shell': Shell,
    'Slot': Slot,
    'SolidCombine': SolidCombine,
    'Stiffener': Stiffener,
    'Split': Split,
    'ThickSurface': ThickSurface,
    'Thickness': Thickness,
    'Thread': Thread,
    'Trim': Trim,
    'TritangentFillet': TritangentFillet,
    'UserPattern': UserPattern,
    'VarRadEdgeFillet': VarRadEdgeFillet,
}
