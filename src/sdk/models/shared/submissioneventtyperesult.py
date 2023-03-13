from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from sdk import utils

class SubmissionEventTypeResultTypeEnum(str, Enum):
    EVENT_TYPE = "event_type"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SubmissionEventTypeResult:
    r"""SubmissionEventTypeResult
    Information about the event type Routing Form Submission result.
    """
    
    type: SubmissionEventTypeResultTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})
    value: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('value') }})
    