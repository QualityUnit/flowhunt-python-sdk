# FlowCronUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**FlowCronStatus**](FlowCronStatus.md) |  | [optional] 
**input_text** | **str** |  | [optional] 
**variables** | **Dict[str, object]** |  | [optional] 
**interval_settings** | **str** |  | [optional] 
**cron_name** | **str** |  | [optional] 

## Example

```python
from flowhunt.models.flow_cron_update_request import FlowCronUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FlowCronUpdateRequest from a JSON string
flow_cron_update_request_instance = FlowCronUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(FlowCronUpdateRequest.to_json())

# convert the object into a dict
flow_cron_update_request_dict = flow_cron_update_request_instance.to_dict()
# create an instance of FlowCronUpdateRequest from a dict
flow_cron_update_request_from_dict = FlowCronUpdateRequest.from_dict(flow_cron_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


