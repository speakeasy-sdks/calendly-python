<!-- Start SDK Example Usage -->
```python
import sdk
from sdk.models import operations, shared

s = sdk.SDK(
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
    
res = s.scheduled_events.list_scheduled_events(req)

if res.list_scheduled_events_200_application_json_object is not None:
    # handle response
```
<!-- End SDK Example Usage -->