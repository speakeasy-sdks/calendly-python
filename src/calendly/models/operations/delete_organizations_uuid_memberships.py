"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import errorresponse as shared_errorresponse
from calendly import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Optional


@dataclasses.dataclass
class DeleteOrganizationsUUIDMembershipsRequest:
    
    uuid: str = dataclasses.field(metadata={'path_param': { 'field_name': 'uuid', 'style': 'simple', 'explode': False }})
    r"""The organization membership's unique identifier"""  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DeleteOrganizationsUUIDMembershipsErrorResponseDetails:
    
    message: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message') }})  
    parameter: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('parameter'), 'exclude': lambda f: f is None }})  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DeleteOrganizationsUUIDMembershipsErrorResponse:
    r"""Error Object"""
    
    message: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message') }})  
    title: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('title') }})  
    details: Optional[list[DeleteOrganizationsUUIDMembershipsErrorResponseDetails]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('details'), 'exclude': lambda f: f is None }})  
    

@dataclasses.dataclass
class DeleteOrganizationsUUIDMembershipsResponse:
    
    content_type: str = dataclasses.field()  
    status_code: int = dataclasses.field()  
    error_response: Optional[DeleteOrganizationsUUIDMembershipsErrorResponse] = dataclasses.field(default=None)
    r"""Request is not valid"""  
    error_response1: Optional[shared_errorresponse.ErrorResponse] = dataclasses.field(default=None)
    r"""Caller not authorized to perform this action"""  
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)  
    