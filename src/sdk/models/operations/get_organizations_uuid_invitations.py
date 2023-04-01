"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import organizationinvitation as shared_organizationinvitation
from ..shared import pagination as shared_pagination
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from sdk import utils
from typing import Optional

class GetOrganizationsUUIDInvitationsStatusEnum(str, Enum):
    r"""Indicates if the results should be filtered by status  (\\"pending\\", \\"accepted\\", or \\"declined\\")"""
    PENDING = 'pending'
    ACCEPTED = 'accepted'
    DECLINED = 'declined'


@dataclasses.dataclass
class GetOrganizationsUUIDInvitationsRequest:
    
    uuid: str = dataclasses.field(metadata={'path_param': { 'field_name': 'uuid', 'style': 'simple', 'explode': False }})
    r"""The organization's unique identifier"""  
    count: Optional[float] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'count', 'style': 'form', 'explode': True }})
    r"""The number of rows to return"""  
    email: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'email', 'style': 'form', 'explode': True }})
    r"""Indicates if the results should be filtered by email address"""  
    page_token: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'page_token', 'style': 'form', 'explode': True }})
    r"""The token to pass to get the next or previous portion of the collection"""  
    sort: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'sort', 'style': 'form', 'explode': True }})
    r"""Order results by the field name and direction specified (ascending or descending). Returns multiple sets of results in a comma-separated list."""  
    status: Optional[GetOrganizationsUUIDInvitationsStatusEnum] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'status', 'style': 'form', 'explode': True }})
    r"""Indicates if the results should be filtered by status  (\\"pending\\", \\"accepted\\", or \\"declined\\")"""  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetOrganizationsUUIDInvitationsErrorResponseDetails:
    
    message: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message') }})  
    parameter: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('parameter'), 'exclude': lambda f: f is None }})  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetOrganizationsUUIDInvitationsErrorResponse:
    r"""Error Object"""
    
    message: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message') }})  
    title: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('title') }})  
    details: Optional[list[GetOrganizationsUUIDInvitationsErrorResponseDetails]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('details'), 'exclude': lambda f: f is None }})  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetOrganizationsUUIDInvitations200ApplicationJSON:
    r"""OK"""
    
    collection: list[shared_organizationinvitation.OrganizationInvitation] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('collection') }})  
    pagination: shared_pagination.Pagination = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pagination') }})  
    

@dataclasses.dataclass
class GetOrganizationsUUIDInvitationsResponse:
    
    content_type: str = dataclasses.field()  
    status_code: int = dataclasses.field()  
    error_response: Optional[GetOrganizationsUUIDInvitationsErrorResponse] = dataclasses.field(default=None)
    r"""Request is not valid"""  
    get_organizations_uuid_invitations_200_application_json_object: Optional[GetOrganizationsUUIDInvitations200ApplicationJSON] = dataclasses.field(default=None)
    r"""OK"""  
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)  
    