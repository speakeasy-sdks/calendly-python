from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import availabilityschedule as shared_availabilityschedule
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from sdk import utils
from typing import Optional


@dataclasses.dataclass
class GetUserAvailabilitySchedulesUUIDPathParams:
    uuid: str = dataclasses.field(metadata={'path_param': { 'field_name': 'uuid', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class GetUserAvailabilitySchedulesUUIDRequest:
    path_params: GetUserAvailabilitySchedulesUUIDPathParams = dataclasses.field()
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetUserAvailabilitySchedulesUUIDErrorResponseDetails:
    message: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message') }})
    parameter: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('parameter'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetUserAvailabilitySchedulesUUIDErrorResponse:
    r"""GetUserAvailabilitySchedulesUUIDErrorResponse
    Error Object
    """
    
    message: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message') }})
    title: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('title') }})
    details: Optional[list[GetUserAvailabilitySchedulesUUIDErrorResponseDetails]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('details'), 'exclude': lambda f: f is None }})
    
class GetUserAvailabilitySchedulesUUID403ApplicationJSONMessageEnum(str, Enum):
    THIS_USER_IS_NOT_IN_YOUR_ORGANIZATION = "This user is not in your organization"

class GetUserAvailabilitySchedulesUUID403ApplicationJSONTitleEnum(str, Enum):
    PERMISSION_DENIED = "Permission Denied"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetUserAvailabilitySchedulesUUID403ApplicationJSON:
    message: Optional[GetUserAvailabilitySchedulesUUID403ApplicationJSONMessageEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message'), 'exclude': lambda f: f is None }})
    title: Optional[GetUserAvailabilitySchedulesUUID403ApplicationJSONTitleEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('title'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetUserAvailabilitySchedulesUUID200ApplicationJSON:
    resource: shared_availabilityschedule.AvailabilitySchedule = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('resource') }})
    

@dataclasses.dataclass
class GetUserAvailabilitySchedulesUUIDResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    error_response: Optional[GetUserAvailabilitySchedulesUUIDErrorResponse] = dataclasses.field(default=None)
    get_user_availability_schedules_uuid_200_application_json_object: Optional[GetUserAvailabilitySchedulesUUID200ApplicationJSON] = dataclasses.field(default=None)
    get_user_availability_schedules_uuid_403_application_json_object: Optional[GetUserAvailabilitySchedulesUUID403ApplicationJSON] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    