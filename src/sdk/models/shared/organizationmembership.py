"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from enum import Enum
from marshmallow import fields
from sdk import utils

class OrganizationMembershipRoleEnum(str, Enum):
    r"""The user's role in the organization"""
    USER = "user"
    ADMIN = "admin"
    OWNER = "owner"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class OrganizationMembershipUser:
    r"""Information about the user."""
    
    avatar_url: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('avatar_url') }})
    r"""The URL of the user's avatar (image)"""  
    created_at: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('created_at'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    r"""The moment when the user's record was created (e.g. \"2020-01-02T03:04:05.678123Z\")"""  
    email: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('email') }})
    r"""The user's email address"""  
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    r"""The user's name (human-readable format)"""  
    scheduling_url: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('scheduling_url') }})
    r"""The URL of the user's Calendly landing page (that lists all the user's event types)"""  
    slug: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('slug') }})
    r"""The portion of URL for the user's scheduling page (where invitees book sessions), rendered in a human-readable format"""  
    timezone: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('timezone') }})
    r"""The time zone to use when presenting time to the user"""  
    updated_at: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('updated_at'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    r"""The moment when the user's record was last updated (e.g. \"2020-01-02T03:04:05.678123Z\")"""  
    uri: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('uri') }})
    r"""Canonical reference (unique identifier) for the user"""  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class OrganizationMembership:
    
    created_at: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('created_at'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    r"""The moment when the membership record was created (e.g. \"2020-01-02T03:04:05.678123Z\")"""  
    organization: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('organization') }})
    r"""A unique reference to the organization"""  
    role: OrganizationMembershipRoleEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('role') }})
    r"""The user's role in the organization"""  
    updated_at: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('updated_at'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    r"""The moment when the membership record was last updated (e.g. \"2020-01-02T03:04:05.678123Z\")"""  
    uri: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('uri') }})
    r"""Canonical reference (unique identifier) for the membership"""  
    user: OrganizationMembershipUser = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('user') }})
    r"""Information about the user."""  
    