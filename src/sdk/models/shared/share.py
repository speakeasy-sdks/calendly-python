"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from datetime import date
from enum import Enum
from marshmallow import fields
from sdk import utils
from typing import Optional

class ShareSchedulingLinksOwnerTypeEnum(str, Enum):
    r"""Resource type (currently, this is always EventType)"""
    EVENT_TYPE = 'EventType'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ShareSchedulingLinks:
    
    booking_url: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('booking_url') }})
    r"""Scheduling link url"""  
    owner: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('owner'), 'exclude': lambda f: f is None }})
    r"""A link to the resource that owns this Scheduling Link (currently, this is always an Event Type)"""  
    owner_type: Optional[ShareSchedulingLinksOwnerTypeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('owner_type'), 'exclude': lambda f: f is None }})
    r"""Resource type (currently, this is always EventType)"""  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ShareShareOverrideAvailabilityRuleRulesIntervals:
    
    from_: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('from'), 'exclude': lambda f: f is None }})
    r"""Format: `\\"hh:mm\\"`"""  
    to: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('to'), 'exclude': lambda f: f is None }})
    r"""Format: `\\"hh:mm\\"`"""  
    
class ShareShareOverrideAvailabilityRuleRulesTypeEnum(str, Enum):
    WDAY = 'wday'
    DATE = 'date'

class ShareShareOverrideAvailabilityRuleRulesWdayEnum(str, Enum):
    SUNDAY = 'sunday'
    MONDAY = 'monday'
    TUESDAY = 'tuesday'
    WEDNESDAY = 'wednesday'
    THURSDAY = 'thursday'
    FRIDAY = 'friday'
    SATURDAY = 'saturday'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ShareShareOverrideAvailabilityRuleRules:
    
    type: ShareShareOverrideAvailabilityRuleRulesTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})  
    date_: Optional[date] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('date'), 'encoder': utils.dateisoformat(True), 'decoder': utils.datefromisoformat, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    r"""Format: `YYYY-MM-DD`"""  
    intervals: Optional[list[ShareShareOverrideAvailabilityRuleRulesIntervals]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('intervals'), 'exclude': lambda f: f is None }})  
    wday: Optional[ShareShareOverrideAvailabilityRuleRulesWdayEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('wday'), 'exclude': lambda f: f is None }})  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ShareShareOverrideAvailabilityRule:
    
    rules: list[ShareShareOverrideAvailabilityRuleRules] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('rules') }})  
    timezone: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('timezone') }})  
    
class ShareShareOverrideLocationConfigurationsKindEnum(str, Enum):
    PHYSICAL = 'physical'
    ASK_INVITEE = 'ask_invitee'
    CUSTOM = 'custom'
    OUTBOUND_CALL = 'outbound_call'
    INBOUND_CALL = 'inbound_call'
    GOOGLE_CONFERENCE = 'google_conference'
    GOTOMEETING_CONFERENCE = 'gotomeeting_conference'
    MICROSOFT_TEAMS_CONFERENCE = 'microsoft_teams_conference'
    ZOOM_CONFERENCE = 'zoom_conference'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ShareShareOverrideLocationConfigurations:
    
    additional_info: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('additional_info'), 'exclude': lambda f: f is None }})  
    kind: Optional[ShareShareOverrideLocationConfigurationsKindEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('kind'), 'exclude': lambda f: f is None }})  
    location: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('location'), 'exclude': lambda f: f is None }})  
    phone_number: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('phone_number'), 'exclude': lambda f: f is None }})  
    position: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('position'), 'exclude': lambda f: f is None }})  
    
class ShareShareOverridePeriodTypeEnum(str, Enum):
    AVAILABLE_MOVING = 'available_moving'
    MOVING = 'moving'
    FIXED = 'fixed'
    UNLIMITED = 'unlimited'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ShareShareOverride:
    
    availability_rule: Optional[ShareShareOverrideAvailabilityRule] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('availability_rule'), 'exclude': lambda f: f is None }})  
    duration: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('duration'), 'exclude': lambda f: f is None }})  
    end_date: Optional[date] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('end_date'), 'encoder': utils.dateisoformat(True), 'decoder': utils.datefromisoformat, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    r"""Format: `YYYY-MM-DD`"""  
    hide_location: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('hide_location'), 'exclude': lambda f: f is None }})  
    location_configurations: Optional[list[ShareShareOverrideLocationConfigurations]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('location_configurations'), 'exclude': lambda f: f is None }})  
    max_booking_time: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('max_booking_time'), 'exclude': lambda f: f is None }})  
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name'), 'exclude': lambda f: f is None }})  
    period_type: Optional[ShareShareOverridePeriodTypeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('period_type'), 'exclude': lambda f: f is None }})  
    start_date: Optional[date] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_date'), 'encoder': utils.dateisoformat(True), 'decoder': utils.datefromisoformat, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    r"""Format: `YYYY-MM-DD`"""  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Share:
    
    scheduling_links: list[ShareSchedulingLinks] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('scheduling_links') }})  
    share_override: ShareShareOverride = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('share_override') }})  
    