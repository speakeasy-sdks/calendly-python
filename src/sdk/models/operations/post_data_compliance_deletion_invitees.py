from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import errorresponse as shared_errorresponse
from dataclasses_json import Undefined, dataclass_json
from sdk import utils
from typing import Any, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostDataComplianceDeletionInviteesRequestBody:
    emails: list[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('emails') }})
    

@dataclasses.dataclass
class PostDataComplianceDeletionInviteesRequest:
    request: PostDataComplianceDeletionInviteesRequestBody = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostDataComplianceDeletionInviteesErrorResponseDetails:
    message: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message') }})
    parameter: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('parameter'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostDataComplianceDeletionInviteesErrorResponse:
    r"""PostDataComplianceDeletionInviteesErrorResponse
    Error Object
    """
    
    message: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message') }})
    title: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('title') }})
    details: Optional[list[PostDataComplianceDeletionInviteesErrorResponseDetails]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('details'), 'exclude': lambda f: f is None }})
    

@dataclasses.dataclass
class PostDataComplianceDeletionInviteesResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    error_response: Optional[PostDataComplianceDeletionInviteesErrorResponse] = dataclasses.field(default=None)
    error_response1: Optional[shared_errorresponse.ErrorResponse] = dataclasses.field(default=None)
    post_data_compliance_deletion_invitees_202_application_json_object: Optional[dict[str, Any]] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    