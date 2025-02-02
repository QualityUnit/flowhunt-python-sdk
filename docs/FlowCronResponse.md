# FlowCronResponse

Flow cron response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**flow_id** | **str** |  | 
**cron_id** | **str** |  | 
**last_run** | **datetime** |  | [optional] 
**next_run** | **datetime** |  | [optional] 
**status** | [**FlowCronStatus**](FlowCronStatus.md) |  | 
**input_text** | **str** |  | [optional] 
**interval_settings** | **str** |  | 
**variables** | **object** |  | [optional] 

## Example

```python
from flowhunt.models.flow_cron_response import FlowCronResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FlowCronResponse from a JSON string
flow_cron_response_instance = FlowCronResponse.from_json(json)
# print the JSON string representation of the object
print(FlowCronResponse.to_json())

# convert the object into a dict
flow_cron_response_dict = flow_cron_response_instance.to_dict()
# create an instance of FlowCronResponse from a dict
flow_cron_response_from_dict = FlowCronResponse.from_dict(flow_cron_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


