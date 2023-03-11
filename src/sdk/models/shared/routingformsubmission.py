from __future__ import annotations
import dataclasses
import dateutil.parser
from ..shared import submissionquestionandanswer as shared_submissionquestionandanswer
from ..shared import submissiontracking as shared_submissiontracking
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from enum import Enum
from marshmallow import fields
from sdk import utils
from typing import Any, Optional

class RoutingFormSubmissionSubmitterTypeEnum(str, Enum):
    INVITEE = "Invitee"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class RoutingFormSubmission:
    r"""RoutingFormSubmission
    Information about a Routing Form Submission.
    """
    
    created_at: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('created_at'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    questions_and_answers: list[shared_submissionquestionandanswer.SubmissionQuestionAndAnswer] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('questions_and_answers') }})
    routing_form: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('routing_form') }})
    submitter: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('submitter') }})
    submitter_type: RoutingFormSubmissionSubmitterTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('submitter_type') }})
    tracking: shared_submissiontracking.SubmissionTracking = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tracking') }})
    updated_at: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('updated_at'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    uri: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('uri') }})
    result: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('result'), 'exclude': lambda f: f is None }})
    