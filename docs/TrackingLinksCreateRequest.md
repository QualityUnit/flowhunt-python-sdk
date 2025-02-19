# TrackingLinksCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**List[TrackingLinkCreateRequest]**](TrackingLinkCreateRequest.md) | The list of links to be created | 
**with_address** | **bool** |  | [optional] 
**unique_id** | **str** |  | [optional] 
**fp** | **str** |  | [optional] 
**session_id** | **str** |  | [optional] 
**ga** | **str** |  | [optional] 

## Example

```python
from flowhunt.models.tracking_links_create_request import TrackingLinksCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TrackingLinksCreateRequest from a JSON string
tracking_links_create_request_instance = TrackingLinksCreateRequest.from_json(json)
# print the JSON string representation of the object
print(TrackingLinksCreateRequest.to_json())

# convert the object into a dict
tracking_links_create_request_dict = tracking_links_create_request_instance.to_dict()
# create an instance of TrackingLinksCreateRequest from a dict
tracking_links_create_request_from_dict = TrackingLinksCreateRequest.from_dict(tracking_links_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


