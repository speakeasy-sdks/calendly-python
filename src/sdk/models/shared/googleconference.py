"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from sdk import utils

class GoogleConferenceStatusEnum(str, Enum):
    r"""Indicates the current status of the Google conference"""
    INITIATED = 'initiated'
    PROCESSING = 'processing'
    PUSHED = 'pushed'
    FAILED = 'failed'

class GoogleConferenceTypeEnum(str, Enum):
    r"""The event location is a Google Meet or Hangouts conference"""
    GOOGLE_CONFERENCE = 'google_conference'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GoogleConference:
    r"""Details about an Event that will take place using a Google Meet / Hangout conference"""
    
    join_url: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('join_url') }})
    r"""Google conference meeting url"""  
    status: GoogleConferenceStatusEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    r"""Indicates the current status of the Google conference"""  
    type: GoogleConferenceTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})
    r"""The event location is a Google Meet or Hangouts conference"""  
    