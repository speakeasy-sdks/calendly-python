from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from sdk import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class MicrosoftTeamsConferenceDataAudioConferencing:
    conference_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('conferenceId'), 'exclude': lambda f: f is None }})
    dialin_url: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('dialinUrl'), 'exclude': lambda f: f is None }})
    toll_number: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tollNumber'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class MicrosoftTeamsConferenceData:
    r"""MicrosoftTeamsConferenceData
    The conference metadata supplied by Microsoft Teams
    """
    
    audio_conferencing: Optional[MicrosoftTeamsConferenceDataAudioConferencing] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('audioConferencing'), 'exclude': lambda f: f is None }})
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is None }})
    
class MicrosoftTeamsConferenceStatusEnum(str, Enum):
    INITIATED = "initiated"
    PROCESSING = "processing"
    PUSHED = "pushed"
    FAILED = "failed"

class MicrosoftTeamsConferenceTypeEnum(str, Enum):
    MICROSOFT_TEAMS_CONFERENCE = "microsoft_teams_conference"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class MicrosoftTeamsConference:
    r"""MicrosoftTeamsConference
    Meeting will take place in a Microsoft Teams conference
    """
    
    data: MicrosoftTeamsConferenceData = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('data') }})
    join_url: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('join_url') }})
    status: MicrosoftTeamsConferenceStatusEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    type: MicrosoftTeamsConferenceTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})
    