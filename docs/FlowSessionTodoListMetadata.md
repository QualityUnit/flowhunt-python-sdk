# FlowSessionTodoListMetadata

Metadata for agent todo list updates.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**todo_id** | **str** | Unique todo list identifier for updates | 
**todos** | [**List[TodoItem]**](TodoItem.md) | List of todo items | 

## Example

```python
from flowhunt.models.flow_session_todo_list_metadata import FlowSessionTodoListMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of FlowSessionTodoListMetadata from a JSON string
flow_session_todo_list_metadata_instance = FlowSessionTodoListMetadata.from_json(json)
# print the JSON string representation of the object
print(FlowSessionTodoListMetadata.to_json())

# convert the object into a dict
flow_session_todo_list_metadata_dict = flow_session_todo_list_metadata_instance.to_dict()
# create an instance of FlowSessionTodoListMetadata from a dict
flow_session_todo_list_metadata_from_dict = FlowSessionTodoListMetadata.from_dict(flow_session_todo_list_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


