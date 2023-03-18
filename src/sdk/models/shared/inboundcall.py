from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from sdk import utils

class InboundCallTypeEnum(str, Enum):
    INBOUND_CALL = "inbound_call"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class InboundCall:
    r"""InboundCall
    Invitee will call meeting publisher at the specified phone number
    """
    
    location: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('location') }})
    type: InboundCallTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})
    