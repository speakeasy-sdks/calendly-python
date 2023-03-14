from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from sdk import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Pagination:
    count: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('count') }})
    next_page: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('next_page') }})
    next_page_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('next_page_token') }})
    previous_page: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('previous_page') }})
    previous_page_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('previous_page_token') }})
    