# SerpClusterAddGroupRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_name** | **str** | Group name of cluster | [optional] [default to '']
**group_id** | **str** |  | [optional] 

## Example

```python
from flowhunt.models.serp_cluster_add_group_request import SerpClusterAddGroupRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SerpClusterAddGroupRequest from a JSON string
serp_cluster_add_group_request_instance = SerpClusterAddGroupRequest.from_json(json)
# print the JSON string representation of the object
print(SerpClusterAddGroupRequest.to_json())

# convert the object into a dict
serp_cluster_add_group_request_dict = serp_cluster_add_group_request_instance.to_dict()
# create an instance of SerpClusterAddGroupRequest from a dict
serp_cluster_add_group_request_from_dict = SerpClusterAddGroupRequest.from_dict(serp_cluster_add_group_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


