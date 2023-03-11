from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import availabilityschedule as shared_availabilityschedule
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from sdk import utils
from typing import Optional


@dataclasses.dataclass
class GetUserAvailabilitySchedulesQueryParams:
    user: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'user', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class GetUserAvailabilitySchedulesRequest:
    query_params: GetUserAvailabilitySchedulesQueryParams = dataclasses.field()
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetUserAvailabilitySchedulesErrorResponseDetails:
    message: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message') }})
    parameter: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('parameter'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetUserAvailabilitySchedulesErrorResponse:
    r"""GetUserAvailabilitySchedulesErrorResponse
    Error Object
    """
    
    message: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message') }})
    title: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('title') }})
    details: Optional[list[GetUserAvailabilitySchedulesErrorResponseDetails]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('details'), 'exclude': lambda f: f is None }})
    
class GetUserAvailabilitySchedules403ApplicationJSONMessageEnum(str, Enum):
    THIS_USER_IS_NOT_IN_YOUR_ORGANIZATION = "This user is not in your organization"

class GetUserAvailabilitySchedules403ApplicationJSONTitleEnum(str, Enum):
    PERMISSION_DENIED = "Permission Denied"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetUserAvailabilitySchedules403ApplicationJSON:
    message: Optional[GetUserAvailabilitySchedules403ApplicationJSONMessageEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message'), 'exclude': lambda f: f is None }})
    title: Optional[GetUserAvailabilitySchedules403ApplicationJSONTitleEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('title'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetUserAvailabilitySchedules200ApplicationJSON:
    collection: list[shared_availabilityschedule.AvailabilitySchedule] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('collection') }})
    

@dataclasses.dataclass
class GetUserAvailabilitySchedulesResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    error_response: Optional[GetUserAvailabilitySchedulesErrorResponse] = dataclasses.field(default=None)
    get_user_availability_schedules_200_application_json_object: Optional[GetUserAvailabilitySchedules200ApplicationJSON] = dataclasses.field(default=None)
    get_user_availability_schedules_403_application_json_object: Optional[GetUserAvailabilitySchedules403ApplicationJSON] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    