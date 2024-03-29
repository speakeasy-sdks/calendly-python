"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from ..shared import cancellation as shared_cancellation
from ..shared import guest as shared_guest
from ..shared import legacycalendarevent as shared_legacycalendarevent
from calendly import utils
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from enum import Enum
from marshmallow import fields
from typing import Any, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class EventEventMemberships:
    
    user: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('user') }})
    r"""Canonical reference (unique identifier) for the user"""  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class EventInviteesCounter:
    
    active: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('active') }})
    r"""Total invitees for an event that have not canceled"""  
    limit: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('limit') }})
    r"""Maximum number of active invitees that can book the event"""  
    total: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('total') }})
    r"""Total invitees for an event, including invitees that have canceled"""  
    
class EventStatusEnum(str, Enum):
    r"""Indicates if the event is \\"active\\" or \\"canceled\\" """
    ACTIVE = 'active'
    CANCELED = 'canceled'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Event:
    r"""Information about a scheduled meeting"""
    
    calendar_event: shared_legacycalendarevent.LegacyCalendarEvent = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('calendar_event') }})
    r"""Information about the calendar event from the calendar provider."""  
    created_at: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('created_at'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    r"""The moment when the event was created (e.g. \\"2020-01-02T03:04:05.678123Z\\")"""  
    end_time: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('end_time'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    r"""The moment the event was scheduled to end in UTC time (e.g. \\"2020-01-02T03:04:05.678123Z\\")"""  
    event_guests: list[shared_guest.Guest] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('event_guests') }})
    r"""Additional people added to an event by an invitee"""  
    event_memberships: list[EventEventMemberships] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('event_memberships') }})
    r"""Event membership list"""  
    event_type: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('event_type') }})
    r"""The event type associated with this event"""  
    invitees_counter: EventInviteesCounter = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('invitees_counter') }})  
    location: Any = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('location') }})
    r"""The polymorphic base type for an event location that Calendly supports"""  
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    r"""The event name"""  
    start_time: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_time'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    r"""The moment the event was scheduled to start in UTC time (e.g. \\"2020-01-02T03:04:05.678123Z\\")."""  
    status: EventStatusEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    r"""Indicates if the event is \\"active\\" or \\"canceled\\" """  
    updated_at: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('updated_at'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    r"""The moment when the event was last updated (e.g. \\"2020-01-02T03:04:05.678123Z\\")"""  
    uri: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('uri') }})
    r"""Canonical reference (unique identifier) for the resource"""  
    cancellation: Optional[shared_cancellation.Cancellation] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('cancellation'), 'exclude': lambda f: f is None }})
    r"""Provides data pertaining to the cancellation of the Event"""  
    