from __future__ import annotations
import dataclasses
import dateutil.parser
from ..shared import cancellation as shared_cancellation
from ..shared import inviteequestionandanswer as shared_inviteequestionandanswer
from ..shared import inviteetracking as shared_inviteetracking
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from enum import Enum
from marshmallow import fields
from sdk import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class InviteeNoShow1:
    r"""InviteeNoShow1
    Provides data pertaining to the associated no show for the Invitee
    """
    
    created_at: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('created_at'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    uri: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('uri') }})
    
class InviteePaymentCurrencyEnum(str, Enum):
    AUD = "AUD"
    CAD = "CAD"
    EUR = "EUR"
    GBP = "GBP"
    USD = "USD"

class InviteePaymentProviderEnum(str, Enum):
    STRIPE = "stripe"
    PAYPAL = "paypal"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class InviteePayment:
    r"""InviteePayment
    Invitee payment
    """
    
    amount: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('amount') }})
    currency: InviteePaymentCurrencyEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('currency') }})
    external_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('external_id') }})
    provider: InviteePaymentProviderEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('provider') }})
    successful: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('successful') }})
    terms: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('terms') }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class InviteeReconfirmation:
    r"""InviteeReconfirmation
    Assuming reconfirmation is enabled for the event type, when reconfirmation is requested this object is present with a `created_at` that reflects when the reconfirmation notification was sent. Once the invitee has reconfirmed the `confirmed_at` attribute will change from `null` to a timestamp that reflects when they took action.
    """
    
    confirmed_at: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('confirmed_at'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    created_at: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('created_at'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    
class InviteeStatusEnum(str, Enum):
    ACTIVE = "active"
    CANCELED = "canceled"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Invitee:
    r"""Invitee
    An individual who has been invited to meet with a Calendly member
    """
    
    cancel_url: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('cancel_url') }})
    created_at: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('created_at'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    email: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('email') }})
    event: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('event') }})
    first_name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('first_name') }})
    last_name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('last_name') }})
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    new_invitee: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('new_invitee') }})
    no_show: InviteeNoShow1 = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('no_show') }})
    old_invitee: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('old_invitee') }})
    payment: InviteePayment = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('payment') }})
    questions_and_answers: list[shared_inviteequestionandanswer.InviteeQuestionAndAnswer] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('questions_and_answers') }})
    reconfirmation: InviteeReconfirmation = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('reconfirmation') }})
    reschedule_url: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('reschedule_url') }})
    rescheduled: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('rescheduled') }})
    routing_form_submission: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('routing_form_submission') }})
    status: InviteeStatusEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    text_reminder_number: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('text_reminder_number') }})
    timezone: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('timezone') }})
    tracking: shared_inviteetracking.InviteeTracking = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tracking') }})
    updated_at: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('updated_at'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    uri: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('uri') }})
    cancellation: Optional[shared_cancellation.Cancellation] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('cancellation'), 'exclude': lambda f: f is None }})
    