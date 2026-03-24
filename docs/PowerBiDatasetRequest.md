# PowerBiDatasetRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workspace_pbi_id** | **str** | Power BI workspace ID | [optional] 

## Example

```python
from flowhunt.models.power_bi_dataset_request import PowerBiDatasetRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PowerBiDatasetRequest from a JSON string
power_bi_dataset_request_instance = PowerBiDatasetRequest.from_json(json)
# print the JSON string representation of the object
print(PowerBiDatasetRequest.to_json())

# convert the object into a dict
power_bi_dataset_request_dict = power_bi_dataset_request_instance.to_dict()
# create an instance of PowerBiDatasetRequest from a dict
power_bi_dataset_request_from_dict = PowerBiDatasetRequest.from_dict(power_bi_dataset_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


