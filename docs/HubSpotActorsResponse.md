# HubSpotActorsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actors** | [**List[HubSpotActorIdResponse]**](HubSpotActorIdResponse.md) |  | 

## Example

```python
from flowhunt.models.hub_spot_actors_response import HubSpotActorsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of HubSpotActorsResponse from a JSON string
hub_spot_actors_response_instance = HubSpotActorsResponse.from_json(json)
# print the JSON string representation of the object
print(HubSpotActorsResponse.to_json())

# convert the object into a dict
hub_spot_actors_response_dict = hub_spot_actors_response_instance.to_dict()
# create an instance of HubSpotActorsResponse from a dict
hub_spot_actors_response_from_dict = HubSpotActorsResponse.from_dict(hub_spot_actors_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


