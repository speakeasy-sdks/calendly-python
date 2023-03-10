from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from sdk import utils

class LegacyCalendarEventKindEnum(str, Enum):
    EXCHANGE = "exchange"
    GOOGLE = "google"
    ICLOUD = "icloud"
    OUTLOOK = "outlook"
    OUTLOOK_DESKTOP = "outlook_desktop"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class LegacyCalendarEvent:
    r"""LegacyCalendarEvent
    Information about the calendar event from the calendar provider.
    """
    
    external_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('external_id') }})
    kind: LegacyCalendarEventKindEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('kind') }})
    