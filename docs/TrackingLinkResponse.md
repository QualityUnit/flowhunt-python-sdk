# TrackingLinkResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**src_link_id** | **str** |  | 
**dst_link_id** | **str** |  | 
**created_at** | **datetime** |  | [optional] 
**valid_until** | **datetime** |  | [optional] 

## Example

```python
from flowhunt.models.tracking_link_response import TrackingLinkResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TrackingLinkResponse from a JSON string
tracking_link_response_instance = TrackingLinkResponse.from_json(json)
# print the JSON string representation of the object
print(TrackingLinkResponse.to_json())

# convert the object into a dict
tracking_link_response_dict = tracking_link_response_instance.to_dict()
# create an instance of TrackingLinkResponse from a dict
tracking_link_response_from_dict = TrackingLinkResponse.from_dict(tracking_link_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


