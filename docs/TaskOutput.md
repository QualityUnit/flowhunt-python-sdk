# TaskOutput

Class that represents the result of a task.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Description of the task | 
**name** | **str** |  | [optional] 
**expected_output** | **str** |  | [optional] 
**summary** | **str** |  | [optional] 
**raw** | **str** | Raw output of the task | [optional] [default to '']
**pydantic** | **object** |  | [optional] 
**json_dict** | **Dict[str, object]** |  | [optional] 
**agent** | **str** | Agent that executed the task | 
**output_format** | [**OutputFormat**](OutputFormat.md) | Output format of the task | [optional] 

## Example

```python
from flowhunt.models.task_output import TaskOutput

# TODO update the JSON string below
json = "{}"
# create an instance of TaskOutput from a JSON string
task_output_instance = TaskOutput.from_json(json)
# print the JSON string representation of the object
print(TaskOutput.to_json())

# convert the object into a dict
task_output_dict = task_output_instance.to_dict()
# create an instance of TaskOutput from a dict
task_output_from_dict = TaskOutput.from_dict(task_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


