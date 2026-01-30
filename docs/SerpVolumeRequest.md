# SerpVolumeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**post_back_url** | **str** | The post back URL where to send the response in body | [optional] 
**keywords** | **List[str]** | List of queries | 
**language_code** | **str** | Language to search | [optional] [default to 'en']
**location_name** | **str** | Location to search | [optional] 
**include_adult_keywords** | **bool** | Include adult keywords | [optional] [default to False]
**date_from** | **date** | Date from | [optional] 
**date_to** | **date** | Date to | [optional] 

## Example

```python
from flowhunt.models.serp_volume_request import SerpVolumeRequest

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


