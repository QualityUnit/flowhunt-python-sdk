# SerpClusterQueryResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query_id** | **str** | Query ID | 
**query** | **str** | Query | 
**country** | **str** |  | [optional] 
**language** | **str** |  | [optional] 
**location** | **str** |  | [optional] 

## Example

```python
from flowhunt.models.serp_cluster_query_response import SerpClusterQueryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SerpClusterQueryResponse from a JSON string
serp_cluster_query_response_instance = SerpClusterQueryResponse.from_json(json)
# print the JSON string representation of the object
print(SerpClusterQueryResponse.to_json())

# convert the object into a dict
serp_cluster_query_response_dict = serp_cluster_query_response_instance.to_dict()
# create an instance of SerpClusterQueryResponse from a dict
serp_cluster_query_response_from_dict = SerpClusterQueryResponse.from_dict(serp_cluster_query_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


