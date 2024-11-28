# SerpClusterQueryIntersectionsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**post_back_url** | **str** |  | [optional] 
**query** | **str** |  | [optional] 
**country** | **str** |  | [optional] 
**language** | **str** |  | [optional] 
**location** | **str** |  | [optional] 
**group_name** | **str** | Group name of cluster | [optional] [default to '']
**group_id** | **str** |  | [optional] 
**live_mode** | **bool** |  | [optional] 
**max_position** | **int** |  | [optional] 

## Example

```python
from flowhunt.models.serp_cluster_query_intersections_request import SerpClusterQueryIntersectionsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SerpClusterQueryIntersectionsRequest from a JSON string
serp_cluster_query_intersections_request_instance = SerpClusterQueryIntersectionsRequest.from_json(json)
# print the JSON string representation of the object
print(SerpClusterQueryIntersectionsRequest.to_json())

# convert the object into a dict
serp_cluster_query_intersections_request_dict = serp_cluster_query_intersections_request_instance.to_dict()
# create an instance of SerpClusterQueryIntersectionsRequest from a dict
serp_cluster_query_intersections_request_from_dict = SerpClusterQueryIntersectionsRequest.from_dict(serp_cluster_query_intersections_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


