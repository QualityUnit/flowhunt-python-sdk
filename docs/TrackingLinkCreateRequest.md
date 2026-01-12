# TrackingLinkCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**src_link_id** | **str** | The source link ID | 
**dst_link_id** | **str** | The destination link ID | 
**valid_until** | **datetime** | The date until the link is valid | [optional] 

## Example

```python
from flowhunt.models.tracking_link_create_request import TrackingLinkCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TrackingLinkCreateRequest from a JSON string
tracking_link_create_request_instance = TrackingLinkCreateRequest.from_json(json)
# print the JSON string representation of the object
print(TrackingLinkCreateRequest.to_json())

# convert the object into a dict
tracking_link_create_request_dict = tracking_link_create_request_instance.to_dict()
# create an instance of TrackingLinkCreateRequest from a dict
tracking_link_create_request_from_dict = TrackingLinkCreateRequest.from_dict(tracking_link_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


