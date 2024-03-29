<div align="center">
    <img src="https://user-images.githubusercontent.com/6267663/231164258-4232466d-cacc-4ec7-9b30-8a8fe4f3073d.svg" width="500" />
    <h1>Python SDK</h1>
   <p>Integrate to save time and deliver insights</p>
   <a href="https://developer.calendly.com/api-docs/4b402d5ab3edd-calendly-developer"><img src="https://img.shields.io/static/v1?label=Docs&message=API Ref&color=5444e4&style=for-the-badge" /></a>
   <a href="https://github.com/speakeasy-sdks/calendly-python/actions"><img src="https://img.shields.io/github/actions/workflow/status/speakeasy-sdks/calendly-python/speakeasy_sdk_generation.yml?style=for-the-badge" /></a>
  <a href="https://opensource.org/licenses/MIT"><img src="https://img.shields.io/badge/License-MIT-blue.svg?style=for-the-badge" /></a>
  <a href="https://github.com/speakeasy-sdks/calendly-python/releases"><img src="https://img.shields.io/github/v/release/speakeasy-sdks/calendly-python?sort=semver&style=for-the-badge" /></a>
</div>

<!-- Start SDK Installation -->
## SDK Installation

```bash
pip install calendly-py
```
<!-- End SDK Installation -->

## SDK Example Usage
<!-- Start SDK Example Usage -->
```python
import calendly
from calendly.models import operations, shared

s = calendly.Calendly(
    security=shared.Security(
        oauth2="Bearer YOUR_ACCESS_TOKEN_HERE",
    ),
)


req = operations.ListScheduledEventsRequest(
    count=5488.14,
    invitee_email="alice@example.com",
    max_start_time="provident",
    min_start_time="distinctio",
    organization="https://api.calendly.com/organizations/EBHAAFHDCAEQTSEZ",
    page_token="quibusdam",
    sort="unde",
    status="canceled",
    user="https://api.calendly.com/users/EBHAAFHDCAEQTSEZ",
)
    
res = s.scheduled_events.list(req)

if res.scheduled_events_response is not None:
    # handle response
```
<!-- End SDK Example Usage -->

<!-- Start SDK Available Operations -->
## Available Resources and Operations


### activity_log

* `list` - List activity log entries

### availability

* `get` - Get User Availability Schedule
* `get_availability` - List User Availability Schedules
* `get_busy_times` - List User Busy Times

### data_compliance

* `create_deletion_event` - Delete Scheduled Event Data
* `delete_invitee_data` - Delete Invitee Data

### event_types

* `get` - Get Event Type
* `get_available_times` - List Event Type Available Times
* `list` - List User's Event Types

### organizations

* `delete_memberships` - Remove User from Organization
* `get_invitations` - Get Organization Invitation
* `invite_user` - Invite User to Organization
* `list_invitations` - List Organization Invitations
* `list_memberships` - List Organization Memberships
* `revoke_invite` - Revoke User's Organization Invitation

### routing_forms

* `get_submissions` - List Routing Form Submissions
* `get_submissions_by_uuid` - Get Routing Form Submission
* `get_by_uuid` - Get Routing Form
* `list` - List Routing Forms

### scheduled_events

* `cancel` - Cancel Event
* `create_no_show` - Create Invitee No Show
* `get_event_by_uuid` - Get Event
* `get_invitees` - List Event Invitees
* `get_invitees_by_uuid` - Get Event Invitee
* `get_no_show` - Get Invitee No Show
* `list` - List Events
* `unmark_no_show` - Delete Invitee No Show

### scheduling_links

* `create` - Create Single-Use Scheduling Link

### shares

* `create` - Create Share

### users

* `get` - Get user
* `get_memberships` - Get Organization Membership
* `me` - Get current user

### webhooks

* `create` - Create Webhook Subscription
* `delete` - Delete Webhook Subscription
* `get` - Get Webhook Subscription
* `list` - List Webhook Subscriptions
<!-- End SDK Available Operations -->

### SDK Generated by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)
