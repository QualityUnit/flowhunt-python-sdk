# SlackChannelResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channel_id** | **str** |  | 
**channel_name** | **str** |  | 

## Example

```python
from flowhunt.models.slack_channel_response import SlackChannelResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SlackChannelResponse from a JSON string
slack_channel_response_instance = SlackChannelResponse.from_json(json)
# print the JSON string representation of the object
print(SlackChannelResponse.to_json())

# convert the object into a dict
slack_channel_response_dict = slack_channel_response_instance.to_dict()
# create an instance of SlackChannelResponse from a dict
slack_channel_response_from_dict = SlackChannelResponse.from_dict(slack_channel_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


