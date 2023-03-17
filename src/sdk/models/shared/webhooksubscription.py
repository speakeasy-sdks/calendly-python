from __future__ import annotations
import dataclasses
import dateutil.parser
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from enum import Enum
from marshmallow import fields
from sdk import utils

class WebhookSubscriptionEventsEnum(str, Enum):
    INVITEE_CREATED = "invitee.created"
    INVITEE_CANCELED = "invitee.canceled"
    ROUTING_FORM_SUBMISSION_CREATED = "routing_form_submission.created"

class WebhookSubscriptionScopeEnum(str, Enum):
    USER = "user"
    ORGANIZATION = "organization"

class WebhookSubscriptionStateEnum(str, Enum):
    ACTIVE = "active"
    DISABLED = "disabled"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class WebhookSubscription:
    r"""WebhookSubscription
    Webhook Subscription Object
    """
    
    callback_url: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('callback_url') }})
    created_at: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('created_at'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    creator: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('creator') }})
    events: list[WebhookSubscriptionEventsEnum] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('events') }})
    organization: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('organization') }})
    retry_started_at: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('retry_started_at'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    scope: WebhookSubscriptionScopeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('scope') }})
    state: WebhookSubscriptionStateEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('state') }})
    updated_at: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('updated_at'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    uri: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('uri') }})
    user: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('user') }})
    