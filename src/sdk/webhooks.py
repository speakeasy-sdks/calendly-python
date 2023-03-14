import requests as requests_http
from . import utils
from sdk.models import operations
from typing import Optional

class Webhooks:
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
        
    def delete_users_user_uuid_webhooks_webhook_uuid(self, request: operations.DeleteUsersUserUUIDWebhooksWebhookUUIDRequest) -> operations.DeleteUsersUserUUIDWebhooksWebhookUUIDResponse:
        r"""Delete Webhook Subscription
        Delete a Webhook Subscription.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, '/webhook_subscriptions/{webhook_uuid}', request.path_params)
        
        
        client = self._security_client
        
        http_res = client.request('DELETE', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.DeleteUsersUserUUIDWebhooksWebhookUUIDResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 204:
            pass
        elif http_res.status_code == 401:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.DeleteUsersUserUUIDWebhooksWebhookUUIDErrorResponse])
                res.error_response = out
        elif http_res.status_code == 403:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.DeleteUsersUserUUIDWebhooksWebhookUUIDErrorResponse])
                res.error_response = out
        elif http_res.status_code == 404:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.DeleteUsersUserUUIDWebhooksWebhookUUIDErrorResponse])
                res.error_response = out
        elif http_res.status_code == 500:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.DeleteUsersUserUUIDWebhooksWebhookUUIDErrorResponse])
                res.error_response = out

        return res

    def get_users_user_uuid_webhooks_webhook_uuid(self, request: operations.GetUsersUserUUIDWebhooksWebhookUUIDRequest) -> operations.GetUsersUserUUIDWebhooksWebhookUUIDResponse:
        r"""Get Webhook Subscription
        Get a specified Webhook Subscription.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, '/webhook_subscriptions/{webhook_uuid}', request.path_params)
        
        
        client = self._security_client
        
        http_res = client.request('GET', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetUsersUserUUIDWebhooksWebhookUUIDResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetUsersUserUUIDWebhooksWebhookUUID200ApplicationJSON])
                res.get_users_user_uuid_webhooks_webhook_uuid_200_application_json_object = out
        elif http_res.status_code == 401:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetUsersUserUUIDWebhooksWebhookUUIDErrorResponse])
                res.error_response = out
        elif http_res.status_code == 403:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetUsersUserUUIDWebhooksWebhookUUIDErrorResponse])
                res.error_response = out
        elif http_res.status_code == 404:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetUsersUserUUIDWebhooksWebhookUUIDErrorResponse])
                res.error_response = out

        return res

    def get_webhooks(self, request: operations.GetWebhooksRequest) -> operations.GetWebhooksResponse:
        r"""List Webhook Subscriptions
        Get a list of Webhook Subscriptions for a specified Organization or User.
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/webhook_subscriptions'
        
        query_params = utils.get_query_params(request.query_params)
        
        client = self._security_client
        
        http_res = client.request('GET', url, params=query_params)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetWebhooksResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetWebhooks200ApplicationJSON])
                res.get_webhooks_200_application_json_object = out
        elif http_res.status_code == 400:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetWebhooksErrorResponse])
                res.error_response = out
        elif http_res.status_code == 401:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetWebhooksErrorResponse])
                res.error_response = out
        elif http_res.status_code == 403:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetWebhooks403ApplicationJSON])
                res.get_webhooks_403_application_json_object = out
        elif http_res.status_code == 404:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetWebhooksErrorResponse])
                res.error_response = out

        return res

    def post_users_uuid_webhooks(self, request: operations.PostUsersUUIDWebhooksRequest) -> operations.PostUsersUUIDWebhooksResponse:
        r"""Create Webhook Subscription
        Create a Webhook Subscription for an Organization or User.
        
        * The `organization` subscription scope triggers the webhook for all subscribed events within the organization.
        * The `user` subscription scope only triggers the webhook for subscribed events that belong to the specific user.
        
        | Event | Allowed Subscription Scopes |
        | ----- | --------------------------- |
        | <pre>invitee.created</pre> | `organization` `user` |
        | <pre>invitee.canceled</pre> | `organization` `user` |
        | <pre>routing_form_submission.created</pre> | `organization` <br /> <small>Create separate Webhook Subscriptions for events with different subscription scopes.</small> |
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/webhook_subscriptions'
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request)
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        
        client = self._security_client
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.PostUsersUUIDWebhooksResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 201:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.PostUsersUUIDWebhooks201ApplicationJSON])
                res.post_users_uuid_webhooks_201_application_json_object = out
        elif http_res.status_code == 400:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.PostUsersUUIDWebhooksErrorResponse])
                res.error_response = out
        elif http_res.status_code == 401:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.PostUsersUUIDWebhooksErrorResponse])
                res.error_response = out
        elif http_res.status_code == 403:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.PostUsersUUIDWebhooks403ApplicationJSON])
                res.post_users_uuid_webhooks_403_application_json_object = out
        elif http_res.status_code == 404:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.PostUsersUUIDWebhooksErrorResponse])
                res.error_response = out
        elif http_res.status_code == 409:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.PostUsersUUIDWebhooksErrorResponse])
                res.error_response = out

        return res

    