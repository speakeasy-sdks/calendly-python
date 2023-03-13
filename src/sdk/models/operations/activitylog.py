from __future__ import annotations
import dataclasses
import dateutil.parser
import requests as requests_http
from ..shared import entry as shared_entry
from ..shared import pagination as shared_pagination
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from enum import Enum
from marshmallow import fields
from sdk import utils
from typing import Optional

class ActivityLogSortEnum(str, Enum):
    ACTION_ASC = "action:asc"
    ACTION_DESC = "action:desc"
    ACTOR_DISPLAY_NAME_ASC = "actor.display_name:asc"
    ACTOR_DISPLAY_NAME_DESC = "actor.display_name:desc"
    ACTOR_URI_ASC = "actor.uri:asc"
    ACTOR_URI_DESC = "actor.uri:desc"
    NAMESPACE_ASC = "namespace:asc"
    NAMESPACE_DESC = "namespace:desc"
    OCCURRED_AT_ASC = "occurred_at:asc"
    OCCURRED_AT_DESC = "occurred_at:desc"


@dataclasses.dataclass
class ActivityLogQueryParams:
    organization: str = dataclasses.field(metadata={'query_param': { 'field_name': 'organization', 'style': 'form', 'explode': True }})
    action: Optional[list[str]] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'action', 'style': 'form', 'explode': False }})
    actor: Optional[list[str]] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'actor', 'style': 'form', 'explode': False }})
    count: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'count', 'style': 'form', 'explode': True }})
    max_occurred_at: Optional[datetime] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'max_occurred_at', 'style': 'form', 'explode': True }})
    min_occurred_at: Optional[datetime] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'min_occurred_at', 'style': 'form', 'explode': True }})
    namespace: Optional[list[str]] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'namespace', 'style': 'form', 'explode': False }})
    page_token: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'page_token', 'style': 'form', 'explode': True }})
    search_term: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'search_term', 'style': 'form', 'explode': True }})
    sort: Optional[list[ActivityLogSortEnum]] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'sort', 'style': 'form', 'explode': False }})
    

@dataclasses.dataclass
class ActivityLogRequest:
    query_params: ActivityLogQueryParams = dataclasses.field()
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ActivityLogErrorResponseDetails:
    message: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message') }})
    parameter: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('parameter'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ActivityLogErrorResponse:
    r"""ActivityLogErrorResponse
    Error Object
    """
    
    message: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message') }})
    title: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('title') }})
    details: Optional[list[ActivityLogErrorResponseDetails]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('details'), 'exclude': lambda f: f is None }})
    
class ActivityLog403ApplicationJSONMessageEnum(str, Enum):
    PLEASE_UPGRADE_YOUR_CALENDLY_ACCOUNT_TO_ENTERPRISE_ = "Please upgrade your Calendly account to Enterprise."
    YOU_DO_NOT_HAVE_PERMISSION_TO_ACCESS_THIS_RESOURCE_ = "You do not have permission to access this resource."

class ActivityLog403ApplicationJSONTitleEnum(str, Enum):
    PERMISSION_DENIED = "Permission Denied"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ActivityLog403ApplicationJSON:
    message: Optional[ActivityLog403ApplicationJSONMessageEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message'), 'exclude': lambda f: f is None }})
    title: Optional[ActivityLog403ApplicationJSONTitleEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('title'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ActivityLog200ApplicationJSON:
    r"""ActivityLog200ApplicationJSON
    Activity log response
    """
    
    collection: list[shared_entry.Entry] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('collection') }})
    exceeds_max_total_count: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('exceeds_max_total_count') }})
    pagination: shared_pagination.Pagination = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pagination') }})
    total_count: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('total_count') }})
    last_event_time: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('last_event_time'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    

@dataclasses.dataclass
class ActivityLogResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    activity_log_200_application_json_object: Optional[ActivityLog200ApplicationJSON] = dataclasses.field(default=None)
    activity_log_403_application_json_object: Optional[ActivityLog403ApplicationJSON] = dataclasses.field(default=None)
    error_response: Optional[ActivityLogErrorResponse] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    