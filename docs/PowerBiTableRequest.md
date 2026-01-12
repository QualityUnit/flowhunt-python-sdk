# PowerBiTableRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workspace_pbi_id** | **str** | Power BI workspace ID | [optional] 
**dataset_id** | **str** | Power BI dataset ID | [optional] 

## Example

```python
from flowhunt.models.power_bi_table_request import PowerBiTableRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PowerBiTableRequest from a JSON string
power_bi_table_request_instance = PowerBiTableRequest.from_json(json)
# print the JSON string representation of the object
print(PowerBiTableRequest.to_json())

# convert the object into a dict
power_bi_table_request_dict = power_bi_table_request_instance.to_dict()
# create an instance of PowerBiTableRequest from a dict
power_bi_table_request_from_dict = PowerBiTableRequest.from_dict(power_bi_table_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


