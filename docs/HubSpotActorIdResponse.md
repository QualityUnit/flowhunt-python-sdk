# HubSpotActorIdResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actor_id** | **str** | Actor ID | 
**actor_email** | **str** | Actor Email | 

## Example

```python
from flowhunt.models.hub_spot_actor_id_response import HubSpotActorIdResponse

# TODO update the JSON string below
json = "{}"
# create an instance of HubSpotActorIdResponse from a JSON string
hub_spot_actor_id_response_instance = HubSpotActorIdResponse.from_json(json)
# print the JSON string representation of the object
print(HubSpotActorIdResponse.to_json())

# convert the object into a dict
hub_spot_actor_id_response_dict = hub_spot_actor_id_response_instance.to_dict()
# create an instance of HubSpotActorIdResponse from a dict
hub_spot_actor_id_response_from_dict = HubSpotActorIdResponse.from_dict(hub_spot_actor_id_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


