# InferenceHistorySearchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**from_date** | **datetime** | From date | [optional] 
**to_date** | **datetime** | To date | [optional] 
**limit** | **int** | The number of results to return | [optional] [default to 10]
**search_after** | **List[object]** | The search_after parameter for pagination (contains sort values from previous page) | [optional] 
**base_model** | [**BaseFoundationModel**](BaseFoundationModel.md) | The base model to filter by | [optional] 
**style** | **str** | The style to filter by | [optional] 
**effect** | **str** | The effect to filter by | [optional] 
**aspect_ratio** | [**AspecRatio**](AspecRatio.md) | The aspect ratio to filter by | [optional] 

## Example

```python
from flowhunt.models.inference_history_search_request import InferenceHistorySearchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InferenceHistorySearchRequest from a JSON string
inference_history_search_request_instance = InferenceHistorySearchRequest.from_json(json)
# print the JSON string representation of the object
print(InferenceHistorySearchRequest.to_json())

# convert the object into a dict
inference_history_search_request_dict = inference_history_search_request_instance.to_dict()
# create an instance of InferenceHistorySearchRequest from a dict
inference_history_search_request_from_dict = InferenceHistorySearchRequest.from_dict(inference_history_search_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


