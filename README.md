# asana-preview [![PyPi Version][pypi-image]][pypi-url]

This is a [preview version](https://forum.asana.com/t/try-an-early-preview-of-our-new-node-js-and-python-sdks/394881) of Asana's new python client library. For feedback and feature requests, please leave a comment on [this forum thread](https://forum.asana.com/t/try-an-early-preview-of-our-new-node-js-and-python-sdks/394881) or through [the feedback form on our documentation site](https://form-beta.asana.com/?k=C4sELCq6hAUsoWEY0kJwAA&d=15793206719)

- Package version: 1.0.4

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

# Configure Bearer authorization: personal_access_token
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
*EventsApi* | [**get_events**](docs/EventsApi.md#get_events) | **GET** /events | Get events on a resource
*ProjectsApi* | [**get_project**](docs/ProjectsApi.md#get_project) | **GET** /projects/{project_gid} | Get a project
*ProjectsApi* | [**get_projects**](docs/ProjectsApi.md#get_projects) | **GET** /projects | Get multiple projects
*SectionsApi* | [**get_sections_for_project**](docs/SectionsApi.md#get_sections_for_project) | **GET** /projects/{project_gid}/sections | Get sections in a project
*StoriesApi* | [**get_stories_for_task**](docs/StoriesApi.md#get_stories_for_task) | **GET** /tasks/{task_gid}/stories | Get stories from a task
*TasksApi* | [**get_subtasks_for_task**](docs/TasksApi.md#get_subtasks_for_task) | **GET** /tasks/{task_gid}/subtasks | Get subtasks from a task
*TasksApi* | [**get_task**](docs/TasksApi.md#get_task) | **GET** /tasks/{task_gid} | Get a task
*TasksApi* | [**get_tasks**](docs/TasksApi.md#get_tasks) | **GET** /tasks | Get multiple tasks
*TasksApi* | [**get_tasks_for_project**](docs/TasksApi.md#get_tasks_for_project) | **GET** /projects/{project_gid}/tasks | Get tasks from a project
*UsersApi* | [**get_user**](docs/UsersApi.md#get_user) | **GET** /users/{user_gid} | Get a user



[pypi-url]: https://pypi.python.org/pypi/asana-preview/
[pypi-image]: https://img.shields.io/pypi/v/asana-preview.svg?style=flat-square
