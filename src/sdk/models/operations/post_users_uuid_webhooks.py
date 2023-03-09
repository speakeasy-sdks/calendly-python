from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import security as shared_security
from ..shared import webhooksubscription as shared_webhooksubscription
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from sdk import utils
from typing import Optional


@dataclasses.dataclass
class PostUsersUUIDWebhooksSecurity:
    oauth2: Optional[shared_security.SchemeOauth2] = dataclasses.field(default=None, metadata={'security': { 'scheme': True, 'type': 'oauth2' }})
    personal_access_token: Optional[shared_security.SchemePersonalAccessToken] = dataclasses.field(default=None, metadata={'security': { 'scheme': True, 'type': 'http', 'sub_type': 'bearer' }})
    
class PostUsersUUIDWebhooksRequestBodyEventsEnum(str, Enum):
    INVITEE_CANCELED = "invitee.canceled"
    INVITEE_CREATED = "invitee.created"
    ROUTING_FORM_SUBMISSION_CREATED = "routing_form_submission.created"

class PostUsersUUIDWebhooksRequestBodyScopeEnum(str, Enum):
    ORGANIZATION = "organization"
    USER = "user"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostUsersUUIDWebhooksRequestBody:
    events: list[PostUsersUUIDWebhooksRequestBodyEventsEnum] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('events') }})
    organization: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('organization') }})
    scope: PostUsersUUIDWebhooksRequestBodyScopeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('scope') }})
    url: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('url') }})
    signing_key: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('signing_key'), 'exclude': lambda f: f is None }})
    user: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('user'), 'exclude': lambda f: f is None }})
    

@dataclasses.dataclass
class PostUsersUUIDWebhooksRequest:
    request: PostUsersUUIDWebhooksRequestBody = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    security: PostUsersUUIDWebhooksSecurity = dataclasses.field()
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostUsersUUIDWebhooksErrorResponseDetails:
    message: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message') }})
    parameter: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('parameter'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostUsersUUIDWebhooksErrorResponse:
    r"""PostUsersUUIDWebhooksErrorResponse
    Error Object
    """
    
    message: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message') }})
    title: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('title') }})
    details: Optional[list[PostUsersUUIDWebhooksErrorResponseDetails]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('details'), 'exclude': lambda f: f is None }})
    
class PostUsersUUIDWebhooks403ApplicationJSONMessageEnum(str, Enum):
    PLEASE_UPGRADE_YOUR_CALENDLY_ACCOUNT_TO_PROFESSIONAL = "Please upgrade your Calendly account to Professional"
    YOU_DO_NOT_HAVE_PERMISSION_TO_ACCESS_THIS_RESOURCE_ = "You do not have permission to access this resource."
    YOU_DO_NOT_HAVE_PERMISSION = "You do not have permission"

class PostUsersUUIDWebhooks403ApplicationJSONTitleEnum(str, Enum):
    PERMISSION_DENIED = "Permission Denied"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostUsersUUIDWebhooks403ApplicationJSON:
    message: Optional[PostUsersUUIDWebhooks403ApplicationJSONMessageEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message'), 'exclude': lambda f: f is None }})
    title: Optional[PostUsersUUIDWebhooks403ApplicationJSONTitleEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('title'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostUsersUUIDWebhooks201ApplicationJSON:
    resource: shared_webhooksubscription.WebhookSubscription = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('resource') }})
    

@dataclasses.dataclass
class PostUsersUUIDWebhooksResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    error_response: Optional[PostUsersUUIDWebhooksErrorResponse] = dataclasses.field(default=None)
    post_users_uuid_webhooks_201_application_json_object: Optional[PostUsersUUIDWebhooks201ApplicationJSON] = dataclasses.field(default=None)
    post_users_uuid_webhooks_403_application_json_object: Optional[PostUsersUUIDWebhooks403ApplicationJSON] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    