from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from sdk import utils

class GoogleConferenceStatusEnum(str, Enum):
    INITIATED = "initiated"
    PROCESSING = "processing"
    PUSHED = "pushed"
    FAILED = "failed"

class GoogleConferenceTypeEnum(str, Enum):
    GOOGLE_CONFERENCE = "google_conference"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GoogleConference:
    r"""GoogleConference
    Details about an Event that will take place using a Google Meet / Hangout conference
    """
    
    join_url: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('join_url') }})
    status: GoogleConferenceStatusEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    type: GoogleConferenceTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})
    