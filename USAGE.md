<!-- Start SDK Example Usage -->
```python
import sdk
from sdk.models import operations, shared

s = sdk.SDK(
    security=shared.Security(
        oauth2="Bearer YOUR_ACCESS_TOKEN_HERE",
    ),
)


req = operations.ActivityLogRequest(
    action=[
        "provident",
        "distinctio",
        "quibusdam",
    ],
    actor=[
        "https://api.calendly.com/users/EBHAAFHDCAEQTSEZ",
        "https://api.calendly.com/users/EBHAAFHDCAEQTSEZ",
        "https://api.calendly.com/users/EBHAAFHDCAEQTSEZ",
    ],
    count=857946,
    max_occurred_at="2021-04-22T12:08:58.275Z",
    min_occurred_at="2022-05-18T09:34:54.894Z",
    namespace=[
        "suscipit",
        "iure",
        "magnam",
    ],
    organization="https://api.calendly.com/organizations/EBHAAFHDCAEQTSEZ",
    page_token="debitis",
    search_term="ipsa",
    sort=[
        "actor.display_name:asc",
        "actor.display_name:desc",
        "actor.uri:asc",
        "namespace:desc",
    ],
)
    
res = s.activity_log.activity_log(req)

if res.activity_log_200_application_json_object is not None:
    # handle response
```
<!-- End SDK Example Usage -->