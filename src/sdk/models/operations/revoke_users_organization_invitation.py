from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import errorresponse as shared_errorresponse
from ..shared import security as shared_security
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from sdk import utils
from typing import Optional


@dataclasses.dataclass
class RevokeUsersOrganizationInvitationSecurity:
    oauth2: Optional[shared_security.SchemeOauth2] = dataclasses.field(default=None, metadata={'security': { 'scheme': True, 'type': 'oauth2' }})
    personal_access_token: Optional[shared_security.SchemePersonalAccessToken] = dataclasses.field(default=None, metadata={'security': { 'scheme': True, 'type': 'http', 'sub_type': 'bearer' }})
    

@dataclasses.dataclass
class RevokeUsersOrganizationInvitationPathParams:
    org_uuid: str = dataclasses.field(metadata={'path_param': { 'field_name': 'org_uuid', 'style': 'simple', 'explode': False }})
    uuid: str = dataclasses.field(metadata={'path_param': { 'field_name': 'uuid', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class RevokeUsersOrganizationInvitationRequest:
    path_params: RevokeUsersOrganizationInvitationPathParams = dataclasses.field()
    security: RevokeUsersOrganizationInvitationSecurity = dataclasses.field()
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class RevokeUsersOrganizationInvitationErrorResponseDetails:
    message: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message') }})
    parameter: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('parameter'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class RevokeUsersOrganizationInvitationErrorResponse:
    r"""RevokeUsersOrganizationInvitationErrorResponse
    Error Object
    """
    
    message: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message') }})
    title: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('title') }})
    details: Optional[list[RevokeUsersOrganizationInvitationErrorResponseDetails]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('details'), 'exclude': lambda f: f is None }})
    
class RevokeUsersOrganizationInvitation403ApplicationJSONMessageEnum(str, Enum):
    YOU_CANNOT_PERFORM_THIS_ACTION_FOR_AN_ORGANIZATION_WITH_SCIM_ENABLED_ = "You cannot perform this action for an organization with SCIM enabled."
    YOU_DO_NOT_HAVE_PERMISSION = "You do not have permission"
    YOU_DO_NOT_HAVE_PERMISSION_TO_ACCESS_THIS_RESOURCE_ = "You do not have permission to access this resource."

class RevokeUsersOrganizationInvitation403ApplicationJSONTitleEnum(str, Enum):
    PERMISSION_DENIED = "Permission Denied"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class RevokeUsersOrganizationInvitation403ApplicationJSON:
    message: Optional[RevokeUsersOrganizationInvitation403ApplicationJSONMessageEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message'), 'exclude': lambda f: f is None }})
    title: Optional[RevokeUsersOrganizationInvitation403ApplicationJSONTitleEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('title'), 'exclude': lambda f: f is None }})
    

@dataclasses.dataclass
class RevokeUsersOrganizationInvitationResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    error_response1: Optional[RevokeUsersOrganizationInvitationErrorResponse] = dataclasses.field(default=None)
    error_response: Optional[shared_errorresponse.ErrorResponse] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    revoke_users_organization_invitation_403_application_json_object: Optional[RevokeUsersOrganizationInvitation403ApplicationJSON] = dataclasses.field(default=None)
    