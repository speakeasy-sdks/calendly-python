from __future__ import annotations
import dataclasses
from ..shared import availabilityrule as shared_availabilityrule
from dataclasses_json import Undefined, dataclass_json
from sdk import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class AvailabilitySchedule:
    r"""AvailabilitySchedule
    The availability schedule set by the user.
    """
    
    default: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('default') }})
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    rules: list[shared_availabilityrule.AvailabilityRule] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('rules') }})
    timezone: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('timezone') }})
    uri: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('uri') }})
    user: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('user') }})
    