"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import pagination as shared_pagination
from ..shared import routingformsubmission as shared_routingformsubmission
from calendly import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Optional


@dataclasses.dataclass
class GetRoutingFormSubmissionsRequest:
    
    form: str = dataclasses.field(metadata={'query_param': { 'field_name': 'form', 'style': 'form', 'explode': True }})
    r"""View routing form submissions associated with the routing form's URI."""  
    count: Optional[float] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'count', 'style': 'form', 'explode': True }})
    r"""The number of rows to return"""  
    page_token: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'page_token', 'style': 'form', 'explode': True }})
    r"""The token to pass to get the next or previous portion of the collection"""  
    sort: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'sort', 'style': 'form', 'explode': True }})
    r"""Order results by the specified field and direction. Accepts comma-separated list of {field}:{direction} values. Supported fields are: created_at. Sort direction is specified as: asc, desc."""  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetRoutingFormSubmissionsErrorResponseDetails:
    
    message: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message') }})  
    parameter: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('parameter'), 'exclude': lambda f: f is None }})  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetRoutingFormSubmissionsErrorResponse:
    r"""Error Object"""
    
    message: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message') }})  
    title: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('title') }})  
    details: Optional[list[GetRoutingFormSubmissionsErrorResponseDetails]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('details'), 'exclude': lambda f: f is None }})  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetRoutingFormSubmissions200ApplicationJSON:
    r"""OK"""
    
    collection: list[shared_routingformsubmission.RoutingFormSubmission] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('collection') }})  
    pagination: shared_pagination.Pagination = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pagination') }})  
    

@dataclasses.dataclass
class GetRoutingFormSubmissionsResponse:
    
    content_type: str = dataclasses.field()  
    status_code: int = dataclasses.field()  
    error_response: Optional[GetRoutingFormSubmissionsErrorResponse] = dataclasses.field(default=None)
    r"""Request is not valid"""  
    get_routing_form_submissions_200_application_json_object: Optional[GetRoutingFormSubmissions200ApplicationJSON] = dataclasses.field(default=None)
    r"""OK"""  
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)  
    