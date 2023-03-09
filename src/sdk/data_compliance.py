import requests as requests_http
from . import utils
from sdk.models import operations, shared
from typing import Any, Optional

class DataCompliance:
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
        
    def post_data_compliance_deletion_events(self, request: operations.PostDataComplianceDeletionEventsRequest) -> operations.PostDataComplianceDeletionEventsResponse:
        r"""Delete Scheduled Event Data
        <!-- theme: info -->
          > This endpoint requires an <strong>Enterprise</strong> subscription.
        
        To submit a request to remove scheduled events data within a time range for your organization, use this endpoint. Requests for data deletion can take up to 7 days to complete.
        
        Time range can be no greater than 24 months and must occur in the past.
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/data_compliance/deletion/events'
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request)
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        
        client = utils.configure_security_client(self._client, request.security)
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.PostDataComplianceDeletionEventsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 202:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[dict[str, Any]])
                res.post_data_compliance_deletion_events_202_application_json_object = out
        elif http_res.status_code == 400:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.PostDataComplianceDeletionEventsErrorResponse])
                res.error_response = out
        elif http_res.status_code == 401:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.PostDataComplianceDeletionEventsErrorResponse])
                res.error_response = out
        elif http_res.status_code == 403:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ErrorResponse])
                res.error_response1 = out
        elif http_res.status_code == 404:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.PostDataComplianceDeletionEventsErrorResponse])
                res.error_response = out
        elif http_res.status_code == 500:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.PostDataComplianceDeletionEventsErrorResponse])
                res.error_response = out

        return res

    def post_data_compliance_deletion_invitees(self, request: operations.PostDataComplianceDeletionInviteesRequest) -> operations.PostDataComplianceDeletionInviteesResponse:
        r"""Delete Invitee Data
        <!-- theme: info -->
          > This endpoint requires an <strong>Enterprise</strong> subscription.
        
        To submit a request to remove invitee data from all previously booked events in your organization, use this endpoint. Requests for data deletion can take up to 7 days to complete.
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/data_compliance/deletion/invitees'
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request)
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        
        client = utils.configure_security_client(self._client, request.security)
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.PostDataComplianceDeletionInviteesResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 202:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[dict[str, Any]])
                res.post_data_compliance_deletion_invitees_202_application_json_object = out
        elif http_res.status_code == 400:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.PostDataComplianceDeletionInviteesErrorResponse])
                res.error_response = out
        elif http_res.status_code == 401:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.PostDataComplianceDeletionInviteesErrorResponse])
                res.error_response = out
        elif http_res.status_code == 403:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ErrorResponse])
                res.error_response1 = out
        elif http_res.status_code == 404:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.PostDataComplianceDeletionInviteesErrorResponse])
                res.error_response = out
        elif http_res.status_code == 500:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.PostDataComplianceDeletionInviteesErrorResponse])
                res.error_response = out

        return res

    