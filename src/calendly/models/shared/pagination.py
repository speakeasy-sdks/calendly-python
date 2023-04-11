"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from calendly import utils
from dataclasses_json import Undefined, dataclass_json


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Pagination:
    
    count: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('count') }})
    r"""The number of rows to return"""  
    next_page: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('next_page') }})
    r"""URI to return the next page of an ordered list (\\"null\\" indicates no additional results are available)"""  
    next_page_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('next_page_token') }})
    r"""Token to return the next page of an ordered list (\\"null\\" indicates no additional results are available)"""  
    previous_page: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('previous_page') }})
    r"""URI to return the previous page of an ordered list (\\"null\\" indicates no additional results are available)"""  
    previous_page_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('previous_page_token') }})
    r"""Token to return the previous page of an ordered list (\\"null\\" indicates no additional results are available)"""  
    