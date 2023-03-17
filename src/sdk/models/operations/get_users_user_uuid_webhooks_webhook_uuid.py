from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import webhooksubscription as shared_webhooksubscription
from dataclasses_json import Undefined, dataclass_json
from sdk import utils
from typing import Optional


@dataclasses.dataclass
class GetUsersUserUUIDWebhooksWebhookUUIDPathParams:
    webhook_uuid: str = dataclasses.field(metadata={'path_param': { 'field_name': 'webhook_uuid', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class GetUsersUserUUIDWebhooksWebhookUUIDRequest:
    path_params: GetUsersUserUUIDWebhooksWebhookUUIDPathParams = dataclasses.field()
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetUsersUserUUIDWebhooksWebhookUUIDErrorResponseDetails:
    message: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message') }})
    parameter: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('parameter'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetUsersUserUUIDWebhooksWebhookUUIDErrorResponse:
    r"""GetUsersUserUUIDWebhooksWebhookUUIDErrorResponse
    Error Object
    """
    
    message: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message') }})
    title: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('title') }})
    details: Optional[list[GetUsersUserUUIDWebhooksWebhookUUIDErrorResponseDetails]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('details'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetUsersUserUUIDWebhooksWebhookUUID200ApplicationJSON:
    resource: shared_webhooksubscription.WebhookSubscription = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('resource') }})
    

@dataclasses.dataclass
class GetUsersUserUUIDWebhooksWebhookUUIDResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    error_response: Optional[GetUsersUserUUIDWebhooksWebhookUUIDErrorResponse] = dataclasses.field(default=None)
    get_users_user_uuid_webhooks_webhook_uuid_200_application_json_object: Optional[GetUsersUserUUIDWebhooksWebhookUUID200ApplicationJSON] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    