from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from sdk import utils

class InPersonMeetingTypeEnum(str, Enum):
    PHYSICAL = "physical"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class InPersonMeeting:
    r"""InPersonMeeting
    Information about the physical (in-person) event location
    """
    
    location: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('location') }})
    type: InPersonMeetingTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})
    