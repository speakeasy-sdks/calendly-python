from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import errorresponse as shared_errorresponse
from ..shared import organizationinvitation as shared_organizationinvitation
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from sdk import utils
from typing import Optional


@dataclasses.dataclass
class PostOrganizationsUUIDInvitationsPathParams:
    uuid: str = dataclasses.field(metadata={'path_param': { 'field_name': 'uuid', 'style': 'simple', 'explode': False }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostOrganizationsUUIDInvitationsRequestBody:
    email: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('email') }})
    

@dataclasses.dataclass
class PostOrganizationsUUIDInvitationsRequest:
    path_params: PostOrganizationsUUIDInvitationsPathParams = dataclasses.field()
    request: PostOrganizationsUUIDInvitationsRequestBody = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostOrganizationsUUIDInvitationsErrorResponseDetails:
    message: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message') }})
    parameter: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('parameter'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostOrganizationsUUIDInvitationsErrorResponse:
    r"""PostOrganizationsUUIDInvitationsErrorResponse
    Error Object
    """
    
    message: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message') }})
    title: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('title') }})
    details: Optional[list[PostOrganizationsUUIDInvitationsErrorResponseDetails]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('details'), 'exclude': lambda f: f is None }})
    
class PostOrganizationsUUIDInvitations403ApplicationJSONMessageEnum(str, Enum):
    YOU_ALREADY_SENT_ALL_THE_INVITATIONS_YOU_RE_ALLOTTED_BASED_UPON_THE_NUMBER_OF_SEATS_PURCHASED_WITH_YOUR_ACCOUNT_PLEASE_PURCHASE_MORE_SEATS_TO_SEND_MORE_INVITATIONS_ = "You already sent all the invitations you're allotted based upon the number of seats purchased with your account. Please purchase more seats to send more invitations."
    YOU_ALREADY_SENT_ALL_THE_INVITATIONS_ALLOTTED_TO_YOU_WITH_A_TRIAL_ACCOUNT_ = "You already sent all the invitations allotted to you with a trial account."
    YOU_DO_NOT_HAVE_PERMISSION = "You do not have permission"
    YOU_CANNOT_PERFORM_THIS_ACTION_FOR_AN_ORGANIZATION_WITH_SCIM_ENABLED_ = "You cannot perform this action for an organization with SCIM enabled."

class PostOrganizationsUUIDInvitations403ApplicationJSONTitleEnum(str, Enum):
    PERMISSION_DENIED = "Permission Denied"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostOrganizationsUUIDInvitations403ApplicationJSON:
    message: Optional[PostOrganizationsUUIDInvitations403ApplicationJSONMessageEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message'), 'exclude': lambda f: f is None }})
    title: Optional[PostOrganizationsUUIDInvitations403ApplicationJSONTitleEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('title'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostOrganizationsUUIDInvitations201ApplicationJSON:
    resource: shared_organizationinvitation.OrganizationInvitation = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('resource') }})
    

@dataclasses.dataclass
class PostOrganizationsUUIDInvitationsResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    error_response1: Optional[PostOrganizationsUUIDInvitationsErrorResponse] = dataclasses.field(default=None)
    error_response: Optional[shared_errorresponse.ErrorResponse] = dataclasses.field(default=None)
    post_organizations_uuid_invitations_201_application_json_object: Optional[PostOrganizationsUUIDInvitations201ApplicationJSON] = dataclasses.field(default=None)
    post_organizations_uuid_invitations_403_application_json_object: Optional[PostOrganizationsUUIDInvitations403ApplicationJSON] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    