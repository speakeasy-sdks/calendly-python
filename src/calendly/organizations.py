"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

import requests as requests_http
from . import utils
from calendly.models import operations, shared
from typing import Optional

class Organizations:
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
        
    def delete_memberships(self, request: operations.DeleteOrganizationsUUIDMembershipsRequest) -> operations.DeleteOrganizationsUUIDMembershipsResponse:
        r"""Remove User from Organization
        Removes a user from an organization.
        
        Notes:
        
        * To remove users, the caller must have admin rights for the organization
        
        * An organization owner can’t be removed
        """
        base_url = self._server_url
        
        url = utils.generate_url(operations.DeleteOrganizationsUUIDMembershipsRequest, base_url, '/organization_memberships/{uuid}', request)
        
        
        client = self._security_client
        
        http_res = client.request('DELETE', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.DeleteOrganizationsUUIDMembershipsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 204:
            pass
        elif http_res.status_code in [400, 401, 404, 500]:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.DeleteOrganizationsUUIDMembershipsErrorResponse])
                res.error_response = out
        elif http_res.status_code == 403:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ErrorResponse])
                res.error_response1 = out

        return res

    def get_invitations(self, request: operations.GetOrganizationsOrgUUIDInvitationsUUIDRequest) -> operations.GetOrganizationsOrgUUIDInvitationsUUIDResponse:
        r"""Get Organization Invitation
        Returns an Organization Invitation that was sent to the organization's members.
        """
        base_url = self._server_url
        
        url = utils.generate_url(operations.GetOrganizationsOrgUUIDInvitationsUUIDRequest, base_url, '/organizations/{org_uuid}/invitations/{uuid}', request)
        
        
        client = self._security_client
        
        http_res = client.request('GET', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetOrganizationsOrgUUIDInvitationsUUIDResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetOrganizationsOrgUUIDInvitationsUUID200ApplicationJSON])
                res.get_organizations_org_uuid_invitations_uuid_200_application_json_object = out
        elif http_res.status_code in [400, 401, 403, 404, 500]:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetOrganizationsOrgUUIDInvitationsUUIDErrorResponse])
                res.error_response = out

        return res

    def invite_user(self, request: operations.PostOrganizationsUUIDInvitationsRequest) -> operations.PostOrganizationsUUIDInvitationsResponse:
        r"""Invite User to Organization
        Invites a user to an organization.
        """
        base_url = self._server_url
        
        url = utils.generate_url(operations.PostOrganizationsUUIDInvitationsRequest, base_url, '/organizations/{uuid}/invitations', request)
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "request_body", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        
        client = self._security_client
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.PostOrganizationsUUIDInvitationsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 201:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.PostOrganizationsUUIDInvitations201ApplicationJSON])
                res.post_organizations_uuid_invitations_201_application_json_object = out
        elif http_res.status_code == 400:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ErrorResponse])
                res.error_response = out
        elif http_res.status_code in [401, 404, 500]:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.PostOrganizationsUUIDInvitationsErrorResponse])
                res.error_response1 = out
        elif http_res.status_code == 403:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.PostOrganizationsUUIDInvitations403ApplicationJSON])
                res.post_organizations_uuid_invitations_403_application_json_object = out

        return res

    def list_invitations(self, request: operations.GetOrganizationsUUIDInvitationsRequest) -> operations.GetOrganizationsUUIDInvitationsResponse:
        r"""List Organization Invitations
        Returns a list of Organization Invitations that were sent to the organization's members.
        """
        base_url = self._server_url
        
        url = utils.generate_url(operations.GetOrganizationsUUIDInvitationsRequest, base_url, '/organizations/{uuid}/invitations', request)
        
        query_params = utils.get_query_params(operations.GetOrganizationsUUIDInvitationsRequest, request)
        
        client = self._security_client
        
        http_res = client.request('GET', url, params=query_params)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetOrganizationsUUIDInvitationsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetOrganizationsUUIDInvitations200ApplicationJSON])
                res.get_organizations_uuid_invitations_200_application_json_object = out
        elif http_res.status_code in [400, 401, 403, 404, 500]:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetOrganizationsUUIDInvitationsErrorResponse])
                res.error_response = out

        return res

    def list_memberships(self, request: operations.ListOrganizationMembershipsRequest) -> operations.ListOrganizationMembershipsResponse:
        r"""List Organization Memberships
        Use this to list the Organization Memberships for all users belonging to an organization, use:
        
        * `user` to look up a user's membership in an organization
        
        * `organization` to look up all users that belong to the organization
        
        This endpoint can also be used to retrieve your organization URI.
        """
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/organization_memberships'
        
        query_params = utils.get_query_params(operations.ListOrganizationMembershipsRequest, request)
        
        client = self._security_client
        
        http_res = client.request('GET', url, params=query_params)
        content_type = http_res.headers.get('Content-Type')

        res = operations.ListOrganizationMembershipsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.ListOrganizationMemberships200ApplicationJSON])
                res.list_organization_memberships_200_application_json_object = out
        elif http_res.status_code in [400, 401, 404, 500]:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.ListOrganizationMembershipsErrorResponse])
                res.error_response = out
        elif http_res.status_code == 403:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ErrorResponse])
                res.error_response1 = out

        return res

    def revoke_invite(self, request: operations.RevokeUsersOrganizationInvitationRequest) -> operations.RevokeUsersOrganizationInvitationResponse:
        r"""Revoke User's Organization Invitation
        Use this to revoke an Organization Invitation to an organization. Once revoked, the invitation link that was sent to the invitee is no longer valid.
        """
        base_url = self._server_url
        
        url = utils.generate_url(operations.RevokeUsersOrganizationInvitationRequest, base_url, '/organizations/{org_uuid}/invitations/{uuid}', request)
        
        
        client = self._security_client
        
        http_res = client.request('DELETE', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.RevokeUsersOrganizationInvitationResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 204:
            pass
        elif http_res.status_code == 400:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ErrorResponse])
                res.error_response = out
        elif http_res.status_code in [401, 404, 500]:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.RevokeUsersOrganizationInvitationErrorResponse])
                res.error_response1 = out
        elif http_res.status_code == 403:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.RevokeUsersOrganizationInvitation403ApplicationJSON])
                res.revoke_users_organization_invitation_403_application_json_object = out

        return res

    