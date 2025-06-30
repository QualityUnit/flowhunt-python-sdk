# FlowDetailResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Flow ID | 
**name** | **str** | Flow name | 
**description** | **str** | Flow description | 
**detailed_description** | **str** |  | [optional] 
**config** | [**FlowConfig**](FlowConfig.md) | Flow configuration | 
**flow_type** | [**FlowType**](FlowType.md) | Flow type | 
**executed_at** | **datetime** |  | [optional] 
**category_id** | **str** |  | [optional] 
**branch** | **str** | Flow branch | 
**enable_cache** | **bool** | Enable cache | 
**draft_version_nr** | **int** |  | [optional] 
**prod_version_nr** | **int** |  | [optional] 

## Example

```python
from flowhunt.models.flow_detail_response import FlowDetailResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FlowDetailResponse from a JSON string
flow_detail_response_instance = FlowDetailResponse.from_json(json)
# print the JSON string representation of the object
print(FlowDetailResponse.to_json())

# convert the object into a dict
flow_detail_response_dict = flow_detail_response_instance.to_dict()
# create an instance of FlowDetailResponse from a dict
flow_detail_response_from_dict = FlowDetailResponse.from_dict(flow_detail_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


