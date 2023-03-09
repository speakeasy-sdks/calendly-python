from __future__ import annotations
import dataclasses


@dataclasses.dataclass
class SchemeOauth2:
    authorization: str = dataclasses.field(metadata={'security': { 'field_name': 'Authorization' }})
    

@dataclasses.dataclass
class SchemePersonalAccessToken:
    authorization: str = dataclasses.field(metadata={'security': { 'field_name': 'Authorization' }})
    