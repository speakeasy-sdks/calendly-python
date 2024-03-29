"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from calendly import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ZoomConferenceDataExtra:
    
    intl_numbers_url: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('intl_numbers_url'), 'exclude': lambda f: f is None }})
    r"""Zoom International Dial-in Numbers URL"""  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ZoomConferenceDataSettingsGlobalDialInNumbers:
    
    city: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('city'), 'exclude': lambda f: f is None }})  
    country: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('country'), 'exclude': lambda f: f is None }})
    r"""Country code"""  
    country_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('country_name'), 'exclude': lambda f: f is None }})  
    number: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('number'), 'exclude': lambda f: f is None }})
    r"""Phone number"""  
    type: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type'), 'exclude': lambda f: f is None }})  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ZoomConferenceDataSettings:
    
    global_dial_in_numbers: Optional[list[ZoomConferenceDataSettingsGlobalDialInNumbers]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('global_dial_in_numbers'), 'exclude': lambda f: f is None }})  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ZoomConferenceData:
    r"""The conference metadata supplied by Zoom"""
    
    extra: Optional[ZoomConferenceDataExtra] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('extra'), 'exclude': lambda f: f is None }})  
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is None }})
    r"""The conference ID provided by Zoom"""  
    password: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('password'), 'exclude': lambda f: f is None }})
    r"""Zoom meeting password"""  
    settings: Optional[ZoomConferenceDataSettings] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('settings'), 'exclude': lambda f: f is None }})  
    
class ZoomConferenceStatusEnum(str, Enum):
    r"""Indicates the current status of the Zoom conference"""
    INITIATED = 'initiated'
    PROCESSING = 'processing'
    PUSHED = 'pushed'
    FAILED = 'failed'

class ZoomConferenceTypeEnum(str, Enum):
    r"""The event location is a Zoom conference"""
    ZOOM_CONFERENCE = 'zoom_conference'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ZoomConference:
    r"""Meeting will take place in a Zoom conference"""
    
    data: ZoomConferenceData = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('data') }})
    r"""The conference metadata supplied by Zoom"""  
    join_url: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('join_url') }})
    r"""Zoom meeting url"""  
    status: ZoomConferenceStatusEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    r"""Indicates the current status of the Zoom conference"""  
    type: ZoomConferenceTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})
    r"""The event location is a Zoom conference"""  
    