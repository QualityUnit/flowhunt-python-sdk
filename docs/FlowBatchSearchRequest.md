# FlowBatchSearchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rows_limit** | **int** | Maximum number of rows to return | [optional] [default to 50]
**rows_cursor** | **int** | Starting row_index for pagination | [optional] 
**rows_status** | [**FlowBatchRowStatus**](FlowBatchRowStatus.md) | Filter rows by status | [optional] 

## Example

```python
from flowhunt.models.flow_batch_search_request import FlowBatchSearchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FlowBatchSearchRequest from a JSON string
flow_batch_search_request_instance = FlowBatchSearchRequest.from_json(json)
# print the JSON string representation of the object
print(FlowBatchSearchRequest.to_json())

# convert the object into a dict
flow_batch_search_request_dict = flow_batch_search_request_instance.to_dict()
# create an instance of FlowBatchSearchRequest from a dict
flow_batch_search_request_from_dict = FlowBatchSearchRequest.from_dict(flow_batch_search_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


