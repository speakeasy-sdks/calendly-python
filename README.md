# calendly

<!-- Start SDK Installation -->
## SDK Installation

```bash
pip install calendly
```
<!-- End SDK Installation -->

## SDK Example Usage
<!-- Start SDK Example Usage -->
```python
import sdk
from sdk.models import operations, shared

s = sdk.SDK(
    security=shared.Security(
        oauth2=shared.SchemeOauth2(
            authorization="Bearer YOUR_ACCESS_TOKEN_HERE",
        ),
    ),
)

   
req = operations.ActivityLogRequest(
    query_params=operations.ActivityLogQueryParams(
        action=[
            "deserunt",
            "porro",
            "nulla",
        ],
        actor=[
            "vero",
            "perspiciatis",
            "nulla",
        ],
        count=423655,
        max_occurred_at="2022-08-01T10:44:41.925Z",
        min_occurred_at="2022-07-24T07:07:49.863Z",
        namespace=[
            "iusto",
            "ullam",
        ],
        organization="saepe",
        page_token="inventore",
        search_term="sapiente",
        sort=[
            "actor.display_name:desc",
            "actor.uri:asc",
        ],
    ),
)
    
res = s.activity_log.activity_log(req)

if res.activity_log_200_application_json_object is not None:
    # handle response
```
<!-- End SDK Example Usage -->

<!-- Start SDK Available Operations -->
## SDK Available Operations


### activity_log

* `activity_log` - List activity log entries

### availability

* `get_user_availability_schedules` - List User Availability Schedules
* `get_user_availability_schedules_uuid` - Get User Availability Schedule
* `get_user_busy_times` - List User Busy Times

### data_compliance

* `post_data_compliance_deletion_events` - Delete Scheduled Event Data
* `post_data_compliance_deletion_invitees` - Delete Invitee Data

### event_types

* `get_event_types_uuid` - Get Event Type
* `get_event_type_available_times` - List Event Type Available Times
* `get_event_types` - List User's Event Types

### organizations

* `delete_organizations_uuid_memberships` - Remove User from Organization
* `get_organization_memberships` - List Organization Memberships
* `get_organizations_org_uuid_invitations_uuid` - Get Organization Invitation
* `get_organizations_uuid_invitations` - List Organization Invitations
* `get_organizations_uuid_memberships` - Get Organization Membership
* `post_organizations_uuid_invitations` - Invite User to Organization
* `revoke_users_organization_invitation` - Revoke User's Organization Invitation

### routing_forms

* `get_routing_form_submissions` - List Routing Form Submissions
* `get_routing_form_submissions_uuid` - Get Routing Form Submission
* `get_routing_forms` - List Routing Forms
* `get_routing_forms_uuid` - Get Routing Form

### scheduled_events

* `delete_invitee_no_show` - Delete Invitee No Show
* `get_scheduled_events_event_uuid_invitees_invitee_uuid` - Get Event Invitee
* `get_scheduled_events_uuid` - Get Event
* `get_invitee_no_show` - Get Invitee No Show
* `get_invitees` - List Event Invitees
* `get_scheduled_events` - List Events
* `post_scheduled_events_uuid_cancellation_json` - Cancel Event
* `post_scheduled_events_uuid_cancellation_multipart` - Cancel Event
* `post_scheduled_events_uuid_cancellation_raw` - Cancel Event
* `post_invitee_no_show` - Create Invitee No Show

### scheduling_links

* `post_scheduling_links` - Create Single-Use Scheduling Link

### shares

* `post_shares` - Create Share

### users

* `get_my_user_account` - Get current user
* `get_user` - Get user

### webhooks

* `delete_users_user_uuid_webhooks_webhook_uuid` - Delete Webhook Subscription
* `get_users_user_uuid_webhooks_webhook_uuid` - Get Webhook Subscription
* `get_webhooks` - List Webhook Subscriptions
* `post_users_uuid_webhooks` - Create Webhook Subscription
<!-- End SDK Available Operations -->

### SDK Generated by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)
