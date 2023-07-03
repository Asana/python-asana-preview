# coding: utf-8

"""
    Asana

    This is the interface for interacting with the [Asana Platform](https://developers.asana.com). Our API reference is generated from our [OpenAPI spec] (https://raw.githubusercontent.com/Asana/openapi/master/defs/asana_oas.yaml).  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from asana_preview.api_client import ApiClient


class ProjectTemplatesApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def delete_project_template(self, project_template_gid, **kwargs):  # noqa: E501
        """Delete a project template  # noqa: E501

        A specific, existing project template can be deleted by making a DELETE request on the URL for that project template.  Returns an empty data record.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_project_template(project_template_gid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str project_template_gid: Globally unique identifier for the project template. (required)
        :return: EmptyResponseData
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_project_template_with_http_info(project_template_gid, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_project_template_with_http_info(project_template_gid, **kwargs)  # noqa: E501
            return data

    def delete_project_template_with_http_info(self, project_template_gid, **kwargs):  # noqa: E501
        """Delete a project template  # noqa: E501

        A specific, existing project template can be deleted by making a DELETE request on the URL for that project template.  Returns an empty data record.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_project_template_with_http_info(project_template_gid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str project_template_gid: Globally unique identifier for the project template. (required)
        :return: EmptyResponseData
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['project_template_gid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_project_template" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'project_template_gid' is set
        if ('project_template_gid' not in params or
                params['project_template_gid'] is None):
            raise ValueError("Missing the required parameter `project_template_gid` when calling `delete_project_template`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'project_template_gid' in params:
            path_params['project_template_gid'] = params['project_template_gid']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json; charset=UTF-8'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        return self.api_client.call_api(
            '/project_templates/{project_template_gid}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='EmptyResponseData',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_project_template(self, project_template_gid, **kwargs):  # noqa: E501
        """Get a project template  # noqa: E501

        Returns the complete project template record for a single project template.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_project_template(project_template_gid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str project_template_gid: Globally unique identifier for the project template. (required)
        :param list[str] opt_fields: This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
        :return: ProjectTemplateResponseData
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_project_template_with_http_info(project_template_gid, **kwargs)  # noqa: E501
        else:
            (data) = self.get_project_template_with_http_info(project_template_gid, **kwargs)  # noqa: E501
            return data

    def get_project_template_with_http_info(self, project_template_gid, **kwargs):  # noqa: E501
        """Get a project template  # noqa: E501

        Returns the complete project template record for a single project template.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_project_template_with_http_info(project_template_gid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str project_template_gid: Globally unique identifier for the project template. (required)
        :param list[str] opt_fields: This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
        :return: ProjectTemplateResponseData
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['project_template_gid', 'opt_fields']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_project_template" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'project_template_gid' is set
        if ('project_template_gid' not in params or
                params['project_template_gid'] is None):
            raise ValueError("Missing the required parameter `project_template_gid` when calling `get_project_template`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'project_template_gid' in params:
            path_params['project_template_gid'] = params['project_template_gid']  # noqa: E501

        query_params = []
        if 'opt_fields' in params:
            query_params.append(('opt_fields', params['opt_fields']))  # noqa: E501
            collection_formats['opt_fields'] = 'csv'  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json; charset=UTF-8'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        return self.api_client.call_api(
            '/project_templates/{project_template_gid}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ProjectTemplateResponseData',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_project_templates(self, **kwargs):  # noqa: E501
        """Get multiple project templates  # noqa: E501

        Returns the compact project template records for all project templates in the given team or workspace.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_project_templates(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str workspace: The workspace to filter results on.
        :param str team: The team to filter projects on.
        :param int limit: Results per page. The number of objects to return per page. The value must be between 1 and 100.
        :param str offset: Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. 'Note: You can only pass in an offset that was returned to you via a previously paginated request.'
        :param list[str] opt_fields: This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
        :return: ProjectTemplateResponseArray
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_project_templates_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_project_templates_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_project_templates_with_http_info(self, **kwargs):  # noqa: E501
        """Get multiple project templates  # noqa: E501

        Returns the compact project template records for all project templates in the given team or workspace.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_project_templates_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str workspace: The workspace to filter results on.
        :param str team: The team to filter projects on.
        :param int limit: Results per page. The number of objects to return per page. The value must be between 1 and 100.
        :param str offset: Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. 'Note: You can only pass in an offset that was returned to you via a previously paginated request.'
        :param list[str] opt_fields: This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
        :return: ProjectTemplateResponseArray
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['workspace', 'team', 'limit', 'offset', 'opt_fields']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_project_templates" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'workspace' in params:
            query_params.append(('workspace', params['workspace']))  # noqa: E501
        if 'team' in params:
            query_params.append(('team', params['team']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if 'opt_fields' in params:
            query_params.append(('opt_fields', params['opt_fields']))  # noqa: E501
            collection_formats['opt_fields'] = 'csv'  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json; charset=UTF-8'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        return self.api_client.call_api(
            '/project_templates', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ProjectTemplateResponseArray',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_project_templates_for_team(self, team_gid, **kwargs):  # noqa: E501
        """Get a team's project templates  # noqa: E501

        Returns the compact project template records for all project templates in the team.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_project_templates_for_team(team_gid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str team_gid: Globally unique identifier for the team. (required)
        :param int limit: Results per page. The number of objects to return per page. The value must be between 1 and 100.
        :param str offset: Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. 'Note: You can only pass in an offset that was returned to you via a previously paginated request.'
        :param list[str] opt_fields: This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
        :return: ProjectTemplateResponseArray
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_project_templates_for_team_with_http_info(team_gid, **kwargs)  # noqa: E501
        else:
            (data) = self.get_project_templates_for_team_with_http_info(team_gid, **kwargs)  # noqa: E501
            return data

    def get_project_templates_for_team_with_http_info(self, team_gid, **kwargs):  # noqa: E501
        """Get a team's project templates  # noqa: E501

        Returns the compact project template records for all project templates in the team.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_project_templates_for_team_with_http_info(team_gid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str team_gid: Globally unique identifier for the team. (required)
        :param int limit: Results per page. The number of objects to return per page. The value must be between 1 and 100.
        :param str offset: Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. 'Note: You can only pass in an offset that was returned to you via a previously paginated request.'
        :param list[str] opt_fields: This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
        :return: ProjectTemplateResponseArray
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['team_gid', 'limit', 'offset', 'opt_fields']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_project_templates_for_team" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'team_gid' is set
        if ('team_gid' not in params or
                params['team_gid'] is None):
            raise ValueError("Missing the required parameter `team_gid` when calling `get_project_templates_for_team`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'team_gid' in params:
            path_params['team_gid'] = params['team_gid']  # noqa: E501

        query_params = []
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if 'opt_fields' in params:
            query_params.append(('opt_fields', params['opt_fields']))  # noqa: E501
            collection_formats['opt_fields'] = 'csv'  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json; charset=UTF-8'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        return self.api_client.call_api(
            '/teams/{team_gid}/project_templates', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ProjectTemplateResponseArray',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def instantiate_project(self, project_template_gid, **kwargs):  # noqa: E501
        """Instantiate a project from a project template  # noqa: E501

        Creates and returns a job that will asynchronously handle the project instantiation.  To form this request, it is recommended to first make a request to [get a project template](/reference/getprojecttemplate). Then, from the response, copy the `gid` from the object in the `requested_dates` array. This `gid` should be used in `requested_dates` to instantiate a project.  _Note: The body of this request will differ if your workspace is an organization. To determine if your workspace is an organization, use the [is_organization](/reference/workspaces) parameter._  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.instantiate_project(project_template_gid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str project_template_gid: Globally unique identifier for the project template. (required)
        :param ProjectTemplateGidInstantiateProjectBody body: Describes the inputs used for instantiating a project, such as the resulting project's name, which team it should be created in, and values for date variables.
        :param list[str] opt_fields: This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
        :return: JobResponseData
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.instantiate_project_with_http_info(project_template_gid, **kwargs)  # noqa: E501
        else:
            (data) = self.instantiate_project_with_http_info(project_template_gid, **kwargs)  # noqa: E501
            return data

    def instantiate_project_with_http_info(self, project_template_gid, **kwargs):  # noqa: E501
        """Instantiate a project from a project template  # noqa: E501

        Creates and returns a job that will asynchronously handle the project instantiation.  To form this request, it is recommended to first make a request to [get a project template](/reference/getprojecttemplate). Then, from the response, copy the `gid` from the object in the `requested_dates` array. This `gid` should be used in `requested_dates` to instantiate a project.  _Note: The body of this request will differ if your workspace is an organization. To determine if your workspace is an organization, use the [is_organization](/reference/workspaces) parameter._  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.instantiate_project_with_http_info(project_template_gid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str project_template_gid: Globally unique identifier for the project template. (required)
        :param ProjectTemplateGidInstantiateProjectBody body: Describes the inputs used for instantiating a project, such as the resulting project's name, which team it should be created in, and values for date variables.
        :param list[str] opt_fields: This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
        :return: JobResponseData
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['project_template_gid', 'body', 'opt_fields']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method instantiate_project" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'project_template_gid' is set
        if ('project_template_gid' not in params or
                params['project_template_gid'] is None):
            raise ValueError("Missing the required parameter `project_template_gid` when calling `instantiate_project`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'project_template_gid' in params:
            path_params['project_template_gid'] = params['project_template_gid']  # noqa: E501

        query_params = []
        if 'opt_fields' in params:
            query_params.append(('opt_fields', params['opt_fields']))  # noqa: E501
            collection_formats['opt_fields'] = 'csv'  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json; charset=UTF-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json; charset=UTF-8'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        return self.api_client.call_api(
            '/project_templates/{project_template_gid}/instantiateProject', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='JobResponseData',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
