# TrackingSourceResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_id** | **str** |  | [optional] 
**link_id** | **str** |  | [optional] 
**source_type** | [**TrackingSourceTypes**](TrackingSourceTypes.md) |  | 
**click_id** | **str** |  | [optional] 
**click_id_name** | [**TrackingClickIdNames**](TrackingClickIdNames.md) |  | [optional] 
**utm_source** | **str** |  | [optional] 
**utm_medium** | **str** |  | [optional] 
**utm_campaign** | **str** |  | [optional] 
**utm_term** | **str** |  | [optional] 
**utm_content** | **str** |  | [optional] 
**ga** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**valid_until** | **datetime** |  | [optional] 
**event_data** | [**List[TrackingEventData]**](TrackingEventData.md) |  | [optional] 

## Example

```python
from flowhunt.models.tracking_source_response import TrackingSourceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TrackingSourceResponse from a JSON string
tracking_source_response_instance = TrackingSourceResponse.from_json(json)
# print the JSON string representation of the object
print(TrackingSourceResponse.to_json())

# convert the object into a dict
tracking_source_response_dict = tracking_source_response_instance.to_dict()
# create an instance of TrackingSourceResponse from a dict
tracking_source_response_from_dict = TrackingSourceResponse.from_dict(tracking_source_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


