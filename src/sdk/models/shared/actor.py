"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from sdk import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ActorGroup:
    r"""User group information about the actor"""
    
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name'), 'exclude': lambda f: f is None }})
    r"""Name of the user group"""  
    role: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('role'), 'exclude': lambda f: f is None }})
    r"""The actor's role in the user group"""  
    uri: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('uri'), 'exclude': lambda f: f is None }})
    r"""Canonical reference (unique identifier) for the user group"""  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ActorOrganization:
    
    role: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('role'), 'exclude': lambda f: f is None }})
    r"""The actors' role in the organization"""  
    uri: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('uri'), 'exclude': lambda f: f is None }})
    r"""Canonical reference (unique identifier) for the organization"""  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Actor:
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
    
    type: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})
    r"""The type of actor"""  
    alternative_identifier: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('alternative_identifier'), 'exclude': lambda f: f is None }})
    r"""Username of the actor"""  
    display_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('display_name'), 'exclude': lambda f: f is None }})
    r"""The user's name (human-readable format)"""  
    group: Optional[ActorGroup] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('group'), 'exclude': lambda f: f is None }})
    r"""User group information about the actor"""  
    organization: Optional[ActorOrganization] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('organization'), 'exclude': lambda f: f is None }})  
    uri: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('uri'), 'exclude': lambda f: f is None }})
    r"""Canonical reference (unique identifier) for the user"""  
    