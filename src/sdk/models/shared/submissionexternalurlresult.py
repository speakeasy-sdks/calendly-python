from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from sdk import utils

class SubmissionExternalURLResultTypeEnum(str, Enum):
    EXTERNAL_URL = "external_url"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SubmissionExternalURLResult:
    r"""SubmissionExternalURLResult
    Information about the external URL Routing Form Submission result.
    """
    
    type: SubmissionExternalURLResultTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})
    value: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('value') }})
    