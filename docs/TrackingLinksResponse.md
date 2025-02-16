# TrackingLinksResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**List[TrackingLinkResponse]**](TrackingLinkResponse.md) |  | 

## Example

```python
from flowhunt.models.tracking_links_response import TrackingLinksResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TrackingLinksResponse from a JSON string
tracking_links_response_instance = TrackingLinksResponse.from_json(json)
# print the JSON string representation of the object
print(TrackingLinksResponse.to_json())

# convert the object into a dict
tracking_links_response_dict = tracking_links_response_instance.to_dict()
# create an instance of TrackingLinksResponse from a dict
tracking_links_response_from_dict = TrackingLinksResponse.from_dict(tracking_links_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


