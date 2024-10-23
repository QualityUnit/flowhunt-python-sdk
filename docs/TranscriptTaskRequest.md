# TranscriptTaskRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**task_id** | **str** | The task ID to get the transcript from | 

## Example

```python
from flowhunt.models.transcript_task_request import TranscriptTaskRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TranscriptTaskRequest from a JSON string
transcript_task_request_instance = TranscriptTaskRequest.from_json(json)
# print the JSON string representation of the object
print(TranscriptTaskRequest.to_json())

# convert the object into a dict
transcript_task_request_dict = transcript_task_request_instance.to_dict()
# create an instance of TranscriptTaskRequest from a dict
transcript_task_request_from_dict = TranscriptTaskRequest.from_dict(transcript_task_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


