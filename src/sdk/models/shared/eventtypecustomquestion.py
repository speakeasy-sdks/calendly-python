from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from sdk import utils

class EventTypeCustomQuestionTypeEnum(str, Enum):
    STRING = "string"
    TEXT = "text"
    PHONE_NUMBER = "phone_number"
    SINGLE_SELECT = "single_select"
    MULTI_SELECT = "multi_select"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class EventTypeCustomQuestion:
    answer_choices: list[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('answer_choices') }})
    enabled: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('enabled') }})
    include_other: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('include_other') }})
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    position: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('position') }})
    required: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('required') }})
    type: EventTypeCustomQuestionTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})
    