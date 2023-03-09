import requests as requests_http
from . import utils
from sdk.models import operations, shared
from typing import Optional

class ScheduledEvents:
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
        
    def delete_invitee_no_show(self, request: operations.DeleteInviteeNoShowRequest) -> operations.DeleteInviteeNoShowResponse:
        r"""Delete Invitee No Show
        Undoes marking an Invitee as a No Show.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, '/invitee_no_shows/{uuid}', request.path_params)
        
        
        client = utils.configure_security_client(self._client, request.security)
        
        http_res = client.request('DELETE', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.DeleteInviteeNoShowResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 204:
            pass
        elif http_res.status_code == 401:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.DeleteInviteeNoShowErrorResponse])
                res.error_response = out
        elif http_res.status_code == 403:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.DeleteInviteeNoShowErrorResponse])
                res.error_response = out
        elif http_res.status_code == 404:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.DeleteInviteeNoShowErrorResponse])
                res.error_response = out
        elif http_res.status_code == 500:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.DeleteInviteeNoShowErrorResponse])
                res.error_response = out

        return res

    def get_scheduled_events_event_uuid_invitees_invitee_uuid(self, request: operations.GetScheduledEventsEventUUIDInviteesInviteeUUIDRequest) -> operations.GetScheduledEventsEventUUIDInviteesInviteeUUIDResponse:
        r"""Get Event Invitee
        Returns information about a specified Invitee (person invited to an event).
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, '/scheduled_events/{event_uuid}/invitees/{invitee_uuid}', request.path_params)
        
        
        client = utils.configure_security_client(self._client, request.security)
        
        http_res = client.request('GET', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetScheduledEventsEventUUIDInviteesInviteeUUIDResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetScheduledEventsEventUUIDInviteesInviteeUUID200ApplicationJSON])
                res.get_scheduled_events_event_uuid_invitees_invitee_uuid_200_application_json_object = out
        elif http_res.status_code == 400:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetScheduledEventsEventUUIDInviteesInviteeUUIDErrorResponse])
                res.error_response = out
        elif http_res.status_code == 401:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetScheduledEventsEventUUIDInviteesInviteeUUIDErrorResponse])
                res.error_response = out
        elif http_res.status_code == 403:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ErrorResponse])
                res.error_response1 = out
        elif http_res.status_code == 404:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetScheduledEventsEventUUIDInviteesInviteeUUIDErrorResponse])
                res.error_response = out
        elif http_res.status_code == 500:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetScheduledEventsEventUUIDInviteesInviteeUUIDErrorResponse])
                res.error_response = out

        return res

    def get_scheduled_events_uuid(self, request: operations.GetScheduledEventsUUIDRequest) -> operations.GetScheduledEventsUUIDResponse:
        r"""Get Event
        Returns information about a specified Event.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, '/scheduled_events/{uuid}', request.path_params)
        
        
        client = utils.configure_security_client(self._client, request.security)
        
        http_res = client.request('GET', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetScheduledEventsUUIDResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetScheduledEventsUUID200ApplicationJSON])
                res.get_scheduled_events_uuid_200_application_json_object = out
        elif http_res.status_code == 401:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetScheduledEventsUUIDErrorResponse])
                res.error_response = out
        elif http_res.status_code == 403:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetScheduledEventsUUID403ApplicationJSON])
                res.get_scheduled_events_uuid_403_application_json_object = out
        elif http_res.status_code == 404:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetScheduledEventsUUIDErrorResponse])
                res.error_response = out
        elif http_res.status_code == 500:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetScheduledEventsUUIDErrorResponse])
                res.error_response = out

        return res

    def get_invitee_no_show(self, request: operations.GetInviteeNoShowRequest) -> operations.GetInviteeNoShowResponse:
        r"""Get Invitee No Show
        Returns information about a specified Invitee No Show.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, '/invitee_no_shows/{uuid}', request.path_params)
        
        
        client = utils.configure_security_client(self._client, request.security)
        
        http_res = client.request('GET', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetInviteeNoShowResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetInviteeNoShow200ApplicationJSON])
                res.get_invitee_no_show_200_application_json_object = out
        elif http_res.status_code == 400:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetInviteeNoShowErrorResponse])
                res.error_response = out
        elif http_res.status_code == 401:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetInviteeNoShowErrorResponse])
                res.error_response = out
        elif http_res.status_code == 403:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetInviteeNoShowErrorResponse])
                res.error_response = out
        elif http_res.status_code == 404:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetInviteeNoShowErrorResponse])
                res.error_response = out

        return res

    def get_invitees(self, request: operations.GetInviteesRequest) -> operations.GetInviteesResponse:
        r"""List Event Invitees
        Returns a list of Invitees for an event.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, '/scheduled_events/{uuid}/invitees', request.path_params)
        
        query_params = utils.get_query_params(request.query_params)
        
        client = utils.configure_security_client(self._client, request.security)
        
        http_res = client.request('GET', url, params=query_params)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetInviteesResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetInvitees200ApplicationJSON])
                res.get_invitees_200_application_json_object = out
        elif http_res.status_code == 400:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetInviteesErrorResponse])
                res.error_response = out
        elif http_res.status_code == 401:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetInviteesErrorResponse])
                res.error_response = out
        elif http_res.status_code == 403:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetInvitees403ApplicationJSON])
                res.get_invitees_403_application_json_object = out
        elif http_res.status_code == 404:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetInviteesErrorResponse])
                res.error_response = out
        elif http_res.status_code == 500:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetInviteesErrorResponse])
                res.error_response = out

        return res

    def get_scheduled_events(self, request: operations.GetScheduledEventsRequest) -> operations.GetScheduledEventsResponse:
        r"""List Events
        Returns a list of  Events.
        
        * Pass `organization` parameter to return events for that organization (requires admin/owner privilege)
        * Pass `user` parameter to return events for a specific User
        
        **NOTES:**
        * If you are the admin/owner of the organization, you can use both `organization` and `user` to get a list of events for a specific user within your organization.
        
        * `user` can only be used alone when requesting your own personal events. This will return your events within any organization that you are currently in or were a part of in the past.
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/scheduled_events'
        
        query_params = utils.get_query_params(request.query_params)
        
        client = utils.configure_security_client(self._client, request.security)
        
        http_res = client.request('GET', url, params=query_params)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetScheduledEventsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetScheduledEvents200ApplicationJSON])
                res.get_scheduled_events_200_application_json_object = out
        elif http_res.status_code == 400:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetScheduledEventsErrorResponse])
                res.error_response = out
        elif http_res.status_code == 401:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetScheduledEventsErrorResponse])
                res.error_response = out
        elif http_res.status_code == 403:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetScheduledEvents403ApplicationJSON])
                res.get_scheduled_events_403_application_json_object = out
        elif http_res.status_code == 404:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetScheduledEventsErrorResponse])
                res.error_response = out
        elif http_res.status_code == 500:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetScheduledEventsErrorResponse])
                res.error_response = out

        return res

    def post_scheduled_events_uuid_cancellation_json(self, request: operations.PostScheduledEventsUUIDCancellationJSONRequest) -> operations.PostScheduledEventsUUIDCancellationJSONResponse:
        r"""Cancel Event
        Cancels specified event.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, '/scheduled_events/{uuid}/cancellation', request.path_params)
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request)
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        
        client = utils.configure_security_client(self._client, request.security)
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.PostScheduledEventsUUIDCancellationJSONResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 201:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.PostScheduledEventsUUIDCancellationJSON201ApplicationJSON])
                res.post_scheduled_events_uuid_cancellation_json_201_application_json_object = out
        elif http_res.status_code == 400:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.PostScheduledEventsUUIDCancellationJSONErrorResponse])
                res.error_response = out
        elif http_res.status_code == 401:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.PostScheduledEventsUUIDCancellationJSONErrorResponse])
                res.error_response = out
        elif http_res.status_code == 403:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.PostScheduledEventsUUIDCancellationJSON403ApplicationJSON])
                res.post_scheduled_events_uuid_cancellation_json_403_application_json_object = out
        elif http_res.status_code == 404:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.PostScheduledEventsUUIDCancellationJSONErrorResponse])
                res.error_response = out
        elif http_res.status_code == 500:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.PostScheduledEventsUUIDCancellationJSONErrorResponse])
                res.error_response = out

        return res

    def post_scheduled_events_uuid_cancellation_multipart(self, request: operations.PostScheduledEventsUUIDCancellationMultipartRequest) -> operations.PostScheduledEventsUUIDCancellationMultipartResponse:
        r"""Cancel Event
        Cancels specified event.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, '/scheduled_events/{uuid}/cancellation', request.path_params)
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request)
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        
        client = utils.configure_security_client(self._client, request.security)
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.PostScheduledEventsUUIDCancellationMultipartResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 201:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.PostScheduledEventsUUIDCancellationMultipart201ApplicationJSON])
                res.post_scheduled_events_uuid_cancellation_multipart_201_application_json_object = out
        elif http_res.status_code == 400:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.PostScheduledEventsUUIDCancellationMultipartErrorResponse])
                res.error_response = out
        elif http_res.status_code == 401:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.PostScheduledEventsUUIDCancellationMultipartErrorResponse])
                res.error_response = out
        elif http_res.status_code == 403:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.PostScheduledEventsUUIDCancellationMultipart403ApplicationJSON])
                res.post_scheduled_events_uuid_cancellation_multipart_403_application_json_object = out
        elif http_res.status_code == 404:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.PostScheduledEventsUUIDCancellationMultipartErrorResponse])
                res.error_response = out
        elif http_res.status_code == 500:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.PostScheduledEventsUUIDCancellationMultipartErrorResponse])
                res.error_response = out

        return res

    def post_scheduled_events_uuid_cancellation_raw(self, request: operations.PostScheduledEventsUUIDCancellationRawRequest) -> operations.PostScheduledEventsUUIDCancellationRawResponse:
        r"""Cancel Event
        Cancels specified event.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, '/scheduled_events/{uuid}/cancellation', request.path_params)
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request)
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        
        client = utils.configure_security_client(self._client, request.security)
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.PostScheduledEventsUUIDCancellationRawResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 201:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.PostScheduledEventsUUIDCancellationRaw201ApplicationJSON])
                res.post_scheduled_events_uuid_cancellation_raw_201_application_json_object = out
        elif http_res.status_code == 400:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.PostScheduledEventsUUIDCancellationRawErrorResponse])
                res.error_response = out
        elif http_res.status_code == 401:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.PostScheduledEventsUUIDCancellationRawErrorResponse])
                res.error_response = out
        elif http_res.status_code == 403:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.PostScheduledEventsUUIDCancellationRaw403ApplicationJSON])
                res.post_scheduled_events_uuid_cancellation_raw_403_application_json_object = out
        elif http_res.status_code == 404:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.PostScheduledEventsUUIDCancellationRawErrorResponse])
                res.error_response = out
        elif http_res.status_code == 500:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.PostScheduledEventsUUIDCancellationRawErrorResponse])
                res.error_response = out

        return res

    def post_invitee_no_show(self, request: operations.PostInviteeNoShowRequest) -> operations.PostInviteeNoShowResponse:
        r"""Create Invitee No Show
        Marks an Invitee as a No Show.
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/invitee_no_shows'
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request)
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        
        client = utils.configure_security_client(self._client, request.security)
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.PostInviteeNoShowResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 201:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.PostInviteeNoShow201ApplicationJSON])
                res.post_invitee_no_show_201_application_json_object = out
        elif http_res.status_code == 400:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.PostInviteeNoShowErrorResponse])
                res.error_response = out
        elif http_res.status_code == 401:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.PostInviteeNoShowErrorResponse])
                res.error_response = out
        elif http_res.status_code == 403:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.PostInviteeNoShowErrorResponse])
                res.error_response = out
        elif http_res.status_code == 404:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.PostInviteeNoShowErrorResponse])
                res.error_response = out
        elif http_res.status_code == 500:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.PostInviteeNoShowErrorResponse])
                res.error_response = out

        return res

    