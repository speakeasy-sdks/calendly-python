import requests as requests_http
from . import utils
from sdk.models import operations
from typing import Optional

class EventTypes:
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
        
    def get_event_types_uuid(self, request: operations.GetEventTypesUUIDRequest) -> operations.GetEventTypesUUIDResponse:
        r"""Get Event Type
        Returns information about a specified Event Type.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, '/event_types/{uuid}', request.path_params)
        
        
        client = self._security_client
        
        http_res = client.request('GET', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetEventTypesUUIDResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetEventTypesUUID200ApplicationJSON])
                res.get_event_types_uuid_200_application_json_object = out
        elif http_res.status_code == 400:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetEventTypesUUIDErrorResponse])
                res.error_response = out
        elif http_res.status_code == 401:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetEventTypesUUIDErrorResponse])
                res.error_response = out
        elif http_res.status_code == 403:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetEventTypesUUIDErrorResponse])
                res.error_response = out
        elif http_res.status_code == 404:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetEventTypesUUIDErrorResponse])
                res.error_response = out
        elif http_res.status_code == 500:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetEventTypesUUIDErrorResponse])
                res.error_response = out

        return res

    def get_event_type_available_times(self, request: operations.GetEventTypeAvailableTimesRequest) -> operations.GetEventTypeAvailableTimesResponse:
        r"""List Event Type Available Times
        Returns a list of available times for an event type within a specified date range.
        
        Date range can be no greater than 1 week (7 days).
        
        **NOTE:**
        * This endpoint does not support traditional keyset pagination.
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/event_type_available_times'
        
        query_params = utils.get_query_params(request.query_params)
        
        client = self._security_client
        
        http_res = client.request('GET', url, params=query_params)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetEventTypeAvailableTimesResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetEventTypeAvailableTimes200ApplicationJSON])
                res.get_event_type_available_times_200_application_json_object = out
        elif http_res.status_code == 400:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetEventTypeAvailableTimesErrorResponse])
                res.error_response = out
        elif http_res.status_code == 401:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetEventTypeAvailableTimesErrorResponse])
                res.error_response = out
        elif http_res.status_code == 403:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetEventTypeAvailableTimesErrorResponse])
                res.error_response = out
        elif http_res.status_code == 404:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetEventTypeAvailableTimesErrorResponse])
                res.error_response = out
        elif http_res.status_code == 500:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetEventTypeAvailableTimesErrorResponse])
                res.error_response = out

        return res

    def get_event_types(self, request: operations.GetEventTypesRequest) -> operations.GetEventTypesResponse:
        r"""List User's Event Types
        Returns all Event Types associated with a specified User. Use:
        
        * `organization` to look up all Event Types that belong to the organization
        
        * `user` to look up a user's Event Types in an organization
        
        Either `organization` or `user` are required query params when using this endpoint.
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/event_types'
        
        query_params = utils.get_query_params(request.query_params)
        
        client = self._security_client
        
        http_res = client.request('GET', url, params=query_params)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetEventTypesResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetEventTypes200ApplicationJSON])
                res.get_event_types_200_application_json_object = out
        elif http_res.status_code == 400:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetEventTypesErrorResponse])
                res.error_response = out
        elif http_res.status_code == 401:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetEventTypesErrorResponse])
                res.error_response = out
        elif http_res.status_code == 403:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetEventTypes403ApplicationJSON])
                res.get_event_types_403_application_json_object = out
        elif http_res.status_code == 404:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetEventTypesErrorResponse])
                res.error_response = out
        elif http_res.status_code == 500:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetEventTypesErrorResponse])
                res.error_response = out

        return res

    