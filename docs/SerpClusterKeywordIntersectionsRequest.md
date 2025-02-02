# SerpClusterKeywordIntersectionsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**keyword_id** | **str** |  | [optional] 
**keyword** | **str** | Keyword to search | 
**language** | **str** |  | [optional] 
**country** | **str** |  | [optional] 
**search_engine** | [**SerpSearchEngineType**](SerpSearchEngineType.md) |  | [optional] 
**customer_id** | **int** | Customer ID of cluster | 
**campaign_id** | **int** |  | [optional] 
**group_id** | **int** |  | [optional] 
**min_cluster_strength** | **int** |  | [optional] 

## Example

```python
from flowhunt.models.serp_cluster_keyword_intersections_request import SerpClusterKeywordIntersectionsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SerpClusterKeywordIntersectionsRequest from a JSON string
serp_cluster_keyword_intersections_request_instance = SerpClusterKeywordIntersectionsRequest.from_json(json)
# print the JSON string representation of the object
print(SerpClusterKeywordIntersectionsRequest.to_json())

# convert the object into a dict
serp_cluster_keyword_intersections_request_dict = serp_cluster_keyword_intersections_request_instance.to_dict()
# create an instance of SerpClusterKeywordIntersectionsRequest from a dict
serp_cluster_keyword_intersections_request_from_dict = SerpClusterKeywordIntersectionsRequest.from_dict(serp_cluster_keyword_intersections_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


