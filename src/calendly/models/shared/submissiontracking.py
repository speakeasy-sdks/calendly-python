"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from calendly import utils
from dataclasses_json import Undefined, dataclass_json


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SubmissionTracking:
    r"""The UTM and Salesforce tracking parameters associated with a Routing Form Submission."""
    
    salesforce_uuid: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('salesforce_uuid') }})
    r"""The Salesforce record unique identifier."""  
    utm_campaign: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('utm_campaign') }})
    r"""The UTM parameter used to track a campaign."""  
    utm_content: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('utm_content') }})
    r"""UTM content tracking parameter."""  
    utm_medium: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('utm_medium') }})
    r"""The UTM parameter that identifies the type of input (e.g. Cost Per Click (CPC), social media, affiliate or QR code)."""  
    utm_source: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('utm_source') }})
    r"""The UTM parameter that identifies the source (platform where the traffic originates)."""  
    utm_term: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('utm_term') }})
    r"""The UTM parameter used to track keywords."""  
    