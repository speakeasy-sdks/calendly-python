"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from calendly import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum

class SubmissionCustomMessageResultTypeEnum(str, Enum):
    r"""Indicates if the routing form submission resulted in a custom \\"thank you\\" message."""
    CUSTOM_MESSAGE = 'custom_message'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SubmissionCustomMessageResultValue:
    r"""Contains an object with custom message headline and body."""
    
    body: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('body') }})
    r"""Body text displayed when answers don't match any routes."""  
    headline: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('headline') }})
    r"""Headline displayed when answers don't match any routes."""  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SubmissionCustomMessageResult:
    r"""Information about the custom message Routing Form Submission result."""
    
    type: SubmissionCustomMessageResultTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})
    r"""Indicates if the routing form submission resulted in a custom \\"thank you\\" message."""  
    value: SubmissionCustomMessageResultValue = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('value') }})
    r"""Contains an object with custom message headline and body."""  
    