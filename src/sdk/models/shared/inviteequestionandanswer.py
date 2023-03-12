from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from sdk import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class InviteeQuestionAndAnswer:
    r"""InviteeQuestionAndAnswer
    A response to a question on a booking page form
    """
    
    answer: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('answer') }})
    position: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('position') }})
    question: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('question') }})
    