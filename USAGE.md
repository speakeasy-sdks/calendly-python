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
            "https://api.calendly.com/users/EBHAAFHDCAEQTSEZ",
            "https://api.calendly.com/users/EBHAAFHDCAEQTSEZ",
            "https://api.calendly.com/users/EBHAAFHDCAEQTSEZ",
        ],
        count=857946,
        max_occurred_at="2022-09-05T03:55:37.924Z",
        min_occurred_at="2022-05-17T19:10:43.322Z",
        namespace=[
            "fuga",
            "facilis",
        ],
        organization="https://api.calendly.com/organizations/EBHAAFHDCAEQTSEZ",
        page_token="eum",
        search_term="iusto",
        sort=[
            "occurred_at:asc",
            "action:asc",
        ],
    ),
)
    
res = s.activity_log.activity_log(req)

if res.activity_log_200_application_json_object is not None:
    # handle response
```
<!-- End SDK Example Usage -->