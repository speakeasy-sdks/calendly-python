"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import eventtypeavailabletime as shared_eventtypeavailabletime
from dataclasses_json import Undefined, dataclass_json
from sdk import utils
from typing import Optional


@dataclasses.dataclass
class GetEventTypeAvailableTimesRequest:
    
    end_time: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'end_time', 'style': 'form', 'explode': True }})
    r"""End time of the requested availability range."""  
    event_type: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'event_type', 'style': 'form', 'explode': True }})
    r"""The uri associated with the event type"""  
    start_time: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'start_time', 'style': 'form', 'explode': True }})
    r"""Start time of the requested availability range."""  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetEventTypeAvailableTimesErrorResponseDetails:
    
    message: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message') }})  
    parameter: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('parameter'), 'exclude': lambda f: f is None }})  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetEventTypeAvailableTimesErrorResponse:
    r"""Error Object"""
    
    message: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message') }})  
    title: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('title') }})  
    details: Optional[list[GetEventTypeAvailableTimesErrorResponseDetails]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('details'), 'exclude': lambda f: f is None }})  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetEventTypeAvailableTimes200ApplicationJSON:
    r"""Service Response"""
    
    collection: list[shared_eventtypeavailabletime.EventTypeAvailableTime] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('collection') }})
    r"""The set of available times for the event type matching the criteria"""  
    

@dataclasses.dataclass
class GetEventTypeAvailableTimesResponse:
    
    content_type: str = dataclasses.field()  
    status_code: int = dataclasses.field()  
    error_response: Optional[GetEventTypeAvailableTimesErrorResponse] = dataclasses.field(default=None)
    r"""Request is not valid"""  
    get_event_type_available_times_200_application_json_object: Optional[GetEventTypeAvailableTimes200ApplicationJSON] = dataclasses.field(default=None)
    r"""OK"""  
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)  
    