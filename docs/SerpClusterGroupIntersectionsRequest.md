# SerpClusterGroupIntersectionsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_id** | **int** | Customer ID of cluster | 
**campaign_id** | **int** |  | [optional] 
**group_id** | **int** |  | [optional] 
**min_cluster_strength** | **int** |  | [optional] 
**suggest_other_matching_keywords** | **bool** |  | [optional] 

## Example

```python
from flowhunt.models.serp_cluster_group_intersections_request import SerpClusterGroupIntersectionsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SerpClusterGroupIntersectionsRequest from a JSON string
serp_cluster_group_intersections_request_instance = SerpClusterGroupIntersectionsRequest.from_json(json)
# print the JSON string representation of the object
print(SerpClusterGroupIntersectionsRequest.to_json())

# convert the object into a dict
serp_cluster_group_intersections_request_dict = serp_cluster_group_intersections_request_instance.to_dict()
# create an instance of SerpClusterGroupIntersectionsRequest from a dict
serp_cluster_group_intersections_request_from_dict = SerpClusterGroupIntersectionsRequest.from_dict(serp_cluster_group_intersections_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


