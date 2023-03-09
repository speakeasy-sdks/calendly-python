from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import cancellation as shared_cancellation
from ..shared import security as shared_security
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from sdk import utils
from typing import Optional


@dataclasses.dataclass
class PostScheduledEventsUUIDCancellationSecurity:
    oauth2: Optional[shared_security.SchemeOauth2] = dataclasses.field(default=None, metadata={'security': { 'scheme': True, 'type': 'oauth2' }})
    personal_access_token: Optional[shared_security.SchemePersonalAccessToken] = dataclasses.field(default=None, metadata={'security': { 'scheme': True, 'type': 'http', 'sub_type': 'bearer' }})
    

@dataclasses.dataclass
class PostScheduledEventsUUIDCancellationPathParams:
    uuid: str = dataclasses.field(metadata={'path_param': { 'field_name': 'uuid', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class PostScheduledEventsUUIDCancellationRawRequest:
    path_params: PostScheduledEventsUUIDCancellationPathParams = dataclasses.field()
    security: PostScheduledEventsUUIDCancellationSecurity = dataclasses.field()
    request: Optional[bytes] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/xml' }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostScheduledEventsUUIDCancellationRawErrorResponseDetails:
    message: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message') }})
    parameter: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('parameter'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostScheduledEventsUUIDCancellationRawErrorResponse:
    r"""PostScheduledEventsUUIDCancellationRawErrorResponse
    Error Object
    """
    
    message: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message') }})
    title: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('title') }})
    details: Optional[list[PostScheduledEventsUUIDCancellationRawErrorResponseDetails]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('details'), 'exclude': lambda f: f is None }})
    
class PostScheduledEventsUUIDCancellationRaw403ApplicationJSONMessageEnum(str, Enum):
    YOU_ARE_NOT_ALLOWED_TO_CANCEL_THIS_EVENT = "You are not allowed to cancel this event"
    EVENT_IN_THE_PAST = "Event in the past"
    EVENT_IS_ALREADY_CANCELED = "Event is already canceled"

class PostScheduledEventsUUIDCancellationRaw403ApplicationJSONTitleEnum(str, Enum):
    PERMISSION_DENIED = "Permission Denied"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostScheduledEventsUUIDCancellationRaw403ApplicationJSON:
    message: Optional[PostScheduledEventsUUIDCancellationRaw403ApplicationJSONMessageEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message'), 'exclude': lambda f: f is None }})
    title: Optional[PostScheduledEventsUUIDCancellationRaw403ApplicationJSONTitleEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('title'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostScheduledEventsUUIDCancellationRaw201ApplicationJSON:
    resource: shared_cancellation.Cancellation = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('resource') }})
    

@dataclasses.dataclass
class PostScheduledEventsUUIDCancellationRawResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    error_response: Optional[PostScheduledEventsUUIDCancellationRawErrorResponse] = dataclasses.field(default=None)
    post_scheduled_events_uuid_cancellation_raw_201_application_json_object: Optional[PostScheduledEventsUUIDCancellationRaw201ApplicationJSON] = dataclasses.field(default=None)
    post_scheduled_events_uuid_cancellation_raw_403_application_json_object: Optional[PostScheduledEventsUUIDCancellationRaw403ApplicationJSON] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    