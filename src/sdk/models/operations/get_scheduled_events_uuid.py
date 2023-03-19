from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import event as shared_event
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from sdk import utils
from typing import Optional


@dataclasses.dataclass
class GetScheduledEventsUUIDPathParams:
    uuid: str = dataclasses.field(metadata={'path_param': { 'field_name': 'uuid', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class GetScheduledEventsUUIDRequest:
    path_params: GetScheduledEventsUUIDPathParams = dataclasses.field()
    
class GetScheduledEventsUUID403ApplicationJSONMessageEnum(str, Enum):
    YOU_ARE_NOT_ALLOWED_TO_VIEW_THIS_EVENT = "You are not allowed to view this event"

class GetScheduledEventsUUID403ApplicationJSONTitleEnum(str, Enum):
    PERMISSION_DENIED = "Permission Denied"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetScheduledEventsUUID403ApplicationJSON:
    message: Optional[GetScheduledEventsUUID403ApplicationJSONMessageEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message'), 'exclude': lambda f: f is None }})
    title: Optional[GetScheduledEventsUUID403ApplicationJSONTitleEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('title'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetScheduledEventsUUIDErrorResponseDetails:
    message: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message') }})
    parameter: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('parameter'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetScheduledEventsUUIDErrorResponse:
    r"""GetScheduledEventsUUIDErrorResponse
    Error Object
    """
    
    message: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message') }})
    title: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('title') }})
    details: Optional[list[GetScheduledEventsUUIDErrorResponseDetails]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('details'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetScheduledEventsUUID200ApplicationJSON:
    resource: shared_event.Event = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('resource') }})
    

@dataclasses.dataclass
class GetScheduledEventsUUIDResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    error_response: Optional[GetScheduledEventsUUIDErrorResponse] = dataclasses.field(default=None)
    get_scheduled_events_uuid_200_application_json_object: Optional[GetScheduledEventsUUID200ApplicationJSON] = dataclasses.field(default=None)
    get_scheduled_events_uuid_403_application_json_object: Optional[GetScheduledEventsUUID403ApplicationJSON] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    