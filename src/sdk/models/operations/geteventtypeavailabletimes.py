from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import eventtypeavailabletime as shared_eventtypeavailabletime
from ..shared import security as shared_security
from dataclasses_json import Undefined, dataclass_json
from sdk import utils
from typing import Optional


@dataclasses.dataclass
class GetEventTypeAvailableTimesSecurity:
    oauth2: Optional[shared_security.SchemeOauth2] = dataclasses.field(default=None, metadata={'security': { 'scheme': True, 'type': 'oauth2' }})
    personal_access_token: Optional[shared_security.SchemePersonalAccessToken] = dataclasses.field(default=None, metadata={'security': { 'scheme': True, 'type': 'http', 'sub_type': 'bearer' }})
    

@dataclasses.dataclass
class GetEventTypeAvailableTimesQueryParams:
    end_time: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'end_time', 'style': 'form', 'explode': True }})
    event_type: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'event_type', 'style': 'form', 'explode': True }})
    start_time: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'start_time', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class GetEventTypeAvailableTimesRequest:
    query_params: GetEventTypeAvailableTimesQueryParams = dataclasses.field()
    security: GetEventTypeAvailableTimesSecurity = dataclasses.field()
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetEventTypeAvailableTimesErrorResponseDetails:
    message: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message') }})
    parameter: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('parameter'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetEventTypeAvailableTimesErrorResponse:
    r"""GetEventTypeAvailableTimesErrorResponse
    Error Object
    """
    
    message: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message') }})
    title: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('title') }})
    details: Optional[list[GetEventTypeAvailableTimesErrorResponseDetails]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('details'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetEventTypeAvailableTimes200ApplicationJSON:
    r"""GetEventTypeAvailableTimes200ApplicationJSON
    Service Response
    """
    
    collection: list[shared_eventtypeavailabletime.EventTypeAvailableTime] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('collection') }})
    

@dataclasses.dataclass
class GetEventTypeAvailableTimesResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    error_response: Optional[GetEventTypeAvailableTimesErrorResponse] = dataclasses.field(default=None)
    get_event_type_available_times_200_application_json_object: Optional[GetEventTypeAvailableTimes200ApplicationJSON] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    