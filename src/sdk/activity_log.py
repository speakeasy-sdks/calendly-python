"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

import requests as requests_http
from . import utils
from sdk.models import operations
from typing import Optional

class ActivityLog:
    _client: requests_http.Session
    _security_client: requests_http.Session
    _server_url: str
    _language: str
    _sdk_version: str
    _gen_version: str

    def __init__(self, client: requests_http.Session, security_client: requests_http.Session, server_url: str, language: str, sdk_version: str, gen_version: str) -> None:
        self._client = client
        self._security_client = security_client
        self._server_url = server_url
        self._language = language
        self._sdk_version = sdk_version
        self._gen_version = gen_version
        
    def list_activity_log(self, request: operations.ListActivityLogRequest) -> operations.ListActivityLogResponse:
        r"""List activity log entries
        <!-- theme: info -->
          > This endpoint requires an <strong>Enterprise</strong> subscription.
        
        Returns a list of activity log entries
        """
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/activity_log_entries'
        
        query_params = utils.get_query_params(operations.ListActivityLogRequest, request)
        
        client = self._security_client
        
        http_res = client.request('GET', url, params=query_params)
        content_type = http_res.headers.get('Content-Type')

        res = operations.ListActivityLogResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.ListActivityLog200ApplicationJSON])
                res.list_activity_log_200_application_json_object = out
        elif http_res.status_code in [400, 404, 500]:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.ListActivityLogErrorResponse])
                res.error_response = out
        elif http_res.status_code == 403:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.ListActivityLog403ApplicationJSON])
                res.list_activity_log_403_application_json_object = out

        return res

    