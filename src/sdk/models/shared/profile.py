"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from sdk import utils

class ProfileTypeEnum(str, Enum):
    r"""Indicates if the profile belongs to a "user" (individual) or "team""""
    USER = "User"
    TEAM = "Team"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Profile:
    r"""The publicly visible profile of a User or a Team that's associated with the Event Type (note: some Event Types don't have profiles)"""
    
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    r"""Human-readable name for the profile of the user that's associated with the event type"""  
    owner: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('owner') }})
    r"""The unique reference to the user associated with the profile"""  
    type: ProfileTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})
    r"""Indicates if the profile belongs to a "user" (individual) or "team""""  
    