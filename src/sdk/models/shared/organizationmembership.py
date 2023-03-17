from __future__ import annotations
import dataclasses
import dateutil.parser
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from enum import Enum
from marshmallow import fields
from sdk import utils

class OrganizationMembershipRoleEnum(str, Enum):
    USER = "user"
    ADMIN = "admin"
    OWNER = "owner"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class OrganizationMembershipUser:
    r"""OrganizationMembershipUser
    Information about the user.
    """
    
    avatar_url: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('avatar_url') }})
    created_at: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('created_at'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    email: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('email') }})
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    scheduling_url: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('scheduling_url') }})
    slug: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('slug') }})
    timezone: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('timezone') }})
    updated_at: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('updated_at'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    uri: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('uri') }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class OrganizationMembership:
    created_at: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('created_at'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    organization: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('organization') }})
    role: OrganizationMembershipRoleEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('role') }})
    updated_at: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('updated_at'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    uri: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('uri') }})
    user: OrganizationMembershipUser = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('user') }})
    