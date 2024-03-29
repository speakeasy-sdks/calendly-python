"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from calendly import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SubmissionQuestionAndAnswer:
    r"""All Routing Form Submission questions with answers."""
    
    question: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('question') }})
    r"""Question name (in human-readable format)."""  
    question_uuid: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('question_uuid') }})
    r"""Unique identifier for the routing form question."""  
    answer: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('answer'), 'exclude': lambda f: f is None }})
    r"""Answer provided by the respondent when the form was submitted."""  
    