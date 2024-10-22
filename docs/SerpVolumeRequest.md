# SerpVolumeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**post_back_url** | **str** |  | [optional] 
**keywords** | **List[str]** |  | [optional] 
**language_code** | **str** |  | [optional] 
**location_name** | **str** |  | [optional] 
**include_adult_keywords** | **bool** |  | [optional] 
**date_from** | **date** |  | [optional] 
**date_to** | **date** |  | [optional] 

## Example

```python
from flowhunt-python-sdk.models.serp_volume_request import SerpVolumeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SerpVolumeRequest from a JSON string
serp_volume_request_instance = SerpVolumeRequest.from_json(json)
# print the JSON string representation of the object
print(SerpVolumeRequest.to_json())

# convert the object into a dict
serp_volume_request_dict = serp_volume_request_instance.to_dict()
# create an instance of SerpVolumeRequest from a dict
serp_volume_request_from_dict = SerpVolumeRequest.from_dict(serp_volume_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


