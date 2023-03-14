from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from sdk import utils

class ProfileTypeEnum(str, Enum):
    USER = "User"
    TEAM = "Team"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Profile:
    r"""Profile
    The publicly visible profile of a User or a Team that's associated with the Event Type (note: some Event Types don't have profiles)
    """
    
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    owner: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('owner') }})
    type: ProfileTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})
    