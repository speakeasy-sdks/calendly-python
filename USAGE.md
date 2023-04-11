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