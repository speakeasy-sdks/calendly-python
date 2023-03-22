"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from ..shared import eventtypecustomquestion as shared_eventtypecustomquestion
from ..shared import profile as shared_profile
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from enum import Enum
from marshmallow import fields
from sdk import utils

class EventTypeBookingMethodEnum(str, Enum):
    r"""Indicates if the event type is for a poll or an instant booking"""
    INSTANT = "instant"
    POLL = "poll"

class EventTypeKindEnum(str, Enum):
    r"""Indicates if the event type is "solo" (belongs to an individual user) or "group""""
    SOLO = "solo"
    GROUP = "group"

class EventTypeKindDescriptionEnum(str, Enum):
    r"""A formatted description of the kind of event type."""
    COLLECTIVE = "Collective"
    GROUP = "Group"
    ONE_ON_ONE = "One-on-One"
    ROUND_ROBIN = "Round Robin"

class EventTypePoolingTypeEnum(str, Enum):
    r"""Indicates if the event type is "round robin" (alternates between hosts) or "collective" (invitees pick a time when all participants are available) or "null" (the event type doesn’t consider the availability of a group participants)"""
    ROUND_ROBIN = "round_robin"
    COLLECTIVE = "collective"

class EventTypeTypeEnum(str, Enum):
    r"""Indicates if the event type is "AdhocEventType" (ad hoc event) or "StandardEventType" (standard event type)"""
    STANDARD_EVENT_TYPE = "StandardEventType"
    ADHOC_EVENT_TYPE = "AdhocEventType"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class EventType:
    r"""A configuration for an Event"""
    
    active: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('active') }})
    r"""Indicates if the event is active or not."""  
    admin_managed: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('admin_managed') }})
    r"""Indicates if this event type is managed by an organization admin"""  
    booking_method: EventTypeBookingMethodEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('booking_method') }})
    r"""Indicates if the event type is for a poll or an instant booking"""  
    color: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('color') }})
    r"""The hexadecimal color value of the event type's scheduling page"""  
    created_at: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('created_at'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    r"""The moment the event type was created (e.g. "2020-01-02T03:04:05.678123Z")"""  
    custom_questions: list[shared_eventtypecustomquestion.EventTypeCustomQuestion] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('custom_questions') }})  
    deleted_at: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('deleted_at'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    r"""The moment the event type was deleted (e.g. "2020-01-02T03:04:05.678123Z"). Since event types can be deleted but their scheduled events remain it's useful to fetch a deleted event type when you still require event type data for a scheduled event."""  
    description_html: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('description_html') }})
    r"""The event type's description (formatted with HTML)"""  
    description_plain: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('description_plain') }})
    r"""The event type's description (in non formatted text)"""  
    duration: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('duration') }})
    r"""The length of sessions booked with this event type"""  
    internal_note: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('internal_note') }})
    r"""Contents of a note that may be associated with the event type"""  
    kind: EventTypeKindEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('kind') }})
    r"""Indicates if the event type is "solo" (belongs to an individual user) or "group""""  
    kind_description: EventTypeKindDescriptionEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('kind_description') }})
    r"""A formatted description of the kind of event type."""  
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    r"""The event type name (in human-readable format)"""  
    pooling_type: EventTypePoolingTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pooling_type') }})
    r"""Indicates if the event type is "round robin" (alternates between hosts) or "collective" (invitees pick a time when all participants are available) or "null" (the event type doesn’t consider the availability of a group participants)"""  
    profile: shared_profile.Profile = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('profile') }})
    r"""The publicly visible profile of a User or a Team that's associated with the Event Type (note: some Event Types don't have profiles)"""  
    scheduling_url: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('scheduling_url') }})
    r"""The URL of the user’s scheduling site where invitees book this event type"""  
    secret: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('secret') }})
    r"""Indicates if the event type is hidden on the owner's main scheduling page"""  
    slug: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('slug') }})
    r"""The portion of the event type's URL that identifies a specific web page (in a human-readable format)"""  
    type: EventTypeTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})
    r"""Indicates if the event type is "AdhocEventType" (ad hoc event) or "StandardEventType" (standard event type)"""  
    updated_at: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('updated_at'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    r"""The moment the event type was last updated (e.g. "2020-01-02T03:04:05.678123Z")"""  
    uri: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('uri') }})
    r"""Canonical reference (unique identifier) for the event type"""  
    