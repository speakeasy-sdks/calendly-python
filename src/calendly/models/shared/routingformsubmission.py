"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from ..shared import submissionquestionandanswer as shared_submissionquestionandanswer
from ..shared import submissiontracking as shared_submissiontracking
from calendly import utils
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from enum import Enum
from marshmallow import fields
from typing import Any, Optional

class RoutingFormSubmissionSubmitterTypeEnum(str, Enum):
    r"""Type of the respondent resource that submitted the form and scheduled a meeting."""
    INVITEE = 'Invitee'
    NULL = 'null'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class RoutingFormSubmission:
    r"""Information about a Routing Form Submission."""
    
    created_at: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('created_at'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    r"""The moment the routing form was submitted."""  
    questions_and_answers: list[shared_submissionquestionandanswer.SubmissionQuestionAndAnswer] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('questions_and_answers') }})
    r"""All Routing Form Submission questions with answers."""  
    routing_form: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('routing_form') }})
    r"""The URI of the routing form that's associated with the submission."""  
    submitter: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('submitter') }})
    r"""The reference to the Invitee resource when routing form submission results in a scheduled meeting."""  
    submitter_type: RoutingFormSubmissionSubmitterTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('submitter_type') }})
    r"""Type of the respondent resource that submitted the form and scheduled a meeting."""  
    tracking: shared_submissiontracking.SubmissionTracking = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tracking') }})
    r"""The UTM and Salesforce tracking parameters associated with a Routing Form Submission."""  
    updated_at: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('updated_at'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    r"""The moment when the routing form submission was last updated."""  
    uri: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('uri') }})
    r"""Canonical reference (unique identifier) for the routing form submission."""  
    result: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('result'), 'exclude': lambda f: f is None }})
    r"""The polymorphic base type for a Routing Form Submission result."""  
    