# SerpClusterGroupSearchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**search** | **str** |  | [optional] 
**customer_id** | **str** |  | [optional] 
**campaign_id** | **str** |  | [optional] 
**group_id** | **str** |  | [optional] 
**include_negative_keywords** | **bool** |  | [optional] 

## Example

```python
from flowhunt.models.serp_cluster_group_search_request import SerpClusterGroupSearchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SerpClusterGroupSearchRequest from a JSON string
serp_cluster_group_search_request_instance = SerpClusterGroupSearchRequest.from_json(json)
# print the JSON string representation of the object
print(SerpClusterGroupSearchRequest.to_json())

# convert the object into a dict
serp_cluster_group_search_request_dict = serp_cluster_group_search_request_instance.to_dict()
# create an instance of SerpClusterGroupSearchRequest from a dict
serp_cluster_group_search_request_from_dict = SerpClusterGroupSearchRequest.from_dict(serp_cluster_group_search_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


