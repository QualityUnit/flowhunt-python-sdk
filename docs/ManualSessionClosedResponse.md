# ManualSessionClosedResponse

Response from manually firing the SessionClosed trigger.  Mirrors the contract of ``invoke_session_flow``: V3 is async, so this returns immediately with PENDING status and a ``run_id`` the frontend uses to subscribe to streamed events that render the close-session branch output.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**flow_id** | **str** | The flow that was fired | 
**session_id** | **str** | The session that was closed | 
**run_id** | **str** | Run ID of the close-session execution; subscribe to the session event stream to watch its output | [optional] 
**response_status** | [**FlowSessionStatus**](FlowSessionStatus.md) | Status of the close-session invocation | 
**error_message** | **str** | Error description on failed status | [optional] 

## Example

```python
from flowhunt.models.manual_session_closed_response import ManualSessionClosedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ManualSessionClosedResponse from a JSON string
manual_session_closed_response_instance = ManualSessionClosedResponse.from_json(json)
# print the JSON string representation of the object
print(ManualSessionClosedResponse.to_json())

# convert the object into a dict
manual_session_closed_response_dict = manual_session_closed_response_instance.to_dict()
# create an instance of ManualSessionClosedResponse from a dict
manual_session_closed_response_from_dict = ManualSessionClosedResponse.from_dict(manual_session_closed_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


