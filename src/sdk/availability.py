import requests as requests_http
from . import utils
from sdk.models import operations, shared
from typing import Optional

class Availability:
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
        
    def get_user_availability_schedules(self, request: operations.GetUserAvailabilitySchedulesRequest) -> operations.GetUserAvailabilitySchedulesResponse:
        r"""List User Availability Schedules
        Returns the availability schedules of the given user.
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/user_availability_schedules'
        
        query_params = utils.get_query_params(request.query_params)
        
        client = utils.configure_security_client(self._client, request.security)
        
        http_res = client.request('GET', url, params=query_params)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetUserAvailabilitySchedulesResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetUserAvailabilitySchedules200ApplicationJSON])
                res.get_user_availability_schedules_200_application_json_object = out
        elif http_res.status_code == 400:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetUserAvailabilitySchedulesErrorResponse])
                res.error_response = out
        elif http_res.status_code == 401:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetUserAvailabilitySchedulesErrorResponse])
                res.error_response = out
        elif http_res.status_code == 403:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetUserAvailabilitySchedules403ApplicationJSON])
                res.get_user_availability_schedules_403_application_json_object = out
        elif http_res.status_code == 404:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetUserAvailabilitySchedulesErrorResponse])
                res.error_response = out
        elif http_res.status_code == 500:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetUserAvailabilitySchedulesErrorResponse])
                res.error_response = out

        return res

    def get_user_availability_schedules_uuid(self, request: operations.GetUserAvailabilitySchedulesUUIDRequest) -> operations.GetUserAvailabilitySchedulesUUIDResponse:
        r"""Get User Availability Schedule
        This will return the availability schedule of the given UUID.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, '/user_availability_schedules/{uuid}', request.path_params)
        
        
        client = utils.configure_security_client(self._client, request.security)
        
        http_res = client.request('GET', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetUserAvailabilitySchedulesUUIDResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetUserAvailabilitySchedulesUUID200ApplicationJSON])
                res.get_user_availability_schedules_uuid_200_application_json_object = out
        elif http_res.status_code == 400:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetUserAvailabilitySchedulesUUIDErrorResponse])
                res.error_response = out
        elif http_res.status_code == 401:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetUserAvailabilitySchedulesUUIDErrorResponse])
                res.error_response = out
        elif http_res.status_code == 403:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetUserAvailabilitySchedulesUUID403ApplicationJSON])
                res.get_user_availability_schedules_uuid_403_application_json_object = out
        elif http_res.status_code == 404:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetUserAvailabilitySchedulesUUIDErrorResponse])
                res.error_response = out
        elif http_res.status_code == 500:
            pass

        return res

    def get_user_busy_times(self, request: operations.GetUserBusyTimesRequest) -> operations.GetUserBusyTimesResponse:
        r"""List User Busy Times
        Returns an ascending list of user internal and external scheduled events within a specified date range.
        
        Date range can be no greater than 1 week (7 days).
        
        **NOTE:**
        * This endpoint does not support traditional keyset pagination.
        * External events will only be returned for calendars that have \"Check for conflicts\" configured.
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/user_busy_times'
        
        query_params = utils.get_query_params(request.query_params)
        
        client = utils.configure_security_client(self._client, request.security)
        
        http_res = client.request('GET', url, params=query_params)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetUserBusyTimesResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetUserBusyTimes200ApplicationJSON])
                res.get_user_busy_times_200_application_json_object = out
        elif http_res.status_code == 400:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetUserBusyTimesErrorResponse])
                res.error_response = out
        elif http_res.status_code == 401:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetUserBusyTimesErrorResponse])
                res.error_response = out
        elif http_res.status_code == 403:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetUserBusyTimes403ApplicationJSON])
                res.get_user_busy_times_403_application_json_object = out
        elif http_res.status_code == 404:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetUserBusyTimesErrorResponse])
                res.error_response = out
        elif http_res.status_code == 424:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ErrorResponse])
                res.error_response1 = out
        elif http_res.status_code == 500:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetUserBusyTimesErrorResponse])
                res.error_response = out

        return res

    