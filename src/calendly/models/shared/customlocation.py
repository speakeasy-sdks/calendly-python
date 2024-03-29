"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from calendly import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum

class CustomLocationTypeEnum(str, Enum):
    r"""The event location doesn't fall into a standard category defined by the event host (publisher)"""
    CUSTOM = 'custom'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CustomLocation:
    r"""Use this to describe an existing Calendly-supported event location."""
    
    location: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('location') }})
    r"""The location description provided by the event host (publisher)"""  
    type: CustomLocationTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})
    r"""The event location doesn't fall into a standard category defined by the event host (publisher)"""  
    