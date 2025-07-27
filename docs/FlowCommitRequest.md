# FlowCommitRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**commit_title** | **str** |  | [optional] 

## Example

```python
from flowhunt.models.flow_commit_request import FlowCommitRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FlowCommitRequest from a JSON string
flow_commit_request_instance = FlowCommitRequest.from_json(json)
# print the JSON string representation of the object
print(FlowCommitRequest.to_json())

# convert the object into a dict
flow_commit_request_dict = flow_commit_request_instance.to_dict()
# create an instance of FlowCommitRequest from a dict
flow_commit_request_from_dict = FlowCommitRequest.from_dict(flow_commit_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


