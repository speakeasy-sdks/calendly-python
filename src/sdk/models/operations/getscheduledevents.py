from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import event as shared_event
from ..shared import pagination as shared_pagination
from ..shared import security as shared_security
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from sdk import utils
from typing import Optional


@dataclasses.dataclass
class GetScheduledEventsSecurity:
    oauth2: Optional[shared_security.SchemeOauth2] = dataclasses.field(default=None, metadata={'security': { 'scheme': True, 'type': 'oauth2' }})
    personal_access_token: Optional[shared_security.SchemePersonalAccessToken] = dataclasses.field(default=None, metadata={'security': { 'scheme': True, 'type': 'http', 'sub_type': 'bearer' }})
    
class GetScheduledEventsStatusEnum(str, Enum):
    ACTIVE = "active"
    CANCELED = "canceled"


@dataclasses.dataclass
class GetScheduledEventsQueryParams:
    count: Optional[float] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'count', 'style': 'form', 'explode': True }})
    invitee_email: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'invitee_email', 'style': 'form', 'explode': True }})
    max_start_time: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'max_start_time', 'style': 'form', 'explode': True }})
    min_start_time: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'min_start_time', 'style': 'form', 'explode': True }})
    organization: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'organization', 'style': 'form', 'explode': True }})
    page_token: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'page_token', 'style': 'form', 'explode': True }})
    sort: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'sort', 'style': 'form', 'explode': True }})
    status: Optional[GetScheduledEventsStatusEnum] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'status', 'style': 'form', 'explode': True }})
    user: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'user', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class GetScheduledEventsRequest:
    query_params: GetScheduledEventsQueryParams = dataclasses.field()
    security: GetScheduledEventsSecurity = dataclasses.field()
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetScheduledEventsErrorResponseDetails:
    message: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message') }})
    parameter: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('parameter'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetScheduledEventsErrorResponse:
    r"""GetScheduledEventsErrorResponse
    Error Object
    """
    
    message: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message') }})
    title: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('title') }})
    details: Optional[list[GetScheduledEventsErrorResponseDetails]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('details'), 'exclude': lambda f: f is None }})
    
class GetScheduledEvents403ApplicationJSONMessageEnum(str, Enum):
    YOU_DO_NOT_HAVE_PERMISSION_TO_ACCESS_THIS_RESOURCE_ = "You do not have permission to access this resource."
    PLEASE_ALSO_SPECIFY_ORGANIZATION_WHEN_REQUESTING_EVENTS_FOR_A_USER_WITHIN_YOUR_ORGANIZATION_ = "Please also specify organization when requesting events for a user within your organization."
    THIS_USER_IS_NOT_IN_YOUR_ORGANIZATION = "This user is not in your organization"
    YOU_DO_NOT_HAVE_PERMISSION = "You do not have permission"

class GetScheduledEvents403ApplicationJSONTitleEnum(str, Enum):
    PERMISSION_DENIED = "Permission Denied"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetScheduledEvents403ApplicationJSON:
    message: Optional[GetScheduledEvents403ApplicationJSONMessageEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message'), 'exclude': lambda f: f is None }})
    title: Optional[GetScheduledEvents403ApplicationJSONTitleEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('title'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetScheduledEvents200ApplicationJSON:
    r"""GetScheduledEvents200ApplicationJSON
    Service response
    """
    
    collection: list[shared_event.Event] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('collection') }})
    pagination: shared_pagination.Pagination = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pagination') }})
    

@dataclasses.dataclass
class GetScheduledEventsResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    error_response: Optional[GetScheduledEventsErrorResponse] = dataclasses.field(default=None)
    get_scheduled_events_200_application_json_object: Optional[GetScheduledEvents200ApplicationJSON] = dataclasses.field(default=None)
    get_scheduled_events_403_application_json_object: Optional[GetScheduledEvents403ApplicationJSON] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    