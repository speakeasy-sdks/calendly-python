from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import security as shared_security
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from sdk import utils
from typing import Optional


@dataclasses.dataclass
class PostSchedulingLinksSecurity:
    oauth2: Optional[shared_security.SchemeOauth2] = dataclasses.field(default=None, metadata={'security': { 'scheme': True, 'type': 'oauth2' }})
    personal_access_token: Optional[shared_security.SchemePersonalAccessToken] = dataclasses.field(default=None, metadata={'security': { 'scheme': True, 'type': 'http', 'sub_type': 'bearer' }})
    
class PostSchedulingLinksRequestBodyOwnerTypeEnum(str, Enum):
    EVENT_TYPE = "EventType"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostSchedulingLinksRequestBody:
    max_event_count: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('max_event_count') }})
    owner: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('owner') }})
    owner_type: PostSchedulingLinksRequestBodyOwnerTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('owner_type') }})
    

@dataclasses.dataclass
class PostSchedulingLinksRequest:
    request: PostSchedulingLinksRequestBody = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    security: PostSchedulingLinksSecurity = dataclasses.field()
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostSchedulingLinksErrorResponseDetails:
    message: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message') }})
    parameter: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('parameter'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostSchedulingLinksErrorResponse:
    r"""PostSchedulingLinksErrorResponse
    Error Object
    """
    
    message: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message') }})
    title: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('title') }})
    details: Optional[list[PostSchedulingLinksErrorResponseDetails]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('details'), 'exclude': lambda f: f is None }})
    
class PostSchedulingLinks201ApplicationJSONResourceOwnerTypeEnum(str, Enum):
    EVENT_TYPE = "EventType"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostSchedulingLinks201ApplicationJSONResource:
    booking_url: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('booking_url') }})
    owner: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('owner'), 'exclude': lambda f: f is None }})
    owner_type: Optional[PostSchedulingLinks201ApplicationJSONResourceOwnerTypeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('owner_type'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostSchedulingLinks201ApplicationJSON:
    resource: PostSchedulingLinks201ApplicationJSONResource = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('resource') }})
    

@dataclasses.dataclass
class PostSchedulingLinksResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    error_response: Optional[PostSchedulingLinksErrorResponse] = dataclasses.field(default=None)
    post_scheduling_links_201_application_json_object: Optional[PostSchedulingLinks201ApplicationJSON] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    