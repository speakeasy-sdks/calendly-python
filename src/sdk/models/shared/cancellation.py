from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from sdk import utils

class CancellationCancelerTypeEnum(str, Enum):
    HOST = "host"
    INVITEE = "invitee"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Cancellation:
    r"""Cancellation
    Provides data pertaining to the cancellation of the Event
    """
    
    canceled_by: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('canceled_by') }})
    canceler_type: CancellationCancelerTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('canceler_type') }})
    reason: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('reason') }})
    