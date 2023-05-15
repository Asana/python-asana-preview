# asana-preview [![PyPi Version][pypi-image]][pypi-url]

This is a [preview version](https://forum.asana.com/t/try-an-early-preview-of-our-new-node-js-and-python-sdks/394881) of Asana's new python client library. For feedback and feature requests, please leave a comment on [this forum thread](https://forum.asana.com/t/try-an-early-preview-of-our-new-node-js-and-python-sdks/394881) or through [the feedback form on our documentation site](https://form-beta.asana.com/?k=C4sELCq6hAUsoWEY0kJwAA&d=15793206719)

- Package version: 1.0.5

## Requirements.

Python >=3.6

## Installation & Usage
### pip install

```sh
pip install asana-preview
```

Then import the package:
```python
import asana_preview
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import asana_preview
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
import asana_preview
from asana_preview.api import users_api
from pprint import pprint

# Configure Bearer authorization: personalAccessToken
configuration = asana_preview.Configuration(
    access_token = 'PERSONAL_ACCESS_TOKEN'
)

# Enter a context with an instance of the API client
with asana_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = users_api.UsersApi(api_client)
    user_gid = "me" # str | A string identifying a user. This can either be the string "me", an email, or the gid of a user.
    opt_fields = ["email", "name", "workspaces"] # [str] | Defines fields to return.  Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below.  The gid of included objects will always be returned, regardless of the field options. (optional)

    # Example passing only required values
    try:
        # Get a user
        user = api_instance.get_user(user_gid)
        pprint(user)
    except asana_preview.ApiException as e:
        print("Exception when calling UsersApi->get_user: %s\n" % e)

    # Example using opt_fields
    try:
        # Get a user with opt_fields
        user = api_instance.get_user(user_gid, opt_fields=opt_fields)
        pprint(user)
    except asana_preview.ApiException as e:
        print("Exception when calling UsersApi->get_user: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *https://app.asana.com/api/1.0*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AttachmentsApi* | [**create_attachment_for_object**](docs/AttachmentsApi.md#create_attachment_for_object) | **POST** /attachments | Upload an attachment
*AttachmentsApi* | [**delete_attachment**](docs/AttachmentsApi.md#delete_attachment) | **DELETE** /attachments/{attachment_gid} | Delete an attachment
*AttachmentsApi* | [**get_attachment**](docs/AttachmentsApi.md#get_attachment) | **GET** /attachments/{attachment_gid} | Get an attachment
*AttachmentsApi* | [**get_attachments_for_object**](docs/AttachmentsApi.md#get_attachments_for_object) | **GET** /attachments | Get attachments from an object
*AuditLogAPIApi* | [**get_audit_log_events**](docs/AuditLogAPIApi.md#get_audit_log_events) | **GET** /workspaces/{workspace_gid}/audit_log_events | Get audit log events
*BatchAPIApi* | [**create_batch_request**](docs/BatchAPIApi.md#create_batch_request) | **POST** /batch | Submit parallel requests
*CustomFieldSettingsApi* | [**get_custom_field_settings_for_portfolio**](docs/CustomFieldSettingsApi.md#get_custom_field_settings_for_portfolio) | **GET** /portfolios/{portfolio_gid}/custom_field_settings | Get a portfolio&#39;s custom fields
*CustomFieldSettingsApi* | [**get_custom_field_settings_for_project**](docs/CustomFieldSettingsApi.md#get_custom_field_settings_for_project) | **GET** /projects/{project_gid}/custom_field_settings | Get a project&#39;s custom fields
*CustomFieldsApi* | [**create_custom_field**](docs/CustomFieldsApi.md#create_custom_field) | **POST** /custom_fields | Create a custom field
*CustomFieldsApi* | [**create_enum_option_for_custom_field**](docs/CustomFieldsApi.md#create_enum_option_for_custom_field) | **POST** /custom_fields/{custom_field_gid}/enum_options | Create an enum option
*CustomFieldsApi* | [**delete_custom_field**](docs/CustomFieldsApi.md#delete_custom_field) | **DELETE** /custom_fields/{custom_field_gid} | Delete a custom field
*CustomFieldsApi* | [**get_custom_field**](docs/CustomFieldsApi.md#get_custom_field) | **GET** /custom_fields/{custom_field_gid} | Get a custom field
*CustomFieldsApi* | [**get_custom_fields_for_workspace**](docs/CustomFieldsApi.md#get_custom_fields_for_workspace) | **GET** /workspaces/{workspace_gid}/custom_fields | Get a workspace&#39;s custom fields
*CustomFieldsApi* | [**insert_enum_option_for_custom_field**](docs/CustomFieldsApi.md#insert_enum_option_for_custom_field) | **POST** /custom_fields/{custom_field_gid}/enum_options/insert | Reorder a custom field&#39;s enum
*CustomFieldsApi* | [**update_custom_field**](docs/CustomFieldsApi.md#update_custom_field) | **PUT** /custom_fields/{custom_field_gid} | Update a custom field
*CustomFieldsApi* | [**update_enum_option**](docs/CustomFieldsApi.md#update_enum_option) | **PUT** /enum_options/{enum_option_gid} | Update an enum option
*EventsApi* | [**get_events**](docs/EventsApi.md#get_events) | **GET** /events | Get events on a resource
*GoalRelationshipsApi* | [**add_supporting_relationship**](docs/GoalRelationshipsApi.md#add_supporting_relationship) | **POST** /goals/{goal_gid}/addSupportingRelationship | Add a supporting goal relationship
*GoalRelationshipsApi* | [**get_goal_relationship**](docs/GoalRelationshipsApi.md#get_goal_relationship) | **GET** /goal_relationships/{goal_relationship_gid} | Get a goal relationship
*GoalRelationshipsApi* | [**get_goal_relationships**](docs/GoalRelationshipsApi.md#get_goal_relationships) | **GET** /goal_relationships | Get goal relationships
*GoalRelationshipsApi* | [**remove_supporting_relationship**](docs/GoalRelationshipsApi.md#remove_supporting_relationship) | **POST** /goals/{goal_gid}/removeSupportingRelationship | Removes a supporting goal relationship
*GoalRelationshipsApi* | [**update_goal_relationship**](docs/GoalRelationshipsApi.md#update_goal_relationship) | **PUT** /goal_relationships/{goal_relationship_gid} | Update a goal relationship
*GoalsApi* | [**create_goal**](docs/GoalsApi.md#create_goal) | **POST** /goals | Create a goal
*GoalsApi* | [**create_goal_metric**](docs/GoalsApi.md#create_goal_metric) | **POST** /goals/{goal_gid}/setMetric | Create a goal metric
*GoalsApi* | [**delete_goal**](docs/GoalsApi.md#delete_goal) | **DELETE** /goals/{goal_gid} | Delete a goal
*GoalsApi* | [**get_goal**](docs/GoalsApi.md#get_goal) | **GET** /goals/{goal_gid} | Get a goal
*GoalsApi* | [**get_goals**](docs/GoalsApi.md#get_goals) | **GET** /goals | Get goals
*GoalsApi* | [**get_parent_goals_for_goal**](docs/GoalsApi.md#get_parent_goals_for_goal) | **GET** /goals/{goal_gid}/parentGoals | Get parent goals from a goal
*GoalsApi* | [**update_goal**](docs/GoalsApi.md#update_goal) | **PUT** /goals/{goal_gid} | Update a goal
*GoalsApi* | [**update_goal_metric**](docs/GoalsApi.md#update_goal_metric) | **POST** /goals/{goal_gid}/setMetricCurrentValue | Update a goal metric
*JobsApi* | [**get_job**](docs/JobsApi.md#get_job) | **GET** /jobs/{job_gid} | Get a job by id
*MembershipsApi* | [**create_membership**](docs/MembershipsApi.md#create_membership) | **POST** /memberships | Create a membership
*MembershipsApi* | [**delete_membership**](docs/MembershipsApi.md#delete_membership) | **DELETE** /memberships/{membership_gid} | Delete a membership
*MembershipsApi* | [**get_memberships**](docs/MembershipsApi.md#get_memberships) | **GET** /memberships | Get multiple memberships
*MembershipsApi* | [**update_membership**](docs/MembershipsApi.md#update_membership) | **PUT** /memberships/{membership_gid} | Update a membership
*OrganizationExportsApi* | [**create_organization_export**](docs/OrganizationExportsApi.md#create_organization_export) | **POST** /organization_exports | Create an organization export request
*OrganizationExportsApi* | [**get_organization_export**](docs/OrganizationExportsApi.md#get_organization_export) | **GET** /organization_exports/{organization_export_gid} | Get details on an org export request
*PortfolioMembershipsApi* | [**get_portfolio_membership**](docs/PortfolioMembershipsApi.md#get_portfolio_membership) | **GET** /portfolio_memberships/{portfolio_membership_gid} | Get a portfolio membership
*PortfolioMembershipsApi* | [**get_portfolio_memberships**](docs/PortfolioMembershipsApi.md#get_portfolio_memberships) | **GET** /portfolio_memberships | Get multiple portfolio memberships
*PortfolioMembershipsApi* | [**get_portfolio_memberships_for_portfolio**](docs/PortfolioMembershipsApi.md#get_portfolio_memberships_for_portfolio) | **GET** /portfolios/{portfolio_gid}/portfolio_memberships | Get memberships from a portfolio
*PortfoliosApi* | [**add_custom_field_setting_for_portfolio**](docs/PortfoliosApi.md#add_custom_field_setting_for_portfolio) | **POST** /portfolios/{portfolio_gid}/addCustomFieldSetting | Add a custom field to a portfolio
*PortfoliosApi* | [**add_item_for_portfolio**](docs/PortfoliosApi.md#add_item_for_portfolio) | **POST** /portfolios/{portfolio_gid}/addItem | Add a portfolio item
*PortfoliosApi* | [**add_members_for_portfolio**](docs/PortfoliosApi.md#add_members_for_portfolio) | **POST** /portfolios/{portfolio_gid}/addMembers | Add users to a portfolio
*PortfoliosApi* | [**create_portfolio**](docs/PortfoliosApi.md#create_portfolio) | **POST** /portfolios | Create a portfolio
*PortfoliosApi* | [**delete_portfolio**](docs/PortfoliosApi.md#delete_portfolio) | **DELETE** /portfolios/{portfolio_gid} | Delete a portfolio
*PortfoliosApi* | [**get_items_for_portfolio**](docs/PortfoliosApi.md#get_items_for_portfolio) | **GET** /portfolios/{portfolio_gid}/items | Get portfolio items
*PortfoliosApi* | [**get_portfolio**](docs/PortfoliosApi.md#get_portfolio) | **GET** /portfolios/{portfolio_gid} | Get a portfolio
*PortfoliosApi* | [**get_portfolios**](docs/PortfoliosApi.md#get_portfolios) | **GET** /portfolios | Get multiple portfolios
*PortfoliosApi* | [**remove_custom_field_setting_for_portfolio**](docs/PortfoliosApi.md#remove_custom_field_setting_for_portfolio) | **POST** /portfolios/{portfolio_gid}/removeCustomFieldSetting | Remove a custom field from a portfolio
*PortfoliosApi* | [**remove_item_for_portfolio**](docs/PortfoliosApi.md#remove_item_for_portfolio) | **POST** /portfolios/{portfolio_gid}/removeItem | Remove a portfolio item
*PortfoliosApi* | [**remove_members_for_portfolio**](docs/PortfoliosApi.md#remove_members_for_portfolio) | **POST** /portfolios/{portfolio_gid}/removeMembers | Remove users from a portfolio
*PortfoliosApi* | [**update_portfolio**](docs/PortfoliosApi.md#update_portfolio) | **PUT** /portfolios/{portfolio_gid} | Update a portfolio
*ProjectBriefsApi* | [**create_project_brief**](docs/ProjectBriefsApi.md#create_project_brief) | **POST** /projects/{project_gid}/project_briefs | Create a project brief
*ProjectBriefsApi* | [**delete_project_brief**](docs/ProjectBriefsApi.md#delete_project_brief) | **DELETE** /project_briefs/{project_brief_gid} | Delete a project brief
*ProjectBriefsApi* | [**get_project_brief**](docs/ProjectBriefsApi.md#get_project_brief) | **GET** /project_briefs/{project_brief_gid} | Get a project brief
*ProjectBriefsApi* | [**update_project_brief**](docs/ProjectBriefsApi.md#update_project_brief) | **PUT** /project_briefs/{project_brief_gid} | Update a project brief
*ProjectMembershipsApi* | [**get_project_membership**](docs/ProjectMembershipsApi.md#get_project_membership) | **GET** /project_memberships/{project_membership_gid} | Get a project membership
*ProjectMembershipsApi* | [**get_project_memberships_for_project**](docs/ProjectMembershipsApi.md#get_project_memberships_for_project) | **GET** /projects/{project_gid}/project_memberships | Get memberships from a project
*ProjectStatusesApi* | [**create_project_status_for_project**](docs/ProjectStatusesApi.md#create_project_status_for_project) | **POST** /projects/{project_gid}/project_statuses | Create a project status
*ProjectStatusesApi* | [**delete_project_status**](docs/ProjectStatusesApi.md#delete_project_status) | **DELETE** /project_statuses/{project_status_gid} | Delete a project status
*ProjectStatusesApi* | [**get_project_status**](docs/ProjectStatusesApi.md#get_project_status) | **GET** /project_statuses/{project_status_gid} | Get a project status
*ProjectStatusesApi* | [**get_project_statuses_for_project**](docs/ProjectStatusesApi.md#get_project_statuses_for_project) | **GET** /projects/{project_gid}/project_statuses | Get statuses from a project
*ProjectTemplatesApi* | [**get_project_template**](docs/ProjectTemplatesApi.md#get_project_template) | **GET** /project_templates/{project_template_gid} | Get a project template
*ProjectTemplatesApi* | [**get_project_templates**](docs/ProjectTemplatesApi.md#get_project_templates) | **GET** /project_templates | Get multiple project templates
*ProjectTemplatesApi* | [**get_project_templates_for_team**](docs/ProjectTemplatesApi.md#get_project_templates_for_team) | **GET** /teams/{team_gid}/project_templates | Get a team&#39;s project templates
*ProjectTemplatesApi* | [**instantiate_project**](docs/ProjectTemplatesApi.md#instantiate_project) | **POST** /project_templates/{project_template_gid}/instantiateProject | Instantiate a project from a project template
*ProjectsApi* | [**add_custom_field_setting_for_project**](docs/ProjectsApi.md#add_custom_field_setting_for_project) | **POST** /projects/{project_gid}/addCustomFieldSetting | Add a custom field to a project
*ProjectsApi* | [**add_followers_for_project**](docs/ProjectsApi.md#add_followers_for_project) | **POST** /projects/{project_gid}/addFollowers | Add followers to a project
*ProjectsApi* | [**add_members_for_project**](docs/ProjectsApi.md#add_members_for_project) | **POST** /projects/{project_gid}/addMembers | Add users to a project
*ProjectsApi* | [**create_project**](docs/ProjectsApi.md#create_project) | **POST** /projects | Create a project
*ProjectsApi* | [**create_project_for_team**](docs/ProjectsApi.md#create_project_for_team) | **POST** /teams/{team_gid}/projects | Create a project in a team
*ProjectsApi* | [**create_project_for_workspace**](docs/ProjectsApi.md#create_project_for_workspace) | **POST** /workspaces/{workspace_gid}/projects | Create a project in a workspace
*ProjectsApi* | [**delete_project**](docs/ProjectsApi.md#delete_project) | **DELETE** /projects/{project_gid} | Delete a project
*ProjectsApi* | [**duplicate_project**](docs/ProjectsApi.md#duplicate_project) | **POST** /projects/{project_gid}/duplicate | Duplicate a project
*ProjectsApi* | [**get_project**](docs/ProjectsApi.md#get_project) | **GET** /projects/{project_gid} | Get a project
*ProjectsApi* | [**get_projects**](docs/ProjectsApi.md#get_projects) | **GET** /projects | Get multiple projects
*ProjectsApi* | [**get_projects_for_task**](docs/ProjectsApi.md#get_projects_for_task) | **GET** /tasks/{task_gid}/projects | Get projects a task is in
*ProjectsApi* | [**get_projects_for_team**](docs/ProjectsApi.md#get_projects_for_team) | **GET** /teams/{team_gid}/projects | Get a team&#39;s projects
*ProjectsApi* | [**get_projects_for_workspace**](docs/ProjectsApi.md#get_projects_for_workspace) | **GET** /workspaces/{workspace_gid}/projects | Get all projects in a workspace
*ProjectsApi* | [**get_task_counts_for_project**](docs/ProjectsApi.md#get_task_counts_for_project) | **GET** /projects/{project_gid}/task_counts | Get task count of a project
*ProjectsApi* | [**project_save_as_template**](docs/ProjectsApi.md#project_save_as_template) | **POST** /projects/{project_gid}/saveAsTemplate | Create a project template from a project
*ProjectsApi* | [**remove_custom_field_setting_for_project**](docs/ProjectsApi.md#remove_custom_field_setting_for_project) | **POST** /projects/{project_gid}/removeCustomFieldSetting | Remove a custom field from a project
*ProjectsApi* | [**remove_followers_for_project**](docs/ProjectsApi.md#remove_followers_for_project) | **POST** /projects/{project_gid}/removeFollowers | Remove followers from a project
*ProjectsApi* | [**remove_members_for_project**](docs/ProjectsApi.md#remove_members_for_project) | **POST** /projects/{project_gid}/removeMembers | Remove users from a project
*ProjectsApi* | [**update_project**](docs/ProjectsApi.md#update_project) | **PUT** /projects/{project_gid} | Update a project
*RulesApi* | [**trigger_rule**](docs/RulesApi.md#trigger_rule) | **POST** /rule_triggers/{rule_trigger_gid}/run | Trigger a rule
*SectionsApi* | [**add_task_for_section**](docs/SectionsApi.md#add_task_for_section) | **POST** /sections/{section_gid}/addTask | Add task to section
*SectionsApi* | [**create_section_for_project**](docs/SectionsApi.md#create_section_for_project) | **POST** /projects/{project_gid}/sections | Create a section in a project
*SectionsApi* | [**delete_section**](docs/SectionsApi.md#delete_section) | **DELETE** /sections/{section_gid} | Delete a section
*SectionsApi* | [**get_section**](docs/SectionsApi.md#get_section) | **GET** /sections/{section_gid} | Get a section
*SectionsApi* | [**get_sections_for_project**](docs/SectionsApi.md#get_sections_for_project) | **GET** /projects/{project_gid}/sections | Get sections in a project
*SectionsApi* | [**insert_section_for_project**](docs/SectionsApi.md#insert_section_for_project) | **POST** /projects/{project_gid}/sections/insert | Move or Insert sections
*SectionsApi* | [**update_section**](docs/SectionsApi.md#update_section) | **PUT** /sections/{section_gid} | Update a section
*StatusUpdatesApi* | [**create_status_for_object**](docs/StatusUpdatesApi.md#create_status_for_object) | **POST** /status_updates | Create a status update
*StatusUpdatesApi* | [**delete_status**](docs/StatusUpdatesApi.md#delete_status) | **DELETE** /status_updates/{status_gid} | Delete a status update
*StatusUpdatesApi* | [**get_status**](docs/StatusUpdatesApi.md#get_status) | **GET** /status_updates/{status_gid} | Get a status update
*StatusUpdatesApi* | [**get_statuses_for_object**](docs/StatusUpdatesApi.md#get_statuses_for_object) | **GET** /status_updates | Get status updates from an object
*StoriesApi* | [**create_story_for_task**](docs/StoriesApi.md#create_story_for_task) | **POST** /tasks/{task_gid}/stories | Create a story on a task
*StoriesApi* | [**delete_story**](docs/StoriesApi.md#delete_story) | **DELETE** /stories/{story_gid} | Delete a story
*StoriesApi* | [**get_stories_for_task**](docs/StoriesApi.md#get_stories_for_task) | **GET** /tasks/{task_gid}/stories | Get stories from a task
*StoriesApi* | [**get_story**](docs/StoriesApi.md#get_story) | **GET** /stories/{story_gid} | Get a story
*StoriesApi* | [**update_story**](docs/StoriesApi.md#update_story) | **PUT** /stories/{story_gid} | Update a story
*TagsApi* | [**create_tag**](docs/TagsApi.md#create_tag) | **POST** /tags | Create a tag
*TagsApi* | [**create_tag_for_workspace**](docs/TagsApi.md#create_tag_for_workspace) | **POST** /workspaces/{workspace_gid}/tags | Create a tag in a workspace
*TagsApi* | [**delete_tag**](docs/TagsApi.md#delete_tag) | **DELETE** /tags/{tag_gid} | Delete a tag
*TagsApi* | [**get_tag**](docs/TagsApi.md#get_tag) | **GET** /tags/{tag_gid} | Get a tag
*TagsApi* | [**get_tags**](docs/TagsApi.md#get_tags) | **GET** /tags | Get multiple tags
*TagsApi* | [**get_tags_for_task**](docs/TagsApi.md#get_tags_for_task) | **GET** /tasks/{task_gid}/tags | Get a task&#39;s tags
*TagsApi* | [**get_tags_for_workspace**](docs/TagsApi.md#get_tags_for_workspace) | **GET** /workspaces/{workspace_gid}/tags | Get tags in a workspace
*TagsApi* | [**update_tag**](docs/TagsApi.md#update_tag) | **PUT** /tags/{tag_gid} | Update a tag
*TasksApi* | [**add_dependencies_for_task**](docs/TasksApi.md#add_dependencies_for_task) | **POST** /tasks/{task_gid}/addDependencies | Set dependencies for a task
*TasksApi* | [**add_dependents_for_task**](docs/TasksApi.md#add_dependents_for_task) | **POST** /tasks/{task_gid}/addDependents | Set dependents for a task
*TasksApi* | [**add_project_for_task**](docs/TasksApi.md#add_project_for_task) | **POST** /tasks/{task_gid}/addProject | Add a project to a task
*TasksApi* | [**add_tag_for_task**](docs/TasksApi.md#add_tag_for_task) | **POST** /tasks/{task_gid}/addTag | Add a tag to a task
*TasksApi* | [**create_subtask_for_task**](docs/TasksApi.md#create_subtask_for_task) | **POST** /tasks/{task_gid}/subtasks | Create a subtask
*TasksApi* | [**create_task**](docs/TasksApi.md#create_task) | **POST** /tasks | Create a task
*TasksApi* | [**delete_task**](docs/TasksApi.md#delete_task) | **DELETE** /tasks/{task_gid} | Delete a task
*TasksApi* | [**duplicate_task**](docs/TasksApi.md#duplicate_task) | **POST** /tasks/{task_gid}/duplicate | Duplicate a task
*TasksApi* | [**get_dependencies_for_task**](docs/TasksApi.md#get_dependencies_for_task) | **GET** /tasks/{task_gid}/dependencies | Get dependencies from a task
*TasksApi* | [**get_dependents_for_task**](docs/TasksApi.md#get_dependents_for_task) | **GET** /tasks/{task_gid}/dependents | Get dependents from a task
*TasksApi* | [**get_subtasks_for_task**](docs/TasksApi.md#get_subtasks_for_task) | **GET** /tasks/{task_gid}/subtasks | Get subtasks from a task
*TasksApi* | [**get_task**](docs/TasksApi.md#get_task) | **GET** /tasks/{task_gid} | Get a task
*TasksApi* | [**get_tasks**](docs/TasksApi.md#get_tasks) | **GET** /tasks | Get multiple tasks
*TasksApi* | [**get_tasks_for_project**](docs/TasksApi.md#get_tasks_for_project) | **GET** /projects/{project_gid}/tasks | Get tasks from a project
*TasksApi* | [**get_tasks_for_section**](docs/TasksApi.md#get_tasks_for_section) | **GET** /sections/{section_gid}/tasks | Get tasks from a section
*TasksApi* | [**get_tasks_for_tag**](docs/TasksApi.md#get_tasks_for_tag) | **GET** /tags/{tag_gid}/tasks | Get tasks from a tag
*TasksApi* | [**get_tasks_for_user_task_list**](docs/TasksApi.md#get_tasks_for_user_task_list) | **GET** /user_task_lists/{user_task_list_gid}/tasks | Get tasks from a user task list
*TasksApi* | [**remove_dependencies_for_task**](docs/TasksApi.md#remove_dependencies_for_task) | **POST** /tasks/{task_gid}/removeDependencies | Unlink dependencies from a task
*TasksApi* | [**remove_dependents_for_task**](docs/TasksApi.md#remove_dependents_for_task) | **POST** /tasks/{task_gid}/removeDependents | Unlink dependents from a task
*TasksApi* | [**remove_follower_for_task**](docs/TasksApi.md#remove_follower_for_task) | **POST** /tasks/{task_gid}/removeFollowers | Remove followers from a task
*TasksApi* | [**remove_project_for_task**](docs/TasksApi.md#remove_project_for_task) | **POST** /tasks/{task_gid}/removeProject | Remove a project from a task
*TasksApi* | [**remove_tag_for_task**](docs/TasksApi.md#remove_tag_for_task) | **POST** /tasks/{task_gid}/removeTag | Remove a tag from a task
*TasksApi* | [**search_tasks_for_workspace**](docs/TasksApi.md#search_tasks_for_workspace) | **GET** /workspaces/{workspace_gid}/tasks/search | Search tasks in a workspace
*TasksApi* | [**set_parent_for_task**](docs/TasksApi.md#set_parent_for_task) | **POST** /tasks/{task_gid}/setParent | Set the parent of a task
*TasksApi* | [**update_task**](docs/TasksApi.md#update_task) | **PUT** /tasks/{task_gid} | Update a task
*TeamMembershipsApi* | [**get_team_membership**](docs/TeamMembershipsApi.md#get_team_membership) | **GET** /team_memberships/{team_membership_gid} | Get a team membership
*TeamMembershipsApi* | [**get_team_memberships**](docs/TeamMembershipsApi.md#get_team_memberships) | **GET** /team_memberships | Get team memberships
*TeamMembershipsApi* | [**get_team_memberships_for_team**](docs/TeamMembershipsApi.md#get_team_memberships_for_team) | **GET** /teams/{team_gid}/team_memberships | Get memberships from a team
*TeamMembershipsApi* | [**get_team_memberships_for_user**](docs/TeamMembershipsApi.md#get_team_memberships_for_user) | **GET** /users/{user_gid}/team_memberships | Get memberships from a user
*TeamsApi* | [**add_user_for_team**](docs/TeamsApi.md#add_user_for_team) | **POST** /teams/{team_gid}/addUser | Add a user to a team
*TeamsApi* | [**create_team**](docs/TeamsApi.md#create_team) | **POST** /teams | Create a team
*TeamsApi* | [**get_team**](docs/TeamsApi.md#get_team) | **GET** /teams/{team_gid} | Get a team
*TeamsApi* | [**get_teams_for_user**](docs/TeamsApi.md#get_teams_for_user) | **GET** /users/{user_gid}/teams | Get teams for a user
*TeamsApi* | [**get_teams_for_workspace**](docs/TeamsApi.md#get_teams_for_workspace) | **GET** /workspaces/{workspace_gid}/teams | Get teams in a workspace
*TeamsApi* | [**remove_user_for_team**](docs/TeamsApi.md#remove_user_for_team) | **POST** /teams/{team_gid}/removeUser | Remove a user from a team
*TeamsApi* | [**update_team**](docs/TeamsApi.md#update_team) | **PUT** /teams | Update a team
*TimePeriodsApi* | [**get_time_period**](docs/TimePeriodsApi.md#get_time_period) | **GET** /time_periods/{time_period_gid} | Get a time period
*TimePeriodsApi* | [**get_time_periods**](docs/TimePeriodsApi.md#get_time_periods) | **GET** /time_periods | Get time periods
*TimeTrackingEntriesApi* | [**create_time_tracking_entry**](docs/TimeTrackingEntriesApi.md#create_time_tracking_entry) | **POST** /tasks/{task_gid}/time_tracking_entries | Create a time tracking entry
*TimeTrackingEntriesApi* | [**delete_time_tracking_entry**](docs/TimeTrackingEntriesApi.md#delete_time_tracking_entry) | **DELETE** /time_tracking_entries/{time_tracking_entry_gid} | Delete a time tracking entry
*TimeTrackingEntriesApi* | [**get_time_tracking_entries_for_task**](docs/TimeTrackingEntriesApi.md#get_time_tracking_entries_for_task) | **GET** /tasks/{task_gid}/time_tracking_entries | Get time tracking entries for a task
*TimeTrackingEntriesApi* | [**get_time_tracking_entry**](docs/TimeTrackingEntriesApi.md#get_time_tracking_entry) | **GET** /time_tracking_entries/{time_tracking_entry_gid} | Get a time tracking entry
*TimeTrackingEntriesApi* | [**update_time_tracking_entry**](docs/TimeTrackingEntriesApi.md#update_time_tracking_entry) | **PUT** /time_tracking_entries/{time_tracking_entry_gid} | Update a time tracking entry
*TypeaheadApi* | [**typeahead_for_workspace**](docs/TypeaheadApi.md#typeahead_for_workspace) | **GET** /workspaces/{workspace_gid}/typeahead | Get objects via typeahead
*UserTaskListsApi* | [**get_user_task_list**](docs/UserTaskListsApi.md#get_user_task_list) | **GET** /user_task_lists/{user_task_list_gid} | Get a user task list
*UserTaskListsApi* | [**get_user_task_list_for_user**](docs/UserTaskListsApi.md#get_user_task_list_for_user) | **GET** /users/{user_gid}/user_task_list | Get a user&#39;s task list
*UsersApi* | [**get_favorites_for_user**](docs/UsersApi.md#get_favorites_for_user) | **GET** /users/{user_gid}/favorites | Get a user&#39;s favorites
*UsersApi* | [**get_user**](docs/UsersApi.md#get_user) | **GET** /users/{user_gid} | Get a user
*UsersApi* | [**get_users**](docs/UsersApi.md#get_users) | **GET** /users | Get multiple users
*UsersApi* | [**get_users_for_team**](docs/UsersApi.md#get_users_for_team) | **GET** /teams/{team_gid}/users | Get users in a team
*UsersApi* | [**get_users_for_workspace**](docs/UsersApi.md#get_users_for_workspace) | **GET** /workspaces/{workspace_gid}/users | Get users in a workspace or organization
*WebhooksApi* | [**create_webhook**](docs/WebhooksApi.md#create_webhook) | **POST** /webhooks | Establish a webhook
*WebhooksApi* | [**delete_webhook**](docs/WebhooksApi.md#delete_webhook) | **DELETE** /webhooks/{webhook_gid} | Delete a webhook
*WebhooksApi* | [**get_webhook**](docs/WebhooksApi.md#get_webhook) | **GET** /webhooks/{webhook_gid} | Get a webhook
*WebhooksApi* | [**get_webhooks**](docs/WebhooksApi.md#get_webhooks) | **GET** /webhooks | Get multiple webhooks
*WebhooksApi* | [**update_webhook**](docs/WebhooksApi.md#update_webhook) | **PUT** /webhooks/{webhook_gid} | Update a webhook
*WorkspaceMembershipsApi* | [**get_workspace_membership**](docs/WorkspaceMembershipsApi.md#get_workspace_membership) | **GET** /workspace_memberships/{workspace_membership_gid} | Get a workspace membership
*WorkspaceMembershipsApi* | [**get_workspace_memberships_for_user**](docs/WorkspaceMembershipsApi.md#get_workspace_memberships_for_user) | **GET** /users/{user_gid}/workspace_memberships | Get workspace memberships for a user
*WorkspaceMembershipsApi* | [**get_workspace_memberships_for_workspace**](docs/WorkspaceMembershipsApi.md#get_workspace_memberships_for_workspace) | **GET** /workspaces/{workspace_gid}/workspace_memberships | Get the workspace memberships for a workspace
*WorkspacesApi* | [**add_user_for_workspace**](docs/WorkspacesApi.md#add_user_for_workspace) | **POST** /workspaces/{workspace_gid}/addUser | Add a user to a workspace or organization
*WorkspacesApi* | [**get_workspace**](docs/WorkspacesApi.md#get_workspace) | **GET** /workspaces/{workspace_gid} | Get a workspace
*WorkspacesApi* | [**get_workspaces**](docs/WorkspacesApi.md#get_workspaces) | **GET** /workspaces | Get multiple workspaces
*WorkspacesApi* | [**remove_user_for_workspace**](docs/WorkspacesApi.md#remove_user_for_workspace) | **POST** /workspaces/{workspace_gid}/removeUser | Remove a user from a workspace or organization
*WorkspacesApi* | [**update_workspace**](docs/WorkspacesApi.md#update_workspace) | **PUT** /workspaces/{workspace_gid} | Update a workspace



[pypi-url]: https://pypi.python.org/pypi/asana-preview/
[pypi-image]: https://img.shields.io/pypi/v/asana-preview.svg?style=flat-square
