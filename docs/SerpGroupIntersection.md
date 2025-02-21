# SerpGroupIntersection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workspace_id** | **str** |  | 
**customer_id** | **str** |  | 
**campaign_id** | **str** |  | 
**group_id** | **str** |  | 
**unique_group_id** | **str** |  | [optional] 
**intersections_count** | **int** |  | 

## Example

```python
from flowhunt.models.serp_group_intersection import SerpGroupIntersection

# TODO update the JSON string below
json = "{}"
# create an instance of SerpGroupIntersection from a JSON string
serp_group_intersection_instance = SerpGroupIntersection.from_json(json)
# print the JSON string representation of the object
print(SerpGroupIntersection.to_json())

# convert the object into a dict
serp_group_intersection_dict = serp_group_intersection_instance.to_dict()
# create an instance of SerpGroupIntersection from a dict
serp_group_intersection_from_dict = SerpGroupIntersection.from_dict(serp_group_intersection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


