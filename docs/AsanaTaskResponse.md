# AsanaTaskResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**task_gid** | **str** |  | 
**task_name** | **str** |  | 
**completed** | **bool** |  | [optional] 
**due_on** | **str** |  | [optional] 
**notes** | **str** |  | [optional] 
**assignee_name** | **str** |  | [optional] 

## Example

```python
from flowhunt.models.asana_task_response import AsanaTaskResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AsanaTaskResponse from a JSON string
asana_task_response_instance = AsanaTaskResponse.from_json(json)
# print the JSON string representation of the object
print(AsanaTaskResponse.to_json())

# convert the object into a dict
asana_task_response_dict = asana_task_response_instance.to_dict()
# create an instance of AsanaTaskResponse from a dict
asana_task_response_from_dict = AsanaTaskResponse.from_dict(asana_task_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


