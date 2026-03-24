# TrackingSourceCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_id** | **str** | The customer ID of the traffic source | [optional] 
**click_id** | **str** | The click ID of the traffic source | [optional] 
**click_id_name** | [**TrackingClickIdNames**](TrackingClickIdNames.md) | The click ID name of the traffic source | [optional] 
**utm_source** | **str** | The UTM source of the traffic source | [optional] 
**utm_medium** | **str** | The UTM medium of the traffic source | [optional] 
**utm_campaign** | **str** | The UTM campaign of the traffic source | [optional] 
**utm_term** | **str** | The UTM term of the traffic source | [optional] 
**utm_content** | **str** | The UTM content of the traffic source | [optional] 
**utm_channel** | **str** | The UTM channel of the traffic source | [optional] 
**ga** | **str** | The &#39;_ga&#39; cookie value for Google Analytics tracking | [optional] 
**url** | **str** | The URL of the page where the click was recorded | [optional] 
**links** | **List[str]** | The links of the traffic source | [optional] 
**valid_days** | **int** | The number of days the source is valid | [optional] [default to 90]
**with_address** | **bool** | The flag to indicate if the source should be created with the address | [optional] [default to True]
**event_data** | [**List[TrackingEventData]**](TrackingEventData.md) | The data of the source click event | [optional] 
**unique_id** | **str** | The unique ID of the click | [optional] 
**fp** | **str** | The browser ID | [optional] 
**session_id** | **str** | The session ID | [optional] 

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


