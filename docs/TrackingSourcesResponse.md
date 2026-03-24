# TrackingSourcesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sources** | [**List[TrackingSourceResponse]**](TrackingSourceResponse.md) |  | 

## Example

```python
from flowhunt.models.tracking_sources_response import TrackingSourcesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TrackingSourcesResponse from a JSON string
tracking_sources_response_instance = TrackingSourcesResponse.from_json(json)
# print the JSON string representation of the object
print(TrackingSourcesResponse.to_json())

# convert the object into a dict
tracking_sources_response_dict = tracking_sources_response_instance.to_dict()
# create an instance of TrackingSourcesResponse from a dict
tracking_sources_response_from_dict = TrackingSourcesResponse.from_dict(tracking_sources_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


