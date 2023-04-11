"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from calendly import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
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
    r"""The conference metadata supplied by Microsoft Teams"""
    
    audio_conferencing: Optional[MicrosoftTeamsConferenceDataAudioConferencing] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('audioConferencing'), 'exclude': lambda f: f is None }})  
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is None }})
    r"""The conference ID provided by Microsoft Teams"""  
    
class MicrosoftTeamsConferenceStatusEnum(str, Enum):
    r"""Indicates the current status of the Microsoft Teams conference"""
    INITIATED = 'initiated'
    PROCESSING = 'processing'
    PUSHED = 'pushed'
    FAILED = 'failed'

class MicrosoftTeamsConferenceTypeEnum(str, Enum):
    r"""The event location is a Zoom conference"""
    MICROSOFT_TEAMS_CONFERENCE = 'microsoft_teams_conference'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class MicrosoftTeamsConference:
    r"""Meeting will take place in a Microsoft Teams conference"""
    
    data: MicrosoftTeamsConferenceData = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('data') }})
    r"""The conference metadata supplied by Microsoft Teams"""  
    join_url: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('join_url') }})
    r"""Microsoft Teams meeting url"""  
    status: MicrosoftTeamsConferenceStatusEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    r"""Indicates the current status of the Microsoft Teams conference"""  
    type: MicrosoftTeamsConferenceTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})
    r"""The event location is a Zoom conference"""  
    