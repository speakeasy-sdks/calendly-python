"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

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
    r"""Object for a created activity log record"""
    
    action: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('action') }})  
    details: dict[str, Any] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('details') }})  
    fully_qualified_name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('fully_qualified_name') }})  
    namespace: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('namespace') }})  
    occurred_at: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('occurred_at'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    r"""The date and time of the entry (format: \"2020-01-02T03:04:05.678Z\")."""  
    organization: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('organization') }})  
    uri: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('uri') }})  
    actor: Optional[shared_actor.Actor] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('actor'), 'exclude': lambda f: f is None }})
    r"""The Calendly actor that took the action creating the activity log entry
    
    Specific actors:
    
    <details>
    <summary>Calendly System</summary>
    
    Used when an action is performed by the Calendly system and not triggered directly by a user interaction.
    
    Example:
    ```json
    {
        \"display_name\": \"Calendly System\",
        \"type\": \"System\"
    }
    ```
    
    </details>
    
    <br />
    
    <details>
    <summary>Calendly Support</summary>
    Used when an action is performed by Calendly support.
    
    Example:
    ```json
    {
      \"display_name\": \"Calendly Support\",
      \"organization\": {
        \"uri\": \"https://api.calendly.com/organizations/AAAAAAAAAAAAAAAA\"
      },
      \"type\": \"User\",
      \"uri\": \"https://api.calendly.com/users/AAAAAAAAAAAAAAAA\"
    }
    ```
    </details>
    
    """  
    