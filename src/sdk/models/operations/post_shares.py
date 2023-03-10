from __future__ import annotations
import dataclasses
import dateutil.parser
import requests as requests_http
from ..shared import share as shared_share
from dataclasses_json import Undefined, dataclass_json
from datetime import date
from enum import Enum
from marshmallow import fields
from sdk import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostSharesRequestBodyAvailabilityRuleRulesIntervals:
    from_: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('from'), 'exclude': lambda f: f is None }})
    to: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('to'), 'exclude': lambda f: f is None }})
    
class PostSharesRequestBodyAvailabilityRuleRulesTypeEnum(str, Enum):
    WDAY = "wday"
    DATE = "date"

class PostSharesRequestBodyAvailabilityRuleRulesWdayEnum(str, Enum):
    SUNDAY = "sunday"
    MONDAY = "monday"
    TUESDAY = "tuesday"
    WEDNESDAY = "wednesday"
    THURSDAY = "thursday"
    FRIDAY = "friday"
    SATURDAY = "saturday"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostSharesRequestBodyAvailabilityRuleRules:
    date_: Optional[date] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('date'), 'encoder': utils.dateisoformat(True), 'decoder': utils.datefromisoformat, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    intervals: Optional[list[PostSharesRequestBodyAvailabilityRuleRulesIntervals]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('intervals'), 'exclude': lambda f: f is None }})
    type: Optional[PostSharesRequestBodyAvailabilityRuleRulesTypeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type'), 'exclude': lambda f: f is None }})
    wday: Optional[PostSharesRequestBodyAvailabilityRuleRulesWdayEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('wday'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostSharesRequestBodyAvailabilityRule:
    rules: Optional[list[PostSharesRequestBodyAvailabilityRuleRules]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('rules'), 'exclude': lambda f: f is None }})
    timezone: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('timezone'), 'exclude': lambda f: f is None }})
    
class PostSharesRequestBodyLocationConfigurationsKindEnum(str, Enum):
    PHYSICAL = "physical"
    ASK_INVITEE = "ask_invitee"
    CUSTOM = "custom"
    OUTBOUND_CALL = "outbound_call"
    INBOUND_CALL = "inbound_call"
    GOOGLE_CONFERENCE = "google_conference"
    GOTOMEETING_CONFERENCE = "gotomeeting_conference"
    MICROSOFT_TEAMS_CONFERENCE = "microsoft_teams_conference"
    WEBEX_CONFERENCE = "webex_conference"
    ZOOM_CONFERENCE = "zoom_conference"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostSharesRequestBodyLocationConfigurations:
    additional_info: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('additional_info'), 'exclude': lambda f: f is None }})
    kind: Optional[PostSharesRequestBodyLocationConfigurationsKindEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('kind'), 'exclude': lambda f: f is None }})
    location: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('location'), 'exclude': lambda f: f is None }})
    phone_number: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('phone_number'), 'exclude': lambda f: f is None }})
    position: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('position'), 'exclude': lambda f: f is None }})
    
class PostSharesRequestBodyPeriodTypeEnum(str, Enum):
    AVAILABLE_MOVING = "available_moving"
    MOVING = "moving"
    FIXED = "fixed"
    UNLIMITED = "unlimited"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostSharesRequestBody:
    event_type: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('event_type') }})
    availability_rule: Optional[PostSharesRequestBodyAvailabilityRule] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('availability_rule'), 'exclude': lambda f: f is None }})
    duration: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('duration'), 'exclude': lambda f: f is None }})
    end_date: Optional[date] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('end_date'), 'encoder': utils.dateisoformat(True), 'decoder': utils.datefromisoformat, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    hide_location: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('hide_location'), 'exclude': lambda f: f is None }})
    location_configurations: Optional[list[PostSharesRequestBodyLocationConfigurations]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('location_configurations'), 'exclude': lambda f: f is None }})
    max_booking_time: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('max_booking_time'), 'exclude': lambda f: f is None }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name'), 'exclude': lambda f: f is None }})
    period_type: Optional[PostSharesRequestBodyPeriodTypeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('period_type'), 'exclude': lambda f: f is None }})
    start_date: Optional[date] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_date'), 'encoder': utils.dateisoformat(True), 'decoder': utils.datefromisoformat, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    

@dataclasses.dataclass
class PostSharesRequest:
    request: PostSharesRequestBody = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostSharesErrorResponseDetails:
    message: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message') }})
    parameter: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('parameter'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostSharesErrorResponse:
    r"""PostSharesErrorResponse
    Error Object
    """
    
    message: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message') }})
    title: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('title') }})
    details: Optional[list[PostSharesErrorResponseDetails]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('details'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostShares201ApplicationJSON:
    resource: shared_share.Share = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('resource') }})
    

@dataclasses.dataclass
class PostSharesResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    error_response: Optional[PostSharesErrorResponse] = dataclasses.field(default=None)
    post_shares_201_application_json_object: Optional[PostShares201ApplicationJSON] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    