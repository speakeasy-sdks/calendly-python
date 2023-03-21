from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from sdk import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ActorGroup:
    r"""ActorGroup
    User group information about the actor
    """
    
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name'), 'exclude': lambda f: f is None }})
    role: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('role'), 'exclude': lambda f: f is None }})
    uri: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('uri'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ActorOrganization:
    role: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('role'), 'exclude': lambda f: f is None }})
    uri: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('uri'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Actor:
    r"""Actor
    The Calendly actor that took the action creating the activity log entry
    
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
    
    type: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})
    alternative_identifier: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('alternative_identifier'), 'exclude': lambda f: f is None }})
    display_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('display_name'), 'exclude': lambda f: f is None }})
    group: Optional[ActorGroup] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('group'), 'exclude': lambda f: f is None }})
    organization: Optional[ActorOrganization] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('organization'), 'exclude': lambda f: f is None }})
    uri: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('uri'), 'exclude': lambda f: f is None }})
    