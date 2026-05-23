# HITLRespondRequest

Request body for HITL tool approval response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hitl_id** | **str** | HITL request ID | 
**approved** | **bool** | Whether the tool call is approved | 
**approve_future** | **bool** | Permanently approve this tool for the project | [optional] [default to False]
**rejection_reason** | **str** | Reason for rejection | [optional] [default to '']

## Example

```python
from flowhunt.models.hitl_respond_request import HITLRespondRequest

# TODO update the JSON string below
json = "{}"
# create an instance of HITLRespondRequest from a JSON string
hitl_respond_request_instance = HITLRespondRequest.from_json(json)
# print the JSON string representation of the object
print(HITLRespondRequest.to_json())

# convert the object into a dict
hitl_respond_request_dict = hitl_respond_request_instance.to_dict()
# create an instance of HITLRespondRequest from a dict
hitl_respond_request_from_dict = HITLRespondRequest.from_dict(hitl_respond_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


