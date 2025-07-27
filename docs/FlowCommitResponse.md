# FlowCommitResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**commit_title** | **str** |  | [optional] 

## Example

```python
from flowhunt.models.flow_commit_response import FlowCommitResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FlowCommitResponse from a JSON string
flow_commit_response_instance = FlowCommitResponse.from_json(json)
# print the JSON string representation of the object
print(FlowCommitResponse.to_json())

# convert the object into a dict
flow_commit_response_dict = flow_commit_response_instance.to_dict()
# create an instance of FlowCommitResponse from a dict
flow_commit_response_from_dict = FlowCommitResponse.from_dict(flow_commit_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


