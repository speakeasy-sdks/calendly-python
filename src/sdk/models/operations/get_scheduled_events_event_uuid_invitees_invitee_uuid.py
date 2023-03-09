from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import errorresponse as shared_errorresponse
from ..shared import invitee as shared_invitee
from ..shared import security as shared_security
from dataclasses_json import Undefined, dataclass_json
from sdk import utils
from typing import Optional


@dataclasses.dataclass
class GetScheduledEventsEventUUIDInviteesInviteeUUIDSecurity:
    oauth2: Optional[shared_security.SchemeOauth2] = dataclasses.field(default=None, metadata={'security': { 'scheme': True, 'type': 'oauth2' }})
    personal_access_token: Optional[shared_security.SchemePersonalAccessToken] = dataclasses.field(default=None, metadata={'security': { 'scheme': True, 'type': 'http', 'sub_type': 'bearer' }})
    

@dataclasses.dataclass
class GetScheduledEventsEventUUIDInviteesInviteeUUIDPathParams:
    event_uuid: str = dataclasses.field(metadata={'path_param': { 'field_name': 'event_uuid', 'style': 'simple', 'explode': False }})
    invitee_uuid: str = dataclasses.field(metadata={'path_param': { 'field_name': 'invitee_uuid', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class GetScheduledEventsEventUUIDInviteesInviteeUUIDRequest:
    path_params: GetScheduledEventsEventUUIDInviteesInviteeUUIDPathParams = dataclasses.field()
    security: GetScheduledEventsEventUUIDInviteesInviteeUUIDSecurity = dataclasses.field()
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetScheduledEventsEventUUIDInviteesInviteeUUIDErrorResponseDetails:
    message: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message') }})
    parameter: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('parameter'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetScheduledEventsEventUUIDInviteesInviteeUUIDErrorResponse:
    r"""GetScheduledEventsEventUUIDInviteesInviteeUUIDErrorResponse
    Error Object
    """
    
    message: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message') }})
    title: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('title') }})
    details: Optional[list[GetScheduledEventsEventUUIDInviteesInviteeUUIDErrorResponseDetails]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('details'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetScheduledEventsEventUUIDInviteesInviteeUUID200ApplicationJSON:
    resource: shared_invitee.Invitee = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('resource') }})
    

@dataclasses.dataclass
class GetScheduledEventsEventUUIDInviteesInviteeUUIDResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    error_response: Optional[GetScheduledEventsEventUUIDInviteesInviteeUUIDErrorResponse] = dataclasses.field(default=None)
    error_response1: Optional[shared_errorresponse.ErrorResponse] = dataclasses.field(default=None)
    get_scheduled_events_event_uuid_invitees_invitee_uuid_200_application_json_object: Optional[GetScheduledEventsEventUUIDInviteesInviteeUUID200ApplicationJSON] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    