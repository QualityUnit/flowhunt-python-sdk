# FlowCronSearchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**FlowCronStatus**](FlowCronStatus.md) |  | [optional] 
**next_run_to** | **datetime** |  | [optional] 
**next_run_from** | **datetime** |  | [optional] 
**last_run_to** | **datetime** |  | [optional] 
**last_run_from** | **datetime** |  | [optional] 
**flow_id** | **str** |  | [optional] 
**cron_name** | **str** |  | [optional] 

## Example

```python
from flowhunt.models.flow_cron_search_request import FlowCronSearchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FlowCronSearchRequest from a JSON string
flow_cron_search_request_instance = FlowCronSearchRequest.from_json(json)
# print the JSON string representation of the object
print(FlowCronSearchRequest.to_json())

# convert the object into a dict
flow_cron_search_request_dict = flow_cron_search_request_instance.to_dict()
# create an instance of FlowCronSearchRequest from a dict
flow_cron_search_request_from_dict = FlowCronSearchRequest.from_dict(flow_cron_search_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


