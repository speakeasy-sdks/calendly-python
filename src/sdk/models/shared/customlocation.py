from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from sdk import utils

class CustomLocationTypeEnum(str, Enum):
    CUSTOM = "custom"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CustomLocation:
    r"""CustomLocation
    Use this to describe an existing Calendly-supported event location.
    """
    
    location: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('location') }})
    type: CustomLocationTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})
    