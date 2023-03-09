from __future__ import annotations
import dataclasses
import dateutil.parser
from ..shared import question as shared_question
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from enum import Enum
from marshmallow import fields
from sdk import utils

class RoutingFormStatusEnum(str, Enum):
    DRAFT = "draft"
    PUBLISHED = "published"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class RoutingForm:
    r"""RoutingForm
    Information about a routing form.
    """
    
    created_at: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('created_at'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    organization: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('organization') }})
    questions: list[shared_question.Question] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('questions') }})
    status: RoutingFormStatusEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    updated_at: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('updated_at'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    uri: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('uri') }})
    