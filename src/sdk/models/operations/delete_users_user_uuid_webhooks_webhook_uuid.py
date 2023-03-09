from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import security as shared_security
from dataclasses_json import Undefined, dataclass_json
from sdk import utils
from typing import Optional


@dataclasses.dataclass
class DeleteUsersUserUUIDWebhooksWebhookUUIDSecurity:
    oauth2: Optional[shared_security.SchemeOauth2] = dataclasses.field(default=None, metadata={'security': { 'scheme': True, 'type': 'oauth2' }})
    personal_access_token: Optional[shared_security.SchemePersonalAccessToken] = dataclasses.field(default=None, metadata={'security': { 'scheme': True, 'type': 'http', 'sub_type': 'bearer' }})
    

@dataclasses.dataclass
class DeleteUsersUserUUIDWebhooksWebhookUUIDPathParams:
    webhook_uuid: str = dataclasses.field(metadata={'path_param': { 'field_name': 'webhook_uuid', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class DeleteUsersUserUUIDWebhooksWebhookUUIDRequest:
    path_params: DeleteUsersUserUUIDWebhooksWebhookUUIDPathParams = dataclasses.field()
    security: DeleteUsersUserUUIDWebhooksWebhookUUIDSecurity = dataclasses.field()
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DeleteUsersUserUUIDWebhooksWebhookUUIDErrorResponseDetails:
    message: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message') }})
    parameter: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('parameter'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DeleteUsersUserUUIDWebhooksWebhookUUIDErrorResponse:
    r"""DeleteUsersUserUUIDWebhooksWebhookUUIDErrorResponse
    Error Object
    """
    
    message: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message') }})
    title: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('title') }})
    details: Optional[list[DeleteUsersUserUUIDWebhooksWebhookUUIDErrorResponseDetails]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('details'), 'exclude': lambda f: f is None }})
    

@dataclasses.dataclass
class DeleteUsersUserUUIDWebhooksWebhookUUIDResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    error_response: Optional[DeleteUsersUserUUIDWebhooksWebhookUUIDErrorResponse] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    