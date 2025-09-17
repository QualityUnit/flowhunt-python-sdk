# MicrosoftPowerBiPushDatasetResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workspace_pbi_id** | **str** | Power BI workspace ID | 
**dataset_id** | **str** | Dataset ID | 
**table_name** | **str** | Table name | 

## Example

```python
from flowhunt.models.microsoft_power_bi_push_dataset_response import MicrosoftPowerBiPushDatasetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MicrosoftPowerBiPushDatasetResponse from a JSON string
microsoft_power_bi_push_dataset_response_instance = MicrosoftPowerBiPushDatasetResponse.from_json(json)
# print the JSON string representation of the object
print(MicrosoftPowerBiPushDatasetResponse.to_json())

# convert the object into a dict
microsoft_power_bi_push_dataset_response_dict = microsoft_power_bi_push_dataset_response_instance.to_dict()
# create an instance of MicrosoftPowerBiPushDatasetResponse from a dict
microsoft_power_bi_push_dataset_response_from_dict = MicrosoftPowerBiPushDatasetResponse.from_dict(microsoft_power_bi_push_dataset_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


