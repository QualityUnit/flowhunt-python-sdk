# ChannelTestResponse

Result of a channel connection test.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**error** | **str** |  | [optional] 
**instructions** | **str** |  | [optional] 

## Example

```python
from flowhunt.models.channel_test_response import ChannelTestResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ChannelTestResponse from a JSON string
channel_test_response_instance = ChannelTestResponse.from_json(json)
# print the JSON string representation of the object
print(ChannelTestResponse.to_json())

# convert the object into a dict
channel_test_response_dict = channel_test_response_instance.to_dict()
# create an instance of ChannelTestResponse from a dict
channel_test_response_from_dict = ChannelTestResponse.from_dict(channel_test_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


