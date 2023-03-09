from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from sdk import utils

class SubmissionCustomMessageResultTypeEnum(str, Enum):
    CUSTOM_MESSAGE = "custom_message"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SubmissionCustomMessageResultValue:
    r"""SubmissionCustomMessageResultValue
    Contains an object with custom message headline and body.
    """
    
    body: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('body') }})
    headline: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('headline') }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SubmissionCustomMessageResult:
    r"""SubmissionCustomMessageResult
    Information about the custom message Routing Form Submission result.
    """
    
    type: SubmissionCustomMessageResultTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})
    value: SubmissionCustomMessageResultValue = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('value') }})
    