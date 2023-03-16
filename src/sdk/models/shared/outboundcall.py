from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from sdk import utils

class OutboundCallTypeEnum(str, Enum):
    OUTBOUND_CALL = "outbound_call"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class OutboundCall:
    r"""OutboundCall
    Meeting publisher will call the Invitee
    """
    
    location: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('location') }})
    type: OutboundCallTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})
    