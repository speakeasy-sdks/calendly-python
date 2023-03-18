from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import cancellation as shared_cancellation
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from sdk import utils
from typing import Any, Optional


@dataclasses.dataclass
class PostScheduledEventsUUIDCancellationPathParams:
    uuid: str = dataclasses.field(metadata={'path_param': { 'field_name': 'uuid', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class PostScheduledEventsUUIDCancellationMultipartRequest:
    path_params: PostScheduledEventsUUIDCancellationPathParams = dataclasses.field()
    request: Optional[dict[str, Any]] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'multipart/form-data' }})
    
class PostScheduledEventsUUIDCancellationMultipart403ApplicationJSONMessageEnum(str, Enum):
    YOU_ARE_NOT_ALLOWED_TO_CANCEL_THIS_EVENT = "You are not allowed to cancel this event"
    EVENT_IN_THE_PAST = "Event in the past"
    EVENT_IS_ALREADY_CANCELED = "Event is already canceled"

class PostScheduledEventsUUIDCancellationMultipart403ApplicationJSONTitleEnum(str, Enum):
    PERMISSION_DENIED = "Permission Denied"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostScheduledEventsUUIDCancellationMultipart403ApplicationJSON:
    message: Optional[PostScheduledEventsUUIDCancellationMultipart403ApplicationJSONMessageEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message'), 'exclude': lambda f: f is None }})
    title: Optional[PostScheduledEventsUUIDCancellationMultipart403ApplicationJSONTitleEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('title'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostScheduledEventsUUIDCancellationMultipartErrorResponseDetails:
    message: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message') }})
    parameter: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('parameter'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostScheduledEventsUUIDCancellationMultipartErrorResponse:
    r"""PostScheduledEventsUUIDCancellationMultipartErrorResponse
    Error Object
    """
    
    message: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message') }})
    title: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('title') }})
    details: Optional[list[PostScheduledEventsUUIDCancellationMultipartErrorResponseDetails]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('details'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostScheduledEventsUUIDCancellationMultipart201ApplicationJSON:
    resource: shared_cancellation.Cancellation = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('resource') }})
    

@dataclasses.dataclass
class PostScheduledEventsUUIDCancellationMultipartResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    error_response: Optional[PostScheduledEventsUUIDCancellationMultipartErrorResponse] = dataclasses.field(default=None)
    post_scheduled_events_uuid_cancellation_multipart_201_application_json_object: Optional[PostScheduledEventsUUIDCancellationMultipart201ApplicationJSON] = dataclasses.field(default=None)
    post_scheduled_events_uuid_cancellation_multipart_403_application_json_object: Optional[PostScheduledEventsUUIDCancellationMultipart403ApplicationJSON] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    