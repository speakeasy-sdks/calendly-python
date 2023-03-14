from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import pagination as shared_pagination
from ..shared import webhooksubscription as shared_webhooksubscription
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from sdk import utils
from typing import Optional

class GetWebhooksScopeEnum(str, Enum):
    ORGANIZATION = "organization"
    USER = "user"


@dataclasses.dataclass
class GetWebhooksQueryParams:
    organization: str = dataclasses.field(metadata={'query_param': { 'field_name': 'organization', 'style': 'form', 'explode': True }})
    scope: GetWebhooksScopeEnum = dataclasses.field(metadata={'query_param': { 'field_name': 'scope', 'style': 'form', 'explode': True }})
    count: Optional[float] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'count', 'style': 'form', 'explode': True }})
    page_token: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'page_token', 'style': 'form', 'explode': True }})
    sort: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'sort', 'style': 'form', 'explode': True }})
    user: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'user', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class GetWebhooksRequest:
    query_params: GetWebhooksQueryParams = dataclasses.field()
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetWebhooksErrorResponseDetails:
    message: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message') }})
    parameter: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('parameter'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetWebhooksErrorResponse:
    r"""GetWebhooksErrorResponse
    Error Object
    """
    
    message: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message') }})
    title: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('title') }})
    details: Optional[list[GetWebhooksErrorResponseDetails]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('details'), 'exclude': lambda f: f is None }})
    
class GetWebhooks403ApplicationJSONMessageEnum(str, Enum):
    YOU_DO_NOT_HAVE_PERMISSION = "You do not have permission"
    YOU_DO_NOT_HAVE_PERMISSION_TO_ACCESS_THIS_RESOURCE_ = "You do not have permission to access this resource."
    UNAUTHORIZED = "Unauthorized"

class GetWebhooks403ApplicationJSONTitleEnum(str, Enum):
    PERMISSION_DENIED = "Permission Denied"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetWebhooks403ApplicationJSON:
    message: Optional[GetWebhooks403ApplicationJSONMessageEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message'), 'exclude': lambda f: f is None }})
    title: Optional[GetWebhooks403ApplicationJSONTitleEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('title'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetWebhooks200ApplicationJSON:
    collection: list[shared_webhooksubscription.WebhookSubscription] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('collection') }})
    pagination: shared_pagination.Pagination = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pagination') }})
    

@dataclasses.dataclass
class GetWebhooksResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    error_response: Optional[GetWebhooksErrorResponse] = dataclasses.field(default=None)
    get_webhooks_200_application_json_object: Optional[GetWebhooks200ApplicationJSON] = dataclasses.field(default=None)
    get_webhooks_403_application_json_object: Optional[GetWebhooks403ApplicationJSON] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    