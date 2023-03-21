from __future__ import annotations
import dataclasses
import dateutil.parser
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from marshmallow import fields
from sdk import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class EventTypeAvailableTime:
    r"""EventTypeAvailableTime
    An available meeting time slot for the given event type
    """
    
    invitees_remaining: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('invitees_remaining') }})
    scheduling_url: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('scheduling_url') }})
    start_time: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_time'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    status: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    