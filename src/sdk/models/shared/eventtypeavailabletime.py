"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from marshmallow import fields
from sdk import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class EventTypeAvailableTime:
    r"""An available meeting time slot for the given event type"""
    
    invitees_remaining: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('invitees_remaining') }})
    r"""Total remaining invitees for this available time. For Group Event Type, more than one invitee can book in this available time. For all other Event Types, only one invitee can book in this available time."""  
    scheduling_url: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('scheduling_url') }})
    r"""The URL of the user’s scheduling site where invitees book this event type"""  
    start_time: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_time'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    r"""The moment the event was scheduled to start in UTC time"""  
    status: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    r"""Indicates that the open time slot is \"available\""""  
    