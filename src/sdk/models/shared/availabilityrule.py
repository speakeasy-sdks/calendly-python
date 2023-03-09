from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from sdk import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class AvailabilityRuleIntervals:
    from_: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('from'), 'exclude': lambda f: f is None }})
    to: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('to'), 'exclude': lambda f: f is None }})
    
class AvailabilityRuleTypeEnum(str, Enum):
    WDAY = "wday"
    DATE = "date"

class AvailabilityRuleWdayEnum(str, Enum):
    SUNDAY = "sunday"
    MONDAY = "monday"
    TUESDAY = "tuesday"
    WEDNESDAY = "wednesday"
    THURSDAY = "thursday"
    FRIDAY = "friday"
    SATURDAY = "saturday"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class AvailabilityRule:
    r"""AvailabilityRule
    The rules for an availability schedule.
    """
    
    intervals: list[AvailabilityRuleIntervals] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('intervals') }})
    type: AvailabilityRuleTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})
    date_: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('date'), 'exclude': lambda f: f is None }})
    wday: Optional[AvailabilityRuleWdayEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('wday'), 'exclude': lambda f: f is None }})
    