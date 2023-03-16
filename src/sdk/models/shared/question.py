from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from sdk import utils

class QuestionTypeEnum(str, Enum):
    NAME = "name"
    TEXT = "text"
    EMAIL = "email"
    PHONE = "phone"
    TEXTAREA = "textarea"
    SELECT = "select"
    RADIOS = "radios"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Question:
    r"""Question
    Routing form questions.
    """
    
    answer_choices: list[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('answer_choices') }})
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    required: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('required') }})
    type: QuestionTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})
    uuid: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('uuid') }})
    