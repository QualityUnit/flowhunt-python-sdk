# MicrosoftPowerBiDatasetResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dataset_id** | **str** | Dataset ID | 
**dataset_name** | **str** | Dataset name | 

## Example

```python
from flowhunt.models.microsoft_power_bi_dataset_response import MicrosoftPowerBiDatasetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MicrosoftPowerBiDatasetResponse from a JSON string
microsoft_power_bi_dataset_response_instance = MicrosoftPowerBiDatasetResponse.from_json(json)
# print the JSON string representation of the object
print(MicrosoftPowerBiDatasetResponse.to_json())

# convert the object into a dict
microsoft_power_bi_dataset_response_dict = microsoft_power_bi_dataset_response_instance.to_dict()
# create an instance of MicrosoftPowerBiDatasetResponse from a dict
microsoft_power_bi_dataset_response_from_dict = MicrosoftPowerBiDatasetResponse.from_dict(microsoft_power_bi_dataset_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


