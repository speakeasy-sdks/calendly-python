from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import organizationinvitation as shared_organizationinvitation
from ..shared import security as shared_security
from dataclasses_json import Undefined, dataclass_json
from sdk import utils
from typing import Optional


@dataclasses.dataclass
class GetOrganizationsOrgUUIDInvitationsUUIDSecurity:
    oauth2: Optional[shared_security.SchemeOauth2] = dataclasses.field(default=None, metadata={'security': { 'scheme': True, 'type': 'oauth2' }})
    personal_access_token: Optional[shared_security.SchemePersonalAccessToken] = dataclasses.field(default=None, metadata={'security': { 'scheme': True, 'type': 'http', 'sub_type': 'bearer' }})
    

@dataclasses.dataclass
class GetOrganizationsOrgUUIDInvitationsUUIDPathParams:
    org_uuid: str = dataclasses.field(metadata={'path_param': { 'field_name': 'org_uuid', 'style': 'simple', 'explode': False }})
    uuid: str = dataclasses.field(metadata={'path_param': { 'field_name': 'uuid', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class GetOrganizationsOrgUUIDInvitationsUUIDRequest:
    path_params: GetOrganizationsOrgUUIDInvitationsUUIDPathParams = dataclasses.field()
    security: GetOrganizationsOrgUUIDInvitationsUUIDSecurity = dataclasses.field()
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetOrganizationsOrgUUIDInvitationsUUIDErrorResponseDetails:
    message: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message') }})
    parameter: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('parameter'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetOrganizationsOrgUUIDInvitationsUUIDErrorResponse:
    r"""GetOrganizationsOrgUUIDInvitationsUUIDErrorResponse
    Error Object
    """
    
    message: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message') }})
    title: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('title') }})
    details: Optional[list[GetOrganizationsOrgUUIDInvitationsUUIDErrorResponseDetails]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('details'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetOrganizationsOrgUUIDInvitationsUUID200ApplicationJSON:
    resource: shared_organizationinvitation.OrganizationInvitation = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('resource') }})
    

@dataclasses.dataclass
class GetOrganizationsOrgUUIDInvitationsUUIDResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    error_response: Optional[GetOrganizationsOrgUUIDInvitationsUUIDErrorResponse] = dataclasses.field(default=None)
    get_organizations_org_uuid_invitations_uuid_200_application_json_object: Optional[GetOrganizationsOrgUUIDInvitationsUUID200ApplicationJSON] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    