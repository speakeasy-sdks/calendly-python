import requests as requests_http
from . import utils
from sdk.models import operations
from typing import Optional

class RoutingForms:
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
        
    def get_routing_form_submissions(self, request: operations.GetRoutingFormSubmissionsRequest) -> operations.GetRoutingFormSubmissionsResponse:
        r"""List Routing Form Submissions
        Get a list of Routing Form Submissions for a specified Routing Form.
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/routing_form_submissions'
        
        query_params = utils.get_query_params(operations.GetRoutingFormSubmissionsQueryParams, request.query_params)
        
        client = self._security_client
        
        http_res = client.request('GET', url, params=query_params)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetRoutingFormSubmissionsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetRoutingFormSubmissions200ApplicationJSON])
                res.get_routing_form_submissions_200_application_json_object = out
        elif http_res.status_code in [400, 401, 403, 404, 500]:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetRoutingFormSubmissionsErrorResponse])
                res.error_response = out

        return res

    def get_routing_form_submissions_uuid(self, request: operations.GetRoutingFormSubmissionsUUIDRequest) -> operations.GetRoutingFormSubmissionsUUIDResponse:
        r"""Get Routing Form Submission
        Get a specified Routing Form Submission.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.GetRoutingFormSubmissionsUUIDPathParams, base_url, '/routing_form_submissions/{uuid}', request.path_params)
        
        
        client = self._security_client
        
        http_res = client.request('GET', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetRoutingFormSubmissionsUUIDResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetRoutingFormSubmissionsUUID200ApplicationJSON])
                res.get_routing_form_submissions_uuid_200_application_json_object = out
        elif http_res.status_code in [400, 401, 403, 404, 500]:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetRoutingFormSubmissionsUUIDErrorResponse])
                res.error_response = out

        return res

    def get_routing_forms(self, request: operations.GetRoutingFormsRequest) -> operations.GetRoutingFormsResponse:
        r"""List Routing Forms
        Get a list of Routing Forms for a specified Organization.
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/routing_forms'
        
        query_params = utils.get_query_params(operations.GetRoutingFormsQueryParams, request.query_params)
        
        client = self._security_client
        
        http_res = client.request('GET', url, params=query_params)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetRoutingFormsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetRoutingForms200ApplicationJSON])
                res.get_routing_forms_200_application_json_object = out
        elif http_res.status_code in [400, 401, 403, 404, 500]:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetRoutingFormsErrorResponse])
                res.error_response = out

        return res

    def get_routing_forms_uuid(self, request: operations.GetRoutingFormsUUIDRequest) -> operations.GetRoutingFormsUUIDResponse:
        r"""Get Routing Form
        Get a specified Routing Form.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.GetRoutingFormsUUIDPathParams, base_url, '/routing_forms/{uuid}', request.path_params)
        
        
        client = self._security_client
        
        http_res = client.request('GET', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetRoutingFormsUUIDResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetRoutingFormsUUID200ApplicationJSON])
                res.get_routing_forms_uuid_200_application_json_object = out
        elif http_res.status_code in [400, 401, 403, 404, 500]:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetRoutingFormsUUIDErrorResponse])
                res.error_response = out

        return res

    