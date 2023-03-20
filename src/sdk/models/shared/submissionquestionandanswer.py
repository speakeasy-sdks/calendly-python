from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from sdk import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SubmissionQuestionAndAnswer:
    r"""SubmissionQuestionAndAnswer
    All Routing Form Submission questions with answers.
    """
    
    question: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('question') }})
    question_uuid: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('question_uuid') }})
    answer: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('answer'), 'exclude': lambda f: f is None }})
    