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
    INSTANT = "instant"
    POLL = "poll"

class EventTypeKindEnum(str, Enum):
    SOLO = "solo"
    GROUP = "group"

class EventTypeKindDescriptionEnum(str, Enum):
    COLLECTIVE = "Collective"
    GROUP = "Group"
    ONE_ON_ONE = "One-on-One"
    ROUND_ROBIN = "Round Robin"

class EventTypePoolingTypeEnum(str, Enum):
    ROUND_ROBIN = "round_robin"
    COLLECTIVE = "collective"

class EventTypeTypeEnum(str, Enum):
    STANDARD_EVENT_TYPE = "StandardEventType"
    ADHOC_EVENT_TYPE = "AdhocEventType"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class EventType:
    r"""EventType
    A configuration for an Event
    """
    
    active: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('active') }})
    admin_managed: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('admin_managed') }})
    booking_method: EventTypeBookingMethodEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('booking_method') }})
    color: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('color') }})
    created_at: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('created_at'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    custom_questions: list[shared_eventtypecustomquestion.EventTypeCustomQuestion] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('custom_questions') }})
    deleted_at: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('deleted_at'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    description_html: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('description_html') }})
    description_plain: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('description_plain') }})
    duration: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('duration') }})
    internal_note: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('internal_note') }})
    kind: EventTypeKindEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('kind') }})
    kind_description: EventTypeKindDescriptionEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('kind_description') }})
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    pooling_type: EventTypePoolingTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pooling_type') }})
    profile: shared_profile.Profile = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('profile') }})
    scheduling_url: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('scheduling_url') }})
    secret: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('secret') }})
    slug: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('slug') }})
    type: EventTypeTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})
    updated_at: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('updated_at'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    uri: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('uri') }})
    