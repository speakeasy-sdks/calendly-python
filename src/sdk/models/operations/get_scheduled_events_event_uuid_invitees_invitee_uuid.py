"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import errorresponse as shared_errorresponse
from ..shared import invitee as shared_invitee
from dataclasses_json import Undefined, dataclass_json
from sdk import utils
from typing import Optional


@dataclasses.dataclass
class GetScheduledEventsEventUUIDInviteesInviteeUUIDPathParams:
    
    event_uuid: str = dataclasses.field(metadata={'path_param': { 'field_name': 'event_uuid', 'style': 'simple', 'explode': False }})
    r"""The event's unique identifier"""  
    invitee_uuid: str = dataclasses.field(metadata={'path_param': { 'field_name': 'invitee_uuid', 'style': 'simple', 'explode': False }})
    r"""The invitee's unique identifier"""  
    

@dataclasses.dataclass
class GetScheduledEventsEventUUIDInviteesInviteeUUIDRequest:
    
    path_params: GetScheduledEventsEventUUIDInviteesInviteeUUIDPathParams = dataclasses.field()  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetScheduledEventsEventUUIDInviteesInviteeUUIDErrorResponseDetails:
    
    message: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message') }})  
    parameter: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('parameter'), 'exclude': lambda f: f is None }})  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetScheduledEventsEventUUIDInviteesInviteeUUIDErrorResponse:
    r"""Error Object"""
    
    message: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message') }})  
    title: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('title') }})  
    details: Optional[list[GetScheduledEventsEventUUIDInviteesInviteeUUIDErrorResponseDetails]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('details'), 'exclude': lambda f: f is None }})  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetScheduledEventsEventUUIDInviteesInviteeUUID200ApplicationJSON:
    r"""OK"""
    
    resource: shared_invitee.Invitee = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('resource') }})
    r"""An individual who has been invited to meet with a Calendly member"""  
    

@dataclasses.dataclass
class GetScheduledEventsEventUUIDInviteesInviteeUUIDResponse:
    
    content_type: str = dataclasses.field()  
    status_code: int = dataclasses.field()  
    error_response: Optional[GetScheduledEventsEventUUIDInviteesInviteeUUIDErrorResponse] = dataclasses.field(default=None)
    r"""Request is not valid"""  
    error_response1: Optional[shared_errorresponse.ErrorResponse] = dataclasses.field(default=None)
    r"""Caller not authorized to view event"""  
    get_scheduled_events_event_uuid_invitees_invitee_uuid_200_application_json_object: Optional[GetScheduledEventsEventUUIDInviteesInviteeUUID200ApplicationJSON] = dataclasses.field(default=None)
    r"""OK"""  
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)  
    