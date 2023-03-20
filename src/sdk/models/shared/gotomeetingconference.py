from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from sdk import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GotoMeetingConferenceData:
    r"""GotoMeetingConferenceData
    The conference metadata supplied by GoToMeeting
    """
    
    conference_call_info: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('conferenceCallInfo'), 'exclude': lambda f: f is None }})
    unique_meeting_id: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('uniqueMeetingId'), 'exclude': lambda f: f is None }})
    
class GotoMeetingConferenceStatusEnum(str, Enum):
    INITIATED = "initiated"
    PROCESSING = "processing"
    PUSHED = "pushed"
    FAILED = "failed"

class GotoMeetingConferenceTypeEnum(str, Enum):
    GOTOMEETING = "gotomeeting"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GotoMeetingConference:
    r"""GotoMeetingConference
    Details about an Event that will take place using a GotoMeeting conference
    """
    
    data: GotoMeetingConferenceData = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('data') }})
    join_url: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('join_url') }})
    status: GotoMeetingConferenceStatusEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    type: GotoMeetingConferenceTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})
    