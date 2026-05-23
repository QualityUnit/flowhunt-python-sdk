# ChannelTestRequest

Request body for the channel connection test endpoint.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channel_spec** | **Dict[str, object]** | Channel specification dict as stored on the project (must include &#x60;&#x60;channel_type&#x60;&#x60; and channel-specific fields). | 

## Example

```python
from flowhunt.models.channel_test_request import ChannelTestRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ChannelTestRequest from a JSON string
channel_test_request_instance = ChannelTestRequest.from_json(json)
# print the JSON string representation of the object
print(ChannelTestRequest.to_json())

# convert the object into a dict
channel_test_request_dict = channel_test_request_instance.to_dict()
# create an instance of ChannelTestRequest from a dict
channel_test_request_from_dict = ChannelTestRequest.from_dict(channel_test_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


