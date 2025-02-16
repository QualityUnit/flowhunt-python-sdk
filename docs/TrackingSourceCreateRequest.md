# TrackingSourceCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_id** | **int** |  | [optional] 
**click_id** | **str** |  | [optional] 
**click_id_name** | [**TrackingClickIdNames**](TrackingClickIdNames.md) |  | [optional] 
**utm_source** | **str** |  | [optional] 
**utm_medium** | **str** |  | [optional] 
**utm_campaign** | **str** |  | [optional] 
**utm_term** | **str** |  | [optional] 
**utm_content** | **str** |  | [optional] 
**ga** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**links** | **List[str]** | The links of the traffic source | [optional] 
**valid_days** | **int** |  | [optional] 
**with_address** | **bool** |  | [optional] 
**event_data** | [**List[TrackingEventData]**](TrackingEventData.md) |  | [optional] 
**unique_id** | **str** |  | [optional] 
**fp** | **str** |  | [optional] 

## Example

```python
from flowhunt.models.tracking_source_create_request import TrackingSourceCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TrackingSourceCreateRequest from a JSON string
tracking_source_create_request_instance = TrackingSourceCreateRequest.from_json(json)
# print the JSON string representation of the object
print(TrackingSourceCreateRequest.to_json())

# convert the object into a dict
tracking_source_create_request_dict = tracking_source_create_request_instance.to_dict()
# create an instance of TrackingSourceCreateRequest from a dict
tracking_source_create_request_from_dict = TrackingSourceCreateRequest.from_dict(tracking_source_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


