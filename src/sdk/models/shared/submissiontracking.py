from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from sdk import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SubmissionTracking:
    r"""SubmissionTracking
    The UTM and Salesforce tracking parameters associated with a Routing Form Submission.
    """
    
    salesforce_uuid: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('salesforce_uuid') }})
    utm_campaign: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('utm_campaign') }})
    utm_content: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('utm_content') }})
    utm_medium: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('utm_medium') }})
    utm_source: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('utm_source') }})
    utm_term: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('utm_term') }})
    