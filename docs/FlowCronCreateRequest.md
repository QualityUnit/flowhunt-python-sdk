# FlowCronCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**flow_id** | **str** |  | 
**status** | [**FlowCronStatus**](FlowCronStatus.md) |  | 
**input_text** | **str** |  | [optional] 
**variables** | **Dict[str, object]** |  | [optional] 
**interval_settings** | **str** |  | 
**cron_name** | **str** |  | 

## Example

```python
from flowhunt.models.flow_cron_create_request import FlowCronCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FlowCronCreateRequest from a JSON string
flow_cron_create_request_instance = FlowCronCreateRequest.from_json(json)
# print the JSON string representation of the object
print(FlowCronCreateRequest.to_json())

# convert the object into a dict
flow_cron_create_request_dict = flow_cron_create_request_instance.to_dict()
# create an instance of FlowCronCreateRequest from a dict
flow_cron_create_request_from_dict = FlowCronCreateRequest.from_dict(flow_cron_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


