from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from sdk import utils

class InviteeSpecifiedLocationTypeEnum(str, Enum):
    ASK_INVITEE = "ask_invitee"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class InviteeSpecifiedLocation:
    r"""InviteeSpecifiedLocation
    Information about an event location that’s specified by the invitee.
    """
    
    location: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('location') }})
    type: InviteeSpecifiedLocationTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})
    