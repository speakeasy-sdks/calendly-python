from __future__ import annotations
import dataclasses
import dateutil.parser
from ..shared import actor as shared_actor
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from marshmallow import fields
from sdk import utils
from typing import Any, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Entry:
    r"""Entry
    Object for a created activity log record
    """
    
    action: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('action') }})
    details: dict[str, Any] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('details') }})
    fully_qualified_name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('fully_qualified_name') }})
    namespace: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('namespace') }})
    occurred_at: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('occurred_at'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    organization: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('organization') }})
    uri: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('uri') }})
    actor: Optional[shared_actor.Actor] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('actor'), 'exclude': lambda f: f is None }})
    