# PowerBiPushDatasetRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workspace_pbi_id** | **str** |  | [optional] 
**dataset_name** | **str** |  | [optional] 
**table_name** | **str** |  | [optional] 

## Example

```python
from flowhunt.models.power_bi_push_dataset_request import PowerBiPushDatasetRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PowerBiPushDatasetRequest from a JSON string
power_bi_push_dataset_request_instance = PowerBiPushDatasetRequest.from_json(json)
# print the JSON string representation of the object
print(PowerBiPushDatasetRequest.to_json())

# convert the object into a dict
power_bi_push_dataset_request_dict = power_bi_push_dataset_request_instance.to_dict()
# create an instance of PowerBiPushDatasetRequest from a dict
power_bi_push_dataset_request_from_dict = PowerBiPushDatasetRequest.from_dict(power_bi_push_dataset_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


