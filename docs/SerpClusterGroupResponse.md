# SerpClusterGroupResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_id** | **str** | Group ID | [optional] [default to '']
**group_name** | **str** | Group name | [optional] [default to '']

## Example

```python
from flowhunt.models.serp_cluster_group_response import SerpClusterGroupResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SerpClusterGroupResponse from a JSON string
serp_cluster_group_response_instance = SerpClusterGroupResponse.from_json(json)
# print the JSON string representation of the object
print(SerpClusterGroupResponse.to_json())

# convert the object into a dict
serp_cluster_group_response_dict = serp_cluster_group_response_instance.to_dict()
# create an instance of SerpClusterGroupResponse from a dict
serp_cluster_group_response_from_dict = SerpClusterGroupResponse.from_dict(serp_cluster_group_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


