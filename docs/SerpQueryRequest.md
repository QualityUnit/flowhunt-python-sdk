# SerpQueryRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**post_back_url** | **str** |  | [optional] 
**query** | **str** |  | [optional] 
**country** | **str** |  | [optional] 
**language** | **str** |  | [optional] 
**location** | **str** |  | [optional] 

## Example

```python
from flowhunt.models.serp_query_request import SerpQueryRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SerpQueryRequest from a JSON string
serp_query_request_instance = SerpQueryRequest.from_json(json)
# print the JSON string representation of the object
print(SerpQueryRequest.to_json())

# convert the object into a dict
serp_query_request_dict = serp_query_request_instance.to_dict()
# create an instance of SerpQueryRequest from a dict
serp_query_request_from_dict = SerpQueryRequest.from_dict(serp_query_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


