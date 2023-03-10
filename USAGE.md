<!-- Start SDK Example Usage -->
```python
import sdk
from sdk.models import operations, shared

s = sdk.SDK()
s.config_security(
    security=shared.Security(
        oauth2=shared.SchemeOauth2(
            authorization="Bearer YOUR_ACCESS_TOKEN_HERE",
        ),
    )
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
        max_occurred_at="2022-07-25T10:50:39.948Z",
        min_occurred_at="2022-07-17T07:13:47.886Z",
        namespace=[
            "iusto",
            "ullam",
        ],
        organization="saepe",
        page_token="inventore",
        search_term="sapiente",
        sort=[
            "actor.uri:asc",
            "actor.uri:desc",
        ],
    ),
)
    
res = s.activity_log.activity_log(req)

if res.activity_log_200_application_json_object is not None:
    # handle response
```
<!-- End SDK Example Usage -->