from __future__ import annotations
import dataclasses
import dateutil.parser
from ..shared import cancellation as shared_cancellation
from ..shared import guest as shared_guest
from ..shared import legacycalendarevent as shared_legacycalendarevent
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from enum import Enum
from marshmallow import fields
from sdk import utils
from typing import Any, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class EventEventMemberships:
    user: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('user') }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class EventInviteesCounter:
    active: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('active') }})
    limit: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('limit') }})
    total: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('total') }})
    
class EventStatusEnum(str, Enum):
    ACTIVE = "active"
    CANCELED = "canceled"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Event:
    r"""Event
    Information about a scheduled meeting
    """
    
    calendar_event: shared_legacycalendarevent.LegacyCalendarEvent = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('calendar_event') }})
    created_at: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('created_at'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    end_time: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('end_time'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    event_guests: list[shared_guest.Guest] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('event_guests') }})
    event_memberships: list[EventEventMemberships] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('event_memberships') }})
    event_type: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('event_type') }})
    invitees_counter: EventInviteesCounter = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('invitees_counter') }})
    location: Any = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('location') }})
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    start_time: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_time'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    status: EventStatusEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    updated_at: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('updated_at'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    uri: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('uri') }})
    cancellation: Optional[shared_cancellation.Cancellation] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('cancellation'), 'exclude': lambda f: f is None }})
    