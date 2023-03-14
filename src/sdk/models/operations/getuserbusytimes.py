from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import errorresponse as shared_errorresponse
from ..shared import userbusytime as shared_userbusytime
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from sdk import utils
from typing import Optional


@dataclasses.dataclass
class GetUserBusyTimesQueryParams:
    end_time: str = dataclasses.field(metadata={'query_param': { 'field_name': 'end_time', 'style': 'form', 'explode': True }})
    start_time: str = dataclasses.field(metadata={'query_param': { 'field_name': 'start_time', 'style': 'form', 'explode': True }})
    user: str = dataclasses.field(metadata={'query_param': { 'field_name': 'user', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class GetUserBusyTimesRequest:
    query_params: GetUserBusyTimesQueryParams = dataclasses.field()
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetUserBusyTimesErrorResponseDetails:
    message: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message') }})
    parameter: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('parameter'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetUserBusyTimesErrorResponse:
    r"""GetUserBusyTimesErrorResponse
    Error Object
    """
    
    message: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message') }})
    title: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('title') }})
    details: Optional[list[GetUserBusyTimesErrorResponseDetails]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('details'), 'exclude': lambda f: f is None }})
    
class GetUserBusyTimes403ApplicationJSONMessageEnum(str, Enum):
    THIS_USER_IS_NOT_IN_YOUR_ORGANIZATION = "This user is not in your organization"

class GetUserBusyTimes403ApplicationJSONTitleEnum(str, Enum):
    PERMISSION_DENIED = "Permission Denied"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetUserBusyTimes403ApplicationJSON:
    message: Optional[GetUserBusyTimes403ApplicationJSONMessageEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message'), 'exclude': lambda f: f is None }})
    title: Optional[GetUserBusyTimes403ApplicationJSONTitleEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('title'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetUserBusyTimes200ApplicationJSON:
    r"""GetUserBusyTimes200ApplicationJSON
    Service Response
    """
    
    collection: list[shared_userbusytime.UserBusyTime] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('collection') }})
    

@dataclasses.dataclass
class GetUserBusyTimesResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    error_response: Optional[GetUserBusyTimesErrorResponse] = dataclasses.field(default=None)
    error_response1: Optional[shared_errorresponse.ErrorResponse] = dataclasses.field(default=None)
    get_user_busy_times_200_application_json_object: Optional[GetUserBusyTimes200ApplicationJSON] = dataclasses.field(default=None)
    get_user_busy_times_403_application_json_object: Optional[GetUserBusyTimes403ApplicationJSON] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    