from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from sdk import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class WebExConferenceDataTelephonyCallInNumbers:
    call_in_number: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('callInNumber') }})
    label: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('label') }})
    toll_type: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tollType') }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class WebExConferenceDataTelephony:
    call_in_numbers: list[WebExConferenceDataTelephonyCallInNumbers] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('callInNumbers') }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class WebExConferenceData:
    r"""WebExConferenceData
    The conference metadata supplied by GoToMeeting
    """
    
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    password: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('password') }})
    telephony: WebExConferenceDataTelephony = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('telephony') }})
    
class WebExConferenceStatusEnum(str, Enum):
    INITIATED = "initiated"
    PROCESSING = "processing"
    PUSHED = "pushed"
    FAILED = "failed"

class WebExConferenceTypeEnum(str, Enum):
    WEBEX_CONFERENCE = "webex_conference"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class WebExConference:
    r"""WebExConference
    Details about an Event that will take place using a WebEx conference
    """
    
    data: WebExConferenceData = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('data') }})
    join_url: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('join_url') }})
    status: WebExConferenceStatusEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    type: WebExConferenceTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})
    